---
id: 01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh
title: "Test Script: Continuous Control Monitoring with SAP Process Control (2OH) (2OH_S4CLD2608_BPD_EN_XX)"
description: "S/4HANA Cloud Public Edition test script, scope item 2OH: SAP Process Control data sources, business rules and ad-hoc queries for continuous control monitoring."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/governance-risk-and-control-monitoring, topic/central-financial-compliance-management]
aliases: [2OH_S4CLD2608_BPD_EN_XX]
keywords: ["Risk, Control and Privacy Monitoring (SAP Risk and…", continuous control monitoring, sap process control, scope item testing, monitoring data sources, business rules, ad-hoc queries, configuration data change, transactional data values, multiple deficiency values]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OH_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-843
topic: 01-solution-foundation-and-platform/governance-risk-and-control-monitoring
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Continuous Control Monitoring with SAP Process Control (2OH) (2OH_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OH_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Risk, Control and Privacy Monitoring (SAP Risk and Assurance Management)** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Continuous Control Monitoring with SAP Process Control (2OH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232842927)

[2 Prerequisites 4](#_Toc232842928)

[2.1 Additional Manual Configuration 4](#_Toc232842929)

[2.2 System Access 4](#_Toc232842930)

[2.3 Roles 4](#_Toc232842931)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232842932)

[2.5 Business Conditions 5](#_Toc232842933)

[2.6 Preliminary Steps 6](#_Toc232842934)

[3 Overview Table 7](#_Toc232842935)

[4 Test Procedures 9](#_Toc232842936)

[4.1 Monitoring Configuration Data Change 9](#_Toc232842937)

[4.1.1 Set Up Data Sources for Monitoring Configuration Data Change 9](#_Toc232842938)

[4.1.2 Set Up Business Rules 10](#_Toc232842939)

[4.1.3 Perform Configuration Change 12](#_Toc232842940)

[4.1.4 Perform Ad-hoc Query 14](#_Toc232842941)

[4.2 Monitoring Transactional Data Values 15](#_Toc232842942)

[4.2.1 Set Up Data Sources for Monitoring Transactional Data Value 15](#_Toc232842943)

[4.2.2 Set Up Business Rules 16](#_Toc232842944)

[4.2.3 Perform Ad-hoc Query for Transactional Data Value Check 18](#_Toc232842945)

[4.2.4 Set Up Data Sources for Monitoring with Multiple Deficiency Values 19](#_Toc232842946)

[4.2.5 Set Up Business Rules for Multiple Deficiency Values 21](#_Toc232842947)

[4.2.6 Perform Ad-hoc Query for Multiple Deficiency Values 23](#_Toc232842948)

[4.2.7 Set Up Data Sources for Monitoring CDS Views via OData Services 23](#_Toc232842949)

[4.2.8 Set Up Business Rules for CDS Views 25](#_Toc232842950)

[4.2.9 Perform Ad-hoc Query for Value Check for CDS Views 27](#_Toc232842951)

## Purpose

Overview

With this scope item, SAP Process Control customers can include SAP S/4HANA Cloud Public Edition processes in continuous control monitoring.

Embedded compliance allows data to be retrieved from SAP S/4HANA Cloud Public Edition and analyzed in SAP Process Control.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6d2046fbd5a52674b7cd8e8373763c30)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition system | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Process Control System | Your system administrator provides you the logon information to access the system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information on Roles in SAP Process Control, please refer to Security Guide in product page for [SAP Process Control](https://help.sap.com/docs/SAP_PROCESS_CONTROL?locale=en-US).

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the tester in S/4HANA Cloud. |
| Cross Continuous Monitoring Data Source Specialist | SAP_GRC_SPC_CRS_CM_DS_SPEC | N/A | N/A | Please ask your system administrator to assign to the tester in SAP Process Control. |
| Cross Continuous Monitoring Business Rule Specialist | SAP_GRC_SPC_CRS_CM_BR_SPEC | N/A | N/A | Please ask your system administrator to assign to the tester in SAP Process Control. |

### Master Data, Organizational Data, and Other Data

This scope item does not make use of Master Data, Organizational Data or Other Data.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BD6 - Basic Credit Management | Make sure BD6 is activated before performing test procedures described in this test script, because customizing enabling Credit Limit contained in BD6 is required for successful execution of this test script. |
| 1GO - Cash Journal | Make sure 1GO is activated before performing test procedures described in this test script, because configurations activated by 1GO will be used as examples during the test procedures. |

### Preliminary Steps

This scope item does not require preliminary steps.

## Overview Table

This scope item consists of several choose the appropriate entity: process steps, reports, items provided in the table below.

| Process Step | Business Role | System | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| [Set Up Data Sources for Monitoring Configuration Data Change](#unique_10) [page ] 9 | Cross Continuous Monitoring Data Source Specialist | On-premise SAP Process Control system | /nnwbc | Data source for monitoring configuration data change is created. |
| [Set Up Business Rules](#unique_11) [page ] 10 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Business rule for monitoring configuration data change is created. |
| [Perform Configuration Change](#unique_12) [page ] 12 | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:BPC ExpertSAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration | SAP S/4HANA Cloud Public Edition | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Manage Your SolutionSAP Central Business Configuration:Configuration Activities | Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configuration change has been performed using SSCUI.Configuration change has been performed using SAP Central Business Configuration |
| [Perform Ad-hoc Query](#unique_13) [page ] 14 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Configuration change is displayed in the ad-hoc query. |
| [Set Up Data Sources for Monitoring Transactional Data Value](#unique_14) [page ] 15 | Cross Continuous Monitoring Data Source Specialist | On-premise SAP Process Control system | /nnwbc | Data source for monitoring transactional data value is created. |
| [Set Up Business Rules](#unique_15) [page ] 16 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Business rule for monitoring transactional data value is created. |
| [Perform Ad-hoc Query for Transactional Data Value Check](#unique_16) [page ] 18 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Transactional value that agrees with the business rule is displayed in the ad-hoc query. |
| [Set Up Data Sources for Monitoring with Multiple Deficiency Values](#unique_17) [page ] 19 | Cross Continuous Monitoring Data Source Specialist | On-premise SAP Process Control system | /nnwbc | Data source for monitoring transactional data using multiple deficiency values is set up. |
| [Set Up Business Rules for Multiple Deficiency Values](#unique_18) [page ] 21 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Business rule for monitoring transactional data value using multiple deficiency values is set up. |
| [Perform Ad-hoc Query for Multiple Deficiency Values](#unique_19) [page ] 23 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Transactional data value that agrees with the business rule is displayed in the ad-hoc query. |
| [Set Up Data Sources for Monitoring CDS Views via OData Services](#unique_20) [page ] 23 | Cross Continuous Monitoring Data Source Specialist | On-premise SAP Process Control system | /nnwbc | Data source for monitoring CDS View data exposed via OData services is set up. |
| [Set Up Business Rules for CDS Views](#unique_21) [page ] 25 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | Business rule for monitoring CDS view data exposed via OData services is set up. |
| [Perform Ad-hoc Query for Value Check for CDS Views](#unique_22) [page ] 27 | Cross Continuous Monitoring Business Rule Specialist | On-premise SAP Process Control system | /nnwbc | CDS view data value that agrees with the business rule is displayed in the ad-hoc query. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitoring Configuration Data Change

#### Set Up Data Sources for Monitoring Configuration Data Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to set up data source for monitoring customizing table of Define Amount Limit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client view for SAP PC is displayed. |  |
| 2 | Navigate to Data Sources | Switch to the tab Rule Setup, and then choose Data Sources under the Continuous Monitoring section. | The Enterprise Object view is displayed. |  |
| 3 | Create Data Source | Choose Create and in the dialog box, fill in the following details:In the General tab, enter the following data:Data Source: <For example, Define Amount Limit>Description: <For example, Data source for Define Amount Limit>Valid From: 01.01.2000Valid To: 31.12.9999Status: In ReviewIn the Object Field tab, enter the following data:Sub Scenario: ConfigurableConnection Type: S/4Main Connector: <For example: the ID of SAP S/4HANA Cloud Public Edition system>Note The Main Connector mentioned above is the one which is created following the Set-up Instruction Guide of 2OH.Choose Main Table Lookup, and in the dialog box, enter TCJ_MAX_AMOUNT in the field Table Name, and then choose Apply. Select the search result representing table TCJ_MAX_AMOUNT and then choose OK.Choose Select Additional Table Fields, and in the dialog box, choose Add All.In the Adhoc Query tab, make the following entries:Target Connector: <Use the Connector selected as Main Connector above>Choose Execute Query, and check whether the query can be performed successfully.Choose Save. |  |  |
| 4 | Update Data Source | Open the data source created in the step above.In the General tab, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Set Up Business Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to set up business rules.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP PC displays. |  |
| 2 | Navigate to Business Rules | Switch to the tab Rule Setup, and then choose Business Rules under the Continuous Monitoring section. | The Enterprise Object view displays. |  |
| 3 | Select Data Source | Choose Create and in the dialog box, fill in the following details:Data Source: <Data source created in previous test procedure>Select the returned entry after choosing Search and then choose OK.Choose Continue. | The Business Rule: Step 1 of 9 (Basic Information) displays. |  |
| 4 | Create Business Rule | In the view Business Rule: Step 1 of 9 (Basic Information), for each step, provide the following details:Step 1: Basic Information:Name: <For example, Define Amount Limit>Description: <For example, Business Rule for Define Amount Limit>Category: Change Log CheckAnalysis Type: ChangesStatus: In ReviewValid from: 01.01.2000Valid to: 31.12.9999Choose Next.Step 2: Data for Analysis:Choose Select All, and then click Next.Choose Next until Step 4: Deficiency Criteria:Choose Select/Unselect Filters, and in the dialog box choose Select Handler. In the next dialog box, choose Handler V_TCJ_MAX_AMOUNT, and then choose OK. In the Deficiency Fields section, select Cash Journal Amount Field with +/- Sign, and then choose OK.Note If using above handler does not find any data, then please re-choose a Handler with Handler Type SCU3 and proceed.Select the entry for field Cash Journal Amount Field with +/- Sign, and for the field Field Analysis Type, select Changes. For the field Currency, specify <EUR>.In the Deficiency Indicator, choose for example, Low.Choose Next until Attachment and Links, and then choose Save. |  |  |
| 5 | Update Business Rule | Open the business rule created in above steps, and in the tab Basic Information, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Perform Configuration Change

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves as a guide on how to make configuration changes.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Navigate | Choose Manage Your Solution (F1241). Navigate to Configure Your Solution. | The Manage Your Solution (F1241) displays. |  |
| 3 | Define Amount Limit | Make the following entries:Application Area: FinanceSub Application Area: Payables/Receivables/CashSearch for Define Amount Limit.Choose the returned row and choose Configure for the configuration step Define Amount Limit.Make following changes, for example:CoCd: 1010Crcy: EURValid from: 01/01/2016Amount: 20,001.00Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Define Amount Limit | Go to the Business Processes Configuration app and search for the following activity: Define Amount Limit.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Amount Limit screen displays. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | Define Amount Limit | Make following changes, for example:CoCd: 1010Crcy: EURValid from: 01/01/2016Amount: 20,001.00Choose Save. |  |  |

#### Perform Ad-hoc Query

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to perform ad-hoc query.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Perform Ad-hoc Query in on-premise SAP Process Control | Open the business rule created in [Set Up Business Rules](#unique_11) [page ] 10, and in the tab Ad-hoc Query, make the following entries:Timeframe: YearExpand the dropdown list by choosing the arrow in the Data Collection, and then choose Apply Rule.Choose Start to execute the query. | The change performed in the previous chapter should be reported in the query result. |  |

### Monitoring Transactional Data Values

#### Set Up Data Sources for Monitoring Transactional Data Value

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to set up data sources for monitoring transactional data value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to On-premise SAP Process Control | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Process Control displays. |  |
| 2 | Navigate to Data Sources | Switch to the tab Rule Setup, and then choose Data Sources under the Continuous Monitoring section. | The Enterprise Object view displays. |  |
| 3 | Create Data Source | Choose the Create button.In the General tab, make the following entries:Data Source: For example, Credit limit for sales orderDescription: For example, Data source for Credit limit for sales orderValid From: 01.01.2000Valid To: 31.12.9999Status: In ReviewIn the Object Field tab, enter the following data:Sub Scenario: ConfigurableConnection Type: S/4Main Connector: For example: the ID of SAP S/4HANA Cloud Public Edition systemNote The Main Connector mentioned above is the one which is created after following the Set-up Instruction Guide of 2OH.Choose Main Table Lookup.In the dialog box, in Table Name, enter UKMBP_CMS_SGM and choose Apply. Select the search result representing table UKMBP_CMS_SGM and then choose OK.Choose Related Table Lookup.In the dialog box, in Table Name, enter UKMCRED_SGM0C . Choose Apply and then Add All. Choose OK.In the Fields section, for both tables UKMCRED_SGM0C and UKMBP_CMS_SGM, choose Select Additional Table Fields, and in the dialog box, choose Add All.Note Make sure the fields of table UKMCRED_SGM0C are added before UKMBP_CMS_SGM.In the Ad-hoc Query tab, enter the following data:Target Connector:<Use the Connector selected as Main Connector above>Choose Execute query, and check that the query can be performed successfully.Choose Save. |  |  |
| 4 | Update Data Source | Open the data source created in the above step, and in the General tab, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Set Up Business Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to set up business conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to On-premise SAP Process Control | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP PC is displayed. |  |
| 2 | Navigate to Business Rules | Switch to the tab Rule Setup, and then choose Business Rules under the Continuous Monitoring section. | The Business Rule view is displayed. |  |
| 3 | Select Data Source | Choose Create and in the dialog box, fill in the following details:Data Source: <Data source created in previous test procedure>Select the returned entry after choosing Search and then choose OK.Choose Continue. | The Business Rule: Step 1 of 9 (Basic Information) view is displayed. |  |
| 4 | Create Business Rule | In the view Business Rule: Step 1 of 9 (Basic Information), for each step, provide the following details:Step 1: Basic Information:Name: <For example, Credit limit for sales order>Description: <For example, Business Rule for Credit limit for sales order>Category: Value CheckAnalysis Type: Monitor ValueStatus: In ReviewValid from: 01.01.2000Valid to: 31.12.9999Choose Next.Step 2: Data for Analysis:Choose Select All, and then click Next.Choose Next until Step 4: Deficiency Criteria:Choose Select/Unselect Filters, and in the dialog box choose Credit Limit. Then choose OK.Select the entry for the field Credit Limit and for the field Field Analysis Type, choose Value Check. For the field Currency, select for example, USD.In the Deficiency Value, specify for example:Deficiency Type: LowSign: Range limit includedOption: Greater than or equal toLow: <For example, 5, or other value which meets your business requirement>Choose Next until Attachment and Links, and then choose Save. |  |  |
| 5 | Update Business Rule | Open the business rule created in above steps, and in the tab Basic Information, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Perform Ad-hoc Query for Transactional Data Value Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to perform ad-hoc query for transactional data value check.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Perform Ad-hoc Query in On-premise SAP Process Control | Open the business rule created in the test above, and in the tab Ad-hoc Query, make the following entries:Timeframe: YearChoose Start to execute the query. | Business partners with credit limit larger than 5 USD should be reported in the query result. |  |

#### Set Up Data Sources for Monitoring with Multiple Deficiency Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step sets up a data source against which multiple deficiency values can be set and monitored.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to On-premise SAP Process Control | Log on a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client view for SAP Process Control displays. |  |
| 2 | Navigate to Data Sources | Switch to the Rule Setup tab. Under the Continuous Monitoring section, choose Data Sources. | The Enterprise Object window displays. |  |
| 3 | Create Data Source | Choose the Create button, and in the dialog box, enter the following details:In the General tab, enter the following data:Data Source: <For example: Legal Regulation Status Reason for Trade Compliance Documents>Description: <For example: Legal Regulation Status Reason for Trade Compliance Documents >Valid From: 01.01.2000Valid To: 31.12.9999Status: In ReviewIn Object Field tab, enter the following data:Sub Scenario: ConfigurableConnection Type: S/4Main Connector: <For example: the ID of SAP S/4HANA Cloud Public Edition system>Note The main connector mentioned above is the one which is created after following the Set-up instruction guide of 2OH. |  |  |
| 4 | Main Table and Related Table Lookups | Choose Main Table Lookup. In the following dialog box, in Table Name, enter /SAPSLL/CLDIT and then choose Apply. Select the search result representing table /SAPSLL/CLDIT then choose OK.Choose Related Table Lookup. In the following dialog box, in Table Name,enter /SAPSLL/CLDLR and select radio button Dependent Tables and then choose Apply. Choose Add All and then choose OK.In the Fields section, for both tables /SAPSLL/CLDLR and /SAPSLL/CLDIT choose Select Additional Table Fields, and in the dialog box, choose Add All.In the Adhoc Query tab, enter the following data:Target Connector: <Use the Connector selected as Main Connector above>Choose Execute query button, and check that the query can be performed successfully.Choose Save to save this data source. |  |  |
| 5 | Update Data Source | Open the data source created in the above step, and in the General tab, make the following adaptation:Status: ActiveChoose Save to save the change. |  |  |

#### Set Up Business Rules for Multiple Deficiency Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this business rule, multiple deficiency values are specified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client view for SAP PC displays. |  |
| 2 | Navigate to Business Rules | Switch to the Rule Setup tab, and then choose Business Rules under the Continuous Monitoring section. | The new window Enterprise Object displays. |  |
| 3 | Select Data Source | Choose Create and in the dialog box, enter the following details:Data Source: <Data source created in previous test procedure>Choose Search.Choose the returned entry and then choose OK.Choose Continue. | The Business Rule: Step 1 of 9 (Basic Information) view displays. |  |
| 4 | Create Business Rule | In the view Business Rule: Step 1 of 9 (Basic Information), for each step, provide the following details:Step 1: Basic Information:Name: <For example: Legal Regulation Status Reason for Trade Compliance Documents">Description: <For example: Legal Regulation Status Reason for Trade Compliance Documents>Category: Value CheckAnalysis Type: Monitor ValueStatus: In ReviewValid from: 01.01.2000Valid to: 31.12.9999Choose Next.Step 2: Data for Analysis:Choose Select All, and then choose Next.Choose Next until Step 4: Deficiency Criteria:Choose Select/Unselect Deficiency, and select the entry for field Legal Regulation Status Reason, and for the field Field Analysis Type, select Value Check.In the Deficiency Value, specify for example:Deficiency Type: LowSign: Range limit includedOption: EqualsLow: <For example, K>Optionally, it is also possible to create multiple deficiency values, for example, choose Add Line button in the row representing above defined Low Deficiency, then specify:Deficiency Type: LowSign: Range limit includedOption: EqualsLow: <For example, M>Choose Next until Step 6: Output Format:Choose Select/Unselect Output Fields, and select fields Document Category, Document Number, Legal Regulation, Legal Regulation Status. Then choose OK.Choose Next until Attachment and Links, then choose Save.Choose Save. |  |  |
| 5 | Update Business Rule | Open the business rule created in above steps, and in the Basic Information tab, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Perform Ad-hoc Query for Multiple Deficiency Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Ad-hoc query is performed to report discovered deficiencies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Perform Ad-hoc Query in on-premise SAP Process Control | Open the business rule created in [Set Up Business Rules for Multiple Deficiency Values](#unique_18) [page ] 21, and in the Ad-hoc Query tab, do the following:Timeframe: YearExpand the dropdown list by choosing the arrow in the Data Collection, and then choose Apply Rule.Choose Start to execute the query. | Trade Compliance Documents with corresponding Legal Regulation Status Reason should be reported in the query result. |  |

#### Set Up Data Sources for Monitoring CDS Views via OData Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to set up sources for monitoring CDS views via OData Services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to On-premise SAP Process Control | Log on to a supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP Process Control is displayed. |  |
| 2 | Navigate to Data Sources | Switch to the tab Rule Setup, and then choose Data Sources under the Continuous Monitoring section. | The Business Rule view displays. |  |
| 3 | Create Data Source | Choose Create and in the dialog box, fill in the following details:In the General tab, enter the following data:Data Source: <for example, Overall blocked status for sales order>Description: <for example, Data source for overall blocked status for sales order>Valid From: 01.01.2000Valid To: 31.12.9999Status: In ReviewIn the Object Field tab, enter the following data:Sub Scenario: External PartnerConnection Type: S/4 ODataMain Connector: for example, <the ID of G type RFC destination created in Set-up Instruction Guide>Choose Query Lookup, and in the dialog box, click the value help button for the field of OData Service Name, and then in the dialog box, choose Go. Select the entry representing the OData service created in the Set-up instruction guide, for example: /sap/opu/odata/sap/Z_SALES_DOCUMENT_CDS.Then choose Apply, and select the returned Service Entity, and choose OK.In the Fields section, click Select Fields, and in the dialog box, select the desired fields by choosing corresponding checkboxes, and then click OK.Note The structure of underlying CDS Views with associations can also be reflected in this hierarchical graphic view.In the Adhoc Query tab, enter the following data:Target Connector: <Use the Connector selected as Main Connector above>Note If OData Services with Input Parameters are used, one more step is required after step 2: Data for Analysis to fill in corresponding Input Parameters.Choose Execute query, and check that the query can be performed successfully.Choose Save. |  |  |
| 4 | Update Data Source | Open the data source created in the above step, and in the General tab, make the following adaptation:Status: ActiveChoose Save. |  |  |

#### Set Up Business Rules for CDS Views

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to set up business rules for CDS views.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to On-premise SAP Process Control | Log on to Internet Explorer or another supported browser with the following URL:http(s)://<ServerName>:<Port Number>/nwbc | The NetWeaver Business Client screen for SAP PC is displayed. |  |
| 2 | Navigate to Business Rules | Switch to the tab Rule Setup, and then choose Business Rules under the Continuous Monitoring section. | The Business Rule view displays. |  |
| 3 | Select Data Source | Choose Create and in the dialog box, fill in the following details:Data Source: <Data source created in previous test procedure>Choose Search, and select the returned entry and then choose OK.Choose Continue. | The Business Rule: Step 1 of 9 (Basic Information) view displays. |  |
| 4 | Create Business Rule | In the view Business Rule: Step 1 of 9 (Basic Information), for each step, provide the following details:Step 1: Basic Information:Name: <For example,Overall blocked status for sales order>Description: <For example,Overall blocked status for sales order>Category: Value CheckAnalysis Type: Monitor ValueStatus: In ReviewValid from: 01.01.2000Valid to: 31.12.9999Choose Next.Step 2: Data for Analysis:Choose Select All, and then click Next.Note If OData Services with Input Parameters are used, one more step is required after step 2: Data for Analysis to fill in corresponding Input Parameters.Choose Next until Step 5: Deficiency Criteria:Choose Select/Unselect Deficiency, and in the dialog box choose the field Overall Block Status. Then choose OK.Select the entry for the field Overall Block Status and for the field Field Analysis Type, choose Value Check.In the Deficiency Value, specify for example:Deficiency Type: LowSource: With Fixed ValueSign: Range limit includedOption: EqualsLow: <For example, C, or other value which meets your business requirement>Choose Next until Attachment and Links, and then choose Save.Choose Save to save the change. |  |  |
| 5 | Update Business Rule | Open the business rule created in above steps, and in the tab Basic Information, make the following adaptation:Status: ActiveChoose Save to save the change. |  |  |

#### Perform Ad-hoc Query for Value Check for CDS Views

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The procedure below serves a guide on how to perform Ad-hoc query for value check for CDS Views.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Perform Ad-hoc Query in On-premise SAP Process Control | Open the business rule created in [Set Up Business Rules for CDS Views](#unique_21) [page ] 25, and in the Ad-hoc Query tab, choose Data Collection, then perform the following operation:Timeframe: YearYear: <Current Year>Choose Star to execute the query.Then select Apply Rule, and click Start to execute the query. | Blocked sales orders is listed in the report and go to the system to perform corresponding subsequent processes to release the blocked sales orders. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-control-monitoring-with-sap-risk-and-assurance-management]]
- related-to :: [[01-solution-foundation-and-platform/test-script-key-risk-indicator-monitoring-with-sap-risk-management-2u2]]
- related-to :: [[01-solution-foundation-and-platform/test-script-privacy-risk-detection-with-sap-risk-and-assurance-managem]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OH_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 40,888 chars in the whole document
