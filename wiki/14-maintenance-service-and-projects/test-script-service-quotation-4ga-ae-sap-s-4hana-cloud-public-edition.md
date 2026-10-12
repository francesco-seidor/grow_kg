---
id: 14-maintenance-service-and-projects/test-script-service-quotation-4ga-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Service Quotation (4GA_AE) - SAP S/4HANA Cloud Public Edition (4GA_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 4GA Service Quotation: prerequisites, service teams, and create/send/change/accept/requote/reject steps."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-quotation]
aliases: [4GA_S4CLD2608_BPD_EN_AE]
keywords: [Service Quotations, service quotation, test procedures, fixed price quotation, service bundle, fixed price service bundle, service teams, quotation requote, quotation acceptance, quotation rejection]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GA_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1022
topic: 14-maintenance-service-and-projects/service-quotation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service Quotation (4GA_AE) - SAP S/4HANA Cloud Public Edition (4GA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Service Quotations** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Quotation (4GA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855009)

[2 Prerequisites 4](#_Toc232855010)

[2.1 System Access 4](#_Toc232855011)

[2.2 Roles 4](#_Toc232855012)

[2.3 Master Data, Organizational Data, and Transactional Data 5](#_Toc232855013)

[2.4 Additional Manual Configuration 6](#_Toc232855014)

[2.5 Configure Service Teams 7](#_Toc232855015)

[2.5.1 Define Service Team Profile 7](#_Toc232855016)

[2.5.2 Assign Service Team Profile to Service Transactions 9](#_Toc232855017)

[2.5.3 Create a Service Team 11](#_Toc232855018)

[3 Overview Table 12](#_Toc232855019)

[3.1 Service Quotation 12](#_Toc232855020)

[3.1.1 Service Quotation Item 12](#_Toc232855021)

[3.1.2 Fixed Price Service Bundle 12](#_Toc232855022)

[3.1.3 Service Bundle 13](#_Toc232855023)

[3.2 Fixed Price Service Quotation 13](#_Toc232855024)

[3.2.1 Fixed Price Item 13](#_Toc232855025)

[3.2.2 Fixed Price Service Bundle 14](#_Toc232855026)

[4 Test Procedures 15](#_Toc232855027)

[4.1 Service Quotation 15](#_Toc232855028)

[4.1.1 Service Quotation Item 15](#_Toc232855029)

[4.1.1.1 Create Service Quotation 15](#_Toc232855030)

[4.1.1.2 Send to Customer 17](#_Toc232855031)

[4.1.1.3 Change or Update Service Quotation 17](#_Toc232855032)

[4.1.1.4 Accept Service Quotation 18](#_Toc232855033)

[4.1.1.5 Create a Requote for Service Quotation 19](#_Toc232855034)

[4.1.1.6 Reject Service Quotation 20](#_Toc232855035)

[4.1.2 Fixed Price Service Bundle 21](#_Toc232855036)

[4.1.2.1 Create Service Quotation 21](#_Toc232855037)

[4.1.2.2 Send to Customer 22](#_Toc232855038)

[4.1.2.3 Change or Update Service Quotation 23](#_Toc232855039)

[4.1.2.4 Accept Service Quotation 24](#_Toc232855040)

[4.1.2.5 Reject Service Quotation 24](#_Toc232855041)

[4.1.3 Service Bundle 25](#_Toc232855042)

[4.1.3.1 Create Service Quotation 25](#_Toc232855043)

[4.1.3.2 Send to Customer 27](#_Toc232855044)

[4.1.3.3 Change or Update Service Quotation 28](#_Toc232855045)

[4.1.3.4 Accept Service Quotation 28](#_Toc232855046)

[4.1.3.5 Reject Service Quotation 29](#_Toc232855047)

[4.2 Fixed Price Service Quotation 30](#_Toc232855048)

[4.2.1 Fixed Price Item 30](#_Toc232855049)

[4.2.1.1 Create Service Quotation 30](#_Toc232855050)

[4.2.1.2 Send to Customer 32](#_Toc232855051)

[4.2.1.3 Change or Update Service Quotation 32](#_Toc232855052)

[4.2.1.4 Accept Service Quotation 33](#_Toc232855053)

[4.2.1.5 Create a Requote for Service Quotation 34](#_Toc232855054)

[4.2.1.6 Reject Service Quotation 35](#_Toc232855055)

[4.2.2 Fixed Price Service Bundle 36](#_Toc232855056)

[4.2.2.1 Create Service Quotation 36](#_Toc232855057)

[4.2.2.2 Send to Customer 37](#_Toc232855058)

[4.2.2.3 Change or Update Service Quotation 38](#_Toc232855059)

[4.2.2.4 Accept Service Quotation 39](#_Toc232855060)

[4.2.2.5 Reject Service Quotation 40](#_Toc232855061)

[5 Appendix 41](#_Toc232855062)

[5.1 Succeeding Scope Items 41](#_Toc232855063)

## Purpose

Overview

This scope item covers the service quotation process in SAP S/4HANA Cloud Public Edition. The service quotations are used to provide legally binding offers with fixed conditions made to a customer for the performance of services.

Customer Service managers may use quotations to provide cost estimates before placing an order. Both Time and Material (T&M) and Fixed Price cost estimates are supported with validity period. The validity period of the service quotation can be changed by the customer service manager with an option to carry out repricing as per the new validity.

Upon finalizing the service quote with required services and price offered, the customer service manager can either print or generate the quote as a PDF, then attach it to an email to be sent to customer for negotiation.

The service quote can then be set to Accepted or Rejected. Finally, the service quote acceptance triggers the automatic creation or update of service orders as a follow-on process

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4GA_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials and customers.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100003 | Domestic UAE Customer 3 | You must either assign the customer pricing procedure 01 (Procedure 01) or ensure that the customer is not assigned to a pricing procedure.To check the assignment, use business role SAP_BR_BUPA_MASTER_SPECIALIST and access Manage Customer Master Data (F0850A). |
| Employee | <employee> | Use the employee ID that is assigned to your user. |  |
| Service Product (Service) | SRV_01 | Services | The service product SRV_01 represents the service itself, for example, an installation, a repair, or maintenance. |
| Service Product (Service Expense) | SRV_02 | Service Expenses | The service product SRV_02 is used to reflect the expense which could occur due to the service, for example, travel cost or fuel. |
| Service Part (Undefined) | SRV_03 | Service Part (Undefined) | The spare part of the material type non-stock can only be procured.This is only used in scope item Procurement for Service Management (3NI). |
| Service Part (Defined) | SRV_04 | Service Part (Defined) | The material type is Non-Stock Material.Note If you want to test a spare part which is procured, you must activate scope item Procurement for Service Management (3NI).A purchasing info record, source supplier, and sales price are needed. |
| Service Part for Pick-from-Stock | SRV_05 | Stock Service Part | The service product SRV_05 represents a material which will be taken from stock (pick-from-stock scenario).Note If you are using a material such as SRV_05 with the item category group Stock Service Part (SVST), this material will be taken from the default storage location of the plant, for example, 331A. |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Configuration for AVC Product |  |  | Note If you are using a configurable product (AVC) in quotation, please refer to the Service Management with Advanced Variant Configuration (6GS) test script. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

### Configure Service Teams

#### Define Service Team Profile

Purpose

A service team profile exists by default. It defines which determination rule is used and for which team types it is relevant. If you want to use a different profile, you can follow the procedure below to create a new entry.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Define Service Team Profile and Assign Service Team Types step, choose Configure. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 7 | Define Team Profile | There should be at least one existing entry:Profile:SRV_FS_PDescription:Field Service Team ProfileDetermination Rule:SHIP_TODescription:Country and postal code of ship-to partyAuto Redetermine:?If you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 8 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_FS_P, you should find the following entry:Team Type: SRV_FSDescription: Field ServiceIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Service Team Profile and Assign Service Team Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The screen Define Service Team Profile and Assign Serv..: Change screen displays. |  |
| 3 | Define Team Profile | There should be at least one existing entry:Profile:SRV_FS_PDescription:Field Service Team ProfileDetermination Rule:SHIP_TODescription:Country and postal code of ship-to partyAuto Redetermine:?If you want to use another profile, you have to create a new entry here. | A valid service team profile exists. |  |
| 4 | Specify Allowed Team Types | Select an existing team profile and doublc-click Specify Allowed Team Types in the Dialog Structure.For the team profile SRV_FS_P, you should find the following entry:Team Type: SRV_FSDescription: Field ServiceIf you have created and selected a new profile, maintain the allowed team types here. | A valid service team profile including allowed team types exists. |  |

#### Assign Service Team Profile to Service Transactions

Purpose

If you want to use the service team concept, you should assign at least a service team profile to a service transaction and to its related confirmation transaction.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: ServiceSub Application Area: Service Order Management |  |  |
| 5 | Open | Open Service Teams. |  |  |
| 6 | Select Configuration Step | For the Assign Service Team Profile to Service Transaction Type step, choose Configure. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 7 | Maintain Data | If you want to use the service team concept in the service quotation, make the following entries and choose Save:Trans.Type: SVQ1Description: Service QuotationService Team Profile: SRV_FS_PDescription: Field Service Team Profile | The service team concept has been activated for the service quotation (SVQ1). |  |
| 8 | Maintain Data | If you want to use the service team concept in the service order, make the following entries and choose Save:Trans.Type: SVQ2Description: Service Quotation (Fixed Price)Service Team Profile: SRV_FS_PDescription: Field Service Team Profile | The service team concept has been activated for the fixed price service quotation (SVQ2). |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Service Team Profile to Service Transaction Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Service Team Profile to Service Transaction screen displays. |  |
| 3 | Maintain Data | If you want to use the service team concept in the service quotation, make the following entries and choose Save:Trans.Type: SVQ1Description: Service QuotationService Team Profile: SRV_FS_PDescription: Field Service Team Profile | The service team concept has been activated for the service quotation (SVQ1). |  |
| 4 | Maintain Data | If you want to use the service team concept in the service order, make the following entries and choose Save:Trans.Type: SVQ2Description: Service Quotation (Fixed Price)Service Team Profile: SRV_FS_PDescription: Field Service Team Profile | The service team concept has been activated for the fixed price service quotation (SVQ2). |  |

#### Create a Service Team

Purpose

If you want to use the service team concept, you have to create at least one service team to run the service process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create A New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: Service_Team_AEDescription: Service Team AEType: SRV_FS |  |  |
| 5 | Enter Responsibility Definitions | Under Responsibility Definitions, make the following entries:Country: AEPostal Code: <empty>Service Part Plant: 3310Service Part Storage Location: 331A |  |  |
| 6 | Enter Team Owner | It is recommended to leave the default team owner. |  |  |
| 7 | Enter Team Members | Choose Create.Choose Edit.Enter data for each team member of this service team:Business Partner: for example, 9980000XXXFull Name: <team member's name>User ID: for example, CB9980000XXXFunction: Executing Service Employee (SRVC_EMPL)Choose Save. | A service team has been created successfully. |  |

## Overview Table

The scope item Service Quotation (4GA) covers legally binding offers with fixed conditions made to a customer for the performance of services. It helps customer service managers provide cost estimates before placing an order. Time and material (T&M) and fixed price based cost estimates are supported with an auto-creation of service orders once accepted by the customer.

This scope item differentiates between the scenario variants time and material, fixed price, and fixed price service bundle.

### Service Quotation

#### Service Quotation Item

This process variant starts with the creation of a service quotation. The key characteristic is that the total quotation amount is calculated on the basis of time and material.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Quotation](#unique_12) [page ] 15 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A standard quotation has been created. |
| [Send to Customer](#unique_13) [page ] 17 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been sent to the customer. |
| [Change or Update Service Quotation](#unique_14) [page ] 17 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been changed to reflect the customer’s feedback. |
| [Accept Service Quotation](#unique_15) [page ] 18 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been accepted and a service order has been created automatically. |
| [Reject Service Quotation](#unique_16) [page ] 20 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been rejected. |

#### Fixed Price Service Bundle

This process variant starts with the creation of a service quotation. The key characteristic is that the total quotation amount is calculated on the basis of time and material.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Quotation](#unique_18) [page ] 30 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A fixed price quotation has been created. |
| [Send to Customer](#unique_19) [page ] 32 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been sent to the customer. |
| [Change or Update Service Quotation](#unique_20) [page ] 32 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been changed to reflect the customer’s feedback. |
| [Accept Service Quotation](#unique_21) [page ] 33 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been accepted and a service order has been created automatically. |
| [Reject Service Quotation](#unique_22) [page ] 35 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been rejected. |

#### Service Bundle

This process variant starts with the creation of a service quotation. The key characteristic is that the total quotation amount is calculated on the basis of time and material.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Quotation](#unique_24) [page ] 25 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A fixed price quotation has been created. |
| [Send to Customer](#unique_25) [page ] 27 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been sent to the customer. |
| [Change or Update Service Quotation](#unique_26) [page ] 28 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been changed to reflect the customer’s feedback. |
| [Accept Service Quotation](#unique_27) [page ] 28 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been rejected. |
| [Reject Service Quotation](#unique_28) [page ] 29 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been accepted and a service order has been created automatically. |

### Fixed Price Service Quotation

#### Fixed Price Item

This scenario means a fixed price is maintained in the service quotation.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Quotation](#unique_30) [page ] 36 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A fixed price quotation for a service bundle has been created. |
| [Send to Customer](#unique_31) [page ] 37 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been sent to the customer. |
| [Change or Update Service Quotation](#unique_32) [page ] 38 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been changed to reflect the customer’s feedback. |
| [Accept Service Quotation](#unique_33) [page ] 39 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been accepted for the service bundle and a service order has been created automatically. |
| [Reject Service Quotation](#unique_34) [page ] 40 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been rejected. |

#### Fixed Price Service Bundle

This scenario means a fixed price is maintained in the service quotation.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Quotation](#unique_30) [page ] 36 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | A fixed price quotation for a service bundle has been created. |
| [Send to Customer](#unique_31) [page ] 37 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been sent to the customer. |
| [Change or Update Service Quotation](#unique_32) [page ] 38 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been changed to reflect the customer’s feedback. |
| [Accept Service Quotation](#unique_33) [page ] 39 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been accepted for the service bundle and a service order has been created automatically. |
| [Reject Service Quotation](#unique_34) [page ] 40 | Customer Service Manager | Manage Service Quotations - Overview (F4251) | The quotation has been rejected. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Service Quotation

#### Service Quotation Item

##### Create Service Quotation

Purpose

Using the quick create option, you can create a service quotation. The service quotation will be in the Open state when it is created. The service quotation can be viewed and edited.

This process variant calculates the total billed amount based on the confirmed service item, expense item or a service part.

|  |
| --- |
| Note Service Quotation supports the following items:Service Product (SRV_01)Expense Product (SRV_02)Service Parts (SRV_03, SRV_04)Stock Service (SRV_05) |

|  |
| --- |
| Note You don't have to create a new service quotation if you have created a follow up from service order template. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | The Create Service Quotation window displays. |  |
| 4 | Maintain Service Quotation Data | Make the following entries:Service Quotation Type: Service QuotationSold-To Party: for example, 33100003Description: <description>Requested Start Date - End Date: <date range>Product ID: for example. SRV_01Quantity: for example, 1Unit: for example, HRProduct ID: for example. SRV_02Quantity: for example, 1Unit: for example, EAProduct ID: for example. SRV_05Quantity: for example, 1Unit: for example, PCPress Enter.Choose Save. | A new service quotation is created with the status Open.Note By default, the service item SRV_01 is a time and material item with item category SQP1.If you need to use a fixed price item instead of a time and material item, change the item category to SQP3 (Fixed Price) or SQW3 (External Service).Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.Note If the service team concept has been enabled for the service quotation (SVQ1), a dialog box may appear and ask you to choose a service team.Select your service team.Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SQW1 (External Service SES).Note If you enabled credit check management for service quotation and the service quotation is blocked by the credit, then please refer to scope item Advanced Credit Management (1QM) for information about resolving it.Note If you are using a configurable product (AVC), please refer to the test script Service Management with Advanced Variant Configuration (6GS). |  |

##### Send to Customer

Purpose

In this step, you send the quote to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003Status: Open | The service quotations are filtered based on your entries. |  |
| 4 | Send Quote to Customer | Choose your service quotation.On the Service Quotation screen, choose Send to Customer. | The service quotation is sent to the customer and the status changes to Sent to Customer. |  |

##### Change or Update Service Quotation

Purpose

In this step, you modify service quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Edit Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Edit. |  |  |
| 5 | Change Service Quotation | Make a change to a service quotation item and choose Save. | The changes are saved.The status changes to Under Review.Note Quotes under review can be sent to the customer or accepted. |  |

##### Accept Service Quotation

Purpose

In this step, you accept the service quotation. A service order is created once the quote is accepted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Accept Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Accept. | The status changes to Accepted.Note Accepted service quotes will automatically create a service order internally.Note down the service order number.Note Items in the quote can be partially accepted and the total quote amount will be adjusted according to total items accepted. |  |

##### Create a Requote for Service Quotation

Purpose

In this step, you provide a requote during the service order review process. Services can be added if required. A new quotation is created, additional items are added, and the quotation is sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Requote | Choose your service quotation.On the Service Quotation screen, choose Requote.Note The Requote button is disabled if the follow-up service order has the status Completed. | The status changes to Open. |  |
| 5 | Edit Service Quotation | Choose Edit. |  |  |
| 6 | Add Item to Service Quotation | Under Items, make the following entries and choose Save:Product ID: for example. SRV_05Quantity: for example, 1Unit: for example, PC | The changes are saved. |  |
| 7 | Send to Customer | Chosse Send to Customer. | The status changes to Sent to Customer. |  |
| 8 | Accept Quotation | Choose Accept. | The status changes to Accepted. |  |
| 9 | Verify Service Order | Under Transaction History, choose the Service Order. | The service order contains the new item added through the requote process.Note The requote is only enabled if the service quotation is accepted and a follow-up service order is created. |  |

##### Reject Service Quotation

Purpose

In this step, you reject service quotations that do not meet customer expectations or have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Reject Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Reject.In the Reject Quotation dialog box, make the following entries and choose Reject:Rejection Reason: for example, Rejected by Customer | The Reject Quotation dialog box displays.The status changes to Rejected. |  |

#### Fixed Price Service Bundle

##### Create Service Quotation

Purpose

Using the quick create option, you can create a service quotation. The service quotation will be in the Open state when it is created. The service quotation can be viewed and edited.

This scenario is a variant of a service quotation which uses a fixed priced service bundle. A fixed price service bundle contains sub items which can be a service item, an expense item or a service part. Your customer is quoted the fixed price amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | The Create Service Quotation window displays. |  |
| 4 | Maintain Service Quotation Data | Make the following entries:Service Quotation Type: Service QuotationSold-To Party: for example, 33100003Description: <description>Requested Start Date - End Date: <date range>Product ID: for example. SRV_BUNDLE_01Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save. | A new service quotation is created with the status Open.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.Note If the service team concept has been enabled for the service quotation (SVQ1), a dialog box may appear and ask you to choose a service team.Select your service team.Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SQW1 (External Service SES). |  |
| 5 | Maintain Subitems | Under Items, make the following entries:Product ID: for example. SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRPress Enter.Make the following entries:Product ID: for example. SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save.Note By default, the item category for a fixed price service bundle is Service Bundle (FP) (SQB2).You can only bill the service bundle upon completion. | A service quotation with a fixed price service bundle is created. |  |

##### Send to Customer

Purpose

In this step, you send the quote to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003Status: Open | The service quotations are filtered based on your entries. |  |
| 4 | Send Quote to Customer | Choose your service quotation.On the Service Quotation screen, choose Send to Customer. | The service quotation is sent to the customer and the status changes to Sent to Customer. |  |

##### Change or Update Service Quotation

Purpose

In this step, you modify service quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Edit Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Edit. |  |  |
| 5 | Change Service Quotation | Make a change to a service quotation item and choose Save. | The changes are saved.The status changes to Under Review.Note Quotes under review can be sent to the customer or accepted. |  |

##### Accept Service Quotation

Purpose

In this step, you accept the service quotation. A service order is created once the quote is accepted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Accept Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Accept. | The status changes to Accepted.Note Accepted service quotes will automatically create a service order internally.Note down the service order number.Note Items in the quote can be partially accepted and the total quote amount will be adjusted according to total items accepted. |  |

##### Reject Service Quotation

Purpose

In this step, you reject service quotations that do not meet customer expectations or have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Reject Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Reject.In the Reject Quotation dialog box, make the following entries and choose Reject:Rejection Reason: for example, Rejected by Customer | The Reject Quotation dialog box displays.The status changes to Rejected. |  |

#### Service Bundle

##### Create Service Quotation

Purpose

Using the quick create option, you can create a service quotation. The service quotation will be in the Open state when it is created. The service quotation can be viewed and edited.

This scenario is a variant of a service quotation uses a service bundle. A service bundle consists of a main item and one or more subitems. The service bundle includes time and materials subitems as well as fixed price subitems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | The Create Service Quotation window displays. |  |
| 4 | Maintain Service Quotation Data | Make the following entries:Service Quotation Type: Service QuotationSold-To Party: for example, 33100003Description: <description>Requested Start Date - End Date: <date range>Product ID: for example. SRV_BUNDLE_02Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save. | A new service quotation is created with the status Open.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.Note If the service team concept has been enabled for the service quotation (SVQ1), a dialog box may appear and ask you to choose a service team.Select your service team.Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SQW1 (External Service SES). |  |
| 5 | Maintain Subitems | Under Items, make the following entries:Product ID: for example. SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRPress Enter.Make the following entries:Product ID: for example. SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAPress Enter.To add a fixed price subitem, make the following entries"Product ID: for example. SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRItem Category: SrvItem (FxPrc)Choose Save. | A service quotation with a service bundle is created. |  |

##### Send to Customer

Purpose

In this step, you send the quote to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003Status: Open | The service quotations are filtered based on your entries. |  |
| 4 | Send Quote to Customer | Choose your service quotation.On the Service Quotation screen, choose Send to Customer. | The service quotation is sent to the customer and the status changes to Sent to Customer. |  |

##### Change or Update Service Quotation

Purpose

In this step, you modify service quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Edit Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Edit. |  |  |
| 5 | Change Service Quotation | Make a change to a service quotation item and choose Save. | The changes are saved.The status changes to Under Review.Note Quotes under review can be sent to the customer or accepted. |  |

##### Accept Service Quotation

Purpose

In this step, you accept the service quotation. A service order is created once the quote is accepted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Accept Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Accept. | The status changes to Accepted.Note Accepted service quotes will automatically create a service order internally.Note down the service order number.Note Items in the quote can be partially accepted and the total quote amount will be adjusted according to total items accepted. |  |

##### Reject Service Quotation

Purpose

In this step, you reject service quotations that do not meet customer expectations or have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Reject Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Reject.In the Reject Quotation dialog box, make the following entries and choose Reject:Rejection Reason: for example, Rejected by Customer | The Reject Quotation dialog box displays.The status changes to Rejected. |  |

### Fixed Price Service Quotation

#### Fixed Price Item

##### Create Service Quotation

Purpose

Using the quick create option, you can create a fixed price service quotation. The service quotation will be in the Open state when it is created. The service quotation can be viewed and edited.

|  |
| --- |
| Note Service Quotation supports the following items:Service Product (SRV_01)Expense Product (SRV_02)Service Parts (SRV_03, SRV_04)Stock Service (SRV_05) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | The Create Service Quotation window displays. |  |
| 4 | Maintain Service Quotation Data | Make the following entries:Service Quotation Type: Service Quotation (Fixed Price)Sold-To Party: for example, 33100003Description: <description>Requested Start Date - End Date: <date range>Product ID: for example. SRV_01Quantity: for example, 1Unit: for example, HRPress Enter.Choose Save and Edit. | A new service quotation is created with the status Open.Note By default, the service item SRV_01 is a time and material item with item category SQP1.If you need to use a fixed price item instead of a time and material item, change the item category to SQP3 (Fixed Price) or SQW3 (External Service).Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.Note If the service team concept has been enabled for the service quotation (SVQ1), a dialog box may appear and ask you to choose a service team.Select your service team.Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SQW1 (External Service SES).Note If you enabled credit check management for service quotation and the service quotation is blocked by the credit, then please refer to scope item Advanced Credit Management (1QM) for information about resolving it. |  |
| 5 | Maintain a Fixed Price | Under Price Details, choose Add to insert a new Price Element.Choose Manual Doc. Amount (PMV0).Make the following entries:Price for example, 600Unit: AEDPress Enter.Choose Save . | A fixed price is maintained for the service quotation. |  |

##### Send to Customer

Purpose

In this step, you send the quote to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003Status: Open | The service quotations are filtered based on your entries. |  |
| 4 | Send Quote to Customer | Choose your service quotation.On the Service Quotation screen, choose Send to Customer. | The service quotation is sent to the customer and the status changes to Sent to Customer. |  |

##### Change or Update Service Quotation

Purpose

In this step, you modify service quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Edit Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Edit. |  |  |
| 5 | Change Service Quotation | Make a change to a service quotation item and choose Save. | The changes are saved.The status changes to Under Review.Note Quotes under review can be sent to the customer or accepted. |  |

##### Accept Service Quotation

Purpose

In this step, you accept the service quotation. A service order is created once the quote is accepted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Accept Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Accept. | The status changes to Accepted.Note Accepted service quotes will automatically create a service order internally.Note down the service order number.Note Items in the quote can be partially accepted and the total quote amount will be adjusted according to total items accepted. |  |

##### Create a Requote for Service Quotation

Purpose

In this step, you provide a requote during the service order review process. Services can be added if required. A new quotation is created, additional items are added, and the quotation is sent to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Requote | Choose your service quotation.On the Service Quotation screen, choose Requote.Note The Requote button is disabled if the follow-up service order has the status Completed. | The status changes to Open. |  |
| 5 | Edit Service Quotation | Choose Edit. |  |  |
| 6 | Add Item to Service Quotation | Under Items, make the following entries and choose Save:Product ID: for example. SRV_05Quantity: for example, 1Unit: for example, PC | The changes are saved. |  |
| 7 | Send to Customer | Chosse Send to Customer. | The status changes to Sent to Customer. |  |
| 8 | Accept Quotation | Choose Accept. | The status changes to Accepted. |  |
| 9 | Verify Service Order | Under Transaction History, choose the Service Order. | The service order contains the new item added through the requote process.Note The requote is only enabled if the service quotation is accepted and a follow-up service order is created. |  |

##### Reject Service Quotation

Purpose

In this step, you reject service quotations that do not meet customer expectations or have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Reject Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Reject.In the Reject Quotation dialog box, make the following entries and choose Reject:Rejection Reason: for example, Rejected by Customer | The Reject Quotation dialog box displays.The status changes to Rejected. |  |

#### Fixed Price Service Bundle

##### Create Service Quotation

Purpose

In this step, you create a fixed price service quotation containing a service bundle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Create Service Quotation | Choose Create Service Quotation > Quick Create . | The Create Service Quotation window displays. |  |
| 4 | Maintain Service Quotation Data | Make the following entries:Service Quotation Type: Service Quotation (Fixed Price)Sold-To Party: for example, 33100003Service Bundle: SelectedDescription: <description>Requested Start Date - End Date: <date range>Product ID: SRV_BUNDLE_01Quantity: for example, 1Unit: for example, EAChoose Save and Edit. | A new service quotation is created.Note If your sold-to party is associated with one or more service contracts, a new popup window will appear and ask you to select a contract per item. Select No Assignment.Note If the service team concept has been enabled for the service quotation (SVQ1), a dialog box may appear and ask you to choose a service team.Select your service team.Note Service material SRV_01 is usually assumed to be performed by an internal employee. If it must be procured from a 3rd party, scope item 3NI must be in scope. And you have to set the item category to SQW1 (External Service SES). |  |
| 5 | Maintain Subitems | Under Items, make the following entries:Product ID: for example, SRV_01Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, HRPress Enter.Make the following entries:Product ID: for example, SRV_02Higher-Level Item: <service bundle item number>Quantity: for example, 1Unit: for example, EAPress Enter.Choose Save. | A service quotation with a service bundle is created. |  |

##### Send to Customer

Purpose

In this step, you send the quote to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003Status: Open | The service quotations are filtered based on your entries. |  |
| 4 | Send Quote to Customer | Choose your service quotation.On the Service Quotation screen, choose Send to Customer. | The service quotation is sent to the customer and the status changes to Sent to Customer. |  |

##### Change or Update Service Quotation

Purpose

In this step, you modify service quotations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Edit Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Edit. |  |  |
| 5 | Change Service Quotation | Make a change to a service quotation item and choose Save. | The changes are saved.The status changes to Under Review.Note Quotes under review can be sent to the customer or accepted. |  |

##### Accept Service Quotation

Purpose

In this step, you accept the service quotation. A service order is created once the quote is accepted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Accept Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Accept. | The status changes to Accepted.Note Accepted service quotes will automatically create a service order internally.Note down the service order number.Note Items in the quote can be partially accepted and the total quote amount will be adjusted according to total items accepted. |  |

##### Reject Service Quotation

Purpose

In this step, you reject service quotations that do not meet customer expectations or have expired.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. |  |  |
| 2 | Access App | Open Manage Service Quotations - Overview (F4251). | The Manage Service Quotations screen displays. |  |
| 3 | Find Service Quotation | Make the following entries and choose Go:Sold-To Party: for example, 33100003 | The service quotations are filtered based on your entries. |  |
| 4 | Reject Service Quotation | Choose your service quotation.On the Service Quotation screen, choose Reject.In the Reject Quotation dialog box, make the following entries and choose Reject:Rejection Reason: for example, Rejected by Customer | The Reject Quotation dialog box displays.The status changes to Rejected. |  |

## Appendix

### Succeeding Scope Items

After completing the activities in this test script, you can continue testing the following scope items:

| Scope Item | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring |  |

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
> Flagged while digesting this document, not verified: Overview table for Service Bundle lists Accept and Reject expected results swapped (Accept says rejected, Reject says accepted); several overview sections reuse the same time-and-material description and links for different variants.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-solution-order-management]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4GA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 65,425 chars in the whole document
