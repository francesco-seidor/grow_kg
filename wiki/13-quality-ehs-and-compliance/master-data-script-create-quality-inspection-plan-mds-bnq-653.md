---
id: 13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653
title: "Master Data Script: Create Quality Inspection Plan - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): prerequisites and Fiori test steps to create and manage quality inspection plans and their master data."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/inspection-plans]
aliases: [BNQ_S4CLD2608_Master_Data_EN_XX]
keywords: [Quality Inspection Plans, quality inspection plan, master inspection characteristics, sampling scheme, sampling procedure, dynamic modification rule, code groups, manage inspection plans, selected sets, inspection methods]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-653
topic: 13-quality-ehs-and-compliance/inspection-plans
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create Quality Inspection Plan - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Quality Inspection Plans** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Quality Inspection Plan - MDS (BNQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233905029)

[2 Prerequisites 4](#_Toc233905030)

[2.1 System Access 4](#_Toc233905031)

[2.2 Roles 4](#_Toc233905032)

[2.3 Required Organizational Units 4](#_Toc233905033)

[2.4 Mandatory and Optional Master Data 5](#_Toc233905034)

[2.5 Business Conditions 6](#_Toc233905035)

[2.6 Main Parameters for Data Creation 6](#_Toc233905036)

[2.6.1 Number Ranges 6](#_Toc233905037)

[3 Overview Table 7](#_Toc233905038)

[4 Test Procedures 8](#_Toc233905039)

[4.1 Characteristic Attributes - Edit Code Groups for Selected Sets 8](#_Toc233905040)

[4.2 Edit Selected Sets for Characteristic Attributes 9](#_Toc233905041)

[4.3 Edit Code Groups for Defects (Optional) 10](#_Toc233905042)

[4.4 Create Inspection Method (Optional) 11](#_Toc233905043)

[4.5 Create Master Inspection Characteristics (Optional) 13](#_Toc233905044)

[4.6 Create Master Inspection Characteristic with Reference to Class Characteristic (Optional) 16](#_Toc233905045)

[4.7 Create Sampling Scheme (Optional) 18](#_Toc233905046)

[4.8 Create Sampling Procedure (Optional) 21](#_Toc233905047)

[4.9 Create Dynamic Modification Rule (Optional) 22](#_Toc233905048)

[4.10 Create Inspection Plan 25](#_Toc233905049)

[4.11 Manage Inspection Plans 26](#_Toc233905050)

[4.12 Copy from Existing Inspection Plans 30](#_Toc233905051)

[4.13 Display Open Inspection Lots 32](#_Toc233905052)

## Purpose

If material quality is supposed to be inspected, one of the prerequisites is that an inspection plan is available. For example inspection may be required at the goods receipt process from the supplier or from the production order, The inspection plan must contain some details about the characteristics to be inspected, how they should be inspected and, for example, how many samples should be checked.

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
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |

### Required Organizational Units

Some segments of master data are dependent on the organizational units of the plant, The following table gives an overview of these different data segments and their relevant organizational units:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Selected Sets for Characteristic Attributes - Edit Selected Sets | Plant | Selected Set and so on | Selected sets combine different code groups and codes on plant level that are useful for certain applications | Plant: |
| Create Inspection Method | Plant | Inspection Method | Inspection Method can be used in an inspection plan |  |
| Create Inspection Plan Characteristics | Plant | Master Insp.Charac, Assignment of Selected Set, and so on | Master Inspection Characteristics can be used in an inspection plan. | Plant: |
| Create Inspection Plan | Plant | Assignment to a Material number, usage, Status, work center, and so on. | Plant data is assigned for every Plant ID of your enterprise structure for an inspection plan | Plant: |

### Mandatory and Optional Master Data

The following table gives an overview of optional and mandatory master data objects to be used in a quality inspection plan data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Code group/Selected set – for Characteristic Attribute |  | Mandatory | Code group/Selected set for characteristic attribute must be created before you create an inspection plan |
| Code group – for Defects |  | Optional | Code group – for Defects can be created before you create an inspection plan |
| Inspection Methods |  | Optional | Inspection Methods can be created before you create an inspection plan |
| Master Inspection Characteristics |  | Optional | Master Inspection Characteristics can be created before you create an inspection plan |
| Sampling scheme |  | Optional | Sampling scheme defines a collection of sampling plans that can be created before you create an inspection plan |
| Sampling procedure |  | Optional | Sampling procedure defines the rules that specify how the system calculates the sample size and the procedure can be created before you create an inspection plan |
| Dynamic Modification Rule |  | Optional | Dynamic modification rule contains the definition of inspection stages and the condition for inspection stage change. A dynamic modification rule can be created before you create an inspection plan |

### Business Conditions

Before this scope item can be tested, meet the following business conditions.

| Scope Item | Business Condition |
| --- | --- |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Material master must be created before you create an inspection plan. |
| 2ZW - Create Batch Management Master Data - MDS (optional) | If the inspection results shall be transferred to the batch class when making the usage decision, ensure that the following prerequisites are met. Also note that a class characteristic must be assigned to a master inspection characteristic (see the section of this document):Class characteristic must exist.Batch class (type 023) must exist.Class characteristic must be assigned to class of type 023.Material must be handled in batches and batch class was assigned to the material master in the classification view.Note If the Usage Decision and the respective quality score shall be transferred to the batch classification, class characteristic LOBM_UDCODE and LOBM_QSCORE, respectively, must be assigned to the batch class. Note that there is no need to link these characteristics to a master inspection characteristic in this case. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create an inspection plan.

#### Number Ranges

The following number ranges are defined for inspection plans and the related, dependent functionality:

| Number Range | Range / Business Partner ID | Comments |
| --- | --- | --- |
| External numeric | 50000000 to 59999999 | This range is for inspection plan |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Characteristic Attributes - Edit Code Groups for Selected Sets](#unique_11) [page ] 8 | Quality Planner | Edit Code Groups (QS41) | Characteristic attributes code group and codes are created. |
| [Edit Selected Sets for Characteristic Attributes](#unique_12) [page ] 9 | Quality Planner | Edit Selected Sets (QS51) | Selected Set for Characteristic Attributes is created. |
| [Edit Code Groups for Defects (Optional)](#unique_13) [page ] 10 | Quality Planner | Edit Code Groups (QS41) | Code Groups are created. |
| [Create Inspection Method (Optional)](#unique_14) [page ] 11 | Quality Planner | Create Inspection Method (QS31) | Inspection Method is created. |
| [Create Master Inspection Characteristics (Optional)](#unique_15) [page ] 13 | Quality Planner | Create Master Inspection Characteristic (QS21) | Master Inspection Characteristics are created. |
| [Create Master Inspection Characteristic with Reference to Class Characteristic (Optional)](#unique_16) [page ] 16 | Quality Planner | Create Master Inspection Characteristic (QS21) | Quantitative master inspection characteristic with link to class characteristic is created. |
| [Create Sampling Scheme (Optional)](#unique_17) [page ] 18 | Quality Planner | Create Sampling Scheme (QDP1) | Sampling scheme is created. |
| [Create Sampling Procedure (Optional)](#unique_18) [page ] 21 | Quality Planner | Create Sampling Procedure (QDV1) | Sample procedure is created. |
| [Create Dynamic Modification Rule (Optional)](#unique_19) [page ] 22 | Quality Planner | Create Dynamic Modification Rule (QDR1) | Dynamic Modification Rule is created. |
| [Create Inspection Plan](#unique_20) [page ] 25 | Quality Planner | Create Inspection Plan (QP01) | Inspection Plan is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Characteristic Attributes - Edit Code Groups for Selected Sets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Characteristic Attributes refers to a standard quality management (QM) catalog that defines possible states of inspected attributes. The codes are grouped together in code groups so that a hierarchical structure is defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Edit Code Groups (QS41). | The Edit Catalog: Initial Screen displays. |  |
| 3 | Enter Catalog | In the Edit Catalog: Initial Screen make the following entries:Catalog: for example, 1Code Group: *Choose Continue. | The Change View "Maintain Code Groups": Overview screen displays. |  |
| 4 | Maintain Code Groups | Select one Code Group, for example SURFACE, and double-click Codes in Dialog Structure. | The Change View "Code group": Overview screen displays. |  |
| 5 | Create Codes | On the Change View "Codes" Overview view, choose New Entries and make the following entries:Code: For example, 0010, 0020, and so onShort Text for Code: <Enter your description> |  |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

### Edit Selected Sets for Characteristic Attributes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Selected sets combine different code groups and codes on the plant level. These selected sets are useful for certain scenarios like characterizing possible analysis results for a certain product attribute (for example, surface properties).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Edit Selected Sets (QS51). | The app opens. |  |
| 3 | Enter Catalog\Plant\Selected Set | On the Edit Selected Set: Initial Screen, make the following entries:Catalog: 1Plant: <plant code>Selected Set: *Press Enter. | The Change View "Selected Sets": Overview screen displays. |  |
| 4 | Maintain Selected Sets | Select a Selected Set, for example, SMOOTH, and then double-click Selected Set Codes in the Dialog Structure. | The Change View "Selected Set Codes" Overview screen displays. |  |
| 5 | Create Selected Set Codes | On the Change View "Selected Set Codes" Overview screen, choose New Entries and make the following entries:Code Group: <code group value>Code: <code value>Valuation Code: either Accepted (OK) or Rejected (not OK)Defect Class: Major defect |  |  |
| 6 | Save Your Data | Choose Save. | Your data is saved. |  |

### Edit Code Groups for Defects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use code groups to categorize or classify possible quality defects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Edit Code Groups (QS41). | The Edit Catalog: Initial view displays. |  |
| 3 | Enter Initial Data | Make the following entries:Catalog: for example, 9Code Group for example, DEF-SURFChoose Continue. | The Change View "Maintain Code Groups": Overview view appears. |  |
| 4 | Maintain Code Groups | In the area of Maintain Code Groups, make the following entries:Short Text: for example, Surface Defects | Ensure that the Status of Code Group is Released. |  |
| 5 | Maintain Codes of Code Groups | In the Maintain Code Groups area, select one item that you created.Navigate to Codes in the dialog structure area, and double-click "Codes". | The Change View "Codes": Overview view appears. |  |
| 6 | Maintain Codes of Code Groups | In the view of Change View "Codes": Overview, choose New Entries.Make the following entries:Code: for example, 0010Short Text for Code: for example, Surface IssueDefect Class: for example, Major defectTo save your data, choose Save. | The code groups are maintained. |  |

### Create Inspection Method (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create inspection method.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Create Inspection Method (QS31). | The Create Inspection Method: Initial Screen appears. |  |
| 3 | Enter Initial Data | Make the following entries:Plant: <Plant Code>Inspect. Method: for example, SURFACEValid From: for example, <current date>Choose Inspection Method. | The Create Inspection Method: General Data screen appears. |  |
| 4 | Enter General Data | Make the following entries:Status: ReleasedShort Text: for example, SurfaceSearch Field: for example, Surface |  |  |
| 5 | Enter Long Text | Choose Create long text next to the Short Text field and enter descriptive text, for example:Please inspect the surface thoroughly, especially regarding roughness and whether there are scratches or dents.Choose Back. |  |  |
| 6 | Save Data | To save your data, choose Save |  |  |
| 7 | Access the SAP Fiori App | Choose Change Inspection Method. | The Change Inspection Method Version: Initial Screen displays |  |
| 8 | Enter Initial Data | Make the following entries:Plant: <Plant Code>Inspect. Method: for example, SURFACEChoose Inspection Method. | The Change Inspection Method Version: General Data view appears. |  |
| 9 | Choose a Document to Attach | Choose Documents from General Information. |  |  |
| 10 | Create Attachment for Document | Choose Create Document.In the Change Inspection Method Version: General Data dialog box, choose Continue/Enter without entering data.Confirm the File Upload message by choosing OK and select a file from your file system via double-click.Choose Transfer to navigate back to the Change Inspection Method Version: General Data screen. |  |  |
| 11 | Save Data | To save your data, choose Save. |  |  |

### Create Master Inspection Characteristics (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Create Master Inspection Characteristic (QS21). | Create Master Inspection Characteristic: Initial view appears. |  |
| 3 | Enter Plant Data | In the Create Master Inspection Characteristic: Initial view, make the following entries:Plant: <Plant Code>Master Insp.Charac: <value>, for example, YQUALI01Valid From: <current date>Choose Master inspection Characteristic | Create Master Inspection Characteristic: General Data view appears. |  |
| 4 | Enter General Data for Qualitative Characteristic | In the Create Master Inspection Characteristic: General Data, make following entries:Qualitative Charc: flaggedShort text: for example, SurfaceSearch field: for example, SurfaceStatus: Select Released and Reference CharacteristicChoose Enter. | A new window appears, Edit Characteristic Control IndicatorsReference characteristicIf you use the master inspection characteristic in an inspection plan, a reference is first created to this characteristic. However, you can cancel this reference and change the data individually, for example tolerances. Optional settings are provided in the following steps.Complete copy modelIf you use the master inspection characteristic in an inspection plan, the reference to this characteristic is canceled. You can immediately change the data, for example, tolerances. Only then, can you use this master inspection characteristic as a copy model.Incomplete copy modelIf you use the master inspection characteristic in an inspection plan, it can only be used in a copy model. This type of master inspection characteristic cannot be used in a material specification. |  |
| 5 | Edit Control Indicators for Qualitative Characteristics | In the Edit Characteristic Control Indicators view, flag the following options:Charac. attributeSampling ProcedureSumm. recordingRequired char.Choose Continue to flag more options.Fixed scopeNo documentationChoose Continue to exit edit. | The Edit Characteristic Control Indicators view displays. |  |
| 6 | Assign Inspection Catalogs | From the Assigned Inspection Catalog dialog box, choose a value for the CGr/SSet field, for example SMOOTH.Choose Continue. | Return to Create Master Inspection Characteristic: General Data viewNote The plant is automatically maintained by choosing Smooth via value help. |  |
| 7 | Assign Inspection Method (Optional) | Choose Inspection Methods and the Assigned Inspection Methods view displays.Make following entries:Method: SurfacePlant: <Plant Code>Choose Continue. | Return to Create Master Inspection Characteristic: General Data view. |  |
| 8 | Save Your Data | Choose Save | Your data is saved |  |
| 9 | Create a Quantitative Master Inspection Characteristic | From the SAP Fiori launchpad, open Create Master Inspection Characteristic: Initial Data view and make the following entries:Plant: <Plant Code>Master Insp Charac: for example, YQUANT01Valid From: <current date>and choose Master Inspection Characteristic | The Create Master Inspection Characteristic: General Data view displays |  |
| 10 | Enter General Data for Quantitative Characteristic | From Create Master Inspection Characteristic: General Data, make the following entries:Quantitative Char: flaggedShort Text: for example, LengthSearch Field: for example, LengthStatus: 2 ReleasedSelect Released and Reference CharacteristicChoose Enter | Edit Characteristic Control Indicators window appearsReference CharacteristicsIf you use the master inspection characteristic in a task list or material specification, a reference is first created to this characteristic. However, you can cancel this reference and change the data individually, for example for tolerances.Complete Copy ModelIf you use the master inspection characteristic in a task list, it can only be used in a copy model. This type of master inspection characteristic cannot be used in a material specification.Incomplete Copy ModelIf you use the master inspection characteristic in a task list, it can only be used in a copy model. This type of master inspection characteristic cannot be used in a material specification. |  |
| 11 | Edit Control Indicators for Quantitative Characteristics | In the Edit Characteristic Control Indicators, flag the following options:Lower specif.limitUpper specif.limitSampling procedureSumm. recordingRequired char.Choose Continue and flag these additional options:Fixed ScopeNo documentationRecord measured valsRR change docsChoose Continue |  |  |
| 12 | Enter Target Value | On the Tolerance Keys view, make the following entry:Target Value: for example 150and choose Continue |  |  |
| 13 | Enter Quantitative Data | On the Quantitative Data view, make the following entries:Decimal Places: for example, 2Msmt unit: for example cmLower Limit: for example, 100Upper Limit: for example, 200Choose Continue |  |  |
| 14 | Save Your Data | Choose Save. | Your data is saved. |  |
| 15 | Enable Defect Recording for an Existing Master Inspection Characteristic (Optional) | Open the Change Master Inspection Characteristic (QS23) app and open the master inspection characteristic you would like to change.Choose Control Indicators.In the Edit Characteristic Control Indicators dialog box, enable the Defects Recording option in the Results confirmation section, and choose Continue.Choose Continue again. |  |  |
| 16 | Assign Inspection Catalogs (Optional) | In General Information area, choose the Catalogs button. | The Assigned Inspection Catalogs dialog box appears. |  |
| 17 | Maintain Defect Codes for Rejection (Optional) | In Defect codes for rejection of the Assigned Inspection Catalogs dialog box, search and enter code group / code for general, upper limit, and lower limit violation, respectively.Choose Continue. |  |  |
| 18 | Save Your Data | Choose Save. | Your data is saved |  |

### Create Master Inspection Characteristic with Reference to Class Characteristic (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The link between master inspection characteristics and class characteristics enables the automatic transfer of inspection results to the batch classification, provided that you inspect with a task list. The class characteristics from the batch class are automatically valuated at inspection completion, on the basis of the inspection results.

When you enter a class characteristic and link it to a master inspection characteristic, certain control indicators and values from this class characteristic are transferred to the master inspection characteristic.

The link between master inspection characteristics and class characteristics allows you to transfer results of a quality inspection to the batch classification.

|  |
| --- |
| Note You can only have a 1:1 relationship between a class characteristic and a master inspection characteristic (that is, you cannot reference the same class characteristic in several master inspection characteristics). Class characteristic is defined on client level and master inspection characteristic is defined on plant level. Therefore, if you want to use batch valuation for multiple plants, it is mandatory to define plant-specific class characteristics and link them to the respective master inspection characteristic on plant level. |

Prerequisites

The prerequisites must be met for the link of master inspection characteristic to class characteristic, see the Business Conditions chapter about 2ZW.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result Comments | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Master Inspection Characteristic (QS21). | The Create Master Inspection Characteristic: Initial Screen view displays. |  |
| 3 | Enter Plant Data | On Create Master Inspection Characteristic: Initial Screen, make the following entries:Plant: Plant CodeMaster Insp.Charac: <value>Valid From: <current date>Class Characteristic: valueChoose Master Inspection Characteristic. | The Create Master Inspection Characteristic: General Data view displays. |  |
| 4 | Execute steps 10-14 in the Previous Chapter | Note The master inspection characteristic must be a reference characteristic.Some data is copied from the class characteristic to the master inspection characteristic. Furthermore, depending on the class characteristic settings, some control indicators of the master inspection characteristic cannot be changed. | Quantitative master inspection characteristic with link to class characteristic is created. |  |
| 5 | Check Batch Characteristics After Quality Inspection (Optional) | Create inspection lot either manually or via goods movement, execute quality inspection and make usage decision.To review batch characteristics, log onto the SAP Fiori launchpad as a Quality Technician and access the SAP Fiori App Manage Batches (F2462) or Batch Information Cockpit (BMBC), and check the characteristics under Classification. | Quality inspection data was transferred to the batch characteristic. |  |

### Create Sampling Scheme (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can, optionally, create a sampling scheme. A sampling scheme is a collection of sampling plans. A sampling plan defines the amount of samples to be inspected (sample size) as a function of the lot size. Furthermore, criteria for accepting or rejecting a sample can be defined (for example, based on the current inspection severity). Inspection severity defines whether a normal, reduced, or tightened inspection is executed so that a quality planner can flexibly adapt the inspection effort to the current quality situation (for example, less inspections, smaller sample size, or higher acceptance criteria when the current quality situation is good).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Create Sampling Scheme (QDP1). | The Create Sampling Scheme: Initial view appears. |  |
| 3 | Enter Sample Sampling Scheme Name | Enter a sample sampling scheme name.Sampling Scheme: for example, QM2Choose Continue. | The Create Sampling Scheme: Header Data view appears. |  |
| 4 | Enter Header Data | Make the following entries or selected:Sampling Scheme: for example, Sampling Scheme for severities (attr.)Valuation Parameters: for example, Attributive Insp.Sampling Table For: for example, Insp.severity.Choose Continue. | The Create Sampling Scheme: Parameters dialog box appears. |  |
| 5 | Enter Insp. Sev. Parameter | In the Create Sampling Scheme: Parameters dialog box, make the following search and entries:Insp.severity: for example, 002(Reduced Inspection)Tip Inspection severity defines whether a normal, reduced, or tightened inspection is executed. A quality planner can flexibly adapt the inspection effort, such as less inspections, smaller sample sizes, or higher acceptance criteria when the current quality situation is good.and select Choose | The Create Sampling Scheme: Sampling Table view appears. |  |
| 6 | Create Sampling Plans | In the Sampling Plans table, make the following entries.Lot size: for example, 10.Sample size: for example, 1.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 100.Sample size: for example, 2.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 1000.Sample size: for example, 5.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 10000000000.Sample size: for example, 50.Acceptance no.1: for example, 0.Rejection no.1: for example, 1. | One sampling plan is created.Acceptance no. N: Highest number of non-conforming units or defects that are tolerated so that the lot or attribute can be accepted.Rejection no. N: Lowest number of non-conforming units or defects resulting in a rejection of the lot or attribute.Remember If the number of non-conforming units or defects is between acceptance and rejection limits, the system determines the next sampling plan. |  |
| 7 | Create Other Table | In the Create Sampling Scheme: Sampling Table view, select Other table (or shift + F5). | The Create Sampling Scheme: Parameters dialog box appears. |  |
| 8 | Enter Insp. Sev. Parameter | In the Create Sampling Scheme: Parameters dialog box, make the following entries:Insp.severity: for example, 004(Normal Inspection)and select Choose | The Create Sampling Scheme: Sampling Table view appears. |  |
| 9 | Create Sampling Plans | In the Sampling Plans table, make the following entries.Lot size: for example, 10.Sample size: for example, 1.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 100.Sample size: for example, 5.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 1000.Sample size: for example, 10.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 10000000000.Sample size: for example, 100.Acceptance no.1: for example, 0.Rejection no.1: for example, 1. | Next sampling plan is created. |  |
| 10 | Create other table | In the Create Sampling Scheme: Sampling Table view, select Other table (or shift + F5) | The Create Sampling Scheme: Parameters dialog box appears. |  |
| 11 | Enter Insp. Sev. Parameter | In the Create Sampling Scheme: Parameters dialog box, make the following entries:Insp.severity: for example, 006(Tightened Inspection)and select Choose | The Create Sampling Scheme: Sampling Table view appears. |  |
| 12 | Create Sampling Plans | In the Sampling Plans table, make the following entries.Lot size: for example, 10.Sample size: for example, 2.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 100.Sample size: for example, 10.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 1000.Sample size: for example, 25.Acceptance no.1: for example, 0.Rejection no.1: for example, 1.Lot size: for example, 10000000000.Sample size: for example, 200.Acceptance no.1: for example, 0.Rejection no.1: for example, 1. | Next sampling plan is created |  |
| 13 | Save Data | To save your data, choose Save. | Sampling Scheme is created. |  |

### Create Sampling Procedure (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Choose Create Sampling Procedure (QDV1). | The Create Sampling Procedure: Initial Screen appears. |  |
| 3 | Enter Sample Procedure Name | Enter a sample procedure name, for example, YPERCIN1.Choose Continue. | A new window appears. |  |
| 4 | Enter Sample Procedure Data | Enter data for the sample procedure:Provide a description, for example 10% inspection w/o inspection pointsSampling type: for example, Percentage sampleValuation mode: for example, Valuation according to char.attrib.codeInspection points: for example, choose Without Inspection PointsUsage Indicator: Leave the Usage Blocked field, blankChoose Continue. | Determination rule is definedNote To use Sampling Schemes, you must choose Use sampling scheme in the Sampling Type field. Then, you assign the sample scheme which you created in the previous procedure. |  |
| 5 | Maintain Sampling Plan | Choose Sample and then enter the following data:Size as % of lot: for example, 10Choose Continue.Choose Save. | Your data is saved. |  |

### Create Dynamic Modification Rule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create dynamic modification rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Create Dynamic Modification Rule (QDR1). | The Create Dynamic Modification Rule: Initial Screen appears. |  |
| 3 | Enter Dynamic Modification Rule Name | Enter a modification rule name, for example QM1 | The Create Dynamic Modification Rule: Header Data screen appears. |  |
| 4 | Enter Header Data | Make the following entries:Short text: for example, Inspection/SkipFor Usage Decision: flaggedReset Period (Days): for example, 90Choose Next Screen | The Create Dynamic Modification Rule: Inspection Stages screen appears. |  |
| 5 | Enter data for Inspection Stage 10 | Make the following entries in the first line:Stage: 10InspSev: 2Initial Insp. Stage: flaggedShort Text: Initial Inspection |  |  |
| 6 | Enter data for Inspection Stage 20 | Make the following entries in the second line:Stage: 20InspSev: leave emptySkip: flaggedShort Text: Skip |  |  |
| 7 | Enter data for Inspection Stage 30 | Make the following entries in the third line:Stage: 30InspSev: 4Short Text: for example, <Normal Inspection> |  |  |
| 8 | Maintain Stage Change for Inspection Stage 10 | Select Inspection Stage 10 and choose Stage Change.In the Create Stage Change screen, make the following entries:OKNo. of Inspections: 1New Insp. Stage: 20Not OKRejections: 1New Insp. Stage: 30 | The entries are reflected in the table. |  |
| 9 | Maintain Stage Change for Inspection Stage 20 (Skip) | Select Inspection Stage 20 and choose Stage Change.In the Create Stage Change screen, make the following entries:OKNo. of Skips: 1Max. Skip Duration: 90New Insp. Stage: 30Not OKRejections: 1New Insp. Stage: 30 | The entries are reflected in the table. |  |
| 10 | Maintain Stage Change for Inspection Stage 30 | Select Inspection Stage 30 and choose Stage Change.In the Create Stage Change screen, make the following entries:OKNo. of Inspections: 1New Insp. Stage: 20Not OKRejections: 1New Insp. Stage: 30 | The entries are reflected in the table. |  |
| 11 | Save Your Data | Save your data. |  |  |

### Create Inspection Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Planner. | The Start page appears. |  |
| 2 | Access the SAP Fiori App | Open Create Inspection Plan (QP01) tile. | Create Inspection Plan (Initial view) appears. |  |
| 3 | Enter Data | In the Create Inspection Plan (Initial view), make the following entries:Material: <your material number>, for example QM001Plant: <Plant Code>Key Date: for example, todayChoose Continue | The Create Inspection Plan: Header Details view appears when there is no plan available for the specified material/plant combination.Note If there is a plan available, choose a group from the dialog box and Inspection Plan Create: Task List Overviewappears. Choose New Entries to create a new inspection plan. |  |
| 4 | Maintain Header Details | Create Inspection Plan (Header Details) appears. Enter the following data:Usage: Choose from the value help list for usage purpose, for example, 5 Goods receiptStatus: Choose from the value help list, for example, 4 Released (General)Lot size: Within 1 to 99,999, for example, 999 pcDynamic Modif. Level (optional): 1 Dynamic Modification at lot levelNote This data is only necessary if you use Dynamic Modification RulesDynamic Modification Rule (optional): <your data>Note This data is only necessary if you use Dynamic Modification RulesDynamic Modification Criteria (optional): for example, Supplier and ManufacturerNote This data is only necessary if you use Dynamic Modification RulesChoose Operations. | Inspection Plan Create: Operation Overview appears |  |
| 5 | Enter Operation Data (Overview) | On the Inspection Plan Create: Operation Overview view, enter the following:Operation Number: for example, 0010Work Center: Choose work center,for example, QMLABSControl Key: Choose a control key, for example, QM01Description: Provide a descriptionMark the operation line item, then choose Operation.Note If the Operation button is not available, choose More > Operation . | Create Inspection Plan: Operation Details appears.Note The Control Key influences the planning and processing of inspection operation, for example whether or not inspection characteristics must be maintained for an inspection operation. |  |
| 6 | Operation Data (Details) | On the Create Inspection Plan: Operation Details view, scroll to review the Recording View: ‘single values and summarized result (default view)’Choose Back to return to the Operation Overview view. |  |  |
| 7 | Enter Inspection Characteristics | Mark the operation line and choose Inspection Characteristic.Assign Master Inspection Characteristics, for example, a master inspection characteristic that is quality related, such as YQUALI01 for a qualitative characteristic, or one that is quantity related, such as YQUANTI01 for a quantitative characteristic.Assign Sample Procedure (optionally), to use in combination with the characteristic being inspected.Assign Dynamic Modification rule (optional): for example QMINote Dynamic modification can be assigned on the header level or on the inspection characteristic level.Choose Enter. | Detail information is displayed. |  |
| 8 | Save Your Data | Choose Save. | Your data is saved. |  |

### Manage Inspection Plans

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step # Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Inspection Plans (F3788). | The app opens. |  |
| 3 | Filter Data | In the Manage Inspection Plans (Initial view), make the following entries:Material: <Material> (by adapting the filters within the Inspection Plan Version section)Plant: <Plant code>Status of the Plan: <Overall status>, for example, 4 Released (general)Choose Go. | The list of Inspection Plans displays fulfilling the selection criteria. |  |
| 4 | Select Inspection Plan | Select the relevant entry and navigate to it by choosing > on the right side of the selected line. | You are navigated to the relevant Inspection Plan. |  |
| 5 | Change Key Date | Within the Manage Inspection Plans (F3788) app, choose Change Key Date. A dialog box displays and you can maintain the Key Date by inserting the date from which the change should be valid:Key Date: <Date>Note The Key Date is only considered for the created or deleted object (for example, inspection operations) but might not be considered for changes. Changes in existing object might display immediately. | The Key Date is changed. |  |
| 6 | Maintain General Data | The Manage Inspection Plans screen displays with theGeneral, Material Assignment, Operations, Attachments and Administrative Data field. Make the following entries to maintain the general data (choose Edit to change the entries):Plant: Choose from the value help list if not inserted yet.Inspection Plan Description: Change the description.Usage: Choose from the value help list for usage purpose, for example, 5 Goods receipt.Overall Status: Choose from the value help list, for example, 4 Released (General).Lot Size: Within 1 to 99,999, for example, 999 pcInspection Point (optional): Insert 101 Time related if you want to create inspection points based on time.Note The following data is only necessary if you use Dynamic Modification Rules.Dynamic Modif. Level (optional): 1 Dynamic Modification at lot levelNote Within Dynamic Modification Rules, it can be decided on which level a dynamization is relevant.Dynamic Modification Rule (optional): <your data>Note The following data is only necessary if you use Dynamic Modification Rules.Dynamic Modification Criteria (optional): For example, Supplier and Manufacturer | The Inspection Plan general data is maintained. |  |
| 7 | Maintain Material Assignment | Maintain the Material Assignment information within the Manage Inspection Plans (choose Add to add entries):Material: <Material>Plant: <Plant code>Supplier (optional): <Supplier number>Customer (optional): <Customer number>Note Further criteria can be displayed by Settings. | The Inspection Plan Material Assignment information is maintained. |  |
| 8 | Maintain Operations | Maintain the Operations information within the Manage Inspection Plans (choose Create to create entries):Description of the operation: <Description>Plant: <Plant code>Base Quantity: <Quantity>Unit of Measurement: <Unit>Note Further criteria can be displayed by Settings.Navigate to the Operation details by choosing > on the right side of the selected line. | The Inspection Plan Operation information is maintained and you are navigated to the item. |  |
| 9 | Maintain Operation (Overview) | Maintain the General Data within the Operation screen:Operation Number: <Given number by the system>Control Key: <Given by the system>Plant: <Plant code>Description of the Operation: <Description>Work Center (optional): Choose a work center, for example, QMLABSBase Quantity: <Quantity>Unit of Measurement: <Unit>Conversion of Units of Measure from Header to Operation.Note Further criteria can be displayed by Inspection Point Settings. | The Operation general data is maintained. |  |
| 10 | Maintain Operation (Characteristics) | Go to Characteristics within the Operation screen. Choose Assign Characteristics to copy master inspection characteristic information, or choose Add to add a new characteristic or master inspection characteristics.Note Even after choosing Add, it is possible to add a reference to a master inspection characteristic afterwards.Make the following entries:Description: <Short description>Master Inspection Characteristics (optional): <Master Inspection Characteristics>Control Indicators: <Control indicators>Note Further criteria can be displayed by Inspection Point Settings.Navigate to the Characteristic details by choosing > on the right side. | The Operation Characteristic information is maintained and you are navigated to the Characteristic. |  |
| 11 | Maintain Characteristic | The Characteristic details display and can be maintained. The following data might be relevant for maintenance:Note Depending on the settings for Control Indicators in the previous step, different fields might display.Description: <Short description>Weighting of Characteristic (optional): Choose from the value help list, for example, <Weighting>Inspection Method, Version, Plant (optional): Choose from the value help list, for example, <Inspection Method>Info Fields (optional): <Further information>Selected Set, Plant: Choose from the value help list, for example, <Selected Set qualitative characteristics>Dynamic Modification for Characteristic (optional): Choose from the value help list, for example, <Other Characteristic>Dynamic Modification Rule (optional): Choose from the value help list, for example, <Dynamic Modification Rule>Note Dynamic Modification Rule only displays if dynamic modification is on the characteristic level.You can find further administrative data in the relevant area.Go back to Operations. | The Characteristic information is maintained and you are navigated to the Operations screen. |  |
| 12 | Checking Administrative Data Operations | The Operations screen displays and can be maintained.You can find further administrative data in the relevant area.Go back to Inspection Plan. | The administrative data is available and you are navigated to the Inspection Plan screen. |  |
| 13 | Add Attachments to Inspection Plan | The Inspection Plan screen displays and the Attachments can be maintained.Choose Add to create a URL with description.Choose Upload to insert a document from the local file system.You can find further administrative data in the relevant area.Go back to Inspection Plan. | The administrative data is available and you are navigated to the Inspection Plan screen. |  |
| 14 | Save Your Data | Choose Save. | Your data is saved. |  |

### Copy from Existing Inspection Plans

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Quality Planner | The Start page appears. |  |
| 2 | Access the SAP Fiori app | Open Manage Inspection Plans (F3788). | Manage Inspection Plans (Initial view) appears. |  |
| 3 | On Initial view Filter Data | In the Manage Inspection Plans (Initial view), make the following entries:Material: <Material> , by adapting the Filters within the section Inspection Plan Version.Plant: <Plant Code>Status of the Plan: <Overall Status> , for e.g. 4 Released (general)Choose Go. | The List of Inspection Plans appear fulfilling the selection criteria. |  |
| 4 | On Filtered view select Inspection Plan | Choose the relevant entry and navigate by choosing the > on the right hand side of the selected line. | The relevant Inspection plan has been entered. |  |
| 5 | Copy from Existing Plan (Start) | Manage Inspection Plans appears. Choose Copy from Existing Plans.Within Copy from Existing Plans dialog box, insert potentially some data or immediately choose OK:Plant: <Plant Code>, Choose from the value help.Group and Group Counter: <Identifier of the plan>, Choose from the value help.Overall Status: <Status>, Choose from the value help list, for example, 4 Released (General)Valid-From Date: Choose from the value help listNote Further Criteria might be displayed by Adapt Filters | Copy from Existing Plans Side Panel appears. |  |
| 6 | Copy from Existing Plan (Copy) | Within the Copy from Existing Plans Side Panel the plans according to the previous selected filters are displayed. By using the > in front of each line the objects of the plans can be collapsed:Plan > Materials > OperationsWithin Materials one material can be selected and by choosing Copy the selected entry is copied to the current inspection plan.Within Operations one or multiple Operation can be chosen and by choosing Copy transferred to the inspection plan.Operation > CharacteristicsWithin Characteristics assigned to single operations one or multiple characteristics can be selected and be transferred to a free to use operation by choosing Copy. It is also possible to mark an operation and one or multiple corresponding characteristics to copy the operation incl. only the marked characteristic(s)Note To copy from existing plans is also possible within the Operation and Characteristic overview within the App Manage Inspection Plans. | Copy from Existing Plans Side Panel appears. |  |
| 7 | Save your data | Choose Save. | Your data is saved. |  |

### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, references are verified as well as the sample size used for quality inspection reviewed. The sample-drawing instruction can be printed.

Prerequisite

The inspection lot is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Enter Filter Fields | Make filter entries and choose Go | If relevant references (e.g. Purchase Order or production order) are not displayed in the Filters, please choose Adapt Filters. On the dialog box Adapt Filters, find Procurement or Production, choose More Filters. Select the relevant document and choose OK. Choose Go. |  |
| 4 | Select Inspection Lot | In the inspection lot list, select the inspection lot which you created before. | Inspection lot is displayed. |  |
| 5 | Print Sample-Drawing Instruction | Choose Print Sample-Drawing Instruction.Choose an output item for printing, duplicate potentially one and choose Send Output.Note If the print is already generated for an inspection lot, the Output Details dialog displays a list of previously printed output items. | The Output Details dialog opens, showing a list of output items with print and email channels configured. A PDF document containing the sample-drawing instruction is triggered and is sent to the Maintain Print Queues application for printing. |  |
| 6 | Mail Sample-Drawing Instruction | Choose Print Sample-Drawing Instruction.Choose an output item for Email and choose Send Output. | An email with the PDF is sent to the intended recipients. |  |

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
> Flagged while digesting this document, not verified: Quantitative characteristic step 10 describes both Complete and Incomplete Copy Model with near-identical wording, which may be a copy error

> [!warning] Conflict
> Flagged while digesting this document, not verified: Section 4.13 Display Open Inspection Lots is listed in the TOC but missing from the Overview Table process steps

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-655]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-657]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 55,834 chars in the whole document
