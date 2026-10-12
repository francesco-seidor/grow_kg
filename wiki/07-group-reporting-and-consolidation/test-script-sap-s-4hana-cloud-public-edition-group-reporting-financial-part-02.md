---
id: 07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-02
title: Test Script SAP S/4HANA Cloud Public Edition - Group Reporting – Financial Consolidation (1SG) (1SG_S4CLD2608_BPD_EN_XX) — part 2 of 2
description: "SAP test script for Group Reporting consolidation (1SG): monitor runs 12/2025-02/2026, reports, configuration, org structure, master data, validation."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/financial-consolidation-process, topic/intercompany-matching-and-reconciliation]
aliases: []
keywords: [Financial Consolidation Process, data monitor, consolidation monitor, initial consolidation, full consolidation, subsequent consolidation, flexible upload, group data analysis, balance sheet reports, p&l by nature of expense]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx#lines-1723-2232"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-763
topic: 07-group-reporting-and-consolidation/financial-consolidation-process
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Group Reporting – Financial Consolidation (1SG) (1SG_S4CLD2608_BPD_EN_XX) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx`, part 2 of 2 (lines 1723–2232 of the extracted text), extracted with `mammoth`. Grouped under **Financial Consolidation Process** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 22 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell for your item and choose Update Run in the toolbar. | No warning / no error. |  |
| 23 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 24 | Block Tasks | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 25 | Exit | Choose Back to exit. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The General Settings screen displays. |  |
| 3 | Set Global Parameters | Set the following parameters:Organizational Units area:Cons Group: CGRXX, replace the XX with your assigned groupCons Unit: <leave blank>Version/Time period area:Version: J10Fiscal year: 2025Period: 12Further settings area:Cons. COA: Y1Choose Continue. |  |  |
| 4 | Select Assign Task Group to Version | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Task Group to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | Consolidation Configuration Steps are filtered. |  |
| 5 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Make the following entries and choose Save:Start Year: 2025Period: 12Period Category: 9Data mon. task group: S10Cons mon. task group: S20Note Skip the step if the entry already exists. |  |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access the SAP Fiori App | Open Assign Rule Group for Balance Validation - Group Reporting (F8138) SAP Fiori app. | The Assign Rule Group For Balance Validation view is displayed. |  |
| 8 | Assign Rule Group for Balance Validation at Unit Level | Choose Create and make the following entries:Task: S1080Version: J10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Unit Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG1Remember Repeat the step to assign the task S1180 to the same consolidation unit selection and validation rule group.Note Ignore the step if the rule group SBV_RG1 has already been assigned to task S1080 and S1180. |  |  |
| 9 | Assign Rule Group for Balance Validation at Group Level | Choose Create and make the following entries:Task: S2980Version: J10Valid From: 2025012Choose Continue.Enter the following entries:Consolidation Group Selection: <leave blank>Periods: <select all periods>Validation Rule Group: SBV_RG2Note Ignore the step if the rule group SBV_RG2 has already been assigned to task S2980. |  |  |
| 10 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 11 | Access Data Monitor | Open Data Monitor (CXCD).In the Hierarchy column, assign validation method column, choose the group CGRXX and choose More > Edit > Open period. | The Data Monitor view is displayed. |  |
| 12 | Flexible Upload of Reported Financial Data | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC).Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J1R_J2R_UPLOAD_2025_12_SRD2_DT_00.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: CGRXX_J10_J1R_J2R_UPLOAD_2025_12_SRD2_DT_00Choose Execute.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2025_12_SRD2_DT_0B.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2025_12_SRD2__0BChoose Execute. | The data files are uploaded successfully. |  |
| 13 | Access Data Monitor | Go back to the home page and open Data Monitor (CXCD) again. | The Data Monitor view is displayed. |  |
| 14 | Data Monitor - Balance Carry Forward | This task does not require execution. |  |  |
| 15 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected results. |  |
| 16 | Data Monitor - Calculate Net Income | In the Calc Net I task, select the cell for your item and choose Update Run in the toolbar. | No warning / no error. |  |
| 17 | Data Monitor - Validation for Reported Data | In the Val.Rpt.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 18 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units in the Man.Std.10 task and choose Update Run to post document.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J20_MJE_2025_12_PL_10.xlsx) and verify that the template has the same settings before you run the upload. To upload the manual journal entries, use the data rows in the provided template.Select the journal entries, choose Check and then Post.Remember Replace the XX in the columns *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 19 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell for your item and choose Update Run in the toolbar. | No warning / no error. |  |
| 20 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 21 | Block Tasks | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 22 | Exit | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: J10Consolidation Group: CGRXXProcess Year Period: 012//2025 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Access SAP Fiori App | Open Group Data Analysis (W0135) |  |  |
| 8 | Enter Criteria | Choose Adapt Filters.Make the following entries and choose Go:Version: J10, J1R, J20, J2RConsolidation COA: Y1Fiscal Year Period: 012.2025Consolidation Group: CGRXXPeriod Mode: YTDKey Date: 31.12.2025Consolidation Unit Hierarchy: $Profit Center Hierarchy: $Segment Hierarchy: $ |  |  |
| 9 | Set Filter | In the Navigation Panel, select the field Version and choose Add field Version to column axis.In the Navigation Panel, select the field Document Type and choose Remove field Document Type from row axis.Note To save the layout you create as your default view, choose arrow button beside No Bookmark Loaded at the upper left of the screen, then choose Save as. Enter a name, and select With Filter Values, and then choose Save. | The report displays the Balance result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2025_12.xlsx). |  |
| 10 | Review Balance Sheet (Optional) | In the Navigation Panel, right-click the FS Item column and choose Hierarchy > Select Hierarchy. Choose item hierarchy Y1/BS and choose OK. |  |  |
| 11 | Display Sign-adjusted Balance Sheet | Choose Filter > Show Additional Filters > Add Filter.Select the field Measures, and then choose Insert New Row. Select the value Sign-Adjusted Amount in Group Crcy for the new row.Choose OK.Note Save the layout you created and enter a new name for sign-adjusted Balance Sheet. | The report displays the result. Review the sign-adjusted Balance Sheet outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2025_12.xlsx). |  |
| 12 | Consolidate Balance Sheet by the Consolidation Unit (Optional) | Now drag the Consolidation Unit dimension to the axis column. Verify that all consolidation units selected are displayed in group currency. | The report displays consolidation units in columns and FS items on rows. |  |
| 13 | Review Sign-adjusted P&L (Optional) | Right-click the FS Item in Navigation Panel and choose Hierarchy > Disable Hierarchy.Choose Hierarchy > Select Hierarchy. Choose Item hierarchy PL and choose OK.Note Save the layout you created and enter a new name for sign-adjusted P&L. | The report displays the result. Review the sign-adjusted P&L outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2025_12.xlsx). |  |

#### 2026.01 Full Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the full consolidation for 01/2026.

Procedure - Data Monitor

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related screen is displayed. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons Group: CGRXXRemember Change the XX to your group number.Cons Unit: NAVersion: J10Fiscal year: 2026Period: 01Cons. COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor - Open Period | Right-click subgroup CGRXX and choose Open period. |  |  |
| 6 | Data Monitor - Balance Carry Forward | In the Data Monitor view, right-click the Bal.Cfwd task for your consolidation group and choose Update or choose Update Run in the toolbar. | No error. |  |
| 7 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 8 | Flexible Upload of Reported Financial Data | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC).Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2026_01_SRD2_DT_00.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2026_01_SRD2_00Choose Execute.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2026_01_SRD2_DT_0B.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2026_01_SRD2_0BChoose Execute. | The data files are uploaded successfully. |  |
| 9 | Access the SAP Fiori App | Go back to the home page and open Data Monitor (CXCD). |  |  |
| 10 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 11 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 12 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 13 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update Run of the task Man.Std.10. Post documents separately for each unit.Option 2As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) SAP Fiori app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J20_MJE_2026_01_PL_10.xlsx) with version J10 and J20. Before uploading the file, please verify that the attached file has the same settings.Select the journal entries, choose Check and then Post.Remember Replace the XX in the columns *Consolidation Unit (18), Remarks (50) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 14 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell for your item and choose Update Run in the toolbar. |  |  |
| 15 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 16 | Data Monitor - Block | Select the row of each task and choose Block to block each task.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 17 | Data Monitor - Exit | Choose Back to exit. |  |  |
| 18 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related screen displays. |  |
| 19 | Set Global Parameters | Set the following global parameters:Cons. Group: CGRXXRemember Change the XX for your values.Cons. Unit: NAVersion: J1SFiscal year: 2026Period: 01Cons COA: Y1 |  |  |
| 20 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 21 | Access the SAP Fiori App | Open Manage Your Solution (F1241) . | The Configure Your Solution view displays. |  |
| 22 | Select the Relevant App | Navigate to Configure Your Solution.Choose Finance for Application Area and Corporate Close for Sub Application Area.Choose Go. | Consolidation Configuration Steps are filtered. |  |
| 23 | Select Data Processing | In the filter result, choose Data Processing. | Consolidation Configuration Steps are filtered. |  |
| 24 | Define Task Group | Choose Configure of the configuration activity Define Task Group. |  |  |
| 25 | Define Task Group J10 | Select S10 and choose Copy As…. Enter the following entries:Task group: for example J10Description: Data monitor (Restatement)Choose Copy > Copy all > Continue.Select J10 task group, double click Assign tasks to task group.Keep task 1010, 1020, 1050, S1080, 1095, 1100, S1180. Select other remaining tasks, and choose Delete > all entries .Check that the Task S1180 is selected as Last task, DM.Choose Save.Choose Back.Note In Data Monitor, task groups for extension versions with Manual run mode cannot have Release of Universal Journals and Line Item Validation tasks. These tasks aren’t supported for extension versions with Manual run mode. |  |  |
| 26 | Assign Task Group to Version | Go back to Data Processing view and choose Assign Task Group to Version. |  |  |
| 27 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Choose New Entries, make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: J10Cons mon. task group: S20 |  |  |
| 28 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 29 | Data Monitor for version J1S | Repeat above steps from the task Data Collection to Validation for Standardized Data in Data Monitor for the version J1S.Note Please don't run the Balance Carryforward task for the version J1S.For the task Data Collection, use the sample files of [DT00](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_00.xlsx) and [DT0B](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B.xlsx) for J1S.For the task Data Monitor - Manual Posting PL10, use the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_MJE_2026_01_PL_10.xlsx) for the version J1S. |  |  |
| 30 | Data Monitor - Block | Select the row of each task and choose Block to block each task.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 31 | Exit Data Monitor | Choose Back to exit. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related screen is displayed. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons Group: CGRXXRemember Change the XX to your group number.Cons Unit: NAVersion: J10Fiscal year: 2026Period: 01Cons. COA: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor - Open Period | Right-click subgroup CGRXX and choose Open period. |  |  |
| 6 | Data Monitor - Balance Carry Forward | In the Data Monitor view, right-click the Bal.Cfwd task for your consolidation group and choose Update or choose Update Run in the toolbar. | No error. |  |
| 7 | Data Monitor - Release Universal Journal | This task does not require execution. |  |  |
| 8 | Flexible Upload of Reported Financial Data | Open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC).Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2026_01_SRD2_DT_00.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2026_01_SRD2_00Choose Execute.Download and edit the [Sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2026_01_SRD2_DT_0B.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2026_01_SRD2_0BChoose Execute. | The data files are uploaded successfully. |  |
| 9 | Access the SAP Fiori App | Go back to the home page and open Data Monitor (CXCD). |  |  |
| 10 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 11 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 12 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 13 | Data Monitor - Manual Posting PL10 | Option 1Select your consolidation units and choose Update Run of the task Man.Std.10. Post documents separately for each unit.Option 2Upload the manual journal entries using the Import Group Journal Entries (F3073) app.Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J20_MJE_2026_01_PL_10.xlsx) and verify that the template has the same settings before you run the upload.Replace the XX with your assigned consolidation group and save as an xlsx, like the downloaded template.Choose Browse to select the adjusted file, check the journal entries and choose Post.Remember Replace the XX in the columns *Consolidation Unit (18), Remarks (50) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 14 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell for your item and choose Update Run in the toolbar. |  |  |
| 15 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 16 | Data Monitor - Block | Select the row of each task and choose Block to block each task. |  |  |
| 17 | Data Monitor - Exit | Choose Exit. |  |  |
| 18 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related screen displays. |  |
| 19 | Set Global Parameters | Set the following global parameters:Cons. Group: CGRXXRemember Change the XX for your values.Cons. Unit: NAVersion: J1SFiscal year: 2026Period: 01Cons COA: Y1 |  |  |
| 20 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 21 | Open Assign Task Group to Dimension | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Task Group.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The General Settings screen displays. |  |
| 22 | Define Task Group J10 | Select S10 and choose Copy As…. Enter the following entries:Task group: for example J10Description: Data monitor (Restatement)Choose Copy > Copy all > Continue.Select J10 task group, double click Assign tasks to task group.Keep task 1010, 1020, 1050, S1080, 1095, 1100, S1180. Select other remaining tasks, and choose Delete > all entries .Check that the Task S1180 is selected as Last task, DM.Choose Save.Choose Back.Note In Data Monitor, task groups for extension versions with Manual run mode cannot have Release of Universal Journals and Line Item Validation tasks. These tasks aren’t supported for extension versions with Manual run mode. |  |  |
| 23 | Assign Task Group to Version | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Task Group to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 24 | Assign Monitor Task Groups | Assign the cons monitor task group for Rule-Based COI by creating a new entry.Choose New Entries, make the following entries and choose Save:Start Year: 2025Period eff: 12Period cat.: 9Data mon. task group: J10Cons mon. task group: S20 |  |  |
| 25 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 26 | Data Monitor for version J1S | Repeat above steps from the task Data Collection to Validation for Standardized Data in Data Monitor for the version J1S.Note Please don't run the Balance Carryforward task for the version J1S.For the task Data Collection, use the sample files of [DT00](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_00.xlsx) and [DT0B](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B.xlsx) for J1S.For the task Data Monitor - Manual Posting PL10, use the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_MJE_2026_01_PL_10.xlsx) for the version J1S. |  |  |
| 27 | Data Monitor - Block | Select the row of each task and choose Block to block each task.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 28 | Exit Data Monitor | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor - Set Filters | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: J10Consolidation Group: CGRXXProcess Year Period: 001/2026 |  |  |
| 4 | Consolidation Monitor - Manual Elimination PL30 (2150) | Select the task 2150 Manual Eliminations (PL 30) for your cons group and then choose Manual Run.In Journal Entry view, post documents.As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) SAP Fiori app and this [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_J20_MJE_2026_01_PL_30.xlsx) with version J10 and J20.Remember Replace the XX in the columns *Consolidation Group (18), Remarks (50), *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 5 | Consolidation Monitor - Remaining Tasks Execute | In the Consolidation Monitor view, select all the remaining tasks for your testing cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 6 | Consolidation Monitor Block | In the Consolidation Monitor view, choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 7 | Consolidation Monitor - Set Filters | To run consolidation monitor tasks for version J1S, maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: J1SConsolidation Group: CGRXXProcess Year Period: 001/2026 |  |  |
| 8 | Consolidation Monitor - Manual Elimination PL30 (2150) | Select the task 2150 Manual Eliminations (PL 30) and then choose Manual Run.In Journal Entry view, post documents.As an alternative, upload the manual journal entries using the Import Group Journal Entries (F3073) SAP Fiori app and this [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J1S_MJE_2026_01_PL_30.xlsx) with version J1S.Remember Replace the XX in the columns *Consolidation Group (18), Remarks (50), *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template. |  |  |
| 9 | Consolidation Monitor - Remaining Tasks Execute | In the Consolidation Monitor view, select all the remaining tasks for your testing cons group CGRXX, and then choose Actions > Update Run.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 10 | Consolidation Monitor Block | In the Consolidation Monitor view, choose Actions > Block on Request to block all the tasks. | The Completion of the Consolidation Monitor for version J1S turns to 100%. |  |
| 11 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 12 | Access the SAP Fiori App | Open Group Data Analysis (W0135).Note You may use the Search function to search for Group Data Analysis and select the title that shows Accessible. |  |  |
| 13 | Display Balance Amount | Choose the Balance layout you created in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters.Make the following entries and choose Go. Keep other entries remain the same.Version: J10, J1R, J20, J2R, J1SFiscal Year Period: 001/2026Key Date: 31.01.2026 | The report displays the Balance result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_01.xlsx).J1R is the same with J10.J2R is the same with J20. |  |
| 14 | Review Sign-adjusted Balance Sheet (Optional) | Choose the layout you created for sign-adjusted Balance Sheet in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Version: J10, J1R, J20, J2R, J1SFiscal Year Period: 001/2026Key Date: 31.01.2026 | The report displays the sign-adjusted Balance Sheet result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_01.xlsx).J1R is the same with J10.J2R is the same with J20. |  |
| 15 | Review Sign-adjusted P&L (Optional) | Choose the layout you created for sign-adjusted P&L in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Version: J10, J1R, J20, J2R, J1SFiscal Year Period: 001/2026Key Date: 31.01.2026 | The report displays the sign-adjusted P&L result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_01.xlsx).J1R is the same with J10.J2R is the same with J20. |  |

#### 2026.02 Subsequent Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the subsequent consolidation for 02/2026.

Procedure - Data Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The related view is displayed. |  |
| 3 | Set Global Parameters | Set the following global parameters:Cons Group: CGRXXRemember Change the XX for your group values.Cons Unit: NAVersion: J10Fiscal year: 2026Period:02Cons Chart of accounts: Y1 |  |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). |  |  |
| 5 | Data Monitor | Right-click subgroup CGRXX and choose Open Period. |  |  |
| 6 | Flexible Upload of Reported Financial Data | Go back to the home page and open Flexible Upload of Reported Financial Data (FINCS_UPL_EXEC).Download and edit the [sample file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J10_UPLOAD_2026_02_SRD2_DT_00.xlsx).Remember Replace XX in the columns ConsolidationUnit, PartnerConsolidationUnit and InvesteeConsolidationUnit in the file with your group number.In File section, choose below entries:Upload method: SRD2Physical file name: J10_UPLOAD_2026_02_SRD2_00Choose Execute. | No warning / no error. |  |
| 7 | Access the SAP Fiori App | Go back to the home page and open Data Monitor (CXCD). |  |  |
| 8 | Data Monitor - Release Universal Journal | This task does not require execution. | No expected result. |  |
| 9 | Data Monitor - LI Validation in Grp.Reporting | This task does not require execution. | No expected result. |  |
| 10 | Data Monitor - Calculate Net Income | In the Data Monitor view, select your cons group of the task NI Rpt. D and choose Update Run from the toolbar. | Logs for automatic postings display. |  |
| 11 | Data Monitor - Validation for Reported Data | In the Data Monitor view, select your cons group of the task Val.Rpt.D and choose Update Run from the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 12 | Data Monitor - Manual Posting PL10 | In the Data Monitor view, update the Manual Posting PL10 task and post documents.As an alternative, you can upload the manual journal entries with app Import Group Journal Entries (F3073).Download the [template](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/CGRXX_J20_MJE_2026_02_PL_10.xlsx) with version J20 before uploading the document and verify that the attached file has the same settings. For uploading the document, use the data rows in the attached file.Select the journal entries, choose Check and then Post.Note Replace the XX in the columns *Consolidation Unit (18) and Partner Unit (18) with your group number and save as an xlsx, like the downloaded template.For the other versions, you don't need to do the manual posting. |  |  |
| 13 | Data Monitor - Currency Translation | In the CurrTrans. task, select the cell for your item and choose Update Run in the toolbar. |  |  |
| 14 | Data Monitor - Validation for Standardized Data | In the Val.Std.D task, select the cell for your item and choose Update Run in the toolbar. | The status of Validation Results are Success with Warnings. |  |
| 15 | Block Data Monitor | Block each task by choosing the Block button.Note For tasks that are not executed, right click your cons group of the task and choose Block Upon User Request. |  |  |
| 16 | Exit Data Monitor | Choose Back to exit. |  |  |

Procedure - Consolidation Monitor

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Consolidation Monitor - New Version (F7271). |  |  |
| 3 | Consolidation Monitor | Maintain the following entries and choose Go.Consolidation Chart of Accounts: Y1Version: J10Consolidation Group: CGRXXProcess Year Period: 002/2026 |  |  |
| 4 | Run Tasks in Consolidation Monitor | Select all the tasks for your cons group CGRXX, and then choose Actions > Update Run.Or you can choose Run Full Consolidation to run all automatic tasks.Choose Go to refresh the page to verify the result.Choose > to check the task logs. | Tasks 2050, 2140, 2150 are manual tasks that don't execute, so the status are Initial.The status of tasks 2060 runs successfully with status Pending Completion of Preceding Task because its preceding task 2050 is not blocked yet. You can block the task 2050 and rerun the task 2060, the status will change to No Errors.Other tasks in Consolidation Monitor run successfully with status No Errors. |  |
| 5 | Consolidation Monitor Block | In the Consolidation Monitor view, select all the tasks and choose Actions > Block to block all the tasks. | The Completion of the Consolidation Monitor turns to 100%. |  |
| 6 | Consolidation Monitor Exit | In the Consolidation Monitor view, choose < (Back). |  |  |
| 7 | Access the SAP Fiori App | Open Group Data Analysis (W0135).Note You may use the Search function to search for Group Data Analysis and select the title that shows Accessible. |  |  |
| 8 | Display Balance Amount | Choose the Balance layout you created in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters.Make the following entries and choose Go. Keep other entries remain the same.Fiscal Year Period: 002/2026Key Date: 28.02.2026 | The report displays the Balance result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_02.xlsx).J1R is the same with J10.J2R is the same with J20. |  |
| 9 | Review Sign-adjusted Balance Sheet (Optional) | Choose the layout you created for sign-adjusted Balance Sheet in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Fiscal Year Period: 002/2026Key Date: 28.02.2026 | The report displays the sign-adjusted Balance Sheet result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_02.xlsx).J1R is the same with J10.J2R is the same with J20. |  |
| 10 | Review Sign-adjusted P&L (Optional) | Choose the layout you created for sign-adjusted P&L in [2025.12 Initial Consolidation](#unique_25) [page ] 144.Choose Adapt Filters to make following changes and choose Go. Keep other entries remain the same.Fiscal Year Period: 002/2026Key Date: 28.02.2026 | The report displays the sign-adjusted P&L result. Review the expected outcome [here](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/2608_Outputs_MGC_2026_02.xlsx).J1R is the same with J10.J2R is the same with J20. |  |

### Reporting

The following section provides procedures for testing reports. The procedures provided are only a small, select number of test cases to execute. To test reporting, we recommend that you consider creating other test cases and perform additional testing.

#### Balance Sheet (B/S) Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the balance sheet reports. The following balance sheet reports are provided in the local reports tile:

- Group Data Analysis

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Group Data Analysis (W0135). |  |  |
| 3 | Consolidated Balance Sheet | Make the following entries and choose Go:Version: A10Consolidation COA: Y1Fiscal Year Period: 012/2025Consolidation Group: CGRXXPeriod Mode: YTDKey Date: 31/12/2025Consolidation Unit Hierarchy: $Profit Center Hierarchy: $Segment Hierarchy: $ |  |  |
| 4 | Remove Document Type | In the Navigation Panel, choose Remove field Document Type from row axis. |  |  |
| 5 | Review Balance Sheet | In the Navigation Panel, right-click the FS Item column and choose Hierarchy > Select Hierarchy . Choose item hierarchy Y1/BS and choose OK. |  |  |
| 6 | Display Sign-adjusted Amount | Choose Filter > Show Additional Filters > Add Filter .Select the field Measures, and then select the value Sign-Adjusted Amount in Group Crcy from the dropdown list for the value.Choose OK.Note To save the layout you create as your default view, choose arrow button beside <No Bookmark Loaded> at the upper left of the screen, then choose Save as. Enter a name, and select With Filter Bar Values, and then choose Save. | Review the amounts with the expected outcome from the previous [2026.01 Full Consolidation](#unique_15) [page ] 93 procedure under the Consolidation Scenario Actual section. |  |
| 7 | Consolidate Balance Sheet by the Consolidation Unit | In the Navigation Panel, select consolidation unit and choose Add field Consolidation Unit to column axis. Verify that all of the consolidation units selected are displayed in group currency. | The report displays consolidation units in columns and FS items on rows. |  |
| 8 | Drill Down to Original Documents | On the right side of the screen, choose Navigate To > Display Group Journal Entries with Reporting Logic . | Journal entries list is displayed. |  |

#### P&L by Nature of Expense

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the P&L by nature of expense. In the group reports tile:

- Group Data Analysis

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Group Data Analysis (W0135). |  |  |
| 3 | Consolidate P&L by Nature of Expense | Make the following entries and choose Go:Version: A10Consolidation COA: Y1Fiscal Year Period: 012.2025Consolidation Group: CGRXXPeriod Mode: YTDKey Date: 31.12.2024Consolidation Unit Hierarchy: $Profit Center Hierarchy: $Segment Hierarchy: $ |  |  |
| 4 | Remove Document Type | In the Navigation Panel, choose Remove field Document Type from row axis. |  |  |
| 5 | Display Sign-adjusted Amount | Choose Filter > Show Additional Filters .Choose the Filter Amount in Group Crcy. In the Define Filter Values - Measure popup, change Amount in Group Crcy to Sign-Adjusted Amount in Group Crcy from the dropdown list for the value.Choose OK. |  |  |
| 6 | Review P&L Items | In the Navigation Panel, right-click the FS Item column and choose Hierarchy > Select Hierarchy . Choose item hierarchy Y1/PL and choose OK.Note To save the layout you create as your default view, choose arrow button beside <No Bookmark Loaded> at the upper left of the screen, then choose Save as. Enter a name, and select With Filter Bar Values, and then choose Save. | Review the amounts with the expected outcome from the previous [2026.01 Full Consolidation](#unique_15) [page ] 93 procedure under the Consolidation Scenario Actual section. |  |
| 7 | Drill Down to Original Documents | On the right side of the screen, choose Navigate To > Display Group Journal Entries with Reporting Logic . | Journal entries list is displayed. |  |

#### Cash Flow Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can generate a cash flow statement in the group reports tile:

- Group Data Analysis – With Reporting Rules

The below procedures are only to show you how to use the app. You can adjust the view as you need.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Group Data Analysis - With Reporting Rules (W0136). | A Group Data Analysis - With Reporting Rules view displays. |  |
| 3 | Enter Criteria | Make the following entries. Press Enter after each entry and choose Go:Version: A10Consolidation COA: Y1Fiscal Year Period: 001.2026Consolidation Group: CGRXXPeriod Mode: YTDKey Date: <31.01.2026>Consolidation Unit Hierarchy: $Profit Center Hierarchy: $Segment Hierarchy: $Rep. Item Hierarchy: X2Reporting Rule Var.: Y10 |  |  |
| 4 | Select Dimensions and Filter | In the Navigation Panel, select Reporting Item in the Available Fields and drag the Reporting Item to the top of the Rows dimension.In the Navigation Panel, select Document Type in the Rows and choose Remove field Document Type from row axis.Note To save the layout you create as your default view, choose arrow button beside <No Bookmark Loaded> at the upper left of the screen, then choose Save as. Enter a name, and select With Filter Bar Values, and then choose Save. | Review the amounts with the expected outcome from the previous [2026.01 Full Consolidation](#unique_15) [page ] 93 procedure. |  |
| 5 | Select Data in Details (Optional) | In the Data Analysis area, expand the hierarchy to display the reporting item SCF442 - Purchase of intangible assets (under SCF400).Right-click Reporting Item, and choose Filter > Select Filter Value . Then search the value SCF442 and choose OK.Right-click the Reporting Item SCF442 in the Data Analysis area, and choose Drill down > Add Drilldown .In the Navigation Panel, add Subitem to the column. | The report displays the detailed information of FS items and subitems under the reporting item SCF442. |  |
| 6 | Analyze Data (Optional) | In the Data Analysis area, use Filter > Show Additional Filters to filter the consolidation unit MXX04 and the posting level 00.In the Data Analysis area, filter the FS item 164200 and display the subitems in the column.Note To verify the configuration of the SCF442 reporting item, use the Define Reporting Rules (FINCS_RRULE) SAP Fiori app.Remember The Assignment for reporting items view displays the source FS items (in the B/S or P&L) and source subitems used to calculate the reporting item. |  |  |
| 7 | Display Journal Entries (Optional) | On the right side of the screen, choose Navigate To > Display Group Journal Entries with Reporting Logic . | Journal entries list displays. |  |

### Configuration App

The main purpose of this section is to demonstrate the configuration capability within the cloud consolidation solution. Most of the activities described in this section are optional, as long as there are no particular customizing points necessary. With the following procedures, you test the configuration options that exist. Use cautiously. Any change could affect the system processes.

#### Configuration Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, we list the activities for self-service configuration user interface. These activities are supposed to be run before solution go-live. All of the changes made using the self-service configuration UI can be recorded by the system to ensure that a content upgrade does not overwrite.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. |  |  |
| 2 | Access the SAP Fiori App | Choose Manage Your Solution (F1241).And then navigate to Configure Your Solution. | The Configure Your Solution view displays. |  |
| 3 | Select the Relevant App | Make the following entries:Application Area: FinanceSub Application Area: Corporate CloseChoose Go. | Consolidation SSCUIs are filtered. |  |
| 4 | Select Basic Settings (SSCUI Group) | In the filter result, choose Basic Settings. | Consolidation SSCUIs are filtered. |  |
| 5 | Set Global Parameter | Access Set Global Parameters and choose Configure on that row.Maintain the entries and choose Save.Go back to the original view.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 6 | Copy Version | Choose Configure of the step Create Version from Reference Version.Input the Template version and target version, deselect Test Run checkbox and choose Run.Go back to the original view. | New version is copied successfully. |  |
| 7 | Define Version | Choose Configure of the step Define Versions .Double-click the version you want to modify and change the value accordingly.Go back to the original view. | Version attribute is maintained. |  |
| 8 | Select Master Data (SSCUI Group) | In the filter result, choose Master Data. | Consolidation SSCUIs are filtered. |  |
| 9 | Configure Additional Characteristics | Choose Configure of the step Define Consolidation Master Data Fields.Change the attribute and attribute value accordingly.Go back to the original view. |  |  |
| 10 | Define FS Item Attribute | Choose Configure of the step Define FS Item Attribute Values.Change the attribute and attribute value accordingly.Go back to the original view. | FS Item attribute is maintained. |  |
| 11 | Subitem Maintenance | Choose Configure of the step Define Subitem Categories and Subitems.Input correct entries in the value field.Go back to the original view. | Subitem category and subitems are maintained. |  |
| 12 | Select Data Processing | In the filter result, choose Data Processing. | Consolidation SSCUIs are filtered. |  |
| 13 | Define Reclassification Methods | Choose Configure of the configuration step Define Reclassification Methods.Input correct entries in the value field.Go back to the original view. | Reclassification methods are modified. |  |
| 14 | Define Tasks | Choose Configure of the configuration step Define Reclassification Tasks.Choose the task and change the assigned methods.If changes of version selection are needed, please go to Edit Item Hierarchy configuration activity and change the global parameter.Go back to the original view. |  |  |
| 15 | Assign Monitor Task Groups | Choose Configure of the step Assign Task Group to Version.Choose the assigned data monitor task group and cons monitor task group.If changes of version selection are needed, please go to Set Global Parameters in SSCUI and change the global parameters.Go back to the original view. |  |  |
| 16 | Select Planning | In the filter result, select Planning. | Consolidation SSCUIs are filtered. |  |
| 17 | Define Consolidation Cycle (Option) | Choose Configure of the step Define Consolidation Cycle.Choose New Entries to create a new cycle or change accordingly.Go back to the original view. | This SSCUI is only valid when plan consolidation is selected.Consolidation cycle is maintained. |  |
| 18 | Assign Cons Cycle to Version (Optional) | Choose Configure of the step Assign Consolidation Cycle to Version.Choose the corresponding cons cycle to be assigned to the version. | This SSCUI is only valid when plan consolidation is selected.Consolidation cycle is maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Global Parameters | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Global Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Change Global Parameter | Set the global parameters and choose Save.Go back to the original view.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 4 | Open Create Version from Reference Version in Consolidation | Search for the configuration activity: Create Version from Reference Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Version from Reference Version in Consolidation screen displays. |  |
| 5 | Copy Version | Input the Template version and target version, deselect Test Run checkbox and choose Run.Go back to the original view. |  |  |
| 6 | Define Version | Search for the configuration activity: Define Versions .Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Double-click the version you want to modify and change the value accordingly.Go back to the original view. | Version attribute is maintained. |  |
| 7 | Specify Selected FS Items for Automatic Posting | Search for the configuration activity: Specify Selected FS Items for Automatic Posting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Change the default value and Save. |  |  |
| 8 | Configure Additional Characteristics | Search for the configuration activity: Define Consolidation Master Data Fields.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Change the attribute and attribute value accordingly.Go back to the original view. |  |  |
| 9 | Define FS Item Attribute | Search for the configuration activity: Define FS Item Attributes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Change the attribute and attribute value accordingly.Go back to the original view. | FS Item attribute is maintained. |  |
| 10 | Subitem Maintenance | Search for the configuration activity: Define Subitem Categories and Subitems.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Input correct entries in the value field.Go back to the original view. | Subitem category and subitems are maintained. |  |
| 11 | Define Reclassification Methods | Search for the configuration activity: Define Reclassification Methods.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Input correct entries in the value field.Go back to the original view. | Reclassification methods are modified. |  |
| 12 | Define Tasks | Search for the configuration activity: Define Reclassification Tasks.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose the task and change the assigned methods.If changes of version selection are needed, please go to Set Global Parameters activity and change the global parameters.Go back to the original view. |  |  |
| 13 | Assign Monitor Task Groups | Search for the configuration activity: Assign Monitor Task Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose the assigned data monitor and cons monitor.If changes of version selection are needed, please go to the activity Set Global Parameters and change the global parameters.Go back to the original view. |  |  |
| 14 | Define Consolidation Cycle (Option) | Search for the configuration activity: Define Consolidation Cycle.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose New Entries to create a new cycle or change accordingly.Go back to the original view. | This configuration activity is only valid when plan consolidation is selected.Consolidation cycle is maintained. |  |
| 15 | Assign Cons Cycle to Version (Optional) | Search for the configuration activity: Assign Consolidation Cycle to Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose the corresponding cons cycle to be assigned to the version.Go back to the original view. | This configuration activity is only valid when plan consolidation is selected.Consolidation cycle is maintained. |  |

#### Organization Structure Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create consolidation units and groups.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Global parameters dialog box displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: <leave empty>Cons. Unit: <leave empty>Version: Y10Fiscal Year: 2025 <The year you are testing>Period: 12 <The period you are testing>Cons. COA: Y1 | The SAP Fiori launchpad displays. |  |
| 4 | Access the SAP Fiori App | Open Define Consolidation Units (F4685). | The Define Consolidation Units view displays. |  |
| 5 | Create Units for Data Integration | In this step, you create units for Data Integration for use with the previous procedure.Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.The unit is used for accounting integration, select a company that exists in the system and type the same name for unit name.Choose Create and enter a Consolidation Unit in the Create Consolidation Unit dialog box. Press Enter and choose Create.In the tab General Information, input Consolidation Unit Description and Local currency (for example Palo Alto, USD).In the tab Time- and Version-Dependent Attributes, input S0903 for field Currency Translation Method.Choose Transfer from Universal Journal for Universal Journal Integration and enter the integrated company code.Ignore the warning and choose Save. |  |  |
| 6 | Create Units for Flexible Upload | In this step, you create units for Flexible Upload for use with the previous Consolidation Scenario Actuals section.Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.To run the test, you create the following eight units:Mxx00 EUR GermanyMxx02 EUR FranceMxx03 USD USA EastMxx04 USD USA WestMxx05 EUR BelgiumMxx06 JPY JapanMxx07 EUR AustriaMxx08 CNY ChinaChoose Create and enter a Consolidation Unit. Press Enter and choose Create.In the tab General Information, input Consolidation Unit Description and Local currency (for example Mxx00, Germany).In the tab Time- and Version-Dependent Attributes, input S0903 for field Currency Translation Method.Choose No integration for Universal Journal Integration.Ignore the warning and choose Save. |  |  |
| 7 | Create Consolidation Group | Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.Open Define Consolidation Groups (F7959).Choose Create.In the Create Consolidation Group popup, enter the ID of your consolidation group CGRXX.Please replace the XX with your own tester ID.Then choose Create.In the Basic Data tab, input following entries:Consolidation Group Description: <for example, the consolidation group name you create, CGRXX>Consolidation Group Medium Description: <for example, the consolidation group name you create, CGRXX>Choose Save. |  |  |
| 8 | Assign Units to Group (Accounting Integration) | Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.Open Manage Group Structure - Group View (F3733).Input one name (for example, CG2) for Consolidation Group and choose Go.Choose Assign and assign the unit you created for flexible upload.In the Assign Consolidation Units dialog box, make following entries:Period of First Consolidation: 012Year of First Consolidation: 2025Period of Divesture: 999Year of Divesture: 9999Choose 10 for Consolidation Method and choose Assign. |  |  |
| 9 | Assign Units to Group (Flexible Upload) | Note This step creates demo data. If you want project-specific settings, you must adapt your requirements.Open Manage Group Structure - Group View (F3733).Input one name (for example, CGRXX) for Consolidation group and choose Go.Choose Assign and assign the unit you created for flexible upload.All the Mxx0x created should be assigned:Mxx00 2025.12-9999.999 00Mxx02 2025.12-9999.999 10Mxx03 2025.12-9999.999 10Mxx04 2025.12-9999.999 10Mxx05 2025.12-9999.999 20Mxx06 2025.12-2026.01 10Mxx07 2025.12-9999.999 10Mxx08 2025.12-9999.999 10Choose Save. |  |  |

#### Master Data Configuration with SAP Fiori UI

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define and update Master Data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | A Global Parameters dialog box displays. |  |
| 3 | Enter Data | Make the following entries and choose Continue:Cons. Group: <blank>Cons. Unit: <blank>Version: A10Fiscal Year: For example, 2025 <The year you are testing>Period: For example, 12 <The period you are testing>Cons. COA: Y1 | The dialog box closes and SAP Fiori launchpad displays. |  |
| 4 | Export FS Items | Open Import Consolidation Master Data (F3924), find the row Financial Statement Item, choose Actions > Download Master Data > Download . | The FS item displays in the Download Master Data dialog box. |  |
| 5 | Import FS Item Master Data | Open Import Consolidation Master Data (F3924), choose Upload and then upload the updated file. After that, choose the row Financial Statement Item and then select the necessary rows. Choose Check and Import.To check the imported FS Item, Open Define FS Items (F3297) to check the FS item detailed definition. | The FS items are imported. |  |
| 6 | Access the SAP Fiori App | Open Manage Consolidation Hierarchies (F7995). |  |  |
| 7 | Update FS Item Hierarchy | Choose Consolidation Financial Statement Item for Type and choose Go.In the hierarchy list, choose one hierarchy and choose Export/Import > Export to Spreadsheet .In the exported hierarchy, maintain the spreadsheet and then import the hierarchy. | FS Item hierarchy is imported. |  |
| 8 | Access the SAP Fiori App | Open Map FS Items with G/L Accounts (F3333). |  |  |
| 9 | Maintain FS Item Mapping Data | Choose YCOA for G/L Chart of Accounts and Y1 for Consolidation COA and choose Go.The existing mapping between the chart of accounts displays.Select an existing mapping between chart of accounts and choose Export.You can review the mapping in local file.Maintain the local file and choose Import, and you can import the new FS item mapping.Select one of the mappings and choose Copy.You can copy one new mapping revision. | The FS item mapping is imported. |  |
| 10 | Assign FS Item Mapping | Open Assign FS Item Mappings (F3334). | New FS item mappings are listed. |  |
| 11 | Access the SAP Fiori App | Open Manage Consolidation Hierarchies (F7995). |  |  |
| 12 | Manage Global Accounting Hierarchies | Choose Create and make the following entries:Type: <a Consolidation segment>Hierarchy ID: ZSEG_01Hierarchy Description: <description of the hierarchy>Valid From: 01.01.2025.Valid to: 31.12.9999Choose Create with ID 1000_A, 1000_B, and 1000_C. | The Hierarchy for segment is enabled via SSCUI Define Consolidation Master Data Fields.You can also check other fields to enable other hierarchies. |  |
| 13 | Access the SAP Fiori App | Open Subitems List (CX1S1). | All of the subitems in the system are listed. |  |
| 14 | Execute Subitems | Choose Run. | The List SAP Consolidation Master Data: Subitems view displays |  |
| 15 | Access the SAP Fiori App | Open Define Master Data for Consolidation Fields (F3007). |  |  |
| 16 | Generic Master Data Maintenance | In the Define Master Data for Consolidation Fields table, choose the master data to display the detailed view.In the consolidation master data table, choose Create to enter new master data.In the accounting master data table, you can review all the master data existing in accounting module. | Available master data is configured. |  |
| 17 | Access the SAP Fiori App | Open Assign Reporting Rules to Versions (FINCS_RRLVS). |  |  |
| 18 | Assign Reporting Rules to Versions | Choose Edit and choose New Entries.Input the values accordingly. | Reporting rules are assigned. |  |
| 19 | Access the SAP Fiori App | Open Define Reporting Rules (FINCS_RRULE). |  |  |
| 20 | Define Reporting Rules | Make the following entries:Cons. COA: Y1Rep Item Hierarchy: X1, X2Reporting Rule Variant: <Y10 or others>Choose Display and maintain the reporting item accordingly. | Reporting rules are maintained. |  |
| 21 | Access the SAP Fiori App | Open Import Consolidation Master Data (F3924). |  |  |
| 22 | Download Master Data | Select a Master Data Type, for example Profit Center and then choose Download Template. | Template downloads. |  |
| 23 | Maintain the Template Master Data for Consolidation Fields | Maintain the download template as required.Choose Save. |  |  |
| 24 | Upload the Template | Choose > of Profit Center to go into details.Choose Upload to upload your modified template.The upload results are displayed in the view. Select the rows and choose Check All and then Import All. | The master data is available in the system. |  |
| 25 | Access the SAP Fiori App to View Reporting | Return to the SAP Fiori launchpad and open Group Data Analysis (W0135).Note You may use the Search function to search for Group Data Analysis and select the title that shows Accessible. | The report is displayed with the hierarchy assigned. |  |
| 26 | Review Created Hierarchy | In the Navigation Panel, right-click the FS Item column and choose Hierarchy > Select Hierarchy . Choose created item hierarchy ZSEG_01 and choose OK. |  |  |
| 27 | Access the SAP Fiori APP to Define Selections | Open Define Selections (F3725) app. |  |  |
| 28 | Save | From the Selection table, select, for example, S-BC-TT-01.On the new column view that displays, choose Copy to copy to a new selection.Choose Save and Activate.Note You can choose different fields and criteria for creating different selections. |  |  |

#### Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section tests the configuration of consolidation validation engine apps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Balance Validation Rules and Rule Groups - Group Reporting (F8001). | The Manage Balance Validation Rules and Rule Groups view s displayed. |  |
| 3 | Review Existing Rules | Review the Rules list. | All rules are displayed. |  |
| 4 | Check Rule Details | Choose a rule to open. | A new view with rules details is displayed. |  |
| 5 | Change Rule Status | To switch the rule status, choose Set to Activate/Inactive status switch button. | Status is changed. |  |
| 6 | Create New Rule | Choose the < (Back) button to return to the previous view.Choose Create Rule to define a new validation rule. You can create Basic Rule or Compound Rule. | A New Rule session is displayed in a column with three tabs for maintaining rule information:General InformationRule ExpressionReference Links. |  |
| 7 | Input the Rule General Information | On the General Information tab, make an entry for the following. For the Rule ID field, only alphanumeric characters and underscores are allowed.Restriction SAP-delivered rules reserved the namespace beginning with S.For the Group By field, you may choose the validation characteristics from the dropdown list. This setting filter is used to sort validation results in later validation result run/display.For the Tolerance field, there are two kinds of calculation types: And, Or used to compare the validation result with tolerance amount and/or tolerance percentage.For the Control Level field, three kinds of control levels are listed in the dropdown:Error (the default value)WarningInformationIf the Comments required checkbox is selected, during the validation run, entering comments are required for the validation result. | General Information is maintained. |  |
| 8 | Input the Rule Expression | Choose the Rule Expression tab.On the Operand Expression Editor section, enter an Alias name and then define the alias:Operand: <Select from the dropdown list: Sum, Amount, Number, or Quantity.>Depending on your selection, different fields are displayed.Sum: Alias is mandatory.Amount: Amount value + Currency Key. If you leave the currency key filed empty, system considers it same as the source currency.Number: Value with +/- signQuantity: Value with +/- signYou can define f(x) type on the operand level or the formula level.Here is an example for different fx types if the result is -100.546:For f(x), the result should be 100.546For ABS, the result should be 100.546For Sign, the result should be -For Round 0, the result should be -100For Round 1, the result should be -100.5For Round 2, the result should be -100.55A list of Where conditions is available in the dropdown list.You can choose the selection operator from the dropdown list (like, equal to, between, in, not equal to…). If you choose Like, add a prefix 0 for the value you entered (check the exact value stored in the DB). | All rules are displayed. |  |
| 9 | Create Left Formula and Right Formula | After the alias is created, add to the formula panel.Create another Alias to add to the Right Formula field.Choose the correct compare criteria: >, <, >=, <=, = or <>.Choose Save to continue to modify without activating or choose Save and Activate to save and activate the rule. | The new rule is activated and added to the Rules list. |  |
| 10 | Create New Validation Groups | Return to the Manage Balance Validation Rules and Rule Groups view. Under the Groups list, choose Create to create a new validation group. |  |  |
| 11 | Maintain Validation Group Attributes | In the Create Group popup, enter the Group ID and Group Description.Choose Create.For the Group ID field, only alphanumeric characters and underscores are allowed.Restriction SAP-delivered rule reserves the namespace beginning with S. | A new validation group is created. |  |
| 12 | Assign Validation Rules to Validation Groups | To assign validation rules, you choose Edit and then + (Add).In the Add Node popup, you can choose Subnode to add subnode if needed and Validation Rule to assign the validation rules.Note In the rule selection list, only validation rules with Activate statue that are not assigned are listed.The selected rules are sorted by the selection sequence.You can choose X (Delete) button to remove assigned validation rules.After the rule is assigned, choose Save and Activate to activate the validation group. |  |  |
| 13 | Import/Export Validation Rules/Groups | Return to the SAP Fiori launchpad and open Import/Export Current Settings - Group Reporting (F3663).Choose Download for downloading all existing validation settings in the current system.Choose Upload and select the suitable template to upload validation settings into the system. |  |  |
| 14 | Access the SAP Fiori App | Return to the SAP Fiori launchpad and open Assign Rule Group for Balance Validation - Group Reporting (F8138) .Enter the Task and Version and choose Go.There are three kinds of task types predelivered by SAP:S1080 Reported Data ValidationS1180 Standardized Data ValidationS2980 Consolidated Data Validation | A Task Change view is displayed. |  |
| 15 | Create New Assignment | Choose Create.Enter the following entries and choose Continue:Task: for example, S1080Version: for example, A10Valid From: for example, 012.2025In the Assign Rule Group for Balance Validation view, enter the following entries and choose Create:Consolidation Unit Selection: <Leave blank or select your cons unit selectionPeriods: <select periods as needed>Validation Rule Group: <select rule group you created>Note In the Validation Rule Group field search help, only the groups with Active status are listed. |  |  |

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
> Flagged while digesting this document, not verified: P&L by Nature of Expense test uses Fiscal Year Period 012.2025 with Key Date 31.12.2024, whereas the Balance Sheet test for the same period uses Key Date 31/12/2025.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/test-script-sap-s-4hana-cloud-public-edition-group-reporting-financial-part-01]]
- see-also :: [[03-financial-accounting-and-close/journal-entry-template-40y-193]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1SG_S4CLD2608_BPD_EN_XX.docx` — lines 1723–2232 of the extracted text · extracted with `mammoth` · 329,699 chars in the whole document
