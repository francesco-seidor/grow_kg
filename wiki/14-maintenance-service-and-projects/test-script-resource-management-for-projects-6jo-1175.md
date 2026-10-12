---
id: 14-maintenance-service-and-projects/test-script-resource-management-for-projects-6jo-1175
title: "Test Script: Resource Management for Projects (6JO) (6JO_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6JO: resource requests, staffing, utilization, and team member assignments/experience via SAP Project and Resource Management."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/resource-management]
aliases: [6JO_S4CLD2608_BPD_EN_XX]
keywords: [Resource Management for Projects, resource management, resource requests, resource staffing, resource utilization, project team member assignments, project experience, test scripts, business roles, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JO_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1175
topic: 14-maintenance-service-and-projects/resource-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Resource Management for Projects (6JO) (6JO_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JO_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Resource Management for Projects** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Resource Management for Projects (6JO) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232826348)

[2 Prerequisites 3](#_Toc232826349)

[2.1 System Access 3](#_Toc232826350)

[2.2 Roles 3](#_Toc232826351)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232826352)

[2.4 Additional Manual Configuration 5](#_Toc232826353)

[2.5 Business Conditions 5](#_Toc232826354)

[3 Overview Table 6](#_Toc232826355)

[4 Test Procedures 7](#_Toc232826356)

[4.1 Manage Resource Requests and Staffing as a Resource Manager 7](#_Toc232826357)

[4.1.1 Manage Resource Requests 7](#_Toc232826358)

[4.1.2 Staff Resource Requests 8](#_Toc232826359)

[4.1.3 Manage Resource Utilization 9](#_Toc232826360)

[4.2 Manage My Assignments and My Project Experience as a Project Team Member 10](#_Toc232826361)

[4.2.1 Manage My Assignments 10](#_Toc232826362)

[4.2.2 Manage My Project Experience 11](#_Toc232826363)

[5 Appendix 13](#_Toc232826364)

[5.1 Process Integration 13](#_Toc232826365)

[5.1.1 Succeeding Processes 13](#_Toc232826366)

## Purpose

Overview

SAP Project and Resource Management allows you as a resource manager to monitor and manage the resource utilization and the staffing of resource requests, ensuring optimal resource management. It allows resources to manage their profile of skills and assignments to be matched with the right kinds of projects. It also allows the project managers to create, manage, and monitor requests for resources on their projects.

This scope item is a public cloud solution delivered on the SAP Business Technology Platform (SAP BTP). The integration with SAP S/4HANA Cloud Public Edition is enabled through this scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Set-Up Instructions - Links to Documentation

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.

If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Project and Resource Management | Your system administrator provides you with the URL of the SAP Project and Resource Management. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Suggested sample user PROJECT_MANAGER_PROF representing the business role Project Manager – Professional Services. |
| Resource Manager - Projects | SAP_BR_RESOURCE_MANAGER_PRJ | Resource Management - Projects | SAP_BR_SPT_RESOURCE_MANAGER_PRJ_PC | Suggested sample user RESOURCE_MANAGER_PRJ representing the business role Resource Manager - Projects. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Suggested sample user EMPLOYEE representing the business role Employee. |
| Project Team Member | SAP_BR_PROJECTTEAMMEMBER | Work Experience - Projects | SAP_BR_SPT_TEAM_MEMBER_PRJ_PC | Suggested sample user PROJECTTEAMMEMBER representing the business role Project Team Member. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

You may use below master data to create a customer project by referring to the J11 test script.

Alternatively use your own master data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 10100002 |  |  |
| Activity Type | T003 | Platinum Consultant |  |
| Activity Type | T005 | Project Manager |  |
| Service Organization/Delivery Organization | 1010 | The following Enterprise Structures are assigned to the Service Organization:Controlling Area: A000Company Code: 1010Cost Center: RMMASTDE01Plant 1 DEDistribution Channel 10Division 00Sales Organization 1010 | The Service Organization – Company DE is also defined as Delivery Organization. |
| Cost Center | 10101902 | Csltg Unit A |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e34a30e0c83a42a6439e7e1499597782)

Then follow the additional configuration steps described below:

1. Maintain the details of the service organizations that are used in resource management capability. For more information, refer to:

[Maintaining Service Organizations](https://help.sap.com/docs/PPRM_OD/542f4545bc9d4ecd80bc3a0a6913a735/627ec119266e483aa8993675d71957d6.html?version=latest)

1. Maintain the details of the resource organizations that are used in resource management capability. For more information, refer to:

[Managing Resource Organizations](https://help.sap.com/docs/PPRM_OD/542f4545bc9d4ecd80bc3a0a6913a735/91cd2042c8634df9aa41840e1fb2f5b3.html?version=latest)

1. Maintain the workforce person availability data that is used in resource management capability. For more information, refer to:

[Maintaining Availability Data](https://help.sap.com/docs/PPRM_OD/542f4545bc9d4ecd80bc3a0a6913a735/28d5e059a5c7442ab0029c76156fec0a.html?version=latest)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services or1A8 - Internal Project Management – Project-Based Services | If you are working on customer projects, before running this test script, you must finish mandatory steps in J11 including Maintain Customer Project, Maintain Work Packages and Time-based Planning, Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects).If you are working on internal projects, please finish mandatory steps in scope item 1A8, including Maintain Internal Project, Maintain Work Packages and Time Based Planning, Maintain Settlement Rules, Maintain Work Package Staffing (With Scope Item 6JO: Resource Management for Projects). |
| 4RF - Project Control – Resourcing and Procurement | If you are working on enterprise projects, before running this test script, you must finish mandatory steps related to Resource Demand in scope item 4RF along with project creation in scope item 1NT |

## Overview Table

This scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Resource Requests and Staffing as a Resource Manager](#unique_9) [page ] 7 |  |  |  |
| [Manage Resource Requests](#unique_10) [page ] 7 | Resource Manager - Projects | Manage Resource Requests (F4723) |  |
| [Staff Resource Requests](#unique_11) [page ] 8 | Resource Manager - Projects | Staff Resource Requests |  |
| [Manage Resource Utilization](#unique_12) [page ] 9 | Resource Manager - Projects | Manage Resource Utilization |  |
| Manage My Assignments and My Project Experience as a Project Team Member |  |  |  |
| [Manage My Assignments](#unique_13) [page ] 10 | Project Team Member | My Assignments (F5991) |  |
| [Manage My Project Experience](#unique_14) [page ] 11 | Project Team Member | My Project Experience (F4705) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Resource Requests and Staffing as a Resource Manager

If you encounter issues in the following steps, please create an incident with component: PPM-CLD-RES.

This activity shows how the Resource Manager manages resource requests and staffing processes.

#### Manage Resource Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Resource Manager can view resource requests that are created from SAP S/4HANA Cloud Public Edition applications like Project Control (F3215) or Create Customer Projects (F0719) or Manage Projects (F8336) / Create Internal Projects - Old Version (F1656) apps. Alternatively, he/she can use BTP apps to create and maintain resource requests in BTP. After publishing resource requests, the resource requests are visible to the resource manager.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Resource Manager - Projects. | The SAP Fiori launchpad displays. |  |
| 2 | View Resource Requests | Open Manage Resource Requests (F4723). You can filter and find your resource requests, for example by Request ID, Work Package, etc. |  |  |
| 3 | Prepare Resource Requests for Staffing | Please refer to step: [Preparing Resource Requests for Staffing](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/7e86a93864cb40868baa3849a719bee1.html) in User Guide for Resource Management in SAP Project and Resource Management.You may use the projects created in scope item 1NT, J11 or 1A8 to filter the desired resource requests.Alternatively you can follow step 4 to 6 to maintain resource requests in BTP. |  |  |
| 4 | Edit Resource Requests | Please refer to step: [Editing Resource Requests](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/bb958b4c46704069b0ad5552530b2113.html) in User Guide for Resource Management in SAP Project and Resource Management. |  |  |
| 5 | Publish Resource Requests | Please refer to step: [Publishing Resource Requests](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/e4278db7d7084607a4853504b76c4c2c.html) in User Guide for Resource Management in SAP Project and Resource Management. | The publishing status of the resource request is set to Published. The resource request is now visible to the resource manager, who can start the staffing process. |  |

#### Staff Resource Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Resource Manager - Projects can assign and/or change staffing and staffed hours, then synchronized back to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to BTP System | Log on to the SAP Project and Resource Management as a Resource Manager - Projects. |  |  |
| 2 | Staff Resource Requests | Please refer to step: [Staffing Resource Requests](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/a3f9f4db6c94435f8c7e19ecca4ca07a.html) in User Guide for Resource Management in SAP Project and Resource Management. | The Assignment Status for Assigned Resources is Hardbooked.The information is synchronized to SAP S/4HANA Cloud Public Edition. You may check in the Customer Project if the staffing is correctly shown in the project. |  |
| 3 | View Resource Assignments in SAP S/4HANA Cloud Public Edition | If you want to see resource assignments for customer/internal projects then log on to the SAP Fiori launchpad as a Project Manager - Professional Services. Open app Create Customer Projects (F0719), tab Team, and check Staffed Resources.OrIf you want to see resource assignments for enterprise projects then log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. Open app Manage Project Demand (F4562), go to Resources tab and choose the demand for which you want to see external staffing, go to tab Assignments, and check Staffed Resources. | The information is synchronized to SAP S/4HANA Cloud Public Edition from BTP. The Staffed Resource is the assigned resource in BTP. |  |

#### Manage Resource Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Resource Manager - Projects checks the overbooked resource and changes his assignments to balance the workload.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to BTP System | Log on to the SAP Project and Resource Management as a Resource Manager - Projects. |  |  |
| 2 | View Resource Utilization and Identify Overbooked Resources and Periods | Please refer to step: [Monitoring Resource Utilization](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/0b8a990024034f61b8dfe1a883bc684d.html) in User Guide for Resource Management in SAP Project and Resource Management. |  |  |
| 3 | Change Assignments to Balance Load | Please refer to step: [Editing Assignments](https://help.sap.com/viewer/afef0d26c811418aaebe8878e0a3cbaa/latest/en-US/574e00ade56c4292aebffb0961f13455.html) in User Guide for Resource Management in SAP Project and Resource Management.You may decrease the staffed hours by 10 hours. |  |  |
| 4 | View Resource Assignments in SAP S/4HANA Cloud Public Edition | If you want to see resource assignments for internal/customer project then log on to the SAP Fiori launchpad as a Project Manager - Professional Services. Open app Create Customer Projects (F0719), tab Team and check Effort (Staffed).OrIf you want to see resource assignments for enterprise projects then log on to the SAP Fiori launchpad as a Project Controller - Resourcing and Procurement. Open app Manage Project Demand (F4562), go to Resources tab and choose the demand for which you want to see external staffing, go to tab Assignments, and check Staffed Resources. | The information is synchronized to SAP S/4HANA Cloud Public Edition from BTP. The staffed hours are decreased by 10 hours. |  |

### Manage My Assignments and My Project Experience as a Project Team Member

#### Manage My Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Team Member navigates from SAP S4/HANA Cloud to BTP System-SAP Project and Resource Management with app My Assignments (F5991).

App My Assignments (F5991) allows you to view and edit assignments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Team Member. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open My Assignments (F5991). |  |  |
| 3 | View and Edit Assignment | View and edit your assignment by referring to step: [My Assignments](https://help.sap.com/docs/PPRM_OD/afef0d26c811418aaebe8878e0a3cbaa/5dd58215e340471885c64af84f4b1bc3.html) in User Guide for Resource Management in SAP Project and Resource Management.Note Project Team Member must be assigned to certain resource request. |  |  |

#### Manage My Project Experience

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Team Member navigates from SAP S4/HANA Cloud to BTP System-SAP Project and Resource Management with app My Project Experience (F4705).

App My Project Experience (F4705) allows you to update project experience, view current assignments, update profile details and monitor your utilization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Team Member. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open My Project Experience (F4705). |  |  |
| 3 | Manage Project Experience | You can update project experience, view current assignments, update profile details and monitor your utilization by referring to step [My Project Experience](https://help.sap.com/docs/PPRM_OD/afef0d26c811418aaebe8878e0a3cbaa/a28e72c9228d4822ad89a63a395cc4a6.html) in User Guide for Resource Management in SAP Project and Resource Management. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes for Customer/Internal projects or Enterprise projects:

| Process | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based ServicesOr1A8 - Internal Project Management – Project-Based Services | If the preceding procedure is in scope item J11, then go back to J11, continue with Maintain Customer Project Billing and finish the remaining J11 steps.If the preceding procedure is in scope item 1A8, then continue with step Run Settlement and finish the remaining 1A8 steps. |
| 4RF - Project Control – Resourcing and Procurement | If the preceding procedure is in scope item 4RF, then go back to 4RF and continue with remaining steps (Assign Resource or Monitor Demand). |

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
- see-also :: [[14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JO_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 24,553 chars in the whole document
