---
id: 10-procurement/test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Purchase Contract (BMD_AE) - SAP S/4HANA Cloud Public Edition (BMD_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item BMD Purchase Contract: prerequisites, configuration and step-by-step test procedures."
cluster: 10-procurement
tags: [kb/procurement, topic/purchase-contracts]
aliases: [BMD_S4CLD2608_BPD_EN_AE]
keywords: [Purchase Contracts, quantity contracts, test scripts, contract version management, item hierarchies, flexible workflow, purchase contract approval, reference purchasing organization, purchase requisitions, source lists]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMD_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1286
topic: 10-procurement/purchase-contracts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Purchase Contract (BMD_AE) - SAP S/4HANA Cloud Public Edition (BMD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Purchase Contract (BMD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232862194)

[2 Prerequisites 5](#_Toc232862195)

[2.1 System Access 5](#_Toc232862196)

[2.2 Roles 5](#_Toc232862197)

[2.3 Master Data and Organizational Data 6](#_Toc232862198)

[2.4 Additional Manual Configuration 7](#_Toc232862199)

[2.5 Preliminary Steps 7](#_Toc232862200)

[2.5.1 Check Flexible Workflow for Purchase Order Approval (Optional) 7](#_Toc232862201)

[2.5.2 Configure Flexible Workflow for Purchase Order (Optional) 8](#_Toc232862202)

[2.5.3 Manage Situation Types (Optional) 8](#_Toc232862203)

[2.5.4 Manage Teams and Responsibility for Procurement (Optional) 9](#_Toc232862204)

[2.5.5 Activate Flexible Workflow for Purchase Contracts (Optional) 10](#_Toc232862205)

[2.5.6 Configure Flexible Workflow for Purchase Contracts (Optional) 12](#_Toc232862206)

[2.5.7 Map the Purchase Organization to Reference Purchase Organization (Optional) 13](#_Toc232862207)

[2.5.8 Extend the Reference Purchase Organization for Supplier (Optional) 15](#_Toc232862208)

[2.5.9 Configure Version Management in Purchase Contracts (Optional) 15](#_Toc232862209)

[2.5.9.1 Define Reasons for Version-Relevant Changes for Purchase Contract 15](#_Toc232862210)

[2.5.9.2 Set Up Version Management for Purchase Contract 17](#_Toc232862211)

[2.5.10 Activate Item Hierarchies in Purchasing (Optional) 19](#_Toc232862212)

[3 Overview Table 22](#_Toc232862213)

[4 Test Procedures 25](#_Toc232862214)

[4.1 Purchase Contract Processing 25](#_Toc232862215)

[4.1.1 Create Purchase Requisition 25](#_Toc232862216)

[4.1.1.1 Create Purchase Requisition (Standard) 25](#_Toc232862217)

[4.1.1.2 Create Purchase Requisition (Outline Agreement) 26](#_Toc232862218)

[4.1.2 Create Purchase Contract 28](#_Toc232862219)

[4.1.2.1 Create Purchase Contract with reference to Purchase Requisition 29](#_Toc232862220)

[4.1.2.2 Create Purchase Contract with reference to Contract Template 30](#_Toc232862221)

[4.1.2.3 Create Reference Purchase Contract (Optional) 32](#_Toc232862222)

[4.1.3 Mass Changes to Purchase Contracts 33](#_Toc232862223)

[4.1.4 Approve Purchase Contract (Optional) 34](#_Toc232862224)

[4.1.5 Monitor Notification (Optional) 35](#_Toc232862225)

[4.1.6 Print Purchase Contract 36](#_Toc232862226)

[4.1.7 Generate Source Lists (Optional) 37](#_Toc232862227)

[4.1.8 Process Purchase Requisition and Create Purchase Order 38](#_Toc232862228)

[4.1.9 Search Purchase Documents with Requirement Tracking Number 40](#_Toc232862229)

[4.1.10 Approve Purchase Orders (Optional) 40](#_Toc232862230)

[4.1.11 Monitor Contract Items (Optional) 41](#_Toc232862231)

[4.1.12 Post Goods Receipt 43](#_Toc232862232)

[4.1.13 Partial Reverse Goods Receipt (Optional) 44](#_Toc232862233)

[4.1.14 Create Supplier Invoice 45](#_Toc232862234)

[4.2 Purchase Contract with Hierarchy Items Processing 47](#_Toc232862235)

[4.2.1 Create Purchase Contract with Hierarchy Items 47](#_Toc232862236)

[4.2.2 Approve Purchase Contract (Optional) 48](#_Toc232862237)

[4.2.3 Create Purchase Order with Reference to Purchase Contract 50](#_Toc232862238)

[4.2.4 Approve Purchase Orders (Optional) 51](#_Toc232862239)

[4.2.5 Post Goods Receipt 52](#_Toc232862240)

[4.2.6 Create Supplier Invoice 53](#_Toc232862241)

[4.3 Versioning of Purchase Contracts 54](#_Toc232862242)

[4.3.1 Create Purchase Contract 55](#_Toc232862243)

[4.3.2 Approve Purchase Contract 56](#_Toc232862244)

[4.3.3 Change Purchase Contracts 56](#_Toc232862245)

[4.3.4 Approve purchase contract with new version 57](#_Toc232862246)

[4.3.5 Display Version History in Purchase Contracts 58](#_Toc232862247)

[4.3.6 Create Purchase Order with Reference to Purchase Contract 59](#_Toc232862248)

[4.3.7 Approve Purchase Orders (Optional) 60](#_Toc232862249)

[4.3.8 Post Goods Receipt 61](#_Toc232862250)

[4.3.9 Create Supplier Invoice 61](#_Toc232862251)

[5 Appendix 64](#_Toc232862252)

[5.1 Process Integration 64](#_Toc232862253)

[5.1.1 Succeeding Processes 64](#_Toc232862254)

[5.1.2 Generate Source List 64](#_Toc232862255)

## Purpose

Overview

Quantity contracts are agreements for a company to order a certain quantity of a product during a specified period. In source determination, contracts replace the purchasing information records and can be assigned in the source list as the fixed source for MRP.

Target groups are purchasing managers as well as buyers. If purchase requisitions and purchase orders do not yet exist, they are created after the contract. You can check the released purchase orders that are referenced to a contract by monitoring the contract.

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 | Trad.Good 10,PD,Third Party |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 001 | Group 001 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Trading Good (“HAWA”) |
| BNE | Create Supplier |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/5aa2cb0cf89ae5570fa4aafadc7e8896)

### Preliminary Steps

#### Check Flexible Workflow for Purchase Order Approval (Optional)

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Please refer to chapter Check Flexible Workflow for Purchase Order Approval in scope item J45 to check Flexible Workflow for Purchase Order Approval.

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order (Optional)

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

Prerequisite

Please activate Flexible workflow for purchase document type NB in your system.

Procedure

Please refer to chapter Configure Flexible Workflow for Purchase Order in scope item J45 to configure Flexible Workflow for Purchase Order.

#### Manage Situation Types (Optional)

Purpose

In this procedure, you configure the situation type by using template.

|  |
| --- |
| Note Scope Item 31N - Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad with the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types.screen displays. |  |
| 3 | Select the template to copy | Choose Go.Select the latest version of PROC_CONTRACTREADYTOUSE, then choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the situation | Make the following entries and choose Save:ID: Z_CONTRACTName: Contract SituationChoose Situation Display tab and make the following entries:Resend Notification: checkedChoose the Condition tab and maintain the attribute value to configure the conditions to use this function.Choose Recipients tab and make the following entries:Filter by Responsibility Definition: select the items you want for Filter by Responsibility, for example, Plant, Purchasing Organization, Material Group.Choose Create. | Then situation type is maintained |  |
| 5 | Enable this situation type | In the dialog box, choose Yes. |  |  |

#### Manage Teams and Responsibility for Procurement (Optional)

Purpose

In this procedure, you configure teams and responsibility for procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412) . | The Team screen displays. |  |
| 3 | Maintain the Team details | On the screen Manage Teams and Responsibilities, choose Create.On the screen New Team , make the following entries:In the General Information tabName: Team_ContractDescription: Team of ContractGlobal ID: Team 1Status: EnabledType: OPPURIn the Team Members tab, choose Create, and make the following entries:Business Partner: use the search function to find the business partner of PurchaserFunctions: Operational PurchasingIn the Team Members tab, choose Create again and make the following entries:Business Partner: use the search function to find the business partner of Purchasing ManagerFunctions: Workflow Administration |  |  |
| 4 | Save the team | Choose Create. | The team is created |  |

#### Activate Flexible Workflow for Purchase Contracts (Optional)

Purpose

If you want to use the flexible workflow to approve the purchase contract, you have to activate Flexible Workflow for Purchase Contracts.

Prerequisite

Please active the flexible workflow for purchase document type MK/WK in your system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launch Pad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, in Application Area choose Sourcing and Procurement, in Sub Application Area choose Operational Procurement.Choose the item for Purchase Contract Processing .On the Configure Your Solution – Purchase Contract Processing screen, choose Configuration under Activate Flexible Workflow for Contracts. |  |  |
| 5 | Activate Flexible Workflow for Purchase Contract Approval | On the screen Document Types Contract Change, make the following entries. :Document Type: MK/WKScenario based workflow:XChoose Save. | The Scenario based workflow is active for Purchase Orders with Document Type: MK/WK. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Contracts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase Contracts Change screen displays. |  |
| 3 | Activate Flexible Workflow for Purchase Contract Approval | Check the following entries, if it does not maintained, please make it and choose Save:Document Type: MK/WKScenario based workflow:XChoose Save. | The Scenario based workflow is active for Purchase Orders with Document Type: MK/WK. |  |

Result

The Scenario based workflow is active for Document Type: MK/WK.

#### Configure Flexible Workflow for Purchase Contracts (Optional)

Purpose

In this procedure, you configure your release conditions for Purchase Contracts Approval.

Prerequisite

Please active the flexible workflow for purchase document type MK/WK in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration role. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Contracts (F3043). | The Manage Workflows screen is displayed. |  |
| 3 | Maintain flexible workflow for Purchase Contract | On Manage Workflow screen, choose Create and make following entries:Name: Test Workflow for Purchase ContractIn the Start Conditions area, select Target value of purchase contract is greater than with 2000 EURIn Steps area, choose Create.On the New Steps creen, make following entries:Step Type: Release of Purchase ContractIn Recipients area:Assignment by:UserRole: Select the User ID with Employee ID PURCHASING_MANAGER from F4 helpStep to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Save the configuration | Choose Create.Choose Save. |  |  |
| 5 | Activate Workflow Item | Choose back to screen Manage Workflows, select the Workflow Item you just created and choose Activate.Note If you don’t want other workflow item work, you can select it and choose Deactivate | The Workflow Item is activated. |  |
| 6 | Active workflow item for Automatic Release of Purchase Contract | Select the workflow Automatic Release of Purchase Contract, then choose Activate. |  |  |

#### Map the Purchase Organization to Reference Purchase Organization (Optional)

Purpose

Reference purchase Organization is used when there is no centralized purchase organization. You have to define one purchase organi-zation as reference purchase organization and link other purchase organizations to this reference purchase organization. When you create a contract using this purchase organization and this contract can be used by other purchase organizations which are linked to this ref. purchase organization. Normally, reference purchasing organization doesn’t have Plants assigned to it, not assigned to any company code either.

Reference purchase organization is basically used for better negotiation.

In this procedure, you can map the purchase organization to the reference purchase organization. Make sure the Purchase Organization data exists in the system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the Configuration Expert - Business Process Configuration role. |  |  |
| 2 | Access the App | Open Manage Your Solution. |  |  |
| 3 | Assign purchasing organization to reference purchasing organization | On the Configure Your Solution screen, in Application Area choose Organization, in Sub Application Area choose Organization, and choose Go.Choose the item for Organization.On the Configure Your Solution – Organization screen, choose Configuration under Assign purch. organization to reference purch. organization.On the following screen, choose New Entries and make the following entry:Purch. Organization: 3310Reference Purchasing Org.: Your reference purchasing organization, for example 1410Release Order: XConditions: X |  |  |
| 4 | Save Team | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the APP | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign purch. organization to reference purch. Organization.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign purchasing organization to reference purchasing organization | Choose New Entries and make the following entry:Purch. Organization: 3310Reference Purchasing Org.: Your reference purchasing organization, for example 1410Release Order: XConditions: X |  |  |
| 4 | Save Team | Choose Save. |  |  |

#### Extend the Reference Purchase Organization for Supplier (Optional)

Purpose

In this procedure, you can extend the purchaser organization data for the supplier in reference purchase organization.

Procedure

Please refer to chapter Creating Supplier Master Data - Purchasing Organization Data in MDS (BNE)- Create Supplier Master - MDS.

Please use the following data:

Business partner: 33300001

Purch. Organization: Your reference purchase organization maintained in step 3 of chapter [Map the Purchase Organization to Reference Purchase Organization (Optional)](#unique_13) [page ] 13. For example, 1710

#### Configure Version Management in Purchase Contracts (Optional)

When you configure version management, you can define the settings to generate and manage versions of a purchasing document, such as purchase contracts. You can also define reasons for changes that result in the creation of newer versions of the purchasing document.

##### Define Reasons for Version-Relevant Changes for Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define reasons for changes that result in the creation of versions of purchase contract (for example, legal changes or documentation issues).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Reasons for Version-Relevant Changes for Purchasing Documents | On Configure Your Solution : Realize Phase screen, in Application Area choose Sourcing and Procurement, in Sub Application Area choose General Settings, and choose Go.Choose the item for Version Management .On the Configure Your Solution – Version Management screen, choose Configuration under Define Reasons for Version-Relevant Changes for Purchasing Documents . |  |  |
| 5 | Define reason for version management of purchase contract | On the Change View “Versioning Maintenance View for Reason Codes” Overview screen, choose New Entries and then make the following entries:Reason: Your Reason, for example: 01Reason Description: Your Reason Description, for example: documentation issuesChoose Save. | Reason for Version management is maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Reasons for Version-Relevant Changes for Purchasing Documents | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Reasons for Version-Relevant Changes for Purchasing Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Reasons for Version-Relevant Changes for Purchasing Documents screen displays. |  |
| 3 | Define reason for version management of purchase contract | On the Change View “Versioning Maintenance View for Reason Codes” Overview screen, choose New Entries and then make the following entries:Reason: Your Reason, for example: 01Reason Description: Your Reason Description, for example: documentation issuesChoose Save. | Reason for Version management is maintained. |  |

##### Set Up Version Management for Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you configure the settings to manage the versioning of a purchasing document.

For a combination of purchasing document category, purchasing document type and purchasing organization, you can:

- Activate version management

If version management is active, changes to a purchasing document are managed in versions.

- Set up field selection for versions

You can specify the fields, which when changed, result in the creation of newer versions.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access Ap p | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Set Up Version Management for Purchasing Documents | On Configure Your Solution : Realize Phase screen, in Application area choose Sourcing and Procurement, in Sub Application area choose General Settings, and choose Go.Choose the item for Version Management .On the Configure Your Solution – Version Management screen, choose Configuration under Set Up Version Management for Purchasing Documents. |  |  |
| 5 | Active version management for purchase contract | On the Set Up Version Management for Purchasing Document screen, choose New Entries and then make the following entries:Category: K Purchase ContractDoc Type: Contract Document Type, WK or MKPurc. Org.: 3310Activate: CheckNecessity of Reason: You can set Optional or RequiredNecessity of Purchaser Note: You can set Optional or RequiredChoose Save. | Version management for your document type is activated. |  |
| 6 | Set up field selection for versions | Choose the item you created and double click Purcahsing Docurement Field Details.On the screen of Purchasing Docurement Field Details, choose New Entries and make the following entries:Version-Relevant Facet: Choose the item you want. For example: HeaderVersion-Relevant Field: Choose the item you want. For example: KTWRT (Target Value)Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Version Management for Purchasing Documents | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Version Management for Purchasing Documents.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Set Up Version Management for Purchasing Documents screen displays. |  |
| 3 | Active version management for purchase contract | On the Set Up Version Management for Purchasing Document screen, choose New Entries and then make the following entries:Category: K Purchase ContractDoc Type: Contract Document Type, WK or MKPurc. Org.: 3310Activate: CheckNecessity of Reason: You can set Optional or RequiredNecessity of Purchaser Note: You can set Optional or RequiredChoose Save. | Version management for your document type is activated. |  |
| 4 | Set up field selection for versions | Choose the item you created and double click Purcahsing Docurement Field Details.On the screen of Purchasing Docurement Field Details, choose New Entries and make the following entries:Version-Relevant Facet: Choose the item you want. For example: HeaderVersion-Relevant Field: Choose the item you want. For example: KTWRT (Target Value)Choose Save. |  |  |

#### Activate Item Hierarchies in Purchasing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can activate the item hierarchy function for purchase contracts, purchase requisitions, purchase orders, and model product specifications.

Important Information: In a standard system this configuration step is switched off by default. Once the switch is on, you cannot turn it off.

|  |
| --- |
| Note If the business function SAP Supplier Relationship Management (SRM) is active, item hierarchies cannot be activated in purchasing. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate Item Hierarchies in Purchasing | On Configure Your Solution : Realize Phase screen, in Application Area choose Sourcing and Procurement, in Sub Application Area choose General Settings, and choose Go.Choose the item for Item Hierarchy .On the Configure Your Solution – Item Hierarchy screen, choose Configuration under Activate Item Hierarchies in Purchasing . |  |  |
| 5 | Activate Item Hierarchies in Purchasing | On the Display /Change State of Business Function screen, choose Change State as following:Switch State: OnChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Item Hierarchies in Purchasing | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Item Hierarchies in Purchasing .Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Item Hierarchies in Purchasing screen displays. |  |
| 3 | Activate Item Hierarchies in Purchasing | On the Display /Change State of Business Function screen, choose Change State as following:Switch State: OnChoose Save. |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_20) [page ] 25 |  |  |  |
| [Create Purchase Requisition (Standard)](#unique_21) [page ] 25 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Purchase Requisition is created. |
| [Create Purchase Requisition (Outline Agreement)](#unique_22) [page ] 26 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Purchase Requisition is created. |
| [Create Purchase Contract](#unique_23) [page ] 28 |  |  |  |
| [Create Purchase Contract with reference to Purchase Requisition](#unique_24) [page ] 29 | Purchaser | Process Purchase Requisitions - Deprecated (F1048) | The Purchase Contract is created with reference to the Purchase Requisition. |
| [Create Purchase Contract with reference to Contract Template](#unique_25) [page ] 30 | Purchaser | Manage Purchase Contracts (F1600A) | The Purchase Contract is created with reference to the Contract Template. |
| [Create Reference Purchase Contract (Optional)](#unique_26) [page ] 32 | Purchaser | Manage Purchase Contracts (F1600A) | A new Purchase Contract is created. Purchase Contract Number is displayed. |
| [Mass Changes to Purchase Contracts](#unique_27) [page ] 33 | Purchaser | Mass Changes to Purchase Contracts (F2669) |  |
| [Approve Purchase Contract (Optional)](#unique_28) [page ] 34 | Purchasing Manager | My Inbox - All Items (F0862) | The Purchase Contract is approved. |
| [Monitor Notification (Optional)](#unique_29) [page ] 35 | Purchaser |  |  |
| [Print Purchase Contract](#unique_30) [page ] 36 | Purchaser | Manage Purchase Contracts (F1600A) |  |
| [Generate Source Lists (Optional)](#unique_31) [page ] 37 | Purchaser | Manage Source Lists (F1859) |  |
| [Process Purchase Requisition and Create Purchase Order](#unique_32) [page ] 38 | Purchaser | Process Purchase Requisitions (F1048A) | Manage Purchase Requisitions appears, purchase requisitions lists out. |
| [Search Purchase Documents with Requirement Tracking Number](#unique_33) [page ] 40 | Purchaser | Purchasing Documents by Requirement Tracking Number (F2905) |  |
| [Approve Purchase Orders (Optional)](#unique_34) [page ] 40 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Monitor Contract Items (Optional)](#unique_35) [page ] 41 (by Item) | Purchaser | Monitor Purchase Contract Items (F2423) | The system displays contract detail information. |
| [Monitor Contract Items (Optional)](#unique_35) [page ] 41 (by Account Assignment) | Accounts Payable Accountant | Purchase Contract Items by Account Assignment (F2421) | The system displays contract detail information. |
| [Post Goods Receipt](#unique_36) [page ] 43 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | A list of purchase orders is displayed. |
| [Partial Reverse Goods Receipt (Optional)](#unique_37) [page ] 44 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Overview is displayed. |
| [Create Supplier Invoice](#unique_38) [page ] 45 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice is created. |
|  |  |  |  |
| [Create Purchase Contract with Hierarchy Items](#unique_39) [page ] 47 | Purchaser | Manage Purchase Contracts (F1600A) | A new Purchase Contract is created. |
| [Approve Purchase Contract (Optional)](#unique_28) [page ] 34 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Create Purchase Order with Reference to Purchase Contract](#unique_40) [page ] 50 | Purchaser | Manage Purchase Contracts (F1600A) | Purchase order with hierarchy items is created. |
| [Approve Purchase Orders (Optional)](#unique_34) [page ] 40 | Purchasing Manager | My Inbox - All Items (F0862) . |  |
| [Post Goods Receipt](#unique_36) [page ] 43 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Create Supplier Invoice](#unique_38) [page ] 45 | Accounts Payable Accountant | Create Supplier Invoice (F0859) |  |
| [Versioning of Purchase Contracts](#unique_41) [page ] 54 |  |  |  |
| [Create Purchase Contract](#unique_42) [page ] 55 | Purchaser | Manage Purchase Contracts (F1600A) |  |
| [Approve Purchase Contract](#unique_43) [page ] 56 | Purchaser | Manage Purchase Contracts (F1600A) |  |
| [Change Purchase Contracts](#unique_44) [page ] 56 | Purchaser | Manage Purchase Contracts (F1600A) | New purchase contract version is created. |
| [Approve purchase contract with new version](#unique_45) [page ] 57 | Purchaser | Manage Purchase Contracts (F1600A) |  |
| [Display Version History in Purchase Contracts](#unique_46) [page ] 58 | Purchaser | Manage Purchase Contracts (F1600A) | Version history in purchase purchase contract is displayed. |
| [Create Purchase Order with Reference to Purchase Contract](#unique_47) [page ] 59 | Purchaser | Manage Purchase Contracts (F1600A) . |  |
| [Approve Purchase Orders (Optional)](#unique_34) [page ] 40 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Post Goods Receipt](#unique_36) [page ] 43 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Create Supplier Invoice](#unique_38) [page ] 45 | Accounts Payable Accountant | Create Supplier Invoice (F0859) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Purchase Contract Processing

#### Create Purchase Requisition

##### Create Purchase Requisition (Standard)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a purchase requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Requisitions Professional | Open Manage Purchase Requisitions - Professional (F2229) . | The Manage Purchase Requisitions- Professional screen is displayed. |  |
| 3 | Create New Purchase Requisition | On the screen Purchase Requisition, choose Create. |  |  |
| 4 | Enter detail data | On the screen New Purchase Requsition, make the following entries:Document Type: Pur. Requisition (NB).Automatic Source Determination: check. |  |  |
| 5 | Add new item | In the Items section, choose Create, then choose Material from the list. |  |  |
| 6 | Enter item data | On the screen Purchase Requisition Item, in the General Information tab, make the following entries:Material: TG10Plant: 3310Choose the Quantity and Date tab, and make the following entries:Quantity: 50Choose the Contact Information tab, and make the following entries:Requirement Tracking Number: For example:Test_TrackPurchasing Group: 001Choose Apply. | The Purchase Requisition item is maintained for the material. |  |
| 7 | Enter item data for another item | Repeat the step 5 and 6 to create another item:Material: TG11Plant: 3310Quantity: 30Requirement Tracking Number: For example:Test_TrackPurchasing Group 001Choose Apply. |  |  |
| 8 | Create the Purchase Requisition | Choose Create.If a warning message Choose a source of supply displays, skip it. | The Purchase Requisition is saved. |  |

##### Create Purchase Requisition (Outline Agreement)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a purchase requisition for Outline Agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Requisitions - Professional (F2229) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Requisitions Professional screen displays. |  |
| 3 | Create New Purchase Requisition | On the screen Purchase Requisition, choose Create. |  |  |
| 4 | Enter detail data | On the screen New Purchase Requsition, make the following entries:Document Type: Outline Agrmt. Reqn.(RV) |  |  |
| 5 | Add Item | In the Items section, choose Create and select Material from the list. | The Purchase Requisition Item screen displays. |  |
| 6 | Enter detail data | On the screen Purchase Requisition Item, in the General Information tab, make the following entries:Material: TG10Plant: 3310Choose the Quantity and Date tab, and make the following en-tries:Quantity: 50Release Date (Quantity and Date): For example, <today>Choose the Contact Information tab, and make the following entries:Requirement Tracking Number: For example:Test_TrackPurchasing Group: 001Choose Apply. |  |  |
| 7 | Enter item data for another item | Repeat the step 5 and 6 to create another item:Material: TG11Plant: 3310Quantity: 10Release Date (Quantity and Date): For example, <today>Requirement Tracking Number: For example:Test_TrackPurchasing Group 001Choose Apply. |  |  |
| 8 | Save your entries | Choose Create to save the document. | Outline Agreement is created. If it needs to be approved, please refer to the step Approve Purchase Requisition in Test Script 18J. |  |

#### Create Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a purchase contract with reference to Purchase Requisition or Contract Template.

Purpose

A quantity contract is an agreement between a purchasing organization and a supplier or vendor to decrease or increase a certain quantity of a product in an indicated period. The purchasing organization fulfills a contract by placing purchase orders against it. These purchase orders are called now as release orders (or call-offs). The supplier or vendor fulfills the contract by supplying the released quantity. When you create a call-off, you refer to the relevant contract. The system automatically updates the released quantities in the contract.

Procedure

A Quantity contract can be created with reference to either an existing Purchase Requisition or an existing Contract Template. Choose any of the following procedures to create a quantity contract.

##### Create Purchase Contract with reference to Purchase Requisition

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
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Process Purchase Requisitions (F1048A) . | The Manage Purchase Requisitions screen displays. |  |
| 3 | Select Purchase Requisition | On the screen Process Purchase Requisitions, enter your Purchase Requistion created in the chapter 4.1.2 Create Purchase Requisition (Outline Agreement) in field Purchase Requisition Number. Or enter some of the following search criteria to filter your purchaser requisition.:Purchasing Organization: For example, 3310Purchasing Group: For example, 001Plant: 3310Material ID: TG10 or TG11Choose Go.Choose your purchase requisition items and choose Create Contract. | Header level details for example, Purchasing Organization, Purchasing Group are filled in the preview header and the Item details are copied from Purchase Requisition on item level. |  |
| 4 | Purchase Contract Preview | Enter the following information in the screen of a Contract:Contract Type: Quantity Contract (MK)Supplier: 33300001Validity From: Start date of the contractValidity To: End date of the contractPurchasing Organization: For example, 3310Company Code:3310In Item tab:Target Quantity: Enter total quantity for document type MK, for example, Item1: 500, Item2: 100Net Order Price: Item 1: 10, Item 2: 15 | The Purchase Contract data is contained in the preview screen. |  |
| 5 | Create Contract | Choose Create. | Purchase contract is created. |  |

##### Create Purchase Contract with reference to Contract Template

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
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Initial entry for contract | On the screen Manage Purchase Contracts, choose Manage Templates. | The Template dialog box displays. |  |
| 4 | Create Contract Template | On the popup window, choose Create Template. | The Purchase Contract screen displays. |  |
| 5 | Enter Contract Header details | Make the following entries:Contract Type: Choose MK Quantity ContractSupplier: 33300001Purchasing Organization: For example, 3310Valid From: Start date of the contractValid To: End date of the contract, for example, end of this yearPurchasing Group: For example, 001Company Code:3310 |  |  |
| 6 | Enter Contract Item details | In the Item section, choose Create and make the following entries:Item Category: Standard(0)Account Assignment Category: Unknown(U)Material: TG10Target Quantity: Enter total quantity for document type MK, for example, 500Plant: For example, 3310Choose the item to go to screen Purchase Contract Item and make the following entries:GR-Based Invoice Verification: CheckChoose Apply.Choose Create and make the following entries for another item:Category: Standard(0)Account Assignment Category: Unknown (U)Material: TG11Target Quantity: Enter total quantity for document type MK, for example, 100Plant: 3310Choose the item to go to screen Purchase Contract Item and make the following entries:GR-Based Invoice Verification: Check | Item gets added and Create Contract Template Page appears. |  |
| 7 | Maintain Template name | Enter a Template name. For example, Lenovo Laptops & AccessoriesAdd Description to the Template and choose Save as Template. | The Contract Template is created. |  |
| 8 | Create Contract | Choos Back to screen Manage Purchase Contracts, choose Manage Templates.On the popup window Template, select the template created in previous step and choose Create Contract. | The Purchase Contract screen displays and the data from the template gets copied in this screen. |  |
| 9 | Save Contract | Choose Create. | The Purchase contract is created. |  |

##### Create Reference Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a Reference Purchase Contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header details | On the screen Manage Purchase Contracts, choose Create and make the following entries:Contract Type: Choose MK Quantity ContractSupplier: 33300001Purchasing Org.: The Org is the Reference Purchase Organization that defined in the Perquisite step 2.6.7 Map the Purchase Organization to Reference Purchase Organization, For example: 3310Valid From: Start date of the contract, for example, todayValid To: End date of the contract, for example, the end of this yearTarget value: For example, 1000 AEDPurchasing Group:001 |  |  |
| 5 |  | In the Items section, choose Create and make the following entries:Material: , For example, TG11Net price: Enter a net price , 10 AED per PC.Target Quantity: For example, 100 . |  |  |
| 6 | Save the Purchase Contract | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new Purchase Contract is created. The Purchase Contract Number is displayed |  |

#### Mass Changes to Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can apply changes to multiple selected Purchase Contracts in bulk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Mass Changes to Purchase Contracts (F2669) app. | The Mass Changes to Purchase Contracts screen is displayed. |  |
| 3 | Search for Purchase Contracts | On the screen Mass Changes to Purchase Contracts, search the Purchase Contracts you need to change, then choose Go. | The search results show the details with the respective filter Criteria. |  |
| 4 | Set Purchase Contracts for Mass Edit | Select the Purchase Contract(s) for Mass Change operation.Choose Mass Edit. | A dialog box will open displaying fields for 3 categories – Header fields, Item fields and Partner fields. |  |
| 5 | Apply Mass Changes | Set new values in the given desired fields e.g.- Payment Terms.Choose Apply Mass Changes.On the popup window Apply Mass Changes, maintain the job description. Then choose Apply. |  |  |
| 6 | Check Application Jobs | On the following popup window, choose View Job List to show the Job status. | It will navigate to Application Jobs page containing the list of Job IDs for all Purchase Contracts.Verify if the job is successful for the selected Purchase Contracts. |  |

#### Approve Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase contract. If the purchase contract’s value is greater than 2000 AED, then the Purchase Contract should get approved.

Prerequisite

A purchase contract must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchasing Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of already created purchase contract is displayed.Note Only if the overall value is populated in the general area of the purchase contract then an approval is needed. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase contract number in the search area, then choose the Search button. | The Purchase contract that meet the criterial, the status is In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase Contract on the left of the screen and choose Approve. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Contract is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Monitor Notification (Optional)

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
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Choose the notifications | Choose the Notifications icon which is at the top right of the Home screen.Choose the notifications which is generated by the system.Note This notification will be displayed only in case there is a valid requisition of any other type than Outline Agreement. | The Manage Purchase Requisitions- Professional screen is displayed. |  |
| 3 | Open Manage Purchase Requisitions Professional | In the screen, it will show one message about the New or updated contract available for usage in purchase requisition.Check the detail information about this purchase requisition and if necessary.Choose Assign Contract. | The Purchase Requisitions- item screen is displayed. |  |
| 4 | Check the source | Then in the Related Information section, the contract will show as one source item. |  |  |

#### Print Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is about printing the purchase contract.

Table 2: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts Screen displays. |  |
| 3 | Input the contract number | On the screen Manage Purchase Contract, search your purchase contract.Choose your purchase contract. |  |  |
| 4 | Preview the contract form | On the screen Purchase Contract, choose the Output Control tab, then choose Display Document. |  |  |
| 5 | Print the contract form | After review the purchase contract, choose Print. |  |  |

#### Generate Source Lists (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you maintain the contract as the source.

Table 3: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the Fiori launchpad with the Purchaser role. | The Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Manage Source Lists (F1859). | The Manage Source Lists screen is displayed. |  |
| 3. | Maintain the filter of the source list | On the screen Manage Source List, in the filter, make the following entries:Material: TG10/TG11Plant: 3310Then choose Go. | If the source list item was already maintained, it will be shown. |  |
| 4. | Check the source list | If there is one item that is valid in the current period, ignore the following steps. If there isn't a valid item, continue with the next steps. |  |  |
| 5. | Create source list | On the screen Manage Source List, choose Create. | The Source List screen is displayed. |  |
| 6. | Enter the detail data | Choose Generate. |  |  |
| 7. | Use the Generated source to choose determine source | On the screen Source List, make the following entries:Material For example: TG10 / TG11Plant For example:3310Choose Generate.On the popup screen Generated Sources, make the following entries:Valid From: For example, TodayValid to: For example, Today +7 daysChoose Go.The valid source of supply are listed. Choose the check box of one contract, for example, select the contract that you created in chapter [Create Reference Purchase Contract (Optional)](#unique_26) [page ] 32.Then choose Add to Existing. |  |  |
| 8. | Save the source list | Choose Create. | The source list is saved. |  |

#### Process Purchase Requisition and Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when you want to review your purchase requisitions and assign them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Choose Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Requisitions screen displays. |  |
| 3 | Check purchase requisition | On the screen Process Purchase Requisitions, choose Standard at top left.Then enter search criteria to filter your purchase requisition.Or you can enter the purchase requisition number created in chapter [Create Purchase Requisition (Standard)](#unique_21) [page ] 25.If have assigned the souce of supply in [Generate Source Lists (Optional)](#unique_31) [page ] 37, please skip to step 6. | Fact sheet of purchase requisition is displayed |  |
| 4 | Check or Assign suppliers | Choose Show More per Row. Then the source of supplier will be displayed.Check source of supply in line Assigned Suppiler.If there is no supplier is assigned, please choose Assign Source of Supplier. On the popup window Assign Souce of Supplier, choose tab contract and then choose the contract you created in previous chapter. And then choose Assign.You can also choose Edit to change the Delivery Date and quantity on the pupup window. After you choose, please choose OK. | Select the source of supply in the dialog box. |  |
| 5 | Create Purchase Order | Select the purchase requisition and choose Create Purchase Order. | The Purchase Order Preview screen displays. |  |
| 6 | Submit the PO | Select the Purchase Order Type, and choose Save. | The system displays: Standard PO held under the number 4500xxxxxx. Choose OK. |  |

#### Search Purchase Documents with Requirement Tracking Number

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this chapter, you can search Purchase Requisitions, RFQs, Purchase Contracts, Scheduling Agreements or Purchase Orders created with Tracking Number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Purchasing Documents by Requirement Tracking Number (F2905) app. | The Purchasing Documents by Requirement screen is displayed. |  |
| 3. | Search for Purchase Documents with a Requirement Tracking Number | On the screen Purchasing Documents by Requirement Tracking Number, enter Requirement Tracking Number,For example: Test_Track.Then choose GO. |  |  |
| 4. | Display Purchsing Document | The purchasing document with this tracking number will be displayed. |  |  |

#### Approve Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All purchase orders that require authorization are listed needs to be approved.

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchasing Manager role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

#### Monitor Contract Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Perform this chapter if you want to monitor purchase contracts. Purchase contracts may be monitored at:

1. Header – Manage Purchase Contracts
2. Item – Monitor Contract Items & Monitor Contract Items by Account Assignment

The Monitor Purchase Contact Items App can be used to monitor purchase contract Items based on various criteria like Supplier/ Material/ Material Group/ Document Number/ Requirement Tracking Number/ Agreement Type/ Purchase Organisation/ Purchase Group

The Purchase Contract Items by Account Assignment App can be used to review Purchase Contract documents based on account assignment.

Procedure

Header Monitoring

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad, as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Monitor Purchase Contract Items (F2423) app. | The Manage Purchase Contracts screen appears, and the purchase contracts are listed out. |  |
| 3 | Display contract Item | On the screen Monitor Purchase Contract Items, enter search criteria to search your contract, or enter the Contract Number that was created in step 4.2 Create Purchase Contract. And make the following entries:Display Currency: for example, AEDThen choose Go. | The system displays contract detail information. |  |
| 4 | Monitor purchase Contract Items | On the screen Monitor Purchase Contract Items, you can review the detail information of the purchas contract. |  |  |

Item Monitoring

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Monitor Purchase Contract Items (F2423) app. | The Monitor Purchase Contract Items screen appears, and the purchase contracts items are listed out. |  |
| 3 | Display contract Item | Display Currency: <Choose one currency>.Choose the item of the Contract Number that was created in step 4.2 Create Purchase Contract. | The system displays contract item detail information. |  |
| 4 | Monitor purchase Contract Items by Account Assignment | Log on to the SAP Fiori Launchpad as Accounts Payable Accountant role. Click the Purchase Contract Items by Account Assignment (F2421) . | The Purchase Contract Items by Account Assignment screen appears, and the purchase contracts items are listed out. |  |
| 5 | Display for contract Item | Choose the Account assignment entered while creating contract that created with account assignment like Cost Center. | The system displays contract item detail information.If there isn't purchase contract with account assignment, it won't show anything in the list. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose Post Goods Receipt for Purchasing Document (F0843) | The Goods Receipt screen displays. |  |
| 3 | Post Goods Receipt | On the screen Post Goods Receipt for Purchasing Document, enter your purchase order number in Purchasing Document.Then make the following entries:Storage Location: 331ADelivery Note: Your delivery noteChoose Enter.Select the item and choose Post. | A list of purchase orders displays. |  |

#### Partial Reverse Goods Receipt (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods receipt posted in the previous chapter is partially reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Documents Overview | Open Material Documents Overview (F1077) . | The Material Documents Overview screen displays. |  |
| 3 | Search for Goods Receipts Material Document | On the screen Material Documents Overview, make the following entries and choose Go.Material Document: the Material Document number created in chapter 4.12 Post Goods Receipt.Year: | The relevant Material Documents / Material Document items are displayed. |  |
| 4 | Choose Your Material Document | Choose your material document item. |  |  |
| 5 | Post Partial Reverse | On the screen Material Document, choose Reverse.On the following popup window Reverse Goods Movement, choose the items you want to reverse and choose OK. |  |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Create Supplier Invoice (F0859) . | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code for zero tax. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code you selected is zero tax, you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

### Purchase Contract with Hierarchy Items Processing

Use

You can use item hierarchies in purchasing documents to structure and sort items, such as materials or services, in a hierarchy.

Prerequisite

Activate Item Hierarchies in Purchasing to active Item Hierarchy function.

Important Information: In a standard system this configuration step is switched off by default. Once the switch is on, you cannot turn it off.

|  |
| --- |
| Note If the business function SAP Supplier Relationship Management (SRM) is active, item hierarchies cannot be activated in purchasing. |

#### Create Purchase Contract with Hierarchy Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we will create a purchase contract with hierarchy item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header details | On the screen Manage Purchase Contracts, choose Create and make the following entries:Contract Type: Choose MK Quantity ContractSupplier: 33300001Purchasing Org.: The Org is the Reference Purchase Organization that defined in the Perquisite step 2.5.7, For example: 3310Valid From: Start date of the contract, for example, todayValid To: End date of the contract, for example, the end of this yearTarget value: For example, 1000 AEDCompany Code:3310 |  |  |
| 4 | Enter Contract Item details | Choose Item tab, in the Purchase Contract Items part, choose Hierarchy List button at right.Choose Create, choose Item Set, and make the following entries:Short Text: For example, Test HierachySelect the item 10 and choose Create - Material. Item 20 will be created.Make the following entries:Item Category: StandardMaterial: TG10Net price: Enter a net price , 10 AED per 1PCTarget Quantity: For example, 10.Select the item 10, choose Create - Material,Item 30 will be created and you can make the following entries:Item Category: StandardMaterial: TG11Net price: Enter a net price , 15 AED per 1PCTarget Quantity: For example, 20 | The Purchase Contract screen displays. |  |
| 5 | Save the Purchase Contract | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new Purchase Contract is created. The Purchase Contract Number is displayed. |  |

#### Approve Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase contract. If the purchase contract’s value is greater than 2000 AED, then the Purchase Contract should get approved.

Prerequisite

A purchase contract must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Purchasing Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of already created purchase contract is displayed.Note Only if the overall value is populated in the general area of the purchase contract then an approval is needed. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase contract number in the search area, then choose the Search button. | The Purchase contract that meet the criterial, the status is In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase Contract on the left of the screen and choose Approve. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Contract is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad is displayed. |  |

#### Create Purchase Order with Reference to Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we will create a purchase contract with item hierarchy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Search your purchase contract | On the screen Manage Purchase Contracts, enter your purchase contract created in chapter 4.2.1 Create Purchase Contract with Hierarchy Items in search bar, then choose Go. |  |  |
| 4 | Convert purchase contract to purchase order | Choose your purchase contract and then choose Create Purchase Order. | The Purchase Order screen displays. |  |
| 5 | Create Purchase Order | On the screen Purchase Order, in part Hierarchy Items, you will find the items in purchase contract are copied to purchase order.Go to details of item 20 and make the following entries and choose Apply:Plant: 3310Order Quantity: For example, 10Goods-Receipt-Based Invoice Verification: CheckGo to details of item 30 and make the following entries and choose Apply:Plant: 3310Order Quantity: For example, 10Goods-Receipt-Based Invoice Verification: CheckOn screen Purchase Order, choose Order. | Purchase order with hierarchy items is created. |  |

#### Approve Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All purchase orders that require authorization are listed needs to be approved.

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchasing Manager role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose Post Goods Receipt for Purchasing Document (F0843) | The Goods Receipt screen displays. |  |
| 3 | Post Goods Receipt | On the screen Post Goods Receipt for Purchasing Document, enter your purchase order number in Purchasing Document.Then make the following entries:Storage Location: 331ADelivery Note: Your delivery noteChoose Enter.Select the item and choose Post. | A list of purchase orders displays. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Create Supplier Invoice (F0859) . | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code for zero tax. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code you selected is zero tax, you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

### Versioning of Purchase Contracts

Purchase contract version management enables you to create a new change request of a purchase contract which allows the user to work on the change request contract by still having the active document as operational contract. As a Purchaser you may want to renew the contract terms or contract dates, differentiate between various versions of Contract or refer to any particular version of a contract.

Prerequisite

1. Please execute chapter [Configure Version Management in Purchase Contracts (Optional)](#unique_15) [page ] 15 to activate Purchase Contracts version management.
2. Please make sure to activate flexible workflow for purchase contract type to use versioning feature.

#### Create Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchaser creates a purchase contract in S/4HANA Hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header details | On the screen Manage Purchase Contracts, choose Create and make the following entries:Contract Type: Choose contract type, for example, WK Value ContractSupplier: 33300001Purchasing Org.: 3310Target value: your contract target value, for example, 10000 AEDValid From: Start date of the contract, for example, todayValid To: End date of the contract, for example, the end of this yearPurchasing Group:001Company code: 3310 |  |  |
| 4 |  | In the Items tab, choose Create and make the following entries:Material: , For example, TG11Target Quantity: For example, 100 .Plant: 3310Net Order Price: 15 AED |  |  |
| 5 | Save the Purchase Contract | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new Purchase Contract is created. The Purchase Contract Number is displayed |  |

#### Approve Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You approve the purchase contract if workflow is triggered for your purchase contract.

Procedure

Please refer to[Approve Purchase Contract (Optional)](#unique_28) [page ] 34 to approve your purchase contract.

#### Change Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After your purchase contract is approved, you can change the purchase contract and generate a new version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) | The Manage Purchase Contractsscreen displays. |  |
| 3 | Search purchase contract | On the Manage Purchase Contracts screen, enter search criteria to search your purchase contract.Then choose your purchase contract. | Your purchase contract displays. |  |
| 4 | Edit purchase contract | On the Purchase Contract screen, choose Edit.Navigate to General Information section. And make the following changes.Target Value: 15Reason for New Version: your Reason for Version-Related Changes.Note You need to edit a version relevant field to trigger the new purchase contract version.If Reason for New Version and Purchase Note are configured as Required, then you have to maintain manually. Otherwise they will be optional. |  |  |
| 5 | Save Purchase Contract | Choose Save.If the purchase contract requires approval, you can repeat chapter 4.15.2 Approve Purchase Contract . | New purchase contract version is created. |  |

#### Approve purchase contract with new version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you approve the purchase contract.

|  |
| --- |
| Note You must activate flexibale workflow for purchase contract if you want to use versioning of purchase contract. If you activate Automatic Release of Purchase Order, you can skip the step. |

Procedure

Please refer to chapter [Approve Purchase Contract](#unique_43) [page ] 56 to approve your purchase contract.

#### Display Version History in Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase contract is changed, you can check version history in purchase purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) | The Manage Purchase Contracts screen displays. |  |
| 3 | Search purchase contract | On the Manage Purchase Contract screen, enter search criteria to search your purchase contract.Then choose your purchase contract. | Your purchase contract displays. |  |
| 4 | Check version details | On the Purchase Contract screen, navigate to Version History section.You can check version details for this purchase contract.The lastest version is the Current Change Document.You can choose the item of Active Document to view the details of Historical Document. |  |  |
| 5 | Compare version | Choose Back.On the Purchase Contracts screen, navigate to Version History section.Select the Active Document and one of Current Change Document, and choose Compare to compare differenct versions. | The Compare Versions screen displays. |  |

#### Create Purchase Order with Reference to Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, we will create a purchase order refer to the purchase contract with hierarchy item.

Procedure

Please refer to chapter [Create Purchase Order with Reference to Purchase Contract](#unique_40) [page ] 50to create purchase order with reference to purchase contract. Please user the purchase contract you created in chapter [Create Purchase Contract](#unique_42) [page ] 55.

#### Approve Purchase Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All purchase orders that require authorization are listed needs to be approved.

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchasing Manager role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) . | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see scope item, J45 -Procurement of Direct Materials Step Review Purchase Order. |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose Post Goods Receipt for Purchasing Document (F0843) | The Goods Receipt screen displays. |  |
| 3 | Post Goods Receipt | On the screen Post Goods Receipt for Purchasing Document, enter your purchase order number in Purchasing Document.Then make the following entries:Storage Location: 331ADelivery Note: Your delivery noteChoose Enter.Select the item and choose Post. | A list of purchase orders displays. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Open Create Supplier Invoice (F0859) . | The New Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 12345678Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Baseline Date: <Today> (in Payment tab)Invoice Party: 33300001 | The New Supplier Invoices screen displays. |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and choose Enter.Reference Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <PO number> | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero. | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code for zero tax. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area.The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount (if tax code you selected is zero tax, you do not have any tax amount) | The supplier invoice is complete to post. |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. The system displays the message that the invoice xxx has been posted and document no. 51xxxxxxxx has been created. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| SAP Fiori Overview Pages for Procurement (1JI)- Real-Time Reporting and Monitoring for Procurement | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Via contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or know more detailed information in the corresponding KPI Drill-Downs. |

#### Generate Source List

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
| 1 | Log On | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Generate Source List (ME05). | The Generate Source List screen displays. |  |
| 3 | Input the value | In the Generate Source List screen, Enter the following information and choose Enter:Material: for example, TG10Plant: for example, 3310Test Run: DeselectChoose Execute. | The Source List is shown. |  |
| 4 | Source list | Select the entries that need to be added into source list, then choose Save. | The source list is saved. |  |

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
> Flagged while digesting this document, not verified: Approval threshold currency differs inside the document: the example flexible workflow start condition is 'greater than 2000 EUR' while the approval procedure says 'greater than 2000 AED'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Reference purchasing organization example values are inconsistent: the mapping step maps 3310 to a reference org (example 1410), the supplier extension step uses 1710, yet the Create Reference Purchase Contract and hierarchy-contract steps give the reference purchase organization as 'for example 3310'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table lists 'Process Purchase Requisitions - Deprecated (F1048)' for creating a contract from a requisition while the procedure uses Process Purchase Requisitions (F1048A); it also lists the Purchaser as role for the versioning Approve Purchase Contract steps whereas the referenced procedure is performed by the Purchasing Manager.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[10-procurement/test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014]]
- see-also :: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BMD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 106,166 chars in the whole document
