---
id: 13-quality-ehs-and-compliance/health-and-safety-management-54a-ae-test-script-sap-s-4hana-cloud-publ
title: "Health and Safety Management (54A_AE) - Test Script, SAP S/4HANA Cloud Public Edition (54A_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 54A_AE Health and Safety Management: roles, sample data, and tests for chemical approvals, risk assessments, safety instructions."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/health-and-safety-and-occupational-health]
aliases: [54A_S4CLD2608_BPD_EN_AE]
keywords: [Health and Safety Management and Occupational Health, health and safety management, chemical approvals, manage use of chemicals, risk assessments, job hazard analysis, equipment safety instructions, substance safety instructions, hazardous substance inventory, hazardous substance overview]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54A_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1065
topic: 13-quality-ehs-and-compliance/health-and-safety-and-occupational-health
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Health and Safety Management (54A_AE) - Test Script, SAP S/4HANA Cloud Public Edition (54A_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54A_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Health and Safety Management and Occupational Health** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 25-09-26 |
| --- | --- |
|  | Health and Safety Management (54A_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc241657431)

[2 Prerequisites 4](#_Toc241657432)

[2.1 System Access 4](#_Toc241657433)

[2.2 Roles 4](#_Toc241657434)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc241657435)

[2.4 Preliminary Steps 6](#_Toc241657436)

[2.4.1 Create Jobs 6](#_Toc241657437)

[2.4.2 Create Locations 6](#_Toc241657438)

[2.4.3 Create Controls 9](#_Toc241657439)

[2.4.4 Create Compliance Purpose 11](#_Toc241657440)

[2.4.5 Activate Feature for AI-Assisted Creation of Safety Instructions for Substances and Equipment 12](#_Toc241657441)

[3 Overview Table 13](#_Toc241657442)

[4 Test Procedures 16](#_Toc241657443)

[4.1 Chemical Approvals 16](#_Toc241657444)

[4.1.1 Request a Chemical Approval 16](#_Toc241657445)

[4.1.2 Add Information to the Request 17](#_Toc241657446)

[4.1.3 Maintain Chemical Compliance View - Unpackaged Product 18](#_Toc241657447)

[4.1.4 Approve the Request 22](#_Toc241657448)

[4.1.5 Perform Follow-Up Activities 23](#_Toc241657449)

[4.2 Manage Use of Chemicals 24](#_Toc241657450)

[4.2.1 Search for Chemicals with Completed Approvals 24](#_Toc241657451)

[4.2.2 Request a New Location for the Chemical 25](#_Toc241657452)

[4.2.3 Check Required Activities for Newly Requested Location 26](#_Toc241657453)

[4.2.4 Perform Follow-Up Activities for the Newly Requested Location 27](#_Toc241657454)

[4.3 Risk Assessments 28](#_Toc241657455)

[4.3.1 Create and Edit a Risk Assessment 28](#_Toc241657456)

[4.3.2 Identify a Risk without Agent 29](#_Toc241657457)

[4.3.3 Identify a Risk with Chemical Agent 32](#_Toc241657458)

[4.3.4 Add an Attachment to the Risk Assessment 34](#_Toc241657459)

[4.3.5 Approve a Risk Assessment 35](#_Toc241657460)

[4.3.6 Create the Risk Assessment Summary Report 36](#_Toc241657461)

[4.3.7 Create a Follow-Up of the Risk Assessment 36](#_Toc241657462)

[4.4 Job Hazard Analyses 37](#_Toc241657463)

[4.4.1 Create and Edit a Job Hazard Analysis 37](#_Toc241657464)

[4.4.2 Create Job Steps 39](#_Toc241657465)

[4.4.3 Identify a Job-Based Risk 40](#_Toc241657466)

[4.4.4 Identify a Job-Based Chemical Risk 42](#_Toc241657467)

[4.4.5 Approve a Job Hazard Analysis 44](#_Toc241657468)

[4.4.6 Create the Job Hazard Analysis Summary Report 45](#_Toc241657469)

[4.4.7 Create a Follow-Up of the Job Hazard Analysis 45](#_Toc241657470)

[4.5 Safety Instructions for Equipment 46](#_Toc241657471)

[4.5.1 Create and Edit Safety Instructions for Equipment 46](#_Toc241657472)

[4.5.2 Release Safety Instructions for Equipment 48](#_Toc241657473)

[4.5.3 Print Safety Instructions for Equipment 49](#_Toc241657474)

[4.6 Safety Instructions for Substances 50](#_Toc241657475)

[4.6.1 Create and Edit Safety Instructions for Substances 50](#_Toc241657476)

[4.6.2 Release Safety Instructions for Substances 52](#_Toc241657477)

[4.7 Hazardous Substance Inventory 53](#_Toc241657478)

[4.7.1 Maintain Hazardous Substance Inventory 53](#_Toc241657479)

[4.7.2 View Hazardous Substance Inventory 54](#_Toc241657480)

[4.8 Hazardous Substance Overview 55](#_Toc241657481)

[4.8.1 Get an Overview of Hazardous Substances in the Company 55](#_Toc241657482)

[4.9 Workplace Safety Overview 56](#_Toc241657483)

[4.9.1 Get an Overview of Workplace Safety in the Company 56](#_Toc241657484)

[4.10 View My Workplace Safety 57](#_Toc241657485)

[4.10.1 Get an Overview of Workplace Safety at my Location for my Job 57](#_Toc241657486)

## Purpose

Overview

This scope item helps you to provide a safe workplace for your employees via different processes. You can create requests for the approval of a new chemical in your company as well as view and manage these requests. Furthermore, you can maintain a hazardous substance inventory to keep track of all chemicals used in your organization. You can also create and manage risk assessments and job hazard analyses to identify, analyze, evaluate, and treat any health or safety risks in your responsible areas. You can also provide employees with safety-relevant information for their individual workplace and with safety instructions for handling different equipment or substances. These processes help that your company always stays up to date with safety standards and regulations.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend that the Business Process Configuration Expert in your organization upgrade the configuration content and deploy the configuration data to your system landscape.

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
| Industrial Hygienist | SAP_BR_INDUSTRIAL_HYGIENIST | Workplace Safety | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| Employee - EHS Info | SAP_BR_EMPLOYEE_EHS_INFO |  |  |  |
| Hazardous Materials Manager | SAP_BR_HAZMAT_MANAGER | Hazardous Substance Management | SAP_EHS_SPT_HAZMAT_MGMT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Jobs

A set of safety instructions refers to a certain job (among other things).

A risk assessment of the type Job Hazard Analysis is also performed for a specific job.

In the context of workplace safety, a job is an activity that a person does within the workplace. In the system, jobs can be chosen from a list of existing entries that are predefined in your configuration environment.

To create a job, follow the steps in the Create Jobs section.

Equipment

The app allows you to choose from a predefined list of equipment.

Locations

Locations represent the physical places or areas where a certain safety instruction or risk assessment or chemical approval is valid. In the real world, they represent workshops, departments or factories.

Create a small location hierarchy by following the next steps in [Create Locations](#unique_6) [page ] 6.

Controls

Controls are measures that are applied on an ongoing basis to prevent damages or harm from taking place. A control can be applied, for example, as a policy, practice, or in the form of a device.

You can create several controls by following the steps in the [Create Controls](#unique_7) [page ] 9 section.

Compliance Purpose

A compliance purpose is a set of compliance requirements that are relevant to an application within a particular country/region. You can use a compliance purpose to group compliance requirements that apply to a specific business process, such as handling chemical substances.

A compliance requirement is a regulation or policy that companies must comply with to fulfill regulatory or company standards, such as GHS classification and GHS substance labeling, or defining measures for personal protection.

You can create a compliance purpose by following the steps in the [Create Compliance Purpose](#unique_8) [page ] 11 section.

### Preliminary Steps

#### Create Jobs

You need to create the following job before you begin the test procedures.

Create a New Job: Welding

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Select Workplace Safety - Operational Risk Management and start the Manage Jobs app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Job | Choose Create Job. |  |  |
| 4 | Enter Relevant Data | Enter the following data:Job: WeldingJob Type: Job |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

#### Create Locations

The following steps assume that there are no locations in your system yet. If there are already locations, you can skip this section. In this case, in the following sections, choose one of the already existing locations under which you want to create the two new production units.

Create a Location Representing the Company

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Locations (EHFND_UI_LOC_ENTRY) app. | The initial screen of the app is displayed. |  |
| 3 | Edit Location Structure | Choose Edit Location Structure. |  |  |
| 4 | Create a New Location Structure | Choose New. | A dialog to enter the relevant information is displayed. |  |
| 5 | Enter Relevant Data | Enter the following data:Location: UXT InnoCorpLocation Type: CompanyRevision Start Date: <today's date> |  |  |
| 6 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered. |  |  |
| 7 | Return to Location Structure | Choose Return to Location Structure. |  |  |
| 8 | Choose Created Location | Choose Set Status and select Active. Choose Save. |  |  |

Create Production Line A

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Location | Select the previously created location UXT InnoCorp.If you don’t see this location, choose Show All Locations first. |  |  |
| 2 | Create a New Production Line | Choose New.This creates a new location hierarchically below the selected location. | A dialog to enter the relevant information is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Location: Production Line ALocation Type: Production UnitRevision Start Date: <today's date>Plant ID: 3310 |  |  |
| 4 | Enter Person Responsible | On the tab Persons Responsible, make the following entries:Name: Enter your own business user.Role: Hazardous Substance ManagerName: Enter your own business user.Role: Environmental ManagerName: Enter your own business user.Role: Industrial HygienistName: Enter your own business user.Role: First AiderName: Enter your own business user.Role: Emergency Officer |  |  |
| 5 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered. |  |  |
| 6 | Return to Location Structure | Choose Return to Location Structure. |  |  |
| 7 | Choose Created Location | Choose Set Status and select Active. Choose Save. |  |  |

Create Production Line B

Repeat the steps from the previous procedure using the location name Production Line B.

Create Equipment: Welding Machine

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Location Production Line A | Select the previously created location Production Line A. If you do not see this location, choose Show All Locations first. |  |  |
| 2 | Create a New Equipment | Choose New.This creates a new location hierarchically below the selected location. | A dialog to enter the relevant information is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Location: Welding MachineLocation Type: EquipmentRevision Start Date: <today's date>Plant ID:1710 |  |  |
| 4 | Save Your Entries | Choose Save.You can ignore the warning that no country/region was entered. |  |  |
| 5 | Return to Location Structure | Choose Return to Location Structure. |  |  |
| 6 | Choose Created Location | Choose Set Status and select Active. Choose Save. |  |  |

#### Create Controls

You need to create the following four controls before you begin the test procedures.

Create a New Control: Flexible Sound Barriers

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Select Workplace Safety - Operational Risk Management and start the Edit Control Master Data app. | The initial screen of the app is displayed. |  |
| 3 | Select a Control Catalog | Expand the Engineering control type, then expand the Encapsulation control subtype. Select the Acoustic Barriers control catalog. |  |  |
| 4 | Add a New Control | Choose Add. | The form for defining a new control is displayed. |  |
| 5 | Enter Relevant Data | Enter the following data:Control Name: Flexible Sound BarriersDesired Effect: Lower Severity |  |  |
| 6 | Save Your Entries | Choose Save. |  |  |

Create a New Control: Scheduled Safety Inspection

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select a Control Catalog | Expand the Administrative control type, then expand the Inspections control subtype. Select the Scheduled Inspections control catalog. |  |  |
| 2 | Add a New Control | Choose Add. | The form for defining a new control is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Control Name: Scheduled Safety InspectionDesired Effect: Lower Likelihood |  |  |
| 4 | Save Your Entries | Choose Save. |  |  |

Create a New Control: Stress Relief Training

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select a Control Catalog | Expand the Administrative control type, then expand the Procedures control subtype. Select the Policy control catalog. |  |  |
| 2 | Add a New Control | Choose Add. | The form for defining a new control is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Control Name: Stress Relief TrainingDesired Effect: Lower Severity |  |  |
| 4 | Save Your Entries | Choose Save. |  |  |

Create a New Control: Neoprene Safety Gloves

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select a Control Catalog | Expand the Person-Related control type, then expand the Personal Protective Equipment control subtype. Select the Hand Protection control catalog. |  |  |
| 2 | Add a New Control | Choose Add. | The form for defining a new control is displayed. |  |
| 3 | Enter Relevant Data | Enter the following data:Control Name: Neoprene Safety GlovesDesired Effect: Lower Severity |  |  |
| 4 | Save Your Entries | Choose Save. |  |  |

#### Create Compliance Purpose

A compliance purpose is a set of compliance requirements that apply to the same application in the same countries or regions. You can use compliance purposes to group compliance requirements to support a specific business process such as handling chemical substances. A compliance requirement is a regulation or policy that companies must adhere to in order to fulfill regulatory or company standards such as the GHS classifications and GHS labeling of substances or the definition of personal protection measures.

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Start the Manage Compliance Purposes (F2632) app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Compliance Purpose | Choose Create. |  |  |
| 4 |  | Under section Compliance Purpose Names, choose Create. | A dialog to enter the relevant information is displayed. |  |
| 5 | Enter Relevant Data | Enter the following data:Language = ENName = Handled in company |  |  |
| 6 | Add Compliance Requirements | Under section Compliance Requirements, choose Add. |  |  |
| 7 | Select Relevant Compliance Requirements | Select the following Compliance Requirements:World-Accidental ReleaseWorld-Firefighting MeasuresWorld-First Aid MeasuresWorld-GHS ClassificationWorld-Personal ProtectionWorld-UN Hazardous Ingredients |  |  |
| 8 |  | Choose Create. |  |  |
| 9 |  | Choose Activate. |  |  |

#### Activate Feature for AI-Assisted Creation of Safety Instructions for Substances and Equipment

You need to activate the feature in your test system before you can use the help of artificial intelligence (AI) to generate safety instructions for substances and equipment.

Activate Feature for AI Assistance

To activate the AI feature, the following steps must be performed:

- Activate the following feature toggles:
    - FTGL_EHSPROD_19937_AI (SI Substances)
    - FTGL_EHSPROD_17404_AI (SI Equipment)
- Assign the following IAM app variants to your business role:
    - F3857A_AI_TRAN (Manage Safety Instructions - Substances (AI))
    - F4425_AI_TRAN (Manage Safety Instruction - Equipment (AI))

## Overview Table

This scope item consists of several process steps provided in the following tables.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage only contains the apps necessary to perform the typical tasks of a business role.

You can use the search bar to find all other apps that are not included on the homepage.

If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.

Table 1: Chemical Approvals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Request a Chemical Approval](#unique_12) [page ] 16 | Hazardous Materials Manager | Request Chemical Approval |  |
| [Add Information to the Request](#unique_13) [page ] 17 | Hazardous Materials Manager | Request Chemical Approval |  |
| [Maintain Chemical Compliance View - Unpackaged Product](#unique_14) [page ] 18 | Hazardous Materials Manager | Request Chemical Approval |  |
| [Approve the Request](#unique_15) [page ] 22 | Hazardous Materials Manager | Request Chemical Approval |  |
| [Perform Follow-Up Activities](#unique_16) [page ] 23 | Hazardous Materials Manager | Request Chemical Approval |  |

Table 2: Manage Use of Chemicals

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Search for Chemicals with Completed Approvals](#unique_17) [page ] 24 | Hazardous Materials Manager | Manage Use of Chemicals (F8658) |  |
| [Request a New Location for the Chemical](#unique_18) [page ] 25 | Hazardous Materials Manager | Manage Use of Chemicals (F8658)l |  |
| [Check Required Activities for Newly Requested Location](#unique_19) [page ] 26 | Hazardous Materials Manager | Manage Chemical Approvals (F3406) |  |
| [Perform Follow-Up Activities for the Newly Requested Location](#unique_20) [page ] 27 | Hazardous Materials Manager | Manage Chemical Approvals (F3406) |  |

Table 3: Risk Assessments

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Edit a Risk Assessment](#unique_21) [page ] 28 | Industrial Hygienist | Manage Risk Assessments (F7348) | A risk assessment is created, and basic information is maintained. |
| [Identify a Risk without Agent](#unique_22) [page ] 29 | Industrial Hygienist | Manage Risk Assessments (F7348) | Risks are identified and assessed. Controls are added. |
| [Identify a Risk with Chemical Agent](#unique_23) [page ] 32 | Industrial Hygienist | Manage Risk Assessments (F7348) | Chemical risks are identified and assessed. Controls are added. |
| [Add an Attachment to the Risk Assessment](#unique_24) [page ] 34 | Industrial Hygienist | Manage Risk Assessments (F7348) | An attachment was added to the risk assessment. |
| [Approve a Risk Assessment](#unique_25) [page ] 35 | Industrial Hygienist | Manage Risk Assessments (F7348) | The risk assessment has the status Approved. |
| [Create the Risk Assessment Summary Report](#unique_26) [page ] 36 | Industrial Hygienist | Manage Risk Assessments (F7348) | You have created the Risk Assessment Summary Report. |
| [Create a Follow-Up of the Risk Assessment](#unique_27) [page ] 36 | Industrial Hygienist | Manage Risk Assessments (F7348) | A new revision for the risk assessment was created. |

Table 4: Job Hazard Analyses

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Edit a Job Hazard Analysis](#unique_28) [page ] 37 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | A job hazard analysis is created, and basic information is maintained. |
| [Create Job Steps](#unique_29) [page ] 39 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | Job steps are created. |
| [Identify a Job-Based Risk](#unique_30) [page ] 40 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | Risks are identified and assessed. Controls are added. |
| [Identify a Job-Based Chemical Risk](#unique_31) [page ] 42 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | Chemical risks are identified and assessed. Controls are added. |
| [Approve a Job Hazard Analysis](#unique_32) [page ] 44 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | The job hazard analysis has the status Approved. |
| [Create the Job Hazard Analysis Summary Report](#unique_33) [page ] 45 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | You have created the Job Hazard Summary Report. |
| [Create a Follow-Up of the Job Hazard Analysis](#unique_34) [page ] 45 | Industrial Hygienist | Manage Job Hazard Analyses (F7896) | A new revision for the job hazard analysis was created. |

Table 5: Safety Instructions for Equipment

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Edit Safety Instructions for Equipment](#unique_35) [page ] 46 | Industrial Hygienist | Manage Safety Instructions - Equipment (F4425) | The chapters of the safety instructions are filled with text, and some symbols are added. |
| [Release Safety Instructions for Equipment](#unique_36) [page ] 48 | Industrial Hygienist | Manage Safety Instructions - Equipment (F4425) | The safety instructions are in status Released. As a result, the generated document from the next step no longer shows an In Process watermark. |
| [Print Safety Instructions for Equipment](#unique_37) [page ] 49 | Industrial Hygienist | Manage Safety Instructions - Equipment (F4425) | You have printed safety instructions. |

Table 6: Safety Instructions for Substances

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create and Edit Safety Instructions for Substances](#unique_38) [page ] 50 | Industrial Hygienist | Manage Safety Instructions - Substances (F3857A) | The chapters of the safety instructions are filled with text, and some symbols are added. |
| [Release Safety Instructions for Substances](#unique_39) [page ] 52 | Industrial Hygienist | Manage Safety Instructions - Substances (F3857A) | The safety instructions are in status Released. As a result, the generated document from the next step no longer shows an In Process watermark. |

Table 7: Hazardous Substance Inventory

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Hazardous Substance Inventory](#unique_40) [page ] 53 | Hazardous Materials Manager | Maintain Hazardous Substance Inventory (F9318) | A sub-inventory is created, maintained, and released. |
| [View Hazardous Substance Inventory](#unique_41) [page ] 54 | Hazardous Materials Manager | View Hazardous Substance Inventory (F9317) | The inventory items are displayed with hazardous substance information. |

Table 8: Hazardous Substance Overview

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Get an Overview of Hazardous Substances in the Company](#unique_42) [page ] 55 | Hazardous Materials Manager | Hazardous Substance Overview (F8620) |  |

Table 9: Workplace Safety Overview

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Get an Overview of Workplace Safety in the Company](#unique_43) [page ] 56 | Industrial Hygienist | Workplace Safety Overview (F7512) |  |

Table 10: View My Workplace Safety

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Get an Overview of Workplace Safety at my Location for my Job](#unique_44) [page ] 57 | Employee - EHS Info | View My Workplace Safety (F8791) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Chemical Approvals

#### Request a Chemical Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Since hazardous substances pose a certain chemical hazard potential, they should generally be used as little as possible. However, sometimes the use of hazardous substances in the company cannot be avoided. If this is the case and the procurement of hazardous substances is necessary, some measures must be taken in advance.

A new chemical is to be introduced in the company. This step requests the approval for this new chemical.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space, and open the Manage Use of Chemicals app in the Hazardous Substances section.On top of the result list, choose Request New Chemical. | The initial screen of the app is displayed. |  |
| 3 | Enter Basic Information | Enter or select the following data:Name of Chemical: AcetoneLocation: Production Line APurposes: Choose Add and enter Surface CoatingMethods of Use: Choose Add and enter SprayingExpected Consumption: 1 L Monthly | All fields are filled in. |  |
| 4 | Enter Date Information | Under Proposed Dates, enter the following data:Duration/Reversal: PermanentDate: <today>. | All fields are filled in. |  |
| 5 | Add Safety Data Sheet Document | Upload the PDF document in the Attachments section. | The document is attached. |  |
| 6 | Save Your Entries | Select Save and Submit. | The request is created. |  |

#### Add Information to the Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Since hazardous substances pose a certain chemical hazard potential, they should generally be used as little as possible. However, sometimes the use of hazardous substances in the company cannot be avoided. If this is the case and the procurement of hazardous substances is necessary, some measures must be taken in advance.

A new chemical is to be introduced in the company. This step adds the needed information for an approval for this new chemical.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Create Chemical | In the Activity section, select the activity Provide Chemical and Information.Choose Edit.Answer the following questions in the Specify Chemical Attributes section:Is the chemical purchased or produced?ProducedIs the chemical a substance or a mixture?SubstanceThen choose the Create Chemical button. |  |  |
| 2 | Check and Add Information | In the same activity, Provide Chemical and Information, check the boxes in the Approval Request Requirement section, and answer the questions with “Yes”.If a mandatory comment is needed, enter a comment.Choose Save.Choose Edit.Set activity to completed.Choose Save. | The activity was completed. |  |
| 3 | Maintain the Chemical Compliance View | In the same activity, in the Reference section, choose the link for the chemical object to navigate into the Manage Basic Compliance Data - Unpackaged Products app. |  |  |

#### Maintain Chemical Compliance View - Unpackaged Product

Compliance views are objects which represent a substance and its chemical aspects (like boiling point) as well as its regulatory aspects (like GHS classification). The Compliance view is the technical successor for the EHS business object Chemical.

As such, substances usually extend the information about products (formerly known as materials) in the SAP system, they are referred to as unpackaged product (for bulk or raw materials) and packaged products (usually packaged finished materials).

For this test script, we only need one compliance view of type unpackaged product.

Assign Purpose

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Compliance View for the Chemical | Select the previously created compliance view for the chemical Acetone. |  |  |
| 2 |  | Choose Edit. |  |  |
| 3 |  | Choose tab Application, Uses, Markets and Purposes. |  |  |
| 4 | Enter Relevant Data | Under section Assigned Compliance Purposes, select all automatically assigned default purposes. |  |  |
| 5 |  | Choose Remove. |  |  |
| 6 |  | Choose Remove again. |  |  |
| 7 |  | Choose Add. |  |  |
| 8 |  | Select the previously created compliance purpose. |  |  |
| 9 |  | Choose OK. |  |  |
| 10 |  | Select purpose SDS for CA, DE, FR, MX, US. |  |  |
| 11 |  | Choose OK. |  |  |
| 12 | Save Your Entries | Choose Save. |  |  |

Maintain Safety Instruction Relevant Data

Assign Related Products in Product Master

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Compliance View for the Chemical | Select the previously created compliance view for the chemical the Acetone. |  |  |
| 2 |  | Choose Edit. |  |  |
| 3 |  | Choose tab Assigned Products. |  |  |
| 4 |  | Select a suitable product in the product master section with the value help.If all available products are already assigned to a specific compliance view, you need to create a new product in the Manage Product Master Data app. For this, the Master Data Specialist - Product Data (SAP_BR_PRODMASTER_SPECIALIST) business role needs to be assigned to your user.Open the app and, in the Create dialog box, select Product. Under Product Type, choose Finished Product (FERT). Next, choose Liter (L) in the Base Unit field. Add a suitable text in the Description field and choose Go. You can then go back and select the product in the product master section with the value help. |  |  |
| 5 | Save Your Entries | Choose Save.You can ignore the warning.Choose Close. |  |  |

Instructions for Maintaining SDS Relevant Information of the Compliance View

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Compliance View for the Chemical | Select the previously created compliance view for the chemical Acetone. |  |  |
| 2 |  | Choose View Compliance Assessments.Each compliance assessment evaluates one compliance object (product, raw material, supplier raw material, or substance) against one compliance requirement. |  |  |
| 3 |  | Switch to tab Safety Data Sheet Assessment, section Safety Data Sheet: Related Assessments. |  |  |
| 4 |  | Select the compliance requirement World Accidental Release Measures. |  |  |
| 5 |  | Choose Edit. |  |  |
| 6 |  | Choose Add in the Environmental Precautions section. |  |  |
| 7 |  | Select relevant phrases. |  |  |
| 8 |  | Choose OK. |  |  |
| 9 |  | Repeat steps 6 to 8 for each relevant section within the compliance requirement. |  |  |
| 10 | Save Your Entries | Choose Save. |  |  |
| 11 |  | Choose Release. |  |  |
| 12 |  | Choose Back and return to the compliance assessment. |  |  |
| 13 |  | Repeat steps 4 – 10 for all relevant compliance requirements. |  |  |

Instructions for Maintaining SDS documents in the Compliance View

| Step | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Previously Created Compliance View for the Chemical | Select the previously created compliance view for the chemical Acetone. |  |  |
| 2 |  | Choose View Compliance Assessments.Each compliance assessment evaluates one compliance object (product, raw material, supplier raw material, or substance) against one compliance requirement. |  |  |
| 3 |  | Switch to tab Safety Data Sheet Assessment, section Safety Data Sheet Assessments. |  |  |
| 4 |  | Select the compliance requirement US Safety Data Sheet. |  |  |
| 5 |  | Choose Edit. |  |  |
| 6 |  | Select entry for language English in the Safety Data Sheets table. |  |  |
| 7 |  | Enter Major Version: 1.Enter Subversion: 0.Upload an attachment. |  |  |
| 8 |  | Choose Save. |  |  |
| 9 |  | Choose Release. |  |  |

|  |
| --- |
| Note The sections differ from compliance requirement to compliance requirement. Environmental precautions was one example for the compliance requirement accidental release measures and do not exist for other compliance requirements. |

#### Approve the Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Since hazardous substances pose a certain chemical hazard potential, they should generally be used as little as possible. However, sometimes the use of hazardous substances in the company cannot be avoided. If this is the case and the procurement of hazardous substances is necessary, some measures must be taken in advance.

A new chemical is to be introduced in the company.

In this step, the hazardous materials manager and the environmental manager must approve the new requested chemical.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App. | Go to the Hazardous Substance Management launchpad space, and open the Manage Chemical Approvals app in the Chemical Approval section. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Chemical Approval Request | Using the search field, search for Acetone.Select the Acetone in the result list. | You are being navigated to the chemical approval request. |  |
| 4 | Hazardous Materials Manager: Approve. | In the Activities section, choose the activity for the approval by the Hazardous Materials Manager.Choose Edit.Add a description.Choose Approve and Save. | Approval by the Hazardous Materials Manager is completed. |  |
| 5 | Environmental Manager: Approve. | In the Activities section, choose the activity for approval by the Environmental Manager.Choose Edit.Add a description.Choose Approve and Save. | Approval by the Environmental Manager is completed. |  |

#### Perform Follow-Up Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Since hazardous substances pose a certain chemical hazard potential, they should generally be used as little as possible. However, sometimes the use of hazardous substances in the company cannot be avoided. If this is the case and the procurement of hazardous substances is necessary, some measures must be taken in advance.

A new chemical is to be introduced in the company.

In this step, the follow-up activities for the newly requested chemical are triggered.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space, and open the Manage Chemical Approvals app in the Chemical Approval section. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Chemical Approval Request | Using the search field, search for Acetone.Select the Acetone in the result list. | You are being navigated to the chemical approval request. |  |
| 4 | Industrial Hygienist: Update Risk Assessment. | In the Activities section, choose the activity for updating the risk assessment.In the Follow-Up Activities section, check the task Risk assessment was created or updated.Set activity to completed.Choose Save. | Follow-up activities are completed.The chemical request is completed. |  |

### Manage Use of Chemicals

#### Search for Chemicals with Completed Approvals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Hazardous Materials Manager has to search for the chemicals to get an overview about existing approvals and rejections to enhance or restrict the approvals.

This step gives an overview of all chemicals with a completed approval process.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the Manage Use of Chemicals app in the Hazardous Substances section. | The initial screen of the app is displayed. |  |
| 3 | Search for a Chemical | Search for the chemical Acetone. | A result list is displayed. |  |
| 4 | Display Locations for the Chemical Acetone | Select the chemical Acetone in the result list. | The list of locations a chemical approval request was performed for is displayed. |  |
| 5 | Display Use Information for Chemical Acetone at Location Production Line A | Select location Production Line A. | Use information is displayed. |  |
| 6 | Check the Use Information | Expected Consumption: 1 L MonthlyPurposes: Surface CoatingMethods of Use: Spraying |  |  |
| 7 | Display Safety Data Sheet | In the Safety Data Sheets section, select the displayed safety data sheet to access it.Navigate back. | Safety Data Sheet Assessment opens with the possibility to display the PDF document. |  |
| 8 | Check Chemical Approval Request Information | In the Related Chemical Approvals section, the request is displayed with the possibility to navigate into it. |  |  |

#### Request a New Location for the Chemical

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The hazardous substance manager needs to search for the chemicals to get an overview about existing approvals and rejections to enhance or restrict the approvals.

This step requests a new location for the already approved chemical.

Procedure

Table 11:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the Manage Use of Chemicals app in the Hazardous Substances section. | The initial screen of the app is displayed. |  |
| 3 | Search for a Chemical | Search for the chemical Acetone. | A result list is displayed. |  |
| 4 | Display Locations for the Chemical Acetone | Select the chemical Acetone in the result list. | The list of locations a chemical approval request was performed for is displayed. |  |
| 5 | Request a New Location for the Chemical | Choose Request New Location on top of the location list.A dialog opens.In the value help, select the following Location: Production Line B.Under Expected Consumption, enter value, unit, period.Select Permanent.As Start Date, enter Today.Select Method of Use: Rinsing.Select Purpose: Surface Coating.Choose Create. | A new approval request is created. |  |

#### Check Required Activities for Newly Requested Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The hazardous materials manager needs to search for the chemicals to get an overview of existing approvals and rejections to enhance or restrict the approvals.

The request for a new location was created.

In this step, the hazardous materials manager checks which activities are necessary to roll out the use of this chemical to the new location.

Procedure

Table 12:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the Manage Chemical Approvals app in the Chemical Approval section. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Approval Request | Using the location value help, search for Production Line B.Select the request in the result list. | You are being navigated to the chemical approval request. |  |
| 4 | Check Activities | In the Activities section, choose the Provide Information activity to check the activities needed.Choose Edit.In the Approval Request Requirements questionnaire, check the Request Information is complete box, and answer the question Are additional approvers required? with No.Choose Complete and Save. | Approval by the Hazardous Materials Manager is completed. |  |

#### Perform Follow-Up Activities for the Newly Requested Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The hazardous materials manager needs to search for the chemicals to get an overview of existing approvals and rejections to enhance or restrict the approvals.

The request for a new location was created.

In this step, the follow-up activities for the newly requested location are triggered.

Procedure

Table 13:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the Manage Chemical Approvals app in the Chemical Approval section. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Approval Request | Using the location value help, search for Production Line B.Select the request in the result list. | You are being navigated to the chemical approval request. |  |
| 4 | Industrial Hygienist: Update Risk Assessment | In the Activities section, choose the activity for updating the risk assessment.Choose Edit.In the Follow-Up Activities section, check the task Risk assessment was created or updated.Set the activity to completed and choose Save. | The follow-up activities are completed.The chemical request is completed with status Approved. |  |

### Risk Assessments

#### Create and Edit a Risk Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to create such a risk assessment in the system.

This step creates a new risk assessment and maintains the basic information.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348)app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Risk Assessment | Select Create. | A dialog to enter the relevant information is displayed. |  |
| 4 | Enter Relevant Data | Enter the following data in the dialog:Assessment Type: HealthChoose Continue. | A new risk assessment is created and opens for further editing. |  |
| 5 | Enter Basic Information | Under Basic Information, enter the following data:Title: Risk Assessment for Production Line ALocations: Production Line ADescription: <Enter meaningful text> | All mandatory fields are filled in. |  |
| 6 | Enter Assessment Reason | Under Assessment Reason, enter the following data:Reason: <Enter meaningful text> | Reason maintained. |  |
| 7 | Save Your Entries | Select Create. | The newly created risk assessment is shown in Display Mode. |  |

#### Identify a Risk without Agent

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to identify risks during a risk assessment.

This step creates a new risk assessment and maintains the basic information.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348)app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are navigated to the details screen of the risk assessment. |  |
| 4 | Go to Edit Mode | Select Edit. | The risk assessment is now editable. |  |
| 5 | Identify a Risk | Under Risks, choose Identify Risk. In the dialog, select Without Agents and enter the following data:Locations: [No Change]Operational Status: Normal OperationHazard: BurnoutSelect Add. | The risk is displayed in the risk list. |  |
| 6 | Assess Risk - Description | Select the new risk from the risk list to expand its details. Enter a meaningful text into the Description field. |  |  |
| 7 | Assess Risk - Impacts | Under Impacts, select Stress from the value help. | The risk's impact is displayed. |  |
| 8 | Assess Risk - Risk Analysis | Under Risk Analysis, choose a value from the matrix.Below the risk matrix, select a Risk Level Effect. | The risk level is displayed. |  |
| 9 | Assess Risk - Catalog Controls | Under Controls, select Add Catalog Control.A wizard opens.Navigate through the first three steps: Engineering, Administrative, and Person-Related.In each step, expand the tree and select the available control.On the last screen of the wizard, select Add Controls to List. | Controls are displayed for the risk. |  |
| 9.1 | Assess Risk - Custom Controls | Under Controls, select Add Custom Control.A dialog opens. Enter the following data:Name: Enter a meaningful name.Description: Enter a meaningful text.Catalog: Select a catalog.Desired Effect: Lower SeveritySelect Add. | The control is displayed for the risk. |  |
| 10 | Create Task for Control | Select the first control from the list to expand its details. Enter a meaningful text into the Description field.Under Tasks, click Add Task. Select task type Task.In the new screen, enter the following data:Title: Enter a meaningful text.Assignee: Enter your own user.Select Create and navigate back. | The task is created for the control. |  |
| 11 | Implement Control | Select the Set to Implemented button. A warning that comes up if there are any open tasks serves informational purposes only. Do the same for the other controls, too.Select Apply to close the Details pane. | All controls receive the Implemented status. |  |
| 12 | Assessment Done | Select Assessment Done (near the top of the screen). Choose Confirm. | The status of the risk becomes Assessment Done. |  |
| 13 | Save Your Entries. | Select Save. | The risk assessment is shown in Display Mode. |  |

#### Identify a Risk with Chemical Agent

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to identify chemical risks during a risk assessment.

This step creates a new chemical risk.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348)app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are navigated to the details screen of the risk assessment. |  |
| 4 | Go to Edit Mode | Select Edit. | The risk assessment is now editable. |  |
| 5 | Identify a Chemical Risk | Under Risks, choose Identify Risk. In the dialog, select With Chemical Agents and enter the following data:Locations: [No Change]Operational Status: Normal OperationChemical: AcetoneMethod of Use: PouringHazard: Skin/EyeSelect Add. | The risk is displayed in the risk list. |  |
| 6 | Assess Risk - Description | Select the new risk from the risk list to expand its details. Enter a meaningful text into the Description field. |  |  |
| 7 | Assess Risk - Catalog Controls | Under Controls, select Add Catalog Control.A wizard opens.Navigate through the first three steps: Engineering, Administrative, and Person-Related.In each step, expand the tree and select the available control.On the last screen of the wizard, select Add Controls to List. | The controls are displayed for the risk. |  |
| 7.1 | Assess Risk - Custom Controls | Under Controls, select Add Custom Control.A dialog opens. Enter the following data:Name: Enter a meaningful name.Description: Enter a meaningful text.Catalog: Select a catalog.Desired Effect: Lower SeveritySelect Add. | Controls are displayed for the risk. |  |
| 8 | Create Task for Control | Select the first control from the list to expand its details. Enter a meaningful text into the Description field.Under Tasks, click Add Task. Select task type Task.In the new screen, enter the following data:Title: Enter a meaningful text.Assignee: Enter own user.Select Create and navigate back. | The control is displayed for the risk. |  |
| 9 | Implement Control | Select the Set to Implemented button. A warning that comes up if there are any open tasks serves informational purposes only. Do the same for the other controls, too.Select Apply to close the Details pane. | All controls receive the Implemented status. |  |
| 10 | Assessment Done | Select Assessment Done (near the top of the screen). | The status of the risk becomes Assessment Done. |  |
| 11 | Save Your Entries. | Select Save. | The risk assessment is shown in Display Mode. |  |

#### Add an Attachment to the Risk Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. Consequently, they need to do operational risk assessments. This test procedure shows how an attachment can be added to the operational risk assessment.

This step adds an attachment to the risk assessment.

Procedure

Table 14:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are being navigated to the details screen. |  |
| 4 | Go to Edit Mode | Select Edit. | The risk assessment is editable now. |  |
| 5 | Attachments | Under Attachments, select Upload and select a document.In the Add Document by Upload dialog, provide the following information:Type: Attachments.Select Add. | An attachment was added to the risk assessment. |  |
| 6 | Save Your Entries | Select Save. | The risk assessment is shown in display mode. |  |

#### Approve a Risk Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. Consequently, they need to do operational risk assessments. This test procedure shows how an operational risk assessment is approved.

This step sets the status of the risk assessment to Approved.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348)app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are navigated to the details screen. |  |
| 4 | Approve the Risk Assessment | Select Approve. | A confirmation dialog is displayed. |  |
| 5 | Set a Reminder | Activate Send Reminder for Reevaluation by Email. | Reminder for reevaluation is displayed. |  |
| 6 | Pick A Date | As date, select the day after tomorrow. |  |  |
| 7 | Confirm the Approval |  | The risk assessment is approved. |  |

#### Create the Risk Assessment Summary Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. For this purpose, they must perform operational risk assessments. This test procedure shows how to generate and print a risk assessment summary report.

This step creates the risk assessment summary report.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page and open the Manage Risk Assessments app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are being navigated to the details screen. |  |
| 4 | Display the Risk Assessment Summary Report | Choose Display Report. | A browser page is shown with the generated PDF document. |  |

#### Create a Follow-Up of the Risk Assessment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. For this purpose, they must perform operational risk assessments. This test procedure shows how to create a follow-up for a risk assessment.

This step creates a new revision of the risk assessment.

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On. | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Risk Assessments (F7348)app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Risk Assessment | Using the search field, search for Risk Assessment for Production Line A. | You are being navigated to the details screen. |  |
| 4 | Create a Follow-Up | Choose Follow-Up.In the dialog, select OK.If a Warnings dialog is displayed, just select Follow-Up to continue.In the Follow-Up Created dialog, select Go to Follow-Up. | A new revision of the risk assessment is created and displayed to the user in edit mode. |  |
| 5 | Save Your Entries | Select Save. | The newly created revision of the risk assessment is shown in display mode. |  |

### Job Hazard Analyses

#### Create and Edit a Job Hazard Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to create a job-based risk assessment, a job hazard analysis, in the system.

This step creates a new job hazard analysis and maintains the basic information.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Job Hazard Analysis | Select Create. | A dialog to enter the relevant information is displayed. |  |
| 4 | Enter Relevant Data | Enter the following data in the dialog:Type: Job Hazard AnalysisChoose Continue. | A new job hazard analysis is created and opens for further editing. |  |
| 5 | Enter Basic Information | Under General Information, enter the following data:Title: Job: Welding for Production Line ALocations: Production Line AJob: WeldingJob Description: <Enter meaningful text>Title of Performing Employee: Welder | All mandatory fields are filled in. |  |
| 6 | Save Your Entries | Select Create. | The newly created job hazard analysis is shown in display mode. |  |

#### Create Job Steps

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to create job steps during a job hazard analysis in the system.

This step creates new job steps for the job hazard analysis.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Use the search field to search for Job: Welding for Production Line A. | You are navigated to the details screen of the job hazard analysis. |  |
| 4 | Go to Edit Mode | Select Edit. | The job hazard analysis is now editable. |  |
| 5 | Create Job Step | Under Risks, enter the first job step name, Step 1: Pre-welding process, and choose Create or Enter. | The job step is created. |  |
| 6 | Repeat Step 5 to Create Two More Job Steps | Step 2: Welding assemblyStep 3: Clean the welding machine | The job steps are created. |  |
| 7 | Save Your Entries | Select Save. | The job hazard analysis is shown in display mode |  |

#### Identify a Job-Based Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to identify job-based risks.

This step creates a new job-based risk.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896)app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Using the search field, search for Job Welding for Production Line A. | You are navigated to the details screen of the job hazard analysis. |  |
| 4 | Go to Edit Mode | Select Edit. | The job hazard analysis is now editable. |  |
| 5 | Identify a Risk | Under Risks, for Step 2, Welding Assembly, select Identify Risk, select Without Agent, and enter the following data:Job Step: Welding AssemblyOperational Status: Normal OperationHazard: Moving Machine PartsSelect Add. | The risk is displayed in the risk list for job step Welding Assembly. |  |
| 6 | Assess Risk - Description | Select the new risk from the risk list to expand its details. Enter a meaningful text into the Description field. |  |  |
| 7 | Assess Risk - Impacts | Under Impacts, select Broken Body Parts from the value help. | The risk's impact is displayed. |  |
| 8 | Assess Risk - Catalog Controls | Under Controls, select Add Catalog Control.A wizard opens.Navigate through the first three steps: Engineering, Administrative, and Person-Related.In each step, expand the tree and select the available control.On the last screen of the wizard, select Add Controls to List. | Controls are displayed for the risk. |  |
| 8.1 | Assess Risk - Custom Controls | Under Controls, select Add Custom Control.A dialog opens. Enter the following data:Name: Enter a meaningful name.Description: Enter a meaningful text.Catalog: Select a catalog.Desired Effect: Lower LikelihoodSelect Add. | The control is displayed for the risk. |  |
| 9 | Create Task for Control | Select the first control from the list to expand its details. Enter a meaningful text into the Description field.Under Tasks, click Add Task. Select task type Task.In the new screen, enter the following data:Title: Enter a meaningful text.Assignee: Enter your own user.Select Create and navigate back. | The task is created for the control. |  |
| 10 | Implement Control | Select the Set to Implemented button. A warning that comes up if there are any open tasks serves informational purposes only. Do the same for the other controls, too.Select Apply to close the Details pane. | All controls receive the Implemented status. |  |
| 11 | Assessment Done | Select Assessment Done (near the top of the screen). Ignore the warning and choose Confirm. | The status of the risk becomes Assessment Done. |  |
| 12 | Save Your Entries | Select Save. | The job hazard analysis is shown in display mode. |  |

#### Identify a Job-Based Chemical Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. This means that they must do operational risk assessments. This test procedure shows how to identify chemical risks.

This step creates a new chemical risk.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Using the search field, search for Job: Welding for Production Line A. | You are navigated to the details screen of the job hazard analysis. |  |
| 4 | Go to Edit Mode | Select Edit. | The job hazard analysis is now editable. |  |
| 5 | Identify a Chemical Risk | Under Risks, for Step 3: Cleaning the welding machine, select Identify Risk, choose With Chemical Agent, and enter the following data:Job Step: Cleaning the welding machineOperational Status: Normal OperationChemical: AcetoneMethod of Use: PouringHazard: Skin/EyeSelect Add. | The risk is displayed in the risk list for job step Cleaning the welding machine. |  |
| 6 | Assess Risk - Description | Select the new risk from the risk list to expand its details. Enter a meaningful text into the Description field. |  |  |
| 7 | Assess Risk - Catalog Controls | Under Controls, select Add Catalog Control.A wizard opens.Navigate through the first three steps: Engineering, Administrative, and Person-Related.In each step, expand the tree and select the available control.On the last screen of the wizard, select Add Controls to List. | Controls are displayed for the risk. |  |
| 7.1 | Assess Risk - Custom Controls | Under Controls, select Add Custom Control.A dialog opens. Enter the following data:Name: Enter a meaningful name.Description: Enter a meaningful text.Catalog: Select a catalog.Desired Effect: Lower LikelihoodSelect Add. | The control is displayed for the risk. |  |
| 8 | Create Task for Control | Select the first control from the list to expand its details. Enter a meaningful text into the Description field.Under Tasks, click Add Task. Select task type Task.In the new screen, enter the following data:Title: Enter a meaningful text.Assignee: Enter your own user.Select Create and navigate back. | The task is created for the control. |  |
| 9 | Implement Control | Select the Set to Implemented button. A warning that comes up if there are any open tasks serves informational purposes only. Do the same for the other controls, too.Select Apply to close the Details pane. | All controls receive the Implemented status. |  |
| 10 | Assessment Done | Select Assessment Done (near the top of the screen). Ignore the warning and choose Confirm. | The status of the risk becomes Assessment Done. |  |
| 11 | Save Your Entries | Select Save. | The job hazard analysis is shown in display mode. |  |

#### Approve a Job Hazard Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. Consequently, they need to do operational risk assessments. This test procedure shows how a job hazard analysis is approved.

This step sets the status of the job hazard analysis to Approved.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Using the search field, search for Job: Welding for Production Line A. | You are navigated to the details screen of the job hazard analysis. |  |
| 4 | Approve the Job Hazard Analysis | Select Approve. | A confirmation dialog is displayed. |  |
| 5 | Set a Reminder | Activate Send Reminder for Reevaluation by Email. | Reminder for reevaluation is displayed. |  |
| 6 | Pick a Date | As date, select in one month. |  |  |
| 7 | Confirm the Approval | Confirm with OK. | The risk assessment is approved. |  |

#### Create the Job Hazard Analysis Summary Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. For this purpose, they must do operational risk assessments. This test procedure shows how to create and print a job hazard analysis summary report.

This step creates the job hazard analysis summary report.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Using the search field, search for Job: Welding for Production Line A. | You are navigated to the details screen of the job hazard analysis. |  |
| 4 | Display the Job Hazard Analysis Summary Report | Select Display Report.In the dialog, select the operational status Normal Operation in the dropdown and select Display Report. | A browser page is shown with the generated PDF document. |  |

#### Create a Follow-Up of the Job Hazard Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager and the industrial hygienist are together responsible for the safety of all employees working in their plant. For this purpose, they must perform operational risk assessments. This test procedure shows how to create a follow-up for a job hazard analysis.

This step creates a new revision of the job hazard analysis.

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On. | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety launchpad space on the Operational Risk Management page, and open the Manage Job Hazard Analyses (F7896) app. | The initial screen of the app is displayed. |  |
| 3 | Select the Newly Created Job Hazard Analysis | Using the search field, search for Job: Welding for Production Line A. | You are being navigated to the details screen. |  |
| 4 | Create a Follow-Up | Choose Follow-Up.In the dialog, select OK.If a Warnings dialog is displayed, just select Follow-Up to continue.In the Follow-Up Created dialog, select Go to Follow-Up. | A new revision of the job hazard analysis is created and displayed to the user in edit mode. |  |
| 5 | Discard Draft | Select Discard Draft. | The draft revision of the job hazard analysis is not created. The list report is shown. |  |

### Safety Instructions for Equipment

#### Create and Edit Safety Instructions for Equipment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager is responsible for the safety of all employees in their plant. Consequently, after finishing the operational risk assessment, they create several safety instructions containing all relevant safety information for the workers performing a certain job at that plant. This test procedure shows how to create such safety instruction.

This step creates a new set of safety instructions for equipment and assigns them to a relevant factory, in this case a production unit.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | On the Workplace Safety page, select Operational Risk Management from the dropdown to open the Manage Safety Instructions - Equipment (F4425) app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Safety Instruction | Choose Create. | A wizard to enter the relevant information is displayed. |  |
| 4 | Enter Relevant Data | Enter the following information in the dialog:Location: Production Line AEquipment Description: Welding MachineJob Description: WeldingLanguage: EnglishChoose Next Step. | The scope of the safety instruction is defined. |  |
| 5 | Select a Job Hazard Analysis | Choose Job Hazard Analysis Job: Welding for Production Line A.Choose Next. | The job hazard analysis is selected. |  |
| 6 | Select Risks | Select all displayed risks.Choose Next. | The risks are selected. |  |
| 7 | Create with AI | Choose Create Draft with AI.Choose Next. | Activate AI. |  |
| 8 | Review Summary | The summary is displayed. Review the defined scope and choose Create. | The safety instruction is created. The chapter texts are generated by AI. |  |
| 9 | Save Your Entries | Choose Create. | The newly created safety instruction is shown in display mode. |  |
| 10 | Preview Document | Choose Generate Document. | A preview of the document is displayed. It still contains the watermark In Process. |  |

#### Release Safety Instructions for Equipment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Releasing a set of safety instructions makes it available for public use. This means that it has been reviewed and that it is adequate for use at the relevant workplace.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Plant Manager - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | On the Workplace Safety page, open the Manage Safety Instructions - Equipment (F4425) app. | The initial screen of the app is displayed. |  |
| 3 | Select Safety Instructions | Choose the newly created set of safety instructions from the list of safety instructions. | You are navigated to the details screen, where all the chapters and their entered texts are visible. |  |
| 4 | Initiate Release | Choose Release. | A dialog is displayed asking whether this was a minor or a major change. |  |
| 5 | Release | Choose the Major Revision option.Choose Release. | You are navigated back to the list of available safety instructions. Your newly created set of safety instructions is shown in this list with revision number 1.0. |  |

#### Print Safety Instructions for Equipment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Printing a released set of safety instructions makes the document available for a physical provision at the workplace. It can also be used for work instructions.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Plant Manager - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | On the Workplace Safety page, open the Manage Safety Instructions - Equipment (F4425) app. | The initial screen of the app is displayed. |  |
| 3 | Select Safety instructions | Choose the newly created set of safety instructions in the list of safety instructions. | You are navigated to the detail screen and can see all the chapters and their entered texts. |  |
| 4 | Generate Document | Choose Generate Document. | A browser page is shown with the generated PDF document. |  |
| 5 | Print Document | Use the browser features to print the document. Usually there is a print button or a print command in the page’s context menu. | The safety instruction document is printed. |  |

### Safety Instructions for Substances

#### Create and Edit Safety Instructions for Substances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The plant manager is responsible for the safety of all employees working in their plant. Consequently, after finishing the operational risk assessment, they must create several safety instructions that contain all the relevant safety information for the employees working at a certain job at that plant. This test procedure shows how to create such a safety instruction.

This step creates a new set of safety instructions for substances and assigns them to a relevant factory—in this case, a production unit.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | On the Workplace Safety page, select Operational Risk Management from the dropdown to open theManage Safety Instructions - Substances (F3857A) app. | The initial screen of the app is displayed. |  |
| 3 | Create a New Safety Instruction | Choose Create. | A wizard to enter the relevant information is displayed. |  |
| 4 | Enter Relevant Data | Enter the following information in the dialog:Location: Production Line ASubstance: AcetoneJob: WeldingLanguage: EnglishChoose Next Step. | The scope of the safety instruction is defined. |  |
| 5 | Select a Risk Assessment | Choose Risk Assessment: Risk Assessment for Production Line A.Choose Next. | The risk assessment is selected. |  |
| 6 | Select Risks | Select all displayed risks.Choose Next. | The risks are selected. |  |
| 7 | Create with AI | Choose Create Draft with AI.Choose Next. | Activate AI. |  |
| 8 | Review Summary | The summary is displayed. Review the defined scope and choose Create. | The safety instruction is created. The chapter texts are generated by AI. |  |
| 9 | Use Text Blocks | Go to the Conduct in the Event of Danger chapter in the safety instructions.Choose Add Text Block.In the next dialog, choose Create Location Text Block.In the next dialog, enter Inform maintenance team.Choose Add.On the first dialog, select the newly added text block.Choose Add. | The text Inform maintenance team is added to the chapter.In addition, this text is available from now on in the Add Text Block dialog for this procedure.Note: This is true only for the currently chosen factory, Production Line A. Each factory has its own text blocks. |  |
| 10 | Add Symbols | Go to the Protective Measures and Rules of Conduct chapter in the safety instructions.Choose Select Symbols.Choose the <!-- image omitted: unnamed -->(Wear Ear Protection) symbol by activating its slider.Choose Close. | The symbol <!-- image omitted: unnamed -->(Wear Ear Protection) indicating the use of ear protection is shown below the Protective Measures and Rules of Conduct chapter. |  |
| 11 | Save Your Entries | Choose Create. | The newly created safety instruction is shown in display mode. |  |
| 12 | Preview Document | Choose Generate Document. | A preview of the document is displayed. It still contains the watermark In Process. |  |

#### Release Safety Instructions for Substances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Releasing a set of safety instructions makes it available for public use. This means that it has been reviewed and that it is adequate for use at the relevant workplace.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Plant Manager - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | On the Workplace Safety page, open theManage Safety Instructions - Substances (F3857A) app. | The initial screen of the app is displayed. |  |
| 3 | Initiate Release | Choose Release. | A dialog is displayed asking whether this was a minor or a major change. |  |
| 4 | Release | Choose the Major Revision option.Choose Release. | You are navigated back to the list of available safety instructions. Your newly created set of safety instructions is shown in this list with revision number 1.0. |  |

### Hazardous Substance Inventory

#### Maintain Hazardous Substance Inventory

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As hazardous substance manager, I aim to compile and provide a comprehensive inventory of all hazardous substances present within the company.

This test procedure shows how to create such an inventory in the system.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the View Hazardous Substance Inventory app in the Hazardous Substances section. | The initial screen of the app is displayed. |  |
| 3 | Maintain Inventory | In the upper right corner, choose Maintain Inventory. | The Maintain Hazardous Substance Inventory app is displayed. |  |
| 4 | Create New Sub-Inventory | Choose Create to create a new sub-inventory. | The Create Sub-Inventory dialog is displayed. |  |
| 5 | Enter Details for New Sub-Inventory | Enter the title Inventory List for Production Line A and select the location Production Line A in the value help.Choose Create. | The sub-inventory is created and displayed. |  |
| 6 | Create an Item for the Sub-Inventory | Choose Create to create an item for the sub-inventory. | The Create Inventory Item dialog is displayed. |  |
| 7 | Maintain Item | Enter the following information:Substance: AcetoneProduct: Select any available productLocation:Production Line AChoose Create. | A new item is created and displayed in the item list of the sub-inventory. |  |
| 8 | Maintain Amount | Enter an amount in the Current Amount input field and maintain an appropriate unit. | Amount and unit are maintained. |  |
| 9 | Save Entries | Choose Save. | Sub-inventory is saved and displayed in display mode. |  |
| 10 | Release | Choose Release and confirm. | The sub-inventory is released. |  |

#### View Hazardous Substance Inventory

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As hazardous substance manager, I require access to relevant attributes of hazardous substances at specific locations or company-wide.

This test procedure shows how to view the inventory in the system.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the View Hazardous Substance Inventory app in the Hazardous Substances section. | The initial screen of the app is displayed. |  |
| 3 | Display Inventory Information | Check if at least one entry is displayed for the substance Acetone and the location Production Line A. | Substance displayed in the result list. |  |
| 4 | Display Substance Details | Select the line for Acetone and location Production Line A. | Object page is displayed. |  |

### Hazardous Substance Overview

#### Get an Overview of Hazardous Substances in the Company

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Since hazardous substances pose a certain chemical hazard potential, they should generally be used as little as possible. However, sometimes the use of hazardous substances in the company cannot be avoided.

The Hazardous Substance Overview app provides an overview of approval requests and approved chemicals.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Hazardous Materials Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Hazardous Substance Management launchpad space and open the Hazardous Substance Overview app in the Insights section. | The initial screen of the app is displayed. |  |
| 3 | Card: Approved Chemicals by Method of Use | The card displays all approved chemicals by method of use in a donut chart.Check if there is at least one approved chemical with Spraying and at least one for Rinsing as method of use. |  |  |
| 4 | Card: Approved Chemicals by Purpose | The card displays all approved chemicals by purpose in a donut chart.Check if there are at least two approved chemicals for the purpose Surface Coating. |  |  |
| 5 | Card: My Requests for Chemical Approval | The card displays the user's own requests for chemical approval.In the dropdown, select Approved Requests.At least the newly created request is displayed. |  |  |
| 6 | Card: Open Requests for Chemical Approval | As the newly created requests are already completed, it is possible that this card is not displaying any data. |  |  |

### Workplace Safety Overview

#### Get an Overview of Workplace Safety in the Company

Purpose

The Workplace Safety Overview app provides an overview of incidents and risk assessments.

This step is about overview cards regarding risk assessments.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Go to the Workplace Safety page and open the Workplace Safety Overview app in the Insights section. | The initial screen of the app is displayed. |  |
| 3 | Card: Recent Risk Assessments | The card displays the recent five risk assessments and job hazard analyses last changed by the current user.Check if there are at least two risk assessments with title Risk Assessment for Production Line A and job: Welding for Production Line A. |  |  |
| 4 | Card: Risk Assessments with Reminder | The card displays all risk assessments with reminder due for reassessment in 60 or less days.Check if there is at least one risk assessment with title Job: Welding for Production Line A. |  |  |
| 5 | Card: Number of Risks | The card displays all open risk assessments displaying the ratio of risks in process to risks with assessment done.Check if there are at least two risk assessments with the title Risk Assessment for Production Line A and Job: Welding for Production Line B. |  |  |
| 6 | Card: Not Approved Risk Assessments | The card displays all not approved risk assessments by risk assessment type.Check if there are at least two risk assessment, one of type Health and one of type Job Hazard Analysis. |  |  |

### View My Workplace Safety

#### Get an Overview of Workplace Safety at my Location for my Job

Purpose

The View My Workplace Safety app provides the starting point for the employee's work, allowing them to familiarize themselves with workplace safety information in advance.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Employee - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the View My Workplace Safety app. | The initial screen of the app is displayed. |  |
| 3 | Filter for Location and Job | In the filter area, filter for location Production Line A and job Welding. |  |  |
| 4 | Safety Dashboard Section | In the Safety Dashboard section, information about incidents, risks and personal protective equipment is displayed. |  |  |
| 5 | Card: Risks | The card displays a list of risks for the selected location and job with the following information:Hazard:Hazard CategoryRisk DescriptionRisk Level |  |  |
| 6 | Card: Personal Protective Equipment | The card displays a list of all personal protective equipment for the selected location and job with the following information:Control Name:Control CatalogControl Description |  |  |
| 7 | Card: Hazardous Substances | The card displays a list of all hazardous substances for the selected location with the following information:Substance NameCAS NumberGHS SymbolsChemical Approval Status (Permitted) |  |  |
| 8 | Card: Quick Links | This card provides the possibility to report an incident. |  |  |
| 9 | Emergency Contacts Section | The Emergency Contacts section lists all emergency contacts (First Aider and Emergency Officer) for the selected location. |  |  |

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
> Flagged while digesting this document, not verified: The Release and Print safety-instruction steps log on as 'Plant Manager - EHS Info', which is not in the Roles table (Industrial Hygienist, Employee - EHS Info, Hazardous Materials Manager). The Overview Tables 5 and 6 name Industrial Hygienist as the business role for those same release steps.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Workplace Safety Overview card 'Number of Risks' expects a risk assessment 'Job: Welding for Production Line B', but the script only creates the job hazard analysis for Production Line A.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-occupational-health-for-environment-health-and-safety-7za]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54A_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 102,609 chars in the whole document
