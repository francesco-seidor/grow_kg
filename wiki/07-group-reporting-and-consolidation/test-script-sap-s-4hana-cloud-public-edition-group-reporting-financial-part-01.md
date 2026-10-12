---
id: 07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01
title: Test Script SAP S/4HANA Cloud Public Edition - Group Reporting – Financial Consolidation (1SG) (1SG_S4CLD2608_BPD_EN_XX) — part 1 of 2
description: "Step-by-step test script for scope item 1SG (Group Reporting financial consolidation, S/4HANA Cloud Public Edition 2608): prerequisites, scenarios, reporting."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/financial-consolidation-process, topic/intercompany-matching-and-reconciliation]
aliases: []
keywords: [Financial Consolidation Process, group reporting consolidation, consolidation test procedures, integrated intercompany, intercompany reconciliation, rule based coi, consolidation method change, multiple group currencies, restatement versions, hierarchy elimination]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx#lines-1-1722"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-763
topic: 07-group-reporting-and-consolidation/financial-consolidation-process
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Group Reporting – Financial Consolidation (1SG) (1SG_S4CLD2608_BPD_EN_XX) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx`, part 1 of 2 (lines 1–1722 of the extracted text), extracted with `mammoth`. Grouped under **Financial Consolidation Process** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Group Reporting – Financial Consolidation (1SG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232858723)

[2 Prerequisites 4](#_Toc232858724)

[2.1 System Access 4](#_Toc232858725)

[2.2 Roles 4](#_Toc232858726)

[2.3 Business Conditions 6](#_Toc232858727)

[2.4 Preliminary Steps 7](#_Toc232858728)

[2.4.1 Basic Settings 7](#_Toc232858729)

[2.4.2 Additional Settings for Multiple Group Currencies and Restatement (Optional) 25](#_Toc232858730)

[3 Overview Table 35](#_Toc232858731)

[4 Test Procedures 40](#_Toc232858732)

[4.1 Consolidation Scenario for Integrated Intercompany 40](#_Toc232858733)

[4.1.1 Preparation for Integration Scenario 41](#_Toc232858734)

[4.1.2 2025.11 Integrated Intercompany 47](#_Toc232858735)

[4.2 Consolidation Scenario Actuals_Rule Based COI 71](#_Toc232858736)

[4.2.1 Create Consolidation Units and Groups 72](#_Toc232858737)

[4.2.2 Define Hierarchies for Hierarchy Elimination (Optional) 76](#_Toc232858738)

[4.2.3 Set up Group Structure 79](#_Toc232858739)

[4.2.4 2025.12 Initial Consolidation 84](#_Toc232858740)

[4.2.5 2026.01 Full Consolidation 93](#_Toc232858741)

[4.2.6 2026.02 Subsequent Consolidation 99](#_Toc232858742)

[4.2.7 2026.03 Subsequent Consolidation 102](#_Toc232858743)

[4.3 Consolidation Scenario Actuals_Method Change (Rule Based COI) 105](#_Toc232858744)

[4.3.1 Create Consolidation Units and Groups 106](#_Toc232858745)

[4.3.2 Set Up Group Structure 109](#_Toc232858746)

[4.3.3 2025.12 Initial Consolidation 112](#_Toc232858747)

[4.3.4 2026.01 Subsequent Consolidation 121](#_Toc232858748)

[4.3.5 2026.02 Method Change at the End of Period 125](#_Toc232858749)

[4.4 Consolidation Scenario_Multiple Group Currencies and Restatement (Optional) 129](#_Toc232858750)

[4.4.1 Create Consolidation Units and Groups 131](#_Toc232858751)

[4.4.2 Set up Group Structure 136](#_Toc232858752)

[4.4.3 2025.12 Initial Consolidation 144](#_Toc232858753)

[4.4.4 2026.01 Full Consolidation 154](#_Toc232858754)

[4.4.5 2026.02 Subsequent Consolidation 166](#_Toc232858755)

[4.5 Reporting 170](#_Toc232858756)

[4.5.1 Balance Sheet (B/S) Reports 170](#_Toc232858757)

[4.5.2 P&L by Nature of Expense 172](#_Toc232858758)

[4.5.3 Cash Flow Statement 174](#_Toc232858759)

[4.6 Configuration App 175](#_Toc232858760)

[4.6.1 Configuration Activities 176](#_Toc232858761)

[4.6.2 Organization Structure Creation 181](#_Toc232858762)

[4.6.3 Master Data Configuration with SAP Fiori UI 184](#_Toc232858763)

[4.6.4 Validation 188](#_Toc232858764)

## Purpose

Overview

This scope item provides statutory financial consolidation capabilities for SAP S/4HANA customers.

The key features included in this release include data integration with SAP S/4HANA Cloud Public Edition, avoids replication (using the main actual table as a data source), flexible upload capability to collect financial data from non-SAP S/4HANA subsidiaries, product validations to ensure data integrity, consolidation methods to produce statutory consolidation, and key audit reports and consolidated financial statements including Profit and Loss and Balance Sheet reports.

This scope item also provides two optional scenarios. You can choose whether to perform them or not according to your own needs:

- Hierarchy Elimination

Hierarchy Elimination covers consolidation for management-oriented organizational units such as profit center and business segment. This functionality addresses the needs of business unit managers and group controllers who need to respond rapidly to changes resulting from internal organization unit restructuring and who need to focus on specific internal performance figures and not the entire group financial statement.

Hierarchy Elimination introduces new reporting dimensions that are derived at report run-time and not persisted in the universal journal. These virtual organizational units allow the reporting user to show inter-unit eliminations at the correct hierarchy level.

- Consolidation with Multiple Group Currencies and Restatement Versions

We provide the following major scenarios of version concept: group currency extension versions, restatements, and simulations.

Group currency extension versions allow you to consolidate in different group currencies.

Restatement versions can be used when new accounting standards are adopted or management organizations are changed. By restating the prior periods, you can compare financial data between prior and current periods.

Simulation versions are used when you need to consolidate the current period using different settings (for example, group structure, cons methods).

|  |
| --- |
| Note The version configuration in this document is only for testing purposes only. In your projects, design your version stack based on your own version settings and requirements. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1SG_S4CLD2602_BPD_EN_XX.docx) ). |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT | Ask your system administrator to assign to the testers.Generic User: G/L Accountant - Group Reporting |
| General Ledger Accountant - Group Reporting | SAP_BR_GL_ACCOUNTANT_GRP | Group Reporting | SAP_BR_GL_ACCOUNTANT_GRP | Ask your system administrator to assign to the testers.Generic User: G/L Accountant - Group Reporting |
| Administrator - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Administration - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Ask your system administrator to assign to the testers.Generic User:Administrator - Group Reporting |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Use the generic user below.Generic User: BPC_EXPERT |
| Group Accountant | SAP_BR_GRP_ACCOUNTANT | Group Reporting | SAP_BR_GRP_ACCOUNTANT | Ask your system administrator to assign to the testers.Generic User:Group Accountant |
| General Ledger Accountant - Intercompany | SAP_BR_RECON_ACCOUNTANT | Intercompany Reconciliation | SAP_BR_RECON_ACCOUNTANT | Use the generic user below.Generic User: RECON_ACCOUNTANT |

### Business Conditions

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

### Preliminary Steps

#### Basic Settings

Before you start the process testing, below manual steps are necessary to complete the system settings.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) and choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate Close | The Configure Your Solution view is displayed. |  |
| 3 | Set Global Parameter | In the results section, choose Item Name Basic Settings.Select Set Global Parameters and choose Configure on that row.Set the following parameters:Version: Y10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 4 | Create Version A10 | Go back to the original view.Select Create Version from Reference Version and choose Configure. Enter the following entries:Template Version: Y10Target Version: A10Test Run: <Deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Choose Run and then Continue.Ignore the information message Documents aren´t auto-reversed in periods greater than 12. and choose Exit.Note Group Currency once defined in Create Version from Reference Version, cannot be changed anymore.Setting group currency to EUR is only for the purpose of the testing in this test script. If you want to maintain your own group currency, please use your own data setting and files instead of the ones we provide.If you have already made postings on A10 with other currencies except EUR, please create your own version for the following testing and adjust all the data files used in this test script accordingly. | Target version A10 is created successfully with template version Y10. |  |
| 5 | Set Global Parameter | Go back and select Set Global Parameters and choose Configure on that row.Set the following parameters:Version: A10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 6 | Assign Process Period Cycles | Go back to the previous view.Search and select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 012Assignment End Year: 9999Assignment End Period: 016Press Enter and then choose Save. | Assign Process Period Cycle to version A10. |  |
| 7 | Select Master Data Fields | Go back to the previous view.Choose Item Name Master Data. Choose Define Consolidation Master Data Fields and choose Configure on that row. |  |  |
| 8 | Define Consolidation Master Data Fields | Ensure the attributes and attribute values are configured, as listed, in the following table:Enable InputsEnable Master DataEnable Hierarchy (*)Enable Hierarchy Elimination (*)Aggregate on CarryforwardAggregate Data on ReleasePartner Company√ProfitCenter√√√√Segment√√√√FunctionalArea√√√ControllingArea√√ChartOfAccounts√√Customer√Material√√PartnerProfitCenter√√√PartnerSegment√√√GLAccount√√AssignmentReference√√√(*): optional, specific to Matrix consolidationIf necessary, select More > Edit and enter the values to align with the table.NoteIf the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again.If additional fields are not activated by default, please delete additional fields mentioned above in the data files in order to run through the test script. |  |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 10 | Access the SAP Fiori App (Optional) | The below two steps are optional for Hierarchy Elimination.Open Manage Rules for Automatic Postings (F8339). |  |  |
| 11 | Update Automatic Posting Rules (Optional) | Under Rules section, select the rule S2_01_0101.Go into the detailed view of the rule and choose Edit.Select the Posting Line 2 and choose Create in Filed Assignments. Add new assignments as the below table.Table 1:FieldAssignment TypeValueApply Only IfControlling AreaValueA000Source field is filledPartner Profit CenterValue OfProfit CenterSource field is filledProfit CenterValue OfPartner Profit CenterSource field is filledPartner Segment for Segmental ReportingValue OfSegment for Segmental ReportingSource field is filledSegment for Segmental ReportingValue OfPartner Segment for Segmental ReportingSource field is filledChoose Save.Remember Repeat the above steps to update another rule S2_01_0104 of its Posting Line 5 and Posting Line 6. |  |  |
| 12 | Access the SAP Fiori App | Open Manage Reporting Rules - Configure Reporting Items (F8535). | The Manage Reporting Rules view displays. |  |
| 13 | Activate Reporting Item Hierarchies | Select the following entries and choose Go:Cons. Chart of Accounts: Y1Reporting Item Hierarchy: X1 Statement of EquityReporting Rule: Y10Choose > (Details) to go to the detailed page of the reporting item hierarchy X1.In the section of Reporting Rule Activations, check if the reporting item hierarchy has been activated. If yes, ignore the following steps. If not, choose Edit and then choose Create.Select resolution date, for example, <Today>, and then choose Save.Go back to the previous view and repeat the steps for reporting item hierarchies X2-Statement of Cash Flow, X3-Statement of Comprehensive Inc and X4-P&L by Function of Expense to activate these hierarchies. | Reporting Item Hierarchies Activated Successfully. |  |
| 14 | Maintain FS Item Mapping | From the SAP Fiori launchpad, open Map FS Items with G/L Accounts (F3333) and verify that Mapping Revisions appear in the table with Active status.If no mapping revisions appear, create mappings by downloading this [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2602_Template_Financial_Statement_Item_Mapping.xlsx). After completing the file, use the Import FS Item Mappings (F3335) SAP Fiori app to import the mappings.Note The mapping template is sample data. The GL accounts in your system depend on your scoping. Please review and adjust if necessary. |  |  |
| 15 | Assign FS Item Mapping | From the SAP Fiori launchpad, open Assign FS Item Mappings (F3334) and verify that the following values appear in the Items list:Start of Assignment: 001/1900Consolidation Version: Y10 (FS item mapping version)Cons. Chart of Accounts: Y1 (Consolidation Chart of Accounts)G/L Chart of Accounts: YCOA (Standard Chart of Accounts)FS Item Mapping: Y1 (Consolidation chart of account)FS Item Mapping Revision: 1If this item is not in the table, choose New to open a dialog box, add the values, and choose Save.Use the < (Back) button to return to the SAP Fiori launchpad. |  |  |
| 16 | Define Master Data] | There are two options available for defining master data. You can either define master data manually or import master data directly, You do not have to do both. The following option describes defining master data for consolidation fields. |  |  |
| 17 | [Option 1] Access the SAP Fiori App to Define Master Data | Open Define Master Data for Consolidation Fields (F3007).Select Profit Center. Choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionPC0001A000PC0001PC0002A000PC0002PC0003A000PC0003PC0004A000PC0004PC0005A000PC0005PC0006A000PC0006PC0007A000PC0007PC0008A000PC0008PC0009A000PC0009PC0010A000PC0010Select < (Back) and choose Segment for Segmental Reporting and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionSE0001SE0001SE0002SE0002SE0003SE0003SE0004SE0004SE0005SE0005Select < (Back) and choose Material Number and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionMERCHANDIZE AMerchandize AMERCHANDIZE BMerchandize BSelect < (Back) and choose Functional Area and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionYD20IC difference - operatingYD70IC difference - financialNote If the values for Consolidation Master Data Fields already exist as the above tables, you don't need to maintain them again. |  |  |
| 18 | [Option 2] Import Master Data] | The following steps are importing master data directly. |  |  |
| 19 | [Option 2] Access the SAP Fiori App to Import Master Data | Open Import Consolidation Master Data (F3924). |  |  |
| 20 | [Option 2] Create Profit Center and Import | In the Master Data Type Profit Center, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.Controlling AreaProfit CenterProfit Center NameA000PC0001PC0001A000PC0002PC0002A000PC0003PC0003A000PC0004PC0004A000PC0005PC0005A000PC0006PC0006A000PC0007PC0007A000PC0008PC0008A000PC0009PC0009A000PC0010PC0010Note If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 21 | [Option 2] Create Segment and Import | In the Master Data Type Segment, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.SegmentSegment DescriptionSE0001SE0001SE0002SE0002SE0003SE0003SE0004SE0004SE0005SE0005Note If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 22 | [Option 2] Create Material and Import | In the Master Data Type Material, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.MaterialMaterial DescriptionMERCHANDIZE AMerchandize AMERCHANDIZE BMerchandize BNote If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 23 | [Option 2] Create Functional Area and Import | In the Master Data Type Functional Area, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.Functional AreaMaterial DescriptionYD20IC difference - operatingYD70IC difference - financialNote If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 24 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 25 | Maintain Foreign Exchange Rates | Open Import Foreign Exchange Rates (F2092). Choose Browse and select exchange rate [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/FX_Rate_1SG_2025_2026.xlsx) to upload. Check FX Rates status and choose Import.Note Check the exchange rates first by opening app Currency Exchange Rates (F3616). If they have already been maintained, ignore the steps, otherwise, please upload the file. | The Import Foreign Exchange Rates view is displayed. |  |
| 26 | Maintain Foreign Exchange Rates for MGC (Optional) | This step is optional and used for MGC scenario.Open Import Foreign Exchange Rates (F2092).Choose Browse and select exchange rate [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/FX_Rate_MGC_2025_2026.xlsx) to upload. Check FX Rates status and choose Import. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access Set Global Parameter | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Set Global Parameter | Set the following parameters:Version: Y10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 4 | Create Version from Reference Version | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Version from Reference Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Create Version A10 | Make the following entries:Template Version: Y10Target Version: A10Test Run: <Deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Choose Run and then Continue.Ignore the information message Documents aren´t auto-reversed in periods greater than 12. and choose Exit.Note Group Currency once defined in Create Version from Reference Version, cannot be changed anymore.Setting group currency to EUR is only for the purpose of the testing in this test script. If you want to maintain your own group currency, please use your own data setting and files instead of the ones we provide.If you have already made postings on A10 with other currencies except EUR, please create your own version for the following testing and adjust all the data files used in this test script accordingly. | Target version A10 is created successfully with template version Y10. |  |
| 6 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 7 | Set Global Parameters | Set the following parameters:Version: A10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 8 | Open Assign Process Period Cycles | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Process Period Cycles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 9 | Assign Process Period Cycles | Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 012Assignment End Year: 9999Assignment End Period: 016Press Enter and then choose Save. | Assign Process Period Cycle to version A10. |  |
| 10 | Open Define Consolidation Master Data Fields | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Consolidation Master Data Fields.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Consolidation Master Data Fields screen displays. |  |
| 11 | Define Consolidation Master Data Fields | Ensure the attributes and attribute values are configured, as listed, in the following table:Enable InputsEnable Master DataEnable Hierarchy (*)Enable Hierarchy Elimination (*)Aggregate on CarryforwardAggregate Data on ReleasePartner Company√ProfitCenter√√√√Segment√√√√FunctionalArea√√√ControllingArea√√ChartOfAccounts√√Customer√Material√√PartnerProfitCenter√√√PartnerSegment√√√GLAccount√√AssignmentReference√√√(*): optional, specific to Matrix consolidationIf necessary, select More > Edit and enter the values to align with the table.NoteIf the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again.If additional fields are not activated by default, please delete additional fields mentioned above in the data files in order to run through the test script. |  |  |
| 12 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 13 | Access the SAP Fiori App (Optional) | The below two steps are optional for Hierarchy Elimination.Open Manage Rules for Automatic Postings (F8339). |  |  |
| 14 | Update Automatic Posting Rules (Optional) | Under Rules section, select the rule S2_01_0101.Go into the detailed view of the rule and choose Edit.Select the Posting Line 2 and choose Create in Filed Assignments. Add new assignments as the below table.Table 2:FieldAssignment TypeValueApply Only IfControlling AreaValueA000Source field is filledPartner Profit CenterValue OfProfit CenterSource field is filledProfit CenterValue OfPartner Profit CenterSource field is filledPartner Segment for Segmental ReportingValue OfSegment for Segmental ReportingSource field is filledSegment for Segmental ReportingValue OfPartner Segment for Segmental ReportingSource field is filledChoose Save.Remember Repeat the above steps to update another rule S2_01_0104 of its Posting Line 5 and Posting Line 6. |  |  |
| 15 | Access the SAP Fiori App | Open Manage Reporting Rules - Configure Reporting Items (F8535). | The Manage Reporting Rules view displays. |  |
| 16 | Activate Reporting Item Hierarchies | Select the following entries and choose Go:Cons. Chart of Accounts: Y1Reporting Item Hierarchy: X1 Statement of EquityReporting Rule: Y10Choose > (Details) to go to the detailed page of the reporting item hierarchy X1.In the section of Reporting Rule Activations, check if the reporting item hierarchy has been activated. If yes, ignore the following steps. If not, choose Edit and then choose Create.Select resolution date, for example, <Today>, and then choose Save.Go back to the previous view and repeat the steps for reporting item hierarchies X2-Statement of Cash Flow, X3-Statement of Comprehensive Inc and X4-P&L by Function of Expense to activate these hierarchies. | Reporting Item Hierarchies Activated Successfully. |  |
| 17 | Maintain FS Item Mapping | From the SAP Fiori launchpad, open Map FS Items with G/L Accounts (F3333) and verify that Mapping Revisions appear in the table with Active status.If no mapping revisions appear, create mappings by downloading this [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2602_Template_Financial_Statement_Item_Mapping.xlsx). After completing the file, use the Import FS Item Mappings (F3335) SAP Fiori app to import the mappings. |  |  |
| 18 | Assign FS Item Mapping | From the SAP Fiori launchpad, open Assign FS Item Mappings (F3334) and verify that the following values appear in the Items list:Start of Assignment: 001/1900Consolidation Version: Y10 (FS item mapping version)Cons. Chart of Accounts: Y1 (Consolidation Chart of Accounts)G/L Chart of Accounts: YCOA (Standard Chart of Accounts)FS Item Mapping: Y1 (Consolidation chart of account)FS Item Mapping Revision: 1If this item is not in the table, choose New to open a dialog box, add the values, and choose Save.Use the < (Back) button to return to the SAP Fiori launchpad. |  |  |
| 19 | Define Master Data] | There are two options available for master data. You can either define master data or import master data, you do not have to do both. The following option describes defining master data for consolidation fields. If you prefer to import master data, skip to step Access the SAP Fiori App to Define Master Data. |  |  |
| 20 | [Option 1] Access the SAP Fiori App to Define Master Data | Open Define Master Data for Consolidation Fields (F3007).Select Profit Center and choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionPC0001A000PC0001PC0002A000PC0002PC0003A000PC0003PC0004A000PC0004PC0005A000PC0005PC0006A000PC0006PC0007A000PC0007PC0008A000PC0008PC0009A000PC0009PC0010A000PC0010Select < (Back) and choose Segment for Segmental Reporting and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionSE0001SE0001SE0002SE0002SE0003SE0003SE0004SE0004SE0005SE0005Select < (Back) and choose Material Number and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionMERCHANDIZE AMerchandize AMERCHANDIZE BMerchandize BSelect < (Back) and choose Functional Area and then choose Create to add the following local master data.Master DataSuperordinate FieldDescriptionYD20IC difference - operatingYD70IC difference - financialNote If the values for Consolidation Master Data Fields already exist as the above tables, you don't need to maintain them again. |  |  |
| 21 | [Option 2] Import Master Data] | The following steps are for importing master data directly. |  |  |
| 22 | [Option 2] Access the SAP Fiori App to Import Master Data | Open Import Consolidation Master Data (F3924). |  |  |
| 23 | [Option 2] Create Profit Center and Import | In the Master Data Type Profit Center, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.Controlling AreaProfit CenterProfit Center NameA000PC0001PC0001A000PC0002PC0002A000PC0003PC0003A000PC0004PC0004A000PC0005PC0005A000PC0006PC0006A000PC0007PC0007A000PC0008PC0008A000PC0009PC0009A000PC0010PC0010Note If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 24 | [Option 2] Create Segment and Import | In the Master Data Type Segment, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.SegmentSegment DescriptionSE0001SE0001SE0002SE0002SE0003SE0003SE0004SE0004SE0005SE0005Note If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 25 | [Option 2] Create Material and Import | In the Master Data Type Material, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.MaterialMaterial DescriptionMERCHANDIZE AMerchandize AMERCHANDIZE BMerchandize BNote If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 26 | [Option 2] Create Functional Area and Import | In the Master Data Type Functional Area, choose Download Template and then adjust the spreadsheet according to the following information in the table.Choose Upload. Upload the spreadsheet you just adjusted. Choose Check All and then Import All.Functional AreaMaterial DescriptionYD20IC difference - operatingYD70IC difference - financialNote If the values for Consolidation Master Data Fields already exist as the above table, you don't need to maintain them again. |  |  |
| 27 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 28 | Maintain Foreign Exchange Rates | Open Import Foreign Exchange Rates (F2092). Choose Browse and select exchange rate [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/FX_Rate_1SG_2025_2026.xlsx) to upload. Check FX Rates status and choose Import.Note Check the exchange rates first by opening app Currency Exchange Rates (F3616). If they have already been maintained, ignore the steps, otherwise, please upload the file. |  |  |
| 29 | Maintain Foreign Exchange Rates for MGC (Optional) | This step is optional and used for MGC scenario.Open Import Foreign Exchange Rates (F2092).Choose Browse and select exchange rate [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/FX_Rate_MGC_2025_2026.xlsx) to upload. Check FX Rates status and choose Import. |  |  |

The exchange rates in the file are defined as follows. You can have a double check.

|  |
| --- |
| Note The “X” in Price Quotation is meant Indirect Quotation.Please avoid maintaining the exchange rates for your currency pairs in both direction when Inverted exchange rate is already enabled for the exchange rate type.(*): additional settings used in group currency extension versions |

| Exchange rate type | Currency pair | Price quotation | 11.2025 | 12.2025 | 01.2026 | 02.2026 | 03.2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AVG | From USD => EUR | X | 1.4706 | 1.4706 | 1.3933 | 1.41 | 1.35 |
| AVG | From JPY => EUR | X |  | 152.33 | 130.23 | 132.0 | 129 |
| AVG | From CNY => EUR | X |  | 7.5 | 8.3 | 8.4 | 8.1 |
| AVG (*) | From JPY => USD | X |  | 103.584 | 93.469 | 93.617 |  |
| AVG (*) | From CNY => USD | X |  | 5.09996 | 5.95708 | 5.95746 |  |
| CLO | From USD => EUR | X | 1.3917 | 1.3917 | 1.4406 | 1.42 | 1.37 |
| CLO | From JPY => EUR | X |  | 126.14 | 133.16 | 135 | 130 |
| CLO | From CNY => EUR | X |  | 7.9 | 8.8 | 8.85 | 8.2 |
| CLO (*) | From JPY => USD | X |  | 90.637 | 92.434 | 95.07 |  |
| CLO (*) | From CNY => USD | X |  | 5.67651 | 6.10857 | 6.23239 |  |
| INC2 | From USD => EUR | X |  |  | 1.3917 |  |  |

#### Additional Settings for Multiple Group Currencies and Restatement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you complete the configuration of the following 5 versions. These settings are for testing purpose only. You can adjust according to your own needs.

- J10 – Standard version / Group Currency = EUR

The standard version is set up to consolidate all the amounts in group currency = EUR. Balance carryforward comes from J10 and J1R.

|  |
| --- |
| Note The standard version is the actual version in this case. You don't need to create it again if you have your own actual version already. |

- J1R – Extension for Restatement / Group Currency = EUR

The extension version J1R is the restatement version to the standard version J10. The local currency amounts are different from the standard version J10.

- J1S – Extension for Simulation / Group Currency = EUR

The extension version J1S is the simulation version to the standard version J10. Consolidation group structure in J1S are different from that in the standard version J10. And the local currency amounts are also different from J10.

- J20 – Group Currency Extension to J10 / Group Currency = USD

The group currency extension version J20 to the standard version J10, is set up to consolidate all the amounts in group currency = USD. Balance carryforward comes from J20 and J2R.

|  |
| --- |
| Note This is for testing purpose only. You can maintain your own group currency other than USD. |

- J2R – Extension for Restatement / Group Currency = USD

The extension version J2R is the restatement version to J20. It is equivalent to J1R but in the group currency USD.

In order to translate local currency into different group currencies, you have to define an exchange rate from each local currency toward each group currency.

Several exchange rate types will be used:

- AVG (average rate used to translate P&L and balance sheet FS items).
- CLO (closing rate used to translate the closing position of the balance sheet FS items and generate the conversion reserve and the currency translation differences).
- INC2 (exchange rate used to translate the opening balance sheet of the incoming CU MXX04 for period 001.2026).

The detailed settings for the five versions are as below. Please follow the instructions to complete the version creation.

| Consolidation version | J10 | J1R | J1S | J20 | J2R |
| --- | --- | --- | --- | --- | --- |
| Template Version | Y10 | J10 | J10 | J10 | J20 |
| Target Version | J10 | J1R | J1S | J20 | J2R |
| Description | ACT/S/ /EUR/ | ACT/R/J10/EUR/SYNC | ACT/R/J10/EUR/ASYNC | ACT/G/J10/USD/SYNC | ACT/R/J20/USD/SYNC |
| Version Type | Standard | Extension | Extension | Group Currency Extension | Extension |
| Ref. Version |  | J10 | J10 | J10 | J20 |
| Group Currency | EUR | EUR | EUR | USD | USD |
| Allow LC, TC, Qty Changes | <uncheck | <check> | <check> | <check> | <check> |
| Run Mode | Manual Run | Automatic Run | Manual Run | Automatic Run | Automatic Run |
| Preparation Ledger | 0L | 0L | 0L | 0L | 0L |
| Group Crcy Source | Global Currency | Global Currency | Global Currency | Global Currency | Global Currency |
| Fiscal Year Variant | K4 | K4 | K4 | K4 | K4 |
| Use Plan Data Integr. |  |  |  |  |  |
| Source Category |  |  |  |  |  |
| Data Entry | Y10 | Y10 | Y10 | Y10 | Y10 |
| Cons. Grp Attribute | Y10 | Y10 | Y10 | Y10 | Y10 |
| Structure | Y10 | Y10 | J1S | Y10 | Y10 |
| Cons. Unit Attribute | S10 | S10 | S10 | S10 | S10 |
| Exchange Rates | Y10 | Y10 | Y10 | Y10 | Y10 |
| Reclass. and Elimin. | Y10 | Y10 | Y10 | Y10 | Y10 |
| FS Items Attributes | S10 | S10 | S10 | S10 | S10 |
| Reporting Rules | Y10 | Y10 | Y10 | Y10 | Y10 |
| FS Group Items | Y10 | Y10 | Y10 | Y10 | Y10 |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) and choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate Close | The Configure Your Solution view is displayed. |  |
| 3 | Check Versions | Select the Basic Settings group.Select Step Define Versions and choose Configure to check whether there are versions J10, J1R, J1S, J20, J2R. If no, please run the following steps. | Consolidation Configuration Steps are filtered. |  |
| 4 | Select Reference Version | Select the Step Create Version from Reference Version, and choose Configure. |  |  |
| 5 | Create Version J10 | In Execution Parameters area, make the following entries and choose Run:Template Version: Y10Target Version: J10Test Run: <Deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Ignore the information message and choose Continue.Note For fields Version Type, Ref. Version, Group Currency, Run Mode, Allow LC, TC, Qty Changes and FY variant, once you defined them in this creating step, you cannot change them in Define Versions any more. | Target version J10 is created successfully with template version Y10. |  |
| 6 | Define Versions | Select Define Versions and choose Configure.Double click the created version J10. Make the following entries and choose Save.Consolidation version: J10 ACT/S/ /EUR/Version Type: StandardGroup Currency: EURRun Mode: Manual RunPreparation Ledger: 0LGroup Crcy Source: Global CurrencyData Entry: Y10Cons. Grp Attribute: Y10Structure: Y10Cons. Unit Attribute: S10Exchange Rates: Y10Reclass. and Elimin.: Y10FS Item Attributes: S10Reporting Rules: Y10FS Group Items: Y10For testing purpose, press Enter to ignore the warning message Documents aren´t auto-reversed in periods greater than 12. to continue.Choose Back. | Message Data was saved shows. |  |
| 7 | Create Other Versions | Repeat above steps to create Version J1R, J1S, J20, J2R. The configuration of the other 4 versions should be performed as the below table.When defining the version J1S, double-click Structure field under the Dialog Structure in the left panel.Choose New Entries and enter the following:Version: J1SDescription: Structure special version J1SChoose Save. Go back to the Change View "Define Versions": Details view and maintain the Structure for J1s as J1S.For testing purpose, choose Continue to ignore the warning message The version type you entered should be the same as on the database. when you define versions. |  |  |
| 8 | Define Balance Carryforward Settings | After you have created these five versions correctly, go back to open the SSCUI Define Balance Carryforward Settings.Choose New Entries and maintain four entries as below:Entry 1Processing Year: 2026Source Version: J1RDestination Version: J10Entry 2Processing Year: 2026Source Version: J2RDestination Version: J20 | Balance Carryforward Destination Versions are maintained. |  |
| 9 | Set Global Parameter | Go back and select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: J10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Go back to the original view. | The Global parameters log displays. |  |
| 10 | Assign Process Period Cycles | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 012Assignment End Year: 9999Assignment End Year: 016Press Enter and then choose Save. | Assign Process Period Cycle S_MTH to version J10. |  |
| 11 | Set Global Parameter | Go back and select the Basic Settings group.Select the step Set Global Parameters and choose Configure.Make the following entries as below and choose Continue:Version: J1SFiscal year: 2026Period: 01Cons. COA: Y1Choose Save.Go back to the original view. | The Global parameters log displays. |  |
| 12 | Assign Process Period Cycles | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 9999Assignment End Year: 016Press Enter and then choose Save. | Assign Process Period Cycle S_MTH to version J1S. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Versions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Versions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Version from Reference Version screen displays. |  |
| 3 | Check Versions | Check whether there are versions J10, J1R, J1S, J20, J2R. If no, please run the following steps. |  |  |
| 4 | Open Create Version from Reference Version | Go back to the original view.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Version from Reference Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Version from Reference Version screen displays. |  |
| 5 | Create Version J10 | In Execution Parameters area, make the following entries and choose Execute > Continue:Template Version: Y10Target Version: J10Test Run: <Deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <deselect>FY variant: K4Ignore the information message and choose Exit.Note For fields Version Type, Ref. Version, Group Currency, Run Mode, Allow LC, TC, Qty Changes and FY variant, once you defined them in this creating step, you cannot change them in Define Versions any more. | Target version J10 is created successfully with template version Y10. |  |
| 6 | Define Versions | Select Define Versions and choose Configure.Double click the created version J10. Make the following entries and choose Save.Consolidation version: J10 ACT/S/ /EUR/Version Type: StandardGroup Currency: EURRun Mode: Manual RunPreparation Ledger: 0LGroup Crcy Source: Global CurrencyData Entry: Y10Cons. Grp Attribute: Y10Structure: Y10Cons. Unit Attribute: S10Exchange Rates: Y10Reclass. and Elimin.: Y10FS Item Attributes: S10Reporting Rules: Y10FS Group Items: Y10For testing purpose, press Enter to ignore the warning message Documents aren´t auto-reversed in periods greater than 12. to continue.Choose Back. |  |  |
| 7 | Create Other Versions | Repeat above steps to create Version J1R, J1S, J20, J2R. The configuration of the other 4 versions should be performed as the below table.When defining the version J1S, double-click Structure field under the Dialog Structure in the left panel.Choose New Entries and enter the following:Version: J1SDescription: Structure special version J1SChoose Save. Go back to the Change View "Define Versions": Details view and maintain the Structure for J1s as J1S.For testing purpose, choose Continue to ignore the warning message The version type you entered should be the same as on the database. when you define versions. |  |  |
| 8 | Open Balance Carryforward Settings | Go back to the original view.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Balance Carryforward Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 9 | Define Balance Carryforward Settings | Choose New Entries and maintain four entries as below:Entry 1Processing Year: 2026Source Version: J1RDestination Version: J10Entry 2Processing Year: 2026Source Version: J2RDestination Version: J20 | Balance Carryforward Destination Versions are maintained. |  |
| 10 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 11 | Set Global Parameter | Make the following entries and choose Continue:Version: J10Fiscal year: 2025Period: 12Cons. COA: Y1Choose Save.Go back to the original view. | The Global parameters log displays. |  |
| 12 | Assign Process Period Cycles | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2025Assignment Start Period: 012Assignment End Year: 9999Assignment End Period: 016Press Enter and then choose Save. | Assign Process Period Cycle S_MTH to version J10. |  |
| 13 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 14 | Set Global Parameter | Make the following entries and choose Continue:Version: J1SFiscal year: 2026Period: 01Cons. COA: Y1Choose Save.Go back to the original view. | The Global parameters log displays. |  |
| 15 | Assign Process Period Cycles | Go back to the previous view.Select the step Assign Process Period Cycles and choose Configure.Choose New Entries and make the following entry:Process Period Cycle: S_MTHAssignment Start Year: 2026Assignment Start Period: 001Assignment End Year: 9999Assignment End Period: 016Press Enter and then choose Save. | Assign Process Period Cycle S_MTH to version J1S. |  |

## Overview Table

This scope item consists of several process steps, reports, or items provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Consolidation Scenario for Integrated Intercompany Matching & Reconciliation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Preparation for Integration Scenario](#unique_9) [page ] 41 | Group AccountantAdministrator - Group Reporting | Consistency Check of Accounting Integration (CX8CCI)Set Global Parameters (CXGP)Map FS Items with G/L Accounts (F3333)Manage Substitution/Validation Rules - Group Journal Entries (F4407) | The consolidation units are integrated. |
| [2025.11 Integrated Intercompany](#unique_10) [page ] 47 | General Ledger AccountantGeneral Ledger Accountant - IntercompanyGeneral Ledger Accountant - Group ReportingConfiguration Expert - Business Process Configuration | Upload General Journal Entries (F2548)Map FS Items with G/L Accounts (F3333)Schedule Jobs for Consolidation Tasks (F5572)Manage Your Solution (F1241)Set Global Parameters (CXGP)Define FS Items (F3297)Data Monitor (CXCD)Manage Journal Entries (F0717A)Consolidation Monitor - New Version (F7271) | Validation passes. |

Table 4: Consolidation Scenario Actuals_Rules Based COI

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Consolidation Units and Groups](#unique_11) [page ] 72 | Administrator - Group Reporting | Import Consolidation Master Data (F3924)Define Consolidation Groups (F7959) |  |
| [Define Hierarchies for Hierarchy Elimination (Optional)](#unique_12) [page ] 76 | General Ledger Accountant - Group Reporting | Set Global Parameters (CXGP)Manage Consolidation Hierarchies (F7995) |  |
| [Set up Group Structure](#unique_13) [page ] 79 | Administrator - Group Reporting | Set Global Parameters (CXGP)Manage Group Structure - Group View (F3733)Import Consolidation Master Data (F3924) |  |
| [2025.12 Initial Consolidation](#unique_14) [page ] 84 | Configuration Expert - Business Process ConfigurationGroup Accountant | Set Global Parameters (CXGP)Assign Rule Group for Balance Validation - Group Reporting (F8138)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.01 Full Consolidation](#unique_15) [page ] 93 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135)Group Data Analysis - With Reporting Rules (W0136) |  |
| [2026.02 Subsequent Consolidation](#unique_16) [page ] 99 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.03 Subsequent Consolidation](#unique_17) [page ] 102 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |

Table 5: Consolidation Scenario Actuals_Method Change (Rule Based COI)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Consolidation Units and Groups](#unique_18) [page ] 106 | Administrator - Group Reporting | Import Consolidation Master Data (F3924)Define Consolidation Groups (F7959) |  |
| [Set Up Group Structure](#unique_19) [page ] 109 | Administrator - Group Reporting | Set Global Parameters (CXGP)Import Consolidation Master Data (F3924) |  |
| [2025.12 Initial Consolidation](#unique_20) [page ] 112 | Configuration Expert - Business Process ConfigurationGroup Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.01 Subsequent Consolidation](#unique_21) [page ] 121 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.02 Method Change at the End of Period](#unique_22) [page ] 125 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |

Table 6: Consolidation Scenario_Multiple Group Currencies and Restatement (Optional)

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Set up Group Structure](#unique_23) [page ] 136 | Administrator - Group Reporting | Import Consolidation Master Data (F3924)Define Consolidation Groups (F7959) |  |
| [Create Consolidation Units and Groups](#unique_24) [page ] 131 | Administrator - Group Reporting | Set Global Parameters (CXGP)Import Consolidation Master Data (F3924)Manage Group Structure - Group View (F3733) |  |
| [2025.12 Initial Consolidation](#unique_25) [page ] 144 | Configuration Expert - Business Process ConfigurationGroup Accountant | Set Global Parameters (CXGP)Assign Rule Group for Balance Validation - Group Reporting (F8138)Data Monitor (CXCD)Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.01 Full Consolidation](#unique_26) [page ] 154 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |
| [2026.02 Subsequent Consolidation](#unique_27) [page ] 166 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC)Consolidation Monitor - New Version (F7271)Group Data Analysis (W0135) |  |

Table 7: Reporting

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Balance Sheet (B/S) Reports](#unique_28) [page ] 170 | Group Accountant | Group Data Analysis (W0135) | You view the balance sheet report. |
| [P&L by Nature of Expense](#unique_29) [page ] 172 | Group Accountant | Group Data Analysis (W0135) | You view the consolidated income statement report. |
| [Cash Flow Statement](#unique_30) [page ] 174 | Group Accountant | Group Data Analysis - With Reporting Rules (W0136) | You view the Cash Flow Statement report. |

Table 8: Configuration App

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Configuration Activities](#unique_31) [page ] 176 | Configure Your Solution:Configuration Expert - Business Process ConfigurationSAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration | Create Version from Reference VersionDefine VersionsSpecify Selected FS Items for Automatic PostingDefine Consolidation Master Data FieldsDefine FS Item AttributesDefine Subitem Categories and Subitems in ConsolidationDefine Reclassification Methods |  |
| [Organization Structure Creation](#unique_32) [page ] 181 | Administrator - Group Reporting | Define Consolidation Units (F4685)Define Consolidation Groups (F7959) | The assignment is maintained. |
| [Master Data Configuration with SAP Fiori UI](#unique_33) [page ] 184 | Administrator - Group Reporting | Import Consolidation Master Data (F3924)Manage Consolidation Hierarchies (F7995) | Configuration activity works. |
| [Validation](#unique_34) [page ] 188 | Administrator - Group Reporting | Manage Balance Validation Rules and Rule Groups - Group Reporting (F8001)Import/Export Current Settings - Group Reporting (F3663)Assign Rule Group for Balance Validation - Group Reporting (F8138) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Please be noted that Scope Item 1SG is step-by-step scenario, one error will lead to subsequent errors. Therefore please raise incidents to component FIN-CS-CNT immediately after you run into errors during testing 1SG. |

|  |
| --- |
| Note Please be noted that all the data files linked in this test script can only be uploaded in English. Change the Language and Region in Setting as English when you upload related data files. |

|  |
| --- |
| Note Please be noted that the latest test script published describes the test procedure based on the latest functions and configuration of the current release. It may not be perfectly fit for customers from prior releases. For those customers who are from prior releases and would like to use current test script, it is recommended that:If your initial release is lower than 1902 release, migrate your data from the old reporting logic to the new reporting logic as mentioned in Section 1.12 in Note [2659656](https://me.sap.com/notes/2659656) - FAQ About SAP S/4HANA Cloud Public Edition, group reporting or refer to the test script 1SG_TestScript_ForInitialReleaseLowerThan1902 attached to the same note.If you have already had the new group reporting applied, refer to Note [2659656](https://me.sap.com/notes/2659656) - FAQ About SAP S/4HANA Cloud Public Edition, group reporting or raise a customer ticket to migrate these new functions into your implemented solution if any have not yet been included in your solution. |

### Consolidation Scenario for Integrated Intercompany

Since the company code master data is customer dependent, confirm your available company codes in your system and pick the corresponding consolidation units.

The values in the following table are provided as examples only.

| Cons unit / company code | Description | Local Currency |
| --- | --- | --- |
| 1010 | Walldorf | EUR |
| 1710 | Palo Alto | USD |
| XX10 |  |  |

The operational chart of account is customer-dependent. G/L accounts are assigned with a group account number for testing purposes only. To verify or change more G/L accounts assignments, open the Import FS Item Mappings (F3335) SAP Fiori app and download the existing master data, data type: Financial Statement Item Mapping, mapping ID Y1.

Test cases overview

Preparation for SAP S/4HANA company's integration

- FI posting in 2025.11
- Review accounting documents to check if relevant field values are generated correctly
- Realignment to fix no-mapping FS Items
- Run data monitor 2025.11
- Release universal journal (S4 accounting)
- Upload flat file for Non-integrated company Intercompany Matching and Reconciliation data
- Validate universal journal (S4 accounting)
- Realignment to fix Breakdown Category error
- Calculate net income
- Validate reported data
- Fix through manual postings for inappropriate FS Item mapping (or any errors left)
- Run matching job
- Run reconciliation Balance Report
- Manage assignment
- Display matching items
- Close reconciliation status
- Run currency translation
- Run rest of data monitor tasks
- Lock tasks
- Run consolidation monitor 2025.11
- Run intercompany Balance Sheet elimination tasks

#### Preparation for Integration Scenario

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you set the global parameters for the integration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open app Consistency Check of Accounting Integration (CX8CCI). | The Consistency Check of Settings for FI Integration view displays. |  |
| 3 | Execute Consistency Check | Make the following entries and choose Run:Version: Y10Consolidation COA: Y1Fiscal Year : 2025Period: 11 |  |  |
| 4 | Verify Integration | Verify your assigned consolidation unit.Remember To read data from SAP S/4HANA company code data, you must solve all the missing configuration issues. And if you use SAP pre-delivered Consolidation Units, manually modify and save again to trigger the integration. Otherwise, you may get error message like No integrated consolidation unit available for company XXXX.Note You only need to verify your own assigned consolidation units. Ignore the error message of other consolidation units. | Assigned consolidation unit is integrated. |  |
| 5 | Access the SAP Fiori App | Open app Set Global Parameters (CXGP). | The Global parameters dialog box displays. |  |
| 6 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: <leave empty>Cons. Unit: <leave empty>Consolidation Version: Y10Fiscal Year and Period: 011.2025 <The period and year you are testing>Cons. COA: Y1 | The SAP Fiori launchpad displays. |  |
| 7 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 8 | Access the SAP Fiori App | Open app Define Consolidation Units (F4685). | The Define Consolidation Units view displays. |  |
| 9 | Create Units for Data Integration | In this step, you create units for Data Integration for use with the previous procedure.Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.The unit is used for accounting integration, select a company that exists in the system and type the same name for unit name.Choose Create. In the Create Consolidation Unit dialog box, enter a Consolidation Unit. Press Enter and then choose Create.In the tab General Information, input Consolidation Unit Description: <for example, Palo Alto>.In the tab Time-Dependent Attributes, input Local Currency: for example USD and Company: for example 1710 for Cons Unit 1710 and 171A.In the tab Time- and Version-Dependent Attributes, input Currency Translation Method: S0903.For Universal Journal Integration, choose Transfer from Universal Journal.Ignore the warning and choose Save. |  |  |
| 10 | Create Units for Flexible Upload | In this step, you create units for Flexible Upload for use with the previous Consolidation Scenario Actuals section.Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.To run the test, you create the following units:1010, CXXXXChoose Create and enter a Consolidation Unit. Press Enter and choose Create.In the tab General Information, input Consolidation Unit Description and Local currency (for example 1010, C1010, FC Unit, EUR).In the tab Time- and Version-Dependent Attributes, input S0904 for unit CXXXX and S0903 for 1010.Choose No integration for Universal Journal Integration.Ignore the warning and choose Save. |  |  |
| 11 | Create Consolidation Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Define Consolidation Groups (F7959).Choose Create.In the Create Consolidation Group popup, enter the ID of your consolidation group, for example, CG2.Then choose Create.In the Basic Data tab, input following entries:Consolidation Group Description: <the consolidation group you create, for example, CG2>Consolidation Group Medium Description: <the consolidation group you create, for example, CG2>Choose Save. |  |  |
| 12 | Assign Units to Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Manage Group Structure - Group View (F3733).Input one name (for example, CG2) for Consolidation group and choose Go.Choose Assign and assign the unit you created for accounting integration (for example 1710, 1010 and C1010).Input following entries:Period of First Consolidation: 011Year of First Consolidation: 2025Period of Divestiture: 999Year of Divestiture: 9999Consolidation Method: 10Choose Assign. |  |  |
| 13 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 14 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 15 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Version: Y10Task: S1080Valid From: 2025011Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group SBV_RG1.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 16 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Version: Y10Task: S2980Valid From: 2025011Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 17 | Maintain FS Item mappings | Open Map FS Items with G/L Accounts (F3333).Filter Mapping ID Y1 and Revision 1 and choose Go. Choose > (Details) of the selected mapping revision.Click Edit and find mapping item of G/L Accounts 33000000 and modify the mapping as below:G/L Account: 33000000FS Item: 311000Choose Save.Note This modification is only for test purpose. | FS item mapping assignment is changed. |  |
| 18 | Access the SAP Fiori App | Open App Manage Substitution/Validation Rules - Group Journal Entries (F4407). |  |  |
| 19 | Create Substitution Rule | Choose Create Rule button and create new substitution rule to map Company 1710, Segment 1000_A to Consolidation Unit 171A.Business Context: GRPL core fieldsEvent: GRPL core fieldsRule Type: Substitution RuleChoose Create. |  |  |
| 20 | Create Rule Details | Enter detailed information of Substitution Rule:In General InformationRule Name: for example Z_SUB_CU_171ADescription: for example Flexible mapping company to CU_171AIn PreconditionCompany equal to 1710Segment equal to 1000_AIn SubstitutionConsolidationUnit substitute with Constant 171AOverwrite: <select>Choose Save and Activate. | Company 1710 with Segment 1000_A is mapped to Cons Unit 171A. |  |
| 21 | Repeat to Create Substitution Rule | Repeat previous two steps to create substitution rule to map Company 1710, Segment 1000_C to Consolidation Unit 1710 with detailed information:In General InformationRule Name: for example Z_SUB_CU_1710Description: for example Flexible mapping company to CU 1710In PreconditionCompany equal to 1710Segment equal to 1000_CIn SubstitutionConsolidationUnit substitute with Constant 1710Overwrite: <select>Choose Save and Activate. |  |  |
| 22 | Create Substitution Rule | Choose Create Rule button and create new substitution rule to map Partner Company 1010 with Detailed information.Business Context: GRPL subassignments to FS itemEvent: GRPL subassignments to FS itemRule Type: Substitution RuleChoose Create. |  |  |
| 23 | Create Rule Details | In General InformationRule Name: for example, Z_SUB_PC_1010Description: for example, Flexible mapping company to PU 1010In PreconditionPartnerCompany equal to 1010In SubstitutionPartnerConsolidationUnit substitute with Constant 1010Overwrite: <select>Choose Save and Activate. |  |  |

#### 2025.11 Integrated Intercompany

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the data monitor for SAP S/4HANA Cloud Private Edition companies.

|  |
| --- |
| Caution Sample values for master data values are country/region-specific and the values provided in the following table are for DE. Substitute the country/region-specific values provided by the SAP Best Practices or use master data values you have created for this purpose. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Download Journal Entry Template | Download the [Journal Entry Template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Journal_Entry_Template_XXXX_PU1010.xlsx).Open the file and update the values as follows:Company Code (4): For example, 1710Journal Entry Type (2): For example, ABJournal Entry Date 11/21/2025Posting Date: For example, : For example, 11/21/2025Fiscal Period (2): For example, 11Transaction Currency (5): For example, USDCost Center (10): For example,: For example, 17101101and save the file locally.Note Replace XXXX with the assigned company code. Replace the first four digits of the cost center XXXX1101 with the assigned company code.Please note that the same field entry is required in more than one spread sheet cell.Note This data is for example. If you use other S/4 company in your testing, please ensure the transaction currency entered here is different from the company’s local currency. | A new journal entry file is created and saved locally. |  |
| 2 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 3 | Access the SAP Fiori App | Open Upload General Journal Entries (F2548). | The Upload General Journal Entries view displays. |  |
| 4 | Upload Template | Browse to the location of the template file and choose Open on the dialog box to upload the file. | A notification appears and a table of Items displays. |  |
| 5 | Post FI Documents | To post the spreadsheet content, select all items displayed and choose Post from the bottom of the view.Confirm the dialog box by choosing OK.Make a note of the journal entry numbers.Note Ignore the warning message Posting takes place in the previous year.To view the log, choose the Show Log button at the bottom of the table, and then navigate to the list of messages.If there are error messages regarding missing master data such as Cost Center, Profit Center, etc., please create relevant master data and post again. Or you can replace the missing master data with the ones which are in use. | The entries are posted. |  |
| 6 | Verify Documents | Click on Document and verify that data was posted correctly.Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code: For example, 1710Fiscal Year: For example, 2025Fiscal Period: For example, 11Choose the > button of the documents you uploaded.Select Line Items section and then in the Ledger View, choose 0L (Ledger 0L) in the dropdown list.Click Settings button and choose Columns Consolidation Financial Statement Item and Consolidation Unit.Check if Consolidation Financial Statement Item and Consolidation Unit have been correctly generated. | Consolidation Financial Statement Item contains value &NOMAPBS. |  |
| 7 | Log On | To fix the error of containing value &NOMAPBS in Consolidation Financial Statement Item, log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 8 | Repair Missing Mappings | Open Map FS Items with G/L Accounts (F3333).Enter entries Mapping ID Y1 and Revision 1. Choose Go.Choose > of the corresponding revision. Choose Edit on the upper right side of the view and create new mapping item by clicking + button with below values:G/L Accounts: 12401100FS Item: 121100And choose Save. | New mapping item is created. |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 10 | Realignment | Open Schedule Jobs for Consolidation Tasks (F5572).Choose Create.Template selectionJob Template: Realign Group Reporting Preparation LedgerChoose Step 2.Check Start Immediately.Choose Step 3.Organizational UnitsConsolidation Unit: 1710Version/Time PeriodVersion: Y10Fiscal Year: 2025Period: 11Technical SettingsCheck Periodic Mode, Log.Choose Schedule.Note Please ensure that all posting periods are open for the test period you test. |  |  |
| 11 | View Realignment Log | Choose the log line item and check the results. | Job runs successfully or without errors. |  |
| 12 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 13 | Check Realignment Results | Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code: For example, 1710Fiscal Year: For example, 2025Fiscal Period: For example, 11Reference Document Type: For example, GRRFPChoose the > button of the documents Realignment generated.Under Ledger View, choose Settings button and choose Columns Consolidation Financial Statement Item.Check if Consolidation Financial Statement Item has been correctly updated. | Consolidation Financial Statement Item &NOMAPBS has been replaced with correct Consolidation Financial Statement Item. |  |
| 14 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 15 | Access the SAP Fiori App | Open App Manage Your Solution (F1241). |  |  |
| 16 | Select the Relevant App | Navigate to Configure Your Solution.Maintain the following entries:Application Area: FinanceSub Application Area: Corporate Close |  |  |
| 17 | Set Global Parameters | In the filter result, choose Basic Settings. Choose Configure of the activity Set Global Parameters.Make the following entries and choose Continue:Cons. Group: <consolidation group you use, for example CG2>Cons. Unit: <4 digit consolidation unit number assigned to you>Version: Y10Fiscal Year: 2025Period: 11Cons. COA: Y1 |  |  |
| 18 | Assign Task Group to Version | Go back and in the Data Processing item, choose Configure of the activity Assign Task Group to Version.Assign the cons monitor task group S24 by creating a new entry. Choose New Entries.On the New Entries: Overview of Added Entries view, make the following entries and choose Save:Start Year: 2025Period eff: 1Period cat.: 9Data mon. task group: SD1Cons mon. task group: S24 |  |  |
| 19 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. |  |  |
| 20 | Maintain Offsetting Target of FS Item | Open Define FS Items (F3297) .Enter the following entry and choose Go.Financial Statement Item: 111100Select > (Details) for the item and go to Attributes for Processing tab. Check if the FS item 221100 is maintained in the Offsetting Target attribute. If yes, ignore the following entry.If not, please choose Edit. Enter the following entry and choose Save:Offsetting Target: 221100 (Borrowing,C)Choose < to go back to the previous view. Search the FS item 213000 and repeat the above the step. Check if the Offsetting Target of 213000 is maintained as 123200 (Oth Assets,C), if yes, ignore the step; if not, please enter the entry. | The Offsetting Target attributes are maintained. |  |
| 21 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 22 | Access the SAP Fiori App | Open Data Monitor (CXCD) . | The Data Monitor view displays. |  |
| 23 | Open Period | Select your consolidation group and choose More > Edit > Open period.Note If your group is already open, you can skip this step. |  |  |
| 24 | Data Monitor-Release Universal Journal | In the Release Universal Journal task, select your consolidation group and choose Test Run in the toolbar.Review the lines for your consolidation group and review the data list (already submitted and pending delta for submission) or delta mode (pending delta for submission) using the left or right buttons.Choose < (Back) and repeat this step.In the Release Universal Journal task, select your consolidation group and choose Update Run in the toolbar.Choose the button Release Universal Documents on the upper left of the screen to continue with release of SAP S/4HANA Cloud Public Edition Accounting data. On the Release of Universal Documents for Consolidation dialog box, choose Continue. | The timestamp is updated.The system displays a green status update. |  |
| 25 | Data Monitor - Data Collection | In the Data Coll. - Milestone:Data Collection task, select the cell of your consolidation group and choose Update Run in the toolbar.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/Upload_2025_11_CG2_CUXXXX_PU1710.xlsx).Replace XXXX with your assigned consolidation unit and save locally.Choose Browse to upload the edited file.File: UPLOAD_2025_11_CG2_CUXXXX_PU1710Choose Import. | Check the notification on the upper right. There is message Import of reported Data has finished. |  |
| 26 | Data Monitor - LI Validation in Grp.Reporting | In the LIV GR column, select the cell of your consolidation group and choose Update Run, or right-click the item and choose Update. | Error message will pop up:Item 311000: Subitem 920 is not in maximum selection S-BC-TT-03 |  |
| 27 | Repair Error by Modifying Mappings | To fix the error of Line Item Validation, log on to the SAP Fiori launchpad as an Administrator - Group Reporting.Open Map FS Items with G/L Accounts (F3333).Filter the entries Mapping ID Y1 and Revision 1 and choose Go. Choose of the selected entry. Choose Edit and find mapping item of G/L Accounts 33000000 and modify the mapping as below:G/L Accounts: 33000000FS Item: 316000Choose Save. | Mapping item is modified. |  |
| 28 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 29 | Realignment | Open Schedule Jobs for Consolidation Tasks (F5572).Choose Create.Template selectionJob Template: Realign Group Reporting Preparation LedgerChoose Step 2.Check Start Immediately.Choose Step 3.Organizational UnitsConsolidation Unit: 1710Version/Time PeriodVersion: Y10Fiscal Year: 2025Period: 11Technical SettingsCheck Periodic Mode, Log.Choose Schedule.Note Please ensure that all posting periods are open for the test period you test. |  |  |
| 30 | View Realignment Log | Choose the log line item and check the results. | Job runs successfully or without errors. |  |
| 31 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 32 | Check Realignment Results | Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code (4): For example, 1710Fiscal Year(4): For Example, 2025Periods(2): For example, 11Reference Document Type: For example, GRRFPChoose the documents Realignment generated.Under Ledger View, choose Settings button and choose Columns Consolidation Financial Statement Item.Check if Consolidation Financial Statement Item has been correctly updated. | G/L account 33000000 has been mapped with Cons. FS Item 316000. |  |
| 33 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 34 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 35 | Data Monitor-Release Universal Journal | In the Release Universal Journal task, select your consolidation group and choose Test Run in the toolbar.Review the line for your consolidation unit and review the data list (already submitted and pending delta for submission) or delta mode (pending delta for submission) using the left or right buttons.Choose < (Back) and repeat this step. Right-click Release Universal Journal and choose Update Run.Choose the button Release Universal Documents on the upper left of the screen to continue with release of SAP S/4HANA Cloud Public Edition Accounting data. On the Release of Universal Documents for Consolidation dialog box, choose Continue. | The timestamp is updated.The system displays a green status update. |  |
| 36 | Data Monitor - LI Validation in Grp.Reporting | In the LIV GR column, select the cell for your item and choose Update Run, or right-click the item and choose Update. | Line validation on group reporting data after releasing universal journal has no error. |  |
| 37 | Sign Based Reclassification (Optional) | In the Sign RCL column, select the cell for your item and choose Update Run.Note If G/L account balance is not at the correct credit/debit side, this enables you to reclassify FS item to the expected asset or liability FS item.Note Currently, the reclassification work when G/L account is assigned to only one FS item. | The G/L account balance is reclassified to the correct side of the target FS item. |  |
| 38 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 39 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | Expect errors:Validation rule SB00008:Transfer flow (950) must balance failed |  |
| 40 | Correct Validation Errors Using PL0C | You can manually correct using manual postings in Posting level PL0C instead of modifying original journal entries.Open Import Group Journal Entries (F3073) app.Download the [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/XXXX_Y10_MJE_2025_11_PL_0C.xlsx) and verify that the template has the same settings before you run the upload.Replace the XXXX with your assigned consolidation unit and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post.Note You could also fix this validation error by modifying transaction type in journal entries and release universal journals again, then you don’t need to proceed the following 3 steps.Note Please be noted, that this case could also apply to the case that certain validation error needs to be corrected. |  |  |
| 41 | Data Monitor - LI Validation in Grp.Reporting | In the LIV GR column, select the cell for your item and choose Update Run. | Line validation on group reporting data after releasing universal journal has no error. |  |
| 42 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 43 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 44 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 45 | Open Reconciliation Period | Open the Fiori app Manage Reconciliation Close (F4774).Enter the parameters as follows, then choose Go:Reconciliation Case: SGR01Period/Year: <current period/year and the period/year that you are testing>Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1710)>Partner Unit: <the units that you use in testing (for example 1010)>Click Open Period button to open period for the unit that you use. |  |  |
| 46 | Access the SAP Fiori App | Open Reconciliation Status Overview (F3865). |  |  |
| 47 | Display Reconciliation Report | To go to Reconciliation Balances view, make the following entries and choose Go:Reconciliation Case: SGR01Consolidation Unit: <the units that you use in testing (for example 1710)>Period/Year: 011/2025Consolidation Version: Y10Consolidation COA Y1Hover over the Reconciliation status bar to show the detail of how many partner companies are reconciled, reconciled within tolerance or not reconciled.If new documents are posted, the New Postings column shows Detected.You can choose button Netting View: to view the report based on paired display groups. | Initial reconciliation status of selected company is displayed. |  |
| 48 | On the Fly Translation | In the dropdown list, choose your created converted measure to see the on the fly translation. |  |  |
| 49 | Manage Assignments | On the upper right above the chart, choose TSL (Amount in Transaction Currency) or HSL (Amnt in Company Code Crcy) or KSL (Amnt in Global Currency). Here, for example, we choose TSL (Amount in Transaction Currency).To manage assignments, choose the right arrow button > for a reconciliation balance line item.Choose Show Filter Bar on the upper right of the screen.The parameters are set as follows :Reconciliation Case: SGR01Display Group: All IC Accounts AR/APCons. Unit: <the units that you use in testing (for example 1710)>Period/Year: 011/2025Amount/Quantity Field: <keep current value, for example, TSL for transaction currency>Consolidation Version: Y10Consolidation COA: Y1Partner Unit: <the partner units that you use in testing (for example 1010)>Choose Go.In the Manage Assignments view, choose Auto Match to automatically assign reason codes.Manually reassign if needed. For example, select assignment reference 202030 and choose Assign.Enter Reason CodeS00 and Comment.Choose Assign. | Details of reconciliation results are displayed. |  |
| 50 | Manage Assignments -Display Assigned Items | All the assigned items (by rule or by manual) are displayed in the lower part of the screen.From the Change Layout drop down menu, choose Lower Area Only mode. From the left filter bar, switch the filter to display the different group of assignments.Select a line and choose the right arrow button > to display more details.Choose the rule link on the upper left of the screen to check the detail.Choose Back. Optionally, you can remove the assignment by selecting the assignment and choosing Unassign. | Details of assigned items are displayed |  |
| 51 | Manage Assignment -Manual Assign Documents | From the unassigned documents display, select documents to manually assign, then choose Assign. | Documents are manually assigned. |  |
| 52 | Display Matching Items | Choose Back.Right click an amount (for example Leading Unit Amount). Choose Show Matching Items. | Matching items are displayed properly. |  |
| 53 | Close Reconciliation Status | In Fiori app Manage Reconciliation Close (F4774),Enter the parameters as follows, then choose Go.Reconciliation Case: SGR01Period/Year: 011/2025Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1710)>Partner Unit: <the units that you use in testing (for example 1010)>Close reconciliation status for the items with Open status under the unit that you use. |  |  |
| 54 | Repeat Reconciliation Status Display | Repeat 44-52 steps by using following parameters.Note When open reconciliation period, use the current period/year that you are testing.Reconciliation Case: SGR03Period/Year: 011/2025Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1010)>Partner Unit: <the units that you use in testing (for example 1710)> |  |  |
| 55 | Post Manual Journals to Use Specific Exchange Rate for Consolidation Unit | You can manually post manual postings in Posting level PL10 to use specific exchange rate for Consolidation Unit during Currency Translation run.Log on to the SAP Fiori launchpad as a General Ledger Accountant - Group Reporting.Open Import Group Journal Entries (F3073) app.Download the [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_MJE_CT_Template.xlsx) and verify that the template has the same settings before you run the upload.Replace the CXXXX with your assigned consolidation unit and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post. |  |  |
| 56 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 57 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 58 | Data Monitor - Currency Translation | In the CurrTrans. column, select the cell for your item and choose Update Run.The task status is Not applicable for the cons units where Local Currency = Global Currency. | More lines with posting level blank and translation indicator 1 and 4 are created based on amount in LC and rules in currency translation method. |  |
| 59 | Data Monitor - Validation for Standardized Data | This task does not require execution. | No expected result. |  |
| 60 | Block Tasks in Data Monitor | Block each task by choosing the Block button. |  |  |
| 61 | Access the SAP Fiori App | Return to the Home view and open Consolidation Monitor - New Version (F7271). |  |  |
| 62 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: Y10Consolidation Group: CG2Process Year Period: 011/2025Select tasks S022 (IC Elim Other Inc/Exp) and 2042 (IC Elim Balance Sheet) for your testing cons group CG2, and then choose Actions > Update Run.Choose Go to refresh the page to verify the result.Choose > to check the task logs.Note S2980 task is not required to run. If you want to run this validation task, there may be error message since in the testing environment, some GL accounts may not be mapped. | The two tasks finish successfully.You can check the status of each task and choose > to check each task log. |  |
| 63 | Block Consolidation Monitor | In the Consolidation Monitor view, select all the tasks and choose Actions > Block on Request to block all the tasks. |  |  |
| 64 | Consolidation Monitor Exit | Choose < to exit. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Download Journal Entry Template | Download the [Journal Entry Template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Journal_Entry_Template_XXXX_PU1010.xlsx).Open the file and update the values as follows:Company Code (4): For example, 1710Journal Entry Type (2): For example, ABJournal Entry Date: For example, 11/21/2025Posting Date: For example, 11/21/2025Fiscal Period (2): For example, 11Transaction Currency (5): For example, EURCost Center (10): For example, 17101101and save the file locally.Note Replace XXXX with the assigned company code. Replace the first four digits of the cost center XXXX1101 with the assigned company code.Please note that the same field entry is required in more than one spread sheet cell.Note This data is for example. If you use other S/4 company in your testing, please ensure the transaction currency entered here is different from the company’s local currency. | A new journal entry file is created and saved locally. |  |
| 2 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 3 | Access the SAP Fiori App | Open Upload General Journal Entries (F2548). | The Upload General Journal Entries view displays. |  |
| 4 | Upload Template | Browse to the location of the template file and choose Open on the dialog box to upload the file. | A notification appears and a table of Items displays. |  |
| 5 | Post FI Documents | To post the spreadsheet content, select all items displayed and choose Post from the bottom of the view.Confirm the dialog box by choosing OK.Make a note of the journal entry numbers.Note Ignore the warning message Fiscal Year: For example, 2025.To view the log, choose the Show Log button at the bottom of the table, and then navigate to the list of messages.If there are error messages regarding missing master data such as Cost Center, Profit Center, etc., please create relevant master data and post again. Or you can replace the missing master data with the ones which are in use. | The entries are posted. |  |
| 6 | Verify Documents | Click on Document and verify that data was posted correctly.Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code: For example, 1710Fiscal Year: For example, 2025Fiscal Period: For example, 11Choose the > button of the documents you uploaded.Select Line Items section and then in the Ledger View, choose 0L (Ledger 0L) in the dropdown list.Click Settings button and choose Columns Consolidation Financial Statement Item and Consolidation Unit.Check if Consolidation Financial Statement Item and Consolidation Unit have been correctly generated. | Consolidation Financial Statement Item contains value &NOMAPBS. |  |
| 7 | Repair Missing Mappings | To fix the error of containing value &NOMAPBS in Consolidation Financial Statement Item, log on to the SAP Fiori launchpad as an Administrator - Group Reporting.Open Map FS Items with G/L Accounts (F3333).Enter entries Mapping ID Y1 and Revision 1. Choose Go.Choose > of the corresponding revision. Choose Edit on the upper right side of the view and create new mapping item by clicking + button with below values:G/L Accounts: 12401100FS Item: 121100And choose Save. | New mapping item is created. |  |
| 8 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 9 | Realignment | Open Schedule Jobs for Consolidation Tasks (F5572).Choose Create.Template selectionJob Template: Realign Group Reporting Preparation LedgerChoose Step 2.Check Start Immediately.Choose Step 3.Organizational UnitsConsolidation Unit: 1710Version/Time PeriodVersion: Y10Fiscal Year: 2025Period: 11Technical SettingsCheck Periodic Mode, Log.Choose Schedule.Note please ensure that all posting periods are open for the test period you test. |  |  |
| 10 | View Realignment Log | Choose the log line item and check the results. | Job runs successfully or without errors. |  |
| 11 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 12 | Check Realignment Results | Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code: For example, 1710Fiscal Year: For example, 2025Fiscal Period: For example, 11Reference Document Type: For example, GRRFPChoose the > button of the documents Realignment generated.Under Ledger View, choose Settings button and choose Columns Consolidation Financial Statement Item.Check if Consolidation Financial Statement Item has been correctly updated. | Consolidation Financial Statement Item &NOMAPBS has been replaced with correct Consolidation Financial Statement Item. |  |
| 13 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 14 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Task Group to Version screen displays. |  |
| 15 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: <consolidation group you use, for example CG2>Cons. Unit: <4 digit consolidation unit number assigned to you>Version: Y10Fiscal Year: 2025Period: 11Cons. COA: Y1 | The dialog box closes and the Home view of the SAP Fiori launchpad displays. |  |
| 16 | Open Assign Task Group to Version | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Task Group to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Task Group to Version screen displays. |  |
| 17 | Assign Monitor Task Groups | Assign the cons monitor task group S24 by creating a new entry. Choose New Entries.On the New Entries: Overview of Added Entries view, make the following entries and choose Save:Start Year: 2025Period eff: 1Period cat.: 9Data mon. task group: SD1Cons mon. task group: S24 |  |  |
| 18 | Log on | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | A Global parameters dialog box displays. |  |
| 19 | Maintain Offsetting Target of FS Item | Open Define FS Items (F3297) .Enter the following entry and choose Go.Financial Statement Item: 111100Select > (Details) for the item and go to Attributes for Processing tab. Check if the FS item 221100 is maintained in the Offsetting Target attribute. If yes, ignore the following entry.If not, please choose Edit. Enter the following entry and choose Save:Offsetting Target: 221100 (Borrowing,C)Choose < to go back to the previous view. Search the FS item 213000 and repeat the above the step. Check if the Offsetting Target of 213000 is maintained as 123200 (Oth Assets,C), if yes, ignore the step; if not, please enter the entry. | The Offsetting Target attributes are maintained. |  |
| 20 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | A Global parameters dialog box displays. |  |
| 21 | Access the SAP Fiori App | Open Data Monitor (CXCD) . | The Data Monitor view displays. |  |
| 22 | Open the Period | Select your consolidation group and choose More > Edit > Open period.Note If your group is already open, you can skip this step. | The system displays the Period 011/2025 for CGXX/ XXXX opened notification. |  |
| 23 | Data Monitor-Release Universal Journal | In the Release Universal Journal column, select the cell of your consolidation group and choose Test Run.Review the lines of your consolidation group and review the data list (already submitted and pending delta for submission) or delta mode (pending delta for submission) using the left or right buttons.Choose < (Back) and repeat this step. Select Release Universal Journal and choose Update Run button.Choose the button Release Universal Documents on the upper left of the screen to continue with release of SAP S/4HANA Cloud Public Edition Accounting data. On the Release of Universal Documents for Consolidation dialog box, choose Continue. | The timestamp is updated.The system displays a green status update. |  |
| 24 | Data Monitor - Data Collection | In the Data Coll. - Milestone:Data Collection task, select the cell of your consolidation group and choose Update Run in the toolbar.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/Upload_2025_11_CG2_CUXXXX_PU1710.xlsx).Replace XXXX with your assigned consolidation unit and save locally.Choose Browse to upload the edited file.File: UPLOAD_2025_11_CG2_CUXXXX_PU1710Choose Import. | Check the notification on the upper right. There is message Import of reported Data has finished. |  |
| 25 | Data Monitor - LI Validation in Grp.Reporting | In the LIV GR column, select the cell for your consolidation group and choose Update Run, or right-click the item and choose Update. | Error message will pop up:Item 311000: Subitem 920 is not in maximum selection S-BC-TT-03 |  |
| 26 | Repair Error by Modifying Mappings | To fix the error of Line Item Validation, log on to the SAP Fiori launchpad as an Administrator - Group Reporting.Open Map FS Items with G/L Accounts (F3333).Choose Mapping ID Y1 and Revision 1. Choose Edit and find mapping item of G/L Accounts 33000000 and modify the mapping as below:G/L Accounts: 33000000FS Item: 316000And choose Save. | Mapping item is modified. |  |
| 27 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | A Global parameters dialog box displays. |  |
| 28 | Realignment | Open Schedule Jobs for Consolidation Tasks (F5572).Choose Create.Template selectionJob Template: Realign Group Reporting Preparation LedgerChoose Step 2.Check Start Immediately.Choose Step 3.Organizational UnitsConsolidation Unit: 1710Version/Time PeriodVersion: Y10Fiscal Year: 2025Period: 11Technical SettingsCheck Periodic Mode, Log.Choose Schedule.Note please ensure that all posting periods are open for the test period you test. |  |  |
| 29 | View Realignment Log | Choose the log line item and check the results. | Job runs successfully or without errors. |  |
| 30 | Access the SAP Fiori App | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | A Global parameters dialog box displays. |  |
| 31 | Check Realignment Results | Open Manage Journal Entries - New Version （F0717A) and update the values as follows:Company Code (4): For example, 1710Fiscal Year(4): For Example, 2025Periods(2): For example, 11Reference Document Type: For example, GRRFPChoose the documents Realignment generated.Under Ledger View, choose Settings button and choose Columns Consolidation Financial Statement Item.Check if Consolidation Financial Statement Item has been correctly updated. | G/L account 33000000 has been mapped with Cons. FS Item 316000. |  |
| 32 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | A Global parameters dialog box displays. |  |
| 33 | Access the SAP Fiori App | Open Data Monitor (CXCD). | The Data Monitor view displays. |  |
| 34 | Data Monitor-Release Universal Journal | In the Release Universal Journal column, select the cell of your consolidation group and choose Test Run.Review the line for your consolidation unit and review the data list (already submitted and pending delta for submission) or delta mode (pending delta for submission) using the left or right buttons.Choose < (Back) and repeat this step.In the Release Universal Journal column, select the cell of your consolidation group and choose Update Run.Choose the button Release Universal Documents on the upper left of the screen to continue with release of SAP S/4HANA Cloud Public Edition Accounting data. On the Release of Universal Documents for Consolidation dialog box, choose Continue. | The timestamp is updated.The system displays a green status update. |  |
| 35 | Data Monitor - LI Validation in Grp.Reporting | In the Data Monitor view, select your cons group of the task LIV GR and choose Update Run from the toolbar. | Line validation on group reporting data after releasing universal journal has no error. |  |
| 36 | Sign Based Reclassification (Optional) | In the Sign RCL column, select the cell for your item and choose Update Run, or right-click the item and choose Update.Note If G/L account balance is not at the correct credit/debit side, this enables you to reclassify FS item to the expected asset or liability FS item.Note Currently, the reclassification work when G/L account is assigned to only one FS item. | The G/L account balance is reclassified to the correct side of the target FS item. |  |
| 37 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 38 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | Expect errors:Validation rule SB00008:Transfer flow (950) must balance failed |  |
| 39 | Correct Validation Errors using PL0C | You can manually correct using manual postings in Posting level PL0C instead of modifying original journal entries.Open Import Group Journal Entries (F3073) app.Download the [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/XXXX_Y10_MJE_2025_11_PL_0C.xlsx) and verify that the template has the same settings before you run the upload.Replace the XXXX with your assigned consolidation unit and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post.Note You could also fix this validation error by modifying transaction type in journal entries and release universal journals again, then you don’t need to proceed the following 3 steps.Note Please be noted, that this case could also apply to the case that certain validation error needs to be corrected. |  |  |
| 40 | Data Monitor - LI Validation in Grp.Reporting | In the Data Monitor view, select your cons group of the task LIV GR and choose Update Run from the toolbar. | Line validation on group reporting data after releasing universal journal has no error. |  |
| 41 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 42 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 43 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant - Intercompany. |  |  |
| 44 | Open Reconciliation Period | Open the Fiori app Manage Reconciliation Close (F4774).Enter the parameters as follows, then choose Go:Reconciliation Case: SGR01Period/Year: <current period/year and the period/year that you are testing>Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1710)>Partner Unit: <the units that you use in testing (for example 1010)>Click Open Period button to open period for the unit that you use. |  |  |
| 45 | Access the SAP Fiori App | Open Reconciliation Status Overview (F3865). |  |  |
| 46 | Display Reconciliation Report | To go to Reconciliation Balances view, make the following entries and choose Go:Reconciliation Case: SGR01Consolidation Unit: <the units that you use in testing (for example 1710)>Period/Year: 011/2025Consolidation Version: Y10Consolidation COA: Y1Hover over the Reconciliation status bar to show the detail of how many partner companies are reconciled, reconciled within tolerance or not reconciled.If new documents are posted, the New Postings column shows Detected.You can choose button Netting View to view the report based on paired display groups. | Initial reconciliation status of selected company is displayed. |  |
| 47 | On the Fly Translation | In the dropdown list, choose your created converted measure to see the on the fly translation. |  |  |
| 48 | Manage Assignments | On the upper right above the chart, choose TSL (Amount in Transaction Currency) or HSL (Amnt in Company Code Crcy) or KSL (Amnt in Global Currency). Here, for example, we choose TSL (Amount in Transaction Currency).To manage assignments, choose the right arrow button > for a reconciliation balance line item.Choose Show Filter Bar on the upper right of the screen.The parameters are set as follows :Reconciliation Case: SGR01Display Group: All IC Accounts AR/APCons. Unit: <the units that you use in testing (for example 1710)>Period/Year: 011/2025Amount/Quantity Field: <keep current value, for example, TSL for transaction currency>Consolidation Version: Y10Consolidation COA: Y1Partner Unit: <the partner units that you use in testing (for example 1010)>Choose Go.In the Manage Assignments view, choose Auto Match to automatically assign reason codes.Manually reassign if needed. For example, select assignment reference 202030 and choose Assign.Enter Reason CodeS00 and Comment.Choose Assign. | Details of reconciliation results are displayed. |  |
| 49 | Manage Assignments -Display Assigned Items | All the assigned items (by rule or by manual) are displayed in the lower part of the screen.From the Change Layout drop down menu, choose Lower Area Only mode. From the left filter bar, switch the filter to display the different group of assignments.Select a line and choose the right arrow button > to display more details.Choose the rule link on the upper left of the screen to check the detail.Choose Back. Optionally, you can remove the assignment by selecting the assignment and choosing Unassign. | Details of assigned items are displayed |  |
| 50 | Manage Assignment -Manual Assign Documents | From the unassigned documents display, select documents to manually assign, then choose Assign. | Documents are manually assigned. |  |
| 51 | Display Matching Items | Choose Back.Right click an amount (for example Leading Unit Amount). Choose Show Matching Items. | Matching items are displayed properly. |  |
| 52 | Close Reconciliation Status | In Fiori app Manage Reconciliation Close (F4774),Enter the parameters as follows, then choose Go.Reconciliation Case: SGR01Period/Year: 011/2025Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1710)>Partner Unit: <the units that you use in testing (for example 1010)>Close reconciliation status for the items with Open status under the unit that you use. |  |  |
| 53 | Repeat Reconciliation Status Display | Repeat 44-52 steps by using following parameters:Note When open reconciliation period, use the current period/year that you are testing.Reconciliation Case: SGR03Period/Year: 011/2025Consolidation Version: Y10Consolidation COA: Y1Consolidation Unit: <the units that you use in testing (for example 1010)>Partner Unit: <the units that you use in testing (for example 1710)> |  |  |
| 54 | Post Manual Journals to Use Specific Exchange Rate for Consolidation Unit | You can manually post manual postings in Posting level PL10 to use specific exchange rate for Consolidation Unit during Currency Translation run.Log on to the SAP Fiori launchpad as a General Ledger Accountant - Group Reporting.Open Import Group Journal Entries (F3073) app.Download the [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_MJE_CT_Template.xlsx) and verify that the template has the same settings before you run the upload.Replace the CXXXX with your assigned consolidation unit and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post. |  |  |
| 55 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 56 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 57 | Data Monitor - Currency Translation | In the CurrTrans. column, select the cell for your item and choose Update Run.The task status is Not applicable for the cons units where Local Currency = Global Currency. | More lines with posting level blank and translation indicator 1 and 4 are created based on amount in LC and rules in currency translation method. |  |
| 58 | Data Monitor - Standardized Data Validation | This task does not require execution. | No expected result. |  |
| 59 | Block Tasks in Data Monitor | Block each task by choosing the Block button. |  |  |
| 60 | Access the SAP Fiori App | Return to the Home view and open Consolidation Monitor - New Version (F7271). |  |  |
| 61 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: Y10Consolidation Group: CG2Process Year Period: 011/2025Select tasks S022 (IC Elim Other Inc/Exp) and 2042 (IC Elim Balance Sheet) for your testing cons group CG2, and then choose Actions > Update Run.Choose Go to refresh the page to verify the result.Choose > to check the task logs.Note S2980 task is not required to run. If you want to run this validation task, there may be error message since in the testing environment, some GL accounts may not be mapped. | The two tasks finish successfully.You can check the status of each task and choose > to check each task log. |  |
| 62 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 63 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |

### Consolidation Scenario Actuals_Rule Based COI

The following table displays the codification of the consolidation groups and consolidation units per tester.

You need to adjust the IDs of the consolidation group/consolidation units/partner units provided in the file to your own IDs (XX= assigned number). Please use the detailed information in [Set up Group Structure](#unique_13) [page ] 79.

Table 9: Consolidation Scenario Actuals_Rule Based COI

| Cons. Group | Consunit | LC | % of share | Period / Year of First Consolidation | Period/year of Divestiture | Method CoI |
| --- | --- | --- | --- | --- | --- | --- |
| CGRXX | MXX00 | EUR | - | 12/2025 | 99/9999 | Parent |
|  | MXX02 | EUR | 80% | 12/2025 | 99/9999 | Purchase |
|  | MXX03 | USD | 80% | 12/2025 | 99/9999 | Purchase |
|  | MXX04 | USD | 0%=> 60% in 01/2026 | 01/2026 | 99/9999 | Purchase |
|  | MXX05 | EUR | 13% | 12/2025 | 99/9999 | at Equity |
|  | MXX06 | JPY | 90%=> 0% in 01/2026 | 12/2025 | 01/2026 | Purchase |
|  | MXX07 | EUR | 90%->70% | 12/2025 | 99/9999 | Purchase |
|  | MXX08 | CNY | 60%->90% | 12/2025 | 99/9999 | Purchase |

It is optional that you can create your second consolidation group and check this closing.

In this scenario, you manage the following periods and activities:

- In 12/2025 you start with the first consolidation (initial consolidation for all units except MXX04).
- In 01/2026 you run the task carry forward and run the tasks as it happens in 12/2025. The following activities based on consolidation of investment will take place:
    - Consolidation unit MXX04 is an incoming unit of the group (60%). There will be the activity “first consolidation”.
    - Consolidation unit MXX06 is divested totally.
    - Consolidation unit MXX07 is partially divested without loss of control (capital decrease).
    - Parent entity MXX00 (as of 12/2025) acquires further interests in consolidation unit MXX08 (capital increase).
- In 02/2026 and 03/2026 you have to run the tasks as it is in 12/2025 with subsequent consolidation including calculation of minorities.

#### Create Consolidation Units and Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download a master data file of consolidation units and then maintain the data relevant for your test, and you upload the maintained file of the relevant consolidation units. And you create your own consolidation group used for testing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Option 1- Download Sample File Directly | Download the consolidation units of rule-based COI [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Consolidation_Units_Rule_Based_A10.xlsx) here. |  |  |
| 3 | Option 2 - Download and Master Data | Open Import Consolidation Master Data (F3924).Select Consolidation Unit and choose Download Master Data.Make the following entries and then choose Download.Consolidation Version: A10Effective Fiscal Year and Period: 012/2025Note The filter is entered in a user-dependent format. If you use the wrong format, a notification displays with the correct format for you to use.Language: EN | The Import Consolidation Master Data view is displayed. |  |
| 4 | Review and Maintain Master Data | Open the downloaded file.Using the provided table, search the file for the relevant MXX consolidation units.Remember Replace the XX with your ID.Verify that the units in the following table exist and the settings are the same as in the table.Note If MXX consolidation units are not in the Master Data file, then manually add the consolidation units according to the Consolidation Units Table below.Note Check if unit 999999 has been created already, if not, please maintain unit 999999 as the below table in the sample file. | The downloaded file contains the correct data for the consolidation units relevant for your test. |  |
| 5 | Upload | Select the Consolidation Unit row to go into the details.In the Import Consolidation Units view, choose Upload to drop your adjusted file on to the dialog.Choose Check All and if it runs in successful results, then choose Import All. | The updated file is uploaded. |  |
| 6 | Correct Errors | When Checked with Errors status appears or other warnings display, it is necessary to correct the data before proceeding.Select the checkboxes for the rows with errors and choose the Download button.A spreadsheet downloads with the selected records.Open the file and correct the data.When the update is complete, choose Upload to drop the file.Choose Check All and then Import AllRerun the previous step and repeat until all units show a successful status. | A successful check result for all of the consolidation units is displayed. |  |
| 7 | Create Consolidation Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Define Consolidation Groups (F7959).Choose Create.In the Create Consolidation Group popup, enter the ID of your consolidation group CGRXX.Please replace the XX with your own tester ID.Then choose Create.In the Basic Data tab, input following entries:Consolidation Group Description: <for example, the consolidation group name you create, CGRXX>Consolidation Group Medium Description: <for example, the consolidation group name you create, CGRXX>Choose Save. |  |  |

Consolidation Units Table

The following table contains the values to verify and maintain in the downloaded Consolidation_Unit file:

|  |
| --- |
| Note Adjust the IDs of the consolidation units provided in the file to your own IDs. You replace the XX with your own tester ID. |

|  |
| --- |
| Note Please choose from dropdown lists instead of entering values manually. |

| *Consolidation Unit (18) | Consolidation Unit Description (15) | Consolidation Unit Medium Description (30) | Consolidation Unit Long Description (60) | *Local Currency (5) | Company (6) | Country/Region (3) | Consolidation Unit is Partner Unit Only (1) | Currency Translation Method (5) | Tax Rate (8) | Deviating Fiscal Year Variant (2) | Universal Journal Integration (1) | Upload Method (5) | Data Collection Selection (30) | Posting Rule Selection (30) | Partner Selection (30) | Validation Selection (30) | Link Title (255) | Link URL (1333) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MXX00 | Germany | Germany |  | EUR -- European Euro |  | DE -- Germany |  | S0903 -- Standard translation Periodic | 35 |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX02 | France | France |  | EUR -- European Euro |  | FR -- France |  | S0903 -- Standard translation Periodic | 39 |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX03 | USA East | USA East |  | USD -- United States Dollar |  | US -- USA |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX04 | USA West | USA West |  | USD -- United States Dollar |  | US -- USA |  | S0904 -- Translation-FC@Incoming Unit |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX05 | Belgium | Belgium |  | EUR -- European Euro |  | BE -- Belgium |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX06 | Japan | Japan |  | JPY -- Japanese Yen |  | JP -- Japan |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX07 | Austria | Austria |  | EUR -- European Euro |  | AT -- Austria |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MXX08 | China | China |  | CNY -- Chinese Yuan Renminbi |  | CN -- China |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| 999999 | Company 999999 | Company 999999 |  | EUR -- European Euro |  |  |  |  |  |  | U -- No Integration |  |  |  |  |  |  |  |

#### Define Hierarchies for Hierarchy Elimination (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Propose

In this activity, you create different management views of consolidation for consolidation units, profit centers, and segment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as General Ledger Accountant - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). |  |  |
| 3 | Enter Details | Make the following entries and choose Continue:Cons Group: CGRXX (replace XX with your created group number)Cons Unit: NAVersion: A10Fiscal Year: 2025Period: 12Cons COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Manage Consolidation Hierarchies (F7995). | The Manage Global Hierarchies view is displayed. |  |
| 5 | Define Hierarchy REGION | Select Create (Create New Hierarchy) and on the New Hierarchy dialog box, enter the following parameters:Type: Consolidation UnitHierarchy ID: REGIONHierarchy Description: RegionChoose Create. | Consolidation unit hierarchy REGION is created. |  |
| 6 | Select Hierarchy | From the Hierarchy List, select the REGION, Consolidation Unit hierarchy to go to the detailed page. | The right column displays the REGION, Consolidation Unit hierarchy. |  |
| 7 | Maintain Spreadsheet | Download the [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_REGION_Consolidation_Unit.xlsx) to local drive and replace XX with your consolidation unit ID. | Structure of consolidation unit hierarchy Region is updated. |  |
| 8 | Upload | Choose Edit from the top of the view.Choose the arrow button on the top right and select Import from Spreadsheet from the dropdown list.Upload your updated local template and choose Upload file.Choose Save and then Activate the hierarchy region. | An Import from Spreadsheet dialog box is displayed. |  |
| 9 | Back | Choose the < (Back) button to return to the previous view. |  |  |
| 10 | Define Hierarchy BRD | Select the Create (Create New Hierarchy) icon.In the New Hierarchy dialog box, enter the following parameters:Type: Consolidation Profit CenterHierarchy ID: BRDControlling Area: A000Hierarchy Description: Lines of BusinessChoose Create. | The Create New Hierarchy dialog box is displayed. |  |
| 11 | Select Hierarchy | From the Hierarchy List, select the newly-created BRD hierarchy. | A BRD - Consolidation Profit Center column displays. |  |
| 12 | Import Spreadsheet | Choose Edit from the top of the view.Choose the arrow button on the upper right and select Import from Spreadsheet from the dropdown. | An Import from Spreadsheet dialog box displays. |  |
| 13 | Upload File | Upload the attached [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_BRD_Consolidation_Profit_Center.xlsx) with hierarchy structure defined and choose Upload File.Choose Save and then choose Activate. | Structure of profit center hierarchy BRD is updated. |  |
| 14 | Back | Choose the < (Back) button to return to the previous view. |  |  |
| 15 | Define Hierarchy LOB | Create an additional hierarchy by selecting the Create (Create New Hierarchy) icon.In the New Hierarchy dialog box, enter the following parameters:Type: Consolidation Profit CenterHierarchy ID: LOBControlling Area: A000Hierarchy Description: BrandChoose Create. | Profit center hierarchy LOB is created and displays in a Hierarchy List. |  |
| 16 | Repeat for LOB Hierarchy | From the Hierarchy List on the left column, select LOB, Consolidation Profit Center. | The right column displays the LOB - Consolidation Profit Center hierarchy. |  |
| 17 | Import Spreadsheet | Choose Edit from the top of the view.Choose the arrow button and select Import from Spreadsheet from the dropdown. | An Import from Spreadsheet dialog box displays. |  |
| 18 | Upload File | Upload the attached [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_LOB_Consolidation_Profit_Center.xlsx) with hierarchy structure defined and choose Upload File.Choose Save and then Activate the hierarchy. | Structure of profit center hierarchy LOB is updated. |  |
| 19 | Back | Choose the < (Back) button to return to the previous view. |  |  |
| 20 | Define Hierarchy SEG | Choose the Create (Create New Hierarchy) icon.In the New Hierarchy dialog box, enter the following parameters:Type: Consolidation SegmentHierarchy ID: SEGHierarchy Description: Segmentand choose Create. | Segment hierarchy SEG is created and displays in a Hierarchy List. |  |
| 21 | Select Hierarchy | From the Hierarchy List, select the SEG, Consolidation Segment hierarchy. | The right column displays the SEG - Consolidation Segment hierarchy. |  |
| 22 | Import Spreadsheet | Choose Edit from the top of the view.Choose the arrow button and select Import from Spreadsheet from the dropdown. | An Import from Spreadsheet dialog box is displayed. |  |
| 23 | Upload File | Upload the attached [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_SEG_Consolidation_Segment.xlsx) with hierarchy structure defined and then choose Upload file.Choose Save and then Activate the hierarchy SEG. | Structure of segment hierarchy SEG is updated. |  |

#### Set up Group Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you verify and maintain consolidation group structure, that is, the assignment of consolidation units to consolidation groups and maintain consolidation group-specific settings of the consolidation units (such as period of first consolidation, consolidation method, and so on.).

The achieved result has the following group structure.

|  |
| --- |
| Note Adjust the IDs of the consolidation group/consolidation units provided in this file to your own IDs. Please replace XX with your own tester ID. |

| Consolidation Group (18) | Consolidation Unit (18) | Start of Assignment (YYYY/PPP) | End of Assignment (Derived Automatically During Upload) | *First Consolidation (YYYY/PPP) | First Consolidation at End of Period (1) | *Divestiture (YYYY/PPP) | Divestiture at Beginning of Period (1) | Divestiture due to Merger (1) | Start of Method Assignment (Ignored during Upload) | End of Method Assignment (Ignored during Upload) | Effective Fiscal Year Period for Method Change (YYYY/PPP) | Method Change at Beginning of Period (1) | Consolidation Method (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CGRXX | MXX00 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 00 -- Parent (Direct Shares) |
| CGRXX | MXX02 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX03 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX04 | 2026/001 | 9999/999 | 2026/001 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX05 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 20 -- Equity Method (Direct Shares) |
| CGRXX | MXX06 | 2025/012 | 2026/016 | 2025/012 | No | 2026/001 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX07 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX08 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |

Procedure Options

|  |
| --- |
| Note There are two options for reviewing and maintaining the group structure. Review both before proceeding. |

The first option uses the Import Consolidation Master Data (F3924) SAP Fiori app.

The second option uses the Manage Group Structure - Group View (F3733) SAP Fiori app.

Option 1 - Using the Import Consolidation Master Data SAP Fiori App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related app is launched and a Global parameters dialog box displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: CGRXXRemember replace the XX with your tester ID.Version: A10Fiscal year: 2025Period: 12Cons. COA: Y1 | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the SAP Fiori App | Open Import Consolidation Master Data (F3924). | The Import Consolidation Master Data view is displayed. |  |
| 5 | Download Template | Select the Consolidation Group Structure row, and choose Download Master Data.In the Consolidation Group Structure view, enter the following entry and choose Download.Consolidation Version: A10 | A Consolidation Group Structure template file is downloaded. |  |
| 6 | Review and Maintain Master Data | Open the downloaded file.Delete the Consolidation Groups and Consolidation Units that are not used in your testing. Maintain your own consolidation unit assignments and settings as the same as those in the table in the above Purpose section.Remember replace the XX with your tester ID.Save the file. | The downloaded file contains the correct data for the consolidation units relevant for your test. |  |
| 7 | Upload | On the Import Consolidation Master Data view, choose the Upload button.On the Upload dialog box, either drag and drop your file on to the dialog or select the Upload button to navigate to the file. | The updated file is uploaded. |  |
| 8 | Verify Upload | Select the multiple consolidation group structures that are relevant for your test and choose Check Selected.Or you can choose the Check All button at the right of the table. | The status for your consolidation groups update. |  |
| 9 | Correct Errors | Note If the Check All run results in successful results, skip this step.When Checked with Errors status appears or other warnings display, it is necessary to correct the data before proceeding.Select the checkboxes for the rows with errors and choose the Download button.A spreadsheet downloads with the selected records.Open the file and correct the data.When the update is complete, choose the Upload button.On the Upload dialog box, either drag and drop the file or choose the Upload button to navigate to the file location and choose Open.Rerun the previous step and repeat until all groups show a successful status. | A successful check result for all of the consolidation groups is displayed. |  |
| 10 | Import Master Data | Select all of the checkboxes for your relevant consolidation groups.Choose the Import Selected button. | The master data of the relevant consolidation groups is imported from your personal staging area to the master data tables of the consolidation. Master data of the consolidation groups is now ready for testing. |  |

Option 2 - Using the Manage Group Structure - Group View SAP Fiori App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related app is launched and a Global parameters dialog box displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: CGRXXRemember replace the XX with your tester ID.Version: A10Fiscal year: 2025Period: 12Cons. COA: Y1 | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the SAP Fiori App | Open Manage Group Structure - Group View (F3733). | The Manage Consolidation Group Structure - Group View displays with a list of Assignments of Units to Groups. |  |
| 5 | Review Existing Unit Assignments | Review if your consolidation unit assignments have already existed.If yes, leave unchanged of those assignments that are the same as what appears in the table in the Purpose section.For more assignments that are not part of the table in the Purpose section, select the checkboxes for the rows of those assignments and choose Remove.For assignments that deviate in their settings from the table in the Purpose section, double-click the row of deviating assignments in the table, then choose Edit and maintain the values of the assignment according to the table in the Purpose section.Choose Save.If the assignments haven’t been done, skip this step. |  |  |
| 6 | Create Missing Assignments | Choose Assign. | The Assign Consolidation Units dialog is displayed. |  |
| 7 | Select Units | Select all consolidation units with IDs starting with MXX .Remember Replace the XX with the group number.Use search field to filter the value of the relevant consolidation units. | All relevant consolidation units are selected. |  |
| 8 | Next | Choose Next. | A different Assign Consolidation Units dialog box is displayed. |  |
| 9 | Adjust Assignments | Enter or validate the appropriate values for First Consolidation, Divestiture, and Consolidation Method. | The Assign button is activated. |  |
| 10 | Assign | Choose Assign. | The newly assigned consolidation units are displayed in the list report. |  |
| 11 | Create More Unit Assignments | If necessary, continue assigning other consolidation units. | The consolidation group structure is ready for testing. |  |

#### 2025.12 Initial Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the initial consolidation for 12/2025.

Procedure - Data Monitor

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution view displays. |  |
| 3 | Configure Your Solution | Navigate to Configure Your Solution.Select Finance for Application Area and Corporate Close for Sub Application Area and choose Go.In the filter result, choose Basic Settings. | Consolidation Configuration Steps are filtered. |  |
| 4 | Set Global Parameters | Choose Configure of the configuration step Set Global Parameters .Set the following parameters:Organizational Units area:Cons. Group: CGRXX, replace the XX with your assigned groupCons. Unit: <leave blank>Version/Time period area:Version: A10Fiscal Year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. | The Global parameters dialog box is displayed. |  |
| 5 | Select Data Processing | Go back to and choose Data Processing. | Consolidation Configuration Steps are filtered. |  |
| 6 | Assign Monitor Task Groups | Choose Configure of the configuration activity Assign Task Group to Version.Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: S10Cons mon. task group: S20Note Ignore the step if this entry already exists. |  |  |
| 7 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 8 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 9 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S1080Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 10 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 11 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 12 | Data Monitor | Open Data Monitor (CXCD).In the Hierarchy column, right-click the group CGRXX and choose Open period. | The Data Monitor view is displayed. |  |
| 13 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 14 | Data Monitor - Data Collection | In the Data Monitor view, select the Data Coll. - Milestone:Data Collection task and choose Update Run in the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2025_12_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: Upload_A10_2025_12_CGRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: Upload_A10_2025_12_CGRXX_SRD2_DT_0BChoose Import. | Files imported successfully. |  |
| 15 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected results. |  |
| 16 | Data Monitor - Calculate Net Income | In the NI Rpt. D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 17 | Data Monitor - Validation for Reported Data | In the Val.Rpt.D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 18 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update Run of the task Man.Std.10. Post documents separately for each unit.Option 2Upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post. |  |  |
| 19 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell of your consolidation group and choose Update Run in the toolbar. | No warning / no error. |  |
| 20 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 21 | Block Tasks | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 22 | Exit | Choose Back to exit. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Set Global Parameters | Set the following parameters:Organizational Units area:Cons Group: CGRXX, replace the XX with your assigned groupCons Unit: >Version/Time period area:Version: A10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. | The Global parameters dialog box is displayed. |  |
| 4 | Open Assign Task Group to Version | Go back to the previous view.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Task Group to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Task Group to Version screen displays. |  |
| 5 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: S10Cons mon. task group: S20 |  |  |
| 6 | Log on | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. |  |  |
| 7 | Set Global Parameters | Open Set Global Parameters (CXGP).Set the following parameters:Organizational Units area:Cons Group: CGRXX, replace the XX with your assigned groupCons Unit: <leave blank>Version/Time period area:Version: A10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. | The Global parameters dialog box displays. |  |
| 8 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 9 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S2980Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 10 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 11 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 12 | Data Monitor | Open Data Monitor (CXCD).In the Hierarchy column, right-click the group CGRXX and choose Open period. | The Data Monitor view is displayed. |  |
| 13 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 14 | Data Monitor - Data Collection | In the Data Monitor view, select the Data Coll. - Milestone:Data Collection task and choose Update Run in the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2025_12_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File name: Upload_A10_2025_12_CGRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File name: Upload_A10_2025_12_CGRXX_SRD2_DT_0BChoose Import. | Files imported successfully. |  |
| 15 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected results. |  |
| 16 | Data Monitor - Calculate Net Income | In the NI Rpt. D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 17 | Data Monitor - Validation for Reported Data | In the Val.Rep.D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 18 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update of the task Man.Std.10. Post documents separately for each unit.Option 2Upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload. For uploading the document, use the data rows in the template.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post. |  |  |
| 19 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell of your consolidation group and choose Update Run in the toolbar. | No warning / no error. |  |
| 20 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell of your consolidation group and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 21 | Block Tasks | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 22 | Exit | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: CGRXXProcess Year Period: 012/2025 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check each task log. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open Group Data Analysis (W0135). Run the report to verify consolidated data with expected outcomes:Note You use the views and tiles that you create for Consolidated Balance Sheet and P&L in the following [Reporting](#unique_38) [page ] 170 section. | This outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Rule_base_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

#### 2026.01 Full Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related screen is displayed. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons Group: CGRXXRemember Change the XX to your group number.Cons Unit: NAVersion: A10Fiscal year: 2026Period: 01Cons. COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor - Open Period | Right-click subgroup CGRXX and choose Open period. |  |  |
| 6 | Data Monitor - Balance Carryforward | In the Data Monitor view, right-click the Bal.Cfwd task and select Update or choose Update Run from the toolbar. | No warning / no error. |  |
| 7 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 8 | Data Monitor - Data Collection | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2026_01_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: Upload_A10_2026_01_CGRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2026_01_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: Upload_A10_2026_01_CGRXX_SRD2_DT_0BChoose Import. | No warning / no error. |  |
| 9 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 10 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 11 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rep.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 12 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update Run of the task Man.Std.10. Post documents separately for each unit.Option 2Upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_MJE_2026_01_PL_10.xlsx) and verify that the template has the same settings before you run the upload.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post. |  |  |
| 13 | Data Monitor - Currency Translation | In the Data Monitor view, select your cons group of the task CurrTrans. and choose Update Run from the toolbar. |  |  |
| 14 | Data Monitor - Validation for Standardized Data | In the Data Monitor view, select your cons group of the task Val.Std.D task and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 15 | Data Monitor - Block | Select the row of each task and choose Block to block each task.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 16 | Data Monitor - Exit | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: CGRXXProcess Year Period: 001/2026 |  |  |
| 4 | Consolidation Monitor - Manual Elimination PL30 (2150) | Select the task 2150 Manual Eliminations (PL 30) for your cons group and then choose Manual Run.In Journal Entry view, post documents.As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) SAP Fiori app and this [file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_MJE_2026_01_PL_30.xlsx).Remember Replace the XX in the columns *Consolidation Group (18), Remarks (50), *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 5 | Consolidation Monitor - Remaining Tasks Execute | Select all the remaining tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 6 | Consolidation Monitor Block | In the Consolidation Monitor view, choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 7 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 8 | Consolidation Reports | Open app Group Data Analysis (W0135). Run the report to check consolidated data with expected outcomes.You use the views and tiles that you create for Consolidated Balance Sheet and P&L in the following [Reporting](#unique_38) [page ] 170 section.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Fiscal Year Period: 001/2026Key Date: 31.01.2026 | The expected outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Rule_base_1SG.xlsx). |  |
| 9 | Display Statement of Cash Flow | Choose Group Data Analysis - With Reporting Rules (W0136).Note You may use the Search function to search for Group Data Analysis with Reporting Rules and select the title that shows Accessible.Run the report to check the Statement of Cash Flow with the expected result.Note Use the views and tiles that you create in [Cash Flow Statement](#unique_30) [page ] 174 in the Reporting section. | The expected outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Rule_base_1SG.xlsx). |  |
| 10 | Consolidation Reports Exit | Choose Exit. |  |  |
| 11 | Hierarchy Elimination Analysis (Optional) | Note Following steps are optional and used for Hierarchy Elimination testing.We suggest that you perform more free-style testing. You can consider using other test cases besides the provided ones.The following reports are provided to specific, selected FS items:By scope and consolidation unit hierarchy RegionBy scope and profit centers hierarchy LOBBy scope and profit centers hierarchy BRDBy scope and segment hierarchy SEGBy any other combinations of management views |  |  |
| 12 | Access the SAP Fiori App (Optional) | Open Group Data Analysis - With Reporting Rules (W0136) |  |  |
| 13 | Enter Criteria (Optional) | Enter the following selections:Version: A10Consolidation COA: Y1Fiscal Year Period: 001/2026Cons. Group: <For example, CGRXX, (replace the XX with your group)>Period Mode: YTDKey Date: 01/31/2026Consolidation Unit Hierarchy: <For example, $>Profit Center Hierarchy: <For example, Line of Business>Segment Hierarchy: <For example, SEGMENT>Rep. Item Hierarchy: <For example, X2>Reporting Rule Variant: Y10Choose Go. | The Group Data Analysis - With Reporting Rules view is displayed. |  |
| 14 | Analysis View by Profit Centers (Optional) | Choose Navigation Panel on the top left.In the Columns area, remove other fields to keep only Fiscal Year, Fiscal Period, Period mode, and Measures in the list.In the Rows area, remove other fields to keep only Reporting Item in the list.From Available Fields, find the Profit Center for Elimination field and drag and drop into Rows to change the display of the report.Right-click the Profit Center for Elimination field in Rows in the navigation panel and choose Hierarchy > Select Hierarchy. Choose item hierarchy Lines of Business and choose OK.Right-click the Profit Center Elimination row header and choose Hierarchy > Expand All.To save this layout as your default view, choose arrow button beside <No Bookmark Loaded> above the report body and then choose Save As.In the Save Bookmark As dialog box, enter a bookmark name, and select the With Filter Values checkbox. Choose Save. | Management consolidation analysis view for profit center is generated. |  |
| 15 | Analysis View by Profit Centers and Segment (Optional) | Now drag the Segment for Elimination dimension to Rows.Right-click the Segment for Elimination field and choose Hierarchy > Select Hierarchy, and then select Segment and choose OK.Right-click Segment for Elimination row header and choose Hierarchy > Expand All. | Consolidation analysis view for profit center and segment is generated. |  |
| 16 | Analysis View by Scope, Profit Centers, and Segment (Optional) | Now drag the Consolidation Group dimension to the Rows axis and add before Profit Center for Elimination. | Consolidation analysis view for scope, profit center, and segment is generated. |  |
| 17 | Review Group Journal Entries (Optional) | Select Navigate To > Display Group Journal Entries With Reporting Logic. | Relevant group journal entries are displayed. |  |

#### 2026.02 Subsequent Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related view is displayed. |  |
| 3 | Set Global Parameters | Set the following global parameters and choose Continue:Cons. Group: CGRXXRemember Change the XX for your group values.Cons. Unit: NAVersion: A10Fiscal Year: 2026Period: 02Cons. COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor | Right-click subgroup CGRXX and choose Open Period. |  |  |
| 6 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 7 | Data Monitor - Data Collection | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2026_02_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: Upload_A10_2026_02_CGRXX_SRD2_DT_00Choose Import. | No warning / no error. |  |
| 8 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. |  |  |
| 9 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 10 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rep.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 11 | Data Monitor - Manual Posting PL10 | This task does not require execution. |  |  |
| 12 | Data Monitor - Currency Translation | In the Data Monitor view, select your cons group of the task CurreTrans. and choose Update Run from the toolbar. |  |  |
| 13 | Data Monitor - Standardized Data Validation | In the Data Monitor view, select your cons group of the task Val.Std.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 14 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 15 | Exit Data Monitor | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: CGRXXProcess Year Period: 002/2026 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open app Group Data Analysis (W0135). Run the report to check consolidated data with expected outcomes.You use the views and tiles that you create for Consolidated Balance Sheet and P&L in the following [Reporting](#unique_38) [page ] 170 section.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Fiscal Year Period: 002/2026Key Date: 28.02.2026 | The expected outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Rule_base_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

#### 2026.03 Subsequent Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Set Global Parameters (CXGP). | The Global parameters dialog box is displayed. |  |
| 3 | Set Global Parameters | Set Global parameters and choose Continue:Cons. Group: CGRXXCons. Unit: <leave blank>Version: A10Fiscal Year: 2026Period: 3Cons.COA: Y1 | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor | Right-choose subgroup CGRXX and choose Open Period. |  |  |
| 6 | Data Monitor - Release Universal Journals | This task does not require execution. |  |  |
| 7 | Data Monitor - Data Collection | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_A10_UPLOAD_2026_03_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2026_03_CGRXX_SRD2_DT_00Choose Import. | No warning / no error. |  |
| 8 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 9 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | The task is executed successfully with detailed log about calculated net income result. |  |
| 10 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 11 | Data Monitor - Manual Posting PL10 | This task does not require execution. |  |  |
| 12 | Data Monitor - Currency Translation | In the Data Monitor view, select your cons group of the task CurrTrans. and choose Update Run from the toolbar. |  |  |
| 13 | Data Monitor - Standardized Data Validation | In the Data Monitor view, select your cons group of the task Val.Std.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 14 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 15 | Exit Data Monitor | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: CGRXXProcess Year Period: 003/2026 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open app Group Data Analysis (W0135). Run the report to check consolidated data with expected outcomes.You use the views and tiles that you create for Consolidated Balance Sheet and P&L in the following [Reporting](#unique_38) [page ] 170 section.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Fiscal Year Period: 003/2026Key Date: 31.03.2026 | The expected outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Rule_base_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

### Consolidation Scenario Actuals_Method Change (Rule Based COI)

The following table displays the codification of the consolidation groups and consolidation units per tester.

You need to adjust the IDs of the consolidation group/consolidation units/partner units provided in this file to your own IDs (XX= assigned number).

Table 10: Consolidation Scenario Actuals_Method Change (Rule Based COI)

| Cons. Group | Consunit | LC | % of Share | Period / Year of First Consolidation | Effective Fiscal Period / Year for Method Change | Method CoI |
| --- | --- | --- | --- | --- | --- | --- |
| MCRXX | MCXX00 | EUR | - | 12/2025 | - | Parent |
|  | MCXX01 | EUR | 20% => 80% | 12/2025 | 02/2026 | at Equity => Purchase |
|  | MCXX02 | EUR | 80% => 20% | 12/2025 | 02/2026 | Purchase => at Equity |

In this scenario, you manage the following periods and activities:

- In 12/2025, you start with the first consolidation (initial consolidation for all units).

MCXX00 is parent unit.

MCXX00 has a significant influence in MCXX01. The direct ownership rate of MCXX00 over MCXX01 is 20%. Consolidation method assigned to MCXX01 is at equity method.

MCXX00 has a direct control in MCXX02. The direct ownership rate of MCXX00 over MCXX02 is 80%. Consolidation method assigned to MCXX02 is purchase method.

- In 01/2026, you run the task carry forward and other relevant tasks for subsequent consolidation in 01/2026.
- In 02/2026, you run the relevant tasks in 02/2026. The following activities based on consolidation of investment will take place:
    - The share % of consolidation unit MCXX01 changes from 20% to 80% at the end of the period. Accordingly, consolidation of investment method changes from at equity method to purchase method at the end of the period.
    - The share % of consolidation unit MCXX02 changes from 80% to 20% at the end of the period. Accordingly, consolidation of investment method changes from purchase method to at equity method at the end of the period.

#### Create Consolidation Units and Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download a master data file of consolidation units and then maintain the data relevant for your test, and you upload the maintained file of the relevant consolidation units. And you create your own consolidation group used for testing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Option 1- Download Sample File Directly | Download the consolidation units of method change [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/Consolidation_Units_Rule_Based_MC.xlsx) here. |  |  |
| 3 | Option 2 - Download Master Data | Open Import Consolidation Master Data (F3924).On the Master Data Types table, select the Consolidation Unit row and choose Download Master Data.Make the following entries and then choose Download.Consolidation Version: A10Effective Fiscal Year and Period: 012/2022Note The filter is entered in a user-dependent format. If you use the wrong format, a notification displays with the correct format for you to use.Language: EN | The Import Consolidation Master Data view displays. |  |
| 4 | Review and Maintain Master Data | Open the downloaded file.Using the provided table, search the file for the relevant MCXX consolidation units.Remember Replace the XX with your ID.Verify that the units in the following table exist and the settings are the same as in the table.Note If MCXX consolidation units are not in the Master Data file, then choose Download Template and manually maintain the consolidation units according to the Consolidation Units Table below.Note Check if unit 999999 has been created already, if not, please maintain unit 999999 as the below table in the sample file. | The downloaded file contains the correct data for the consolidation units relevant for your test. |  |
| 5 | Upload | Select the Consolidation Units row and choose >.In the Import Consolidation Master Data view, choose Upload.In the Upload dialog box, either drag and drop your file on to the dialog or select the + (Upload) button to navigate to the file.Choose OK. | The updated file is uploaded. |  |
| 6 | Verify Upload | Select the field help of the Consolidated Unit filter and in the dialog box, search for and select the multiple consolidation units that are relevant for your test.Choose OK and those consolidation units display in the table.In the Status column, choose To Be Checked for all rows and choose Check Selected at the right of the table. | The status for your consolidation units updates. |  |
| 7 | Correct Errors | Note If the Check run results in successful results, skip this step.When Checked with Errors status appears or other warnings display, it is necessary to correct the data before proceeding.Select the check boxes for the rows with errors and choose the Download button.A spreadsheet downloads with the selected records.Open the file and correct the data.When the update is complete, choose Upload.In the Upload dialog box, either drag and drop the file or choose the + (Upload) button to navigate to the file location and choose OK.Rerun the previous step and repeat until all units show a successful status. | A successful check result for all of the consolidation units is displayed. |  |
| 8 | Import Master Data | Select all of the check boxes for your relevant consolidation units.Choose Import Selected. | The master data of the relevant consolidation units is imported from your personal staging area to the master data tables of the consolidation. Master data of the consolidation units is now ready for testing. |  |
| 9 | Create Consolidation Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Define Consolidation Groups (F7959).Choose Create.In the Create Consolidation Group pop up, enter the ID of your consolidation group MCRXX.Please replace the XX with your own tester ID.Then choose Create.In the Basic Data tab, input following entries:Consolidation Group Description: <for example, the consolidation group name you create, MCRXX>Consolidation Group Medium Description: <for example, the consolidation group name you create, MCRXX>Choose Save. |  |  |

Consolidation Units Table

The following table contains the values to verify and maintain in the downloaded Consolidation_Unit file:

|  |
| --- |
| Note Adjust the IDs of the consolidation units provided in the file to your own IDs. You replace the XX with your own tester ID. |

|  |
| --- |
| Note Please choose from drop down lists instead of entering values manually. |

| *Consolidation Unit (18) | Consolidation Unit Description (15) | Consolidation Unit Medium Description (30) | Consolidation Unit Long Description (60) | *Local Currency (5) | Company (6) | Country/Region (3) | Consolidation Unit is Partner Unit Only (1) | Currency Translation Method (5) | Tax Rate (8) | Deviating Fiscal Year Variant (2) | Universal Journal Integration (1) | Upload Method (5) | Data Collection Selection (30) | Posting Rule Selection (30) | Partner Selection (30) | Validation Selection (30) | Link Title (255) | Link URL (1333) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCXX00 | Germany | Germany |  | EUR -- European Euro |  | DE -- Germany |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MCXX01 | France | France |  | EUR -- European Euro |  | FR -- France |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| MCXX02 | Austria | Austria |  | EUR -- European Euro |  | AT -- Austria |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration |  |  |  |  |  |  |  |
| 999999 | Company 999999 | Company 999999 |  | EUR -- European Euro |  |  |  |  |  |  | U -- No Integration |  |  |  |  |  |  |  |

#### Set Up Group Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you verify and maintain consolidation group structure that is the assignment of consolidation units to consolidation groups and maintain consolidation group-specific settings of the consolidation units (such as period of first consolidation, consolidation method, and so on.).

The achieved result has the following group structure.

|  |
| --- |
| Note Adjust the IDs of the consolidation group/consolidation units provided in this file to your own IDs. Please replace XX with your own tester ID. |

| Consolidation Group (18) | Consolidation Unit (18) | Start of Assignment (YYYY/PPP) | End of Assignment (Derived Automatically During Upload) | *First Consolidation (YYYY/PPP) | First Consolidation at End of Period (1) | *Divestiture (YYYY/PPP) | Divestiture at Beginning of Period (1) | Divestiture due to Merger (1) | Start of Method Assignment (Ignored during Upload) | End of Method Assignment (Ignored during Upload) | Effective Fiscal Year Period for Method Change (YYYY/PPP) | Method Change at Beginning of Period (1) | Consolidation Method (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCRXX | MCXX00 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 00 -- Parent (Direct Shares) |
| MCRXX | MCXX01 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 20 -- Equity Method (Direct Shares) |
| MCRXX | MCXX02 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Global parameters dialog box appears. |  |
| 3 | Set Global Parameters | Set Global parameters:Cons. Group: MCRXXVersion: A10Fiscal year: 2025Period: 12Choose Continue. | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the SAP Fiori App | Open Import Consolidation Master Data (F3924). | The Import Consolidation Master Data view displays. |  |
| 5 | Navigate to Master Data | Under the Master Data Types, on the Consolidation Group Structure row, select Actions > Download Master Data . | A Download Master Data dialog box displays. |  |
| 6 | Enter Criteria | Enter the following values:Consolidation Version: A10 | The Download button is active. |  |
| 7 | Download | Choose Download. | An xlsx file with consolidation unit master data downloads. |  |
| 8 | Review and Maintain Master Data | Open the downloaded file.Delete the Consolidation Groups and Consolidation Units that are not used in your testing. Maintain your own consolidation unit assignments and settings as the same as those in the table in the above Purpose section.Remember replace the XX with your tester ID.Save the file. | The downloaded file contains the correct data for the consolidation units relevant for your test. |  |
| 9 | Upload | On the Import Consolidation Master Data view, choose the Upload button.On the Upload dialog box, either drag and drop your file on to the dialog or select the Upload button to navigate to the file. | The updated file uploads. |  |
| 10 | Verify Upload | Select the multiple consolidation group structures that are relevant for your test and choose Check Selected. | The status for your consolidation groups update. |  |
| 11 | Correct Errors (Optional) | Note If the Check Selected run results in successful results, skip this step.When Checked with Errors status appears or other warnings display, it is necessary to correct the data before proceeding.Select the check boxes for the rows with errors and choose the Download button.A spreadsheet is downloaded with the selected records.Open the file and correct the data.When the update is complete, choose the Upload button.On the Upload dialog box, either drag and drop the file or choose the Upload button to navigate to the file location and choose OK.Rerun the previous steps and repeat until all groups show a Checked Successfully status. | A successful check result for all of the consolidation groups display. |  |
| 12 | Import Master Data | Select all of the check boxes for your relevant consolidation groups.Choose the Import Selected button. | The master data of the relevant consolidation groups is imported from your personal staging area to the master data tables of the consolidation. Master data of the consolidation groups is now ready for testing. |  |

#### 2025.12 Initial Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the initial consolidation for 12/2025.

Procedure - Data Monitor

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution view displays. |  |
| 3 | Select the Relevant App | Navigate to Configure Your Solution.Select Finance for Application Area and Corporate Close for Sub Application Area and choose Go.Choose Basic Settings. | Consolidation Configuration Steps are filtered. |  |
| 4 | Set Global Parameters | Choose Configure of the configuration activity Set Global Parameters.Set the following parameters:Organizational Units area:Cons Group: MCRXX, replace the XX with your assigned groupCons Unit: <leave blank>Version/Time period area:Version: A10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. | The Global parameters dialog box displays. |  |
| 5 | Select Data Processing | Go back and choose Data Processing. | Consolidation Configuration Steps are filtered. |  |
| 6 | Assign Monitor Task Groups | Choose Configure of the configuration activity Assign Task Group to Version.Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: S10Cons mon. task group: S20Note Ignore the step if this entry already exists. |  |  |
| 7 | Log on | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. |  |  |
| 8 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 9 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S1080Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 10 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 11 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 12 | Data Monitor | Open Data Monitor (CXCD).In the Hierarchy column, select the group MCRXX and choose More > Edit > Open period. | The Data Monitor view displays. |  |
| 13 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 14 | Data Monitor - Release Universal Journals | This task does not require execution. |  |  |
| 15 | Data Monitor - Rpt. Data - Milestone:Data Collection - Rp (1021) | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2025_12_MCRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2025_12_MCRXX_SRD2_DT_0BChoose Import.Note For any missing master data, please refer to step Maintain Local Master Data of this procedure to maintain missing master data as local master data and rerun your data collection task to continue the testing. |  |  |
| 16 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. |  |  |
| 17 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 18 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 19 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update of the task Man.Std.10. Post documents separately for each unit.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload. For uploading the document, use the data rows in the template.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Check all of your entries and choose Post. | The Journal Entry dialog box displays. The document is posted. |  |
| 20 | Data Monitor - Currency Translation | This task does not require execution. |  |  |
| 21 | Data Monitor - Standardized Data Validation | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 22 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 23 | Exit | Choose Back to exit. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Task Group to Version screen displays. |  |
| 3 | Set Global Parameters | Set the following parameters:Organizational Units area:Cons Group: MCRXX, replace the XX with your assigned groupCons Unit: <leave blank>Version/Time period area:Version: A10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. |  |  |
| 4 | Open Assign Task Group to Version | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Task Group to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Task Group to Version screen displays. |  |
| 5 | Assign Task Group to Version | Add your reconciliation case and ensure column Active is checked. |  |  |
| 6 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: S10Cons mon. task group: S20Note Ignore the step if this entry already exists. |  |  |
| 7 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 8 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S1080Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 9 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: A10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 10 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 11 | Data Monitor | Open Data Monitor (CXCD).In the Hierarchy column, select the group MCRXX and choose More > Edit > Open period. | The Data Monitor view displays. |  |
| 12 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 13 | Data Monitor - Release Universal Journals | This task does not require execution. |  |  |
| 14 | Data Monitor - Rpt. Data - Milestone:Data Collection - Rp (1021) | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File name: UPLOAD_A10_2025_12_MCRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2025_12_MCRXX_SRD2_DT_0BChoose Import.Note For any missing master data, please refer to step Maintain Local Master Data of this procedure to maintain missing master data as local master data and rerun your data collection task to continue the testing. |  |  |
| 15 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No data available. |  |
| 16 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 17 | Data Monitor - Reported Data Validation | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 18 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update of the task Man.Std.10. Post documents separately for each unit.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload. For uploading the document, use the data rows in the template.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Check all of your entries and choose Post. | The Journal Entry dialog box displays. The document is posted. |  |
| 19 | Data Monitor - Standardized Data Validation | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 20 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 21 | Exit | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: MCRXXProcess Year Period: 012/2025 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group MCRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors.Note To check the detailed log of the task 2060 Preparation Cons Group Change, access the app Consolidation Monitor - Old Version (CX20). Right click the task 2060 Preparation Cons Group Change and choose Last log. The expected result is as follows:CU MCXX01, Period 012: Values revoked with record type E. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open Group Data Analysis (W0135). Run the report to verify consolidated data with expected outcomes:Note You use the views and tiles that you create for Consolidated Balance Sheet and Consolidated Income Statement from the following Reporting section. | This outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Method_Change_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

#### 2026.01 Subsequent Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Global parameters dialog box is displayed. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons Group: MCRXXRemember Change the XX to your group number.Cons Unit: NAVersion: A10Fiscal year: 2026Period: 01Cons. COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor (Original) | Right-click subgroup MCRXX and choose Open period. |  |  |
| 6 | Data Monitor - Balance Carry Forward | In the Data monitor view, select your testing item of the task Bal.Cfwd and choose Update Run from the toolbar. | No warning / no error. |  |
| 7 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 8 | Data Monitor - Data Collection | In the Data Monitor view, select your cons group of the task Data Coll. - Milestone:Data Collection and choose Update Run from the toolbar.Download and edit the [sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2026_01_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2026_01_MCRXX_SRD2_DT_00Choose Import. | No warning / no error. |  |
| 9 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 10 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 11 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your testing item of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 12 | Data Monitor - Manual Posting PL10 | This task does not require execution. |  |  |
| 13 | Data Monitor - Currency Translation | This task does not require execution. |  |  |
| 14 | Data Monitor - Validation for Standardized Data | In the Data Monitor view, select your testing item of the task Val.Std.D task and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 15 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 16 | Data Monitor - Exit | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: MCRXXProcess Year Period: 001//2026 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group MCRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors.Note To check the detailed log of the task 2060 Preparation Cons Group Change, access the app Consolidation Monitor - Old Version (CX20). Right click the task 2060 Preparation Cons Group Change and choose Last log. The expected result is as follows:CU MCXX01, Period 000: Values revoked with record type E.CU MCXX01, Period 001: Values revoked with record type E. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open app Group Data Analysis (W0135). Run the report to check consolidated data with expected outcomes.Note Use the views and tiles that you create for Consolidated Balance Sheet and Consolidated Income Statement in the following [Reporting](#unique_38) [page ] 170 section. | This outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Method_Change_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

#### 2026.02 Method Change at the End of Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Global parameters dialog box displays. |  |
| 3 | Set Global Parameters | Set the following global parameters and choose Continue:Cons. Group: MCRXXRemember Change the XX for your group values.Cons. Unit: NAVersion: A10Fiscal year: 2026Period:02Cons. COA: Y1 |  |  |
| 4 | Manage Consolidation Group Structure - Group View | Open Manage Group Structure - Group View (F3733).Select the assigned consolidation unit MCXX01 and choose > (Details). Then choose Edit.In the section Attributes for Processing, under Time- and Version-Dependent Attributes, change the Consolidation Method from 20 Equity Method (Direct Shares) to 10 Purchase Meth. (Direct Shares) and choose Save.Repeat the same step for the assigned consolidation unit MCXX02 and change the Consolidation Method from 10 Purchase Meth. (Direct Shares) to 20 Equity Method (Direct Shares). | Consolidation method of consolidation units MCXX01 and MCXX02 are changed at the end of the period. |  |
| 5 | Define Consolidation Units (Optional) | Open Define Consolidation Units (F4685).This step is optional for this test scenario as the local currency of consolidation units MCXX01 and MCXX02 is EUR which is the same as group currency.Select the assigned consolidation unit MCXX01 and choose > (Details). Then choose Edit.In the section Time- and Version-Dependent Attributes, change the Currency Translation Method to SMCEP (Method change at end of period) and choose Save.Repeat the same step for consolidation unit MCXX02 and save the update.Note You need to assign SMCBP (Method change at beg of period) if the consolidation method of consolidation unit changes at the beginning step. |  |  |
| 6 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 7 | Data Monitor | Choose subgroup MCRXX. In the toolbar, choose Menu > Edit > Open Period . |  |  |
| 8 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 9 | Data Monitor - Data Collection | In the Data Monitor view, select your item of the task Data Coll. - Milestone:Data Collection and choose Update Run in the toolbar.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2026_02_SRD2_DT_00.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2026_02_MCRXX_SRD2_DT_00Choose Import.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_UPLOAD_2026_02_SRD2_DT_0B.xlsx).Replace XX in the file with your consolidation unit.Choose Browse to upload the edited file.File: UPLOAD_A10_2026_02_MCRXX_SRD2_DT_0BChoose Import. | No warning / no error. |  |
| 10 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. |  |  |
| 11 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 12 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your item in the Val.Rpt.D task and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 13 | Data Monitor - Manual Posting PL10 | Option 1Select your testing items of the task Manual Posting PL10 and choose Update Run. Post documents separately for each unit.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/MCRXX_A10_MJE_2026_02_PL_10.xlsx) and verify that the template has the same settings before you run the upload. For uploading the document, use the data rows in the template.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template. |  |  |
| 14 | Data Monitor - Currency Translation | This task does not require execution. |  |  |
| 15 | Data Monitor - Validation for Standardized Data | In the Data Monitor view, select your item in the Val.Std.D task and choose Update Run in the task bar. | The status of Validation Results are Success with Warnings. |  |
| 16 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 17 | Exit Data Monitor | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: A10Consolidation Group: MCRXXProcess Year Period: 002/2026 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors.Note To check the detailed log of the task 2060 Preparation Cons Group Change, access the app Consolidation Monitor - Old Version (CX20). Right click the task 2060 Preparation Cons Group Change and choose Last log. The expected result is as follows:CU MCXX00, Period 002: Values revoked with record type E for PU MCXX01.CU MCXX00: Values adjusted for method change for PU MCXX01.CU MCXX00: Values adjusted for method change for PU MCXX02.CU MCXX01: Values adjusted for method change (Equity to Purchase).CU MCXX01, Period 000: Values revoked with record type E.CU MCXX01, Period 001: Values revoked with record type E.CU MCXX01, Period 002: Values revoked with record type E.CU MCXX02, Period 002: Values revoked with record type E for PU MCXX00.CU MCXX02: Values adjusted for method change (Purchase to Equity). |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Consolidation Reports | Open app Group Data Analysis (W0135). Run the report to check consolidated data with expected outcomes.Note You create the views and tiles for Consolidated Balance Sheet and Consolidated Income Statement in following [Reporting](#unique_38) [page ] 170 section. | This outcome file can be accessed [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outcome_Method_Change_1SG.xlsx). |  |
| 8 | Consolidation Reports Exit | Choose Exit. |  |  |

### Consolidation Scenario_Multiple Group Currencies and Restatement (Optional)

The following table displays the codification of the consolidation groups and consolidation units per tester.

You need to adjust the IDs of the consolidation group/consolidation units/partner units provided in this file to your own IDs (XX= assigned number).

Table 11: Versions J10, J1R, J20, J2R

| Cons. Group | Consunit | LC | % of share | Period / Year of First Consolidation | Period/year of Divestiture | Method CoI |
| --- | --- | --- | --- | --- | --- | --- |
| CGRXX | Mxx00 | EUR | - | 12/2025 | 99/9999 | Parent |
|  | Mxx02 | EUR | 80% | 12/2025 | 99/9999 | Purchase |
|  | Mxx03 | USD | 80% | 12/2025 | 99/9999 | Purchase |
|  | Mxx04 | USD | 0%=> 60% in 01/2026 | 01/2026 | 99/9999 | Purchase |
|  | Mxx05 | EUR | 13% | 12/2025 | 99/9999 | at Equity |
|  | Mxx06 | JPY | 90%=> 0% in 01/2026 | 12/2025 | 01/2026 | Purchase |
|  | Mxx07 | EUR | 90%->70% | 12/2025 | 99/9999 | Purchase |
|  | Mxx08 | CNY | 60%->90% | 12/2025 | 99/9999 | Purchase |

In the scenario for J10, J1R, J20, J2R, you manage the following periods and activities:

- In 12/2025 you start with the first consolidation (initial consolidation for all units except Mxx04).
- In 01/2026 you run the task carry forward and run the tasks as it happens in 12/2025. The following activities based on consolidation of investment will take place:
    - Consolidation unit Mxx04 is an incoming unit of the group (60%). There will be the activity “first consolidation”.
    - Consolidation unit Mxx06 is divested totally.
    - Consolidation unit Mxx07 is partially divested without loss of control (no capital decrease).
    - Parent entity Mxx00 (as of 12/2025) acquires further interests in consolidation unit Mxx08 (no capital increase).
- In 02/2026 you have run the tasks as it is in 12/2025 with subsequent consolidation including calculation of minorities.

Table 12: Version J1S

| Cons. Group | Consunit | LC | % of share | Period / Year of First Consolidation | Period/year of Divestiture | Method CoI |
| --- | --- | --- | --- | --- | --- | --- |
| CGRXX | Mxx00 | EUR | - | 12/2025 | 99/9999 | Parent |
|  | Mxx01 | USD | 0%=> 60% in 01/2026 | 01/2026 | 99/9999 | Purchase |
|  | Mxx02 | EUR | 80% | 12/2025 | 99/9999 | Purchase |
|  | Mxx03 | USD | 80% | 12/2025 | 99/9999 | Purchase |
|  | Mxx04 | USD | 0%=> 60% in 01/2026 | 01/2026 | 99/9999 | Purchase |
|  | Mxx05 | EUR | Parent entity Mxx00 (as of 12/2025) acquires further interests in13%=> 35% in 01/2026 | 12/2025 | 99/9999 | at Equity |
|  | Mxx06 | JPY | 90%=> 0% in 01/2026 | 12/2025 | 01/2026 | Purchase |
|  | Mxx07 | EUR | 90%->80% in 01/2026 | 12/2025 | 99/9999 | Purchase |
|  | Mxx08 | CNY | 60%->90% in 01/2026 | 12/2025 | 99/9999 | Purchase |

In the scenario for J1S, you manage the following periods and activities:

- In 01/2026, the following activities based on consolidation of investment will take place:
    - Consolidation unit Mxx01 is an incoming unit of the group (60%). There will be the activity “first consolidation”.
    - Consolidation unit Mxx04 is an incoming unit of the group (60%). There will be the activity “first consolidation”.
    - Parent entity Mxx00 acquires further interests in consolidation unit Mxx05 (no capital increase).
    - Consolidation unit Mxx06 is divested totally.
    - Consolidation unit Mxx07 is partially divested without loss of control (no capital decrease).
    - Parent entity Mxx00 acquires further interests in consolidation unit Mxx08 (no capital increase).
- In 02/2026 you have run the tasks as it is in 12/2025 with subsequent consolidation including calculation of minorities.

#### Create Consolidation Units and Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download a master data file of consolidation units and then maintain the data relevant for your MGC test, and you upload the maintained file of the relevant consolidation units. And you create a new consolidation group used for MGC test.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Option 1- Download Sample File Directly | There are two options of acquiring consolidation master data sample files. You can choose one of them.Download the consolidation units of Rule-based COI [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2502_Consolidation_Units_Rule_Based_J10.xlsx) for the versions J10, J1R, J20, J2R.Download the consolidation units of Rule-based COI [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2502_Consolidation_Units_Rule_Based_J1S.xlsx) for the version J1S. |  |  |
| 3 | Option 2- Access Import Consolidation Master Data | Open Import Consolidation Master Data (F3924).On the Master Data Types table, select the Consolidation Unit row and choose Download Master Data.Make the following entries and then choose Download.Consolidation Version: J10Effective Fiscal Year and Period: 012/2025Note The filter is entered in a user-dependent format. If you use the wrong format, a notification displays with the correct format for you to use.Language: EN | The Import Consolidation Master Data view is displayed. |  |
| 4 | Review and Maintain Master Data | Open the downloaded file.Using the provided table, search the file for the relevant MXX consolidation units.Remember Replace the XX with your ID.Verify that the units in the following table exist and the settings are the same as in the table.Note If MXX consolidation units are not in the Master Data file, then choose Actions > Download Template and manually maintain the consolidation units according to the Consolidation Units Table below.Note Check if unit 999999 has been created already, if not, please maintain unit 999999 as the below table in the sample file. | The downloaded file contains the correct data for the consolidation units relevant for your test. |  |
| 5 | Upload | In the Import Consolidation Master Data view, choose Upload.In the Upload dialog box, either drag and drop your file on to the dialog or select the + (Upload) button to navigate to the file.Choose OK. | The updated file is uploaded. |  |
| 6 | View Details | Select the Consolidation Unit row on the Import Consolidation Master Data view to go into the details. | A details view appears. |  |
| 7 | Verify Upload | Select the field help of the Consolidated Unit filter and in the dialog box, search for and select the multiple consolidation units that are relevant for your test.Choose OK and those consolidation units display in the table.In the Status column, choose To Be Checked for all rows and choose Check Selected at the right of the table. | The status for your consolidation units updates. |  |
| 8 | Correct Errors | Note If the Checked with Errors appears or other warnings display, it is necessary to correct the data before proceeding.When run results in successful results, skip this step.Select the checkboxes for the rows with errors and choose the Download button.A spreadsheet downloads with the selected records.Open the file and correct the data.When the update is complete, choose Upload.In the Upload dialog box, either drag and drop the file or choose the + (Upload) button to navigate to the file location and choose OK.Rerun the previous step and repeat until all units show a successful status. | A successful check result for all of the consolidation units is displayed. |  |
| 9 | Import Master Data | Select all of the checkboxes for your relevant consolidation units.Choose Import Selected. | The master data of the relevant consolidation units is imported from your personal staging area to the master data tables of the consolidation. Master data of the consolidation units is now ready for testing. |  |
| 10 | Access the SAP Fiori App | Open Define Consolidation Groups (F7959). | The Consolidation Group Create view is displayed. |  |
| 11 | Consolidation Group Create | Choose Create.In the Create Consolidation Group popup, enter the ID of your consolidation group CGRXX, for example, CGR03.Remember Replace the XX with your group number.Then choose Create. | A new consolidation group is created. |  |
| 12 | Maintain Consolidation Group Details | Make the following entries:In Basic Data:Consolidation Group Description: <for example, the consolidation group name you create, CGR03>Consolidation Group Medium Description: <for example, the consolidation group name you create, CGR03>Choose Save. |  |  |

Consolidation Units Table

The following table contains the values to verify and maintain in the downloaded Consolidation_Unit file.

|  |
| --- |
| Note Adjust the IDs of the consolidation units provided in the file to your own IDs. You replace the XX with your own group number. |

|  |
| --- |
| Note Please check if consolidation unit 999999 has already been created. If so, you don’t need to create it again. |

Table 13: Consolidation Units in the Consolidation Group CGRXX in Versions J10, J1R, J20, J2R

| *Consolidation Unit (18) | Consolidation Unit Description (15) | Consolidation Unit Medium Description (30) | *Local Currency (5) | Country (3) | Currency Translation Method (5) | Tax Rate (8) | Universal Journal Integration (1) | Upload Method (5) | Data Collection Selection (30) | Posting Rule Selection (30) | Partner Selection (30) | Validation Selection (30) | Link Title (255) | Link URL (1333) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MXX00 | Germany | Germany | EUR -- European Euro | DE -- Germany | S0903 -- Standard translation Periodic | 35 | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX02 | France | France | EUR -- European Euro | FR -- France | S0903 -- Standard translation Periodic | 39 | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX03 | USA East | USA East | USD -- United States Dollar | US -- USA | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX04 | USA West | USA West | USD -- United States Dollar | US -- USA | S0904 -- Translation-FC@Incoming Unit |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX05 | Belgium | Belgium | EUR -- European Euro | BE -- Belgium | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX06 | Japan | Japan | JPY -- Japanese Yen | JP -- Japan | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX07 | Austria | Austria | EUR -- European Euro | AT -- Austria | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX08 | China | China | CNY -- Chinese Yuan Renminbi | CN -- China | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| 999999 | Company 999999 | Company 999999 | EUR -- European Euro |  |  |  | U -- No Integration | SRD2 |  |  |  |  |  |  |

Table 14: Consolidation Units in the Consolidation Group CGRXX in Versions J1S

| *Consolidation Unit (18) | Consolidation Unit Description (15) | Consolidation Unit Medium Description (30) | *Local Currency (5) | Country (3) | Currency Translation Method (5) | Tax Rate (8) | Universal Journal Integration (1) | Upload Method (5) | Data Collection Selection (30) | Posting Rule Selection (30) | Partner Selection (30) | Validation Selection (30) | Link Title (255) | Link URL (1333) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MXX00 | Germany | Germany | EUR -- European Euro | DE -- Germany | S0903 -- Standard translation Periodic | 35 | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX01 | USA North | USA North | USD -- United States Dollar | US -- USA | S0904 -- Translation-FC@Incoming Unit |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX02 | France | France | EUR -- European Euro | FR -- France | S0903 -- Standard translation Periodic | 39 | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX03 | USA East | USA East | USD -- United States Dollar | US -- USA | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX04 | USA West | USA West | USD -- United States Dollar | US -- USA | S0904 -- Translation-FC@Incoming Unit |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX05 | Belgium | Belgium | EUR -- European Euro | BE -- Belgium | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX06 | Japan | Japan | JPY -- Japanese Yen | JP -- Japan | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX07 | Austria | Austria | EUR -- European Euro | AT -- Austria | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |
| MXX08 | China | China | CNY -- Chinese Yuan Renminbi | CN -- China | S0903 -- Standard translation Periodic |  | U -- No Integration | SRD2 |  |  |  |  |  |  |

#### Set up Group Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain your created consolidation group structure to manage rule-based COI approach.

The achieved result has the following group structure. The group structures of the version J10, J1R, J20, J2R are the same, which are different from that of version J1S.

|  |
| --- |
| Note Adjust the IDs of the consolidation group/consolidation units provided in this file to your own IDs. Please replace XX with your own group number. |

Table 15: Group Structure in Versions J10, J1R, J20, J2R

| Consolidation Group (18) | Consolidation Unit (18) | Start of Assignment (YYYY/PPP) | End of Assignment (Derived Automatically During Upload) | *First Consolidation (YYYY/PPP) | First Consolidation at End of Period (1) | *Divestiture (YYYY/PPP) | Divestiture at Beginning of Period (1) | Divestiture due to Merger (1) | Start of Method Assignment (Ignored during Upload) | End of Method Assignment (Ignored during Upload) | Effective Fiscal Year Period for Method Change (YYYY/PPP) | Method Change at Beginning of Period (1) | Consolidation Method (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CGRXX | MXX00 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 00 -- Parent (Direct Shares) |
| CGRXX | MXX02 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX03 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX04 | 2025/012 | 9999/999 | 2026/001 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX05 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 20 -- Equity Method (Direct Shares) |
| CGRXX | MXX06 | 2025/012 | 2026/016 | 2025/012 | No | 2026/001 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX07 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX08 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |

Table 16: Group Structure in Versions J1S

| *Consolidation Group (18) | *Consolidation Unit (18) | *Start of Assignment (YYYY/PPP) | End of Assignment (Derived Automatically During Upload) | *First Consolidation (YYYY/PPP) | First Consolidation at End of Period (1) | *Divestiture (YYYY/PPP) | Divestiture at Beginning of Period (1) | Divestiture due to Merger (1) | Start of Method Assignment (Ignored during Upload) | End of Method Assignment (Ignored during Upload) | Effective Fiscal Year Period for Method Change (YYYY/PPP) | Method Change at Beginning of Period (1) | Consolidation Method (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CGRXX | MXX00 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 00 -- Parent (Direct Shares) |
| CGRXX | MXX01 | 2025/012 | 9999/999 | 2026/001 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX02 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX03 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX04 | 2025/012 | 9999/999 | 2026/001 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX05 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 20 -- Equity Method (Direct Shares) |
| CGRXX | MXX06 | 2025/012 | 2026/016 | 2025/012 | No | 2026/001 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX07 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |
| CGRXX | MXX08 | 2025/012 | 9999/999 | 2025/012 | No | 9999/999 | No | No |  |  |  |  | 10 -- Purchase Meth. (Direct Shares) |

Procedure Options

There are two procedure options for reviewing and maintaining the group structure. Review both before proceeding.

The first option uses the Import Consolidation Master Data (F3924) SAP Fiori app.

The second option uses the Manage Group Structure - Group View (F3733) SAP Fiori app.

Option 1 - Using the Import Consolidation Master Data SAP Fiori App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Note There are two options for reviewing and maintaining the group structure. Review both before proceeding.Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Import Consolidation Master Data (F3924). | The Import Consolidation Master Data view is displayed. |  |
| 3 | Navigate to Master Data | Under the Master Data Types, select the Consolidation Group Structure row, and choose Download Master Data. | A Download Master Data dialog box is displayed. |  |
| 4 | Download | Enter the following values:Consolidation Version: J10Note To maintain the group structure for the version J1S, change the input of Version to J1S.Choose Download. | An xlsx file with consolidation unit master data is downloaded. |  |
| 5 | Review and Maintain Master Data | Open the downloaded file.Delete the Consolidation Groups and Consolidation Units that are not used in your testing. Maintain your own consolidation unit assignments and settings as the same as those in the table in the above Purpose section.Remember replace the XX with your tester ID.Save the file. | The downloaded file contains the correct data for the consolidation units relevant for your test.There are two files ready for your testing, one is for J10 version and the other is for J1S version. |  |
| 6 | Upload | On the Import Consolidation Master Data view, choose the Upload button.On the Upload dialog box, either drag and drop your file on to the dialog or select the Upload button to navigate to the file. | The updated file is uploaded. |  |
| 7 | View Details | Select the Consolidation Group Structure row on the Import Consolidation Master Data view to view the details. | A details view appears. |  |
| 8 | Verify Upload | Select the field help of the Consolidated Group filter and in the dialog box, search for and select the multiple consolidation groups that are relevant for your test. Choose OK and those consolidation units display in the table.In the Status column, choose To Be Checked for your relevant rows and choose Check Selected at the right of the table. | The status for your consolidation groups update. |  |
| 9 | Correct Errors | Note If the Check Selected run results in successful results, skip this step.When Checked with Errors status appears or other warnings display, it is necessary to correct the data before proceeding.Select the checkboxes for the rows with errors and choose the Download button.A spreadsheet downloads with the selected records.Open the file and correct the data.When the update is complete, choose the Upload button.On the Upload dialog box, either drag and drop the file or choose the Upload button to navigate to the file location and choose OK.Rerun the previous step and repeat until all groups show a successful status. | A successful check result for all of the consolidation groups is displayed. |  |
| 10 | Import Master Data | Select all of the checkboxes for your relevant consolidation groups.Choose the Import Selected button. | The master data of the relevant consolidation groups is imported from your personal staging area to the master data tables of the consolidation. Master data of the consolidation groups is now ready for testing. |  |

Option 2 - Using the Manage Group Structure - Group View SAP Fiori App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related app is launched. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Consolidation Group: CGRXXRemember replace the XX with your group number.Version: J10Fiscal year: 2025Period: 12Note To maintain the group structure for the version J1S, change the input of Version to J1S. | The SAP Fiori launchpad is displayed. |  |
| 4 | Access the SAP Fiori App | Open Manage Group Structure - Group View (F3733). | The Manage Consolidation Group Structure - Group view displays with a list of Assignments of Units to Groups. |  |
| 5 | Review Existing Unit Assignments | Review if your consolidation unit assignments have already existed.If yes, leave unchanged of those assignments that are the same as what appears in the table in the Purpose section.For more assignments that are not part of the table in the Purpose section, select the checkboxes for the rows of those assignments and choose Remove.For assignments that deviate in their settings from the table in the Purpose section, double-click the row of deviating assignments in the table, then choose Edit and maintain the values of the assignment according to the table in the Purpose section.Choose Save.If the assignments haven’t been done, skip this step. |  |  |
| 6 | Create Missing Assignments | Choose Assign. | The Assign Consolidation Units dialog is displayed. |  |
| 7 | Select Units | Select all consolidation units with IDs starting with MXX .Remember Replace the XX with the group number. Use search field to filter the value of the relevant consolidation units. | All relevant consolidation units are selected. |  |
| 8 | Next | Choose Next. | A different Assign Consolidation Untis dialog box is displayed. |  |
| 9 | Adjust Assignments | Enter or validate the appropriate values for First Consolidation, Divestiture, and Consolidation Method. | The Assign button is activated. |  |
| 10 | Assign Consolidation Method | Choose Assign. | The newly assigned consolidation units are displayed in the list report. |  |
| 11 | Create More Unit Assignments | If necessary, continue assigning other consolidation units.Repeat above steps to maintain consolidation group structure for version J1S. | The consolidation group structure is ready for testing. |  |

#### 2025.12 Initial Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the initial consolidation for 12/2025.

Procedure - Data Monitor

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) . | The Configure Your Solution view displays. |  |
| 3 | Select the Relevant App | Navigate to Configure Your Solution.Enter the following entries and choose Go.Application Area: FinanceSub Application Area: Corporate Close | Consolidation Configuration Steps are filtered. |  |
| 4 | Select Basic Settings | In the filter result, choose Basic Settings. | Consolidation Configuration Steps are filtered. |  |
| 5 | Set Global Parameters | Choose Set Global Parameters.Set the following parameters:Organizational Units area:Cons Group: CGRXX, replace the XX with your assigned groupCons Unit: <leave blank>Version/Time period area:Version: J10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. |  |  |
| 6 | Select Data Processing | Go back and in the filter result, choose Data Processing. | Consolidation Configuration Steps are filtered. |  |
| 7 | Assign Task Group to Version | Choose Assign Task Group to Version. |  |  |
| 8 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period: 12Period Category: 9Data mon. task group: S10Cons mon. task group: S20Note Skip the step if the entry already exists. |  |  |
| 9 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 10 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 11 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S1080Version: J10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 12 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: J10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 13 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 14 | Access Data Monitor | Open Data Monitor (CXCD).Select your group CGRXX and choose Menu > Edit > Open period. | The Data Monitor view is displayed. |  |
| 15 | Flexible Upload of Reported Financial Data | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC).Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J1R_J2R_UPLOAD_2025_12_SRD2_DT_00.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: CGRXX_J10_J1R_J2R_UPLOAD_2025_12_SRD2_DT_00Choose Execute.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2025_12_SRD2__0BChoose Execute. | The data files are uploaded successfully. |  |
| 16 | Access Data Monitor | Go back to the home page and open Data Monitor (CXCD) again. | The Data Monitor view is displayed. |  |
| 17 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 18 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected results. |  |
| 19 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 20 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 21 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update Run of the task Man.Std.10. Post documents separately for each unit.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J20_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload. To upload the manual journal entries, use the data rows in the provided template.Select the journal entries, choose Check and then Post.Remember Replace the XX in the columns *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Rule Based COI 2025.12 Initial Consolidation, SAP Central Business Configuration path step 9 (unit level) assigns task S2980 to SBV_RG1 while the Configure Your Solution path assigns S1080 for the same unit-level step and then repeats for S1180.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Partial divestiture of MXX07 is described as 'capital decrease' (and MXX08 'capital increase') in the Rule Based COI scenario but as 'no capital decrease' / 'no capital increase' in the MGC scenario; MXX07 share goes 90%->70% in Tables 9 and 11 but 90%->80% in J1S (Table 12).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Integrated intercompany Configure Your Solution journal entry template uses transaction currency USD for company 1710 (local currency USD per the unit table) although the note requires a transaction currency different from local currency; the Central Business Configuration path uses EUR.

> [!warning] Conflict
> Flagged while digesting this document, not verified: MXX04 Start of Assignment is 2026/001 in the Rule Based COI group structure but 2025/012 in the MGC group structures (Tables 15 and 16), with First Consolidation 2026/001 in both.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-02]]
- see-also :: [[03-financial-accounting-and-close/journal-entry-template-40y-193]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx` — lines 1–1722 of the extracted text · extracted with `mammoth` · 329,699 chars in the whole document
