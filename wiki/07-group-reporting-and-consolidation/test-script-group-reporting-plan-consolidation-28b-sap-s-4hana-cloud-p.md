---
id: 07-group-reporting-and-consolidation/test-script-group-reporting-plan-consolidation-28b-sap-s-4hana-cloud-p
title: "Test Script: Group Reporting – Plan Consolidation (28B), SAP S/4HANA Cloud Public Edition (28B_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 28B Group Reporting Plan Consolidation: ZA1/ZB2/ZF2 versions, uploads, monitors, SAC planning."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/plan-consolidation]
aliases: [28B_S4CLD2608_BPD_EN_XX]
keywords: [Plan Consolidation, group reporting, consolidation versions, budget planning, forecast planning, exchange rates, copy transaction data, flexible upload, data monitor, consolidation monitor]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/28B_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-807
topic: 07-group-reporting-and-consolidation/plan-consolidation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Group Reporting – Plan Consolidation (28B), SAP S/4HANA Cloud Public Edition (28B_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/28B_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Plan Consolidation** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Group Reporting – Plan Consolidation (28B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846737)

[2 Prerequisites 4](#_Toc232846738)

[2.1 System Access 4](#_Toc232846739)

[2.2 Roles 4](#_Toc232846740)

[2.3 Business Conditions 5](#_Toc232846741)

[2.4 Version Settings 6](#_Toc232846742)

[3 Overview Table 14](#_Toc232846743)

[4 Test Procedures 16](#_Toc232846744)

[4.1 Actuals @ Budget Rate CT 16](#_Toc232846745)

[4.1.1 Maintain Exchange Rates 16](#_Toc232846746)

[4.1.2 Set Global Parameters and Open Period 17](#_Toc232846747)

[4.1.3 Data Preparation by Copying Totals Records 12/2025 from A10 to ZA1 18](#_Toc232846748)

[4.1.4 Data and Consolidation Monitor in 2025 20](#_Toc232846749)

[4.2 ZB2 Budget 2026 (12+1+1+1) 22](#_Toc232846750)

[4.2.1 Set Global Parameters and Open Period 22](#_Toc232846751)

[4.2.2 Data Preparation 23](#_Toc232846752)

[4.2.2.1 Copy Totals Records 00-03/2026 from A10 to ZB2 23](#_Toc232846753)

[4.2.2.2 Flexible Upload of Subsequent Year and Period Reported Financial Data (04-12/2026, 2027-2029) 26](#_Toc232846754)

[4.2.3 Data and Consolidation Monitor in 2026 - 2029 27](#_Toc232846755)

[4.3 ZF2 Forecast (2+10) 31](#_Toc232846756)

[4.3.1 Set Global Parameters and Open Period 31](#_Toc232846757)

[4.3.2 Data Preparation 32](#_Toc232846758)

[4.3.2.1 Copy Totals Records Periods 00-02/2026 from A10 to ZF2 32](#_Toc232846759)

[4.3.2.2 Flexible Upload of Financial Data 03-12/2026 in ZF2 34](#_Toc232846760)

[4.3.3 Data and Consolidation Monitor in 03-12/2026 35](#_Toc232846761)

[4.4 SAC – ZB4 (2028) Integration Planning Scenario (Optional) 38](#_Toc232846762)

[4.4.1 Export SAC Data to SAP S/4HANA Cloud Public Edition Using the SAC Export to SAP S/4HANA Feature 38](#_Toc232846763)

[4.4.2 **Pull Plan Data from SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition** 44](#_Toc232846764)

## Purpose

Overview

With this scope item, you can either collect the plan data from a file using the flexible upload feature of SAP S/4HANA Cloud Public Edition or generate the plan data from the previous year's actual data. The user can then run a full consolidation process including currency translation, intercompany, and investments eliminations and reporting. The application includes several versions to enable reporting (Actual versus Plan, Plan, and Forecast).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Note Please finish the Preliminary Steps and 4.2 section Consolidation Scenario Actuals_Rule Based COI in Group Reporting – Financial Consolidation (1SG) first to prepare the testing data.The test system uses the functionality of enhanced table structure of ACDOCU. |

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
| General Ledger Accountant - Group Reporting | SAP_BR_GL_ACCOUNTANT_GRP | Group Reporting | SAP_BR_GL_ACCOUNTANT_GRP | Ask your system administrator to assign to the testers.Generic User: G/L Accountant - Group Reporting |
| Administrator - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Administration - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Ask your system administrator to assign to the testers.Generic User:Administrator - Group Reporting |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Use the generic user below.Generic User: BPC_EXPERT |
| Group Accountant | SAP_BR_GRP_ACCOUNTANT | Group Reporting | SAP_BR_GRP_ACCOUNTANT | Ask your system administrator to assign to the testers.Generic User:Group Accountant |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1SG - Group Reporting – Financial Consolidation | Make sure that 1SG - Group Reporting – Financial Consolidation is activated before performing test procedures described in this test script for successful execution. |

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

| Feature Toggle ID | Feature Toggle Description |
| --- | --- |
| FINCS_BV_ADAPTATION | Toggle for FE of the Balance Validation |
| FINCS_ADDL_RPTG_RULE_DIMENS | Toggle for New Reporting Rules |

### Version Settings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Testing scenario in this test script use EUR as group currency. In this section, you copy SAP pre-delivered versions to testing versions with EUR as group currency.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) and choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate Close | The Configure Your Solution view is displayed. |  |
| 3 | Set Global Parameter | Select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: Y11Fiscal year: 2025Period: 012Cons. COA: Y1Go back to the original view. | The Global parameters log displays. |  |
| 4 | Create Version ZA1 | Select Create Version from Reference Version and choose Configure. Enter the following entries:Template Version: Y11Target Version: ZA1Test Run: <deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Choose Run and then Continue. | Target version ZA1 is created successfully with template version Y11. |  |
| 5 | Create Version ZB2 | Change Template Version to YB2. Change Target Version to ZB2 and remain other entries as the same.Choose Run and then Continue. | Target version ZB2 is created successfully with template version YB2. |  |
| 6 | Create Version ZF2 | Change Template Version to YF2. Change Target Version to ZF2 and remain other entries as the same.Choose Run and then Continue. | Target version ZF2 is created successfully with template version YF2. |  |
| 7 | Create Version ZB4 | Remain Template Version as YB4. Change Target Version to ZB4 and remain other entries as the same.Choose Run and then Continue. | Target version ZB4 is created successfully with template version YB4. |  |
| 8 | Define Versions | Go back to the previous view.Select Define Versions and choose Configure.Change the description of version ZB2 as Budget (2024).Change the description of version ZB4 as Budget (2026).Choose Save. |  |  |
| 9 | Set Global Parameter | Go back and select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: ZA1Fiscal year: 2025Period: 12Cons. COA: Y1Go back to the original view. | The Global parameters log displays. |  |
| 10 | Assign Process Period Cycle to ZA1 | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 001Assignment End Year: 9999Assignment End Period: 016Choose Save. | Assign Process Period Cycle S_MTH to version ZA1. |  |
| 11 | Set Global Parameter | Go back and select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: ZB2Fiscal year: 2026Period: 01Cons. COA: Y1Go back to the original view. | The Global parameters log displays. |  |
| 12 | Assign Process Period Cycle to ZB2 | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_001Assignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 2029Assignment End Period: 012Choose Save. | Assign Process Period Cycle S_001 to version ZB2. |  |
| 13 | Set Global Parameter | Go back and select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: ZB2Fiscal year: 2026Period: 01Cons. COA: Y1Go back to the original view. | The Global parameters log displays. |  |
| 14 | Assign Process Period Cycle to ZF2 | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 9999Assignment End Period: 016Choose Save. | Assign Process Period Cycle S_MTH to version ZF2. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Version: Y11Fiscal year: 2025Period: 12Cons. COA: Y1Go back to the original view. | The Global parameters log displays. |  |
| 4 | Create Version ZA1 | Select Create Version from Reference Version and choose Configure. Enter the following entries:Template Version: Y11Target Version: ZA1Test Run: <deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Choose Run and then Continue. | Target version ZA1 is created successfully with template version Y11. |  |
| 5 | Create Version ZB2 | Change Template Version to YB2. Change Target Version to ZB2 and remain other entries as the same.Choose Run and then Continue. | Target version ZB2 is created successfully with template version YB2. |  |
| 6 | Create Version ZF2 | Change Template Version to YF2. Change Target Version to ZF2 and remain other entries as the same.Choose Run and then Continue. | Target version ZF2 is created successfully with template version YF2. |  |
| 7 | Create Version ZB4 | Remain Template Version as YB4. Change Target Version to ZB4 and remain other entries as the same.Choose Run and then Continue. | Target version ZB4 is created successfully with template version YB4. |  |
| 8 | Define Versions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Versions.Change the description of version ZB2 as Budget (2026).Change the description of version ZB4 as Budget (2028).Choose Save. |  |  |
| 9 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 10 | Set Global Parameter | Make the following entries as below and choose Continue:Version: ZA1Fiscal year: 2025Period: 12Cons. COA: Y1 | The Global parameters log displays. |  |
| 11 | Open Assign Process Period Cycles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Process Period Cycles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 12 | Assign Process Period Cycle to ZA1 | Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 001Assignment End Year: 9999Assignment End Period: 016Choose Save. | Assign Process Period Cycle S_MTH to version ZA1. |  |
| 13 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 14 | Set Global Parameter | Make the following entries as below and choose Continue:Version: ZB2Fiscal year: 2026Period: 01Cons. COA: Y1 | The Global parameters log displays. |  |
| 15 | Open Assign Process Period Cycles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Process Period Cycles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 16 | Assign Process Period Cycle to ZB2 | Choose New Entries and make the following entry:Process Period Cycle: S_001Assignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 2029Assignment End Period: 012Choose Save. | Assign Process Period Cycle S_001 to version ZB2. |  |
| 17 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 18 | Set Global Parameter | Make the following entries as below and choose Continue:Version: ZF2Fiscal year: 2026Period: 01Cons. COA: Y1 | The Global parameters log displays. |  |
| 19 | Open Assign Process Period Cycles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Process Period Cycles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 20 | Assign Process Period Cycle to ZF2 | Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 9999Assignment End Period: 016Choose Save. | Assign Process Period Cycle S_MTH to version ZF2. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Table 1: Actuals @ Budget Rate CT

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Maintain Exchange Rates](#unique_8) [page ] 16 | Group Accountant | Currency Exchange Rates (F3616). |  |
| [Set Global Parameters and Open Period](#unique_9) [page ] 17 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD) |  |
| [Data Preparation by Copying Totals Records 12/2025 from A10 to ZA1](#unique_10) [page ] 18 | Group Accountant | Copy Transaction Data (CXCK) |  |
| [Data and Consolidation Monitor in 2025](#unique_11) [page ] 20 | Group Accountant | Data Monitor (CXCD)Consolidation Monitor - New Version (F7271) |  |

Table 2: Table 2: ZB2 Budget 2024 (12 + 1 + 1 + 1)

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Set Global Parameters and Open Period](#unique_12) [page ] 22 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD) |  |
| [Copy Totals Records 00-03/2026 from A10 to ZB2](#unique_13) [page ] 23 | Group Accountant | Copy Transaction Data (CXCK) |  |
| [Flexible Upload of Subsequent Year and Period Reported Financial Data (04-12/2026, 2027-2029)](#unique_14) [page ] 26 | Group Accountant | Data Monitor (CXCD)Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC) |  |
| [Data and Consolidation Monitor in 2026 - 2029](#unique_15) [page ] 27 | Administrator - Group ReportingGroup Accountant | Data Monitor (CXCD)Consolidation Monitor - New Version (F7271) |  |

Table 3: Table 3: ZF2 Forecast (2+10)

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Set Global Parameters and Open Period](#unique_16) [page ] 31 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD) |  |
| [Copy Totals Records Periods 00-02/2026 from A10 to ZF2](#unique_17) [page ] 32 | Group Accountant | Copy Transaction Data (CXCK) |  |
| [Flexible Upload of Financial Data 03-12/2026 in ZF2](#unique_18) [page ] 34 | Group Accountant | Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC) |  |
| [Data and Consolidation Monitor in 03-12/2026](#unique_19) [page ] 35 | Administrator - Group ReportingGroup Accountant | Data Monitor (CXCD)Consolidation Monitor - New Version (F7271) |  |

Table 4: SAC – ZB3 (2026) Integration Planning Scenario

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Export SAC Data to SAP S/4HANA Cloud Public Edition Using the SAC Export to SAP S/4HANA Feature](#unique_20) [page ] 38 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD) |  |
| [Pull Plan Data from SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition](#unique_21) [page ] 44 | Configuration Expert - Business Process ConfigurationAdministration - Group Reporting | Manage Your Solution (F1241)Manage Group Plan Data - for SAP Analytics Cloud Integration (FINCS_SAC_INT_PULL) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Actuals @ Budget Rate CT

In this version ZA1 you will consolidate the already loaded actuals data in version A10 but using another exchange rate for currency translation. All other automatic or manual consolidation tasks in data and consolidation monitor can be executed as it is in version A10. The only difference is the separate exchange rate which is taken for this version.

|  |
| --- |
| Note At least the data entry process in version A10 (refer to test script 1SG) must be executed. Otherwise no data are available for copying. |

#### Maintain Exchange Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the exchange rates are maintained for the budget rate. The exchange rates for this version are assigned to exchange rate type AVG1 and CLO1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Currency Exchange Rates (F3616). | The Currency Exchange Rates screen displays. |  |
| 3 | Display Exchange Rates | You can check if these exchange rates have been maintained, if not, please go to the next step to create these exchange rates:From JPY to EURAVG1: 31.12.2025CLO1: 31.12.2025From USD to EURAVG1: 31.12.2025CLO1: 31.12.2025From CNY to EURAVG1: 31.12.2025CLO1: 31.12.2025From AUD to EURAVG1: 31.12.2025CLO1: 31.12.2025 |  |  |
| 4 | Create Exchange Rates | In the Currency Exchange Rates view, choose Create.In the section Exchange Rate Details, maintain the following entries:Exchange Rate Type: AVG1From Currency: JPYTo Currency: EURValid From: 31.12.2025Quotation: IndirectExchange Rate: for example, 151Repeat the steps to finish creating all the exchange rates. | The exchange rates for AVG1 and CLO1 are maintained. |  |

#### Set Global Parameters and Open Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the global parameters are set.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Set Global Parameters screen displays. |  |
| 3 | Global Parameters | Enter the following values:Organizational Units:Cons. Group: CGRXXVersion/Time period:Version: ZA1Fiscal Year: 2025Period: 12Further Settings:Cons. COA: Y1Choose Continue. | The global parameters are set. |  |
| 4 | Open Period | Open Data Monitor (CXCD).In the Hierarchy column, right click your consolidation group and choose Menu > Edit > Open period . |  |  |

#### Data Preparation by Copying Totals Records 12/2025 from A10 to ZA1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, reported financial data can be loaded or, copied in the specific version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Copy Transaction Data (CXCK). | The Copy Totals Records screen is displayed. |  |
| 3 | Enter Parameters | Enter the following values.Organizational units sectionConsolidation Group: CGRxxConsolidation Unit: Mxx00 to Mxx08Posting level sectionReported financial data: <Select>Standardized financial data: <Select>Elimination entries: <Deselect>Consolidation entries: <Deselect>Settings sectionFrom version: A10 to ZA1From fiscal year: 2025 to 2025From period: 12 to 12Further settings sectionConsolidation COA: Y1Technical Settings sectionLog: <Select>Test Run: <Select>Delete target data first: <Select>Cumulative: <Select>Check the data based on the log and if this is sufficient, choose Run in production run mode by deselecting Test run. |  |  |

#### Data and Consolidation Monitor in 2025

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Data Monitor (CXCD). | The Data Monitor screen displays. |  |
| 3 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task Calc Net I and choose Update Run from the toolbar. |  |  |
| 4 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rep.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 5 | Data Monitor - Currency Translation | In the Data Monitor view, select your cons group of the task CurrTrans. and choose Update Run from the toolbar. |  |  |
| 6 | Check the Result after Currency Translation | Check in the log if the exchange rates 31.12.2025 AVG1 and CLO1 were taken. | Log shows the CT based on the Exchange rates AVG1 and CLO1 what you have maintained in Step [Maintain Exchange Rates](#unique_8) [page ] 16. |  |
| 7 | Data Monitor - Validation for Standardized Data | In the Data Monitor view, select your cons group of the task Val.Std.D task and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 8 | Block Tasks | Click on the respective tasks and choose Block.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 9 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 10 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Consolidation Group: CGRXXProcess Year Period: 012/2025Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 11 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block on Request to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 12 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |

### ZB2 Budget 2026 (12+1+1+1)

In this version ZB2 you will copy the reported financial data (RFD) from version A10 of periods 01-03/2026 to version ZB2 of periods 01-03/2026 (cumulative all data records, including consolidation and elimination).

Next step is to load data for 04-12/2026 in one upload step (periodic data) and consolidate all remaining periods in 2026 by running tasks in data and consolidation monitors in bundle mode.

Further steps are:

- Load data for 12/2027 and run tasks in data monitor / optional consolidation monitor
- Load data for 12/2028 and run tasks in data monitor / optional consolidation monitor
- Load data for 12/2029 and run tasks in data monitor / optional consolidation monitor

The copy and multiperiod data upload functions are provided as those of release 1802.

|  |
| --- |
| Note The 1SG test script must be completed before running the whole process successfully. If this could not happen for any reason the copy function cannot be used. Instead of copying the data from source version A10, you can run the consolidation process described in test script 1SG for the version ZB2 instead of using A10. Please refer to chapter 4.2 Consolidation Scenario Actuals. There you find all steps on how to run a consolidation process for the periods 12/2025, 01/2026 and 02/2026. When using the upload files which are located in 1SG test script, please replace the version A10 with ZB2.The period 12/2025 must be executed in A10 and cannot be executed in ZB2 due to the fact that the first valid period for ZB2 is 01/2026. That means that the balance carry forward values must be in the source system. |

#### Set Global Parameters and Open Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the global parameters are set.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Set Global Parameters screen displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: CGRXXVersion/Time period:Version: ZB2Fiscal Year: 2026Period: 1Cons. COA: Y1 | The global parameters are set. |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Open Periods | (If all the required periods are already opened for your group, you can skip this step.)Select your consolidation group and choose Menu > Edit > Open period.Repeat all these steps to open other periods by changing the parameter period by period (01-03/2026). | The periods open. |  |

#### Data Preparation

Purpose

In this process step, reported financial data will be loaded, copied in the specific version.

##### Copy Totals Records 00-03/2026 from A10 to ZB2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, reported financial data from the actuals version A10 will be copied into the budget version ZB2.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the app Copy Transaction Data (CXCK). | The Copy Totals Records screen displays. |  |
| 3 | Enter Parameters | Enter the following values in the following sections:Organizational units sectionConsolidation Group: CGRXXConsolidation Unit: Mxx00 to Mxx08Posting level sectionReported financial data: <Select>Standardized financial data: <Select>Elimination entries: <Select>Consolidation entries: <Select>Settings sectionFrom version: A10 to ZB2From fiscal year: 2026 to 2026From period: <leave blank> to <leave blank>Leave blank for period 00 for balance carryforward. Change to 01, 02, 03 for period 01, 02, 03.Further settings sectionConsolidation COA: Y1Technical settings sectionLog: <Select>Test Run: <Deselect>Delete target data first: <Select>Cumulative: <Deselect>Balance Carryforward: <Select for period 00, deselect for period 01, 02, 03>Check the data based on the log and if this is sufficient, choose Run in production run mode by deselecting Test Run.Note Repeat the copy program for period 01, 02, 03. | No error messages in the log.The data from Version A10 is copied. |  |
| 4 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Global parameters dialog box is displayed. |  |
| 5 | Set Global Parameters | Make the following entries and choose Continue:Cons Group: CGRXXRemember Change the XX to your group number.Cons Unit: NAVersion: ZB2Fiscal year: 2026Period: 01Cons. COA: Y1 |  |  |
| 6 | Block Tasks in Data Monitor | Open the app Data Monitor (CXCD).Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 7 | Repeat Block of Other Periods | Repeat the above steps to block data monitor tasks for period 2026/02 and 2026/03. |  |  |

##### Flexible Upload of Subsequent Year and Period Reported Financial Data (04-12/2026, 2027-2029)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you upload the reported financials to the budget version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Set Global Parameters screen displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: CGRXXVersion/Time period:Version: ZB2Fiscal Year: 2026Period: 04Cons. COA: Y1 | The global parameters are set. |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Open Periods | (If all the required periods are already opened for your group, you can skip this step.)Select your consolidation unit and choose Menu > Edit > Open Period .Repeat all these steps to open other periods by changing the Global Parameters period by period (04/2026 -12/2026, 12/2027, 12/2028 and 12/2029). | The periods opens. |  |
| 6 | Access the SAP Fiori App | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC). | The Flexible Upload of Reported Financial Data view is displayed. |  |
| 7 | Load RFD in One Step as Multiperiod Loading | Save the linked [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_UPLOAD_ZB2_CGRXX_SRD2.xlsx) locally and replace the with your assigned consolidation unit.Enter the following values in the following sections:General Selections section:Consolidation COA: Y1File section:Upload method: SRD2Physical file name: <Upload the attached file which has been saved locally>Technical Settings section:Test Run: <deselect, if necessary you can choose first to test run>Choose Execute. | No error messages in the log.The data listed in the excel file provided are uploaded in the expected and assigned period from 2026 to 2029. |  |

#### Data and Consolidation Monitor in 2026 - 2029

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The data for the budget years will be uploaded using the monitor. There is only one period =12 available. After uploading data, all tasks for data preparation and consolidation must be executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set Global Parameter | Open Set Global Parameters (CXGP).Enter the following values:Consolidation group: CGRXXVersion: ZB2Fiscal Year: 2026Period: 04Choose Continue. | The parameters are set. |  |
| 3 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138). |  |  |
| 4 | Assign Rule Group for Balance Validation at Unit Level | Choose Create.Version: ZB2Task: S1080Valid From: 2026001Choose Continue.Maintain the following entries and choose Create.Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 5 | Assign Rule Group for Balance Validation at Group Level | Go back to the original view.Choose Create and make the following entries:Version: ZB2Task: S2980Valid From: 2026001Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access the SAP Fiori App | Open Data Monitor (CXCD). | The Data Monitor screen is displayed. |  |
| 8 | Open Periods | Select your consolidation group and choose Menu > Edit > Open period. |  |  |
| 9 | Run All Tasks in Data Monitor of 04/2026 | Data are posted in the previous step in general.Run tasks from Calculate Net Income to Standardized Data Validation.Manual tasks can be closed without posting, but you can also post any adjustment document as you want. |  |  |
| 10 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 11 | Run Data Monitor for Periods 05/2026 to 12/2026, 012/2027, 012/2028 and 012/2029. | Change period from 05/2026 to 12/2026 by selecting Global Parameters to repeat.Open the period and run all necessary tasks in Data Monitor for period from 05 to 12. And then block all tasks.Repeat steps for period 12/2027, 12/2028 and 12/2029. |  |  |
| 12 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). | The New Consolidation Monitor screen is displayed. |  |
| 13 | Run Consolidation Monitor of Period 012/2026 | Maintain the following entries and choose Go:Consolidation Chart of Accounts: Y1Version: ZB2Consolidation Group: CGRXXProcess Year Period: 012/2026Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 14 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 15 | Repeat Steps in Consolidation Monitor of Periods 012/2027, 012/2028 and 012/2029 | Change Process Year Period as periods 012/2027, 012/2028 and 012/2029 and choose Run Full Consolidation separately. |  |  |
| 16 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 17 | Check Data | You can check data with app Group Data Analysis (W0135). |  |  |

### ZF2 Forecast (2+10)

In this version ZF2 you will copy the reported financial data (RFD) from version A10 from periods 01-02/2026 to version ZF2 periods 01-02/2026 (cumulative all data records, including consolidation, and elimination).

Next step is to load data for 03-12/2026 in one upload step (periodic data) and consolidate all remaining periods in 2026 by running all tasks in data and consolidation monitors.

The 1SG test script must be completed before running the whole process successfully. If this could not happen for any reason the copy function cannot be used. Instead of copying the data from source version A10, you can run the consolidation process described in test script 1SG with using the version ZF2 instead of using A10. Please refer to chapter 4.2 Consolidation Scenario Actuals. There you find all steps on how to run a consolidation process for the periods 12/2025, 01/2026 and 02/2026. When using the upload files which are located in 1SG test script, please replace the version A10 with ZF2.

#### Set Global Parameters and Open Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step the global parameters are set and periods are opened.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Set Global Parameters screen is displayed. |  |
| 3 | Global Parameters | Enter the following values:Consolidation group: CGRXXVersion: ZF2Fiscal Year: 2026Period: 01Cons. COA: Y1Choose Continue. | Global parameters are set. |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Open Periods 01-12/2026 | Note If all the 2026 periods are already opened for your group, you can skip this step.To open period 01:Select your consolidation group. Choose Menu > Edit > Open period .To open subsequent periods:Repeat all these steps by changing the global parameters period by period (02-12/2026, etc.). | The message Period 001/2026 for CG/CU CGRXX opened is displayed by system. |  |

#### Data Preparation

Purpose

In this process step, reported financial data will be loaded and copied in the specific version.

##### Copy Totals Records Periods 00-02/2026 from A10 to ZF2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, reported financial data will be copied to the specific version ZF2.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Copy Transaction Data (CXCK). | The Copy Totals Records screen displays. |  |
| 3 | Copy Transaction Data | Enter the following values in the Organizational units sectionConsolidation Group: CGRxxConsolidation Unit: MXX00 to MXX08Posting level sectionReported financial data: <Select>Standardized financial data: <Select>Elimination entries: <Select>Consolidation entries: <Select>Setting sectionFrom version: A10 to ZF2From fiscal year: 2026 to 2026From period: <leave blank> to <leave blank>Leave blank for period 00 for balance carryforward. Change to 01, 02 for period 01, 02.Further settings sectionConsolidation COA: Y1Technical Settings sectionLog: <Select>Test Run: <Deselect>Delete target data first: <Select>Cumulative: <Deselect>Balance Carryforward: <Select for period 00, deselect for period 01, 02>Ignore the warning message and choose Continue.Note Repeat the copy program for period 01, 02. | No error messages, data from A10 are copied to ZF2 for the selected consolidation unitsCheck data availability via data base listing or reporting feature. |  |

##### Flexible Upload of Financial Data 03-12/2026 in ZF2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Load the reported financial data for version 03-12/2026 in one step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC). | The Flexible Upload of Reported Financial Data screen is displayed. |  |
| 3 | Load RFD for period 03- 12/2026 by Multiperiod | Please use the upload [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_UPLOAD_ZF2_CGRXX_SRD2.xlsx) attached. Save the file locally and replace the XX as per IDs of companies in your assigned consolidation group.Enter the following values in the following sections:General selections sectionConsolidation COA: Y1File sectionUpload method: SRD2Physical file name: <Upload the attached file which has been saved locally>Technical settings sectionTest Run: <deselect>Original List: <deselect>Choose Execute. | No error messages in the log.The data listed in the excel file provided is uploaded in the expected and assigned period of year 2026. |  |
| 4 | Group Data Analysis | You can check data by using the app Group Data Analysis (W0135). |  |  |

#### Data and Consolidation Monitor in 03-12/2026

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 2 | Set Global Parameters | Open Set Global Parameters (CXGP).Make the following entries and choose Continue:Consolidation Group: CGRXXVersion: ZF2Fiscal Year: 2026Period: 03 | The parameters are set. |  |
| 3 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138). |  |  |
| 4 | Assign Rule Group for Balance Validation at Unit Level | Choose Create.Version: ZF2Task: S1080Valid From: 2026001Choose Continue.Maintain the following entries and choose Create.Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 5 | Assign Rule Group for Balance Validation at Group Level | Go back to the original view.Choose Create and make the following entries:Version: ZF2Task: S2980Valid From: 2026001Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 7 | Data Monitor | Open Data Monitor (CXCD). | The Data Monitor screen displays. |  |
| 8 | Open Periods | Select your consolidation group and choose Menu > Edit > Open period. |  |  |
| 9 | Run All Tasks in Data Monitor of 04/2026 | Data are posted in the previous step in general.Run tasks from Calculate Net Income to Standardized Data Validation.Manual tasks can be closed without posting, but you can also post any adjustment document as you want. |  |  |
| 10 | Repeat Running Data Monitor | Change period from 05/2026 to 12/2026 by selecting Global Parameters to repeat.Open the period and run all necessary tasks in Data Monitor for period from 05 to 12.And then block all tasks. |  |  |
| 11 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 12 | Run Consolidation Monitor of 003/2026 | Maintain the following entries and choose Go:Consolidation Chart of Accounts: Y1Version: ZF2Consolidation Group: CGRXXProcess Year Period: 003/2026Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 13 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block on Request to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 14 | Repeat Run Tasks in Consolidation Monitor | Change Process Year Period one by one to run Data Monitor and Consolidation Monitor for periods from 004/2026 to 012/2026.And then block all tasks. |  |  |
| 15 | Access App Group Data Analysis | Open Group Data Analysis (W0135)Select the related filters and check data. |  |  |

### SAC – ZB4 (2028) Integration Planning Scenario (Optional)

With SAP Analytics Cloud (SAC) financial plan data be available, you're allowed to make a connection between SAC and Group Reporting (GR) to transfer (Pull or Push) transactional data from GR to SAC and the other way around. In this chapter, there are two options for you to transfer planning data from SAC to GR, one is to push plan data in SAC to GR with an exporting job, the other is to pull plan data from SAC into GR by executing a Data Monitor in Group Reporting. The integration scenario happens in the version ZB4 for fiscal year 2028.

#### Export SAC Data to SAP S/4HANA Cloud Public Edition Using the SAC Export to SAP S/4HANA Feature

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the SAC environment, plan data to export are available in the SAP_FI_GFP_IM_GroupFinance model, also referred to as the SAC best practice model for group planning. The following procedure explains how to export data from this model to SAP S/4HANA Cloud Public Edition using the export to SAP S/4HANA Cloud Public Edition feature.

Prerequisite

1. Import SAP Business Content: Group Financial Planning for SAP S/4HANA and SAP S/4HANA Cloud with reference to [Importing SAP Business Content: Group Financial Planning for SAP S/4HANA and SAP S/4HANA Cloud | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/f630b7a572714719b4bf463af630eaa4.html?state=latest)
2. Activate the connection between SAP Analytics Cloud for Planning and SAP S/4HANA Cloud Public Edition with reference to Group Financial Planning scenario in [Integrating SAP Analytics Cloud with SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/2f610a5f08cb4142ac188c3e6a127b4e.html?state=latest).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On (SAP S/4HANA Cloud Public Edition) | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set Global Parameters | Open Set Global Parameters (CXGP).Enter the following values:Organizational Units:Cons. Unit: <Your consolidation unit>Version/Time period:Version: ZB4Fiscal Year: 2028Period: <From 1 to 12>Further Settings:Cons. COA: Y1Choose Continue. | The global parameters are set. |  |
| 3 | Open Period | Open Data Monitor (CXCD).In the Hierarchy column, right click your consolidation unit and choose Open Period.Repeat the step for periods 2-12. | The 12 periods of 2028 are open. |  |
| 4 | Log On (SAC) | Log on to the SAC system with the test user provided. | The SAC home page is displayed.(“Hello, <user name>”) |  |
| 5 | Open the Modeler List | In the left panel, select Files. | All files are displayed. |  |
| 6 | Open the Model | In the search field on the top, search the source model SAP_FI_GFP_IM_GroupFinance and open it. | The main ribbon shows Model Structure screen of SAP_FI_GFP_IM_GroupFinance. |  |
| 7 | Open Data Management | On the upper left side of the screen, in the dropdown list, switch to the Data Management screen. | The Data Management screen displays. |  |
| 8 | Run the Export Wizard | In the Export Jobs area, choose the Export Data icon on the right side and choose Export Data To SAP S/4HANA. | The Export Data to SAP S/4HANA window opens.The model name is displayed in the first list. |  |
| 9 | Choose the Connection | In the Connection section, from the drop-down list, select the connection you set earlier and choose Next. | The Target Data Selection – SAP S/4HANA window opens. |  |
| 10 | Select the Target Dimensions | From the S/4HANA Application list, choose Group Reporting Planning Integration from the dropdown list.Select the checkboxes of the following fields and then choose Next:Consolidation FS ItemSubitemSubitem CategoryCons. Chart of AccountsDocument TypeConsolidation UnitConsolidation VersionFinancial Transaction TypePosting PeriodFiscal YearPartner UnitLocal CurrencyAmount in Local Currency | The list of selected dimensions are displayed on the right-hand side of the window as Selected Fields. |  |
| 11 | Map Balance Sheet Transaction Data | Map the dimensions as per the following information:Target DimensionsSource DimensionConsolidation FS ItemSAP_FI_GFP_FSITEMSubitemSAP_FI_GFP_TRANSACTIONTYPESubitem CategoryChoose Not Mapped in the Source Dimension dropdown list.Set 1 as Default Value.Cons. Chart of AccountsChoose Not Mapped in the Source Dimension dropdown list.Set Y1 as Default Value.Document TypeChoose Not Mapped in the Source Dimension dropdown list.Set 08 as Default Value.Consolidation UnitSAP_FI_GFP_CONSUNITConsolidation VersionChoose Not Mapped in the Source Dimension dropdown list.Set ZB4 as Default Value.Financial Transaction TypeSAP_FI_GFP_TRANSACTIONTYPEPosting PeriodDateFiscal YearDatePartner UnitSAP_FI_GFP_PRTNRCONSUNITAmount in Local CrcyAMOUNT_LCChoose + Add Filter to add three more filters:Select Version. Choose Plan Bottom Up and then choose OK.Select SAP_FI_GFP_FSITEM. Choose Hierarchy and then BS and PL and then choose OK.Select SAP_FI_GFP_TRANSACTIONTYPE. Choose Opening balance, Changing balance, Closing balance and then choose OK. |  |  |
| 12 | Run the Export | Choose Next. | The export process window is displayed (waiting window).The completion message is displayed at the bottom of the screen. |  |
| 13 | Name the Export Job | For the newly-finished export job, you can rename it as S4HANA_EXPORT_BS. |  |  |
| 14 | Log On (SAP S/4HANA Cloud Public Edition) | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 15 | Access the Fiori App | Open Manage Your Solution (F1241). |  |  |
| 16 | Configure Your Solution | Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate CloseThen choose the item Basic Settings. |  |  |
| 17 | Copy New Document Type | To create a new document type for exporting P&L data, select the step Define Document Types and choose Configure.Select the Doc. Type 08 and then choose Copy As...Enter the Document Type name as you want, for example, Z8.Choose Copy > copy all > Continue. |  |  |
| 18 | Repeat Steps for Exporting P&L Transaction Data | Repeat steps 9 to 11 to run another export job of P&L transaction data. |  |  |
| 19 | Map P&L Transaction Data | The mapping is automatically defined for the following two dimensions and cannot be changed:Local CurrencyAmount in Local CrcyMap the other dimensions as per the following information:Target DimensionsSource DimensionConsolidation FS ItemSAP_FI_GFP_FSITEMSubitemSAP_FI_GFP_FUNCTIONALAREASubitem CategoryChoose Not Mapped in the Source Dimension dropdown list.Set 2 as Default Value.Cons. Chart of AccountsChoose Not Mapped in the Source Dimension dropdown list.Set Y1 as Default Value.Document TypeChoose Not Mapped in the Source Dimension dropdown list.Set the newly-created document type , for example, Z8 as Default Value.Consolidation UnitSAP_FI_GFP_CONSUNITConsolidation VersionChoose Not Mapped in the Source Dimension dropdown list.Set ZB4 as Default Value.Financial Transaction TypeSAP_FI_GFP_TRANSACTIONTYPEPosting PeriodDateFiscal YearDatePartner UnitSAP_FI_GFP_PRTNRCONSUNITChoose + Add Filter to add three more filters.Select Version. Choose Plan and then choose OK.Select SAP_FI_GFP_FSITEM. Choose Profit and loss and then choose OK.Select SAP_FI_GFP_TRANSACTIONTYPE. Choose 900 and C99 both and then choose OK. |  |  |
| 20 | Run the Export | Choose Next. | The export process window is displayed (waiting window).The completion message is displayed at the bottom of the screen. |  |
| 21 | Rename the Export Job | For the newly-finished export job, you can rename it as S4HANA_EXPORT_PL. |  |  |
| 22 | Log On (SAP S/4HANA Cloud Public Edition) | Log on to the SAP Fiori launchpad as a Consolidation Specialist. | The SAP Fiori launchpad displays. |  |
| 23 | Check Status in SAP S/4HANA Cloud Public Edition | Open Data Monitor (CXCD).Right click the Status icon of Data Collection task. Choose Last log. Check the export status of each period. |  |  |

#### Pull Plan Data from SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

There's a more flexible integration of SAC planning data in Group Reporting. The following procedure explains how to pull data from SAP Analytics Cloud into SAP S/4HANA Cloud Public Edition – Group Reporting. You can execute a Pull Data from SAP Analytics Cloud task (task category 0G) in the Data Monitor app.

Prerequisite

Import SAP Business Content: Group Financial Planning for SAP S/4HANA and SAP S/4HANA Cloud with reference to [Importing SAP Business Content: Group Financial Planning for SAP S/4HANA and SAP S/4HANA Cloud | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/f630b7a572714719b4bf463af630eaa4.html?state=latest)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set Global Parameters | Open Manage Your Solution (F1241) and choose Configure Your Solution.Make the following entries and choose Go:Application Area: FinanceSub Application Area: Corporate Close | The Configure Your Solution view is displayed. |  |
| 3 | Set Global Parameter | In the results section, choose Item Name Basic Settings.Select Set Global Parameters and choose Configure on that row.Set the following parameters:Organizational Units:Cons. Unit: <Your consolidation unit>Version/Time period:Version: ZB4Fiscal Year: 2028Period: 1Further Settings:Cons. COA: Y1Choose Continue.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The global parameters are set. |  |
| 4 | Create Task Group | Go back to the previous view.Choose Item Name Data Processing.Select Define Task Group and choose Configure on that row.Select task group S10 and choose Copy As….Enter the Task group name as Z10, and Description as Data Monitor (SAC)Press Enter and then choose copy all in the popup message.Choose Continue.Select newly created task group Z10 and double click Assign tasks to task group on the left Dialog Structure.Choose New Entries.Make the following entries and choose Save.Task: S1021Block auto.: <Deselect>Milestone: <Deselect>Position: 16Last task, DM: <Deselect> | A new task group is created. |  |
| 5 | Assign Task Group to Version | Go back to the previous view.Select Assign Task Group to Version and choose Configure on that row.Choose New Entries.Make the following entries and choose Save.Start Year: 2028Period eff: 1Period cat.: 9Data mon. task group: Z10Cons mon. task group: S20 |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Administration - Group Reporting . | The SAP Fiori launchpad is displayed. |  |
| 7 | Create a Tenant ID | Open Manage Group Plan Data - for SAP Analytics Cloud Integration (FINCS_SAC_INT_PULL).Make the following entries to Tenant ID for Group Plan Data:Tenant ID: PULL_SAC_T1Note The tenant ID is used to identify the SAP Analytics Cloud tenant when accessing the system to read group plan data.Communication Arrangement: Pull_SAC_0370_CANote You can create the communication arrangement in the app Communication Arrangements (F1763), using the arrangement scenario SAP_COM_0370. If the scenario SAP_COM_0370 doesn't exist, please refer to the 2U6 setup guide to create.Press Save. | The Tenant Pull_SAC_T1 is created. |  |
| 8 | Create Configuration ID PULL_SAC_C1 | Double click Configuration ID for Group Plan Data on the left Dialog Structure.Choose New Entries and enter the following entries:Configuration ID: PULL_SAC_C1Description: Test for Pull SACActive: <Checked>Tenant ID for Plan Data: PULL_SAC_T1Provider ID for Plan Data: CCQ11PVVYUUX6U3GNOFQNPZCOWPackage Size: <leave empty>Choose Save. | The Configuration ID PULL_SAC_C1 is created. |  |
| 9 | Maintain Mappings | Select Configuration ID PULL_SAC_C1, and double click Mapping of Group Plan Data and make the following entries:SAP S/4HANA FieldMapping TypeSource FieldFixed ValueAMOUNTINTLOCALCURRENCYField MappingAMOUNT_LCCONSOLIDATIONCHARTOFACCOUNTSFixed ValueY1CONSOLIDATIONDOCUMENTTYPEFixed Value09CCONSOLIDATIONUNITField MappingSAP_FI_GFP_CONSUNITCONSOLIDATIONVERSIONFixed ValueZB4FINANCIALSTATEMENTITEMField MappingSAP_FI_GFP_FSITEMFINANCIALTRANSACTIONTYPEField MappingSAP_FI_GFP_TRANSACTIONTYPEFISCALPERIODField MappingDateFISCALYEARField MappingDateFUNCTIONALAREAField MappingSAP_FI_GFP_FUNCTIONALAREAPARTNERCONSOLIDATIONUNITField MappingSAP_FI_GFP_PRTNRCONSUNITCONTROLLINGAREAFixed ValueA000PROFITCENTERField MappingSAP_FI_GFP_PROFITCENTER |  |  |
| 10 | Filter Settings for Group Plan Data | Double click Filter Settings for Group Plan Data on the left Dialog Structure.Choose new entries and make the following entries:Source Filed: VersionOption: EqualFixed Value Low: public.Actual Bottom Up |  |  |
| 11 | Task Assignment | Double click Task Assignment on the left Dialog Structure.Choose new entries and make the following entries:From Year: 2028From Period: 001Task: S1021Choose Save. |  |  |
| 12 | Log On | Log on to the SAP Fiori launchpad as a a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 13 | Open Period | Open Data Monitor (CXCD).In the Hierarchy column, right click your consolidation unit and choose Open Period.Repeat the step for periods 2-12. |  |  |
| 14 | Execute Task | Select the cons group of the task S1021 and then choose Update Run. Choose Yes in the Application Jobs pop up. |  |  |

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
> Flagged while digesting this document, not verified: Version descriptions differ between the two configuration paths: Configure Your Solution step 8 sets ZB2 to 'Budget (2024)' and ZB4 to 'Budget (2026)', while the SAP Central Business Configuration path sets ZB2 to 'Budget (2026)' and ZB4 to 'Budget (2028)'; the Overview Table also labels ZB2 as 'Budget 2024' while section 4.2 says 2026.

> [!warning] Conflict
> Flagged while digesting this document, not verified: In the Configure Your Solution version setup, step 13 sets global parameters to version ZB2 before 'Assign Process Period Cycle to ZF2' (step 14), whereas the Central Business Configuration path sets version ZF2 for the same step.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Pull scenario filter is 'Version Equal public.Actual Bottom Up' for pulling plan data into ZB4, while the push export filters use 'Plan Bottom Up' (balance sheet) and 'Plan' (P&L); it is unclear whether the pull filter is intended to differ.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[07-group-reporting-and-consolidation/2608-upload-zb2-cgrxx-srd2-129]]
- see-also :: [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/28B_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 71,778 chars in the whole document
