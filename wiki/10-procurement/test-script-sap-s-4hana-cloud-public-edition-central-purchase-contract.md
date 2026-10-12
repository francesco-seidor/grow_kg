---
id: 10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract
title: Test Script SAP S/4HANA Cloud Public Edition - Central Purchase Contracts (2ME_AE) (2ME_S4CLD2608_BPD_EN_AE)
description: "SAP test script, scope item 2ME (AE): setup and test steps for central purchase contracts, distribution, hierarchy, versioning, mass changes, situations."
cluster: 10-procurement
tags: [kb/procurement, topic/central-procurement]
aliases: [2ME_S4CLD2608_BPD_EN_AE]
keywords: ["Central Requisitioning, Purchasing and Purchase Contracts", central purchase contracts, central procurement, contract distribution, hierarchy central contracts, contract versioning, mass changes, contract monitoring, price history, situation handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ME_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-835
topic: 10-procurement/central-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Central Purchase Contracts (2ME_AE) (2ME_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ME_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Central Requisitioning, Purchasing and Purchase Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Purchase Contracts (2ME_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849594)

[2 Prerequisites 4](#_Toc232849595)

[2.1 System Access 4](#_Toc232849596)

[2.2 Roles 4](#_Toc232849597)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849598)

[2.4 Additional Manual Configuration 6](#_Toc232849599)

[2.5 Business Conditions 6](#_Toc232849600)

[2.6 Preliminary Steps 7](#_Toc232849601)

[2.6.1 Configure Flexible Workflow for Central Purchase Contracts 7](#_Toc232849602)

[2.6.2 Configure Flexible Workflow for Hierarchy Central Contracts 8](#_Toc232849603)

[2.6.3 Manage Teams and Responsibilities 8](#_Toc232849604)

[2.6.4 Create Situation Type for Expiration of Central Contract 9](#_Toc232849605)

[2.6.5 Create Situation Type for Central Contract Item Consumption 11](#_Toc232849606)

[2.6.6 Setup Analytical Reporting Currencies 12](#_Toc232849607)

[3 Overview Table 14](#_Toc232849608)

[4 Test Procedures 16](#_Toc232849609)

[4.1 Central Purchase Contracts 16](#_Toc232849610)

[4.1.1 Create Central Purchase Contracts and Distribution 16](#_Toc232849611)

[4.1.2 Release Central Purchase Contract (Optional) 28](#_Toc232849612)

[4.1.3 Display Central Purchase Contracts 29](#_Toc232849613)

[4.1.4 Schedule Output for Central Purchase Contracts (Optional) 30](#_Toc232849614)

[4.1.5 Check Source List - In Connected System 32](#_Toc232849615)

[4.1.6 Create Follow-on Documents - In Connected System 32](#_Toc232849616)

[4.1.7 Import Release Orders 33](#_Toc232849617)

[4.1.8 Display Central Purchase Contract Release Order Information 34](#_Toc232849618)

[4.1.9 Post Goods Receipt – In Connected System 35](#_Toc232849619)

[4.1.10 Create Supplier Invoice – In Connected System 36](#_Toc232849620)

[4.1.11 Renew Central Purchase Contracts 36](#_Toc232849621)

[4.1.12 Block Central Purchase Contract Items 37](#_Toc232849622)

[4.2 Mass Changes to Central Purchase Contracts 38](#_Toc232849623)

[4.3 Monitor Central Purchase Contract Items (Optional) 41](#_Toc232849624)

[4.4 Price History for Central Purchase Contract Items 43](#_Toc232849625)

[4.4.1 Schedule Update of Price Details for Central Purchase Contracts 43](#_Toc232849626)

[4.4.2 Price History for Central Purchase Contract Items 44](#_Toc232849627)

[4.5 Hierarchy Central Contracts 45](#_Toc232849628)

[4.5.1 Create Hierarchy Central Contracts 45](#_Toc232849629)

[4.5.2 Release Hierarchy Central Contract (Optional) 48](#_Toc232849630)

[4.5.3 Display Subordinate Central Contracts 48](#_Toc232849631)

[4.6 Versioning of Central Purchase Contracts 50](#_Toc232849632)

[4.6.1 Create Central Purchase Contract 50](#_Toc232849633)

[4.6.2 Release Central Purchase Contract (Optional) 52](#_Toc232849634)

[4.6.3 Change Central Purchase Contracts 53](#_Toc232849635)

[4.6.4 Display Version History in Central Purchase Contracts 54](#_Toc232849636)

[4.7 Detect and React to Situation (Optional) 55](#_Toc232849637)

[4.7.1 Detect Critical Expiration of Central Contract Situation 55](#_Toc232849638)

[4.7.2 React to Critical Expiration of Central Contract Situation 55](#_Toc232849639)

[4.7.3 Detect Critical Central Contract Item Consumption Situation 56](#_Toc232849640)

[4.7.4 React to Critical Central Contract Item Consumption Situation 56](#_Toc232849641)

## Purpose

Overview

Central contracts are global long-term agreements negotiated between an organization and a supplier. This helps in getting the best rates and conditions while bundling purchasing volume across multiple subsidiaries. These contracts are typically negotiated by the central purchasing organization, mostly at the headquarters, and used for globally driving operational efficiency, reduced cost while complying with regulations across multiple subsidiaries.

The central contract, created at the headquarters, can be distributed to subsidiaries to generate local contracts or scheduling agreements. Subsidiaries can then continue with the operational procurement in a seamless manner by leveraging this local contract or Scheduling agreement. Central monitoring of contract consumption across subsidiaries and renewal of expiring contracts is easily managed by the headquarters.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2ME_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | The SAP S/4HANA Cloud Public Edition system acts as a hub system when it is connected to multiple connected systems.Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP system from release SAP ERP6.0 EHP6 and above with add-on HUBERPI is considered as the connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher, with add-on HUBS4IC is considered as connected system.Any SAP S/4HANA Cloud Public Edition system is considered as connected system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Central Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Central Purchasing Group | 001 | Group 001 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS– MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/6e263c68b920f1384c75c79a4a076330)

### Business Conditions

Before this scope item can be tested, the following business condition must be met:

| Scope Item | Business Condition |
| --- | --- |
| 31N - Situation Handling | This scope item must be installed for situation handling steps. |

### Preliminary Steps

#### Configure Flexible Workflow for Central Purchase Contracts

Purpose

In this procedure, you configure your release conditions for Central Purchase Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Workflow for Central Purchase Contract | Choose Manage Workflows for Central Purchase Contracts (F3401). | The Manage Workflows screen displays. |  |
| 3 | Create Workflow | Choose Create and make following entries.Name: Workflow for Central Purchase ContractIn the Start Conditions area, make following entries:Company code of central purchase contract is: 3310Total net price of all central purchase contract items is greater than: 1000 AEDIn Step Sequence area choose the Create and make following entries:Step Type: Release of Central Purchase ContractAssignment By: Select User and search for Purchasing_manager from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created Workflow and choose Activate. | The Workflow is activated. |  |

#### Configure Flexible Workflow for Hierarchy Central Contracts

Purpose

In this procedure, you configure your release conditions for Hierarchy Central Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Workflow for Central Purchase Contract | Choose Manage Workflows for Central Purchase Contracts (F3401). | The Manage Workflows screen displays. |  |
| 3 | Create Workflow | Choose Create and make following entries.Name: Workflow for Hierarchy Central ContractsIn the Start Conditions area, make following entries:Company code of central purchase contract is:3310Document type of central purchase contract hierachy is : QuantityIn Step Sequence area choose the Create and make following entries:Step Type: Release of Central Purchase Contract HierarchyAssignment By: Select User and search for Purchasing_manager from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created Workflow and choose Activate. | The Workflow is activated. |  |

#### Manage Teams and Responsibilities

Purpose

In this procedure, you create teams and responsibilities for central purchasing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Manage Teams and Responsibilities screen is displayed. |  |
| 3 | Create manage team and responsibilities | Choose Create and make the following entries:Name: CCTR_TEAM (for example)Global ID: CCTR_TEAM (for example)Description: Central Purchase Contract Team (for example)Status: EnabledType: SCPRCIn Responsibility Definitions section, make the following entries:Purchasing Group: 001In Team Members section, and choose Create and make the following entries on the next screen:Business Partner: <your business partner>, for example, search Last Name for Purchaser - Central Procurement to get the user IDFunctions: SCTPUR (Central Purchasing) |  |  |
| 4 | CreateTeam | Choose Create. | The team has been created. |  |

#### Create Situation Type for Expiration of Central Contract

Purpose

In this procedure, you create situation type for Expiration of Central Contract.

When a purchaser logs into the Fiori Launchpad, will get a notification of central contracts “Central purchase contract is about to expire”. The expiration date criteria can be maintained in terms of days in custom situation types. The framework checks if the validity date of the central contract is less than or equal to the number of days that is configured. A situation is then triggered, and notification is sent. The purchaser can then navigate from the Fiori notification to the contract object. The purchaser can then choose to dismiss the situation and take corrective actions. Dismissing a situation will ensure that no further situation messaging is triggered for the same situation type and contract number. The purchaser can choose from the one of the following reasons to dismiss the situation message:

- Obsolete
- Resolved
- Invalid

|  |
| --- |
| Note 31N - Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Business Process Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Copy Standard Situation Template | On the Manage Situation Types screen, choose Go.Choose standard situation template: PROC_CENTRALCONTRACTEXPIRY Expiration of Central contract and choose Copy. |  |  |
| 4 | Create Ready-to-Use Situation Type | It will create a ready-to-use situation type.On the Situation Type screen, make the following entries:ID: ZPROC_CENTRALCONTRACTEXPIRY (for example)This field is the unique identifier of a ready-to-use situation type. The ID of a ready-to-use situation type should start with 'Z' or 'Y'. ID is a mandatory field that cannot be left blank.Name: Expiration of Central contract (for example)This field is the name of the Ready-to-Use Situation Type.Go to section Conditions:Choose Processing Order and make the following entries:Company Code: 3310Expiration Period: less than LASTDAYOFCURRENTMONTH Last day of current month (for example)Purchasing Group: 001Go to section Recipients and make the following entries:Filter by Responsibility Definitions: Purchasing groupFilter byMember Functions: Central PurchasingGo to section Situation Monitoring:Check Monitor Instances.Go to the section Batch Job Scheduling:Choose one time zone in the field Time Zone and maintain the time for the field Start Batch Job At.Choose Create. | The Ready-to-Use Situation Type has been saved. |  |
| 5 | Enable Ready-to-Use Situation Type | On the Do you want to enable the situation type? screen, choose Yes. | The ready-to-use situation type is enabled. |  |

#### Create Situation Type for Central Contract Item Consumption

Purpose

In this procedure, you create situation type for central contract item consumption.

When a purchaser logs into the Fiori launchpad will get a notification of central contracts “consumed contract %”.

For value based central contracts, the total value consumption is calculated at the item level as the aggregate of all release orders and delivery schedules created against it. A threshold consumption % value is maintained in custom situation types. When the total consumption % reaches the value that is configured, a situation is triggered, and notification is sent.

For quantity based central contracts, the total consumption is calculated at the item level. A threshold consumption % value is maintained in custom situation types. When the total quantity consumption % reaches the value that is configured, a situation is triggered, and notification is sent.

The purchaser can then navigate from the Fiori notification to the central contract object. The purchaser can then choose to set the situation status as dismiss and take corrective action offline.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Business Process Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Copy Standard Situation Template | On the Manage Situation Types screen, choose Go.Choose standard situation template PROC_CENTRALCONTRACTCONSUMPTION Central contract item consumption and choose Copy. |  |  |
| 4 | Create Ready-to-Use Situation Type | It will create a Ready-to-Use Situation Type.On the Situation Type screen, make the following entries:ID: ZPROC_CENTRALCONTRACTCONSUMPTION (for example)This field is the Unique Identifier of a Ready-to-Use Situation Type. The ID of a Ready-to-Use Situation Type should start with 'Z' or 'Y'. ID is a Mandatory Field and cannot be left blank.Name: Central contract item consumption (for example)This field is the name of the Ready-to-Use Situation Type.Go to section Condition:Choose Processing Order Instance Set to Status Open and make the following entries:Consumption Percentage: greater than or equal to 80 (for example)Purchasing Group: 001Choose Processing Order Instance Set to Status Resolved and make the following entries:Consumption Percentage : less 80 (for example)Purchasing Group: 001Go to section Recipients and make the following entries:Filter by Responsibility Definition: Product Group and Purchasing groupFilter by Member Function: Central PurchasingGo to section Situation Monitoring:Check Monitor Instances.Choose Create. | The Ready-to-Use Situation Type has been saved. |  |
| 5 | Enable Ready-to-Use Situation Type | On the Do you want to enable the situation type? screen, choose Yes. | The Ready-to-Use Situation Type is enabled. |  |

#### Setup Analytical Reporting Currencies

Purpose

In this procedure, you can setup two analytical reporting currencies that will be used in various analytical KPIs and queries Procurement in SAP S/4HANA Cloud Public Edition. If user selects one of the two configured reporting currencies as display currency in an analytical KPI, the system doesn't convert the reporting currency to display currency at runtime. This enhances the performance of the KPI.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Setup the analytical reporting currencies | Choose Sourcing and Procurement in the Application Area field, then navigate to the Procurement Analytics item by choosing the Chevron (>).On the Procurement Analytics screen, in the Configuration Steps tab, choose Configure of step 1 Setup Analytical Reporting Currencies.Choose New Entries and enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. | Reporting currencies are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Setup Analytical Reporting Currencies | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Setup Analytical Reporting Currencies. |  |  |
| 3 | Setup the analytical reporting currencies | Choose New Entries and enter below data:Reporting Curr. Id: for example, Reporting Currency 1Currency: for example, AEDChoose Save.Two reporting currencies can be setup. | Reporting currencies are added. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Central Purchase Contracts |  |  |  |
| [Create Central Purchase Contracts and Distribution](#unique_16) [page ] 16 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Release Central Purchase Contract (Optional)](#unique_17) [page ] 28 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Display Central Purchase Contracts](#unique_18) [page ] 29 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Schedule Output for Central Purchase Contracts (Optional)](#unique_19) [page ] 30 | Configuration Expert - Business Process Configuration | Schedule Output for Central Purchase Contracts (F5429) |  |
| [Check Source List - In Connected System](#unique_20) [page ] 32 | Purchaser | ECC |  |
| [Create Follow-on Documents - In Connected System](#unique_21) [page ] 32 | Purchaser | ECC |  |
| [Import Release Orders](#unique_22) [page ] 33 | Configuration Expert - Business Process Configuration | Schedule Import of Release Orders |  |
| [Display Central Purchase Contract Release Order Information](#unique_23) [page ] 34 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Post Goods Receipt – In Connected System](#unique_24) [page ] 35 | Warehouse Clerk | ECC |  |
| [Create Supplier Invoice – In Connected System](#unique_25) [page ] 36 | Accounts Payable Accountant | ECC |  |
| [Renew Central Purchase Contracts](#unique_26) [page ] 36 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Mass Changes to Central Purchase Contracts](#unique_27) [page ] 38 | Purchaser - Central Procurement | Mass Changes to Central Purchase Contracts (F3792) |  |
| [Monitor Central Purchase Contract Items (Optional)](#unique_28) [page ] 41 | Purchaser - Central Procurement | Monitor Central Purchase Contract Items (F3492) |  |
| Price History for Central Purchase Contract Items |  |  |  |
| [Schedule Update of Price Details for Central Purchase Contracts](#unique_29) [page ] 43 | Configuration Expert - Business Process Configuration | Schedule Update of Price Details for Central Purchase Contracts (F5688) |  |
| [Price History for Central Purchase Contract Items](#unique_30) [page ] 44 | Purchaser - Central Procurement | Price History for Central Purchase Contract Items (F5711) |  |
| Hierarchy Central Contracts |  |  |  |
| [Create Hierarchy Central Contracts](#unique_31) [page ] 45 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Release Central Purchase Contract (Optional)](#unique_17) [page ] 28 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Display Central Purchase Contracts](#unique_18) [page ] 29 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Versioning of Central Purchase Contracts](#unique_32) [page ] 50 |  |  |  |
| [Create Central Purchase Contract](#unique_33) [page ] 50 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Release Central Purchase Contract (Optional)](#unique_34) [page ] 52 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Change Central Purchase Contracts](#unique_35) [page ] 53 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Display Version History in Central Purchase Contracts](#unique_36) [page ] 54 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| Detect and React to Situation (Optional) |  |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Central Purchase Contracts

#### Create Central Purchase Contracts and Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchaser responsible for Central Procurement creates a central contract in SAP S/4HANA Cloud Public Edition Hub system. After maintaining the required data in General information section, he maintains the distribution entries at item level for distributing the contract items to the connected systems. A local copy of the contract/scheduling agreement gets created in the respective connected system.

Procedure

Table 2: Scenario 1 Create central quantity contract with free text material and distribute to local contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. Start Contracts creation. | The Central Purchase Contract screen displays. |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDFlexible Distribution: checkNote You can check Flexible Distribution to allow more or less than 100% distribution.You can enable single line distribution for contracts or scheduling agreements or both by using the field Single Line Distribution.In Legal Transactions section, you can assign legal transactions to central purchase contract. For details about legal transactions, please check scope item 1XV - SAP S/4HANA for Enterprise Contract Management |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Item Category: section, choose StandardMaterial Group: Your material group, for example, L002Material Description: Your material description, for example, demo materialNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 10 AEDTarget Quantity: for example, 100 EA |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section and choose Create to create new distribution entries and make the following entries:In the Item Distribution section, make the following entries:General Information section:Outline Agreement Category: ContractCompany Code: Your company code in connected system, for example, 1000Plant: section, chooseYour plant in connected system, for example, 1000Storage Location: Your Storage Location in connected system, for example, 0001Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDInfo Record Update Code: Update with or without plantNavigate to Distribution Details section:Distribution type: for example, QuantityTarget Quantity: for example, 100Choose Apply to save the Distribution.Choose Apply to save the Item.Note You can choose Use Templates to use the Distribution Template that you created in SSCUI 107336: Maintain Distribution Templates for Central Purchase Contracts |  |  |
| 7 | Save Central Contract | On the Central Purchase Contract screen , choose Save In Preparation and note down the central contract number. | Central purchase contract is created with In Preparation status. |  |
| 8 | Print Preview | On the Central Purchase Contract screen , choose Print Preview on the right upper corner. | Print Preview screen displayed. |  |
| 9 | Simulate Distribution | On the Central Purchase Contract screen, choose Edit and then choose Simulate on the right upper corner.Choose Process on the popup Warning screen. | The simulation has begun. |  |
| 10 | Check Simulation Result | On the Central Purchase Contract screen , choose Simulate Results on the right upper corner.If there is error occurred in simulation, you can click Error on the popup screen to see detail error message and fix the error before release Central Contract. | The simulation is successful. |  |
| 11 | Release Central Contract | On the Central Purchase Contract screen , choose Edit and choose Release. | Central purchase contract is released. |  |

Table 3: Scenario 2 create central value contract with material and distribute to local scheduling agreement

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contracts screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Value ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AED |  |  |
| 5 | Create Header Distribution | Navigate to Distribution section, choose Create to create new distribution entries and make the following entries:General Information section:Outline Agreement Category: Scheduling AgreementCompany Code: Your company code in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Outline Agreement Type: Your scheduling agreement type, for example, LPPlant: Your plant in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDDistribution %: 100Update Source List: checkSource List Restriction: No RestrictionChoose Apply to save the entries. |  |  |
| 6 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Material: In search help, input your connected system and search for your material, for example, METAL01Navigate to Quantity and Price section and make the following entries:Target Quantity: for example, 50 EATarget Value: 1000 |  |  |
| 7 | Maintain Item Condition | Navigate to Conditions section, choose Create.On the Create Condition Record screen, make the following entries:Plant independent: checkCondition Type: PPROValid From: todayValid From: today + 1 monthReason: your reasonChoose Create.On the Condition Amounts plant independent conditon table, make the following entries:Default Gross Price (PPRO): 20 AEDChoose Apply to save the entries. |  |  |
|  | Update Target Value | On the Central Purchase Contract screen , navigate to General Information section.On the Target Value field, choose to update target value with sum of all item target values. |  |  |
| 8 | Save and Release Central Contract | On the Central Purchase Contract screen , choose Release and note down the central contract number. | Central purchase contract is created. |  |

Table 4: Scenario 3 Create central value contract with material group item and distribute to local contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contracts screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Value ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDTarget Value: 1000You can check Flexible Distribution to allow more than 100% distribution. |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Item Category: Material groupMaterial Group: Your material group for example, L002Material Description: Your material description, for example, demo material groupNavigate to Quantity and Price section and make the following entries:Target Value: for example, 1000 AED |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section, choose Create to create new distribution entries and make the following entries:General Information section:Company Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Storage Location: Your Storage Location in connected system, for example, 0001Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDNavigate to Distribution Details section:Distribution type: for example, PercentageDistribution %: for example, 100Choose Apply to save the Distribution.Choose Apply to save the Item. |  |  |
| 7 | Save and Release Central Contract | On the Central Purchase Contract screen , choose Release and note down the central contract number. | Central purchase contract is created. |  |

Table 5: Scenario 4 Create central quantity contract with material unknown item and distribute to local contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contract screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Value ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDYou can check Flexible Distribution to allow more than 100% distribution. |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Item Category: Material unknownMaterial Group: Your material group for example, L002Material Description: Your material description, for example, demo material groupNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 10 AEDTarget Quantity: for example, 100 EA |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section, choose Create to create new distribution entries and make the following entries:General Information section:Outline Agreement Category: ContractCompany Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDNavigate to Distribution Details section:Distribution type: for example, PercentageDistribution %: for example, 100Choose Apply to save the Distribution.Choose Apply to save the Item. |  |  |
| 7 | Save and Release Central Contract | On the Create Central Contract screen , choose Release and note down the central contract number. | Central purchase contract is created. |  |

Table 6: Scenario 5 Create central quantity contract with subcontracting item and distribute to local contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contract screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDYou can check Flexible Distribution to allow more than 100% distribution. |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Item Category: SubcontractingMaterial Group: Your material group for example, L002Material Description: Your material description, for example, demo subcontractingNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 10 AEDTarget Quantity: for example, 100 EA |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section, choose Create to create new distribution entries.In the Item Distribution section, make the following entries:General Information:Company Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDNavigate to Distribution Details section:Distribution type: for example, PercentageDistribution %: for example, 100Navigate to Delivery Address section:Address Type: for example, Address Reference NumberAddress Reference Number: Your address reference number in connected systemChoose Apply to save the Distribution.Choose Apply to save the Item. |  |  |
| 7 | Save and Release Central Contract | On the Central Purchase Contract screen , choose Release and note down the central contract number. | Central purchase contract is created. |  |

Table 7: Scenario 6 Create quantity contract with consignment item and distribute to contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contract screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDYou can check Flexible Distribution to allow more than 100% distribution. |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Item Category: ConsignmentMaterial: In search help, input your connected system and search for your material, for example, METAL01Navigate to Quantity and Price section and make the following entries:Net Order Price: for example, 100 AEDTarget Quantity: for example, 10 EA |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section, choose Create to create new distribution entries.In the Item Distribution section, make the following entries:General Information:Outline Agreement Category: ContractInfo Record Update Code: Update with or without plantCompany Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDNavigate to Distribution Details section:Distribution type: for example, PercentageDistribution %: for example, 100Choose Apply to save the Distribution.Choose Apply to save the Item. |  |  |
| 7 | Save and Release Central Contract | On the Central Purchase Contract screen , choose Release and note down the central contract number. | Central purchase contract is released. |  |

|  |
| --- |
| Note Before you start test steps in Scenario 7, please make sure item hierarchies in central procurement business function has been switched on by using SSCUI Activate Item Hierarchies in Central Procurement. For detail, please check set-up instructuion for this scope item. |

Table 8: Scenario 7 Create central quantity contract with item hierarchy

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contract screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AED |  |  |
| 5 | Create Header Distribution | Navigate to Distribution section, choose Create to create new distribution entries and make the following entries:General Information section:Outline Agreement Category: ContractCompany Code: Your company code in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDDistribution %: 100Choose Apply. |  |  |
| 6 | Maintain Central Contract Item Hierarchy data | Navigate to Items section, choose Hierarchy List on the right upper corner.Choose Create -> Item Set and make following entries:Short Text: Item Set 01Select Item 10 and chose Create -> Material.Choose Details for Item 20.Navigate to General Information section and make the following entries:Item Category: StandardMaterial: Your material, for example, TG0011Navigate to Quantity and Price section and make the following entries:Net Order Price: for example, 10 AEDTarget Quantity: for example, 10 EAChoose Apply.Choose Create -> Item Set and make following entries:Short Text: Item Set 02Select Item 30 and chose Create -> Material.Choose Details for Item 40.Navigate to General Information section and make the following entries:Item Category: StandardMaterial Group: Your material group, for example, L002Material Description: Your material description, for example, Service MaterialNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 20 AEDTarget Quantity: for example, 10 EAChoose Apply. |  |  |
| 7 | Release Central Contract | On the Central Purchase Contract screen , choose Release. | Central purchase contract is released. |  |

#### Release Central Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You release the central purchase contract if workflow is triggered for your central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F0862) . | The My Inbox screen displays. |  |
| 3 | Search for Central Purchase Contract | On the My Inbox screen, enter the central purchase contract number in the search area, then choose the Search button. |  |  |
| 4 | Release Central Purchase Contract | Select the central purchase contract in left of the screen and choose Release in bottom right. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the release reason if needed, then choose Submit. | The Central Purchase Contract is released. |  |

#### Display Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a central contract is approved, you can check the distribution status and local contract/scheduling agreement in central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract displays. |  |
| 4 | Check Output Control | On the Central Purchase Contract screen, navigate to Output Control section.You can check output details.Note If the Dispatch Time is Scheduled, you need to use Fiori app Schedule Output for Central Purhase Contracts to schedule the output. |  |  |
| 5 | Check distribution status and local contract number | On the Central Purchase Contract screen, navigate to Distributed Outline Agreements section.You can check the local contract/schedule agreement number in column Outline Agreements.Note If Distribution Status is Error in Distribution, you can click Information icon in the column of Error Information to check detail error information. After error is fixed in connected system, you can select the line and choose Reinitiate Distribution to distribute central purchase contract again. |  |  |
| 6 | Check Source List Information | On the Central Purchase Contract screen, navigate to Distributed Outline Agreements section.If Update Source List is chekced in contract distribution, you can check Source List Status and click Information icon in the column of Source List Information for details.Note If Source List Status is Error, you can click Information icon in the column of Source List Information to check detail error information. After error is fixed, you can select the line and choose Reinitiate Source List to update source list again. |  |  |
| 7 | Check Local Outline Agreements | On the Central Purchase Contract screen, navigate to Distributed Outline Agreements section.Choose Outline Agreements number to display your local contract/scheduling agreements in connected system on webgui screen.If Info Record Update Code is assigned in contract distribution, you can check the updated info record by choosing Menu > Environment > Info Record in local contract / scheduling agreement.The account assignment category 'U' (Unknown) for free text and ' ' (Blank) for material are currently supported as account assignment category for central contract item.The editability of the distributed outline agreements can be configured in SSCUI Maintain Fields for Editability of Purchase Outline Agreements which is described in Set-Up Instructions for this scope item. | The Local Contract/Scheduling Agreement is displayed on connected system Webgui screen. |  |

#### Schedule Output for Central Purchase Contracts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a central contract is approved, you can schedule the output for the central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Import of Release Orders | Choose Schedule Output for Central Purchase Contracts (F5429) | The Application Jobs screen displays. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2.Job Template: Schedule Output for Central Purchase ContractsJob Name: Schedule Output for Central Purchase ContractsOn the Scheduling Options screen, make the following entries and choose Step 3.Start Immediately: checkOn the Parameters screen, make the following entries.Application Object Type: CENTRAL_PURCHASE_CONTRACTCentral Contract Number: Your Central Purchase Contract Number | The Application Jobs Detail screen displays. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Schedule Output for Central Purchase Contracts has been scheduled. |  |
| 5 | Check schedule Job status | On the Application Job screen, choose Log for the job you scheduled.Check Log Details. |  |  |

#### Check Source List - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the source list which is a updated by the central contract in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system to which employee belongs as a Purchaser . |  |  |
| 2 | Check Source List | Check the source list with transaction ME03.If Update Source List is chekced in contract distribution, you can input the Material and Plant to display the source list. You can find the new outline agreement is added in the source list. |  |  |

#### Create Follow-on Documents - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can refer the local contract/schedule agreement which is replicated from central contract in connected system to created follow-on document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system to which employee belongs as a Purchaser . |  |  |
| 2 | Create Follow-on Documents | You can refer the local purchase contract to create purchase order with transaction ME21N.Or you can refer the local scheduling agreement to create delivery schedule with transaction ME38.As only account assignment category 'U' (Unknown) and ' ' (Blank) are supported for central contract item, you need to check and change the account assignment when you create follow-on document.For local purchase contract with item category ‘W’ (Material group) and ‘M’(Material unknown), you need input the material when create purchase order. |  |  |

#### Import Release Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase order is created in the connected system, you can schedule import of the release orders to update purchase order/ delivery schedule information in central purchase contract in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Import of Release Orders | Choose Schedule Import of Release Orders | The Application Jobs screen displays. |  |
| 3 | Create New Import Job | On the Application Jobs screen, chooseCreate.On the Template Selection screen, make the following entries and choose Step 2.Job Template: Import Release Orders from Connected SystemsJob Name: Import Release Orders from Connected SystemsOn the Scheduling Options screen, make the following entries and choose Step 3.Start Immediately: checkOn the Parameters screen, make the following entries.Import Type: Ad hoc ImportConnected System ID: Your connected system IDCentral Contract From: Your Central Purchase Contract NumberCentral Contract To: Your Central Purchase Contract Number | The Application Jobs Detail screen displays. |  |
| 4 | Schedule the Job | Choose Schedule. |  |  |

#### Display Central Purchase Contract Release Order Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After release orders is imported in the hub systems, you can display the purchase order information in the central contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) | The Manage Central Purchase Contractsscreen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract displays. |  |
| 4 | Display Purchase Order information | On the Central Purchase Contract screen, navigate to Item section and choose your item.On the Central Purchase Contract Item screen, navigate to Release Documentation section.Check the Release Order information. | Your release order displays. |  |

#### Post Goods Receipt – In Connected System

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
| 1 | Log onto ECC | Access the respective connected system to which employee belongs as a Warehouse Clerk . |  |  |
| 2 | Post Goods Receipt | Post goods receipt with Transaction MIGO | Goods Receipt is posted in connected system. |  |

#### Create Supplier Invoice – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system to which employee belongs as an Accounts Payable Accountant . |  |  |
| 2 | Create Invoice Verification | Create supplier invoice with Transaction Code MIRO. | Invoice is created in the connected system. |  |

#### Renew Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test test, you renew the central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) | The Manage Central Purchase Contractsscreen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract. | Your central contract displays. |  |
| 4 | Renew central contract | Select your central purchase contract and choose Renew.On the Renew popup screen, make the following entries and choose Renew.Valid To: for example, today + 2 monthNote You can choose Advance to open central purchase contract in edit mode. | The central contract is renewed. |  |
| 5 | Display renewed central contract | On the Manage Central Purchase Contracts screen, choose your purchase contract.On the Central Purchase Contract screen, you can check the renewed contract contract details. |  |  |

#### Block Central Purchase Contract Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test step, you block the central purchase contract items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract displays. |  |
| 4 | Edit central contract | On the Central Purchase Contract screen, choose Edit. | The central contract is in Edit mode. |  |
| 5 | Block central contract | On the Central Purchase Contract screen, navigate to Items section.Select one item line and choose Block.Choose a Block Reason Code.Choose Release. | The central contract item is blocked. |  |
| 6 | Display blocked local central contract | After your centralpurchase contract is successfully distributed.On the Central Purchase Contract screen, navigate to Distributed Outline Agreements section.Choose Outline Agreements number to display your local contract/scheduling agreements in connected system on webgui screen.Check Deletion Flag field in item line is set to Blocked. |  |  |

### Mass Changes to Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can apply changes to multiple selected Central Purchase Contracts in bulk.

Procedure

Scenario 1 Use Mass Edit to change Central Purchase Contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Purchaser - Central Procurement role. |  |  |
| 2 | Access the App | Open Mass Changes to Central Purchase Contracts (F3792). | The Mass Changes to Central Purchase Contracts screen is displayed. |  |
| 3 | Search for Central Purchas Contracts | On the Mass Changes to Central Purchase Contracts screen, make the following entries:Supplier: 33300001Central Purchasing Organization: 3310Central Purchasing Group: 001Central Company Code: 3310Choose Go. | The search results show the details with the respective filter Criteria. |  |
| 4 | Set Central Purchase Contracts for Mass Edit | In the Central Purchase Contract Headers tab, select Central Purchase Contracts that you created and choose Mass Edit. | A dialog box will open displaying fields for Mass Edit. |  |
| 5 | Simulate Mass Changes | On the Mass Edit screen, make the following entries:Valid To: choose <Replace Field Value> and input the last day of current month.Choose Simulate Job. And choose Simulate on popup screen.Choose View Job on the Success popup screen. | Simulate job has been scheduled. |  |
| 6 | Apply Mass Changes | On the Monitor Mass Changes screen, choose your simulate job and check detail messages.On the simuate job detail screen, choose Apply Mass Changes.Choose Apply on popup screen. | Mass change job has been scheduled. |  |
| 7 | Check Application Job | Choose View Job on the Success popup screen or on the Mass Changes to Central Purchase Contracts screen, choose Monitor Mass Changes.You can choose Mass Change Jobs to check the job details. | Verify if the job is successful for the mass change of central purchase contracts. |  |

Scenario 2 Mass change Central Purchase Contract Distribution Percentage

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Purchaser - Central Procurement role. |  |  |
| 2 | Access the App | Open Mass Changes to Central Purchase Contracts (F3792). | The Mass Changes to Central Purchase Contracts screen is displayed. |  |
| 3 | Search for Central Purchase Contracts | On the Mass Changes to Central Purchase Contracts screen, choose Adapt Filters.On the Adapt Filters screen, choose Flexible Distribution and choose OK.Make the following entries:Supplier: 33300001Central Purchasing Organization: 3310Flexible Distribution: YesChoose Go. | The search results show the details with the respective filter Criteria. |  |
| 4 | Set Central Purchase Contracts for Distribution Change | On the Central Purchase Contract Items tab, select Central Purchase Contracts that you created and choose Item Distribu-tion. |  |  |
| 5 | Change Distribution Percentage | On the Item Distribution screen, choose Edit Distribution Percentage and make following entries:Distribution %: 80Choose Apply Mass Changes.Note You can choose Simulate Job to simulate changes for the selected Central Purchase Contract. | Mass change job has been scheduled. |  |
| 6 | Check Application Job | Choose View Job on the Success popup screen or on the Mass Changes to Central Purchase Contracts screen, choose Monitor Mass Changes.You can choose Mass Changes Jobs to check the job log details. | Verify if the job is successful for the mass change of central purchase contracts. |  |

Scenario 3 Use Excel Download/Upload to change Central Purchase Contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Purchaser - Central Procurement role. |  |  |
| 2 | Access the App | Open Mass Changes to Central Purchase Contracts (F3792). | The Mass Changes to Central Purchase Contracts screen is displayed. |  |
| 3 | Search for Central Purchas Contracts | On the Mass Changes to Central Purchase Contracts screen, choose Adapt Filters.On the Adapt Filters screen, check Central Contract and choose OK.Input your central purchase contract number and choose Go. | The search results show the details with the respective filter Criteria. |  |
| 4 | Download Central Purchase Contract | On the Mass Changes to Central Purchase Contracts screen, choose Download, and choose Central Purchase Contracts. | Central Purchase Contracts are downloaded successfully with excel format. |  |
| 5 | Change Central Purchase Contract in Excel file | Open your downloaded Excel file, and make the following changes.Change your contral purchase contract Target Value to 1500 in Central Purchase Contract Headers sheet and save the excel file. | Central Purchase Contracts are changed in excel file |  |
| 6 | Upload Excel file | On the Mass Changes to Central Purchase Contracts screen, choose Upload and choose Central Purchase Contracts.Select your changed excel file and choose Open.Note You can choose Simulate Job to simulate changes for the selected Central Purchase Contract. | Mass change job has been scheduled. |  |
| 7 | Check Application Job | Choose View Job on the Success popup screen or on the Mass Changes to Central Purchase Contracts screen, choose Monitor Mass Changes.You can choose Mass Change Jobs to check the job details. | Verify if the job is successful for the mass change of central purchase contracts. |  |

### Monitor Central Purchase Contract Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can use Monitor Central Purchase Contract Items app to analyze the central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Monitor Central Purchase Contract Items (F3492) . | The Monitor Central Purchase Contract Items screen displays. |  |
| 3 | Use the Global Filter | On the Monitor Central Purchase Contract Items screen, make the following entries.Display Currency: AEDMaterial Group: L002Choose Go. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose the Visual Filter icon in the upper right corner of the screen to toggle to the visual filter view. A donut chart is displayed that works as a visual filter and allows different filter options:Contract Consumption in % by Central Contract ItemContract Consumption in % by Item DistributionNumber Target Amount by SupplierNumber of Items by Validity StatusNumber of Items by Distribution StatusCheck if the content of the corresponding data is filtered accordingly. |  |  |
| 5 | Toggle to Different View on Content Part | Choose the Chart and Table View, Chart View, and Table View in the upper right part of the screen. | Check that Table View and Chart View are displayed correctly. |  |
| 6 | Drill Down by Dimension | Choose the View By icon (second icon on the icon bar). In the dialog box that opens, choose one dimension to drill down to a more detailed level. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose the Selected Chart Type icon. In the dialog box that opens, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Show Released Values | Go to the table section and view single contract items. For items whose released value is not equal to 0, purchase orders have been created against that contract item. | Check the historical trend of contract consumption. |  |

### Price History for Central Purchase Contract Items

#### Schedule Update of Price Details for Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule update of price details for central purchase contracts.

|  |
| --- |
| Note Before you schedule update of price details for central purchase contracts, you must configure reporting currencies in SSCUI Setup Analytical Reporting Currencies first. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Import of Release Orders | Choose Schedule Update of Price Details for Central Purchase Contracts (F5688) | The Application Jobs screen displays. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.Navigate to General Information section and make the following entries:Job Template: Update Price Details for Central Purchase ContractsJob Name: Update Price Details for Central Purchase ContractsNavigate to Scheduling Options section and make the following entries:Start Immediately: checkNavigate to Parameters section and make the following entries:Load Mode: Ad hoc LoadCentral Contract Active ID: Your Central Purchase Contract NumberNote Before you start schedule Ad-hoc Load, please make sure you have scheduled Initial Load in the system. | The Application Jobs Detail screen displays. |  |
| 4 | Schedule the Job | Choose Schedule. |  |  |

#### Price History for Central Purchase Contract Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can use Price History for Central Purchase Contract Items app to analyze the price details for central purchase contract items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Price History for Central Purchase Contract Items (F5711). | The Price History for Central Purchase Contract Items screen displays. |  |
| 3 | Use the Global Filter | On the Price History for Central Purchase Contract Items screen, make the following entries.Display Currency: AEDCondition Change Valid From: todayCondition Change Valid To: today + 1 monthCen trol Contract Item: your central purchase contract itemsChoose Go. | The corresponding data is filtered accordingly. |  |
| 5 | Toggle to Different View on Content Part | Choose the Chart and Table View, Chart View, and Table View in the upper right part of the screen. | Check that Table View and Chart View are displayed correctly. |  |
| 6 | Drill Down by Dimension | Choose the View By icon (second icon on the icon bar). In the dialog box that opens, choose one dimension to drill down to a more detailed level. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose the Selected Chart Type icon. In the dialog box that opens, choose one chart type. | Check if changing the chart type works correctly. |  |
| 8 | Show Price History | Go to the table section and view single contract items.Choose Effective Price to show the condition details. | Check the price history for central purchase contract items. |  |

### Hierarchy Central Contracts

Hierarchy Central Contract is another variant of Central Contract allowing only one level of hierarchy, shall distribute to create child Central Contract within the Central Pro-curement system.

Hierarchy Central Contract is parent of the subordinate central contracts. Subordinate Central Contracts are subset of the Hierarchy Central Contract and split of subordinate central contract(s) is based upon the company code grouping customization. Hierarchy Central Contract can have 1-N subordinate central contracts.

|  |
| --- |
| Note To distribute the items of a central purchase contract hierarchy to the connected systems in SAP S/4HANA Cloud Public Edition, you need to perform a document type mapping. This is done in the BADI Change of Outline Agreements Created from Central PC Before Distribution (MM_PUR_S4_CCTR_MOD_DISTR_CTR) in the Custom Fields and Logic app. You need to define the type of purchase contract that needs to be created for a specific type of subordinate central contract in the BADI definition. |

#### Create Hierarchy Central Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchaser responsible for Central Procurement creates a hierarchy central contract in S/4HANA Hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Hierarchy Central Contracts creation | On the Manage Central Purchase Contracts screen, choose tab Central Purchase Contract Hierarchy.Choose Create to create a new hierarchy central contract. | The Central Purchase Contract Hierarchy screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract Hierarchy screen, navigate to General Information section and make the following entries:Contract Type: QuantityValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDYou can check Flexible Distribution to allow more than 100% distribution.Note In Legal Transactions section, you can assign legal transactions to hierarchy cen-tral contract. For details about legal transactions, please check scope item 1XV - SAP S/4HANA for Enterprise Contract Management. |  |  |
| 5 | Add Header Distribution | Navigate to Distribution section, choose Add.On the Add Distribution screen, select your connected company code (for example: 1000) and choose Add. |  |  |
| 6 | Maintain Header Distribution | Make the following entries:Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 3310Purchasing Group: Your purchasing group in connected system, for example, 001Outline Agreement Category: ContractDistibtution Percentage: 100Choose Apply to save the Item. |  |  |
| 7 | Maintain Hierarchy Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Product Type: MaterialMaterial Group: Your material groupfor example, L001Material Description: Your material description, for example, demo materialNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 10Target Quantity: for example, 100 EA |  |  |
| 8 | Disable Header Distribution on Item | Navigate to Distribution section, click Distribution Enable / Disable to disable header distribution. |  |  |
| 9 | Add Item Distribution | Navigate to Distribution section, choose Add.On the Add Distribution screen, select your connected company code (for example: 1000) and choose Add. |  |  |
| 10 | Maintain Item Distribution | Navigate to Distribution section, and make the following entries on new item distribution:Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 002Outline Agreement Category: ContractDistribution Type: QuantityTarget Quantity: 100Choose Apply to save the Item. |  |  |
| 11 | Save Hierarchy Central Contract | On the Create Central Contract Hierarchy screen , choose Save In Preparation and note down the hierarchy central contract number. | Hierarchy Central Contract is created with In Preparation status.. |  |
| 12 | Release Hierarchy Central Contract | On the Create Central Contract Hierarchy screen , choose Edit and choose Release. | Hierarchy Central Contract is released. |  |

#### Release Hierarchy Central Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You release the hierarchy central contract if workflow is triggered for your hierarchy central contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F0862) . | The My Inbox screen displays. |  |
| 3 | Search for Hierarchy Central Contract | On the My Inbox screen, enter the hierarchy central contract number in the search area, then choose the Search button. |  |  |
| 4 | Release Hierarchy Central Contract | Select the hierarchy central contract in left of the screen and choose Release in bottom right. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the release reason if needed, then choose Submit. | The Hierarchy Central Contract is released. |  |

#### Display Subordinate Central Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a hierarchy central contract is approved, you can check subordinate central contracts that created by hierarchy central contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) | The Manage Central Purchase Contractsscreen displays. |  |
| 3 | Search hierarchy central contract | On the Manage Central Purchase Contracts screen, choose tab Central Purchase Contract Hierarchy.Enter search criteria to search your hierarchy central contract.Then choose your hierarchy central contract. | Your hierarchy central contract displays. |  |
| 4 | Check Subordinate Central Contract | On the Central Purchase Contract Hierarchy screen, navigate to Subordinate Central Contracts section.You can check subordinate central contract in column Central Purchase Contract.Choose Central Purchase Contract number to display the details of subordinate central contract.Note If Last Upate Status is in Error status, you can click Information icon in the column of Error Information to check detail error information. After error is fixed, you can select the line and choose Retrigger Update to update subordinate central contract again. | The Central Purchase Contract screen displays. |  |
| 5 | Check Subordinate Central Contract Details | On the Central Purchase Contract screen, you can check the detail information for subordinate central contract.Navigate to Distributed Outline Agreements section.Choose Outline Agreements number to display your local contract/scheduling agreements in connected system on webgui screen. | The Local Contract/Scheduling Agreement is displayed on connected system webgui screen |  |

### Versioning of Central Purchase Contracts

Central purchase contract version management enables you to create a new change request of a central purchase contract which allows the user to work on the change request contract by still having the active document as operational contract. As a Central Purchaser you may want to renew the contract terms or contract dates, differentiate between various versions of Contract or refer to any particular version of a contract.

To activate Central Purchase Contrasts version management, you must configure following SSCUIs in the central procurement system which is described in Set-Up Instructions for this scope item.

- Define Reasons for Version-Relevant Changes for Purchasing Documents
- Set Up Version Management for Purchasing Documents

#### Create Central Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchaser responsible for Central Procurement creates a central contract in SAP S/4HANA Cloud Public Edition Hub system. After maintaining the required data in General information section, he maintains the distribution entries at item level for distributing the contract items to the connected systems. A local copy of the contract/scheduling agreement gets created in the respective connected system.

Procedure

Table 9: Scenario 1 Create central quantity contract with free text material and distribute to local contract

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Start Contracts creation | Without making any selection, choose Create to create a new central purchase contract. | The Central Purchase Contracts screen displays |  |
| 4 | Enter Central Contract data | On the Central Purchase Contract screen, navigate to General Information section and make the following entries:Contract Type: Value ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 3310Central Purchasing Group: 001Supplier: 33300001Currency: AEDTarget Value: 1000 |  |  |
| 5 | Maintain Central Contract Item data | Navigate to Items section, choose Create.On the Central Purchase Contract Item screen, navigate to General Information section and make the following entries:Material Group: Your material groupfor example, L002Material Description: Your material description, for example, version testNavigate to Quantity and Price section and make the following entries:Net Order Price: for example, 20 AEDTarget Quantity: for example, 50 EATarget Value: 1000 |  |  |
| 6 | Distribute Contract item | Navigate to Distribution section, choose Create to create new distribution entries and make the following entries:In the Item Distribution section, make the following entries:General Information section:Outline Agreement Category: ContractCompany Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Storage Location: Your Storage Location in connected system, for example, 0001Purchasing Organization: Your purchase organization in connected system, for example, 1000Purchasing Group: Your purchasing group in connected system, for example, 001Currency: AEDNavigate to Distribution Details section:Distribution type: for example, PercentageDistribution Percentage: for example, 100Choose Apply to save the Distribution.Choose Apply to save the Item. |  |  |
| 7 | Save and Release Central Contract | On the Create Central Contract screen , choose Release and note down the central contract number. | Central purchase contract is created. |  |

#### Release Central Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You release the central purchase contract if workflow is triggered for your central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F0862) . | The My Inbox screen displays. |  |
| 3 | Search for Central Purchase Contract | On the My Inbox screen, enter the central purchase contract number in the search area, then choose the Search button. |  |  |
| 4 | Release Central Purchase Contract | Select the central purchase contract in left of the screen and choose Release in bottom right. | The Submit Decision screen displays. |  |
| 5 | Enter Release Reason | Enter the release reason if needed, then choose Submit. | The Central Purchase Contract is released. |  |

#### Change Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a central contract is approved, you can check the central purchase contract and generate a new version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) | The Manage Central Purchase Contractsscreen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract displays. |  |
| 4 | Edit central contract | On the Central Purchase Contract screen, choose Edit.Navigate to General Information section. And make the following changes.Target Value: 1500Reason for New Version: your Reason for Version-Related Changes.Note You need to edit a version relevant field (for example Target Value) for triggering the new version.If Reason for New Version and Purchase Note are configured as Required, then you have to enter them manually. Otherwise they will be optional. |  |  |
| 5 | Save Central Contract | On the Central Purchase Contract screen , choose Release.If the central purchase central requires approval, you can repeat step [Release Central Purchase Contract (Optional)](#unique_34) [page ] 52. | New central purchase contract version is created. |  |

#### Display Version History in Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a central contract is changed, you can check version history in central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Central Purchase Contracts (F3144) | The Manage Central Purchase Contracts screen displays. |  |
| 3 | Search central contract | On the Manage Central Purchase Contract screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract displays. |  |
| 4 | Check version details | On the Central Purchase Contract screen, navigate to Version History section.You can check version details for this central purchase contract.The lastest version is the Active Document.You can choose historical versions to view the details of Historical Document. |  |  |
| 5 | Compare version | Choose Back.On the Central Purchase Contracts screen, navigate to Version History section.Select the Active Document and one Historical Document, and choose Compare to compare differenct versions. | The Compare Versions screen displays. |  |

### Detect and React to Situation (Optional)

#### Detect Critical Expiration of Central Contract Situation

The system automatically detects critical situations, which refer to the expiration of central contract. The detection process is automatically triggered by the system on a regular basis and indicates critical expiration of central contract situations to the purchaser, using the notification functionality on the home screen. This enables the purchaser to proactively react to situations and avoid negative implications for the business of the company.

#### React to Critical Expiration of Central Contract Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor expiration of central contract through the notification.

Situation and Notification will be triggered according to the criteria set in the preliminary steps. System automatically detects situations of expiration of central contract situations on a daily basis, and indicates critical situations using the notification functionality on the home screen. This enables Team Member to proactively react to potential expiration of central contract and avoid negative implications for the business processes of the company.

|  |
| --- |
| Note You must perform the steps[Manage Teams and Responsibilities](#unique_11) [page ] 8 and [Create Situation Type for Expiration of Central Contract](#unique_12) [page ] 9 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Choose the notifications | Choose Notifications on the upper right part of the screen.Choose the notifications: The item XXX of purchase order XXX is overdue which is generated by the system batch daily job. | The Central Purchase Contract screen is displayed. |  |
| 3 | Check Situation Message | On the Central Purchase Contract screen, the detailed situation message is displayed on the Situations tab.You can choose Dismiss and pick a reason for dismissing the situation. | Situation Message is shown and dismissed. |  |

#### Detect Critical Central Contract Item Consumption Situation

The system automatically detects critical situations, which refer to the consumption of central contract. The detection process is automatically triggered when the release order from connected system is imported. It indicates critical situations of central contract consumption to the purchaser, using the notification functionality on the home screen. This enables the purchaser to proactively react to situations and avoid negative implications for the business of the company.

#### React to Critical Central Contract Item Consumption Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor consumption of central contract through the notification.

Situation and Notification will be triggered according to the criteria set in the preliminary steps. System automatically detects situations of central contract consumption when the release order from connected system is imported. It indicates critical situations using the notification functionality on the home screen. This enables Team Member to proactively react to potential expiration of central contract and avoid negative implications for the business processes of the company.

|  |
| --- |
| Note You must perform the steps [Manage Teams and Responsibilities](#unique_11) [page ] 8 and[Create Situation Type for Central Contract Item Consumption](#unique_13) [page ] 11 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Purchaser role. | The Fiori Launch Pad is displayed. |  |
| 2 | Choose the notifications | Choose Notifications on the upper right part of the screen.Choose the notifications: XX% of Central contract XXX / item XXX has been consumed which is generated by the system batch daily job. | The Central Purchase Contract Item screen is displayed. |  |
| 3 | Check Situation Message | On the Central Purchase Contract Item screen, the detailed situation message is displayed on the Situations tab.You can choose Dismiss and pick a reason for dismissing the situation. | Situation Message is shown and dismissed. |  |

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
> Flagged while digesting this document, not verified: Scenario titles say 'central quantity contract' (Table 5 Scenario 4 material unknown; Table 9 Scenario 1 free text) but their step 4 enters Contract Type: Value Contract.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Flexible Distribution is described as allowing 'more or less than 100%' distribution in the first scenario but 'more than 100%' in the later scenarios and hierarchy creation.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]
- related-to :: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchasing-2xt-88]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2ME_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 105,693 chars in the whole document
