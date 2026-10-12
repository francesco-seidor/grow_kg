---
id: 03-financial-accounting-and-close/advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public
title: "Advanced Credit Management (1QM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1QM_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 1QM_AE Advanced Credit Management, S/4HANA Cloud Public Edition 2608: credit limits, ratings, requests, blocked orders, reports, jobs"
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/credit-management]
aliases: [1QM_S4CLD2608_BPD_EN_AE]
keywords: [Credit Management and Credit Agency Integration, advanced credit management, credit limit, credit rating, credit limit requests, blocked orders, credit exposure reporting, credit management jobs, business partner updates, credit data deletion]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1QM_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-755
topic: 03-financial-accounting-and-close/credit-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Advanced Credit Management (1QM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1QM_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1QM_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Credit Management and Credit Agency Integration** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Advanced Credit Management (1QM_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Advanced Credit Management (1QM_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847546)

[2 Prerequisites 4](#_Toc232847547)

[2.1 System Access 4](#_Toc232847548)

[2.2 Roles 4](#_Toc232847549)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847550)

[2.4 Business Conditions 6](#_Toc232847551)

[2.5 Preliminary Steps 7](#_Toc232847552)

[2.5.1 Assign Credit Analyst 7](#_Toc232847553)

[3 Overview Table 9](#_Toc232847554)

[4 Test Procedures 13](#_Toc232847555)

[4.1 Set a Credit Limit 13](#_Toc232847556)

[4.2 Calculation of Score, Risk Class and Credit Limit 14](#_Toc232847557)

[4.2.1 Calculate Credit Rating 14](#_Toc232847558)

[4.3 Credit Limit Request 17](#_Toc232847559)

[4.3.1 Create Credit Limit Request 17](#_Toc232847560)

[4.3.2 Approve Credit Limit Request 18](#_Toc232847561)

[4.3.3 Review Credit Limit in Business Partner 19](#_Toc232847562)

[4.4 Sales Order Processing: Sale from Stock 20](#_Toc232847563)

[4.5 Sales of Non-Stock Item with Order-Specific Procurement (Optional) 21](#_Toc232847564)

[4.6 Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional) 21](#_Toc232847565)

[4.7 Service Order Management and Monitoring (Optional) 22](#_Toc232847566)

[4.8 Service Contract Management (Optional) 22](#_Toc232847567)

[4.9 Management of Blocked Orders 23](#_Toc232847568)

[4.9.1 Review and Release or Reject a Sales Order/Service Order/Service Contract 23](#_Toc232847569)

[4.9.1.1 Review Sales Order/Service order/Service Contract 24](#_Toc232847570)

[4.9.1.2 Release Sales Order/Service Order/Service Contract 25](#_Toc232847571)

[4.9.1.3 Reject Sales Order/Service Order/Service Contract 26](#_Toc232847572)

[4.10 Reporting 27](#_Toc232847573)

[4.10.1 Credit Management Reporting - Credit Exposure 27](#_Toc232847574)

[4.10.2 Display Credit Account Data 28](#_Toc232847575)

[4.10.3 Display Credit Exposure 29](#_Toc232847576)

[4.10.4 Analyze Credit Exposure 30](#_Toc232847577)

[4.10.5 Display Credit Log 31](#_Toc232847578)

[4.10.6 Display Credit Limit Utilization 32](#_Toc232847579)

[4.10.7 Credit Limit Utilization 33](#_Toc232847580)

[4.11 Schedule Background Jobs for Credit Check on SD Documents 34](#_Toc232847581)

[4.12 Schedule Background Jobs for Business Partner Update 36](#_Toc232847582)

[4.12.1 Assign Credit Management Role to Business Partners 36](#_Toc232847583)

[4.12.2 Update Score for Business Partners 38](#_Toc232847584)

[4.12.3 Update Credit Limit for Business Partners 39](#_Toc232847585)

[4.12.4 Update Rule for Scoring and Credit Check 40](#_Toc232847586)

[4.13 Schedule Background Jobs to Send Delta of Payment Behavior Summary 42](#_Toc232847587)

[4.13.1 Send Delta of Payment Behavior Summary 42](#_Toc232847588)

[4.14 Schedule Background Jobs to Delete Credit Management Data 44](#_Toc232847589)

[4.14.1 Delete Credit Exposure 44](#_Toc232847590)

[4.14.2 Delete Payment Behavior Summary 45](#_Toc232847591)

[4.15 Schedule Background Jobs to Rebuild Credit Management Data 46](#_Toc232847592)

[4.15.1 Rebuild Credit Exposure 47](#_Toc232847593)

[4.15.2 Recreate Payment Behavior Summary 48](#_Toc232847594)

[4.15.3 Schedule Background Jobs to Reorganize Credit Segment Assignment in Journal Entries 50](#_Toc232847595)

[4.16 Import Credit Account Hierarchies 51](#_Toc232847596)

[5 Appendix 53](#_Toc232847597)

[5.1 Succeeding Processes 53](#_Toc232847598)

## Purpose

Overview

Your company's business outcomes are directly impacted by the creditworthiness and payment practices of your business partners. Effective management of receivables and credit can mitigate financial loss risks, thereby enhancing relationships with the said partners. Advanced Credit Management aids your company in recognizing possible receivables loss risks early on and in making efficient credit decisions. The Credit Controller can rapidly make credit decisions using flexible, automatic calculation formulas.

Advanced Credit Management compares the existing credit limit with your business partner's exposure. The credit limit can be verified when sales documents, service contracts, or service orders are changed. Additionally, you can execute credit limit requests. Other checks, such as the oldest open item, maximum dunning level, or last payment, can also be conducted. If a new order is blocked, authorized personnel can either release or reject it.

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
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100011 |  |  |
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
| BD9 -Sell from Stock | To run through this scope item, the materials must be available in stock.You can create stock using the Manage Stock or Transfer Stock apps. |
| BDN -Sales of Non-Stock Item with Order-Specific Procurement | Execute the Create Sales Order (Optional) step. The Item Category of the sales order must have Credit Active set. |
| BJE - Make-to-Order Production – Finished Goods Sales and Final Assembly | Execute the Create Sales Order (Optional) step. The Item Category of the sales order must have Credit Active set. |
| 3D2 - Service Order Management and Monitoring | Execute the Create Service Order (Optional) step. Service order credit management must be activated using the Activate Management in Transactions configuration step (available either via the Manage Your Solution (F1241) app or the Central Business Coniguration project experience)). |
| 3MO - Service Contract Management | Execute the Create Service Contract (Optional) step. Service order credit management must be activated using the Activate Management in Transactions configuration step (available either via the Manage Your Solution (F1241) app or the Central Business Coniguration project experience)). |

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
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33100011For the row in the Worklist pane, choose Detail (>). |  |  |
| 4 | Credit Segment | Choose the Credit Segments tab.For the following credit segment, choose Details (>):Credit Segment: 1000 Credit Segment 1000(Maintained) | The Manage Credit Accounts - Credit Segment view displays. |  |
| 5 | Edit | Choose the Edit button. |  |  |
| 6 | Manage Relationship | In the Credit Analysts section, choose Assign Credit Analyst . | The Assign Credit Analyst view displays. |  |
| 7 | Add Relationship | Select the dropdown box.In the Select Credit Analyst) dialog box, enter the Last name and First name created in the prior procedure and choose Go.The dialog box displays the search results. Select the employee from the results and OK. | The credit analyst is assigned. |  |
| 8 | Create | Choose Apply. |  |  |
| 9 | Save | Save your entries. | Changes have been saved. |  |

## Overview Table

Credit Management Process: Set credit limit, calculate credit rating, create and manage sales/service orders, review and release orders, schedule credit checks and background jobs. Use for managing credit accounts, exposure, limits, and background job scheduling in SAP.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Set a Credit Limit](#unique_9) [page ] 13 | Credit Controller | Manage Credit Accounts (F4596) | Credit limit is set. |
| Calculation of Score, Risk Class, and Credit Limit |  |  |  |
| [Calculate Credit Rating](#unique_10) [page ] 14 | Credit Controller | Manage Credit Accounts (F4596) | The credit rating is calculated. |
| Credit Limit Request |  |  |  |
| [Create Credit Limit Request](#unique_11) [page ] 17 | Internal Sales Representative | Manage Credit Limit Requests (F5602) | The Case is created. |
| [Approve Credit Limit Request](#unique_12) [page ] 18 | Credit Controller | Manage Credit Limit Requests (F5602) | The Case is approved successfully. |
| [Review Credit Limit in Business Partner](#unique_13) [page ] 19 | Credit Controller | Manage Credit Accounts (F4596) | The Credit case is updated. |
| [Sales Order Processing: Sale from Stock](#unique_14) [page ] 20 |  | Procedure described in the Sell from Stock(BD9) test script. | Sales Order for the Business Partner is created. |
| [Sales of Non-Stock Item with Order-Specific Procurement (Optional)](#unique_15) [page ] 21 |  | Execute the Create Sales Order procedure from the Sales of Non-Stock Item with Order-Specific Procurement(BDN) test script | Sales Order for the Business Partner is created. |
| [Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional)](#unique_16) [page ] 21 |  | Execute all the steps under the Quotation Processing MTO and the Create Sales Order with Ref. to Follow-On Quotation procedures described in the Make-to-Order Production – Finished Goods Sales and Final Assembly(BJE) test script. | Sales Order for the Business Partner is created. |
| [Service Order Management and Monitoring (Optional)](#unique_17) [page ] 22 |  | Execute the Create Service Order procedure from the Service Order Management and Monitoring (3D2) test script | The service order for the business partner is created. |
| [Service Contract Management (Optional)](#unique_18) [page ] 22 |  | Execute the Create Service Contract procedure from the Service Contract Management (3MO) test script | The service contract for the business partner is created. |
| Management of Blocked Orders |  |  |  |
| [Review Sales Order/Service order/Service Contract](#unique_19) [page ] 24 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The sales order/service order/service/contract is reviewed. |
| [Release Sales Order/Service Order/Service Contract](#unique_20) [page ] 25 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The sales order/service order/service/contract is released. |
| [Reject Sales Order/Service Order/Service Contract](#unique_21) [page ] 26 | Credit Controller | Manage Documented Credit Decision - New Version (F5587A) | The sales order/service order/service/contract is rejected. |
| Reporting |  |  |  |
| [Credit Management Reporting - Credit Exposure](#unique_22) [page ] 27 | Credit Controller | Credit Management Reporting - Credit Exposure (F4492) | You reviewed the credit exposure. |
| [Display Credit Account Data](#unique_23) [page ] 28 | Credit Controller | Display Credit Account Data (F4825) | The Credit Data is displayed. |
| [Display Credit Exposure](#unique_24) [page ] 29 | Credit Controller | Display Credit Exposure (F4826) | The Credit Exposure is displayed. |
| [Analyze Credit Exposure](#unique_25) [page ] 30 | Credit Controller | Analyze Credit Exposure - By Country (F2541) | Credit Exposure analytics display. |
| [Display Credit Log](#unique_26) [page ] 31 | Credit Controller | Display Credit Management Log (F2162) | The log is displayed. |
| [Display Credit Limit Utilization](#unique_27) [page ] 32 | Credit Controller | Credit Limit Utilization - Business Partner gt 80% Today (F1751) | The Credit Limit Utilization is displayed. |
| [Credit Limit Utilization](#unique_28) [page ] 33 | Credit Controller | Credit Limit Utilization - Business Partner gt 80% Today (F1751) | The Credit Limit Utilization shown. |
| [Schedule Background Jobs for Credit Check on SD Documents](#unique_29) [page ] 34 | Credit Controller | Schedule Credit Management Jobs (F3748) | Credit Checks are scheduled. |
| Schedule Background Jobs for Business Partner Update |  |  |  |
| [Assign Credit Management Role to Business Partners](#unique_30) [page ] 36 | Credit Controller | Schedule Credit Management Jobs (F3748) | Assignment of the roles to business partners is scheduled. |
| [Update Score for Business Partners](#unique_31) [page ] 38 | Credit Controller | Schedule Credit Management Jobs (F3748) | Changes to scores are scheduled. |
| [Update Credit Limit for Business Partners](#unique_32) [page ] 39 | Credit Controller | Schedule Credit Management Jobs (F3748) | Changes to credit limits are scheduled. |
| [Update Rule for Scoring and Credit Check](#unique_33) [page ] 40 | Credit Controller | Schedule Credit Management Jobs (F3748) | Changes to rules and check rules are scheduled. |
| Schedule Background Jobs to Send Delta of Payment Behavior Summary |  |  |  |
| [Send Delta of Payment Behavior Summary](#unique_34) [page ] 42 | Credit Controller | Schedule Credit Management Jobs (F3748) | You scheduled the delta job. |
| Schedule Background Jobs to Delete Credit Management Data |  |  |  |
| [Delete Credit Exposure](#unique_35) [page ] 44 | Credit Controller | Delete Credit Management Data (F4802) | You scheduled the deletion job. |
| [Delete Payment Behavior Summary](#unique_36) [page ] 45 | Credit Controller | Delete Credit Management Data (F4802) | You scheduled the deletion job. |
| Schedule Background Jobs to Rebuild Credit Management Data |  |  |  |
| [Rebuild Credit Exposure](#unique_37) [page ] 47 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the rebuild job. |
| [Recreate Payment Behavior Summary](#unique_38) [page ] 48 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the recreation job. |
| [Schedule Background Jobs to Reorganize Credit Segment Assignment in Journal Entries](#unique_39) [page ] 50 | Credit Controller | Rebuild Credit Management Data (F4234) | You scheduled the reorganization job. |
| [Import Credit Account Hierarchies](#unique_40) [page ] 51 | Credit Controller | Import Credit Account Hierarchies (F6020) | You imported the credit account hierarchies. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Set a Credit Limit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set a credit limit for the customer. The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency that is defined when the solution is activated. |

|  |
| --- |
| Note If you use the Create Credit Segment configuration step, if you want to set the Credit Segment 1000 in the FLEXIBLE_CHECK field to a value of 3 on the Main Segment and Segment levels, you must also enter a credit limit for Credit Segment 0000. |

Prerequisite

Business partner master record 33100011 is already created with credit management profile.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts (F4596) view is displayed. |  |
| 3 | Select Customer | Make the following entries and choose Go:Business Partner: 33100011For the row in the Worklist, choose Details (>). |  |  |
| 4 | Credit Profile | Choose the Scoring tab.Choose Edit.Make the following entries:Calculation Rule: Standard rule without automatic calculationRisk Class: Medium Default RiskCredit Check Rule: 01 Default - All Checks Active |  |  |
| 5 | Credit Segment | Choose the Credit Segments tab. Review or enter the following values in the Credit Segment field:Credit Segment: 1000 Credit Segment 1000(Maintained)Credit Limit: 5.00Go to the Credit Segment line and make the following entry and choose Apply:Limit Valid To: <End of Year>Note If the Valid To field is not visible, you can go into View Settings and select it to display it.Note Repeat this step to set a credit limit on Credit Segment 0000 to avoid the sales order being blocked at headquarter credit check. | The amount and validity date are set for the credit limit. |  |
| 6 | Save | Save your entries. | Changes have been saved. |  |

### Calculation of Score, Risk Class and Credit Limit

#### Calculate Credit Rating

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you Set Rules, Calculate Score, Risk Class, and Credit Limit for the customer.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency, which is defined when the solution is activated. |

|  |
| --- |
| Note If the license for Credit Agency Integration (1RY) was purchased, there is also the opportunity to import external credit information provided by an external credit agency. Please see test script 1RY for detailed information on the process. |

Prerequisite

Business partner master record 33100011 is already created with credit management profile.

You have completed your own mapping on [SAP S/4HANA Cloud for credit integration](https://help.sap.com/viewer/p/SAP_S4HANA_FINANCE_CLOUD_FOR_CREDIT_INTEGRATION)(separate license is required) for using external credit risk information and predefining risk formulas.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). | The Manage Credit Accounts view displays. |  |
| 3 | Select Customer | Enter the desired customer to process,Business Partner: 33100011and choose Enter. | The Manage Credit Accounts - Credit Profile view displays. |  |
| 4 | Edit | Choose Edit. |  |  |
| 5 | Credit Profile | Enter or review that the following information exists on the Scoring tab.Calculation Rule: SAP_ALL - All External Agencies & Int. Scoring & Limit ruleCheck Rule: 01 Default - All Checks Active (Stat. Credit Limit). |  |  |
| 6 | Calculate Credit Limit | In the External Rating tab, make the following entries and choose Create:Note To enter the values correctly, enter the rating procedure value, choose OK, then enter the rating value.Rating Procedure: 0ALLIRating: 80Rating Procedure: 0CREDSRating: 82Rating Procedure: 1ELLIRating: 78Rating Procedure: 0INT1Rating: 90 | The credit score values, which are delivered from the respective credit agencies in scope, can be mapped to a master scale on the SAP S/4HANA Cloud for credit integration.Using SAP S/4HANA Cloud for credit integration, access the Configure Credit Agency Integration app and go to Credit Rating under the Maintain Mapping section.At this location you maintain your own master scale. The rating values you use should be 0 - 100 on the master scale (0 = No rating; 1 = Worst value to 100 = Best value). The predefined formulas then works with these credit score values.Restriction SAP S/4HANA Cloud for credit integration requires a separate license. Also, additional role authorization may be required for the Credit Controller role to provide access to the credit integration solution app. For more information, see the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_S4HANA_FINANCE_CLOUD_FOR_CREDIT_INTEGRATION). |  |
| 7 | Calculate External Credit Limit | To access External Credit information using Credit Agency integration, refer to the Credit Agency Integration (1RY) test script. | Credit Limit and Risk class are automatically calculated based on the 50% Internal rating and 50% External Rating. Please note that when you import multiple external ratings, the ratings are weighted equally within the 50% External Rating.Note If you do not set Internal rating in step 7, then the Credit Limit and Risk class are calculated based on 100% External Rating. |  |
| 8 | Calculate Score | Choose Calculate Score.Choose the Scoring tab. The Score is calculated based on the external ratings entered.Note If you cannot find the Calculate Score button, choose Save, then return to the view. The Calculate Score button should then be visible. |  |  |
| 9 | Save | Save your entries. | Changes have been saved notification displays. |  |

### Credit Limit Request

#### Create Credit Limit Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The credit controller requests a new credit limit for the business partner. In this activity, you create the Credit Limit Request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Limit Requests (F5602). | The Manage Credit Limit Requests view displays. |  |
| 3 | Create Credit Limit Request | Choose Create. | The New Object view is displayed. |  |
| 4 | Create Credit Limit Request | Make the following entries and choose Create:Business Partner: 33100011Credit Segment: 1000 | The credit limit request you created is displayed. |  |
| 4 | Enter Criteria | To modify the credit limit request, choose Edit.Make the following entries and choose Save:Status: NewReason: 01 - Credit Limit for New CustomerProcessor: Credit Controller User IDRequested Credit Limit: 5Credit Limit Validity Date: for example, <End of Year> | A new case is created. |  |
| 5 | Exit | Choose Exit to return to the Home view. |  |  |

#### Approve Credit Limit Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you approve the credit limit request created in the previous procedure.

Prerequisite

Credit Limit Request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Limit Requests (F5602). | The Credit Limit Requests view displays. |  |
| 3 | Execute Credit Limit Request Search | Make the following entries and choose Go :Business Partner: 33100011Credit Segment: 1000Choose Create. | A list of Credit Limit Requests displays |  |
| 4 | Select Case | Select the row of the credit limit request you created in the previous step. |  |  |
| 5 | Change to Edit | Choose Edit. | The view changes to allow editing. |  |
| 6 | Process Credit Limit | Enter the following data:Status: In Processand choose the Save icon above the Header Data. | In process status is saved. |  |
| 7 | Process Credit Limit | Make the following entries and choose Save (above the Header Data area):Status: In Approval | The status is saved. |  |
| 8 | Approve Credit Limit | Enter the following data:Approved : 5Status : Approvedand choose the Save icon above the Header Data. | The credit limit request is approved. The new credit limit is updated in the business partner master data. |  |
| 9 | Back | Choose Back to return to the Home view. |  |  |

#### Review Credit Limit in Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the credit limit for a business partner.

|  |
| --- |
| Note The credit limit currency in all company codes is set to use the group currency, which was defined when the solution is activated. |

Prerequisite

You created a credit limit request. The approval of the request is complete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Credit Accounts (F4596). |  |  |
| 3 | Enter Business Partner | Make the following entry and choose Go:Business Partner: 33100011 |  |  |
| 4 | Select Business Partner | In the Credit Account Data list, for the business partner row you want to work with, choose Details (>). |  |  |
| 5 | Credit Limit | Choose the Credit Segments tab.Review the following values:Credit Limit: 5Valid To: <End of Year> | Amount and validity date for credit limit is reviewed. |  |
| 6 | Exit | Choose Back to return to the Home view. |  |  |

### Sales Order Processing: Sale from Stock

Context

This scope item describes the entire process sequence for a standard sales process (sale from stock) with a customer.

To test credit management, execute the Create Sales Order procedure, described in the Sell from Stock (BD9) test script. Only the Create Sales Order procedure is required, other procedures in that scope item are optional.

Prerequisites

Sales order with customer 33100011 must be created.

Procedure

Complete all activities regarding the creation of a sales order using the master data from the Sell from Stock (BD9) test script.

### Sales of Non-Stock Item with Order-Specific Procurement (Optional)

Context

In this activity, a customer orders a material that is currently not in stock. The material is procured from an external supplier.

In order to test credit management, execute the Create Sales Order procedure from the Sales of Non-Stock Item with Order-Specific Procurement (BDN) test script. Any additional procedures from that test script are optional.

|  |
| --- |
| Note This step should only be executed if Enterprise Management Cloud is active in your system. |

Prerequisites

Sales order with customer 33100011 must be created. The Item Category of the sales order must have Credit Active set.

Procedure

Complete all activities regarding the creation of a sales order using the master data from the Sales of Non-Stock Item with Order-Specific Procurement (BDN) test script.

### Make-to-Order Production – Finished Goods Sales and Final Assembly (Optional)

Context

This activity describes the entire process for a standard Make-to-Order (MTO) sales process with a customer.

In order to test credit management, execute all the steps under the Quotation Processing MTO and the Create Sales Order with Ref. to Follow-On Quotation procedures described in the Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script. Completing the remainder of procedures for that test script is optional.

|  |
| --- |
| Note These procedures can be executed only if you have a license for SAP S/4HANA Enterprise Management Cloud. |

Prerequisites

Sales order with customer 33100011 must be created. The Item Category of the sales order must have Credit Active set.

Procedure

Complete all activities regarding the creation of a sales order using the master data from the Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE) test script.

### Service Order Management and Monitoring (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The Service Order Management and Monitoring (3D2) scope item describes the entire process sequence for a standard service order process with a customer.

To test credit management, execute the Create Service Order procedure only, described in the Service Order Management and Monitoring (3D2) test script.

|  |
| --- |
| Note Only execute this step if Enterprise Management Cloud is active in your system. |

Prerequisites

A service order with customer 10100011 must be created.

Service order credit management must be activated using the Activate Management in Transactions configuration step (available either via the Manage Your Solution (F1241) app or the Central Business Coniguration project experience)).

Procedure

Complete all activities regarding the creation of a service order using the master data from the Service Order Management and Monitoring (3D2) test script.

### Service Contract Management (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The Service Contract Management (3MO) scope item describes the entire process sequence for a standard service order process with a customer.

To test credit management, execute the Create Service Contract procedure only, described in the Service Contract Management (3MO) test script.

|  |
| --- |
| Note Only execute this step if Enterprise Management Cloud is active in your system. |

Prerequisites

A service order with customer 10100011 must be created.

Service order credit management must be activated using the Activate Credit Management in Transactions configuration step (available either via the Manage Your Solution (F1241) app or the Central Business Coniguration project experience)).

Procedure

Complete all activities regarding the creation of a service order using the master data from the Service Contract Management (3MO) test script.

### Management of Blocked Orders

#### Review and Release or Reject a Sales Order/Service Order/Service Contract

Context

The sales order/service order/service contract failed the credit check. In following procedures, you review blocked sales orders/service orders/service contracts and resolve any credit issues.

Prerequisites

Sales orders/service orders/service contracts exceeding the Credit Limit settings are blocked due to credit check block.

Credit case has been assign to a Credit Analyst or Person Responsible.

##### Review Sales Order/Service order/Service Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order/service order/service contract failed the credit check. In this activity, you review blocked sales orders/service orders/service contracts.

Prerequisites

Sales orders/service orders/service contracts exceeding the Credit Limit settings are blocked, due to credit check block.

Documented credit decision has been assigned to a Credit Analyst or Person Responsible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. | The Document view is displayed. |  |
| 5 | Enable Editing | Choose Edit. |  |  |
| 6 | Update | Update Header Data fields to your requirements:Credit Analyst: <Your user with HR Master Record created> | The DCD data is updated. |  |
| 7 | Save | Choose Save. | The changes are saved. |  |
| 8 | Set In Process | Choose Set To In Process | Status changed to In Process. |  |

##### Release Sales Order/Service Order/Service Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order/service order/service contract failed the credit check. In this activity, you release sales orders/service orders/service contracts.

Prerequisites

Sales orders/service orders/service contracts exceeding the Credit Limit settings are blocked due to credit check block.

Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Searchicontrol>Continue</uicontrol>.</p></note> | Make the following entries and choose Go:Business Partner: <your business partner>Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select | Select the row of the documented credit decision you generated in the previous step. |  |  |
| 5 | Release | Choose Release. On the Release dialog box, enter an approval note and choose Release | The log displays. Under the Classification and Changes facet, the Last Action is Release. |  |

##### Reject Sales Order/Service Order/Service Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order/service order/service contract failed the credit check. In this activity, you reject sales orders/service orders/service contracts.

Prerequisites

Sales orders/service orders/service contracts exceeding the Credit Limit settings are blocked due to credit check block.

Documented credit decision has been assigned to a Credit Analyst.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Documented Credit Decision - New Version (F5587A). | The Manage Documented Credit Decision (New Version) view displays. |  |
| 3 | Select Documented Credit Decision - Search | Make the following entries and choose Go:Business Partner: 33100005Credit Segment: 1000 | A list of documented credit decisions is displayed. |  |
| 4 | Select Case | Select the row of the documented credit decision you generated in the previous step. Choose Details (>). | The Document with Credit Block view displays. |  |
| 5 | Reject | Choose Reject. | The Reject dialog box displays. |  |
| 6 | Select Rejection Reason | Make the following entry and choose Reject:Rejection Reason: for example, Rejected by ApproverRejection Note: <any note> | The sales order/service order/service contract is rejected and the DCD Status changes to Closed and the Notes are updated with the note of type Rejection Reason. |  |

### Reporting

#### Credit Management Reporting - Credit Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this analytic activity, you review the Credit Management Reporting and monitor Customer Credit in respective tabs, for example:

- Credit Limit Utilization
- Credit Exposure
- Credit Limit Validity
- Credit Limit Review
- Accounts in Focus
- Accounts with Tasks
- Open Limit Requests
- Closed Limit Requests
- Blocked Sales Documents
- Blocked Sales Orders

At the left side of each tab, you may select dimensions and filters according to your needs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Credit Management Reporting - Credit Exposure (F4492). | The Credit Management Reporting view displays the respective tabs for you to monitor the customer credit. |  |
| 3 | Respective Review in Credit Management Reporting | Choose the respective tab. | The system displays the respective tab. |  |

#### Display Credit Account Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the credit data by business partner is generated.

Prerequisite

A business partner has been created and credit management profile has been maintained.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Account Data (F4825). | The Display Credit Account Data view displays. |  |
| 3 | Execute Search | Make the following entries and choose Go:Business Partner: 33100011 |  |  |
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

In this activity, the Credit Exposure by a business partner is generated.

Prerequisite

A business partner has been created and credit management profile has been maintained.

Sales orders/service orders/service contracts have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Exposure (F4826). | The Display Credit Exposure view displays. |  |
| 3 | Execute Search | Make the following entries and choose Go:Business Partner: 33100011 | A list of credit exposure by business partner is displayed. |  |
| 4 | Business Partner | For the Business Partner, choose the arrow button at the right of the row. |  |  |
| 4 | Display Data in Different Formats | Review the credit exposure items. You can choose the arrow button at the right of a row to view details. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Analyze Credit Exposure - By Country (F2541). |  |  |
| 3 | Navigation | Use the filters at the top of the view to analyze credit exposure. The required filters are:Critical UtilizationExchange Rate TypeDisplay CurrencyRead FI Line ItemsAdditional filters can be applied according to your requirements.Use the dropdown menu to view credit exposure:By Risk ClassBy Risk Class (table)By Business PartnerBy Business Partner (table)By Credit SegmentBy Credit Segment (table)By CountryBy Country (table) | Different views display. |  |

#### Display Credit Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Credit Application Logs are displayed.

Prerequisite

A business partner has been created and credit management profile has been maintained.

Sales orders/service orders/service contracts have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Display Credit Management Log (F2162). | The Application Logs view displays. |  |
| 3 | Search Criteria | Enter the following:Severity: select all options availableDate From To: |  |  |
| 4 | Execute Search | Choose Go. | A list of Application Logs are displayed. |  |
| 5 | Select Log | Choose any log to display details. | Log details are displayed with results of credit checks. |  |

#### Display Credit Limit Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Credit Limit Utilization by business partner is generated.

Prerequisite

A business partner has been created and credit management profile has been maintained.

Sales orders/service orders/service contracts have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. | . |  |
| 2 | Access the SAP Fiori App | Open Credit Limit Utilization - Business Partner gt 80% Today (F1751) | SAP Credit Management: Credit Exposure List view displays. |  |
| 3 | Execute Search | Choose Execute. | A list of credit limit utilization by business partner is displayed. |  |
| 4 | Display Data in Different Formats | Use the icons at the top of the view, and select a row or a column to display data in other formats. | Business partner details are displayed, sorted, totals and subtotals can be created. |  |

#### Credit Limit Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Key Performance Indicator (KPI) Credit Limit Utilization, that is, the utilization of a business partner's credit limit.

Prerequisite

Sales orders/service orders/service contracts have been created, credit check has been executed and cases have been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Credit Limit Utilization - Business Partner gt 80% Today (F1751). |  |  |
| 3 | Navigation | To change the view, choose the drill down button or other buttons in the report.You can view credit limit utilization and credit exposure according to business partner, credit segment, country, and region.You can drill down by the top 10 business partners with the highest credit limit utilization and by the top 10 business partners with the highest credit exposure. |  |  |

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

In this activity, you schedule background jobs for business partner update.

#### Assign Credit Management Role to Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the assignment of the credit management role to the business partners.

Prerequisites

The business partner exists without the UKM000 role.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Template Selection section:Job Template: Assign Credit Management Role to Business PartnersJob Name: Assign Credit Management Role to Business PartnersMake the following entries and choose Step 3:Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK.Make the following entries and choose Schedule:Parameters section:Business Partner: enter the Business Partner needed to create the UKM000 roleNote To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Create Credit Profile: DeselectedNote If you need to create a credit profile, ensure that you assigned the default rules in the Define Checking Rules and Create Rule for Scoring and Credit Limit Calculationconfiguration steps.Test Run: DeselectedUpdate Run: Selected | The job is scheduled. |  |
| 5 | Check Result | Check that the business partner for the UKM000 role is created. For more information on how to do the check, see [Set a Credit Limit](#unique_9) [page ] 13. |  |  |

#### Update Score for Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the update of the scores for business partners.

Prerequisites

A business partner exists where the calculated score is different than the score in the business partner master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Template Selection section:Job Template: Update Score for Business PartnersJob Name: Update Score for Business PartnersMake the following entries and choose Step 3Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK.Make the following entries and choose ScheduleParameters section:Rules: enter the Rules needed for the changeBusiness Partner: enter the Business Partner needed for the changeNote To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Test Run: DeselectedUpdate Run: Selected | The job is scheduled. |  |
| 5 | Check Result | Check that the business partner for the score is changed. For more information on how to do the check, see [Set a Credit Limit](#unique_9) [page ] 13. |  |  |

#### Update Credit Limit for Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the update of credit limits for business partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Credit Management Jobs (F3748). |  |  |
| 3 | Create Job | Choose Create. | The New Job view displays. |  |
| 4 | Create Job | Make the following entries and choose Step 2:Template Selection section:Job Template: Update Credit Limit for Business PartnersJob Name: Update Credit Limit for Business PartnersMake the following entries and choose Step 3:Scheduling Options section:Start Immediately: SelectedRecurrence Pattern: Single RunNote To schedule a recurrence pattern, choose the Define Recurrence Pattern button and in the Scheduling Information dialog box, enter your parameters and choose OK.Make the following entries and choose Schedule:Parameters section:Business Partner: enter the Business Partner needed for the changeNote To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Test Run: DeselectedUpdate Run: Selected | The job is scheduled. |  |
| 5 | Check Result | Check that the business partner for the credit limit is changed. For more information on how to do the check, see [Set a Credit Limit](#unique_9) [page ] 13. |  |  |

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

|  |
| --- |
| Caution Deletion and rebuilding of credit management data is not part of the regular or daily business. This should be taken into consideration if the respective data are wrong. We strongly recommend that you check SAP Notes before you delete and rebuild credit management data. |

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
| 2 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 3 | Access the SAP Fiori App | Open Delete Credit Management Data (F4802). |  |  |
| 4 | Create Job | Choose Create. | The New Job view displays. |  |
| 5 | Add General Information | In the Template Selection section, make the following entries and choose Step 2:Job Template: Delete Payment Behavior SummaryJob Name: Delete Payment Behavior Summary |  |  |
| 6 | Scheduling Options | In the Scheduling Options section, make the following entries and choose Step 3:Start Immediately: SelectedTo schedule a recurrence pattern, choose the Define Recurrence Pattern button. In the Scheduling Information dialog box, enter Recurrence Pattern: Single Run and choose OK. |  |  |
| 7 | Parameter Section | In the Parameters section, make the following entries and choose Schedule:Business Partner: <enter the Business Partner needed for the deletion>To make the change on multiple Business Partners, choose the Drop Down button and in the Select: Business Partner (List displays max. 500 hits. If available, use the filter to see all values.)dialog box, enter your parameters and choose OK.Credit Segment: <enter the Credit Segment needed for the deletion>Test Run: leave blankDisplay Details: Selected | The job is scheduled. |  |

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

### Import Credit Account Hierarchies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you import credit account hierarchies. You can also use the app to delete existing credit account hierarchies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Credit Controller. |  |  |
| 2 | Access the SAP Fiori App | Open Import Credit Account Hierarchies (F6020). |  |  |
| 3 | Download Template | Choose Download Template. | The template is downloaded into your local download folder. |  |
| 4 | Modify Import file | Copy the downloaded template to your local folder and rename it to a suitable name.Add the items of the Business Partner Number of Higher-Level Account, Business Partner Number of Lower-Level Account and the relevant Action (I=Insert, D=Delete) into the file. | You created the Import Credit Account Hierarchies file. |  |
| 5 | Upload Import file | In the Import Credit Account Hierarchies view, choose Browse. |  |  |
| 6 | File Name | Enter your file name and the folder and choose Open. | The file is uploaded. The system displays a new line in the Credit Account Hierarchies area. |  |
| 7 | Import Credit Account Hierarchies | Select the newly added line and choose Import. | The file is imported into the credit accounts. You may check the results as mentioned in the Display Credit Accounts Section, in the Partner Hierarchy view. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Process | Business Condition |
| --- | --- |
| BD9 - Sell from Stock (optional) | Entire process sequence for a standard sales process (sale from stock) with a customer.Using the master data from this document, complete the following activities described in the test script:Process Sales Order: Sale from Stock |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement (optional) | Customer orders a material that is currently not in stock. The material is procured from an external supplier.Using the master data from this document, complete the following activities described in the test script:Sales of Nonstock Item with Order-specific Procurement |
| BKK - Sales Order Fulfillment Monitoring and Operations (optional) | Collection of periodic activities such as day ending activities or legal requirements like Intrastat and Extrastat reporting.Using the master data from this document, complete the following activities described in the test script:Sales: Period End Closing Operations (BKK) (Review Blocked Sales Orders section) |
| 3D2 - Service Order Management and Monitoring | Entire process sequence for a standard service order process with a customer.Using the master data from this document, complete the following activities described in the test script: Service Order Management and Monitoring |
| 3MO - Service Contract Management | Entire process sequence for a standard service contract process with a customer.Using the master data from this document, complete the following activities described in the test script: Service Contract Management |

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
> Flagged while digesting this document, not verified: Test data is inconsistent within the script: credit master data is set up only for customer 33100011 (company code 3310), but the service order and service contract prerequisites name customer 10100011, and the Reject step searches business partner 33100005, neither of which is created in this script.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-basic-credit-management-bd6-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[03-financial-accounting-and-close/test-script-credit-agency-integration-1ry-759]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1QM_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 83,939 chars in the whole document
