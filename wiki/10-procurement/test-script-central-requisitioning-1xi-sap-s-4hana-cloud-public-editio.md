---
id: 10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio
title: "Test Script: Central Requisitioning (1XI) - SAP S/4HANA Cloud Public Edition (1XI_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for Central Requisitioning (1XI): hub/connected-system setup, PR-to-invoice and reservation test steps."
cluster: 10-procurement
tags: [kb/procurement, topic/central-procurement]
aliases: [1XI_S4CLD2608_BPD_EN_XX]
keywords: ["Central Requisitioning, Purchasing and Purchase Contracts", central requisitioning, hub and connected systems, purchase requisitions, purchase requisition approval, flexible workflow, default settings for users, connected system configuration, reservations, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XI_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-781
topic: 10-procurement/central-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Central Requisitioning (1XI) - SAP S/4HANA Cloud Public Edition (1XI_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XI_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Requisitioning, Purchasing and Purchase Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 02-09-26 |
| --- | --- |
|  | Central Requisitioning (1XI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc239509394)

[2 Prerequisites 4](#_Toc239509395)

[2.1 System Access 4](#_Toc239509396)

[2.2 Roles 4](#_Toc239509397)

[2.3 Additional Manual Configuration 5](#_Toc239509398)

[2.4 Preliminary Steps 5](#_Toc239509399)

[2.4.1 Define Company Code, Plant, Purchasing Organization and Communication System 5](#_Toc239509400)

[2.4.2 Define Connected System Material Group in the HUB System 8](#_Toc239509401)

[2.4.3 Define Connected System Purchasing Group in the HUB System 10](#_Toc239509402)

[2.4.4 Harmonize Account Assignment Category and Purchasing Requisition Document Type 11](#_Toc239509403)

[2.4.5 Maintain Requisitioning Groups (Optional) 11](#_Toc239509404)

[2.4.6 Set up Source of Supply Extraction 13](#_Toc239509405)

[2.4.7 Configure Flexible Workflow for Purchase Requisition (optional) 14](#_Toc239509406)

[2.4.7.1 Check Flexible Workflow for Central Purchase Requisition Approval 14](#_Toc239509407)

[2.4.7.2 Configure Flexible Workflow for Central Purchase Requisition 16](#_Toc239509408)

[2.4.8 Settings for Creation of Reservation – In Connected system 17](#_Toc239509409)

[2.4.9 Initializing Material Stock 18](#_Toc239509410)

[3 Overview Table 20](#_Toc239509411)

[4 Test Procedures 22](#_Toc239509412)

[4.1 Scenario 1: Central Requisitioning 22](#_Toc239509413)

[4.1.1 Maintain the Default Setting for Users 22](#_Toc239509414)

[4.1.2 Create Purchase Requisition – In HUB System 23](#_Toc239509415)

[4.1.3 Approve Purchase Requisition (Optional) – In HUB System 26](#_Toc239509416)

[4.1.4 Check My Purchase Requisition – In HUB System 27](#_Toc239509417)

[4.1.5 Process Purchase Requisition (Optional) – In Connected System 29](#_Toc239509418)

[4.1.6 Check Change Log of Purchase Requisition (Optional) – In HUB System 31](#_Toc239509419)

[4.1.7 Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System 33](#_Toc239509420)

[4.1.8 Create Confirmation for HUB Purchase Requisition – In HUB System 34](#_Toc239509421)

[4.1.9 Create a Return Delivery for HUB Purchase Requisition (Optional) – In HUB System 36](#_Toc239509422)

[4.1.10 Create Service Entry Sheet for HUB Lean Service Purchase Requisition – In Connected System 37](#_Toc239509423)

[4.1.11 Create Supplier Invoice – In Connected System 38](#_Toc239509424)

[4.1.12 Create Credit Memo (Optional) – In Connected System 40](#_Toc239509425)

[4.2 Scenario 2: Reservation for Central Requisitioning 42](#_Toc239509426)

[4.2.1 Maintain the Default Setting for Users 42](#_Toc239509427)

[4.2.2 Create Purchase Requisition – In HUB System 42](#_Toc239509428)

[4.2.3 Approve Purchase Requisition (Optional) – In HUB System 42](#_Toc239509429)

[4.2.4 Check Reservation Number – In HUB System 43](#_Toc239509430)

[4.2.5 Post Goods Issue for Reservation – In Connected System 43](#_Toc239509431)

[5 Appendix 45](#_Toc239509432)

[5.1 Configure Rework Flexible Workflow for Purchase Requisition 45](#_Toc239509433)

[5.2 Rework Purchase Requisition 46](#_Toc239509434)

## Purpose

Overview

Central Processing of Purchase Requisitions offers a centralized requisitioning processes across industries with a deep integration into the customer's landscape. It is connected to the customer’s ERP systems, and exchanges master data and business documents to ensure end-to-end business processes into Finance and Logistics that run in the connected Systems.

This scope item offers one platform where a procurement specialist can work centrally on requisitions from different organizations. Operational procurement processes are not the only tasks to profit from the hub approach. Strategic procurement tasks including Supplier Management benefit from the transparency and the possibility to initiate strategic activities from a central digital procurement control center.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | Identifies the SAP S/4HANA Cloud Public Edition system. The SAP S/4HANA Cloud Public Edition system acts as a hub system when it is connected to multiple connected systems.Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any SAP ERP system from release SAP ERP 6.0 Enhancement Package 6 and above, with add-on HUBERPI can be considered as a connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher, with add-on HUBS4IC can be considered as a connected system.Any SAP S/4HANA Cloud Public Edition 1808 and higher can be considered as a connected system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/4455461fa28ef2ce1f064967b4560123)

### Preliminary Steps

#### Define Company Code, Plant, Purchasing Organization and Communication System

Context

In this procedure, you can specify a unique combination of a plant, company code, purchasing organization and communication system in the HUB system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Open Manage Your Solution | Choose Manage Your Solution (F1241) . | The SAP S/4HANA Cloud Private Edition Guided Configuration screen displays. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Define Company Code, Plant, Purchasing Organization for Connected system | On the Configure Your Solution: Realize Phase screen, choose Sourcing and Procurement in the Application area. Choose Integration in Sub Application area, and then choose Go.Choose the item of Central Procurement – Settings in Hub System.On the Central Procurement – Settings in Hub System screen, choose Configure in the line of Define Company Code, Plant, Purchasing Organization for Connected system. |  |  |
| 5 | Create Connected system | Choose New Entries and make the following entries:Connected System ID: Your Connected system IDConnected System Name: Your Connected system nameCommunication System: Your Communication System configured in the Set-Up InstructionsChoose Save and choose Back. | The Connected system is created. |  |
| 6 | Create Connected System Company Codes | Select the newly created Connected System, and double click Connected Company Codes. Choose New Entries and make the following entries:Connected Company Code: Your Company Code in the Connected SystemCompany Code ID: Your company code unique IDCompany Name: Your company nameActive: CheckedChoose Save and choose Back. | The Connected Company Code is created. |  |
| 7 | Create Connected System System Plants | Select Connected Company Code you created, and double click Connected Plants. In the Dialog box Determine Work Area: Entry, choose Continue. Choose New Entries, and make the following entries:Connected Plant: Your Plant in the Connected SystemPlant Name: Your plant namePlant Unique ID: Your Plant Unique IDActive: CheckedChoose Save and choose Back. | The Connected Plant is created. |  |
| 8 | Create Connected System Purchasing Organization | Select the newly created Connected System, and double click Connected Purchasing Organization. Choose New Entries and make the following entries:Connected Purch Org: Your Purchasing Organization in the Connected System.Connected Purch Org ID: Your Connected Purchasing Organization Unique IDConnected Purch Org Name: Your Connected Purchasing Organization NameActive: CheckedChoose Save and choose Back. | The Connected Purchasing Organization is created. |  |
| 9 | Save Your Entries | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Company Code, Plant, Purchasing Organization for Connected system | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Company Code, Plant, Purchasing Organization for Connected system. |  |  |
| 3 | Create Connected system | Make the following settings:Connected System ID: Your Connected system IDConnected System Name: Your Connected system nameCommunication System: Your Communication System configured in the Set-Up InstructionsChoose Save and choose Back. | The Connected system is created. |  |
| 4 | Create Connected System Company Codes | Select the newly created Connected System, and double click Connected Company Codes. Choose New Entries and make the following entries:Connected Company Code: Your Company Code in the Connected SystemCompany Code ID: Your company code unique IDCompany Name: Your company nameActive: CheckedChoose Save and choose Back. | The Connected Company Code is created. |  |
| 5 | Create Connected System Plants | Select Connected Company Code you created, and double click Connected Plants. In the Dialog box Determine Work Area: Entry, choose Continue. Choose New Entries, and make the following entries:Connected Plant: Your Plant in the Connected SystemPlant Name: Your plant namePlant Unique ID: Your Plant Unique IDActive: CheckedChoose Save and choose Back. | The Connected Plant is created. |  |
| 6 | Create Connected System Purchasing Organization | Select the newly created Connected System, and double click Connected Purchasing Organization. Choose New Entries and make the following entries:Connected Purch Org: Your Purchasing Organization in the Connected System.Connected Purch Org ID: Your Connected Purchasing Organization Unique IDConnected Purch Org Name: Your Connected Purchasing Organization NameActive: CheckedChoose Save and choose Back. | The Connected Purchasing Organization is created. |  |
| 7 | Save Your Entries | Choose Save. |  |  |

#### Define Connected System Material Group in the HUB System

Context

In this procedure, you define the connected system material groups in the HUB system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Open Manage Your Solution | Choose Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Material Groups | On the Configure Your Solution: Realize Phase screen, search item Material Groups.Choose the line with Item Name- Materials.On the Configure Your Solution – Materials screen, choose Configure for item Define Material Groups. | The Material Groups screen displays. |  |
| 5 | Create New Entries | Choose Add and then make the following entries:Material Group: Your Material Group in the Connected SystemDescription: Your Description of the Material GroupDefault Unit of Measure: Your Default Unit of Measure of the Material Group |  |  |
| 6 | Save Your Entries | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Material Groups | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Material Groups. | The Material Groups screen displays. |  |
| 3 | Create New Entries | Choose Add and create the following entries:Material Group: Your Material Group in the Connected SystemDescription: Your Description of the Material GroupDefault Unit of Measure: Your Default Unit of Measure of the Material Group |  |  |
| 4 | Save Your Entries | Choose Save. |  |  |

#### Define Connected System Purchasing Group in the HUB System

Context

In this activity, you define the connected system purchasing groups in the HUB system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Open Manage Your Solution | Choose Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Purchasing Groups | On the Configure Your Solution: Realize Phase screen, search item Create Purchasing Groups.Choose the item for Sourcing and Procurement.On the Configure Your Solution – Organization screen, choose Configure in the item of Create Purchasing Groups. | The Create Purchasing Groups screen displays. |  |
| 5 | Create New Entries | Choose Add and then enter the following entries:Purchasing Group: Your Purchasing Group in the Connected SystemDescription: Your Description of the Purchasing Group |  |  |
| 6 | Save Your Entries | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Create Purchasing Groups | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Create Purchasing Groups. | The Create Purchasing Groups screen displays. |  |
| 3 | Create New Entries | Choose Add and create the following entries:Purchasing Group: Your Purchasing Group in the Connected SystemDescription: Your Description of the Purchasing Group |  |  |
| 4 | Save Your Entries | Choose Save. |  |  |

#### Harmonize Account Assignment Category and Purchasing Requisition Document Type

Purpose

Create a ticket for component XX-S4C-SRV-CON using the SAP Support Launchpad with detail information to request that the SAP Cloud Service Center harmonizes your account assignment category and purchasing requisition document type to the Hub System.

|  |
| --- |
| Note This step is only needed once you want to use the account assignment category and purchasing requisition document type which exist in the Connected System but do not exist in the Hub System. |

#### Maintain Requisitioning Groups (Optional)

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Maintain Requisitioning Groups | On the Configure Your Solution: Realize Phases screen, search Maintain Requisitioning Groups, then choose Search.Select the item Maintain Requisitioning Groups and go to the next screen.On the Requirements Processing screen, choose Configure on the line of configuration step with name Maintain Requisitioning Groups. | The Change View "Maintenance View for Requisitioning Groups for Purchasing" screen is displayed. |  |
| 5 | Create and save new entry. | Choose New Entries, then enter below data:RequisitioningGrpID: For example, Z001;Validity Start Date: <current data>;Validity End Date: <current data + 6 months>;RequisitionGrpName: for example, SOB testingChoose Save. | Requisition Group created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Requisitioning Groups | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Maintain Requisitioning Groups. | The Change View "Maintenance View for Requisitioning Groups for Purchasing" screen is displayed. |  |
| 3 | Create and save new entry. | Choose New Entries, then enter below data:RequisitioningGrpID: For example, Z001;Validity Start Date: <current data>;Validity End Date: <current data + 6 months>;RequisitionGrpName: for example, SOB testingChoose Save. | Requisition Group created. |  |

#### Set up Source of Supply Extraction

Context

To create a Purchase Requisition, the sources of supply from the Connected system need to be extracted to the SAP S/4HANA Cloud Public Edition HUB system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Import of Catalog Data (F2666). | The Application Jobs screen displays. |  |
| 3 | Create a New Job | On the Application Jobs screen, choose Create. |  |  |
| 4 | Enter the General Information | In section 1. Template Selection, enter the following entries:Job Template: Import Catalog DataJob Name:Your Job Name, by default is Import Catalog DataChoose Step 2.In section 2. Scheduling Options, by default Scheduling Options is set to Start immediately.To change the Scheduling Options, choose Define Recurrence Pattern.On the Scheduling Information screen, choose the required option and maintain the fields accordingly and confirm with OK. |  |  |
| 5 | Enter the Catalog Data | Choose Step 3. In section 3. Parameters, in Catalog Data area, enter the following entries:Web Service: Multi_BackendConnected system: Your connected systemCompany Code: Your Connected Company CodePlant: Your Connected PlantImport Type: Select either Full Import or Delta Import.If you choose Full Import, select either Material Group or MaterialIf you select Material Group:Material Group From: Your Material Group FromMaterial Group to: Your Material Group ToIf you select Material:Material: Optional, Your Special Material |  |  |
| 7 | Schedule the Job | Choose Schedule. | The Job status change to Finished. |  |

#### Configure Flexible Workflow for Purchase Requisition (optional)

##### Check Flexible Workflow for Central Purchase Requisition Approval

Purpose

In this procedure, you activate flexible workflow for hub purchase requisition approval.

|  |
| --- |
| Note If you want to use the flexible workflow to approve the purchase requisition, you have to perform the steps: Check Flexible Workflow for Purchase Requisition Approval and Configure Flexible Workflow for Purchase Requisition. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Purchase Requisitions,choose item Requirements processing from search result, then choose Configure on the right of Activate Flexible Workflow for Purchase Requisitions.On the Approval Settings for Purchase Requisition screen, choose NB. Then choose Edit on the next screen. | The Document Types Purchase Requisitions Change screen displays. |  |
| 5 | Activate Flexible Workflow for PR Approval | On the screen Document Types Purchase Requisition Change, check if the following entry selected for NB and NBS:Scenario based workflow:X | The Flexible workflow is active for Purchase Requisitions with DocumentType: NB & NBS. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Flexible Workflow for Purchase Requisitions | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Activate Flexible Workflow for Purchase Requisitions. | The Document Types Purchase Requisitions Change screen displays. |  |
| 3 | Open Active Flexible Workflow | On the Approval Settings for Purchase Requisition screen, choose NB. Then choose Edit on the next screen. |  |  |
| 4 | Activate Flexible Workflow for PR Approval | On the screen Document Types Purchase Requisition Change, check if the following entry selected for NB and NBS:Scenario based workflow:X | The Flexible workflow is active for Purchase Requisitions with DocumentType: NB & NBS. |  |

##### Configure Flexible Workflow for Central Purchase Requisition

Purpose

In this procedure, you configure your release conditions for Purchase Requisition Approval.

|  |
| --- |
| Note SAP Note 2485779 - Configure Workflow using SAP Fiori in S/4HANA, which provides information on steps to use the workflow framework in purchase requisition. Any question regarding this SAP note, please raise ticket to component MM-FIO-PUR-REQ-SSP. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert . | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Purchase Requisition | Open Manage Workflows for Purchase Requisitions (F2705)Note Before release 1911, please use App Manage Workflows for Purchase Requisitions - New. | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Select Release of Central PR Item then choose Add and make following entries:Name: Test Workflow for Central Purchase RequisitionPreconditions：<Net amount of central purchase requisition item is greater than> <your value, for example 100> <your currency, for example, EUR>Step Sequence: AddType: Release of Central Purchase Requisition ItemRecipients: Assignment By: <User>Note Please check if the employee data has been maintained with the chapter [Maintain the Default Setting for Users](#unique_15) [page ] 22 for Users if you can’t find User for approval.Select User with Manager_procurement from F4 helpChoose Add.Choose Save. | The Workflow for Central Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |
| 5 | Define Order | Choose Define Order.On the Define Order screen, then choose Test Workflow for Central Purchase Requisition then move the selected workflow one level up. | Define the priority for workflow. |  |

#### Settings for Creation of Reservation – In Connected system

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With this setting, you can choose automatic creation of reservation for a purchasing group and material group combination.

|  |
| --- |
| Note The Settings for Creation of Reservation is prerequisite to run chapter [Scenario 2: Reservation for Central Requisitioning](#unique_17) [page ] 42 |

Procedure

Table 1: Case1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access the respective Connected system. |  |  |
| 2 | Configure Your Settings for Reservation | In SPRO, go to Materials Management > Purchasing > Central Procurement – Settings in Connected Systems > Centrally Managed Purchase Requisition > Reservation .Open setting Define Settings for Creation of Reservation. Choose New Entries to create or choose Edit to change your settings as following:Movement Type: 201Rules: 03Unrestricted Stock: X Check Unrestricted Stock OnlyChoose Save.Choose Back.Open setting Define Material Group and Purchasing Group for Reservation.Choose New Entries and then make the following entries:Material Group: Your material group, for example, L001Purchasing Group: Your purchasing group, for example, 001Auto Resrv: 1 AllowYou can also delete existing combination. |  |  |

Table 2: Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Settings for Creation of Reservation (F2278) . |  |  |
| 3 | Configure Your settings for crea-tion of reservation | On screen Settings for Creation of Reservation, choose Edit to change your settings as following:Rules: Goods Issue(03)Movement Type: GI for cost center(201)Choose Add to add combination of purchasing group and material group for automatic reservation. You can also delete existing combination. | The Configure Your Solution screen displays |  |
| 4 | Save Your Entries | Choose Save. |  |  |

#### Initializing Material Stock

Case 1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system. |  |  |
| 2 | Initial Stock | You can initial stock with Transaction Code MIGO. |  |  |

Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Manage Stock (F1062). | The Manage Stock (Original) screen display. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material (Original) : TG0011 (otherwise , Z001)Plant: 1010 | The stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon next to the stock to add initial stock. For example:Storage Location: 101A Unrestricted Use Stock | A dialog box displays. The Storage Location, Stock Type, and Current Quantity fields are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document date: <Today>Posting date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the message:1 new document has been created: Material Document XXXThe stock is added. |  |

## Overview Table

The scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Scenario 1: Central Requisitioning with Standard Item Category

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain the Default Setting for Users](#unique_15) [page ] 22 | Configuration Expert - Business Process Configuration | Default Settings for Users - Purchase Requisitions (F1995) |  |
| [Create Purchase Requisition – In HUB System](#unique_20) [page ] 23 | Employee - Procurement | Create Purchase Requisition - Deprecated (F1643) | Purchase Requisition is created. |
| [Approve Purchase Requisition (Optional) – In HUB System](#unique_21) [page ] 26 | Manager - Procurement | My Inbox - All Items (F0862) | Purchase Requisition is approved. |
| [Check My Purchase Requisition – In HUB System](#unique_22) [page ] 27 | Employee - Procurement | My Purchase Requisitions - Deprecated (F1639) | Purchase Requisition is checked. |
| [Process Purchase Requisition (Optional) – In Connected System](#unique_23) [page ] 29 | Purchaser | ME57 |  |
| [Check Change Log of Purchase Requisition (Optional) – In HUB System](#unique_24) [page ] 31 | Purchaser | ME52N/ Process Purchase Requisitions - Deprecated (F1048) |  |
| [Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System](#unique_25) [page ] 33 | Purchaser | ME21N/ Process Purchase Requisitions - Deprecated (F1048) |  |
| [Create Confirmation for HUB Purchase Requisition – In HUB System](#unique_26) [page ] 34 | Employee - Procurement | My Purchase Requisitions (F1643A) | Goods Receipt post in Connected system. |
| [Create a Return Delivery for HUB Purchase Requisition (Optional) – In HUB System](#unique_27) [page ] 36 | Employee - Procurement | My Purchase Requisitions - Deprecated (F1639) | Return delivery post in Connected system. |
| [Create Service Entry Sheet for HUB Lean Service Purchase Requisition – In Connected System](#unique_28) [page ] 37 | Purchaser | ML81N/ Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet is created. |
| [Create Supplier Invoice – In Connected System](#unique_29) [page ] 38 | Accounts Payable Accountant | MIRO/ Create Supplier Invoice (F0859) | Invoice is created. |
| [Create Credit Memo (Optional) – In Connected System](#unique_30) [page ] 40 | Accounts Payable Accountant | MIRO/ Create Supplier Invoice (F0859) | Credit Memo is created. |

Table 4: Scenario 2: Central Requisitioning for Reservation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain the Default Setting for Users](#unique_31) [page ] 42 | Configuration Expert - Business Process Configuration | Default Settings for Users - Purchase Requisitions (F1995) |  |
| [Create Purchase Requisition – In HUB System](#unique_20) [page ] 23 | Employee - Procurement | Create Purchase Requisition - Deprecated (F1643) | Purchase Requisition is created. |
| [Approve Purchase Requisition (Optional) – In HUB System](#unique_21) [page ] 26 | Manager - Procurement | My Inbox - All Items (F0862) | Purchase Requisition is approved. |
| [Check Reservation Number – In HUB System](#unique_32) [page ] 43 | Employee - Procurement | My Purchase Requisitions - Deprecated (F1639) | Purchase Requisition is checked. |
| [Post Goods Issue for Reservation – In Connected System](#unique_33) [page ] 43 | Warehouse Clerk | Post Goods Movement (MIGO) |  |

## Test Procedures

### Scenario 1: Central Requisitioning

We can create central purchase requisition with standard item category, and the same would be replicated to connected ERP systems (or other SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition systems). As the connected system is ERP many times it is required to create Central PRs with different item category.

#### Maintain the Default Setting for Users

Context

The default setting for an employee should be maintained by the Configuration Expert mandatorily. Plant and Company code needs to be presented a primary information in the user defaults screen．

The user must be an employee user, because this scope item is focused on employee procurement.

The user for Purchase Requisition approval also must be an employee user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Default Settings for Users - Purchase Requisitions (F1995). | The Default Settings for Users screen displays. |  |
| 3 | Enter the User ID | On the Default Settings for Users screen, enter the User ID and then choose Enter.Note Please use the Search Help to find the User ID for User Name EmployeeProcurement.Note You need to find the user with role employee_procurement. |  |  |
| 4 | Edit the Default Setting for User | On the Default Settings for Users screen, choose Edit in the lower right corner.Make the following entries:Shop on Behalf Type: Select the type according to your requirement.Requisitioning Group (Optional): If you select Shop on Behalf Type "Group Based", you must select the group you define in chapter Maintain Requistioning Group. For example, Z001Note Please make sure to select Plant, Company Code and Purchaser Organization through F4 help.Plant: Connected Plant Employee belongs toCompany Code: Connected Company Code Employee belongs toPurchasing Doc. Type: Your Purchasing Documentation Type．For example, NB.Source Determination: <Select>The following field is not mandatory for Configuration Expert; Employee can update before create Purchase Requisition:Material Group: <Your Material Group>Currency: Your CurrencyPurchasing Group: Your Purchasing GroupPurchasing Organization: Your Purchasing OrganizationAccount Assignment Category: Your Account Assignment CategoryIf you use account assignment category K, please make the following entries:Cost Center: Your Connected Cost CenterChoose Save. | Default Settings are set for users. |  |

#### Create Purchase Requisition – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Employee create shopping cart, and generate a purchase requisition in hub system.

Prerequisite

The default setting for an employee should be maintained by the Configuration Expert mandatorily. Plant and Company code needs to be presented as a primary information in the user defaults screen. The user must be an employee user because this scope item is focused on employee procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access to My Purchase Requisitions | Open My Purchase Requisitions (F1643A). | The My Purchase Requisition Item screen displays. |  |
| 3 | Check Default Setting for User | On the My Purchase Requisitions screen, choose Profile of <employee name> at the upper right corner and select Default Settings for User.Check the following entries:Material Group: <Your Material Group>Currency: <Your Currency>Purchasing Group:<Your Purchasing Group>Purchasing Organization:<Your Connected Purchasing Organization>Purchasing Doc. Type: <NB>Account Assignment Category: <Your Account Assignment Category>If you use account assignment category K, please also make the following entry:Cost Center:<Your Connected Cost Center>Choose Save.Some default setting for user will also display at the bottom right of the screen, for example, Plant, Company Code. You can also choose Edit to change the setting. | Default Settings are set for users. |  |
| 4 | Case 1: For the extracted material | On the My Purchase Requisitions screen, enter the material number in the Search bar at top left and choose Enter.Search: <Your Extracted Material Number which was extracted in chapter “Set up Source of Supply Extraction” in Preliminary Steps>On the screen Cross-Catalog Search, the material will be listed.Choose Add at the right of the item.Choose Cart at top right of the screen. And then choose View Cart.Choose Purchase Requisition Items to go to screen Purchase Requisition Item.Choose item under part Account Assignment, and maintain or check the following entries and then choose Apply:GL Account: <Your G/L account>Cost Center: <Your cost center>On the screen Purchase Requisition Item, in part Source of Supply, you can choose Add.On the popup window Fixed Supplier, enter the following entry and choose Add:Supplier: <Your supplier>Choose Apply to go back to screen <Employee user name><Data>. | Only material with the same default company code and plant will display. |  |
|  | Case 2: For Purchase Product/Material or Service without material number | On the My Purchase Requisitions screen, choose Create Item.On the Purchase Requisition Item screen, make the following entries:Product Type Group: Choose Product/Material or Service from the drop-down boxItem Description: <Short text for your purchase>Material Group: <Material Group>Valuation Price: <Valuation Price, for example 10 EUR>Price Unit: <Price Unit, for example, 1 EA>Quantity Requested: <Number of items you want to purchase, for example, 100 EA>Delivery Date: <Delivery Date>Account Assignment Category: for example, K.Choose Enter after change account assignment category.Choose item under part Account Assignment, and maintain or check the following entries and then choose Apply:GL Account: <Your G/L account>Cost Center: <Your cost center>On screen Your Product Description, in part Source of Supply, you can choose Add.On the popup window Fixed Supplier, enter the following entry and choose Add:Supplier: <Your supplier>Choose Apply to go back to screen <Employee user name><Data>. |  |  |
| 5 | View Shopping Cart | On the screen <Employee user name><Data>, you can choose Create in part Items to create more item for this PR,In Part Items, choose the item to check the details:You can change plant and company code that belongs to same logical system (logical system of the default plant and Company code combination assigned).Once the company code and plant is changed, other data including purchase organization, G/L account, cost center also need to be manually changed accordingly.Note If you want to replicate the attachment to ERP connected system, please make sure to maintain the document type in connected system.You can also enter the Notes for the Item text, Item node or other value if it is necessary.Requested By (Optional): you can select the employee you are going to shop on behalf. |  |  |
| 6 | Create Purchase Requisition | Choose Order.If you use account assignment U when you create the PR, please make sure to follow the steps in chapter Process Purchase Requisition(Optional) to change account assignment from U to K to trigger the PO creation process.If you create service purchase requisition, please make sure to follow the steps in Create Service Entry Sheet for Service Purchasing. |  |  |

#### Approve Purchase Requisition (Optional) – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note Please ignore this chapter if you didn't perform the steps in chapter Configure Flexible Workflow for Purchase Requisition(Optional) in Preliminary Steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Manager - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Open My Inbox - All Items (F0862) . | A list of already created Purchase Requisition is displayed. |  |
| 3 | Select Purchase Requisition | Select the Purchase Requisition from the left screen and choose Approve at the bottom right of the screen. | The Submit Decision dialog box displays. |  |
| 4 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Requisition is approved. |  |
| 5 | Back to SAP Fiori launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

#### Check My Purchase Requisition – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After Hub Purchase Requisition is created and approved, the Hub Purchase Requisition will be replicated to connected system and a new Purchase Requisition will be created in connected system.

In this activity, you can check your Hub Purchase Requisition and the Purchase Requisition number created in connected system. And the follow-on documentation number including Purchase Order, Goods Receipt and Supplier invoice.

|  |
| --- |
| Note If you have activated Replication Before Approval by processing the chapter Define Settings for Central Requisitioning in Setting Up Central Requisitioning (1XI), the purchase requisition can be replicated to connected system before Approval. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access My Purchase Requisition | Choose My Purchase Requisitions (F1643A). | The My Purchase Requistions screen displays. |  |
| 3 | Check item details | Search your Requisition number in the Purchase Requisition list.Note In case you want to search for the Purchase Requisition which is created as "Shop of Behalf", please choose checkbox Shop on Behalf in Filter Bar, and choose Go.The central purchase requisition may have the following status:Awaiting Approved: If workflow is activated and the status is Awaiting Approve, go to step [Approve Purchase Requisition (Optional) – In HUB System](#unique_21) [page ] 26to approve the Purchase Requisition. You can go to PR item detail to check Approval Process Overview.Approved: If the status is Approved and no purchase order is created in connected system, please go to chapter [Process Purchase Requisition (Optional) – In Connected System](#unique_23) [page ] 29 to check whether source of supply needs to be assigned, or if the PR needs to be approved in connected system. If the Purchase Order still can't be created automatically even though all prerequisites are met, you can go to chapter Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System to manually convert PR to PO.PR Modified: If the replicated PR in connected system is changed, then the stastus of the Hub PR will be changed to PR Modified. If you want to check what is changed, you can go to chapter Check Change Log of Purchase Requisition(Optional) - In connected SystemFollow on Document Created: If the Hub Purchase Requisition is replicated to Connected system and covert to Purchase Order successfully, the status should be Follow on Document Created.Note If you want to automate the material purchase requisition conversion to a purchase order, please make sure to check Automatic Purchase Order in supplier master data, and execute Chapter Automatic Generation of Purchase Orders for the PR Replicated from Hub System under the sections of Configure the Connected System – ERP or SAP S/4HANA Cloud Private Edition, and Configure the Connected System – SAP S/4HANA Cloud Public Edition in Setting Up Central Requisitioning (1XI).A new Purchase Requisition will be replicated into connected system if the status is Approved or Follow on Document Created.On the screen My Purchase Requisitions, choose 1 item (or X items) in the line for your Purchase Requisition.In the dialog box Purchase Requisition Items, choose the item.Choose Zoom in button to check the follow on documentation number including PR or PO number in connected systemIf status of the PR or PO in connected system is In Release, it indicates the release strategy for this PR or PO is activated. Then you need to release the PR or PO in connected system. After releasing the PO, you can perform chapter Create Confirmation for HUB Purchase Requisition – In HUB System.If status of the PR or PO in connected system is In External Approval and the release strategy is not activated, it indicates Central Approval is activated for this PR or PO. Please refer to the following chapters in test script 2XT - Central Purchasing to release this PR or PO.For PR:Import Purchase RequisitionsProcess Purchase Requisitions CentrallyApprove Purchase Requisitions(Optional)For PO:Import Purchase OrderManage Purchase Orders CentrallyApprove Purchase Order (Optional)Note For service PR, if connected system is SAP S/4HANA Cloud Public Edition, you must go to chapter Process Purchase Requisition (Optional) – In HUB System to maintain all necessary value manually in service PR and then convert it to PO. | Detail information of the Purchase Requisition item displays.Note down:Purchase Requisition numberPurchase Order number (if have). |  |

#### Process Purchase Requisition (Optional) – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Once hub purchase requisition is created and approved, this hub purchase requisition will be replicated to connected system, and a new purchase requisition is created in connected system. You can check and change this purchase requisition.

Procedure

Case 1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system as an employee who is a Purchaser . |  |  |
| 2 | Change Account Assignment or assign source of supply | Change the account assignment or assign source of supply with Transaction Code ME57.After assigning source of supply and changing account assignment, the PO creation process is triggered and PO should be created automatically. If the PO still can not be created, you can go to chapter Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System to manually convert the PR to a PO in connected system. |  |  |

Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Find your Purchase Requisition | In area Purchase Requisition Processing, open Assign and Process Purchase Requisitions.On the screen Assign and Process Purchase Requisitions, make the following entries:Purchase Requisition: Your purchase requisition number replicated from the hub system (checked in step [Check My Purchase Requisition – In HUB System](#unique_22) [page ] 27).Assigned Purchase Requisitions: CheckChoose Execute. |  |  |
| 3 | Change Purchase Requisition | On the screen Assign and Process Purchase Requisitions, choose your purchase requisition and choose Edit Items and maintain the following value according to your requirement.AcctAssCat: change from U to KOpen Item Detail, choose Account Assignment and make the following entries:Cost Center: your cost centerOpen item Detail, choose tab Source of Supply and make the following entries:Fixed Supplier: your supplierChoose Save. | Note If you change the Purchase Requisition in connected system, the status of Purchase Requisition in hub system will also be updated . For example, if your system active workflow, then the status will be changed to: Approved: PR Modified. |  |
| 4 | Maintain mandatory value for Service Purchase Requisition(only for service PR in SAP S/4HANA Cloud Public Edition system) | Open Manage Purchase Requisitions - Professional.Search you purchase requisition and choose it.On the screen Purchase Requisition, choose Edit.Choose tab Item and choose the item.On the screen Purchase Requisition Item, choose tab Quantity and Data. Maintain the Start Date and End Date.Choose tab Source of Supplier, then choose Assign Source of Supplier, on the popup screen Source of supplier, select the source of supplier.Choose Apply. Then you need to manually convert service PR to PO.Note After you have maintained mandatory information in the Purchase Requisition, please go to chapter Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System to convert service PR to PO. |  |  |

#### Check Change Log of Purchase Requisition (Optional) – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Once the purchase requisition which is replicated from the hub system is changed in the connected system, you can check the change log in related Hub Purchase Requisition.

Currently, only if the following 5 fields of the purchase requisition are changed in the connected system, the change log can be displayed in related Hub Purchase Requisition.

|  |
| --- |
| Note Currently, only if the following 5 fields of purchase requisition are changed in connected system, the change log can be displayed in related Hub Purchase Requisition.QuantityDelivery DatePriceItem Deletion IndicatorMaterial |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to connected system | Access the respective Connected system to which employee belongs as a Purchaser. |  |  |
| 2 | Change purchase requisition in connected system | Case 1: ERP as connected systemThe purchase requisition replicated from the hub system can be changed in connected system with Transaction Code ME52N.Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as connected system.Logon to SAP Fiori Launchpad as a Purchaser.Choose Manage Purchase Requisitions.Enter you purchase requisition in search bar and choose Go.Choose your purchase requisition.On Purchase Requisition screen, choose Edit.Change your Purchase Requisition replicated from the hub system and choose Save. |  |  |
| 3 | Logon to Hub system | Logon to SAP Fiori launchpad as an Employee - Procurement. |  |  |
| 4 | Check change log in Hub system | Choose My Purchase Requisitions (F1643A)Search your Requisition number in the Purchase Requisition list.Choose the hub purchase requisition item to go to screen Purchase Requisition.On the screen Purchase Requisition, go to Item Areas and choose item to go to screen Purchase Requisition Item.On the screen Purchase Requisition Items, choose View Change Log at top right of the screen. The change log of connected system PR will be listed on popup window Change Log.Once the value of any one of the 5 fields in the purchase requisition is changed in connected system, the status of the Hub PR will be changed to PR Modified. |  |  |

#### Convert Purchase Requisition to Purchase Order Manually (Optional) – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Case 1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system as an employee who is a Purchaser . |  |  |
| 2 | Convert Purchase Requisition to Purchase Order | You can convert your purchase requisition to a purchase order manually with Transaction Code ME21N. |  |  |

Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Logon to SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Manage Purchase Requisitions | Please refer to step Convert Purchase Requisitions to Purchase Orders in Test Script J45. |  |  |
| 3 | Convert Purchase Requisition to Purchase Order | On Process Purchase Requisitions screen, search your PR.Then choose your PR and choose Create Purchase Order.Note Please make sure to maintain all necessary information to enable converting PR to PO. for example, Supplier. |  |  |

#### Create Confirmation for HUB Purchase Requisition – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Employee can confirm the Good receipt quantity against the respective Purchase Requisition.

|  |
| --- |
| Note This step does not apply to service purchasing. |

Procedure

There are two options to confirm the goods receipt.

Option A:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access My Purchase Requisition | Open My Purchase Requisitions (F1643A). | My Purchase Requisition initial screen appears. |  |
| 3 | Confirm goods receipt quantity | On My Purchase Requisitions screen. Search your Requisition and then choose Confirm.On the screen Confirm Requisitions, choose your PR item.At top right of the screen, choose Edit.Now you can check or change the following entries:In General Information section:Document Date: <Date of creation of document>Posting Date: <Date of posting the document>Delivery Note: <Reference of the delivery note>Header Text: <Description of material document>In Items section:Check or change the quantity in filed Delivered Quantity. | Confirm goods receipt and follow on goods receipt post in Connected system. |  |
| 4 | Finalize the delivery (Optional) | If the Delivered Quantity is less than Purchase Requistion quantity, and you need to close the Purchase Requisition, choose Final Delivery. |  |  |
| 5 | Confirm the Goods Receipt | Choose the checkbox for the item and choose Confirm.If release strategy is activated for your PO but you didn't release it in ECC connected system, there will be error message: Purchasing document 4XXXXXXXXX not yet released. | Confirm goods receipt and follow on goods receipt post in Connected system. |  |
| 6 | Check the follow on Goods Receipt document | Choose Back to go back My Purchase Requisitions screen . Choose 1 Item under the column Number for Items.On the dialog screen Purchase Requisition Items, choose the item.On the following screen, there will be one more material document for Good Receipt.Choose Zoom In to check the follow-on documentation number. | Business Process Flow display. |  |

Option B:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access Confirm Receipt of Goods | Choose Confirm Receipt of Goods (F4489). | Confirm Requisitions initial screen appears. |  |
| 3 | Confirm goods receipt quantity | On the Confirm Requisitions screen , enter your PR number and choose Go.Choose your PR item in the list.On the right screen, choose Edit.Now you can make the following entries:In General Information part:Document Date: <Date of creation of document>Posting Date: <Date of posting the document>Delivery Note: <Reference of the delivery note>Header Text: <Description of material document>In Items part:Check or change the quantity in filed Delivered Quantity. |  |  |
| 4 | Finalize the delivery (Optional) | If the Delivered Quantity is less than Purchase Requistion quantity, and you need to close the Purchase Requisition, choose Final Delivery. |  |  |
| 5 | Confirm the Goods Receipt | Choose the checkbox for the item and choose Confirm. | Confirm goods receipt and follow on goods receipt post in Connected system. |  |
| 6 | Check the follow on Goods Receipt document | Choose My Purchase Requisition screen .Choose 1 item under the column Number for Items.On the dialog screen Purchased Items, choose the item.On the Business Process Flow screen, there will be one more material document for Good Receipt.Choose Zoom In to check the follow-on documentation number. | Business Process Flow display. |  |

#### Create a Return Delivery for HUB Purchase Requisition (Optional) – In HUB System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In case goods received is of poor quality or damaged, employee can initiate the Return Delivery Process against the respective Purchase Requisition once the Good receipt is carried out.

|  |
| --- |
| Note This step does not apply to service purchasing. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access My Purchase Requisition | Choose My Purchase Requisitions (F1643A). | My Purchase Requisition initial screen appears. |  |
| 3 | Return Delivery | On My Purchase Requisitions screen. Choose your Requisition that contains the item(s) to be returned in the Purchase Requisition list.Choose Return.On the Return Delivery screen, make the following entries:Document Date: <Your document date>Posting Date: <Your posting date>Return Quantity: < The number of items you want to return>Reason for Return: < Description of reason for returning the items>Choose the checkbox for the return item and choose Return. | Returun delivery and follow on goods return post in Connected system. |  |
| 4 | Check the follow on Goods Receipt document | Choose Back to go back to My Purchase Requisitions screen . Choose the item under the column Number for Items.On the dialog screen Purchased Items, choose the item.On the Business Process Flow screen, there will be one more material document for Return Delivery.Choose Zoom In to check the follow-on documentation number. |  |  |

#### Create Service Entry Sheet for HUB Lean Service Purchase Requisition – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you maintain the Service Entry sheet for the service purchase order in Connected system.

|  |
| --- |
| Note This step only applies for service purchasing. |

Procedure

Case 1: ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system. |  |  |
| 2 | Maintain Service Entry Sheet | Create service entry sheet with Transaction Code ML81N.Maintain for your service purchase order. | Service entry sheet is created. |  |

Case 2: S/4 HANA as Connected System

Refer to Step Maintain Service Entry Sheet in Test Script 22Z -Procurement of Services.

#### Create Supplier Invoice – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you perform the invoice verification.

Procedure

Case 1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system to which employee belongs as Accounts Payable Accountant. |  |  |
| 2 | Create Invoice Verification | Create supplier invoice with Transaction Code MIRO.Choose Invoice. | Invoice is created in the Connected system. |  |

Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoices screen is dis played. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries:Transaction: <Invoice>Company Code: <your company>Invoice Date: <Today>Posting Date: <Today>Gross Invoice Amount : <Value in PO Calculate Tax>Invoice Party: <your supplier number>Reference: <reference invoice number from invoicing party> | The Create Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchase Order References, make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number |  |  |
| 5 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax CodeNote If the amount is more than 5.5% of the initial amount, it will trigger supplier invoice workflow, which means you need to do next step – Release Blocked Supplier Invoice and amount changes only work for single account assignment. |  |  |
| 6 | Post invoice | Choose Post. | The invoice is created. |  |

#### Create Credit Memo (Optional) – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

If you need to return delivery after create supply invoice, you can create the credit memo.

Procedure

Case 1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access the respective Connected system to which employee belongs as Accounts Payable Accountant. |  |  |
| 2 | Create Credit Memo | Create Credit Memo with Transaction Code MIRO.Choose Credit Memo. | Credit Memo is created in the Connected system. |  |

Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice app | Open Create Supplier Invoice (F0859) . | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | In section General Data, make the following entries:Transaction: Credit MemoCompany Code: your companyGross Invoice Amount: Invoice amountCurrency: your currencyInvoice Date: TodayPosting Date: TodayReference: xxxInvoicing Party: 10300001 |  |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).Reference: Purchase OrderPurchase Order: xxx | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create credit memo for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Add Amount and Quantity | Check the Items that you want to post, and enter the following field entries.Amount: xxxQuantity: xxxThen choose the Check button at the bottom right of the screen. | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax | In the section Tax, check if the Tax Amount equals the sum of Amount multiplied by Tax Code value of the selected items in Step 6 | The section tax is displayed. |  |
| 8 | Simulate Credit memo and Check Messages | Choose the Simulate button.If there are no differences(or if the value is within the defined tolerance), the Supplier Invoice is complete to post.Check the Gross Invoice Amount against the items plus tax amount(if tax code is,V0 you do not have any tax amount) | Invoice is consistent.In case that an error message is displayed, a correction of the entries is necessary |  |
| 9 | Post Credit Memo | Select the Post button to post the Credit Memo | The Invoice is posted. The system displays the message Invoice xxx posted. |  |

Result

The credit memo is created.

### Scenario 2: Reservation for Central Requisitioning

With this scenario, you can automatively create reservation for a hub purchase requisiton. The purpose of a reservation is to ensure that a material will be available when it is needed. It also serves to simplify and accelerate the goods issue process and prepare the tasks at the point of goods issue.

#### Maintain the Default Setting for Users

Please refer to chapter [Maintain the Default Setting for Users](#unique_15) [page ] 22.

#### Create Purchase Requisition – In HUB System

Please refer to chapter [Create Purchase Requisition – In HUB System](#unique_20) [page ] 23 to create your purchaser requisiton in hub system. In step 4, please refer to Case 1: Search for the extracted material.

|  |
| --- |
| Note As creation of a reservation is subject to stock availability. Please make sure there is enough stock of the material in connected system to create Reservation for hub Purchase Requisition. |

#### Approve Purchase Requisition (Optional) – In HUB System

Please refer to chapter [Approve Purchase Requisition (Optional) – In HUB System](#unique_21) [page ] 26 to approve the purchase requisition in hub system.

|  |
| --- |
| Note If you have performed the steps in chapter [Configure Flexible Workflow for Central Purchase Requisition](#unique_14) [page ] 16 in Preliminary Steps to active workflow, a reservation is created only after the purchase requisition item has been approved. |

#### Check Reservation Number – In HUB System

On creation of a reservation, a Reservation document is created as a follow-on document for the hub Purchase Requisition item.

Please refer to the steps to check your follow on documentation number in chatper [Check My Purchase Requisition – In HUB System](#unique_22) [page ] 27 to check your Reservation number.

The reservation number will be used in the chapter [Post Goods Issue for Reservation – In Connected System](#unique_33) [page ] 43.

|  |
| --- |
| Note If you have activated Replication Before Approval by processing the chapter Define Settings for Central Requisitioning in Setting Up Central Requisitioning (1XI), the purchase requisition can be replicated to connected system before Approval. But reservation will not be created in connected system before approval is carried out in hub system. |

#### Post Goods Issue for Reservation – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Table 5: Case1: SAP ERP as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access the respective Connected system to which employee belongs as Accounts Payable Accountant. |  |  |
| 2 | Create Credit Memo | Post Goods Issue for Reservation with Transaction Code MIGO.Choose Goods Issue for Reservation. | Credit Memo is created in the Connected system. |  |

Table 6: Case 2: SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition as Connected System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Post Goods Movement (MIGO) . |  |  |
| 3 | Post Goods Issue for Reservation | On the screen, make the following entries:Trans./Event: Goods IssueReference Document : ReservationDocument Number: Your Reservation numberChoose Enter.Qty in UnE: the quantity you need to post.SLoC: Your stock location.Choose Post. |  |  |

## Appendix

### Configure Rework Flexible Workflow for Purchase Requisition

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration。 | The SAP Fiori Launchpad displays. |  |
| 2 | Open Manage Workflow for Purchase Requisition | Open Manage Workflows for Purchase Requisitions (F2705). | The Manage Your Solution screen displays. |  |
| 3 | Create Rework Workflow | Select Workflows: Overall release of Central PR . Then choose Add and make the following entries:Name: Test Rework Workflow for Central Purchase RequisitionStart Conditions：for exampleTotal net amount of purchase requisition is greater than 500.00 USDIn Workflow Steps section, choose Create.On the screen Automatic Release of Central Purchase Requisition, make the following entries:Step Type: Overall Release of Reworkable Central PRIn Step Properties section:Is Optional Step: for example, NoIn Recipients section:Assignment By: for example, UserUser: Select User from F4 help, for example, Manager_procurementIn Exception Handling section:In part Rework Requested, make the following entries:Required Action: Rework Central PRRecipients: Role and Determined AutomaticallyAction Result: for example, Repeat step.Note Action result should be (after re-work):Continue Workflow: Current Workflow shall move to next stepRepeat Step: repeat the current step of current workflowRestart workflow: restart the workflowChoose Create.Choose Save. | The Rework Workflow for Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

### Rework Purchase Requisition

Purpose

According to the setting in previous chapter, when the total amount of central PR is more than 500.00 USD and document type is NBS. This PR will be perform workflow (Note: Order type is configured in Maintain the Default Setting for Users). In this chapter, you rework a central purchase requisition.

When the approver reviews the central and PR and wants the requestor to rework this PR, he can execute rework.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Logon to SAP Fiori launchpad as a Manager - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Open My Inbox - All Items (F5331) .Note Maybe you can find the value of Confidence Level for PR approval in the top right corner, that's because scope item 43E was activated. | A list of already created Purchase Requisition is displayed. |  |
| 3 | Rework purchase requisition | Select the Purchase Requisition at the left and choose Request Rework at the bottom of the screen.Enter the rework reason in the Submit Decision dialog then choose Submit. | The Purchase Requisition is approved. |  |
| 4 | Back to SAP Fiori launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

After the approver choose Rework, the status of the central PR should be changed to Awaiting Approval-Rework Required.Then the central purchase requisition should be editable again. Requestor can change this purchase requisition in APP - My Purchaser Requisition according to the requirement from approver.

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
> Flagged while digesting this document, not verified: Post Goods Issue for Reservation, Case 1 (SAP ERP): step 1 names role Accounts Payable Accountant and step 2 is titled 'Create Credit Memo' with expected result 'Credit Memo is created', although the step is a MIGO goods issue; Overview Table 4 and Case 2 give the role as Warehouse Clerk.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Tables 3 and 4 list apps 'Create Purchase Requisition - Deprecated (F1643)' and 'My Purchase Requisitions - Deprecated (F1639)', while the procedures use My Purchase Requisitions (F1643A); My Inbox - All Items is F0862 in the approval chapter but F5331 in the rework chapter.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Rework Purchase Requisition step 3 (Request Rework) gives expected result 'The Purchase Requisition is approved', whereas the text after the table says the status becomes 'Awaiting Approval-Rework Required'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchasing-2xt-88]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XI_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 82,294 chars in the whole document
