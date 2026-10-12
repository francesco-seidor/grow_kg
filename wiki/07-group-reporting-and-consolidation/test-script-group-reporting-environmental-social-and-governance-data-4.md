---
id: 07-group-reporting-and-consolidation/test-script-group-reporting-environmental-social-and-governance-data-4
title: "Test Script: Group Reporting – Environmental, Social, and Governance Data (4R7) (4R7_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4R7: ESG data collection forms and greenhouse gas consolidation in Group Reporting."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/esg-and-ghg-consolidation]
aliases: [4R7_S4CLD2608_BPD_EN_XX]
keywords: [ESG Data Collection and Greenhouse Gas Consolidation, esg data collection, greenhouse gas consolidation, group reporting, package parameters, ghg emission form, global parameters, business roles, test prerequisites, consolidation units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R7_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1046
topic: 07-group-reporting-and-consolidation/esg-and-ghg-consolidation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Group Reporting – Environmental, Social, and Governance Data (4R7) (4R7_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R7_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **ESG Data Collection and Greenhouse Gas Consolidation** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Group Reporting – Environmental, Social, and Governance Data (4R7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232838129)

[2 Prerequisites 3](#_Toc232838130)

[2.1 System Access 3](#_Toc232838131)

[2.2 Roles 3](#_Toc232838132)

[2.3 Business Conditions 4](#_Toc232838133)

[3 Overview Table 5](#_Toc232838134)

[4 Test Procedures 7](#_Toc232838135)

[4.1 Maintain ESG Forms 7](#_Toc232838136)

[4.1.1 Set Global Parameters and Open Period 7](#_Toc232838137)

[4.1.2 Enter Package Parameters 8](#_Toc232838138)

[4.1.3 GHG Emission Form 10](#_Toc232838139)

[4.1.4 Energy Consumption Form 10](#_Toc232838140)

[4.1.5 Water Consumption and Withdrawal 11](#_Toc232838141)

[4.1.6 Personnel, Diversity & Inclusion 12](#_Toc232838142)

[4.1.7 Personnel, Discrimination Cases 13](#_Toc232838143)

[4.1.8 Anti-Corruption Training 14](#_Toc232838144)

[4.1.9 R&D Projects Description 14](#_Toc232838145)

[4.2 Consolidation Scenario - Green House Gas Emission 15](#_Toc232838146)

[4.2.1 Preparation for Consolidation of Green House Gas Emission 15](#_Toc232838147)

[4.2.2 Full Consolidation 19](#_Toc232838148)

## Purpose

Overview

This scope item includes two separate functions:

- Increase efficiency in building your own Environmental, Social, Corporate governance (ESG) data collection forms by the sample forms as reference. In this test script, we demonstrate how to collect data using these sample forms.
- Enable group level green house gas consolidation to comply with upcoming reporting standards (ISSB, SEC, EFRAG) . There are different source data collection channels; in this test script, we’ll use offline upload data to simulate the real transactional carbon accounting data.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Table 1:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| Administrator - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Administration - Group Reporting | SAP_BR_ADMINISTRATOR_GRP | Ask your system administrator to assign to the testers.Generic User:Administrator - Group Reporting |
| Group Accountant | SAP_BR_ADMINISTRATOR_GRP | Group Reporting | SAP_BR_GRP_ACCOUNTANT | Ask your system administrator to assign to the testers.Generic User:Group Accountant |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Use the generic user below.Generic User: BPC_EXPERT |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| 1SG - Group Reporting – Financial Consolidation | Make sure that 1SG - Group Reporting – Financial Consolidation is activated before performing test procedures described in this test script for successful execution. |
| 287 - Group Reporting – Data from SAP Group Reporting Data Collection | The scope item should be activated and set up completed. |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Maintain ESG Forms

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Set Global Parameters and Open Period](#unique_7) [page ] 7 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD) | The period is open. |
| [Enter Package Parameters](#unique_8) [page ] 8 | Administrator - Group Reporting | Manage Packages (F4314) | Package Parameters are maintained. |
| [GHG Emission Form](#unique_9) [page ] 10 | Group Accountant | Enter Package Data | GHG Emission Form are ready. |
| [Energy Consumption Form](#unique_10) [page ] 10 | Group Accountant | Enter Package Data | Energy Consumption Form are ready. |
| [Water Consumption and Withdrawal](#unique_11) [page ] 11 | Group Accountant | Enter Package Data | Water Consumption and Withdrawal information is displayed. |
| [Personnel, Diversity & Inclusion](#unique_12) [page ] 12 | Group Accountant | Enter Package Data | Personnel, Diversity & Inclusion information is displayed. |
| [Personnel, Discrimination Cases](#unique_13) [page ] 13 | Group Accountant | Enter Package Data | Personnel, discrimination cases are displayed. |
| [Anti-Corruption Training](#unique_14) [page ] 14 | Group Accountant | Enter Package Data | Anti-Corruption Training information is displayed. |
| [R&D Projects Description](#unique_15) [page ] 14 | Group Accountant | Enter Package Data | R&D Projects Description is displayed. |

Table 3: Consolidation Scenario - Green House Gas Emission

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Preparation for Consolidation of Green House Gas Emission](#unique_16) [page ] 15 | Group Accountant | Set Global Parameters (CXGP)Data Monitor (CXCD)Define Consolidation Units (F4685)Define Consolidation Groups (F7959)Manage Group Structure - Group View (F3733) |  |
| [Full Consolidation](#unique_17) [page ] 19 | Administrator - Group Reporting | Manage Packages (F4314) |  |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Maintain ESG Forms

The inclusion of ESG metrics helps companies to manage long-term company performance and provide transparency to stakeholders on the connectivity between ESG and financial KPIs.

This chapter provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

#### Set Global Parameters and Open Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you set the global parameters and open the testing periods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Set Global Parameters (CXGP). | The Set Global Parameters screen displays. |  |
| 3 | Global Parameters | Enter the following values:Note This is for testing purpose, you can choose your own parameters.Organizational Units:Cons. Unit: <your own unit>Version/Time period:Version: Y10Fiscal Year: 2021Period: 12Further Settings:Cons. COA: Y1Choose Continue. | The global parameters are set. |  |
| 4 | Open Period | Open Data Monitor (CXCD).In the Hierarchy column, right click your consolidation unit and choose Open Period. | The period is open. |  |

#### Enter Package Parameters

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You'll choose your unit, period parameter to input the ESG information.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Administrator - Group Reporting. |  |  |
| 2 | Access App | Open Manage Packages (F4314).It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Set Parameter | You can remove all the filters in Package Definitions part. And then input your own entries in the filters.In the list packages, click Collect ESG Data.And in the detailed page, choose Edit.Note If you cannot find the data package, you can click Create button to create a new one. |  |  |
| 4 | Maintain General Information | In the General Information tab, check the parameters you want to use to input the data. Or if you're creating one, please maintain the followings for example:Consolidation Version: Y10Start Fiscal Year : 2021End Fiscal Period: 12Period = 1 (The period status should be open, otherwise you should go to previous step to open the period)Consolidation Chart of Accounts = Y1Consolidation Unit = 1010Description = Maintain ESG InformationRemember Please remember the parameters, they'll be used in following section. |  |  |
| 5 | Maintain Data Entry Steps | In the tab Data Entry Steps, enter Maintain ESG Information as step description.Set the following sections as:Data Release: 1015Forms: 1020Validations: 1050Validations: S1080Choose ESG Data as Folders.Set the Document Types as:Read document type = 04Write document type = 03And then choose Save. |  |  |

#### GHG Emission Form

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account.Set the parameter value which is set in step [Enter Package Parameters](#unique_8) [page ] 8. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7100 - GHG Emissions, in tCO2e.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit's CO2 emission and choose Save to save your input. |  |  |

#### Energy Consumption Form

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7200 - Energy Consumption, in KWh.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and choose Save. |  |  |

#### Water Consumption and Withdrawal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7300 - Water Consumption and Withdrawal, in ML.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and choose Save. |  |  |

#### Personnel, Diversity & Inclusion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7400 - Personnel, Diversity & Inclusion.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and then choose Save. |  |  |

#### Personnel, Discrimination Cases

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Data Package.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7500 - Personnel, Discrimination Cases.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and then choose Save. |  |  |

#### Anti-Corruption Training

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7600 - Anti-Corruption Training.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and then choose Save. |  |  |

#### R&D Projects Description

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Input the relevant information for your ESG forms.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. |  |  |
| 2 | Access App | Open Enter Package Data.It'll link you to SAP BTP page. Please input your BTP account. |  |  |
| 3 | Access Data Package | In the list packages, select the package that you just created and choose >. |  |  |
| 4 | Access Form | In the Forms list, choose SI7700 - R&D Projects Description.And then choose Go on the right of the view to display the format. | The form appears. |  |
| 5 | Input Data | Input the amount for the unit and choose Save. |  |  |

### Consolidation Scenario - Green House Gas Emission

Gathering and accounting for Green House Gas emissions on consolidated group level will be managed with SAP S/4HANA for Group Reporting. With it, intercompany transactions along a value chain crossing different subsidiaries can transparently be handled applying standards and techniques for intercompany financial accounting.

#### Preparation for Consolidation of Green House Gas Emission

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) and choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Corporate Close | The Configure Your Solution view is displayed. |  |
| 3 | Set Global Parameters | In the results section, choose Item Name Basic Settings.Select Set Global Parameters and choose Configure on that row.Set the following parameters:Version: Y10Fiscal year: 2021Period: 12Cons. COA: Y1Choose Save.Note Fulfill the entries as above if global parameters have not been set yet; otherwise, skip this step. | The Global parameters log displays. |  |
| 4 | Enable GHG Additional Fields | Go back to the original view.Select Activate Fields for Greenhouse Gas and choose Configure.Check if the Switch State is ON, if not, choose button Change State. | Additional fields for Greenhouse Gas are activated. |  |
| 5 | Create Version G10 | Go back to the original view.Select Create Version from Reference Version and choose Configure. Enter the following entries:Template Version: Y10Target Version: G10Test Run: <Deselect>Version Type: StandardRef. Version: <leave blank>Group Currency: EURRun Mode: Manual RunAllow LC, TC, Qty Changes: <Deselect>FY variant: K4Choose Execute and then Continue.Ignore the information message Documents aren´t auto-reversed in periods greater than 12. and choose Exit.Note G10 is used for the test process in this document. You can use your own version in your real business process. | Target version G10 is created successfully with template version Y20. |  |
| 6 | Check Breakdown Category Configuration | Go back to the original view.Chose Item Name Master Data.Select Step Define Breakdown Categories and choose Configure.Select breakdown category 1L10.Double-click Breakdown by subassignment in the left Dialog Structure.For char Unit of measure, maintain or review the following entry:Break.Type: 1Choose Save.Perform the same step for breakdown category 2A10 and 2B10. | Breakdown Categories configuration is maintained. |  |
| 7 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Group Reporting. | The SAP Fiori launchpad displays. |  |
| 8 | Set Global Parameters | Make the following entries and choose Continue:Organizational units area:Cons. Group: <leave blank>Cons. Unit: <leave blank>Version/Time period area:Version: G10Fiscal year: 2021Period: 12Further settings area:Cons. COA: Y1 | The global parameters are set. |  |
| 9 | Access the SAP Fiori App | Open app Define Consolidation Units (F4685). | The SAP Fiori launchpad displays. |  |
| 10 | Create Units for GHG Emission | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Choose Create. In the Create Consolidation Unit dialog box, enter a Consolidation Unit, for example GHGx0. Press Enter and then choose Create.In the tab General Information, input Consolidation Unit Description: <for example, Palo Alto>.In the tab Time-Dependent Attributes, input Local currency: for example USD.In the tab Time- and Version-Dependent Attributes, input Upload Method: SRD2.Choose Save.Perform the same steps to create units GHGx1, GHGx11 and GHGx2. | Units for GHG Emission are created. |  |
| 11 | Create Consolidation Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Define Consolidation Groups (F7959).In the tile, input one name (for example, CGHGx) for Consolidation group and press Enter.In the Basic Data tab, input following entries:Consolidation Group Description: <short description of the consolidation group>Consolidation Group Medium Description: <long description of the consolidation group>Choose Save. | The consolidation group is created.. |  |
| 12 | Assign Units to Group | Note This step creates demo data. If you want project-specific settings, then adapt to your requirements.Open Manage Group Structure - Group View (F3733).Enter the following entries and choose Go.Consolidation Group: for example, CGHGxConsolidation Version: G10Fiscal Year and Period: 012.2021Choose Assign and assign the unit you created for accounting integration (for example GHGx0, GHGx1, GHGx11 and GHGx2).Input following entries:First Consolidation: 012.2021Divestiture: 999.9999Consolidation Method:GHGx0: 00GHGx1: 10GHGx11: 10GHGx2: 20Choose Assign. | Units are assigned to your consolidation group. |  |

#### Full Consolidation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this release, the full consolidation of CO2e is not covered. The function is ready and customer can create own elimination reclassification methods.

In the test script, we demonstrate how to correctly upload the carbon emission data and check the emission report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Group Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open app Set Global Parameters (CXGP). | The Global parameters dialog box displays. |  |
| 3 | Set Global Parameters | Make the following entries and choose Continue:Cons. Group: CGHGxCons. Unit: <leave empty>Consolidation Version: G10Fiscal Year and Period: <The period and year you are testing, for example, 012.2021>Cons. COA: Y1 | The global parameters are set. |  |
| 4 | Access the SAP Fiori App | Open Data Monitor (CXCD). | The Data Monitor view displays. |  |
| 5 | Open Period | Select your consolidation group and choose More > Edit > Open Period . | The system displays the Period 012/2021 for CGHGx / GHGxx opened. |  |
| 6 | Data Monitor - Data Collection | In the Data Monitor view, right click the Data Coll. - Milestone:Data Collection task and choose Update or choose Update Run on the toolbar.Download and edit the [Sample File](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/GHG_UPLOAD_2021_12_SRD2_DT_00.xlsx).Remember Replace GHGx in the columns ConsolidationUnit, PartnerConsolidationUnit and in the file with your real group and unit ID.Choose Flexible upload to upload the edited file. In the Flexible Upload of : Reported financial data view, enter the following entries:Consolidation group: CGHGxConsolidation unit: from GHGx0 toUpload method: SRD2Physical file name: Your download fileChoose Execute.Choose Exit. |  |  |
| 7 | Access Reporting | Open Group Data Analysis (W0135).Choose Adapt Filters.Make the following entries and choose Go:Version: G10Consolidation COA: Y1Fiscal Year Period: 012/2021Consolidation Group: CGHGxPeriod Mode: YTDKey Date: 31.12.2021Consolidation Unit Hierarchy: $Profit Center Hierarchy: $Segment Hierarchy: $ |  |  |
| 8 | Check Report | In the Navigation Panel, in columns Measures, choose > to expand. Then add Quantity and remove Amount in Group Crcy.In the Navigation Panel, select the field Greenhouse Gas Scope and choose Add field to rows axis.In the Navigation Panel, select the field Document Type and choose Remove field Document Type from rows axis.If the report is not refreshed, press button Go. |  |  |

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
> Flagged while digesting this document, not verified: Create Version G10 step uses template version Y10 but its expected result says the target version is created with template version Y20.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/ghg-upload-2021-12-srd2-dt-00-191]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4R7_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 30,552 chars in the whole document
