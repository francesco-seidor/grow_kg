---
id: 01-solution-foundation-and-platform/test-script-automated-provisioning-via-sap-cloud-identity-access-gover
title: "Test Script: Automated Provisioning via SAP Cloud Identity Access Governance (3AB) (3AB_S4CLD2608_BPD_EN_XX)"
description: "S/4HANA Cloud Public Edition test script for scope item 3AB: SuccessFactors HR events (hire, job change, termination) drive role provisioning via Cloud IAG."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/successfactors-employee-central-and-user-provisioning]
aliases: [3AB_S4CLD2608_BPD_EN_XX]
keywords: [SuccessFactors Employee Central Integration and User…, automated provisioning, access request approval, employee recruitment, employee job change, employee termination, global assignment, concurrent employment, international transfer, contingent worker]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3AB_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-920
topic: 01-solution-foundation-and-platform/successfactors-employee-central-and-user-provisioning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automated Provisioning via SAP Cloud Identity Access Governance (3AB) (3AB_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3AB_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **SuccessFactors Employee Central Integration and User Provisioning** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automated Provisioning via SAP Cloud Identity Access Governance (3AB) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232837846)

[2 Prerequisites 5](#_Toc232837847)

[2.1 Additional Manual Configuration 5](#_Toc232837848)

[2.2 System Access 5](#_Toc232837849)

[2.3 Roles 5](#_Toc232837850)

[2.4 Master Data, Organizational Data, and Other Data 7](#_Toc232837851)

[2.5 Preliminary Step 7](#_Toc232837852)

[2.5.1 Preliminiary Step 7](#_Toc232837853)

[3 Overview Table 8](#_Toc232837854)

[4 Test Procedures 12](#_Toc232837855)

[4.1 Employee Recruitment 12](#_Toc232837856)

[4.1.1 Hire New Employee 12](#_Toc232837857)

[4.1.2 View Employee Basic Data 14](#_Toc232837858)

[4.1.3 Schedule HR Triggers Job 15](#_Toc232837859)

[4.1.4 Access Request Validation and Approval 17](#_Toc232837860)

[4.1.5 Schedule Provisioning Job 18](#_Toc232837861)

[4.1.6 Employee Recruitment Validation 19](#_Toc232837862)

[4.2 Employee Recruitment (JB1 as Prerequisite) 20](#_Toc232837863)

[4.2.1 Hire New Employee 20](#_Toc232837864)

[4.2.2 View Employee Basic Data 22](#_Toc232837865)

[4.2.3 Initialize Employee’s Job Information 24](#_Toc232837866)

[4.2.4 Workflow Request Approval (Optional) 25](#_Toc232837867)

[4.2.5 Schedule HR Triggers Job 26](#_Toc232837868)

[4.2.6 Access Request Validation and Approval 28](#_Toc232837869)

[4.2.7 Schedule Provisioning Job 29](#_Toc232837870)

[4.2.8 Business Role Validation 30](#_Toc232837871)

[4.3 Employee Jobs Change 31](#_Toc232837872)

[4.3.1 Change Employee's Job 31](#_Toc232837873)

[4.3.2 Workflow Request Approval (Optional) 32](#_Toc232837874)

[4.3.3 Schedule HR Triggers Job 33](#_Toc232837875)

[4.3.4 Access Request Validation and Approval 35](#_Toc232837876)

[4.3.5 Schedule Provisioning Job 37](#_Toc232837877)

[4.3.6 Employee Status Change Validation 38](#_Toc232837878)

[4.4 Global Assignment 39](#_Toc232837879)

[4.4.1 Start Global Assignment 39](#_Toc232837880)

[4.4.2 End Global Assignment 40](#_Toc232837881)

[4.5 Concurrent Employment 41](#_Toc232837882)

[4.5.1 Start Concurrent Employment 41](#_Toc232837883)

[4.5.2 End Concurrent Employment 42](#_Toc232837884)

[4.6 International Transfer 44](#_Toc232837885)

[4.6.1 Terminate Old Employment 44](#_Toc232837886)

[4.6.2 Rehire with New Employment 45](#_Toc232837887)

[4.7 Employee Termination 47](#_Toc232837888)

[4.7.1 Terminate Employee 47](#_Toc232837889)

[4.7.2 Workflow Request Approval (Optional) 48](#_Toc232837890)

[4.7.3 Schedule HR Triggers Job 49](#_Toc232837891)

[4.7.4 Access Request Validation and Approval 50](#_Toc232837892)

[4.7.5 Schedule Provisioning Job 51](#_Toc232837893)

[4.7.6 Employee Termination Validation 52](#_Toc232837894)

[4.8 Contingent Worker 53](#_Toc232837895)

[4.8.1 Hire Contingent Worker 53](#_Toc232837896)

[4.8.2 End Contingent Worker 55](#_Toc232837897)

## Purpose

Overview

You can achieve automated provisioning in SAP S/4HANA Cloud Public Edition based on employee events in SAP SuccessFactors. SAP Cloud Identity Access Governance performs the provisioning and supports compliance activities with automated routing of actions for approval. You can maintain rules to determine the roles to be provisioned.

The following table listed the use cases supported in this test script.

| Use Case | Sub Use Case | Event in SuccessFactors | Event Reason | Test script chapter | Expected result in S4 HANA |
| --- | --- | --- | --- | --- | --- |
| Hire employee |  | Hire | New Hire | Employee Recruitment | Business users created and business roles assigned |
| Employment change | Job change | TransferData ChangeJob ReclassificationPosition ChangePromotion/Demotion | Cost Center ChangeData changeJob ReclassificationPosition ChangePromotion/Demotion | Employee Jobs Change | Old business roles removed and new business roles added. |
|  | Start Global Assignment | Away on Global AssignmentAdd Global Assignment | Add Global AssignmentAway on Global Assignment | [Start Global Assignment](#unique_2) [page ] 39 | New business roles added. |
|  | End Global Assignment | End Global AssignmentBack from Global Assignment | End Global AssignmentBack from Global Assignment | [End Global Assignment](#unique_3) [page ] 40 | Old business roles removed. |
|  | Start Concurrent Employment | Hire | Concurrent Hire | [Start Concurrent Employment](#unique_4) [page ] 41 | New business roles added. |
|  | End Concurrent Employment | Termination | End of Contract | [End Concurrent Employment](#unique_5) [page ] 42 | Old business roles removed. |
| International transfer | Terminate old employment | Termination | International transfer | [Terminate Old Employment](#unique_6) [page ] 44 | Business user deleted. |
|  | Rehire with new employment | Hire | International transfer | [Rehire with New Employment](#unique_7) [page ] 45 | Business users created and business roles assigned |
| Terminate employee |  | Termination | Early/Normal RetirementDismissalSelf-Termination | Employee Termination | Business user deleted. |
| Contingent worker management | Hire contingent worker | Start Contingent Worker | Start Contingent Worker | [Hire Contingent Worker](#unique_8) [page ] 53 | Business users created and business roles assigned |
|  | End contingent worker | End Contingent Worker | End Contingent Worker | [End Contingent Worker](#unique_9) [page ] 55 | Business user deleted. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c76b6ef4f272558297f0494ef67827e2)

### System Access

| System | Details |
| --- | --- |
| SAP SuccessFactors Employee Central | Accessible via SAP SuccessFactors Employee Central web-based portal. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Cloud Identity Access Governance | Accessible via SAP Cloud Identity Access Governance web-based launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

In SAP S/4 HANA Cloud:

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Administrator - HR Info | SAP_BR_ADMINISTRATOR_HRINFO | Administration - HR Info | SAP_BR_ADMINISTRATOR_HRINFO |  |

In SAP Cloud Identity Access Governance:

| Business User | Name | Log On |
| --- | --- | --- |
| Administrator | As defined under role-based permission in SAP Cloud SAP Cloud Identity Access Governance |  |
| Manager | The employee's manager maintained in SAP SuccessFactors Employee Central and captured by SAP Cloud Identity Access Governance; for testing purpose, use the admin role. |  |
| Role Owner | The business role's owner maintained in SAP Cloud SAP Cloud Identity Access Governance; for testing purpose, use the admin role. |  |
| Security Officer | As defined under role-based permission in SAP Cloud SAP Cloud Identity Access Governance; for testing purpose, use the admin role. |  |

In SAP SuccessFactors Employee Central:

| Business User | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Administrator | As defined under role-based permission in SAP SuccessFactors Employee Central | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| HR Manager | As defined under role-based permission in SAP SuccessFactors Employee Central; for testing purpose, use the Admin role. |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| SAP S/4HANA: <company code> | 1710 | Company code: US | SAP SuccessFactors Employee Central: <value is mapped to legal entity ID>. |
| SAP S/4HANA: <company code> | 1010 | Company code: DE | SAP SuccessFactors Employee Central: <value is mapped to legal entity ID>. |

### Preliminary Step

#### Preliminiary Step

Before proceeding step: Hire New Employee, make sure that you've set up the integration between SAP SuccessFactors Employee Central and SAP S/4HANA Cloud Public Edition via [Workforce Person Replication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/8d2cbcdb056e4461b313fbcb68160896.html?locale=en-US&version=2308.500) or [Conversion from Scope Item JB1 to an SAP Master Data Integration between SAP S/4HANA Cloud Public Edition and SAP SuccessFactors Employee Central](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/22cc1179951c4bd7a9fe539aaed552d5.html?locale=en-US&version=2308.500).

## Overview Table

The Automated Provisioning via SAP Cloud Identity Access Governance (3AB) scope item consists of several process steps provided in the table below.

Employee Recruitment

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Hire New Employee](#unique_17) [page ] 12 | SFEC/HR Manager | Add New Employee | New employee is added successfully. |
| [View Employee Basic Data](#unique_18) [page ] 14 | Administrator | Manage Workforce | New employee is created successfully. |
| [Schedule HR Triggers Job](#unique_19) [page ] 15 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | HR triggers job is scheduled and access request is created. |
| [Access Request Validation and Approval](#unique_20) [page ] 17 | SAP Cloud Identity Access Governance/Manager, Role Owner, Security Officer | Access Request Inbox | Access Request is validated and approved. |
| [Schedule Provisioning Job](#unique_21) [page ] 18 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | Provisioning Job is scheduled. |
| [Employee Recruitment Validation](#unique_22) [page ] 19 | S/4HANA Cloud/Administrator | Maintain Business Users (F1303) | Business User is created and business role(s) is assigned correctly. |

Employee Recruitment (JB1 as Prerequisite)

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Hire New Employee](#unique_23) [page ] 20 | SFEC/HR Manager | Add New Employee | New employee is added successfully. |
| [View Employee Basic Data](#unique_24) [page ] 22 | S/4HANA Cloud/Administrator | Maintain Business Users (F1303) | New business user is created successfully. |
| [Initialize Employee’s Job Information](#unique_25) [page ] 24 | SFEC/HR Manager | Employee Files | Job Information is initialized successfully. |
| [Workflow Request Approval (Optional)](#unique_26) [page ] 25 | SFEC/Administrator | Manage Workflow Request | Employee’s data change request is approved. |
| [Schedule HR Triggers Job](#unique_27) [page ] 26 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | HR triggers job is scheduled and access request is created. |
| [Access Request Validation and Approval](#unique_28) [page ] 28 | SAP Cloud Identity Access Governance/Manager, Role Owner, Security Officer | Access Request Inbox | Access Request is validated and approved. |
| [Schedule Provisioning Job](#unique_29) [page ] 29 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | Provisioning Job is scheduled. |
| [Business Role Validation](#unique_30) [page ] 30 | S/4HANA Cloud/Administrator | Maintain Business Users (F1303) | Business role(s) is assigned correctly. |

Employee Jobs Change

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Change Employee's Job](#unique_31) [page ] 31 | SFEC/HR Manager | Employee Files | Job Information is updated successfully. |
| [Workflow Request Approval (Optional)](#unique_32) [page ] 32 | SFEC/Administrator | Manage Workflow Request | Employee’s data change request is approved. |
| [Schedule HR Triggers Job](#unique_33) [page ] 33 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | HR triggers job is scheduled and access request is created. |
| [Access Request Validation and Approval](#unique_34) [page ] 35 | SAP Cloud Identity Access Governance/Manager, Role Owner, Security Officer | Access Request Inbox | Access Request is validated and approved. |
| [Schedule Provisioning Job](#unique_35) [page ] 37 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | Provisioning Job is scheduled. |
| [Employee Status Change Validation](#unique_36) [page ] 38 | S/4HANA Cloud/Administrator | Maintain Business Users (F1303) | Business role(s) is changed correctly. |

Global Assignment

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Start Global Assignment](#unique_2) [page ] 39 | SFEC/HR Manager | Employee Files | Global assignment is added. |
| [End Global Assignment](#unique_3) [page ] 40 | SFEC/HR Manager | Employee Files | Global assignment is terminated. |

Concurrent Employment

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Start Concurrent Employment](#unique_4) [page ] 41 | SFEC/HR Manager | Employee Files | Concurrent employment is added. |
| [End Concurrent Employment](#unique_5) [page ] 42 | SFEC/HR Manager | Employee Files | Concurrent employment is terminated. |

International Transfer

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Terminate Old Employment](#unique_6) [page ] 44 | SFEC/HR Manager | Employee Files | Current employment is terminated. |
| [Rehire with New Employment](#unique_7) [page ] 45 | SFEC/HR Manager | Rehire Inactive Employee | Employee is rehired. |

Employee Termination

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Terminate Employee](#unique_37) [page ] 47 | SFEC/HR Manager | Employee Files | Employee is terminated successfully. |
| [Workflow Request Approval (Optional)](#unique_38) [page ] 48 | SFEC/Administrator | Manage Workflow Request | Employee’s data change request is approved. |
| [Schedule HR Triggers Job](#unique_39) [page ] 49 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | HR triggers job is scheduled and access request is created. |
| [Access Request Validation and Approval](#unique_40) [page ] 50 | SAP Cloud Identity Access Governance/Security Officer | Access Request Inbox | Access Request is validated and approved. |
| [Schedule Provisioning Job](#unique_41) [page ] 51 | SAP Cloud Identity Access Governance/Administrator | Job Scheduler | Deprovisioning Job is scheduled. |
| [Employee Termination Validation](#unique_42) [page ] 52 | S/4HANA Cloud/Administrator | Maintain Business Users (F1303) | Business User is not listed. |

Contingent Worker

| Process Step | System/Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Hire Contingent Worker](#unique_8) [page ] 53 | SFEC/HR Manager | Add Contingent Worker | Contingent worker is added. |
| [End Contingent Worker](#unique_9) [page ] 55 | SFEC/HR Manager | Employee Files | Contingent worker is terminated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Employee Recruitment

#### Hire New Employee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR manager enters hiring data for a newly hired employee. This new hire event will trigger Business Partner and Employee creation automatically on SAP S/4HANA Cloud Public Edition with the help of [Workforce Person Replication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/8d2cbcdb056e4461b313fbcb68160896.html).

Prerequisite

Before you start hiring a new employee, make sure the setup guide of this scope item has been followed through to ensure working connectivity between SuccessFactors, SAP Cloud Identity Access Governance and SAP S/4HANA Cloud Public Edition. What’s more, make sure the Preliminiary Step > [Workforce Person Replication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/8d2cbcdb056e4461b313fbcb68160896.html) is proceeded successfully and Employee can be synchronized correctly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SuccessFactors System | Log on to SuccessFactors Employee Central as HR manager. |  |  |
| 2 | Admin Center | From the Home dropdown, choose Admin Center. | SuccessFactors Admin Center page is displayed. |  |
| 3 | Add New Employee | In the Manage Employees portlet of the Admin Center screen, choose Update User Information > Add New Employee.Note The following example fields to be filled are just mandatory for fields mapping in SAP Cloud Identity Access Governance. You may need to type in additional information based on your SuccessFactors' setting. | Add New Employee page is displayed. |  |
| 4 | Enter Identity Information for New Employee | In the Identity section, make the following entries:Hire Date: <yesterday's date>Company: <Company USA (1710)>Event Reason: <New Hire(HIRNEW)>Name Information section:First Name: <Frank>Last Name: <Ford>Biographical Information section:Date Of Birth: <select from calendar help>Person ID: <FRANKFORD>Note Person Id is an external field, which is used to identify the employee in both SAP Cloud Identity Access Governance and SAP S/4HANA Cloud Public Edition.Choose Continue. | The Personal Information section in the Add New Employee screen is expanded. |  |
| 5 | Enter Personal Information for New Employee | In the Personal Information section, make the following entries:Country/Region: <leave the defaulted value>In the Email Information section, select the (+) Add link. The editable fields show up and you can enter the following information:Email Type: select Business.Email Address: <enter as appropriate>Note For testing purposes, we recommend that you add your own valid email address, in order to receive an email from the system with the log on data to the SAP SuccessFactors Employee Central instance.Is Primary: select Yes.Choose Continue. | The Job Information section in the Add New Employee screen is expanded. |  |
| 6 | Enter Job Information for New Employee | In the Organizational Information section, make the following entries:Company: <leave the defaulted value>Business Unit: <select as appropriate>Cost Center: <select from dropdown list>Caution The Cost Center field must be filled, or the sync of Business Partner and Employee to SAP S/4HANA Cloud Public Edition will be failed! It will be required in order to staff the employee on a project in SAP S/4HANA Cloud Public Edition. It is also needed by the employee for recording times in timesheet, especially for non-project related tasks.In the Job Information section, make the following entries:Supervisor: <enter as appropriate>Note In case of the first employee in the instance, select No Manager.Job Classification: <select as appropriate>Employee Class: select Employee from dropdown.Employment Type: <select as appropriate>Choose Submit on the bottom right of page.Choose Confirm on the dialog box. | The new employee is added successfully. |  |

#### View Employee Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Administrator - HR Info views the basic data of the employee as replicated from SAP SuccessFactors Employee Central. This replication is realized by [Workforce Person Replication](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/8d2cbcdb056e4461b313fbcb68160896.html?locale=en-US&version=2308.500). The existence of employee in S/4HANA Cloud is indispensable for the following process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Go to the Manage Workforce | Open the Manage Service Level Agreements (F6183A)app. |  |  |
| 3 | Search for Employee | In the search field, enter the Person Id you created in SuccessFactors.Choose Go. |  |  |
| 4 | Verify Employee | On the Search Results screen, choose the employee and check the data.Note The employee replication job is executed periodically based on the setting. If there is no result, please wait until the background job finish. | The employee is replicated to S/4HANA system. |  |

#### Schedule HR Triggers Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Schedule HR Triggers Job on SAP Cloud Identity Access Governance to capture the HR event and create an access request.

Prerequisite

Before you start the test procedures, make sure that the new employee is hired successfully in SuccessFactors Employee Central .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as an Administrator. |  |  |
| 2 | Schedule HR Triggers Job | Choose Job Scheduler in the Administration section.In the Job Name field, enter <HR_Triggers_Job_1>.From the Job Category dropdown list, select HR Triggers.Choose Schedule Job.Note You can choose Yes to start job immediately or choose No to schedule a job weekly, daily, hourly or by “X” minutes. "X" is recommended to be more than 20 minutes. | HR Triggers Job is scheduled. |  |
| 3 | Validate Scheduled HR Triggers Job in Job History List | Validate the HR Triggers Job scheduled in step 2 in Job History List. | You should see a log message to indicate that the request was created. |  |
| 4 | Failure Job’s Analysis (Optional) | If the message in job history list shows that 0 request(s) created, the reason could be as follows,no business rules are defined,there are application issues,no access is associated for the event. |  |  |
| 5 | Resolve the Issue (Optional) | Contact your IT support to find out the root cause and fix the issue. |  |  |
| 6 | Reprocess Missing HR Events (Optional) | Navigate to Reports section and open Reprocess Missed HR Events tile.Search for user in the above failure job by entering the value in the Filter Option.Select the right record by clicking the available Checkbox. Then click on Retry button.Reschedule the HR Triggers Job in Job Scheduler tile. | Access request should be created successfully. |  |

#### Access Request Validation and Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as different roles and approve the access request, which would be the prerequisites of the role provisioning in SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure that the HR Triggers Job is scheduled successfully and that the access request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Manager. |  |  |
| 2 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_19) [page ] 15 step under Requests list, click on it and then go to the Approve Requests page.Note If Access Analysis Service is active, SoD risk or Critical Access risk may be detected in new access request or in the existing access. You could reject the access request with risks or remediate the risks.For risk remediation purpose, click on Remediate Risks and navigate to Risks section.For each Risk line, select the Mitigation Control Master Data from the Assignment of Control list. Select Monitor Group from the Monitor Group list. Select Validity from the Validity Period form.Choose the Simulate button to simulate your risk remediation action.Choose the Confirm button.Note Request Delegation for a time period can be configured. Choose Configuration in the Administrator section. Click Request Delegation(Admin) and you can create the approver delegates within a period of time. | On Access Requested lines, the value of action column for relevant system request should be Add. |  |
| 3 | Approve or Reject Request | Find the request lines of relevant system in the Access Requested section and choose the Approve button.Choose the Submit button. | Assess Request of relevant system is approved by Manager. |  |
| 4 | Log On | Log on to the SAP Cloud Identity Access Governance System as Role Owner. |  |  |
| 5 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_19) [page ] 15 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 6 | Role Owner Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Role Owner. |  |
| 7 | Log On | Log on to the SAP Cloud Identity Access Governance System as Security Officer. |  |  |
| 8 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_19) [page ] 15 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 9 | Security Officer Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Security Officer. |  |

#### Schedule Provisioning Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as Administrator and schedule the provisioning job to SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure the access request is approved by all the relevant roles and is ready to be provisioned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Administrator. |  |  |
| 2 | Schedule Provisioning Job | Choose Job Scheduler in the Administrator section.In the Job Name field, enter <S4_Prov_1>.Select Provisioning from the Job Category dropdown list.Choose Schedule Job. | Provisioning Job is scheduled. |  |
| 3 | Validate Provisioning Job in Job History List | Validate the Provisioning Job scheduled in the previous step in Job History List. | There should be several lines of log information such as Role "SAP_XX_XXX_XXXXXX" assigned to user "Frank-Ford (Frank Ford)": Provisioned (Successful). in the detailed page of Job under Job History List. |  |

#### Employee Recruitment Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP S/4HANA Cloud Public Edition as Administrator and validate the business user is created and business role(s) is assigned correctly.

Prerequisites

Before you start the test procedure, make sure the provisioning job is successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition System as an Administrator. |  |  |
| 2 | Validate Provisioning Result - Business User Creation | Choose Maintain Business Users (F1303).In the User Name field, enter <Frank Ford> as mentioned in preliminary steps and choose Go. | Frank Ford is listed in the Business Users section. |  |
| 3 | Validate Provisioning Result - Business Role Assignment | Click the user and drill down to the detailed page. Validate the synchronized roles under Assigned Business Roles. | Relevant business role(s) is assigned to the new created business user. |  |

### Employee Recruitment (JB1 as Prerequisite)

#### Hire New Employee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The HR manager enters hiring data for a newly hired employee.

Prerequisite

Before you start hiring a new employee, make sure the setup guide of this scope item has been followed through to ensure working connectivity between SuccessFactors, SAP Cloud Identity Access Governance and SAP S/4HANA Cloud Public Edition. What’s more, make sure the prerequisite scope item JB1 is activated successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SuccessFactors System | Log on to SuccessFactors Employee Central as HR manager. |  |  |
| 2 | Admin Center | From the Home dropdown, choose Admin Center. | SuccessFactors Admin Center page is displayed. |  |
| 3 | Add New Employee | In the Manage Employees portlet of the Admin Center screen, choose Update User Information > Add New Employee.Note The following example fields to be filled are just mandatory for fields mapping in SAP Cloud Identity Access Governance. You may need to type in additional information based on your SuccessFactors' setting. | Add New Employee page is displayed. |  |
| 4 | Enter Identity Information for New Employee | In the Identity section, make the following entries:Hire Date: <yesterday's date>Company: <Company USA (1710)>Event Reason: <New Hire(HIRNEW)>Name Information section:First Name: <Frank>Last Name: <Ford>Biographical Information section:Date Of Birth: <select from calendar help>Person ID: <FRANKFORD>Note Person Id is an external field, which is used to identify the employee in both SAP Cloud Identity Access Governance and SAP S/4HANA Cloud Public Edition.User Name: <FRANKFORD>Choose Continue. | The Personal Information section in the Add New Employee screen is expanded. |  |
| 5 | Enter Personal Information for New Employee | In the Personal Information section, make the following entries:Country/Region: <leave the defaulted value>In the Email Information section, select the (+) Add link. The editable fields show up and you can enter the following information:Email Type: select Business.Email Address: <enter as appropriate>Is Primary: select Yes.Choose Continue. | The Job Information section in the Add New Employee screen is expanded. |  |
| 6 | Enter Job Information for New Employee | In the Organizational Information section, make the following entries:Company: <leave the defaulted value>Business Unit: <keep as blank for the following fill in>Cost Center: <select from dropdown list>In the Job Information section, make the following entries:Supervisor: <enter as appropriate>Note In case of the first employee in the instance, select No Manager.Job Classification: <select as appropriate>Choose Submit on the bottom right of page.Choose Confirm on the dialog box. | The new employee is added successfully. |  |

#### View Employee Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This new hire event will trigger Business Partner, Employee and Business User creation automatically in SAP S/4HANA Cloud Public Edition with the help of scope item JB1 - Exception-Based Core HR with SAP SuccessFactors Employee Central. The Administrator views the basic data of the employee as replicated from SAP SuccessFactors Employee Central.

|  |
| --- |
| Note For the employee replication, you can do it via Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1) or using the Manage Workforce (F6097A) Fiori App with template as mentioned below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. |  |  |
| 2 | Validate Employee Replication by JB1 | Choose Maintain Business Users (F1303)In the User Name field, search for the newly added employee <Frank Ford> in SuccessFactor and choose Go. | Frank Ford is listed in the Business Users section. There is no business role assigned.Note If there is no user data, please turn to check whether JB1 is activated.If JB1 is not configured, continue the next steps. Otherwise, skip step 3 and continue from step 4. |  |
| 3 | Import Employee on SAP S/4HANA Cloud Public Edition with Template (Optional) | Choose Manage Workforce (F6097A) in Workforce Master Data section.Choose Import > CSV > Worker and Work Agreement (Basic Import) .Select the delimiter.Click on Download Templates link to download the import template.Edit the following content in the template:WorkerID & UserName should be the same value as that you maintain in SuccessFactor, eg. FRANKFORDFirstName & LastName should be the same value as that you maintain in SuccessFactor.Company Code: <1710>Cost Center: <Fill in the same as maintain in SuccessFactor>StartDate: <The New Hire date in SuccessFactor>Choose Browse and then select the CSV file you filled in. Enter a name in the Import Name field and choose Import. | Job Scheduling should be successful and Business User can be find out with Maintain Business Users Fiori tile. |  |
| 4 | Log On SAP Cloud SAP Cloud Identity Access Governance System | Log on to the SAP Cloud Identity Access Governance System as an Administrator. |  |  |
| 5 | Schedule Repository Sync Job in SAP Cloud Identity Access Governance | Choose Job Scheduler on the Administration section and make the following entries:Job Name: <S4_Repo_Sync>Job Category: Repository SyncSystem Type: SAP S/4HANA Cloud Public EditionSystem: <SAP S/4HANA Cloud Public Edition system name>Select the Delta Sync checkbox.Choose Schedule Job. | Job Scheduling should be successful. After several minutes, the information that Job S4_Repo_Sync is finished could be seen in Job History tile. |  |

#### Initialize Employee’s Job Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Update Employee’s Organization Information for the initial business role assignment in SAP S/4HANA Cloud Public Edition. This role assignment will act as a simple onboarding process for the new employee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile view is displayed. |  |
| 3 | Update Job Information of Employee | Go to Position Information section, choose Edit.Click on When would you like your changes to take effect?.Select <today's date> from the date choose form.Make the following entries:Event: <Data Change>Event Reason: <Data Change (DATACHG)>Business Unit: <select as appropriate>Choose Save. | Employee’s Business Unit is initialized. |  |

#### Workflow Request Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is required only in the case that Approval Workflow is enabled in SuccessFactors System. Based on your setting, the employee’s data change request should be approved by the manager or other people first in SuccessFactors, then the HR event can be active and be captured by SAP Cloud Identity Access Governance system.

For testing purpose, proxy tool is used in the steps to save your time. Normally, you need to change the logon user to the specific role to approve the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central as Administrator. |  |  |
| 2 | Search Workflow Request and Proxy Approver | Search Manage Workflow Requests in search field at the right top of the Home page.In the Search Workflow Requests form, make the following entry and choose Search:Effective Date From: <Today>Effective Date To: <Today> |  |  |
| 3 | Update Workflow Approved User | Find the request record line. Then click the Actions button and choose Change Approvers.In the Update to field, copy <person's name> and close the dialog box.Choose Proxy Now in user profile dropdown list on top of the page.Paste the copied <person's name> in the dialog and wait for the automatic name matching. Then choose the provided name from drop down list.Choose OK. | Workflow Approved User is updated.The user’s role is changed to the target person who can approve the change request. |  |
| 4 | Search Workflow Request | Select Approve Requests section, find the status change request. | The Approve Requests view is displayed. |  |
| 5 | Approve Employee Status Change Request | On Approve Requests dialog box, choose Approve of request.Choose Become Self in user profile dropdown list on top of the view to go back to the Admin user. | Employee Status Change request is approved. |  |

#### Schedule HR Triggers Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Schedule HR Triggers Job on SAP Cloud Identity Access Governance to capture the HR event and create an access request.

Prerequisite

Before you start the test procedures, make sure the employee’s organizational information is initialized successfully in SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as an Administrator. |  |  |
| 2 | Schedule HR Triggers Job | Choose Job Scheduler in the Administration section.In the Job Name field, enter <HR_Triggers_Job_1>.From the Job Category dropdown list, select HR Triggers.Choose Schedule Job.Note You can choose Yes to start job immediately or choose No to schedule a job weekly, daily, hourly or by “X” minutes. "X" is recommended to be more than 20 minutes. | HR Triggers Job is scheduled. |  |
| 3 | Validate Scheduled HR Triggers Job in Job History List | Validate the HR Triggers Job scheduled in step 2 in Job History List. | You should see a log message to indicate that the request was created. |  |
| 4 | Failure Job’s Analysis (Optional) | If the message in job history list shows that 0 request(s) created, the reason could be as follows,no business rules are defined,there are application issues,no access is associated for the event. |  |  |
| 5 | Resolve the Issue (Optional) | Contact your IT support to find out the root cause and fix the issue. |  |  |
| 6 | Reprocess Missing HR Events (Optional) | Navigate to Reports section and open Reprocess Missed HR Events tile.Search for user in the above failure job by entering the value in the Filter Option.Select the right record by clicking the available Checkbox. Then click on Retry button.Reschedule the HR Triggers Job in Job Scheduler tile. | Access request should be created successfully. |  |

#### Access Request Validation and Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as different roles and approve the access request, which would be the prerequisites of the role provisioning in SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure that the HR Triggers Job is scheduled successfully and that the access request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Manager. |  |  |
| 2 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_27) [page ] 26 step under Requests list, click on it and then go to the Approve Requests page.Note If Access Analysis Service is active, SoD risk or Critical Access risk may be detected in new access request or in the existing access. You could reject the access request with risks or remediate the risks.For risk remediation purpose, click on Remediate Risks, choose the step under Simulate button, select the Mitigation Control Master Data from the Assignment of Control list.Select Monitor Group from the Monitor Group step under list and select Validity from the Validity Period form for each Risk line.Choose the Confirm button.Note Request Delegation for a time period can be configured. Choose Configuration in the Administrator section. Click Request Delegation(Admin) and you can create the approver delegates within a period of time. | On Access Requested lines, the value of action column for relevant system request should be Add. |  |
| 3 | Approve or Reject Request | Find the request lines of relevant system in the Access Requested section and choose the Approve button.Choose the Submit button. | Assess Request of relevant system is approved by Manager. |  |
| 4 | Log On | Log on to the SAP Cloud Identity Access Governance System as Role Owner. |  |  |
| 5 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_27) [page ] 26 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 6 | Role Owner Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Role Owner. |  |
| 7 | Log On | Log on to the SAP Cloud Identity Access Governance System as Security Officer. |  |  |
| 8 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_27) [page ] 26 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 9 | Security Officer Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Security Officer. |  |

#### Schedule Provisioning Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as Administrator and schedule the provisioning job to SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure the access request is approved by all the relevant roles and is ready to be provisioned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Administrator. |  |  |
| 2 | Schedule Provisioning Job | Choose Job Scheduler in the Administrator section.In the Job Name field, enter <S4_Prov_1>.Select Provisioning from the Job Category dropdown list.Choose Schedule Job. | Provisioning Job is scheduled. |  |
| 3 | Validate Provisioning Job in Job History List | Validate the Provisioning Job scheduled in the previous step in Job History List. | There should be several lines of log information such as Role "SAP_XX_XXX_XXXXXX" assigned to user "Frank-Ford (Frank Ford)": Provisioned (Successful). in the detailed page of Job under Job History List. |  |

#### Business Role Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP S/4HANA Cloud Public Edition as Administrator and validate the business role(s) is assigned correctly.

Prerequisites

Before you start the test procedure, make sure the provisioning job is successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition System as an Administrator. |  |  |
| 2 | Validate Provisioning Result - Business User Creation | Choose Maintain Business Users (F1303).In the User Name field, enter <Frank Ford> as mentioned in preliminary steps and choose Go. | Frank Ford is listed in the Business Users section. |  |
| 3 | Validate Provisioning Result - Business Role Assignment | Click the user and drill down to the detailed page. Validate the synchronized roles under Assigned Business Roles. | Relevant business role(s) is assigned to the new created business user. |  |

### Employee Jobs Change

#### Change Employee's Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Change employee's job inoformation in SuccessFactors Employee Central. This would be the prerequisite of the provision and deprovision from SAP Cloud Identity Access Governance to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile view is displayed. |  |
| 3 | Update Job Information of Employee | Go to Position Information section, choose Edit.Click on When would you like your changes to take effect?.Select <today's date> from the date choose form.Make the following entries:Event: <Transfer>Event Reason: <Cost Center Change (DATACOST)>Note If Event Reason Derivation Business Rules is enabled, Event and Event Reason fields should be invisible and there is no need to maintain them. The system automatically selects the appropriate event reason based on your changes.Business Unit: <select a different one>Cost Center: <Select as appropriate>Choose Save. | Employee’s Business Unit is changed. |  |

#### Workflow Request Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is required only in the case that Approval Workflow is enabled in SuccessFactors System. Based on your setting, the employee status change request should be approved by the manager or other people first in SuccessFactors, then the HR event can be active and be captured by SAP Cloud Identity Access Governance system.

For testing purpose, proxy tool is used in the steps to save your time. Normally, you need to change the logon user to the specific role to approve the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central as Administrator. |  |  |
| 2 | Search Workflow Request and Proxy Approver | Search Manage Workflow Requests in search field at the right top of the Home page.In the Search Workflow Requests form, make the following entry and choose Search:Effective Date From: <Today>Effective Date To: <Today> |  |  |
| 3 | Update Workflow Approved User | Find the request record line. Then click the Actions button and choose Change Approvers.In the Update to field, copy <person's name> and close the dialog box.Choose Proxy Now in user profile dropdown list on top of the page.Paste the copied<person's name> in the dialog and wait for the automatic name matching. Then choose the provided name from drop down list.Choose OK. | Workflow Approved User is updated.The user’s role is changed to the target person who can approve the change request. |  |
| 4 | Search Workflow Request | Select Approve Requests tile, find the status change request. | The Approve Requests view is displayed. |  |
| 5 | Approve Employee Status Change Request | On Approve Requests dialog box, choose Approve of request.Choose Become Self in user profile dropdown list on top of the view to go back to the Admin user. | Employee Status Change request is approved. |  |

#### Schedule HR Triggers Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Schedule HR Triggers Job on SAP Cloud Identity Access Governance to capture the HR event and create an access request.

Prerequisites

Before you start the test procedures, make sure the employee’s business unit is changed successfully in SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as an Administrator. |  |  |
| 2 | Schedule HR Triggers Job | Choose Job Scheduler in the Administration section.In the Job Name field, enter <HR_Triggers_Job_2>.From the Job Category dropdown list, select HR Triggers.Choose Schedule Job.Note You can choose Yes to start job immediately or choose No to schedule a job weekly, daily, hourly or by “X” minutes. "X" is recommended to be more than 20 minutes. | HR Triggers Job is scheduled. |  |
| 3 | Validate Scheduled HR Triggers Job in Job History List | Validate the HR Triggers Job scheduled in step 2 in Job History List. | You should see a log message to indicate that the request was created. |  |
| 4 | Failure Job’s Analysis (Optional) | If the message in job history list shows that 0 request(s) created, the reason could be as follows,no business rules are defined,there are application issues,no access is associated for the event. |  |  |
| 5 | Resolve the Issue (Optional) | Contact your IT support to find out the root cause and fix the issue. |  |  |
| 6 | Reprocess Missing HR Events (Optional) | Navigate to Reports section and open Reprocess Missed HR Events tile.Search for user in the above failure job by entering the value in the Filter Option.Select the right record by clicking the available Checkbox. Then click on Retry button.Reschedule the HR Triggers Job in Job Scheduler tile. | Access request should be created successfully. |  |

#### Access Request Validation and Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as different roles and approve the access request, which would be the prerequisite of the role provisioning and deprovisioning in SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure the HR Triggers Job is scheduled successfully and the access request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Manager. |  |  |
| 2 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_33) [page ] 33 step under Requests list, click on it and then go to the Approve Requests page.Note If Access Analysis Service is active, SoD risk or Critical Access risk may be detected in new access request or in the existing access. You could reject the access request with risks or remediate the risks.For risk remediation purpose, click on Remediate Risks, choose the step under Simulate button, select the Mitigation Control Master Data from the Assignment of Control list.Select Monitor Group from the Monitor Group step under list and select Validity from the Validity Period form for each Risk line.Choose the Confirm button.Note Request Delegation for a time period can be configured. Choose Configuration in the Administrator section. Click Request Delegation(Admin) and you can create the approver delegates within a period of time. | On Access Requested lines, the value of action column for relevant system request should be Add and Remove. |  |
| 3 | Approve and Reject Request Lines | Find the request lines of relevant system in the Access Requested section and choose the Approve button.Choose the Submit button. | Assess Request of relevant system is approved by Manager. |  |
| 4 | Log On | Log on to the SAP Cloud Identity Access Governance System as Role Owner. |  |  |
| 5 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_33) [page ] 33 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 6 | Role Owner Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Role Owner. |  |
| 7 | Log On | Log on to the SAP Cloud Identity Access Governance System as Security Officer. |  |  |
| 8 | Request Validation | Choose Access Request Inbox in the Access Request section.Find the request which is created in the [Schedule HR Triggers Job](#unique_33) [page ] 33 step under Requests list, click on it and then go to the Approve Requests page. |  |  |
| 9 | Security Officer Approval | Choose Approve All and then choose Submit. | Assess Request is approved by Security Officer. |  |

#### Schedule Provisioning Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as Administrator and schedule the provision job to SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure the access request is approved by all the relevant roles and is ready to be provisioned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Administrator. |  |  |
| 2 | Schedule Provisioning Job | Choose Job Scheduler in the Administrator section.In the Job Name field, enter <S4_Prov_2>.Select Provisioning from the Job Category dropdown list.Choose Schedule Job. | Provisioning Job is scheduled. |  |
| 3 | Validate Provisioning Job in Job History List | Validate the Provisioning Job scheduled in the previous step in Job History List. | There should be several lines of log information such as Role "SAP_XX_XXX_XXXXXX" assigned to user "Frank-Ford (Frank Ford)": Provisioned (Successful). in the detailed page of Job under Job History List. |  |

#### Employee Status Change Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP S/4HANA Cloud Public Edition as Administrator and validate that the business role(s) assigned to the business user is changed correctly.

Prerequisites

Before you start the test procedure, make sure the provisioning job is successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition System as an Administrator. |  |  |
| 2 | Validate Provisioning Result | Choose Maintain Business Users (F1303).In the User Name field, enter <Frank Ford> as mentioned in Preliminary Steps and choose Go.Click the user and drill down to the detail page. Validate the synchronized roles under Assigned Business Roles. | The business roles of business user are changed. |  |

### Global Assignment

#### Start Global Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Add a global assignment on employee in SuccessFactors System. This would result in new business roles assigned in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile page is displayed. |  |
| 3 | Add Global Assignment for Employee | Choose Actions at the top-right of the Employee Profile page and choose Add: Global Assignment Details in the list.Make the following entries and choose Save:Event Reason: <Add Global Assignment(ADDGA)>Assignment Type: <Short-term assignment>Company: <Different from current one, eg. DE 1010>Start Date: <Select as appropriate, eg. Today>Planned End Date: <Select as appropriate>Note For testing purpose, please use different values for Business Unit&Job Classification fields, or there will be no new business roles assigned in SAP S/4HANA Cloud Public Edition.Business Unit: <select as appropriate>Cost Center: <select from dropdown list>Job Classification: <select from dropdown list>Employee Class: <select from dropdown list>Employment Type: <select from dropdown list> | A new assignment appears under the home assignment in the header of the employee profile. |  |
| 4 | Access Management | Refer to step 2~6 in Employee Jobs Change for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | New business roles are added to the business user. |  |

#### End Global Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

End the global assignment for employee in SuccessFactors System. This would result in business roles unassigned in SAP S/4HANA Cloud Public Edition.

HR event (End Global Assignment) will be raised automatically on the end date of this assignment and it will be shown as Past Assignment in the header of the employee profile. This HR event could be captured by SAP Cloud Identity Access Governance and provisioned to SAP S/4HANA Cloud Public Edition. Alternatively, global assignment could be re-arranged or terminated manually during the assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. Select the global assignment in the header of the employee profile | Employee Profile page is displayed. |  |
| 3 | Terminate Employee | Choose Actions at the top-right of the Employee Profile page and choose Manage Global Assignment in the list.Change the end date or delete the global assignment directly.Note The effective date of event end global assignment is the next day of your selection. You need to choose yesterday as the end date if you want to continue immediately. Otherwise the event will not be captured by SAP Cloud Identity Access Governance right now. | Global assignment is re-arranged. |  |
| 4 | Access Management | Refer to step 2~6 in Employee Termination for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | Business roles bundled with global assignment are removed from the business user. User still exist with Business roles bundled with home assignment |  |

### Concurrent Employment

#### Start Concurrent Employment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Add a concurrent employment to employee in SuccessFactors System. This would result in new business roles assigned in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile page is displayed. |  |
| 3 | Add Concurrent Employment for Employee | Choose Actions at the top-right of the Employee Profile page and choose Add: Concurrent Employment in the list.Make the following entries and choose Save:Event Reason: <Concurrent Hire (CONHIRE)>Hire Date: <Select as appropriate, eg. Today>New Concurrent Employment: <US Company 1710>Note Please use different values for Business Unit and Job Classification fields, or there will be no new business roles assigned in SAP S/4HANA Cloud Public Edition.Business Unit: <select from dropdown list>Cost Center: <select from dropdown list>Job Classification: <select from dropdown list>Employee Class: <select from dropdown list>Employment Type: <select from dropdown list> | A new assignment appears in the header of the employee profile. |  |
| 4 | Access Management | Refer to step 2~6 in Employee Jobs Change for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | New business roles are added to the business user. |  |

#### End Concurrent Employment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

End the employee’s concurrent employment in SuccessFactors System. This would result in business roles unassigned in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. Select the concurrent assignment in the header of the employee profile. | Employee’s concurrent assignment is displayed on the Employee Profile page. |  |
| 3 | End Concurrent Employment for Employee | Choose Actions at the top-right of the Employee Profile page and click Terminate in the list.Choose the line of “Terminate selected assignment xxx” and click Continue.Make the following entries and choose Save:Termination Date: <Yesterday>Note The effective date of termination is the next day of your selection. If you choose today, there will be no termination event right now and you have to wait until tomorrow to have the event captured by SAP Cloud Identity Access Governance.Termination Reason: <End of Contract (TERCONT)>OK to Rehire: <Yes> | Concurrent assignment is shown as past in the header of the employee profile. |  |
| 4 | Access Management | Refer to step 2~6 in Employee Termination for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | Business roles bundled with concurrent employment are removed from the business user. User still exist with business roles bundled with original employment. |  |

### International Transfer

#### Terminate Old Employment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Terminate employee’s old employment on SuccessFactors System. This would result in business roles unassigned and business user deleted in SAP S/4HANA Cloud Public Edition.

Employees’ international transfer to a new country/ region and different legal entity within the company’s organization is recommended to be implemented with a termination and rehire with a new employment. This is because most payroll systems do not accept a legal entity change within an active employment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile page is displayed. |  |
| 3 | Terminate Employee’s Current Employment | Choose Actions at the top-right of the Employee Profile page and choose Terminate in the list.In the Terminate dialog box, make the following entries and choose Save:Termination Date: <Yesterday>Note The effective date of termination is the next day of your selection. If you choose today, there will be no termination event right now and you have to wait until tomorrow to have the event captured by SAP Cloud Identity Access Governance.Termination Reason: <International Transfer (TERINTNL)>OK to Rehire: <Yes> | Employee’s current employment is terminated. |  |
| 4 | Access Management | Refer to step 2~6 in Employee Termination for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | Business user is deleted and could not be found. |  |

#### Rehire with New Employment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Rehire the terminated employee with new employment in SuccessFactors System. This would result in the business user recreation and business roles assigned in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note Before scheduling the provision job in SAP Cloud Identity Access Governance to recreate the business user, logon SAP S/4HANA Cloud Public Edition with Administrator and go to app Maintain Deleted Business Users (F4347). Search the user you have deleted in step 4.7.1, select it and allow re-creation. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Rehire Inactive Employee in the search field on the right top of the home page. In Rehire Inactive Employee screen, search the terminated employee <Frank Ford>. Click the action button beside the employee’s name and choose Rehire with new employment. | Add new employee page is displayed. |  |
| 3 | Rehire Employee with New Employment | Make the following entries and choose Save:In the Identity section, make the following entries:Hire Date: <today>Company: <Company DE (1010)>Event Reason: <International Transfer (HIRINTNL)>Name Information section:User Name: <FRANKFORD2>Country/Region: <Germany>For the other fields’ value, keep as default.Choose Continue. |  |  |
| 4 | Rehire Employee with New Employment | In the Organizational Information section, make the following entries:Company: <leave the defaulted value>Business Unit: <select from dropdown list>Cost Center: <select from dropdown list>In the Job Information section, make the following entries:Supervisor: <enter as appropriate>Job Classification: <IT Analyst Demo (ITAnlst)>Employee Class: select Employee from dropdown.Employment Type: select Salaried from dropdown.Choose Submit on the bottom right of page.Choose Confirm on the dialog box. | Employee is rehired. |  |
| 5 | Access Management | Refer to step 3~6 in Employee Recruitment for access approval in SAP Cloud Identity Access Governance and validation in SAP S/4HANA Cloud Public Edition. | Business user is recreated and new business roles are assigned. |  |

### Employee Termination

#### Terminate Employee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Terminate Employee on SuccessFactors System. This would be the prerequisite of the deprovisioning from SAP Cloud Identity Access Governance to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Employee | Search Employee <Frank Ford> in the search field on the right top of the home page. | Employee Profile page is displayed. |  |
| 3 | Terminate Employee | Choose Actions at the top-right of the Employee Profile page and choose Terminate in the list.In the Terminate dialog box, make the following entries and choose Save:Termination Date: <Yesterday>Note The effective date of termination is the next day of your selection. If you choose today, there will be no termination event right now and you have to wait until tomorrow to have the event captured by SAP Cloud Identity Access Governance.Termination Reason: <Early Retirement (TERERLRT)>OK to Rehire:<Yes>Regret Termination:<Yes> | Employee is terminated. |  |

#### Workflow Request Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is required only in the case that Approval Workflow is enabled in SuccessFactors System. Based on your setting, the employee status change request should be approved by the manager or other people first in SuccessFactors, then the HR event can be active and be captured by SAP Cloud Identity Access Governance system.

For testing purpose, proxy tool is used in the steps to save your time. Normally, you need to change the logon user to the specific role to approve the request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central as Administrator. |  |  |
| 2 | Search Workflow Request and Proxy Approver | Search Manage Workflow Requests in search field at the right top of the Home page.In the Search Workflow Requests form, make the following entry and choose Search:Effective Date From: <Today>Effective Date To: <Today> |  |  |
| 3 | Update Workflow Approved User | Find the request record line. Then click the Actions button and choose Change Approvers.In the Update to field, copy <person's name> and close the dialog box.Choose Proxy Now in user profile dropdown list on top of the page.Paste the copied<person's name> in the dialog and wait for the automatic name matching. Then choose the provided name from drop down list.Choose OK. | Workflow Approved User is updated.The user’s role is changed to the target person who can approve the change request. |  |
| 4 | Search Workflow Request | Select Approve Requests tile, find the status change request. | The Approve Requests view displays. |  |
| 5 | Approve Employee Status Change Request | On Approve Requests dialog box, choose Approve of request.Choose Become Self in user profile dropdown list on top of the view to go back to the Admin user. | Employee Status Change request is approved. |  |

#### Schedule HR Triggers Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Schedule HR Triggers Job on SAP Cloud Identity Access Governance to capture the HR event and create an access request.

Prerequisites

Before you start the test procedures, make sure the employee is terminated successfully in SuccessFactors Employee Central.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as an Administrator. |  |  |
| 2 | Schedule HR Triggers Job | Choose Job Scheduler in the Administration section.In the Job Name field, enter <HR_Triggers_Job_3>.From the Job Category dropdown list, select HR Triggers.Choose Schedule Job.Note You can choose Yes to start job immediately or choose No to schedule a job weekly, daily, hourly or by “X” minutes. "X" is recommended to be more than 20 minutes. | HR Triggers Job is scheduled. |  |
| 3 | Validate Scheduled HR Triggers Job in Job History List | Validate the HR Triggers Job scheduled in step 2 in Job History List. | You should see a log message to indicate that the request was created. |  |
| 4 | Failure Job’s Analysis (Optional) | If the message in job history list shows that 0 request(s) created, the reason could be as follows,no business rules are defined,there are application issues,no access is associated for the event. |  |  |
| 5 | Resolve the Issue (Optional) | Contact your IT support to find out the root cause and fix the issue. |  |  |
| 6 | Reprocess Missing HR Events (Optional) | Navigate to Reports section and open Reprocess Missed HR Events tile.Search for user in the above failure job by entering the value in the Filter Option.Select the right record by clicking the available Checkbox. Then click on Retry button.Reschedule the HR Triggers Job in Job Scheduler tile. | Access request should be created successfully. |  |

#### Access Request Validation and Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as Security Officer and approve the access request, which would be the prerequisite of the user and role deprovisioning in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note Only access request triggered by Early Retirement event needs to be approved. Access request triggered by other HR event reasons in Termination is approved automatically in SAP Cloud Identity Access Governance. |

Prerequisites

Before you start the test procedures, make sure the HR Triggers Job is scheduled successfully and the access request is created.

Procedure

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Cloud Identity Access Governance System as Security Officer. |  |  |
| 2 | Request Validation and Approval by Security Officer | Choose Access Request Inbox in the Access Request section.Find the request created in the [Schedule HR Triggers Job](#unique_39) [page ] 49 step under the Requests list, click on it and then go to the Approve Requests page.Choose the Approve radio button under Access Requested and then choose Submit. | Access Request is approved by Security Officer.Note On Access Requested line, the value of action column should be Remove. |  |

#### Schedule Provisioning Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP Cloud Identity Access Governance System as Administrator and schedule the provision job to SAP S/4HANA Cloud Public Edition.

Prerequisites

Before you start the test procedures, make sure the access request is approved by all the relevant roles and is ready to be provisioned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Cloud Identity Access Governance System as Administrator. |  |  |
| 2 | Schedule Provisioning Job | Choose Job Scheduler in the Administrator section.In the Job Name field, enter <S4_Ter_1>.Select Provisioning from the Job Category dropdown list.Choose Schedule Job. | Deprovisioning Job is scheduled. |  |
| 3 | Validate Provisioning Job in Job History List | Validate the Provisioning Job scheduled in the previous step in Job History List. | There should be several lines log information such as FRANKFORD (Frank Ford)" deprovision: Deprovisioned (Successful) - requested from Access Request with ID XXX. in the detailed page of Job under Job History List. |  |

#### Employee Termination Validation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Log on to the SAP S/4HANA Cloud Public Edition as Administrator and validate that the business user is deleted successfully.

Prerequisites

Before you start the test procedure, make sure the deprovisioning job is successful.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP S/4HANA Cloud Public Edition System as an Administrator. |  |  |
| 2 | Validate Synchronization and Provision Result | Choose Maintain Business Users (F1303).In the User Name field, enter <Frank Ford> as mentioned in Add New Employee section and choose Go. | You should not be able to find the user. |  |

### Contingent Worker

#### Hire Contingent Worker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Hire a new contingent worker in SuccessFactors System. The steps are nearly the same as that in hire a new employee. However, “Contingent Worker” should be selected for Employee Group field.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SuccessFactors System | Log on to SuccessFactors Employee Central as HR manager. |  |  |
| 2 | Admin Center | From the Home dropdown, choose Admin Center. | SuccessFactors Admin Center page is displayed. |  |
| 3 | Add New Contingent Worker | Under the Tools section, search for Add Contingent Worker.Note The following example fields to be filled are just mandatory for fields mapping in SAP Cloud Identity Access Governance. You may need to type in additional information based on your SuccessFactors' setting. | Add Contingent Worker page is displayed. |  |
| 4 | Enter Identity Information for New Contingent Worker | In the Identity section, make the following entries:Start Date: <today>Company: <Company USA (1710)>Name Information section:First Name: <Frank>Last Name: <Ford>Employee Information section:Person ID: <FRANKFORD>User Name: <FRANKFORD>Choose Continue. | The Personal Information section in the Add Contingent Worker screen is expanded. |  |
| 5 | Enter Personal Information for New Contingent Worker | In the Personal Information section, enter data as appropriate.In the Contact Information section, select the (+) Add link. Make the following entries:Email Type: select Business.Email Address: <enter as appropriate>Is Primary: select Yes.Choose Continue. | The Job Information section in the Add Contingent Worker screen is expanded. |  |
| 6 | Enter Job Information for New Contingent Worker | In the Organizational Information section, make the following entries:Company: <leave the defaulted value>Business Unit: <Corporate (CORP)>Cost Center: <select from dropdown list>Caution The Cost Center field must be filled, or the sync of contingent worker to S/4HANA Cloud will be failed!In the Job Information section, make the following entries:Supervisor: <enter as appropriate>Job Classification: <select from drop-down list>Employee Class: select Contingent Worker from dropdown.Employment Type:<select from dropdown list>In the Work Order Information section, make the following entries:Work Order ID: <enter as appropriate>Work Order Name: <enter as appropriate>Owner ID: <enter as appropriate>Supplier: <select from drop-down list>End Date: <select from calendar>Start Date: <keep as default>Choose Submit on the bottom right of page. | The new contingent worker is added successfully. |  |
| 7 | Access Management | Refer to step 3~6 in Employee Recruitment for access approval in SAP Cloud Identity Access Governance and validation in S/4HANA Cloud. | Business user is created and new business roles are assigned. |  |

#### End Contingent Worker

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Contingent worker will be terminated automatically in SuccessFactors at the end date of the work order. HR event (End of Contingent Worker) will be raised automatically on the end date. Alternatively, the worker could also be manually terminated by editing the end date. The HR event could be captured by SAP Cloud Identity Access Governance and provisioned to S/4HANA cloud.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors as HR Manager. |  |  |
| 2 | Search Contingent Worker | Search contingent worker <Frank Ford> in the search field on the right top of the home page. | Contingent worker Profile page is displayed. |  |
| 3 | Check Contingent Worker’s Event | Navigate to the Employment Information section. Click the clock button beside Job Information to see the change history. | Contingent worker is terminated. |  |
| 4 | Terminate contingent worker ahead (Optional) | Choose Actions at the top-right of the Contingent Worker Profile page and choose Edit Work Order Information in the list.In the dialog box, make the following entries and choose Save:End Date: <Yesterday>Note The effective date of termination is the next day of your selection. If you choose today, there will be no end contingent worker event right now and you have to wait until tomorrow to have the event captured by SAP Cloud Identity Access Governance. |  |  |
| 5 | Access Management | Access request approval for end contingent worker process is not required. Please refer to the step 2, 3, 5 and 6 in Employee Termination for removing business user in S/4HANA Cloud and validating the result. | Business user is deleted and could not be found. |  |

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
> Flagged while digesting this document, not verified: App naming inconsistency inside the document: Employee Recruitment > View Employee Basic Data step 'Go to the Manage Workforce' says to open 'Manage Service Level Agreements (F6183A)', while the Overview Table lists 'Manage Workforce' and the JB1 section names 'Manage Workforce (F6097A)'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3AB_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 94,340 chars in the whole document
