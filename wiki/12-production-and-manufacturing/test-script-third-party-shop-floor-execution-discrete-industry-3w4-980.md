---
id: 12-production-and-manufacturing/test-script-third-party-shop-floor-execution-discrete-industry-3w4-980
title: "Test Script: Third-Party Shop Floor Execution – Discrete Industry (3W4) (3W4_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3W4: MES/third-party shop floor integration, from PIRs and MRP to capacity check and production orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/mes-and-shop-floor-integration]
aliases: [3W4_S4CLD2608_BPD_EN_XX]
keywords: [Manufacturing Execution System and Third-Party Shop Floor…, third-party shop floor execution, mes integration, planned independent requirements, material requirements planning, capacity evaluation, work center capacity, production orders, test prerequisites, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W4_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-980
topic: 12-production-and-manufacturing/mes-and-shop-floor-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Third-Party Shop Floor Execution – Discrete Industry (3W4) (3W4_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W4_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Manufacturing Execution System and Third-Party Shop Floor Integration** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Third-Party Shop Floor Execution – Discrete Industry (3W4) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232843302)

[2 Prerequisites 4](#_Toc232843303)

[2.1 System Access 4](#_Toc232843304)

[2.2 Roles 4](#_Toc232843305)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232843306)

[2.4 Additional Manual Configuration 5](#_Toc232843307)

[2.5 Business Conditions 5](#_Toc232843308)

[2.6 Preliminary Steps 6](#_Toc232843309)

[2.6.1 Create Initial Material Stock 6](#_Toc232843310)

[2.6.2 Check Available Capacity in Work Center 7](#_Toc232843311)

[3 Overview Table 9](#_Toc232843312)

[4 Test Procedures 10](#_Toc232843313)

[4.1 Create Planned Independent Requirements 10](#_Toc232843314)

[4.2 Material Requirements Planning 11](#_Toc232843315)

[4.3 Evaluate Capacity Situation 13](#_Toc232843316)

[4.3.1 Check Capacity Situation 13](#_Toc232843317)

[4.3.2 Apply Changes to Available Capacity 14](#_Toc232843318)

[4.4 Conversion of Planned Orders to Production Orders 16](#_Toc232843319)

[4.5 Production Order Processing for Subassembly 17](#_Toc232843320)

[4.6 Production Order Processing for Final Assembly 18](#_Toc232843321)

[5 Appendix 19](#_Toc232843322)

[5.1 Succeeding Processes 19](#_Toc232843323)

## Purpose

Overview

This scope item covers the setup of the integration from SAP S/4HANA Cloud Public Edition to Manufacturing Execution Systems (MES).

An MES integrates business and manufacturing processes that help to run efficient, high-quality production on the shop floor.

You can use this scope item as an example of how to integrate a local customer shop floor system directly into SAP S/4HANA Cloud Public Edition, giving manufacturing staff a clear overview of production operations and improving analytical capability for the management team. SAP S/4HANA Cloud Public Edition is the system of record for all master data. An MES or a shop floor system is the system of record for all work in progress (WIP) data.

This communication scenario provides end points (inbound and outbound) that can be used to integrate an on-premise third-party MES solution (Manufacturing Execution System) to production operation through OData calls and SOAP messages.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

The sample master data are reused from Production Capacity Evaluation (31L) scope item from US version as an example (plant 1710, storage location 171C). Please adopt according to your plant.

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/84a745f7b8ab8e2ad6dd37ecd8209b65)

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 31L - Production Capacity Evaluation | You have activated Production Capacity Evaluation (31L) scope item or any other scope item for production like Make-to-Stock Production – Discrete Manufacturing (BJ5).Demo data are reused from 31L scope item. |

### Preliminary Steps

#### Create Initial Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers in that case, process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations for raw materials RM1_CP, RM2_CP, RM3_CP and RM4_CP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). |  |  |
| 3 | Input Material | Make the following entries and press Enter:Material: <Material Number>Plant: for example, Plant 1 US (1710) |  |  |
| 4 | Select Stock | Choose the icon beside the stock that you want to add initial stock:Storage Location: for example, Raw mat. sto. loc.(171C)Unrestricted-Use Stock | The Manage Stock dialog box displays. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: <Enter a number>, for example, 1000Document Date: <Today>Posting Date: <Today> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

We recommend that you check the stock for SG1_CP and FG1_CP. To check, log on to the SAP Fiori launchpad as a Production Planner and open Manage Material Coverage - New Version (F0251A). If there is sufficient stock, remove some stock; otherwise, no plan orders are generated later. After removing some stock, run the test again.

You can either post initial stock directly to the storage location or refer to the Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test scripts.

#### Check Available Capacity in Work Center

Purpose

In the Best Practice pre-delivered contents, standard available capacity is applied to the work centers, and no shifts assigned initially. In case these values have been adjusted during test, we recommend you have a check to have better understanding of current available capacity for work center TURNING1, TURNING2, DRILING, FINICLN and ASSPKG.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center (CR02) screen, make the following entries, and press Enter:Plant: for example, 1710Work center: <Work Center> |  |  |
| 4 | Choose Capacity Category 001 | Choose the Capacities tab, and you can find 2 Capacity categories defined: 001 and 002.Double-click Capacity category: 001 | The Change Work Center: Capacity Overview screen displays. |  |
| 5 | Check Standard Available Capacity | On the Change Work Center: Capacity Overview screen for capacity 001, check standard available capacity. Following values are pre-set in this test scenario:Start time: 07:00:00End time: 16:00:00Length of break: 01:00:00Capacity Utilization: 100No. Ind. Capacities: 1For test purpose, we recommend to use the same values as above. |  |  |
| 6 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner.On the Change Work Center Capacity: Header screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend to delete any shifts effective within next 6 weeks.Choose any line you want to delete, then choose the Delete line icon in the upper right.Choose Back twice to screen Change Work Center Capacity: Header. |  |  |
| 7 | Choose Capacity Category 002 | Under the Capacities tab, double-click Capacity category: 002 | The Change Work Center: Capacity Overview screen displays. |  |
| 8 | Check Default Settings for Capacity Category 002 | Repeat step #5 and #6 for category 002 |  |  |
| 9 | Save | Choose Save | Work center XXX in plant 1710 is changed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_11) [page ] 10 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning](#unique_12) [page ] 11 | Production Planner | Schedule MRP Runs (F1339) | MRP Run is executed. |
| Evaluate Capacity Situation |  |  |  |
| [Check Capacity Situation](#unique_13) [page ] 13 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is identified. |
| [Apply Changes to Available Capacity](#unique_14) [page ] 14 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is resolved. |
| [Conversion of Planned Orders to Production Orders](#unique_15) [page ] 16 | Production Planner | Manage Material Coverage - New Version (F0251A) | Production Order is created. |
| [Production Order Processing for Subassembly](#unique_16) [page ] 17 |  |  |  |
| [Production Order Processing for Final Assembly](#unique_17) [page ] 18 |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Planned independent requirements are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Maintain PIRs screen, choose the user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the entry below is assigned:For example, Plant 1 US (1710)MRP Controller 002 (002)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of the other entries. |  |  |
| 4 | Filter Result | On the Maintain PIRs screen, make the following entries and choose Go:Plant: for example, 1710Period Indicator: Weekly (W)Search: FG1_CP | Material item displays. |  |
| 5 | Select Material Item | Select the material item, and choose Edit at upper right. |  |  |
| 6 | Edit PIRs | On the screen, enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 20 PC.Week 2 (current week + 3 weeks): 20 PC.Week 3 (current week + 4 weeks): 100 PC.Week 4 (current week + 5 weeks): 100 PC. |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirement planning is to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 1710 (or your plant).

Prerequisite

The finished product for MTS (FG1_CP) is planned at plant level. There is now a requirement for the material Finished Product MTS (FG1_CP) in plant 1710 (or your plant).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entriesFor 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: MRP for FG1_CPChoose Step 2.For 2. Scheduling Options section:Start Immediately: XChoose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3. Parameters section:Plant: for example, 1710Material: FG1_CPChanged BOM Components: selectSchedule: 2Planning Mode: 3Choose Check at bottom right.Choose Schedule. | A messsage appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job's status, enter MRP for FG1_CP in the search box and choose Go at the top right section of the screen. | The new job is created and displayed in the Application Jobs table when refreshed. |  |

### Evaluate Capacity Situation

#### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. In this activity, the capacities are checked for overload on bottleneck resources.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity screen displays. |  |
| 3 | Check App Settings | On the Manage Work Center Capacity screen, choose the user icon and select App Settings.In the dialog box, check only this entry is chosen for Area of Responsibility:For example, Plant 1 USMRP &Controller& 002 (002)Check entries for Load Personalization:Critical Load： 100%Normal Load: 80% |  |  |
| 4 | Filter | Make the following entries as filter, and choose Go.Editing Status: AllLoad Type: OverLoadEvaluation Horizon: 6 weeksWe here only focus on capacity requirement due to PIRs we just created. | A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Create Planned Independent Requirements section, increase the PIRs for FG1_CP in step 7. Then rerun the whole process. |  |
| 5 | Check Bottleneck Work Centers | Choose Settings from the above table. From Columns, you can choose different KPIs.KPIs on Capacity load (for example, Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. Red /Yellow/Green bar shows different percentage level of capacity utilization, with color coding according to the Critical Load/Normal Load settings. The Red bar indicates the available capacity exceeds Critical Load percentage, thus there is bottleneck with the work center. |  |  |
| 6 | Next Step | After identifying the bottleneck work center(s), stay on this page and go on test as described in the next section. |  |  |

#### Apply Changes to Available Capacity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the bottleneck resources, you may need to optimize capacity utilization by changing available capacity, e.g., via adding/changing shifts.

Procedure

Log on to the SAP Fiori launchpad as a Production Planner and open Manage Work Center Capacity (F3289). Execute steps as described in previous Check Capacity Situation section.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 0 | Check Capacity Situation | Check capacity utilization to identify bottleneck workcenter, as described in last section Check Capacity Situation. |  |  |
| 1 | Choose Bottleneck Resource | From the bottleneck work center list, choose one of them, for example:Work center: TURNING1 (CP-WC1, Turning 1)Capacity Category: Machine (001) |  |  |
| 2 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In the Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In the Operations section, the list provides details on related source orders, e.g. Planned Order for SG1_CP.In the Shift section, it gives review of available capacity for the specific work center. Check the shifts in bottleneck dates, and consider which shifts can be added in these dates in order to add available capacity. For example, if shift YS3 is not arranged, we may consider to add YS3 in these dates for this work center. | Bottleneck dates and possible addtitional shifts are identied. |  |
| 3 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 4 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | The Add Shift screen displays. |  |
| 5 | Check Shift is Added | Check items in Shift section, choose More in the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter e.g., Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 6 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under the Shift section, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 120%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 7 | Check Bottleneck | Check capacity utilization in section Overview. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 8 | Check Bottleneck for all the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity. | The bottleneck for all resources are resolved. |  |

### Conversion of Planned Orders to Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After capacity bottleneck is resolved, the planned orders for goods are to be produced internally.

Prerequisite

The MRP run has generated planned orders for Material Subassembly (SG1_CP) and Final Assembly (FG1_CP).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Find Material dialog box displays. |  |
| 3 | Select Material | Make the following entries and then choose OK.Material: FG1_CPPlant: for example, 1710Shortage Definition: MRP Standard | The Manage Material Coverage screen displays. |  |
| 4 | Find Planned Order | Choose the generated planned order. | Order information displays. |  |
| 5 | Convert Planned Order to Production Order | Select Convert from the Edit dropdown list in the Action column for planned order (PldOrd XXXX).In the Convert Planned order XXXX dialog box, choose the Convert to Production Order radio button, confirm End Date and Quantity. Choose OK.Repeat step#2 to #5 for SG1_CP. | The production order is created. |  |

### Production Order Processing for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute the scope item BJ5 for complete processing of production for semi-finished products: SG1_CP.

Procedure

Complete all the activities under Prodcution Order Processing for Subassembly described in the Test Script of the scope item Make-to-Stock Production – Discrete Manufacturing (BJ5), including:

- Material Staging for Subassembly
- Release Production Order for Subassembly (production order will be distributed to your 3rd party shop floor system).
- Confirm Production Operations for Subassembly in shop floor system
- Post Goods Receipt for Subassembly Production Order

Result

Semifinished goods SG1_CP is produced.

### Production Order Processing for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute the scope item BJ5 for complete processing of production for Finished products: FG1_CP.

Procedure

Complete relevant activities under Prodcution Order Processing for Final Assembly described in the Test Script of the scope item Make-to-Stock Production – Discrete Manufacturing (BJ5), including:

- Material Staging for Final Assembly
- Release Production Order for Final Assembly (production order will be distributed to your 3rd party shop floor system).
- Pick Components for Final Assembly
- Confirm Production Operations for Final Assembly in 3rd party shop floor system
- Post Goods Receipt for Final Assembly Production Order

Result

Finished goods FG1_CP is produced.

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| BEI - Period-End Closing – Plant | These are executed collectively as a part of month-end closing. For more information on the month-end closing procedure, see the Test Script Period-End Closing – Plant (BEI).Note that month-end closing can only be executed once a month. |

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
- related-to :: [[12-production-and-manufacturing/test-script-production-operations-with-manufacturing-execution-system]]
- related-to :: [[12-production-and-manufacturing/test-script-third-party-shop-floor-execution-process-industry-3w3-979]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3W4_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,346 chars in the whole document
