---
id: 14-maintenance-service-and-projects/test-script-project-control-intercompany-4au-ae-sap-s-4hana-cloud-publ
title: "Test Script: Project Control – Intercompany (4AU_AE), SAP S/4HANA Cloud Public Edition (4AU_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4AU (AE): intercompany project control, from project creation to expense posting and billing."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/intercompany-project-services]
aliases: [4AU_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Project-Based Services and Project Control, intercompany project control, project creation, project release, direct activity allocation, intercompany expense posting, intercompany billing, intercompany cost rates, activity types, time recording]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AU_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1013
topic: 14-maintenance-service-and-projects/intercompany-project-services
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Intercompany (4AU_AE), SAP S/4HANA Cloud Public Edition (4AU_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AU_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Project-Based Services and Project Control** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Control – Intercompany (4AU_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854828)

[2 Prerequisites 4](#_Toc232854829)

[2.1 System Access 4](#_Toc232854830)

[2.2 Roles 4](#_Toc232854831)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854832)

[2.4 Business Conditions 6](#_Toc232854833)

[2.5 Preliminary Steps 7](#_Toc232854834)

[2.5.1 (Optional) Configure Activity Types 7](#_Toc232854835)

[2.5.2 Maintain Inter Company Cost Rates 8](#_Toc232854836)

[2.5.3 Check/Create Intercompany Sales Order 10](#_Toc232854837)

[3 Overview Table 11](#_Toc232854838)

[4 Test Procedures 12](#_Toc232854839)

[4.1 Create Project 12](#_Toc232854840)

[4.2 Release Projects/Project Parts 16](#_Toc232854841)

[4.3 Direct Activity Allocation 17](#_Toc232854842)

[4.4 Time Recording 18](#_Toc232854843)

[4.5 Post Intercompany Expense 19](#_Toc232854844)

[4.6 Run Intercompany Billing Process 20](#_Toc232854845)

[5 Appendix 21](#_Toc232854846)

[5.1 Process Integration 21](#_Toc232854847)

[5.1.1 Preceding Processes 21](#_Toc232854848)

[5.1.2 Succeeding Processes 21](#_Toc232854849)

## Purpose

Overview

A company has an affiliate company that delivers a service to the ordering company during a project. The affiliate company posts expenses and records time on the project. These expenses are transformed into billing document requests. The delivering company creates an intercompany invoice that references billing document request. The intercompany invoice is also posted automatically to the accounts payables of the ordering company.

Note:

The intercompany process described here is sample data. In this case, the ordering company is DE, and the delivering company is US. The scenario is restricted to one direction: US delivers services for DE.

If you want to apply intercompany for other countries, adapt country-specific data as mentioned in scope item Intercompany Billing for Cross-Company Cost Accounting Postings (4AN).

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
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Internal Sales - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | P002 | Project-Based Service: Time & Expenses | Material which is used in order to describe different services being provided to the customer |
| Material | E001 | Accommodation |  |
| Material | E002 | Airfare |  |
| Material | E003 | Ground Transportation |  |

|  |
| --- |
| Note Allowed changes to the above listed service-related materials are limited to descriptions and some attributes, since they are provided with DIP-Profile, a technical object necessary for selling of project-based services. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling Area | A000 | Controlling Area A000 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Cost Center | 331015013310160133101321 | R&D Cost centerMarketing Cost CenterServices/Consltg |  |
| Activity Types | 8 | Consulting |  |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers and activity types:Cost centers: 33101321, 33101101Activity types: 8 |  | Cost Rates are defined time-dependent |
| G/L Account | 61005000 | Trav. Expense – Ground transportation |  |
| 61007000 | Trav. Expense – Airfare, Rail, Mileage |  |  |
| 61003000 | Travel Expenses – Hotel and Accommodation |  |  |
| 61008000 | Travel Expenses – Miscellaneous |  |  |
| 10010000 | Petty Cash |  |  |
| Profit Center | YB600YB110 | Shared ServicesProduct A |  |
| Functional Area | YB25YB75 | Consulting/ServicesOther expenses |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT – Project Control – Finance | To execute the project creation /execution related activities, the Project Control – Finance (1NT) scope item must be activated. |
| 4AN – Intercompany Billing for Cross-Company Cost Accounting Postings | To execute the intercompany billing process for projects, the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item must be activated. |

### Preliminary Steps

#### (Optional) Configure Activity Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can configure your own activity types. Activity type 8 is already delivered. It is recommended to create your own activity type by copying Activity 8.

|  |
| --- |
| Note Currently, activity types with G/L 94308000 are supported only for the IC process. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Activity Types (F1605A) app. | The Manage Activity Types (Version 2) screen is displayed. |  |
| 3 | Find the consulting activity valid on the current date | Make the following entries and choose Go:Activity Type: 8Valid On: Today | The consulting activity valid on the current date is displayed in the list view. |  |
| 4 | Create a new activity type | Select the displayed line item, and choose Copy.The New Activity Type screen displays in the right pane.On the General Information tab, make the following entries:Activity Type: PActivity Unit: HName: Project ConsultingValid From: <Current date>Valid To: 12/31/9999Cost Center Categories: *(All Categories)On the Allocation tab, make the following entry:Activity Type Category: 1(Manual entry, manual allocation)Choose Save. | The activity type P is created and a confirmation message is displayed. |  |

#### Maintain Inter Company Cost Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check whether actual inter-company cost rates are maintained. If they are not, you define your own actual inter-company cost rates.

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Manage Cost Rates - Services (F3161) app. | The Manage Cost Rates - Services screen is displayed. |  |
| 3 | Check the actual inter-company cost rates | Set an appropriate filter to check the actual inter-company cost rates.Example Set the filter by making the following entries, and choose Go:Company Code: 3310Valid On: <Current date>Receiving Company: 1010Cost Center: 3310 1321 and 3310 1101Tip The cost centers to which employees belong and against which the activity allocation is being done.Activity Type: 8Currency: AED | The actual inter-company cost rates for the specified cost center, activity type, and period are displayed in the list view. |  |
| 4 | Maintain additional actual inter-company cost rates | If the actual inter-company cost rates are not defined or if you want to add additional actual inter-company cost rates, then proceed as follows:Choose Add.On the Create Cost Rates - Company Code xxxx dialog box, make the appropriate entries.ExampleReceiving Company: 1010Select the ICO Rate check box.Cost Center: 3310 1321 and 3310 1101Activity Type: 8WBS Element: O.0000011From FY: <Current fiscal year>From Period: <Current period>Rate: 100Currency: AEDper: 1Activity Unit: HTip The WBS Element should be of the project created under the Receiving Company code.Choose Save. | Additional cost rates are created. |  |

#### Check/Create Intercompany Sales Order

To execute this activity, perform the step Check Intercompany Sales Order under Time and Expenses Intercompany Settlement in the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) test script.

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Project](#unique_11) [page ] 12 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Release Projects/Project Parts](#unique_12) [page ] 16 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project status is changed to REL (Released). |
| [Direct Activity Allocation](#unique_13) [page ] 17 | Project Financial Controller | Manage Direct Activity Allocation - Deprecated (F3697) | Actual activities that occurred in relation to a WBS element are confirmed. |
| [Time Recording](#unique_14) [page ] 18 | See the Time Recording (1Q4) scope item. | See the Time Recording (1Q4) scope item. | See the Time Recording (1Q4) scope item. |
| [Post Intercompany Expense](#unique_15) [page ] 19 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Actual primary costs are posted to WBS elements. |
| [Run Intercompany Billing Process](#unique_16) [page ] 20 | See the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item. | See the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item. | See the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) scope item. |

## Test Procedures

### Create Project

Purpose

In this activity, you create projects of the following type based on the business requirement, with the project definition and WBS element using the Fiori app Project Control - Enterprise Projects (F3215):

- Overhead Project
- Investment Project
- Project with Revenue
- Statistical Project

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Project Financial Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen is displayed. |  |
| 3 | Create Project: Definition | Choose Create.Make entries as shown in the following example in the Header and General Information sections:Example HeaderProject Name: Overhead ProjectProject ID: O.000001Note If the entered ID is in use for another project, then the system prompts an available ID.Project Profile: Overhead ProjectPlanned Start: <Current date>Planned Finish: <Current date + 3 months>General information:Responsible Cost Center: <Example:3310 1501(R&D)>Profit Center: <YB600 (Shared Services)>Project Currency: EUR (Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project specific financial reports.Project Manager: The Project Manager IDPriority: the priority suitable for projectProject Type: Project Type created using the Create Project Types for WBS Elements SSCUI.Attachments: Choose + to upload project relevant documents from your local drive.Note To rename the existing attachment, choose the Edit icon present next to the attachment and change the file name according to the requirement.Choose Rename.Choose Create.A success message tells you that the project is saved. | Project is created with the provided definition parameters.One WBS Element with details as shown in the following example will be created under the project:Example WBS Element ID: <O.000001>Project Name: <Overhead Project> |  |
| 4 | Add Values to the Project Summary Task WBS Element | Once the project is created, from the header section, choose Edit.Make the following entries:General InformationPlant: 3310 (for example)Functional Area: <YB75 (Other expenses)>ControlInvestment Profile: <000001>Note The Investment profile field is relevant only for investment projects and the profile can be selected based on the business requirementCosting Sheet:3310 PI (for example)The following are optional entries, maintain them according to your requirements.Availability Control Profile: ZS001If project currency is maintained, you can assign an availability control profile where the budget currency is maintained as Global Currency or Project CurrencyIf project currency is not maintained, you can only assign an availability control profile where the budget currency is maintained as Global Currency.Availability Control Profile is active: SelectedYou can define your own budget availability profile using the Maintain Budget Availability Profile SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Note You would be able to see Joint Venture (JV) attributes under the section Joint Venture Accounting during project creation, if the Joint Venture accounting functionality has been activated in the system. For the detailed explanation on JV attributes, you can refer to the scope item 3F7-Joint Venture Accounting.Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>NoteYou can also block certain functions based on the business requirement for the project being created.The Block functions need to be set at the individual Work Package level to enable the functionality.Setting up the block functions at Project Header level will not impact the complete project hierarchy.Choose SaveA system message tells you that the project has been saved | WBS Element updates with all the provided parameters.Note In case you have entered an availability control profile and activated the budget availability control, all postings resulting into commitments or actual costs will be checked against the available budget of the WBS element used as account assignment object. In case the WBS element itself does not have any budget, the next higher-level budget carrying WBS element will be used for the budget availability check. Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages. Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a fiscal year or across fiscal years.This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a WBS element. Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. |  |
| 5 | Navigate to Project Planning | Once the project is created, from the header section, choose Related Apps. A pop-up screen appearsFrom the pop-up screen, select Project Planning to go to the Project Planning app.Note By default, the project will open in the Display mode. To edit the project, choose Edit. | The Project Planning app is opened and you can make further entries. |  |
| 6 | Create WBS Elements under Project Summary Task WBS Element. | In the Project Structure view, select WBS Element created in the above step, and choose Create.Make the following entries in the Details screen onto the right.ID: <Example: O.0000011>Name: WBS for project planningProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element created in the above step, and choose Create.ID: <Example: O.0000012>Name: WBS for project executionProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsCreate WBS Element structure based on your requirements.Note You can also create WBS Element by making use of the Copy functionality available in the Project Planning Application. | Project with WBS Element structure is updated with the provided parameters. |  |
| 7 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved |  |

### Release Projects/Project Parts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the project to enable the project execution.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project: <Refer the respective Project created in the chapter Create ProjectO.000001 (for Overhead Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Release Project and Structure | Select the project and in header section choose Processing Status > Release | Project status is changed to Released.For investment projects, AuCs will be created for those WBS elements with a proper investment profile assigned.You can also use the Change Processing status using the Project Briefs as a Project Manager role.Project once released cannot be renamed or deleted. |  |
| 5 | Maintain Actual Start Date in WBS Elements | Choose Related Apps > Project Planning. Choose Edit to open the project in change mode.For all created WBS elements, maintain Actual Start Date field in WBS Element detailed overview pageChoose Save. | Project is saved with WBS elements Actual start dates. |  |

### Direct Activity Allocation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm actual activities that occurred in relation to a WBS element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Manage Direct Activity Allocation - Deprecated (F3697). | The Manage Direct Activity Allocation screen is displayed. |  |
| 3 | Enter Activity Allocation | In the Activity Allocations tab choose Create and , make the following entries:Header Information:Journal Entry Date: TodayPosting Date: TodayIn the Allocation Items area, make the following entries and press Enter:Sender Cost Center: 3310 1321Sender Activity Type: 8Receiver WBS Element: <Refer the respective WBS element created in the chapter Create Project >Quantity: 10 | A new object page appears. |  |
| 4 | Post Activity Allocation | Choose Save. | The Journal Entries section appears showing the document number. |  |

### Time Recording

Purpose

In this activity, employee enters the time recording for WBS Element using Manage My Timesheet (F1823) application.

Procedure

To execute this activity, execute Time Recording (1Q4) test script, using the WBS Element from this document.

Note While creating the task, maintain the Activity Type as 8 and WBS Element created in the Create Project step of this test script. The employee should belong to delivering company.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element ID | <O.0000012> | <WBS for project execution> |  |

### Post Intercompany Expense

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post actual primary costs to WBS elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Create Supplier Invoice (F0859) app. | The Create Supplier Invoice screen is displayed |  |
| 3 | Enter General Data | On the New Supplier Invoice screen,In the General Information area, make the following entries:Basic dataTransaction: InvoiceCompany Code: 3310 (for example)Invoice date: <Today>Posting date: <Today>Gross Invoice Amount: Value of IC Expense <Ex:100>Invoicing Party: 3310 0002 (for example)Choose See More.DetailsDocument Type: ER (Manual Expense Travel)In the G/L Account Items area, make the following entries:Choose “+” to G/L account ItemDebit /Credit ind : DebitG/L Account: 61003000Amount : Value of IC Expense <Ex:100>Choose Expand All.Tax Code: I0WBS Element: <Refer the respective Work Package created in the chapter Create Project >Personnel Number: <Employee ID>Note The employee must belong to the delivering company.Choose Save as Completed. | A success message appears showing the document number. |  |
| 4 | Post invoice | Choose Post. | the Invoice is Created |  |

### Run Intercompany Billing Process

Procedure

To execute this activity, perform the steps Generate Intercompany Billing Request under Time and Expenses Intercompany Settlement section and Create Intercompany Invoice under Invoicing section in the Intercompany Billing for Cross-Company Cost Accounting Postings (4AN) test script.

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BNA | Period-End Closing – Projects |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-intercompany-processes-project-based-services-16t-ae-704]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AU_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 30,246 chars in the whole document
