---
id: 12-production-and-manufacturing/test-script-rework-processing-work-in-process-bjq-ae-1276
title: "Test Script: Rework Processing - Work-in-Process (BJQ_AE) (BJQ_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item BJQ (AE): rework operation inserted within a production order, confirmed and settled in S/4HANA Cloud Public Edition 2608, plant 3310."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/rework-processing]
aliases: [BJQ_S4CLD2608_BPD_EN_AE]
keywords: [Rework Processing, production order confirmation, rework operation, reference operation set, routing, manage production operations, manufacturing object pages, master data scripts, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1276
topic: 12-production-and-manufacturing/rework-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Rework Processing - Work-in-Process (BJQ_AE) (BJQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rework Processing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Rework Processing – Work-in-Process (BJQ_AE)Purpose PUBLIC 1Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Rework Processing – Work-in-Process (BJQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861908)

[2 Prerequisites 4](#_Toc232861909)

[2.1 System Access 4](#_Toc232861910)

[2.2 Roles 4](#_Toc232861911)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861912)

[2.4 Business Conditions 6](#_Toc232861913)

[2.5 Preliminary Steps 6](#_Toc232861914)

[2.5.1 Assigning Reference Operation Set to Routing 6](#_Toc232861915)

[3 Overview Table 9](#_Toc232861916)

[4 Test Procedures 10](#_Toc232861917)

[4.1 Confirm Rework Required for Defective Material 10](#_Toc232861918)

[4.2 Confirm Production Order at Rework Operation 11](#_Toc232861919)

[4.3 Manage Production Operations 12](#_Toc232861920)

[4.4 Confirm Subsequent Operation Including Reworked Quantity 14](#_Toc232861921)

[4.5 Review Manufacturing Object Pages 15](#_Toc232861922)

[4.6 Delete Reference Operation Set from Routing 16](#_Toc232861923)

[5 Appendix 18](#_Toc232861924)

[5.1 Process Integration 18](#_Toc232861925)

[5.1.1 Succeeding Processes 18](#_Toc232861926)

## Purpose

Overview

This scope item focuses on a rework process within production. All required rework activities are related to the production order. For this reason, defects are recognized and corrections are initiated, such as insertion of a rework operation within the same production order. The additional rework operation is confirmed and settled within the production order, causing production variances within controlling and price differences for the dedicated product.

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
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo | Other finished good materials can be used |
| Reference Operation Set | 43310005 |  | Could be assigned to any other routing operation. In this test script, it is assigned to routing for material FG126 (see Preliminary steps). |
| Routing | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo | You can assign the reference operation set to any other routing for which you want to show the rework functionality. For demo purposes, we only listed the data originating from Make-to-Stock Production – Discrete Manufacturing (BJ5) scope item. |
| Plant | 3310 | Plant 1 AE |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLE | Create Reference Operation Set - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the following steps described in the test script MDS: Create Costing Run - MDS (Product Costing) (BNU). |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | After you have assigned the reference operation set to the routing (see section Preliminary Steps), complete the following activities described in the test script Make-to-Stock Production – Discrete Manufacturing (BJ5)Create Production Order for final assembly (Finished Good). Make sure that planned orders are generated in the system.Material Staging for Assembly (Finished Good). Make sure that the required components are available in stock.Releasing Assembly Order (Finished Good)Picking Components (Finished Good)Confirming Assembly Activities (Finished Good), only the first activity |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Assigning Reference Operation Set to Routing

Purpose

This process step shows you how to assign the reference operation set to any routing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing: Initial Screen displays. |  |
| 3 | Enter Details | Make the following entries and press Enter:Material: FG126Plant: 3310Group: 43310000Group counter: 01 | The Change Routing: Operation Overview screen displays. |  |
| 4 | Turn to Trigger Point Overview | Select operation number 0020 and choose Menu > GoTo > Trigger point overview . | The Change Routing: Operation Trigger Points screen displays. |  |
| 5 | Enter Trigger Point | Make the following entries and choose Enter.Trigger point usage: 00004Description: Insert operation setIndicator: Functions: Set |  |  |
| 6 | Turn to Trigger Point Details | Select the row of your trigger point and choose Menu > Details > Trigger point . | The Change Routing: Trigger Point Details screen displays. |  |
| 7 | Enter the Trigger Point details | Make the following entries and choose Enter.Indicator: Release succeeding operations: Function: SetSyst. Sts.: PCNFChange: +Indicator: Insert reference operation set: Function: SetSyst.Sts: PCNFChange: + |  |  |
| 8 | Turn to the Parameters | Mark Insert reference operation set and choose Parameters. | The Parameters for Function dialog box displays. |  |
| 9 | Enter the Parameters | Make the following entries and choose Enter:Group: 43310005Group Counter: 1After Operation: 0020 |  |  |
| 10 | Save | Select Back and choose Save. | Note If you get the pop up that says Task list data contains errors. Do you still want to save? and has the buttons Yes, No and Cancel, choose Yes and save. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Confirm Rework Required for Defective Material](#unique_9) [page ] 10 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | Defects are recorded within the time ticket confirmation.The new Rework - Operation is automatically inserted in the Parent Production Order. |
| [Confirm Production Order at Rework Operation](#unique_10) [page ] 11 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The rework operation is confirmed, costs were settled within the original production order. The rework process is complete. |
| [Manage Production Operations](#unique_11) [page ] 12 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | Detailed operations status displays. |
| [Confirm Subsequent Operation Including Reworked Quantity](#unique_12) [page ] 14 | Production Operator - Discrete Manufacturing | Confirm Production Order Operation (CO11N) | The subsequent operation is confirmed. |
| [Review Manufacturing Object Pages](#unique_13) [page ] 15 | Any role for production listed in chapter Roles | Search function | The list of search result displays. |
| [Delete Reference Operation Set from Routing](#unique_14) [page ] 16 | Production Engineer - Discrete Manufacturing | Change Routing (CA02) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Confirm Rework Required for Defective Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Some operations produce more defects due to operational or component defects. To simulate the process, some predefined operations are triggered automatically at the end of the planned required operation. These are also released automatically and are followed by production execution as normal production parts.

In the following scope item, the assembly of the finished product is confirmed. During the next operation, defects are detected in the final acceptance. A rework process is triggered immediately, the rework activity is confirmed, and the additional material consumption is posted.

To simulate the process, we assume that some defects were found by inspection during production. For this reason, the insertion of a rework operation within the same production order is initiated automatically.

Prerequisite

The reference operation set for Finished Good MTS (FG126) is defined. The production order is created and released, and has an order quantity of less than 100. The goods movements for the components have been posted. The first operation of the production order is finally confirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Enter.Order: <Order Number>Enter the number of your Finished Good order that you noted down before.Operation: 20Rework: <Quantity>. Must be equal or less than the confirmed yield quantity of the previously confirmed operation 0010. For example, 2. | The system displays the message Activities are recalculated due to quantity change. |  |
| 4 | Save | Choose Post. |  |  |
| 5 | Confirm the Remaining Quantity of the Order | Repeat steps 1 to 4 for operation 0020 with confirmation type Final Confirmation and save via choosing Post and Complete.Yield: <Quantity>Must be equal or less than the amount that order quantity minus rework quantity.Scrap: <Quantity>Enter the scrap quantity (order quantity - rework quantity - yield quantity) and choose Enter. |  |  |

### Confirm Production Order at Rework Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step step shows you how to confirm and settle the additional rework operation within the original production order. This causes production variances within controlling and price differences for the dedicated product.

Prerequisite

Defects are recorded in the confirmation of the previous operation. The Rework Operation is automatically inserted into the operative routing of the Production Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Enter.Order: Order Number. Enter the number of your Finished Good order you noted down in the previous step.Operation: 0022 | Ignore possible warning messages.The defects are now repaired (rework is finished). |  |
| 4 | Confirm the Quantity and Labor | Make the following entries and choose Enter.Yield: <Quantity>. Must be equal or less than the confirmed rework quantity of the previously confirmed operation 0020. For example, 2.Labor: <Labor time>, for example, 60MIN |  |  |
| 5 | Enter the Goods Movement Details | In the Material Movements section, choose Add Material, make the following entries and choose Add.Material: <any raw material in the BOM>, for example, RM20Plant: 3310Storage Location: 331BQuantity to be Posted: 2UoM: EA or PC <Depends on the material> |  |  |
| 6 | Post | Choose Post and Complete. |  |  |

### Manage Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the release /confirm of finished goods orders is performed, this process step shows you how to display and review the order using the Manage Production Operations (F2335) App for the Finished Good MTS (FG126).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335). | The Manage Production Operations (F2335) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations (F2335) screen, enter the following search condition as filter.To review the Default Area of Responsibility (supervisor), select the user from the top left of the view: App Settings Area of Responsibility Production Supervisor and ensure only the following displays:Plant: 3310MTS DI - Valuated (YB1)Choose Adapt Filters to display more selection filters. Select the checkbox for Material and Plant, and choose OK. Material and Plant fields are then added to filter bar.Status: ConfirmedMaterial: FG126Plant: 3310 (Production plant)Choose Go to execute. | Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issues:Empty if there is no issue for production order.Delay/Missing Components/PRT issue/Quantity Deviation/Quality Issue information shows if relevant issue exists.Components: Material, total quantity and Issued/open quantity information for order components displays.Order Schedule: Detailed operation information with relevant work center, confirmed quantity, start/end time displays.Work Center Schedule: The relevant order that covering the same work center capacity (operation is partially confirmed) displayed.Operations not Started: The relevant order that would cover the same work center capacity (operation is released) displayed.Confirmation: Detailed confirmation information with 'Yield', 'Scrap' & 'Rework' quantity displays if confirmation executed.Inspection: Detailed inspection lots information displays if existed. |  |  |

### Confirm Subsequent Operation Including Reworked Quantity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to confirm the subsequent operations after rework operation confirmation executed, which could summarize the yield quantity from previous operation and rework operation.

Prerequisite

The confirmation of the previous operations (including rework operation) is executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Details | Make the following entries and press Enter.Order: <Order Number>. Enter the number of your Finished Good order you noted down in the previous step.Operation: 0030Confirm. Type: Final confirmation |  |  |
| 4 | Confirm the Quantity and Labor | Make the following entries and press Enter.Yield: <Quantity>. Must be equal or less than the overall confirmed yield quantities of operation 0020 and rework operation 0022.Scrap: <enter the amount you want to Scrap>Setup: <Setup time that you want to confirm for this operation>Machine: <Machine time that you want to confirm for this operation>Labor: <Labor time that you want to confirm for this operation> |  |  |
| 5 | Save | Choose Save. | Entries are saved. |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Roles section above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:Products: Material (see the Master Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In the All field, choose Down arrow.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message is displayed instead. |  |
| 5 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort) to filter the results list. | The results list is filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1-5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

### Delete Reference Operation Set from Routing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to delete the reference operation set from routing after finish all steps for BJQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). | The Change Routing: Initial Screen displays. |  |
| 3 | Enter the Details | Make the following entries and press Enter:Material: FG126Plant: 3310Group counter: 01, from Lot Size 1 to Lot Size 100. | The Change Routing: Operation Overview screen displays. |  |
| 4 | Turn to Trigger Point Overview | Select operation number 0020 and choose Menu > GoTo > Trigger point overview . | The Change Routing: Operation Trigger Points screen displays. |  |
| 5 | Delete Trigger Point | Select the trigger point you have created and choose Delete.Trigger point usage: 00004Description: Insert operation setIndicator: Function: SetOn the Delete message choose Yes. | Trigger point is deleted. |  |
| 6 | Save | Choose Back and choose Save. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Make-to-Stock Production – Discrete Manufacturing (BJ5) | Using the master data from this document, complete the following activities described in the test script:Final Confirmation of ProductionPosting Goods Receipt for Production Order |

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
- related-to :: [[12-production-and-manufacturing/rework-processing-stock-manufactured-material-bjn-ae-test-script-1275]]
- related-to :: [[12-production-and-manufacturing/test-script-rework-with-quality-management-consumer-products-6a9-ae-11]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,970 chars in the whole document
