---
id: 01-solution-foundation-and-platform/test-script-information-lifecycle-management-1ka-sap-s-4hana-cloud-pub
title: "Test Script: Information Lifecycle Management (1KA), SAP S/4HANA Cloud Public Edition (1KA_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 1KA Information Lifecycle Management: audit areas, ILM rules, rule generator, archiving, data destruction and file conversion steps."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/information-lifecycle-and-data-protection]
aliases: [1KA_S4CLD2608_BPD_EN_XX]
keywords: [Information Lifecycle Management and Data Protection, information lifecycle management, audit areas, ilm policies and rules, rule generator, ilm business rules, archiving variants, archiving jobs, data destruction, ilm file conversion]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1KA_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-732
topic: 01-solution-foundation-and-platform/information-lifecycle-and-data-protection
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Information Lifecycle Management (1KA), SAP S/4HANA Cloud Public Edition (1KA_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1KA_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Information Lifecycle Management and Data Protection** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Information Lifecycle Management (1KA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232851075)

[2 Prerequisites 3](#_Toc232851076)

[2.1 System Access 3](#_Toc232851077)

[2.2 Roles 3](#_Toc232851078)

[3 Overview Table 4](#_Toc232851079)

[4 Test Procedures 5](#_Toc232851080)

[4.1 Maintain Audit Area 5](#_Toc232851081)

[4.2 Assign ILM Object to Audit Area 6](#_Toc232851082)

[4.2.1 Purpose 6](#_Toc232851083)

[4.3 Maintain Authorization Groups for ILM Blocking 7](#_Toc232851084)

[4.3.1 Purpose 8](#_Toc232851085)

[4.4 Maintain ILM Object Groups 9](#_Toc232851086)

[4.5 Maintain ILM Policies and Rules 10](#_Toc232851087)

[4.6 Rule Generator 12](#_Toc232851088)

[4.6.1 Manage ILM Business Rules 17](#_Toc232851089)

[4.7 ILM Rules Overview Page 18](#_Toc232851090)

[4.8 Manage Archiving Variants 21](#_Toc232851091)

[4.9 Monitor Archiving Jobs 23](#_Toc232851092)

[4.10 ILM Data Destruction 25](#_Toc232851093)

[4.11 Manage ILM File Conversion 26](#_Toc232851094)

## Purpose

Overview

Personal data in SAP applications must be protected according to the data protection laws. This is achieved by blocking and deleting data according to residence and retention rules. Residence rules are set to define the time for which data can stay in the database, after which it is archived. Retention rules are defined to store the archive files for a set amount of time, after which they can be destroyed.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Audit Area](#unique_6) [page ] 5 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Assign ILM object to Audit Area](#unique_7) | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Maintain Authorization Groups for ILM Blocking](#unique_8) | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Maintain ILM Object Groups](#unique_9) [page ] 9 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Maintain ILM Policies and Rules](#unique_10) | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Rule Generator](#unique_11) [page ] 12 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) |  |
| [Manage ILM Business Rules](#unique_12) [page ] 17 | Data Privacy Specialist | Manage ILM Business Rules (F2340) |  |
| [Manage Archiving Variants](#unique_13) [page ] 21 | Data Privacy Specialist | Manage Archiving Variants (F0627A) |  |
| [Monitor Archiving Jobs](#unique_14) [page ] 23 | Data Privacy Specialist | Monitor Archiving Jobs (F0510A) |  |
| [Manage ILM File Conversion](#unique_15) | Data Privacy Specialist | Manage ILM File Conversion (F5366) |  |
| [ILM Data Destruction](#unique_16) [page ] 25 | Data Privacy Specialist | ILM Data Destruction (F2662) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Maintain Audit Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you're testing the maintenance of the audit area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution (F1241). Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Audit Area.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Lanchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Maintain Audit Area configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management. |  |  |
| 3 | Create an Audit Area | To create a new audit area, click on Configure for the corresponding configuration step. Go to Edit. Choose New entries and enter Audit Area, a Description, and select the Policy Category. Save your entry.Note You need to create an audit area in Y or Z customer namespace. |  |  |
| 4 | Edit the Audit Area | Select an existing audit area from the list. To edit it, choose Edit and update the description. Save your entry. |  |  |
| 5 | Copy the Audit Area | Select an existing audit area from the list and choose Copy as from the application toolbar. In the dialog box, enter a name for the new audit area to which you want to copy the existing one and click on Copy. Save the entry. |  |  |
| 6 | Delete Audit Area | Select an existing audit area from the list. Choose Delete from the toolbar option. Save your changes. |  |  |

### Assign ILM Object to Audit Area

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

#### Purpose

In this step, you're testing the assignment of ILM object to an audit area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution (F1241). Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign ILM Object to Audit Area.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Launchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Assign ILM Object to Audit Area configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management. |  |  |
| 3 | Assign ILM Object to Audit Area | To create a new assignment of ILM object to audit area or to edit an existing assignment, click on Configure for the corresponding configuration step. Select Policy Category and Audit Area and click on Execute. On the next screen, choose Edit and click on New Entries. Enter the ILM Object and set Status to Active.If you want to edit an assignment, select an exisiting assignment and click on Edit. Update Status to Inactive and save the entry. |  |  |

### Maintain Authorization Groups for ILM Blocking

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

#### Purpose

In this step, you're testing the maintenance of authorization groups for ILM Blocking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution (F1241). Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Authorization Groups for ILM Blocking.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Launchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Maintain Authorization Groups for ILM Blocking configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management. |  |  |
| 3 | Maintain Authorization Groups for ILM Blocking | To create a new authorization group, click on Configure for the corresponding configuration step. Click on New Entries. Select Auth. Grp. and add Description and Save your entry. |  |  |
| 4 | Edit Authorization Groups | Select an existing authorization group. Change Description and Save. |  |  |

### Maintain ILM Object Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this configuration activity to maintain ILM object groups. You can assign ILM objects to an object group. You can also create rule groups and maintain authorization groups in them.

In this step, you're creating, editing, and deleting object groups that can be used during the creation of ILM rules for ILM objects. ILM object groups are used to group logically related ILM objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution. Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain ILM Object GroupsChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Launchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Maintain ILM Object Groups configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management. | The Maintain ILM Object Groups app is displayed. |  |
| 3 | Maintain ILM Object Groups | To create a new object group, start by choosing Edit. Click on New Entries. Select Policy Category. Enter the values for Object Group and Description and Save your entry.To assign the object to a rule group, select the newly created object group and double-click on Rule Group . Click on New Entries. Select Rule Group, add Description, and Save your entry.For assigning an ILM object to an object group, select the object group and double-click on Object Group and ILM Object Assignment. Select the ILM Object and tick the UseRuleGrpif you need the rule groups column to be displayed in all policies of the corresponding ILM object. Save your entry. |  |  |
| 4 | Edit an ILM Object Group | Select the object group to be edited and choose Edit.You can edit the Description and Save your entry. |  |  |
| 5 | Copy an ILM Object Group | Select an existing object group and click on Copy As. Specify the target entries and click on Copyand Save. |  |  |
| 6 | Delete an ILM Object Group | Select an existing object group and click on Delete and Save your entry. |  |  |

### Maintain ILM Policies and Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you're testing the maintenance of ILM policies and rules.

Rules generated using the Rule Generator can be displayed here.

You can use this app to create a specific rule for a specific ILM object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution (F1241). Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain ILM Policies and Rules.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Launchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Maintain ILM Policies and Rules configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management.Note You might need to set the country version first (see the button on the lower right side of the screen. |  |  |
| 3 | Maintain ILM Policies and Rules | Click on Configure for the corresponding configuration step. To view an existing policy, select theILM Object, a Policy Category and an Audit Area and click on ExecuteTo create a new policy, choose Edit and click on New Entries.Enter a Policy name, add a Comment and Save the entry.Optionally, you can add condition fields to the created policy. To do so, select the newly created policy and double-click on Selected Condition Fields. Click on New Entries. Enter values for Position and select a value for Condition Field. Save your entry.Note You can maintain a maximum of four condition fields.Depending on the chosen policy category, you can create residence or retention rules for the ILM Policy. To do so, select the policy and double-click on Residence Rules or Retention Rules. Enter the values for all the fields ( Residence Period or Retention Period, Time Unit, Time Reference, Time Offset, Priority and Comment for a Rule) and Save the entry.For the rule created above, you can assign condition field values. To do so, select the rule and double-click on Conditions. Enter values for Condition Field, From and To fields and Save your entry.Go back to the policy and set the Status to Live.You can click the ILM Rules Overview button to get an overview of the rules based upon selection parameters like Policy Category and Audit Area(s). |  |  |
| 4 | Edit an ILM Policy | Select an existing policy and click on Copy As. Specify the target entries and click on Apply. Save your entry. |  |  |
| 5 | Delete an ILM Policy | Select an existing policy and click on Delete. Confirm deletion and Save your entry. |  |  |

|  |
| --- |
| Note To enable the Data Protection and Privacy (5LE) scope, a set of Retention and Residence Rules need to be maintained. The modeling of the rules needs to be done by customers to meet their legal and personal requirements. Find here an example of what kind of rules are required for Master Data objects: |

| Policy Category | Audit Area | ILM Object | Application Name |
| --- | --- | --- | --- |
| Retention Rules | BUPA_DP | CA_BUPA | BUP |
| Retention Rules | BUPA_DP | FI_ACCPAYB | ERP_VEND |
| Retention Rules | BUPA_DP | FI_ACCRECV | ERP_CUST |
| Residence Rules | BUPA_DP | CA_BUPA | BUP |
| Residence Rules | BUPA_DP | FI_ACCPAYB | ERP_VEND |
| Residence Rules | BUPA_DP | FI_ACCRECV | ERP_CUST |

|  |
| --- |
| Note The ILM residence rules have to be created by maintaining the value of Audit Area = ARCHIVING. |

### Rule Generator

A set of optional configuration steps to ensure the compliance of personal data with general data privacy acts.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Rule Generator app to ensure that personal data is stored according to applicable legal requirements and in compliance with the general data privacy acts. Any personal data collected or processed is linked to a predefined purpose. The data controller determines the purposes for which and the manner in which any personal data is to be processed. Even after the residence period ends, personal data can still be retained for other explicit legal reasons. The reasons include retention periods prescribed by law, statutes, or contracts. After the end of all retention periods, personal data must be destroyed.

The Rule Generator app simplifies the maintenance of these residence periods and retention periods. It defines the purpose of storing personal data representing the business processes used and the business objects involved. The definition of the data controller assigns the line organization attributes, which represent the data controller in the system. The rule maintenance is based on the data controller and the purposes defined for a data controller. The data controller and the defined purposes are related to the data in the system and to the Information Lifecycle Management (ILM) objects. The activation of maintained rules creates all the required ILM configuration and policies for each assigned ILM object according to its individual settings.

A customer key user maintains a business rule and then triggers the generation of ILM residence and retention rules.

The configuration steps for the ILM Rule Generator app are:

- Set Default Audit Area
- Set Time Reference and Time Offset
- Define Data Controller
- Define Purpose of Retention Rules

Prerequisite

The Configuration Expert - Business Process Configuration business role must be assigned to you.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

1. Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the configuration activity | Open Manage Your Solution. Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Rule Generator. You can see all the configuration steps listed on the right-hand side.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the configuration activity.Then, choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesLog on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration ( SAP_BR_BPC_EXPERT).Navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management > Data Controller Rule Framework.Note You might need to set the country version first (see the button on the lower right side of the screen. |  |  |
| 3 | Set Default Audit Area | To set default audit area, choose Configure for the corresponding configuration step.Select an audit area and click on Execute to set it as default. | You have set the default audit area that is used by the rule generator for the creation of retention policies. |  |
| 4 | Set Time Reference and Time Offset | To set a new time reference and time offset, choose Configure for the corresponding configuration step.On the Set Time Reference and Time Offset: Overview screen, choose New Entries.Select the values for ILM Object, Time Reference, Time Offset and Time Offset, and save your entry. | You have set the default time reference and time offset for an ILM object, which is to be used to generate rules for all ILM policies. |  |
| 5 | Define Data Controller | To maintain the data controller, choose Configure for the corresponding configuration step.On the screen, choose New Entries. Enter a name and a description for the data controller object and save your entry.Select the newly created data controller object from the list and double-click on Assign Organization Entities.Select an organizational entity and click Save to assign the entity to a data controller.Next, select the newly created entity and double-click on Set Conditions for Organization.Choose New Entries. Enter the required values in the Range from Value and Range to Value fields.Save your entry. | You have defined the organization entity. |  |
| 6 | Define Purpose | To maintain the purpose definition, choose Configure for the corresponding configuration step.On the app screen, choose New Entries.Enter the values for Purpose ID and a description and save your entry.Select the newly created purpose from the list and double-click on Assign ILM Objects to Purpose and choose New Entries. Select an ILM object that you want to assign to purpose and click Save.Select the newly created object from the ILM Object list.Double-click on Maintain Condition Fields and choose New Entries. Enter the required information in the Condition fields, From and To fields. Choose Save.Note Make sure that the field maintained in Data Controller created in step 6 is not part of the ILM Object Condition field. | You have defined a purpose, which indicates a purpose that can be used when defining retention rules in SAP ILM or when providing information about personal data. The purpose represents a business process that groups ILM objects relevant for that process. These ILM objects have the same residence rules and retention rules. |  |

1. SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Project Experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. For this test step, search for the following configuration activities:Set Default Aufit AreaSet Time Reference and Time OffsetDefine Data ControllerDefine PurposeChoose Open documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system.Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Set Default Audit Area | To set default audit area, choose Configure for the corresponding configuration step.Select an audit area and click on Execute to set it as default. | You have set the default audit area that is used by the rule generator for the creation of retention policies. |  |
| 4 | Set Time Reference and Time Offset | To set a new time reference and time offset, choose Configure for the corresponding configuration step.On the Set Time Reference and Time Offset: Overview screen, choose New Entries.Select the values for ILM Object, Time Reference, Time Offset and Time Offset, and save your entry. | You have set the default time reference and time offset for an ILM object, which is to be used to generate rules for all ILM policies. |  |
| 5 | Define Data Controller | To maintain the data controller, choose Configure for the corresponding configuration step.On the screen, choose New Entries. Enter a name and a description for the data controller object and save your entry.Select the newly created data controller object from the list and double-click on Assign Organization Entities.Select an organizational entity and click Save to assign the entity to a data controller.Next, select the newly created entity and double-click on Set Conditions for Organization.Choose New Entries. Enter the required values in the Range from Value and Range to Value fields.Save your entry. | You have defined the organization entity. |  |
| 6 | Define Purpose | To maintain the purpose definition, choose Configure for the corresponding configuration step.On the app screen, choose New Entries.Enter the values for Purpose ID and a description and save your entry.Select the newly created purpose from the list and double-click on Assign ILM Objects to Purpose and choose New Entries. Select an ILM object that you want to assign to purpose and click Save.Select the newly created object from the ILM Object list.Double-click on Maintain Condition Fields and choose New Entries. Enter the required information in the Condition fields, From and To fields. Choose Save.Note Make sure that the field maintained in Data Controller created in step 6 is not part of the ILM Object Condition field. | You have defined a purpose, which indicates a purpose that can be used when defining retention rules in SAP ILM or when providing information about personal data. The purpose represents a business process that groups ILM objects relevant for that process. These ILM objects have the same residence rules and retention rules. |  |

#### Manage ILM Business Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the Manage ILM Business Rules (F2340) app, you can create, delete, edit, and display business rules. In this step, you're defining the data controller and purpose to be used and you're defining residence and retention periods. On activation of this business rule, the ILM rules are generated. You can check the rules in the [Maintain ILM Policies and Rules](#unique_10) configuration activity.

Prerequisite

You must have been assigned to the Data Privacy Specialist business role.

Procedure

| Test Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Manage ILM Business Rules (F2340) app. |  |  |
| 3 | Create a Business Rule | In the Manage ILM Business Rules (F2340) app, click on Create.In the General Information section, enter the values for all the fields and click on Create. Go back to see the newly created rule listed under ILM Business Rules. | The ILM business rule is saved as a draft. |  |
| 4 | Activate the ILM Business Rule | Select the radio button of the newly created business rule in the previous step.Choose Activate.Note You might need to choose Refresh to see the status Active.After activation, select the business rule. On the next screen, go to the Generated Rules tab to view the rules that were autmatically created. |  |  |

|  |
| --- |
| Note The rule generator cannot be used to generate rules for objects like CA_BUPA. The generated rules can also be viewed via the [Maintain ILM Policies and Rules](#unique_10) configuration app. |

### ILM Rules Overview Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you are displaying the rules related to various live and non-live policies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the Maintain ILM Policies and Rules configuration activity | Open Manage Your Solution (F1241). Then, go to Configure Your Solution. Enter filter criteria with Application Area as Application Platform and Infrastructure and Sub application Area as Retention Management. Open the configuration item Settings. You can see all the configuration steps listed on the right-hand side.Note You might need to set the country version first (see the button on the lower right side of the screen.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain ILM Policies and Rules.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Implementation ActivitiesFrom SAP Fiori Launchpad, navigate to Implementation Activities tile.Choose Implementation Activities > Change Hierarchy > SAP Reference IMG.Access the Maintain ILM Policies and Rules configuration step from the path SAP Customizing Implementation Guide > ABAP Platform > Application Server > Basis Services > Information Lifecycle Management > Retention Management.Note You might need to set the country version first (see the button on the lower right side of the screen. |  |  |
| 3 | Display the ILM Rules Overview screen for Live Policies | Enter the Policy Category.Enter the Audit Area.Enter the ILM Object (optional) and Run.In the next screen, click on ILM Rules Overview button.Enter the Maximum No. of Hits.Click on the Display button. | The detailed ILM Rules Overview Screen is displayed in the following format:Audit AreaILM ObjectPolicy NameRule No.Only the Live tab is displayed since the Include Non-Live Policies checkbox was not selected in the previous screen.The Fetch Next button is disabled if the number of rules to be displayed < Maximum No. of Hits in the previous screen.The Fetch Next button is disabled if the number of rules to be displayed = Maximum No. of Hits in the previous screen.The Fetch Next button is enabled if the number of rules to be displayed > Maximum No. of Hits in the previous screen.By clicking on the Fetch Next button, the next set of rules along with the previous ones are displayed on the screen. |  |
| 4 | Display the ILM Rules Overview screen for Non-Live Policies | Enter the Policy Category.Enter the Audit Area.Enter the ILM Object (optional) and Run.In the next screen, click on ILM Rules Overview button.Select the Include Non-Live Policies checkbox.Enter the Maximum No. of Hits.Click on Display. | The detailed ILM Rules Overview Screen is displayed in the following format:Audit AreaILM ObjectPolicy NameRule No.The Non-Live Policies tab is displayed in addition to the Live tab is displayed if rules exist for non-live policies.The Fetch Next button is disabled if the number of rules to be displayed < Maximum No. of Hits in the previous screen.The Fetch Next button is disabled if the number of rules to be displayed = Maximum No. of Hits in the previous screen.The Fetch Next button is enabled if the number of rules to be displayed > Maximum No. of Hits in the previous screen.By clicking on the Fetch Next button, the next set of rules along with the previous ones are displayed on the screen. |  |
| 5 | Expand Subtree Button | On the detailed overview screen, click on the Expand Subtree button. | The rules are displayed in a tree format in the following hierarchy:Audit AreaILM ObjectPolicy NameRule No. |  |
| 6 | Collapse Subtree Button | On the detailed overview screen, click on the Collapse Subtree button. | The tree collapses. |  |
| 7 | Export Rules to Excel | On the detailed overview screen, click on the Export Rules to Excel button.A popup window with the file name and extension type by default is displayed.Click on OK. | All the rules related to live policies or non-live policies, depending on which rules are displayed, get exported as a CVS file and downloaded to your local system. |  |

|  |
| --- |
| Note The modeling of Retention and Residence rules needs to be done by customers to meet their legal and personal requirements. |

### Manage Archiving Variants

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Manage Archiving Variants (F0627A) app. | The Manage Archiving Variants (F0627A) app is displayed. On the left side of the screen, the Archiving Objects list is displayed. On the right side of the screen, the default archiving object details are displayed.Note Archiving objects should be ILM enabled and be active/assigned to the Audit Area. Archiving objects that don't have variants are also displayed in the master list. |  |
| 3 | Select an Archiving Object | Select an archiving object from the master list. |  |  |
| 4 | Create a New Variant | To create a new variant, choose Add New Variant at the bottom of the screen.Maintain values for Variant Details and Selection Parameters.Note Depending on the settings of the archiving object, the Action field in the Variant Details section may have two different options:Archiving and Data DestructionData DestructionIf the archiving object has the Data Destruction option in the Action field, you can only schedule the data destruction job without archiving.Choose Save.After you have saved your changes, a success message is displayed.Choose the back arrow to exit the Add New Variant screen.Note Variant selection parameters vary from object to object. Selection parameters are changed based on the variant type (Write or Preprocessing). |  |  |
| 5 | View Existing and New variants | To view all existing and newly created variants, go to the All Variants tab.All variants that belong to the selected archiving object are displayed. |  |  |
| 6 | View the Details of a Variant | Choose a variant to view its details.Note On this screen, you can schedule archiving. To do so, choose Schedule archiving. Choose Monitor Archiving Jobs (F0510A) to go to the Monitor Archiving Jobs (F0510A). |  |  |
| 7 | Edit a Variant | Choose Edit.Make the necessary changes.Choose Save.Note Check if the changes that you have made are updated correctly after you have saved them.Choose the back arrow to exit the Edit Variant screen. |  |  |
| 8 | Schedule Archiving | To schedule archiving, choose Schedule Archiving.The Schedule Archiving dialog box is displayed.If you want to schedule preprocessing, select the Include preprocessing checkbox.Note This is only possible if the Preprocessing variant type has been assigned to the variant.Once selected, the Preprocessing Variant field is enabled and automatically populated.Choose Schedule.Note The archiving job runs every Friday at 10pm in the production system. |  |  |
| 9 | View the Scheduled Job | To view the scheduled job, choose Monitor Archiving Jobs (F0510A) to navigate to the Monitor Archiving Jobs (F0510A) app where you can view all archiving jobs.A confirmation dialog box is displayed. Choose OK to access the app.To view the scheduled job, go to the Scheduled tab. |  |  |
| 10 | View the History | Go back to the Manage Archiving Variants (F0627A) app and select an archiving object.Go to the Non-Empty Runs tab.Click on a variant bar in the graph. An information box is displayed.Choose More Details. |  |  |

### Monitor Archiving Jobs

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Monitor Archiving Jobs (F0510A) app. |  |  |
| 3 | Select an Archiving Object | Select an archiving object from the Archiving Objects list on the left side of the screen. |  |  |
| 4 | Delete a Job | On the Failed tab, select the jobs that you want to delete.Choose Delete on the lower right part of the screen. A dialog box is displayed. If you want to delete the job, choose OK. Otherwise, choose Cancel. |  |  |
| 5 | Check the Details of a Failed Job | On the Failed tab, select a job to check its details. | You have accessed the job details, job log, and the application log of the job. |  |
| 6 | Reschedule a Job | Choose Reschedule at the bottom of the screen to reschedule the job. The Reschedule Job dialog box is displayed.To reschedule the job, choose OK. Otherwise, choose Cancel.Note To directly delete the job, choose Delete. If you want to send an email with this log, choose Send Log.Choose the back arrow to go back to the Failed Jobs list. |  |  |
| 7 | Terminate a Scheduled Job | Go to the Scheduled tab.Choose a scheduled job from the list and choose Terminate at the bottom of the screen.To terminate the job, choose OK in the dialog box. Otherwise, choose Cancel.Note The technical jobs for archiving-run in production mode is triggered every Friday in the system.The test mode runs are triggered daily. Results are available the next day. |  |  |

### ILM Data Destruction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you're checking the process of ILM data destruction.

This application enables customers to display the expired archive files per ILM object and destruction objects and schedule the deletion.

|  |
| --- |
| Note The archive files created via archiving will be stored on SAP Business Technology Platform (SAP BTP). The storage job can be shown in the Monitor Archiving Jobs (F0510A) app. |

Prerequisite

There are archived files available that have reached the expiration date and the mandatory destruction date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the ILM Data Destruction (F2662) app. |  |  |
| 3 | Select an ILM Object | From the table Archive Files, select an ILM object from the list of ILM objects. | A list of expired resources is displayed indicating the Expiration Date and Mandatory Destruction Date. |  |
| 4 | Select an Archive File to Be Deleted | On the Resources tab, select one or more expired resources to be deleted. |  |  |
| 5 | Delete the Archive File | Choose Schedule at the top right of the list and confirm the deletion. |  |  |
| 6 | Check Deletion Jobs | After the scheduled job has run, check the Jobs tab to see if the job log of the deletion is displayed. The job is triggered by a technical job.Note The technical job runs every Saturday in the production system. |  |  |
| 7 | Run Using Destruction Objects | To delete the data, go back to the ILM Data Destruction (F2662) app and go to the Destruction Objects tab. |  |  |
| 8 | Schedule the Destruction | Go to the Not Scheduled tab, select one or more destruction objects, and choose Schedule at the top right of the list. Confirm the deletion. | The destruction job has been scheduled for the selected objects. |  |
| 9 | Check Scheduled Jobs | To see if the job scheduled for deletion is displayed, go to the Scheduled tab.Note The deletion jobs run every Saturday in the production system. Test-mode run is triggered everyday. |  |  |

### Manage ILM File Conversion

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to data privacy regulations such as GDPR, you should set the Information Lifecycle Management (ILM) rules on data objects for their archiving and destruction. If archive files that were created without ILM rules exist, or if you want to apply changed ILM rules to the archive files, you can recreate the archive files using the ILM File Conversion function.

You can schedule the ILM file conversion using Manage ILM File Conversion app. Specify the archiving objects and the time frame in the new scheduled run.

By default, the ILM conversion job is scheduled to run every Saturday in the production system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Data Privacy Specialist. |  |  |
| 2 | Access the App | Open the Manage ILM File Conversion (F5366) app. |  |  |
| 3 | Display Existing Conversion Run | Select the Go option. | A list of existing conversion runs are listed. |  |
| 4 | Schedule New Conversion Run | Select the Schedule option.Enter a Name.Select the Archiving Object from the value help list.Enter the Session From Date and Session To Date.Select the Schedule option. | A conversion run is created and displayed in the list page. |  |
| 5 | Check Logs of Schedule Conversion Run | After the scheduled job has run, select the conversion run to check the logs. Select the Archiving Object. Select the Application Log tab to check the application logs.The conversion job is triggered by a technical job. The technical job runs every Saturday in the production system. |  |  |

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
- related-to :: [[01-solution-foundation-and-platform/data-protection-and-privacy-data-controller-and-purpose-6n9-ae-1180]]
- related-to :: [[01-solution-foundation-and-platform/test-script-sap-s-4hana-cloud-public-edition-data-protection-and-priva]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1KA_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 52,518 chars in the whole document
