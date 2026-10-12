---
id: 13-quality-ehs-and-compliance/test-script-sap-fiori-analytical-apps-for-quality-management-2v0-875
title: "Test Script: SAP Fiori Analytical Apps for Quality Management (2V0) (2V0_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP S/4HANA Cloud scope item 2V0: Quality Engineer/Technician overview pages and Fiori quality analytics apps, with roles and prerequisites."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/quality-management-analytics]
aliases: [2V0_S4CLD2608_BPD_EN_XX]
keywords: [Quality Management Analytics, scope item test script, quality engineer overview, quality technician overview, inspection lot analytics, skip rate analysis, inspection lot detailed analytics, characteristic analytics, nonconformance analytics, defect management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V0_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-875
topic: 13-quality-ehs-and-compliance/quality-management-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Fiori Analytical Apps for Quality Management (2V0) (2V0_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V0_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management Analytics** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Quality Management (2V0) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232840871)

[2 Prerequisites 4](#_Toc232840872)

[2.1 System Access 4](#_Toc232840873)

[2.2 Roles 4](#_Toc232840874)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232840875)

[2.4 Business Conditions 5](#_Toc232840876)

[3 Overview Table 6](#_Toc232840877)

[4 Test Procedures 8](#_Toc232840878)

[4.1 Quality Engineer Overview 8](#_Toc232840879)

[4.2 Quality Technician Overview 11](#_Toc232840880)

[4.3 Analyze Accepted and Rejected Lots 13](#_Toc232840881)

[4.4 Analyze Skipped and Non Skipped Lots 16](#_Toc232840882)

[4.5 Analyze Inspection Lots Leveraging Inspection Lot Detailed Analytics 18](#_Toc232840883)

[4.6 Analyze Inspection Characteristics 20](#_Toc232840884)

[4.7 Analyze Inspection Characteristics Leveraging Inspection Characteristic Detailed Analytics 21](#_Toc232840885)

[4.8 Analyze Nonconformance 23](#_Toc232840886)

[4.9 Analyze Nonconformance Leveraging Nonconformance Detailed Analytics 24](#_Toc232840887)

[4.10 Manage Defects 25](#_Toc232840888)

[4.11 Display Results History 27](#_Toc232840889)

[4.12 Quality Level History - Skip Rate in Last 180 Days 29](#_Toc232840890)

[4.13 Manage Control Charts 31](#_Toc232840891)

[4.14 Manage Quality Tasks 33](#_Toc232840892)

## Purpose

Overview

This scope item provides overview pages for the quality technician and the quality engineer. The quality engineer overview page displays important information and tasks related to quality inspection management with a focus on usage decisions (for example, inspection lots without usages decisions, or lots that are ready for usage decision), defects (for example, top defective materials, inspection lots with defects), action limits, quality levels, and quality tasks. The quality technician overview page focuses on processing of the inspection lot, executing the quality inspection, and processing of quality tasks. Further apps for the detailed analysis of the past and current quality situation are provided: You can analyze accepted and rejected inspection lots or inspection characteristics with respect to different KPIs and drill down by accounting for additional parameters. Defects and results history can be analyzed to deduce measures to improve the current quality situation.

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
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or sample data in Preliminary Steps to go through the test procedure.

### Business Conditions

The scope items listed below describe how to create business data. Carry out the required steps in order to obtain data that can be analyzed leveraging the apps described in this document.

| Scope Item ID | Business Condition |
| --- | --- |
| 1E1 - Quality Management in Discrete and Process Manufacturing | Must be run before this test script. |
| 1FM - Quality Management in Procurement | Must be run before this test script. |
| 1MR - Quality Management in Stock Handling | Must be run before this test script. |
| 1MP - Quality Management in Sales | Must be run before this test script. |
| 2QN - Nonconformance Management | Must be run before this test script. |

## Overview Table

This scope item SAP Fiori Analytical Apps for Quality Management consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Quality Engineer Overview](#unique_8) [page ] 8 | Quality Engineer | Quality Engineer Overview (F2360) | Overview page is displayed correctly. |
| [Quality Technician Overview](#unique_9) [page ] 11 | Quality Technician | Quality Technician Overview (F2361) | Overview page is displayed correctly. |
| [Analyze Accepted and Rejected Lots](#unique_10) [page ] 13 | Quality Engineer | Inspection Lot Analytics - UDs Made in Last 365 Days (F3239) | The SAP Fiori app is running correctly. |
| [Analyze Skipped and Non Skipped Lots](#unique_11) [page ] 16 | Quality Engineer | Inspection Lot Analytics - UDs Made in Last 365 Days (F3239) | The SAP Fiori app is running correctly. |
| [Analyze Inspection Lots Leveraging Inspection Lot Detailed Analytics](#unique_12) [page ] 18 | Quality Engineer | Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273) | The SAP Fiori app is running correctly. |
| [Analyze Inspection Characteristics](#unique_13) [page ] 20 | Quality Engineer | Characteristic Analytics - Results in Last 365 Days (F3383) | The SAP Fiori app is running correctly. |
| [Analyze Inspection Characteristics Leveraging Inspection Characteristic Detailed Analytics](#unique_14) [page ] 21 | Quality Engineer | Characteristic Detailed Analytics - Results Recorded in Last 365 Days (F3382) | The SAP Fiori app is running correctly. |
| [Analyze Nonconformance](#unique_15) [page ] 23 | Quality Engineer | Nonconformance Analytics - Defects Created in Last 365 Days (F3584) | The SAP Fiori app is running correctly. |
| [Analyze Nonconformance Leveraging Nonconformance Detailed Analytics](#unique_16) [page ] 24 | Quality Engineer | Nonconformance Detailed Analytics - Defects Created in Last 365 Days (F3583) | The SAP Fiori app is running correctly. |
| [Manage Defects](#unique_17) [page ] 25 | Quality Engineer | Manage Defects (F2649) | The SAP Fiori app is running correctly. |
| [Display Results History](#unique_18) [page ] 27 | Quality Engineer | Display Results History (F2428) | The SAP Fiori app is running correctly. |
| [Quality Level History - Skip Rate in Last 180 Days](#unique_19) [page ] 29 | Quality Engineer | Quality Level History - Skip Rate in Last 180 Days (F2915) | The SAP Fiori app is running correctly. |
| [Manage Control Charts](#unique_20) [page ] 31 | Quality Engineer | Manage Control Charts (F2810) | The SAP Fiori app is running correctly. |
| [Manage Quality Tasks](#unique_21) [page ] 33 | Quality Engineer | Manage Quality Tasks (F3381) | The SAP Fiori app is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Quality Engineer Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Quality Engineer Overview shows in a single page the most important information and tasks related to inspection management that are relevant for you right now. The information is displayed on set of cards.

Procedure

Quality Engineer Overview Page - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Quality Engineer Overview (F2360). | Check that the app starts correctly and that (at least) the following cards are displayed (exact names might vary):Action Limit ViolationsQuality Info Records with ExceptionsQuality Levels for CharacteristicsInspection Lots Without Usage DecisionInspection Lots Ready for Usage DecisionTop Defective MaterialsTop Defective CodesQuality Levels for Inspection LotsInspection Severity of Next Inspection StageInspection Lots with DefectsInspection Lots Without Inspection PlanOpen Quality Tasks by Planned EndOpen Quality Tasks by Processor Assignment |  |
| 3 | Filter Cards | At the top of the Quality Engineer Overview page, you could filter cards based on different values of Plant and Inspection Lot Origin.Additional fields can be added via Adapt Filters and selecting More Filters in the dialog box. | Check if the content of the corresponding cards is filtered accordingly. |  |
| 4 | Pass On Filter Criteria to Corresponding App | If you have an active filter criteria (for example, filtered via a specific supplier), click on different card headers. | Check if the filter values from the Quality Engineer Overview page have been applied in the corresponding App / KPI drilldown as well. |  |
| 5 | Hide Cards | Choose the User Icon at the top right of the page.Choose Manage Cards.Disable various cards via the toggle buttons in the dialog box and choose OK.In the same way, you can add the cards to the Overview Page again (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards on the Quality Engineer Overview Page. | Check if the cards can be rearranged, hidden, and shown again. |  |

Quality Engineer Overview Page - Card Specific Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Investigate Cards | After launching the Quality Engineer Overview page, investigate the following cards:Quality Info Records with ExceptionsQuality Levels for CharacteristicsInspection Lots Without Usage DecisionInspection Lots Ready for Usage DecisionTop Defective MaterialsTop Defective CodesQuality Levels for Inspection LotsInspection Severity of Next Inspection StageAction Limit ViolationsInspection Lots with DefectsInspection Lots Without Inspection PlanOpen Quality Tasks by Planned EndOpen Quality Tasks by Processor Assignment | The data is shown as expected. |  |
| 2 | Header Navigation to Apps | Click on the headers of these cards. | Inspection Lots Without Inspection Plan: Selecting the header takes you to the Manage Inspection Lots (F2343) app.Inspection Lots Without Usage Decision: Selecting the header takes you to the Manage Usage Decisions (F2345) app.Inspection Lots Ready for Usage Decision: Selecting the left area takes you to the Manage Usage Decisions (F2345) app.Inspection Lots with Defects: Selecting the header takes you to the Manage Defects (F2649) app.Top Defective Materials: Selecting the header takes you to the Manage Defects (F2649) app.Top Defective Codes: Selecting the header takes you to the Manage Defects (F2649) app.Inspection Severity of Next Inspection Stage: Selecting the header takes you to the Manage Quality Levels (F2914) app.Quality Level for Inspection Lots: Selecting the header takes you to the Manage Quality Levels (F2914) app.Quality Level for Characteristics: Selecting the header takes you to the Manage Quality Levels (F2914) app.Open Quality Tasks by Planned End / Processor Assignment: Selecting the header takes you to the Manage Quality Tasks (F3381) app. |  |
| 3 | Item Navigation to Apps | Click on items of these cards. | Inspection Lots Without Inspection Plan: Selecting an item takes you to the Manage Inspection Lot screen.Inspection Lots Without Usage Decision: Selecting a section of the donut chart also takes you to the Manage Usage Decisions (F2345) app, but the inspection lots are now filtered based on the results recording status of the selected section.Inspection Lots Ready for Usage Decision: Selecting the right area opens a collection of scrollable cards, with each card representing an inspection lot that is ready for usage decision, along with the option to make a usage decision for that inspection lot.Inspection Lots with Defects: Selecting a section of the donut chart also takes to the Manage Defects (F2649) app, but the defects are now filtered based on the inspection lot origin of the selected section.Top Defective Materials: Selecting a column also takes you to the Manage Defects (F2649) app, but the defects are now filtered based on the material.Top Defective Codes: Selecting a column also takes you to the Manage Defects (F2649) app, but the defects are now filtered based on the defect code and the defect code group.Inspection Severity of Next Inspection Stage: Selecting a column also takes you to the Manage Quality Levels (F2914) app, but the quality levels for inspection lots and characteristics are now filtered based on inspection severity.Quality Level for Inspection Lots: Selecting a section of the donut chart also takes to the Manage Quality Levels (F2914) app, but the quality levels for inspection lots are now filtered based on skip status.Quality Level for Characteristics: Selecting a section of the donut chart also takes to the Manage Quality Levels (F2914) app, but the quality levels for characteristics are now filtered based on skip status.Open Quality Tasks by Planned End / Processor Assignment: Selecting the bar or a section of the donut chart takes you to the Manage Quality Tasks (F3381) app, but the quality tasks are now filtered based on the date or processor assignment status. |  |

### Quality Technician Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Quality Technician Overview shows in a single page the most important information and tasks related to inspection management that are relevant for you right now. The information is displayed on set of cards.

Procedure

Quality Technician Overview Page - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Quality Technician Overview (F2361) app. | Check that the app starts correctly and that (at least) the following cards are displayed (exact names might vary):Inspection Lots with Open Results Recording, No Inspection PointsInspection Lots Without Inspection PlanMy TasksInspection Lots with Open Results for Inspection Points |  |
| 3 | Filter Cards | At the top of the Quality Technician Overview (F2361)page, you could filter cards based on different values of Plant and Inspection Lot Origin.Additional fields can be added via Adapt Filters and selecting More Filters in the dialog box. | Check if the content of the corresponding cards is filtered accordingly. |  |
| 4 | Pass On Filter Criteria to Corresponding App | If you have an active filter criteria (for example, filtered via a specific supplier), click on different card headers. | Check if the filter values from the Quality Technician Overview (F2361) page have been applied in the corresponding App / KPI drilldown as well. |  |
| 5 | Hide Cards | Choose the user icon at the top right of the page.Choose Manage Cards.Disable various cards by deselecting the items in the dialog box and choose OK.In the same way, you can add the cards to the Quality Technician Overview page again (or simply choose Reset in the Manage Cards dialog box).In addition, you can drag and drop the cards on the Quality Technician Overview page. | Check if the cards can be rearranged, hidden, and shown again. |  |

Quality Technician Overview Page - Card Specific Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Investigate Cards | After launching the Quality Technician Overview (F2361)page, investigate the following cards:Inspection Lots with Open Results Recording, No Inspection PointsInspection Lots Without Inspection PlanMy TasksInspection Lots with Open Results for Inspection Points |  |  |
| 2 | Header Navigation to Apps | Click on the headers of these cards. | Inspection Lots Without Inspection Plan: Selecting the header takes you to the Manage Inspection Lots (F2343) app.Inspection Lots with Open Results Recording, No Inspection Points: Selecting the header takes you to the Record Inspection Results app.My Tasks: Selecting the header takes you to the Process Quality Tasks (F3250) app where processor equals the current user.Inspection Lots with Open Results for Inspection Points: Selecting the header takes you to the Record Results for Inpsection Points app. |  |
| 3 | Item Navigation to Apps | Click on items of these cards. | Inspection Lots Without Inspection Plan Selecting an item takes you to the Change Inspection Lot screen.Inspection Lots with Open Results Recording, No Inspection Points: Selecting a column also takes you to the Record Inspection Results app, but the inspection lots are now filtered based on the end date of inspection.My Tasks: Selecting the item takes to the object page of the corresponding task.Inspection Lots with Open Results for Inspection Points: Selecting a column also takes you to the Record Results for Inpsection Points app but the results are now filtered based on the end date of inspection. |  |

### Analyze Accepted and Rejected Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to analyze inspection lots by Time, Materials, Suppliers, Inspection Types, Customers, etc. The information system allows you to display accepted and rejected inspection lots with respect to time, inspection type, or material and plant. You can drill down a hierarchy to carry out specific analysis or compare suppliers, materials, etc. A vast number of chart types enables you to visualize data according to your requirements.

Procedure

Inspection Lot Analytics - Key Figures - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Inspection Lot Analytics - UDs Made in Last 365 Days (F3239) app. | The Inspection Lot Analytics screen displays. |  |
| 3 | Filter the Inspection Lots | In the Key Figures section, you can filter by UD Made on - Date Function.Additional fields can be added via Adapt Filters and selecting More Filters in the dialog box.You can also add fillters by choosing Add Filter in the top left. | Check if the content of the corresponding cards is filtered accordingly. |  |
| 4 | Change Displayed Data | From the drop down in the upper left of the chart, select the data that should be displayed, for example:Accepted and Rejected Lots by Time SeriesAccepted and Rejected Lots by Inspection TypeAccepted and Rejected Lots by Material and PlantLots Skipped and Not Skipped by Time SeriesLots Skipped and Not Skipped by Inspection TypeLots Skipped and Not Skipped by Material and Plant | Respective data is displayed in a column chart (default setting)Accepted and Rejected Lots: The number of accepted and rejected lots is shown in a stacked column chart (left y-axis). The rejection rate is displayed in a bar chart (right y-axis)Lots Skipped and Not Skipped: The number of skipped and non-skipped lots is shown in a stacked column chart (left y-axis). The skip rate is displayed in a bar chart (right y-axis) |  |
| 5 | Switch to Table View | Choose Tabular View on the upper right of the chart. | The graphical view is replaced with a table view. |  |
| 6 | Switch Back to Graphical View | Choose Chart View on the upper right of the table. | The table view changes back to a graphical view. |  |
| 7 | Change Display Settings | Choose Settings on the upper right of the chart.Select a different chart type, activate a data item by selecting the box and select an appropriate role of the data item. | The graphical view is adapted according to your chosen settings. |  |
| 8 | Reset to Default View | Open Settings, choose button Reset and button OK. | Data is displayed as defined in the default settings. |  |
| 9 | Remove the Filter | Choose the Reset Filter on the top right of the page, choose OK in the Reset Filters screen. | The data displayed in the graph is changed accordingly. |  |
| 10 | Drill Down | Choose View By on the upper right of the chart and choose a drill down dimension (e.g. material or inspection type). | Values on x-axis are split up according to the selected drill-down dimension. |  |
| 11 | Drill Up | Choose Drill Up on the upper right of the chart to drill up one dimension | Drill-down dimension is removed from the x-axis. |  |
| 12 | Check Jump To… Function | Choose Jump To… in the top right corner of the table. | The following options for navigation with Jump To… are displayed:Inspection Lot Detailed Analytics - The app Inspection Lot Detailed Analytics (F3273) is opened with applied filter parameter.Manage Inspection Lots - The app Manage Inspection Lots (F2343) is opened with applied filter parameter. |  |

Inspection Lot Analytics - Key Figures - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open the Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273) app. | The Inspection Lot Detailed Analytics screen displays. |  |
| 3 | Display Number of Accepted and Rejected Lots by Usage Decision Made On | In the bottom left corner of the Inspection Lot Detailed Analytics screen, choose the + button.On the Category screen, select Accepted and Rejected Lots by Usage Decision Made On.Choose Line Chart with Time Axis. | The number of accepted and rejected lots is displayed in the chart. |  |
| 4 | Display Number of Accepted and Rejected Lots in Detailed Time Series | In the bottom left corner of the Inspection Lot Detailed Analytics screen, choose the + button.On the Category screen, select Accepted and Rejected Lots by Calendar Year, Accepted and Rejected Lots by Calendar Year and Quarter, Accepted and Rejected Lots by Calendar Year and Month, Accepted and Rejected Lots by Calendar Year and Week .You can open the result by either Column Chart, Stacked Column Chart or Line Chart with Two Vertical Axes.You can also switch chart type by choosing the column icon near top right of the chart. | The number of accepted inspection lots per inspection type is displayed in the chart. |  |
| 5 | Display Number of Accepted lots Per Inspection Type | In the bottom left corner of the Inspection Lot Detailed Analytics screen, choose the + button.On the Category screen, select Accepted and Rejected Lots by Inspection Type.You can open the result by either Column Chart, Stacked Column Chart or Line Chart with Two Vertical Axes.You can also switch chart type by choosing the column icon near top right of the chart. | The number of accepted inspection lots per inspection type is displayed in the chart. |  |
| 6 | Display Number of Accepted lots by Material | In the bottom left corner of the Inspection Lot Detailed Analytics screen, choose the + button.On the Category screen, select Accepted and Rejected Lots by Material.You can open the result by either Column Chart, Stacked Column Chart or Line Chart with Two Vertical Axes.You can also switch chart type by choosing the column icon near top right of the chart. | The number of accepted inspection lots per inspection type is displayed in the chart. |  |

### Analyze Skipped and Non Skipped Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to analyze inspection lots by time, materials, suppliers, inspection types, customers, etc. The information system allows you to display skipped and non skipped lots with respect to time, inspection type, or material and plant. You can drill down a hierarchy to carry out specific analysis or compare suppliers, materials, etc. A vast number of chart types enables you to visualize data according to your requirements.

Procedure

Inspection Lot Analytics - Key Figures - General Test

See previous chapter.

Inspection Lot Analytics - Key Figures - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

From the Inspection Lot Analytics - UDs Made in Last 365 Days (F3239) app, you can choose Jump To ... and select Inspection Lot Detailed Analytics to open the detailed anlytics app.

You can also open the Inspection Lot Detailed Analytics (F3273) app directly from the SAP Fiori Launchpad.

Choose Add Analysis Step and select Lots Skipped and Not Skipped.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Skipped and Non Skipped Lots by Usage Decision Made On | From the drop down in the upper left of the chart, select Lots Skipped and Not Skipped by Usage Decision Made On.Choose Line Chart with Time Axis. | The number of skipped and not skipped inspection lots is displayed in the chart. |  |
| 2 | Skipped and Non-Skipped Lots by Detailed Time Series | From the drop down in the upper left of the chart, select Lots Skipped and Not Skipped by Calendar Year, Lots Skipped and Not Skipped by Calendar Year and Quarter, Lots Skipped and Not Skipped by Calendar Year and Month, Lots Skipped and Not Skipped by Calendar Year and Week .You can open the result by either Column Chart, Stacked Column Chart or Line Chart with Two Vertical Axes.You can also switch chart type by choosing the column icon near top right of the chart. | The number of skipped and not skipped inspection lots is displayed in the chart. |  |
| 3 | Skipped and Non-Skipped Lots Per Material and Plant | From the drop down in the upper left of the chart, select Lots Skipped and Not Skipped by Material.From the drop down in the upper left of the chart, select Lots Skipped and Not Skipped by Plant.You can open the result by either Column Chart, Stacked Column Chart or Line Chart with Two Vertical Axes.You can also switch chart type by choosing the column icon near top right of the chart. | The number of skipped and not skipped inspection lots is displayed in the chart. |  |

### Analyze Inspection Lots Leveraging Inspection Lot Detailed Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality engineer can interactively explore inspection lot data step by step from different perspectives to analyze the current quality situation. In each analysis step, he can investigate KPIs and select relevant data to filter the information displayed in subsequent steps. By combining different analysis steps and filters, he interactively creates his own flexible analysis path, e.g. for root cause analysis.

Procedure

Inspection Lot Detailed Analytics - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Logon to the SAP Fiori Launchpad as the Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273). | The Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273)screen displayed. |  |
| 3 | Add Analysis Step | The analysis path can be specified in the left vertical section. Choose Add Analysis Step and choose a category in the dialogue box. | A new graph is displayed that visualizes the chosen data. |  |
| 4 | Fllter the Result | At the header, you may filter the result by UD Made on - Date Function.Additional fields can be added via Filters and entering a filter in the dialog box (e.g. plant, inspection type, material, etc.). | Check if the content of the chart is filtered according to the chosen filters. |  |
| 5 | Add A Second Analysis Step | To add an additional analysis step, repeat the previous test step. | An additional graph is displayed in the left vertical section. |  |
| 6 | Select Data | Open the first analysis step and select one or more data points. Note that the data in the 2nd analysis step only displays data points that are included in the selected data of the 1st analysis step.If you want to investigate the underlying raw data (for example, inspection lots), select one or more data points and choose Jump To... > Manage Inspection Lots in the lower right corner. The Manage Inspection Lots app is opened and the selected parameters are transferred to this app. | Based on the selection of data in the 1st analysis step, the displayed data in the 2nd analysis step is changed. |  |
| 7 | Add Further Analysis Steps (Optional) | Repeat step 5 to add additional analysis steps. |  |  |
| 8 | Switch to List View | Choose button List View in the upper right of the graph to switch to a tabular view. | Data is displayed in a tabular view. |  |
| 9 | Save Analysis Path | Choose Save As from the Related Options drop down above the left vertical section. Enter a description and choose OK to save the analytical path. | Analytical path is saved for later use. |  |
| 10 | Open Existing Analysis Path | Choose Open from the Related Options drop down above the left vertical section and select one Analysis Path in the pop-up. | Analytical path is displayed. |  |

Inspection Lot Detailed Analytics - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Analyze the Number of Accepted and Rejected Inspection Lots Per Year and Week for Different Materials | First step:Accepted and Rejected Lots > Accepted and Rejected Lots by MaterialSecond step:Accepted and Rejected Lots > Accepted and Rejected Lots by Calendar Year and WeekSelect one or more materials in the first step. Open 2nd analysis step and review the number of accepted and rejected lots as a function of time for the selected material(s). | The analysis path contains two analysis steps. Data of the 2nd step is influenced by the data points selected in the 1st step. |  |
| 2 | Identify Materials with Highest Rejection Rate As A Function of Time | First step:Rejection Rate > Top 10 Materials with Highest Rejection RateSecond step:Accepted and Rejected Lots > Accepted and Rejected Lots by Calendar Year and WeekSelect the data point that corresponds to the material with the highest rejection rate in the first analysis step. Switch to the second analysis step and check e.g. whether there is a trend or whether the high number of rejected lots has occurred in a certain week. | The 2nd analysis step displays the inspection lots per year and week for the material selected in the 1st analysis step. |  |

### Analyze Inspection Characteristics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to analyze quality inspections with respect to time, (master) inspection characteristics, material and plant, and work center. The information system allows you to display accepted and rejected inspections, skipped and not skipped inspections, and inspected and non-conformance units. You can drill down a hierarchy to carry out specific analysis or compare plants, materials, inspection characteristics, etc. A vast number of chart types enables you to visualize data according to your requirements.

Procedure

Characteristic Analytics - General Test

This app is based on the same template as the app Inspection Lot Analytics - UDs Made in Last 365 Days (F3239). See section [Analyze Accepted and Rejected Lots](#unique_10) [page ] 13 for a description of the technical features.

Characteristic Analytics - Example Analytics

The following table describes examples for analysis of inspection characteristics. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the app | Open the Characteristic Analytics - Results in Last 365 Days (F3383) app. | The Characteristic Analytics screen displays. |  |
| 3 | Show Tolerance Violations for Quantitative Characteristics for Plant / Material / Master Inspection Characteristic | Choose Show Mini Tiles and choose the Characteristics Analytics - Quantitative Characteristics Comparison Micro Chart.From the drop down in the upper left, select Value Under and Value Over Tolerance by Material and Plant.Drill down by choosing View By > Master Inspection Characteristics . | A stocked column chart with 2 Y-axes is displayed. The left y-axis displays the absolute number of inspections. The right y-axis displays the amount of tolerance violations, split into upper and lower violations.The x-axis displays the different master inspection characteristics per plant and material. |  |
| 4 | Display Accepted and Rejected Inspections for Different Suppliers | Open Show Mini Tiles again and choose Characteristic Analytics - Key Figures.From the drop down in the upper left, select Accepted and Rejected Inspections by Material and Plant.Drill down by choosing View By > Supplier . | A stocked column chart with 2 Y-axes is displayed. The left y-axis displays the absolute number of accepted and rejected inspections. The right y-axis displays the rejection rate of the quality inspections.The x-axis displays the different suppliers per plant and material. |  |

### Analyze Inspection Characteristics Leveraging Inspection Characteristic Detailed Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to interactively explore inspection characteristics step by step from different perspectives to analyze the current quality situation. In each analysis step, you can investigate KPIs and select relevant data to filter the information displayed in subsequent steps. By combining different analysis steps and filters, you interactively create your own flexible analysis path, e.g. for root cause analysis.

Procedure

Characteristic Detailed Analytics - General Test

This app is based on the same template as the app Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273). See chapter Analyze Inspection Lots Leveraging Inspection Lot Detailed Analytics.

Characteristic Detailed Analytics - Example Analytics

The following table describes examples for analysis of inspection characteristics. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

Open the app Characteristic Detailed Analytics - Results Recorded in Last 365 Days (F3382) and choose Add Analysis Step.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Analyze the Rejection Rate of Different Materials Per Supplier | First step:Rejection Rate > Rejection Rate by MaterialSecond step:Rejection Rate > Rejection Rate by SupplierSelect one or more materials in the first step. Open 2nd analysis step and review the rejection rate for the different materials per supplier in the selected time frame. | The analysis path contains two analysis steps. Data of the 2nd step is influenced by the data points selected in the 1st step. |  |
| 2. | Analyze the Total Number of Inspections for Materials per Plant | First step:Total No. of Inspections > Total No. of Inspections by PlantSecond step:Total No. of Inspections > Total No. of Inspections by MaterialSelect one or more plants in the first step. Open 2nd analysis step and review the total number of inspections for the different materials in the selected time frame. | The analysis path contains two analysis steps. Data of the 2nd step is influenced by the data points selected in the 1st step. |  |

### Analyze Nonconformance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to analyze defect records with respect to time, (master) inspection characteristic, material and plant, work center and plant, defect category, defect code group and code, customer, and supplier. You can drill down a hierarchy to carry out specific analysis or compare plants, materials, inspection characteristics, etc. A vast number of chart types enables you to visualize data according to your requirements.

Procedure

Nonconformance Analytics – General Test

This app is based on the same template as the app Inspection Lot Analytics - UDs Made in Last 365 Days (F3239). See section [Analyze Accepted and Rejected Lots](#unique_10) [page ] 13 for a description of the technical features.

Nonconformance Analytics – Example Analytics

The following table describes examples for analysis of defects. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Acess the App | Open Nonconformance Analytics - Defects Created in Last 365 Days (F3584). |  |  |
| 3 | Visualize the Number of Defects per Code as a Function of Time | Open Show Mini Tiles. On the Defect Analytics screen, in the dropdown field, select Defects by Time Series. | A column chart displays. The x-axis shows the different defect codes per year and month. The y-axis shows the number of defect records per category. |  |
| 4 | Pareto-Like Diagram for Defect Code Groups | Choose Drill Up to view the details. Choose Drill Down and select Defect Code Group.Choose Chart Type and select Waterfall Chart. | A pareto-like diagram displays. The x-axis shows the different defect code groups. The y-axis shows the number of defect records per category. |  |
| 5 | Visualize the Number of Notifications per Material | Choose Show Mini Tiles and choose Notification Analytics – Key Figures tile.From the dropdown list in the upper left, select Quality Notifications by Time Series.Choose Drill Down and select Material. | A column chart displays. The x-axis shows the different material per year and month. The y-axis shows the number of notifications per category. |  |

### Analyze Nonconformance Leveraging Nonconformance Detailed Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a quality engineer, you want to interactively explore defects step by step from different perspectives to analyze the current defect or quality situation. In each analysis step, you can investigate KPIs and select relevant data to filter the information displayed in subsequent steps. By combining different analysis steps and filters, you interactively create your own flexible analysis path, e.g. for root cause analysis.

Procedure

Nonconformance Detailed Analytics – General Test

This app is based on the same template as the app Inspection Lot Detailed Analytics - On Lots with Usage Decision in Last 365 Days (F3273). See chapter Analyze Inspection Lots Leveraging Inspection Lot Detailed Analytics.

Nonconformance Detailed Analytics – Example Analytics

The following table describes examples for analysis of defects. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

Open the app Nonconformance Detailed Analytics - Defects Created in Last 365 Days (F3583) and choose Add Analysis Step.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Analyze the Time Series of Defect per Material | First step:Defect > Defect by MaterialSecond step:Defect > Defect by Create OnSelect one or more materials in the first step. Open 2nd analysis step and review the creation dates of defects per material in the selected time frame. | The analysis path contains two analysis steps. Data of the 2nd step is influenced by the data points selected in the 1st step. |  |
| 2. | Analyze the Time Series of the Top 10 Inspection Characteristics with Defects | First step:Defect > Top 10 Inspection Characteristics with Most DefectsSecond step:Defect > Defect by Created OnSelect one or more Inspection Characteristics in the first step. Open 2nd analysis step and review the creation dates of defects per Inspection Characteristics in the selected time frame. | The analysis path contains two analysis steps. Data of the 2nd step is influenced by the data points selected in the 1st step. |  |

### Manage Defects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can easily monitor and manage defects created during the inspection process. The app also displays notification items from quality notifications and generic defects that were created manually.

Procedure

Manage Defects - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Defects (F2649). | The Manage Defects (F2649) screen displays. |  |
| 3 | Filter the Defects | In the header, you could filter defect with different values.Additional fields can be added to the Filter Bar via Adapt Filters and selecting More Filters in the dialog box. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page to toggle to the Visual Filter view. Choose a part of the donut chart or bar chart, respectively, to filter data. | Check if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different Views on Content Part | Choose Chart View and Table View at the top right of the page. | The Table View and Chart View are displayed. |  |
| 6 | Drilldown by Dimension | Choose View By on the icon bar and choose one dimension to drill to a more detailed data level. | The drilldown function should work properly. |  |
| 7 | Change Chart Type | Choose the Settings on the icon bar. In the dialog box, choose one chart type, select data types to be displayed and assign a role to each data type. | You are able to change the chart type. |  |
| 8 | Apply Visual Filter | Switch to Chart and Table View, representation and click one bar, data point, donut or pie chart section, etc. in the data chart. | The table below the chart is filtered according to the selected chart element. |  |
| 9 | Navigate to Defect | Select Details button in the table view (last column on the right) to display the respective defect. | Defect is opened. |  |

Manage Defects - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Analyze Defects Identified at Goods Receipt with Respect to Calender Year and Week per Plant | Enter the following data in the filter.Inspection Lot Origin: Goods Receipt (01)Drill down dimension:Plant | A line chart is displayed which displays the number of defects (y-axis) as a function of time and plant (x-axis). |  |
| 2 | Get an Overview over All Defects in a Pie Chart | Switch to Chart Type: Pie Chart.Open Settings:Choose No. of Occurrences for Measures.Choose Category for Defect Code. | A pie chart is displayed. The size of the segment corresponds to the number of defects of a certain code. |  |

### Display Results History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app you can display the results history for a task list characteristic or a master inspection characteristic for a quantitative characteristic. The valuation of a characteristic is shown as a graphic for the selected inspection lots. This allows you to compare inspection results over a longer period of time.

Procedure

Display Results History - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as the Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Results History (F2428). | The Display Results History (F2428) screen displays. |  |
| 3 | Filter the Result | In the header, you could filter results with different values.Additional fields can be added to or removed via Adapt Filters and selecting or deselecting Filters in the dialog box. | The corresponding data is filtered accordingly. |  |
| 4 | Display Data | To display data in the table, choose an aggregation level from the drop-down list and choose Go. | Data is displayed in the table. |  |
| 5 | Navigate to Aggregated Inspection Result | Select one line item that corresponds to a quantitative inspection characteristic. | Inspection results are displayed in a graph and table. Furthermore, statistical information (e.g. mean value, CpK index, and Cp index) is displayed. |  |
| 6 | Change Displayed Data | In table Inspection Results, select inspection results that shall be displayed in the chart. | The chart only displays selected inspection results. |  |

Display Results History - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Visualize Time Series of A Quantitative Inspection Result for A Selected Time | Aggregation level: Master Inspection CharacteristicOpen the Aggregated Inspection Result and display column Created On in table Inspection Results.Open Settings of Table Inspection Results and make the following settings:Filter by Created On between <DateFrom> to <DateTo>.Sort by Created On, Ascending | The inspection result (y-axis) is displayed as a function of the inspection lot ID (x-axis) in a run chart. As the table is sorted by creation date of the inspection lot, the x-axis implicitly corresponds to a time series. |  |

### Quality Level History - Skip Rate in Last 180 Days

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, the KPI skip rate of inspection lots and inspection characteristics is calculated. You can also use this app to analyze quality levels with respect to different criteria, e.g. material, date, plant, inspection type, etc. in order to further optimize the quality inspection process. It is possible to drill down to get more insight. Furthermore, you can navigate to the related raw data for further analysis.

The skip rate of inspection lots and inspection characteristics is displayed in the following views:

Skip History: Inspection Lots and Characteristics

Inspection Severities by Inspection Lots and Characteristics

Inspection Stages by Inspection Lots and Characteristics

List: Inspection Lots and Characteristics

Procedure

Quality Level History - Skip Rate in Last 180 Days - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Quality Level History - Skip Rate in Last 180 Days (F2915). | The app launched successfully. |  |
| 3 | Filter the Result | In the header, you could filter results by . Rel Date Function.Additional fields can be added to the Filter via Adapt Filters and selecting a filter in the dialog box (e.g. plant, inspection type, material, etc.). | Check if the content of the corresponding results is filtered accordingly. |  |
| 4 | Change Displayed Data | From the drop down in the upper left of the chart, select the data that should be displayed, for example:Skip History: Inspection Lots and CharacteristicsInspection Severities by Inspection Lots and CharacteristicsInspection Stages by Inspection Lots and CharacteristicsList: Inspection Lots and Characteristics | Respective data is displayed in a column chart or table view.Skip History: Inspection Lots and Characteristics The number of skipped and not skipped lots (characteristics) is shown on the left (right) y-axis as a function of time.Inspection Severities by Inspection Lots and Characteristics The number of inspection lots and inspection characteristics per severity level is displayed as a function of time.Inspection Stages by Inspection Lots and Characteristics The number of inspection lots and inspection characteristics per inspection stage and of the dynamic modification role is displayed as a function of time.List: Inspection Lots and Characteristics The list shows inspection lots and characteristics with skip status and skip rate. |  |
| 5 | Switch to Table View | Choose Tabular View on the upper right of the chart. | The graphical view is replaced with a table view. |  |
| 6 | Switch Back to Graphical View | Choose Chart View on the upper right of the table. | The table view changes back to a graphical view. |  |
| 7 | Change Display Settings | Select a different chart type.Choose the Settings button on the upper right of the chart.Activate a data item by selecting the box and select an appropriate role of the data item. | The graphical view is adapted according to your chosen settings. |  |
| 8 | Reset to Default View | Open Settings, choose button Restore and button OK. | Data is displayed as defined in the default settings. |  |
| 9 | Remove the Global Filter | Choose the Reset Filter icon on the top right of the page, choose OK in the Reset Filters screen. | The data displayed in the graph is changed accordingly. |  |
| 10 | Drill Down | Choose Drill Down button on the upper right of the chart and choose a dimension (e.g. material or inspection type). | Values on x-axis are split up according to the selected drill-down dimension. |  |
| 11 | Drill Up | Choose Drill Up button on the upper right of the chart to drill up one dimension | Drill-down dimension is removed from the x-axis. |  |
| 12 | Check Jump To… Function | Choose Jump To… in the top right corner of the page. | The following options for navigation with Jump To… are displayed:Manage Inspection Lots - This navigation option is relevant for List: Inspection Lots and Characteristics. If you select a lot from this list, the system navigates you to the object page of the respective lot.Manage Usage Decisions - The app Manage Usage Decisions (F2345) is opened with applied filter parameter. |  |

Quality Level History - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Display Ratio of Skipped and Non Skipped Lots and Characteristics For A Selected Plant and Per Calendar Year and Month in A Stacked Bar Chart | Global Filter:Plant: <Plant>Displayed data:Skip History: Inspection Lots and CharacteristicsChart Type:100 % Stacked Column Chart with 2 Y-Axes | The ratio of skipped and non skipped lots (left y-axis) and characteristics (right y-axis) is displayed in a bar chart. Each bar displays the absolute number of inspection lots / characteristics and the height of the bar corresponds to the relative ratio of skipped / non skipped lots (characteristics). |  |
| 2 | Display the Number of Inspection Lots and Characteristics That Were Inspected with A Certain Inspection Severity with Respect to Calendar Year and Month | Displayed data:Inspection Severities by Inspection Lots and CharacteristicsChart Type:Stacked Bar Chart with 2 X-Axes | The absolute number of inspection results (upper x-axis) and inspection characteristics (lower x-axis) is displayed in bars. On the y-axis, the bars are broken down to the inspection severity, calendar year, and calendar month, respectively. |  |

### Manage Control Charts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can display and manage control charts. Control charts graphically represent the characteristic values in an inspection and help detect deviations by comparing measured values against action limits.

Procedure

Manage Control Charts - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open the Manage Control Charts (F2810). | The Manage Control Charts (F2810) screen displays.. |  |
| 3 | Filter the Results | In the header, you could filter results with different values.Additional fields can be added to or removed from the Filter via Adapt Filters and selecting or deselecting Filters in the dialog box. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page to toggle to the Visual Filter view. Choose a part of the donut chart or bar chart, respectively, to filter data. | Check if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different Views on Content Part | Choose Chart View and Table View at the top right of the page. | The graphical view is replaced with a table view. |  |
| 6 | Drilldown by Dimension | Choose View By on the icon bar and choose one dimension to drill to a more detailed data level. | The drilldown function should work properly. |  |
| 7 | Change Chart Type | Choose the Settings on the icon bar. In the dialog box, choose one chart type, select data types to be displayed and assign a role to each data type. | You are able to change the chart type. |  |
| 8 | Apply Visual Filter | Switch to Chart and Table View, representation and click one bar, data point, donut or pie chart section, etc. in the data chart. | The table below the chart is filtered according to the selected chart element. |  |
| 9 | Navigate to Control Chart | Select Details button in the table view (last column on the right) to display the respective control chart. | Control chart is opened. |  |

Manage Control Charts - Example Analytics

The following table describes examples for analysis of inspection lots. Before executing each test step, we recommend to reset to default view in order to obtain a defined starting point.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Display the Number of Action Limit Violations per Material and Inspection end Date | Violated Type: 1 (Action Limit Violation)View Settings:Chart type: Column ChartSelect Inspection End Date, Material and Action Limit Violations.Choose Category for Inspection End Date and Material, respectively, and make sure that Inspection End Date (Material) corresponds to the first (second) line item. If not, change the order respectively.Choose Axis 1 for Action Limit Violations. | The absolute number of action limit violations (y-axis) is displayed as a function of the inspection end date and material number.Note It might be required to maximize the chart in order to being able to read the material number and description. |  |

### Manage Quality Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, the quality engineer can display, manage, and analyze quality tasks. Quality tasks are assigned to (generic) defects and usually document defect analysis, resolution, or mitigation. The quality engineer can get a list of tasks, the respective status and whether or not a task processor has been assigned. Furthermore, a graphical to-do list is generated by displaying the number of tasks as a function of time.

|  |
| --- |
| Note Only tasks generated with Scope Item 2QN (Defects and Problem-Solving Process) can be analyzed. |

Procedure

Manage Quality Tasks - General Test

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Manage Quality Tasks (F3381). | The app launched successfully. |  |
| 3 | Filter the Results | In the header, you could filter results with different values.Additional fields can be added to or removed from the Filter via Adapt Filters and selecting or deselecting Filters in the dialog box. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter at the top right of the page to toggle to the Visual Filter view. Choose a part of the donut chart or bar chart, respectively, to filter data. | Check if the content of the corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different Views on Content Part | Choose Chart View and Table View at the top right of the page. | The graphical view is replaced with a table view. |  |
| 6 | Change Chart Type | Choose the Settings on the icon bar. In the dialog box, choose one chart type, select data types to be displayed and assign a role to each data type. | You are able to change the chart type. |  |
| 7 | Apply Visual Filter | Switch to Chart and Table View, representation and click one bar, data point, donut or pie chart section, etc. in the data chart. | The table below the chart is filtered according to the selected chart element. |  |
| 8 | Change Task Status or Assign Processor (Optional) | Select one or more tasks and choose action Set in Process. Choose action Assign Processor and enter a processor business partner ID in the Assign Task Processor pop up. | Task status is changed to in process. A task processor is changed or assigned.Note Not every task can be set to In Process because superordinate object (defect or problem-solving process) does not allow this status change. In this case the message Task X cannot be set in process: Prohibited by superordinate object is displayed. |  |
| 9 | Navigate to Task Details | Choose the blue triangle in the right column of a task line item to navigate to the tasks details. | Task is opened in app . |  |

Manage Quality Tasks - Example Analytics

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Visualize Tasks by Task Processor | Chart type: Column ChartView Settings:Select Tasks and Task ProcessorChoose Axis 1 for Tasks and Category for Task Processor, respectively. | A column chart is displayed that shows the number of tasks assigned to each task processor. |  |
| 2 | Display Tasks Time Series by Planned End Date | Chart type: Bar ChartView Settings:Select Calender Year , Calendar Week and Tasks.Choose Axis 1 for Tasks and Category for Calender Year and Calendar Weeks, respectively. | A bar chart is displayed that shows the number of tasks (y-axis) as a function of the planned start date (x-axis). |  |
| 3 | Display a List Where a Task Processor Must be Assigned | Switch to Table View.Filter on header level by Processor Assignment = Not Assigned. | A list of tasks with empty task processor is displayed. You can select one or more tasks and assign a task processor by executing the respective user action Assign Processor.Note The same filter can also be set leveraging a visual filter. Switch to visual filters an select Not Assigned in the donut chart Tasks by Processor Assignment. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/test-script-quality-management-in-discrete-manufacturing-consumer-prod]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2V0_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 68,946 chars in the whole document
