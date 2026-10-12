---
id: 01-solution-foundation-and-platform/test-script-situation-handling-31n-sap-s-4hana-cloud-public-edition-89
title: "Test Script: Situation Handling (31N) - SAP S/4HANA Cloud Public Edition (31N_S4CLD2608_BPD_EN_XX)"
description: "SAP Best Practices test script for scope item 31N Situation Handling: roles, prerequisite teams/data, and step-by-step tests of the standard and extended frameworks."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/responsibility-management-and-situation-handling]
aliases: [31N_S4CLD2608_BPD_EN_XX]
keywords: [Responsibility Management and Situation Handling, situation handling, standard framework, extended framework, situation types, responsibility management, closing situations, situation monitoring, test scripts, situation templates]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31N_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-895
topic: 01-solution-foundation-and-platform/responsibility-management-and-situation-handling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Situation Handling (31N) - SAP S/4HANA Cloud Public Edition (31N_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31N_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Responsibility Management and Situation Handling** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Situation Handling (31N) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232837291)

[2 Prerequisites 4](#_Toc232837292)

[2.1 System Access 4](#_Toc232837293)

[2.2 Roles 4](#_Toc232837294)

[2.3 Additional Manual Configuration 5](#_Toc232837295)

[2.4 Business Conditions 5](#_Toc232837296)

[2.5 Preliminary Steps for the Standard Framework 6](#_Toc232837297)

[2.5.1 Prepare Data 6](#_Toc232837298)

[2.5.2 Create Team 8](#_Toc232837299)

[2.6 Preliminary Steps for the Extended Framework 10](#_Toc232837300)

[2.6.1 Create Team 10](#_Toc232837301)

[3 Overview Table 12](#_Toc232837302)

[4 Test Procedures 13](#_Toc232837303)

[4.1 Test the Standard Framework 13](#_Toc232837304)

[4.1.1 Create and Trigger Situation Type 13](#_Toc232837305)

[4.1.2 Handle Situation 15](#_Toc232837306)

[4.1.3 Monitor Situation (optional) 16](#_Toc232837307)

[4.2 Test the Extended Framework 17](#_Toc232837308)

[4.2.1 Create Situation Type 18](#_Toc232837309)

[4.2.2 Trigger Situation 19](#_Toc232837310)

[4.2.3 Handle Situation 20](#_Toc232837311)

[4.2.4 Monitor Situation (optional) 22](#_Toc232837312)

## Purpose

Overview

Critical business situations, such as upcoming deadlines and pending confirmations, can negatively impact your business if users aren’t aware of them and don’t take action. Situation Handling speeds up the resolution of urgent issues by detecting them automatically, informing the right users, and proposing follow-up actions. With its monitoring capabilities, you can optimize your business processes by tracking the life cycle of situations from alert to solution.

With the standard framework, you can select from a wide range of predefined use cases and adapt them to your business requirements.

With the extended framework, you can model your own situations from scratch by reusing existing application artefacts.

For testing Situation Handling, choose one of the two frameworks and follow the respective test procedure. Of course, you can also test both frameworks, but this isn't required. For more information about their capabilities, refer to [Situation Handling in a Nutshell](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/4f5e8536fe82403ea6685439db5afc3c.html).

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

Roles Required for Situation Handling

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |

Additional Role Required for Testing

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

You also need the Business Process Specialist business role template to create teams with responsibility management. Teams determine who is responsible for solving a situation.

You need the Accounts Payable Accountant business role template to create a supplier invoice, which is the basis for the test case of the standard framework. If you just want to test the extended framework, you don't need this business role template.

The Accounts Payable Accountant business role template isn't required for using Situation Handling apps, but it's a prerequisite for testing Situation Handling end to end.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/4ff3008e458c73920f5d7ab84862c4d5)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1NJ - Responsibility Management | Must be activated before this test script. |

### Preliminary Steps for the Standard Framework

#### Prepare Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To test the standard framework, you need to prepare data that can later trigger situations.

In this example, a supplier invoice with a blocked payment is created. Situations are later triggered with a situation type based on the situation template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON). In this use case, relevant users are notified about blocked invoices that are due soon.

This use case let's you test Situation Handling without further preparation or setting up a productive system. If you're already running a productive system, you can use your own data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open the Create Supplier Invoice (F0859) app. | The Create Supplier Invoice screen is displayed. |  |
| 3. | Enter General Information | On the General Information tab under Basic Data, enter the following information:Transaction: InvoiceCompany Code: 1010Note In this example, sample data is used to make sure everything works well. If you're already running a productive system, you can use your own data.Gross Invoice Amount: Only select the currency EUR in the second input field. The amount is entered later.Invoice Date: TodayPosting Date: TodayReference: Any value such as XXXInvoicing Party: Enter 1010 as the filter and pick any supplier that shows up for company code 1010. |  |  |
| 4. | Add G/L Account Item | On the G/L Account Items tab, choose Add. | A new row for a G/L Account Item appears. |  |
| 5. | Enter G/L Account Item information | Enter the following information:Debit/Credit Indicator: DebitGL/ Account: 61003000 (Travel Expenses - Hotel and Accomodation)Amount: 100To expand the G/L Account Items line item section, choose Show Details.Enter Tax Code: V0 (Input Tax non taxable).Choose a Cost Center. |  |  |
| 7. | Enter Gross Invoice Amount | Go back to the upper General Information tab.Enter Gross Invoice Amount: 100. |  |  |
| 8. | Enter Payment Details | In the Payment tab, check that the Baseline Date is the same date you entered in the fields Invoice Date/Posting Date on the General Information tab.Tip If you experience any issues entering data in the Payment section, try to select another Invoicing Party under General Information.In Payment Block (JE), select A (Blocked for payment). |  |  |
| 9. | Simulate Supplier Invoice | Choose Simulate.If errors occur, resolve them and choose Simulate again.Tip This is a simplified standard procedure. Errors may occur, because different fields are available on the UI in some locations. If this is not covered in this procedure, go to [J13](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J13). Select your location/langugage from the dropdown list and open Test Script in the Details section. In the document, search for "supplier invoice", find the standard process for creating a supplier invoice. While creating the supplier invoice, select Payment Block (JE): A (Blocked for payment) in the Payment section and set any due dates to today's date.If everything seems fine, choose Post. | The invoice is posted. A dialog box displays a success message.Remember Don't close the dialog box yet. |  |
| 10. | Note Down Number | Note down the supplier invoice number, for example 5105792484/2023.Close the dialog box by choosing No. |  |  |

#### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To test the standard framework, create a team using responsibility management and add your user as a member. This way, your user will be notified about new situations. To create a team, use the Manage Teams and Responsibilities (F2412) app.

For more information, refer to the app description under [Manage Teams and Responsibilities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/73c04858392e9244e10000000a4450e5.html).

In this procedure, you create the team and responsibilities later used by situation template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Business Process Specialist. |  |  |
| 2 | Access the App | Open the Manage Teams and Responsibilities (F2412) app. | All teams are displayed. |  |
| 3 | Create a Team | Choose Create. | A new object page opens where you can define your team. |  |
| 4 | Maintain General Information | Enter the following information in the General Information section:Name: Any value such as Operational PurchasingGlobal ID: Any value such as OPPURStatus: Choose Enabled.Type: Choose OPPUR (Operational Purchasing). |  |  |
| 5 | Maintain Team Member | In the Team Members section, choose Create and add your user.Under Functions, open the value help and add OP_PURCH (Operational Purchasing). | Your user is listed in the Team Members section with the necessary function.Note This is not a real use case. You need to add yourself to "Operational Purchasing" to test the standard framework and to get notifications based on the situation template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON). In a productive system, the Business Process Specialist defines team members from operational purchasing in this section as recipients and not themselves. |  |
| 6 | Save the Team | Choose Create to create and save the team. | You've created a team with your user as a team member. Your user will be notified about situations based on the situation template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON) that you'll define in a later process step [Create and Trigger Situation Type](#unique_9) [page ] 13. |  |

### Preliminary Steps for the Extended Framework

#### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To test the extended framework, create a team using responsibility management and add your user as a member. This way, your user will be notified about new situations. To create a team, use the Manage Teams and Responsibilities (F2412) app.

For more information, refer to the app description under [Manage Teams and Responsibilities](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/73c04858392e9244e10000000a4450e5.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Business Process Specialist. |  |  |
| 2 | Access the App | Open the Manage Teams and Responsibilities (F2412) app. | All teams are displayed. |  |
| 3 | Create a Team | Choose Create. | A new object page opens. You can define your team there. |  |
| 4 | Maintain General Information | Enter the following information in the General Information section:Name and Global ID: Enter a value, such as SITDEMOTEAM.Status: Choose Enabled.Type: Choose Situation Handling Demo (SITDEMO). |  |  |
| 5 | Maintain Team Member | In the Team Members section, choose Create and add your user.Under Functions, open the value help and add Travel Agent (STRVL_AGNT). | Your user is listed in the Team Members section with the necessary function. |  |
| 6 | Save the Team | Choose Create to create and save the team. | You've created a team with your user as a team member. Your user will be notified about situations based on a Situation Handling demo use case, that you'll define in a later process step [Create Situation Type](#unique_11) [page ] 18. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Test the Standard Framework

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Trigger Situation Type](#unique_9) [page ] 13 | Business Process Specialist | Manage Situation Types (F2947) | You've created a situation type that can trigger situations. |
| [Handle Situation](#unique_13) [page ] 15 | Employee | My Situations (F4154) | You've closed a situation. |
| [Monitor Situation (optional)](#unique_14) [page ] 16 | Business Process Specialist | Monitor Situations (F3264) | You've monitored the occurrence and the life cycle of the situations. |

Test the Extended Framework

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Situation Type](#unique_11) [page ] 18 | Configuration Expert - Business Process Configuration | Manage Situation Types - Extended (F5437) | You've created a situation type that can trigger situations. |
| [Trigger Situation](#unique_15) [page ] 19 | Business Process Specialist | Situation Handling Demo (F5697) | You've triggered situations. |
| [Handle Situation](#unique_16) [page ] 20 | Employee | My Situations - Extended (F4537) | You've closed a situation. |
| [Monitor Situation (optional)](#unique_17) [page ] 22 | Business Process Specialist | Monitor Situations - Extended (F6780) | You've monitored the occurrence and the life cycle of the situations. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Test the Standard Framework

#### Create and Trigger Situation Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Manage Situation Types (F2947) app to create situation types that are used in the standard framework to inform end users about issues.

For more information, refer to the app description under [Manage Situation Types](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/60748ea9f37d4692912578b698aaefee.html).

Follow this procedure to create and activate a situation type to trigger situations, based on the situation template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON). This template is used as an example that lets you test Situation Handling with the data that you've already created in the process step [Prepare Data](#unique_7) [page ] 6. You can use any other template but don't forget to prepare data for it.

Prerequisites

- You've prepared data for template Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON): [Prepare Data](#unique_7) [page ] 6
- You've created a suitable team: [Create Team](#unique_8) [page ] 8

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the App | Open the Manage Situation Types (F2947) app. | On the Manage Situation Types screen, there are two tabs, Situation Templates and Situation Types. Per default, you are on the Situation Templates tab. |  |
| 3 | Create a Situation Type | Choose the Due Date for Blocked Invoice Approaching (MM_DUEDATEREACHSOON) situation template.Choose Copy to create your situation type. | A new object page opens. It has inherited all the default settings from the situation template. |  |
| 4 | Define Admin Information for the Situation Type | Enter the following information:ID: Start with Y or Z and enter a meaningful ID such as Z_MM_DUEDATEREACHSOON.Name: Keep or change the proposal from the selected situation template.Tip You can freely define the ID and Name. If you need more information about structuring and filling these fields, refer to the [UI text guidelines](https://experience.sap.com/internal/fiori-design-web/situation-handling-framework-ui-text-guidelines/#configuration-texts1). |  |  |
| 5 | Modify Condition | On the Conditions tab, open Used Filters.For Net Due Date, remove all values and make sure it's blank. This enables the situation type to find blocked invoices of every due date. |  |  |
| 6 | Monitor Instances | On the Situation Monitoring tab, select the checkbox in Monitor Instances. |  |  |
| 7 | Create Batch Job | On the Batch Job Scheduling tab, enter the following information:Time Zone: Select a time zone, such as CET, based on your location.Start Batch Job At: Select the preferred time, such as 12:00. |  |  |
| 8 | Select Recipient | On the Recipients tab in the Filter by Member Fuction column, select Operational Purchasing from the list.Remember If you haven't done it so far, make sure to create an enabled team with your user as a member, following process step [Create Team](#unique_8) [page ] 8. | Your user will be notified about situations triggered by the situation type. |  |
| 9 | Save the Situation Type | Choose Create to create and save the new situation type. | The situation type is saved and a dialog window appears. |  |
| 10 | Enable the Situation Type | Enable the new situation type by choosing Yes in the dialog window. | The situation type is enabled. |  |
| 11 | Trigger the Situation Type | At the top of the object page, choose Trigger Now.Choose OK in the success message. | You've triggered the newly created situation type. Situations are created and displayed. A notification is displayed.Note Sometimes, it can take some time for the situations to be created and the notification to be displayed. Choose the Refresh button to update the list. |  |

#### Handle Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the My Situations (F4154) app to see all situations that are in your area of responsibility. In this app, you can:

- Go from the situation list entry to the situation object page in a corresponding business app.
- Close a situation manually.

For more information, refer to the app description under [My Situations](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/67439c313b834f7ca2048da985824faa.html).

You're also informed about situations with notifications on SAP Fiori launchpad or email notifications. For more information about notifications, refer to [Notifications](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/359191322c5a405984be3681bc5f529e.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Employee. |  |  |
| 2 | Access the App | Open the My Situations (F4154) app. | You see all open situations in your area of responsibility. |  |
| 3 | Go to the Corresponding App | Choose an open situation from the list.Tip Alternatively, you can go directly to the corresponsing business app by choosing the notification that you've received on SAP Fiori launchpad. | This takes you to the corresponding business app.Tip In the corresponding app for the affected business object, you can try to resolve the cause of the situation, which closes the situation automatically. In this example, you could open the invoice and then reverse or release it. This would close the situation automatically. For this test procedure, don't do that now because you will close the situation manually in the next step. |  |
| 4 | Close the Situation Manually | Go back to the My Situations (F4154) app.In the list, select the checkbox of a situation.Then choose Close Situations. | There are three statuses available for when you close a situation manually:ResolvedObsoleteInvalid |  |
| 5 | Confirm | Select one of the three options such as Resolved, then choose Confirm. | The status of the situation changes, and it is no longer displayed in the list. |  |

#### Monitor Situation (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Monitor Situations (F3264) app to monitor the occurrence and the life cycle of situations. In this analytical app, you can display activities performed for situations in a variety of chart types and/or as a table.

For more information, refer to the app description under [Monitor Situations](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/1bfaf5c220304709bffa5e05502dbe97.html).

Prerequisites

The Monitor Instances option is enabled in the situation type that you've created in a previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the App | Open the Monitor Situations (F3264) app. | By default, you see all activities from the current year in a chart and a table with additional details. |  |
| 3 | Try Out Different Filters, Visualizations, Fields | Play around with the app to get a feel for the filter and visualization options. For example, filter for the situation type that you created in a previous step or choose a different chart type, such as a bar chart.Scroll down to the Instance Details table view. By choosing  (Settings) , you can also display additional fields. For example, display the Description of Activity Trigger and Status to show who triggered the instance and what its current status is. | You are familiar with the options for analyzing situation data. |  |

### Test the Extended Framework

In the extended framework for Situation Handling, you can select from standard use cases, delivered as situation templates by SAP.

To test the extended framework, use a demo situation template that informs end users about overbooked flights, based on a simplified, fictional booking portal.

In addition to the standard use cases, you can create custom situations based on a specific business object, such as a contract, a service order, an invoice, or a material. A wide range of configuration options help you tailor your custom situations to your business requirements. For example, you can model your own situation objects, specify events that trigger situations, or configure a situation page including actions that help the end user solve situations.

Creating custom situations isn't required for testing the extended framework, especially since more profound planning of the use case is needed. However, if you already want to try out creating custom situations, check out the following information material to better understand the process:

- Introductory information on SAP Help Portal: [Situation Handling - Extended Framework](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/92a58a164a4c4320bd6bf563d745baca.html)
- Blog post series that shows you how to create custom situations step by step, starting with the first blog post: [Custom Situation Cases: Configure Your Own Use Cases (1/6)](https://blogs.sap.com/2022/03/15/custom-situation-cases-configure-your-own-use-cases-1-6/)

#### Create Situation Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Manage Situation Types - Extended (F5437) app to create situation templates and types that can be used in the extended framework to inform end users about issues.

For more information, refer to the app description under [Manage Situation Types - Extended](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/45d60edcf02d409c87076f9270372eb8.html).

Follow this procedure to create and activate a situation type to trigger situations, based on a demo situation template for overbooking. For more information, refer to [Demo Template: Booking Rate](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/a94dcc693bd84c168985d01e9469eded.html).

Prerequisites

- You've created a team as described under [Create Team](#unique_10) [page ] 10.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open the Manage Situation Types - Extended (F5437) app. | You see all exisiting situation templates and types. |  |
| 3 | Create a Situation Type | Choose Create > Create Situation Type. | A dialog box appears. |  |
| 4 | Select a Situation Template and Define Basic Information for the Situation Type | Enter the following information:ID: Enter a meaningful ID, such as SITDEMO_OVERBOOKING. The system automatically adds a prefix, for example, YY1_, YY2_, and so on.Name: Enter a meaningful name, such as Overbooked Economy Class.Description: Enter a meaningful description of the use case, such as Checks for overbooked economy class seats.Situation Scenario: SITDEMO_FLIGHT_PROFITABILITYSituation Template: SITDEMO_BOOKING_RATETip You can freely define the ID, Name, and Description. If you need more information about structuring and filling these fields, refer to the [UI text guidelines](https://experience.sap.com/internal/fiori-design-web/situation-handling-framework-ui-text-guidelines/#configuration-texts1).Choose Create. | A new object page opens. This page has inherited all the default settings from the situation template. |  |
| 5 | Check that Your User Is a Recipient | On the Recipients tab, make sure that the Situation Handling Demo Team is enabled and that your user is a member of the team. | Your user will be notified about situations triggered by the situation type. |  |
| 6 | Save the Situation Type | Choose Create to create and save the new situation type. | The situation type is saved and a dialog window appears. |  |
| 7 | Enable the Situation Type | Enable the new situation type by choosing Yes in the dialog window. | The situation type is enabled. |  |

#### Trigger Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Situation Handling Demo (F5697) app to trigger situations for the situation type that you created and enabled in the previous process step. This app contains test data for exploring the extended framework. This app is a simplified version of a booking portal focusing on actions for flights and bookings.

For more information, refer to the app description under [Situation Handling Demo](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/6a2a048d025e46aa936a0264caa0309c.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the App | Open the Situation Handling Demo (F5697) app. |  |  |
| 3 | Generate New Flight Data | Choose Generate New Data and confirm in the dialog box. | Sample flight data is generated. You see a list of upcoming flights with additional information, such as the seating occupancy or the sales rate. |  |
| 4 | Select a Flight | Select a flight that departs within the next two weeks. Note down the Connection ID and Flight Date. | An object page opens. It shows detailed information about the flight you've selected. |  |
| 5 | Overbook the Flight | On the Bookings tab, select an economy class passenger (E). Replicate the booking as many times as needed to exceed the maximum number of economy class seats.Note You can overbook economy passengers up to the maximum number of business class seats. | An information message displays the new confirmed and unconfirmed economy class bookings. An overbooking situation is triggered. |  |

#### Handle Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the My Situations - Extended (F4537) app to see all situations that are assigned to you. In this app, you can:

- Go from the situation list view to the situation page where you can try to close the situation with the help of proposed actions.
- Close a situation manually.

For more information, refer to the app description under [My Situations - Extended](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/5137227e8fce4240830d20a875b99704.html).

You are also informed about situations with notifications on SAP Fiori launchpad or email notifications. For more information about notifications, refer to [Notifications](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/359191322c5a405984be3681bc5f529e.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Employee. |  |  |
| 2 | Access the App | Open the My Situations - Extended (F4537) app. | You see all open situations in your area of responsibility. |  |
| 3 | Go to the Situation Page | Select an overbooking situation from the list. Then choose the arrow on the right-hand side of the table entry.Tip You can go directly to the situation page by choosing the notification that you received on SAP Fiori launchpad. | You are on the situation page where the booking details for each of the overbookings are displayed. |  |
| 4 | Under Common Actions, Select an Action(Alternatively, Go to Step 5) | On the Common Actions tab, three actions that close the situation are displayed:Cancel BookingsUpgrade PassengersRebook Passengers | If you choose any of these options, the proposed action is performed and the situation is closed automatically. |  |
| 5 | Go to the Corresponding App | The buttons in the Related Apps section take you to other apps that may help you remove the root cause of a situation.In our test case, the Manage Flight Bookings option lets you go to the Situation Handling Demo (F5697) app. There, on the Bookings tab, you can remove some of the overbooked economy class bookings by choosing the appropriate action:Upgrade to business class.Change to the next flight for the same connection.Cancel the bookings.Note If you remove all overbooked economy class bookings, the situation is closed automatically. | In the My Situations - Extended (F4537) app, the booking information is updated accordingly. |  |
| 6 | Close the Situation Manually | Choose Close Situation.Three statuses are available for closing a situation manually:ResolvedObsoleteInvalid | For the remaining overbookings, choose Resolved and confirm your selection.The status of the situation changes and the situation is no longer displayed in the list of open situations in the My Situations - Extended (F4537) app. |  |

#### Monitor Situation (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Monitor Situations - Extended (F6780) app to monitor the occurrence and the life cycle of situations. In this analytical app, you can display activities performed for situations in a variety of chart types and/or as a table.

For more information, refer to the app description under [Monitor Situations - Extended](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/6867ecc92b144a5083971a3d01b7a623.html).

Prerequisites

The Monitor Instances option is enabled in the situation type that you've created in a previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the App | Open the Monitor Situations - Extended (F6780) app. | By default, you can see all activities from the current year in a chart and a table with additional details. |  |
| 3 | Try Out Different Filters, Visualizations, Fields | Play around with the app to get an idea of the filter and visualization options. For example, filter for the situation type that you've created in a previous step or choose a different chart type such as a bar chart. With the Settings icon, you can also display additional fields.Scroll down to the Instance Details table view. By choosing  (Settings) , you can also display additional fields. For example, display Activity Source and Instance Status to show who triggered the instance and what the current status of the instance is. | You are familiar with the possibilities of analyzing situation data. |  |

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
- related-to :: [[01-solution-foundation-and-platform/test-script-responsibility-management-1nj-746]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31N_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 40,919 chars in the whole document
