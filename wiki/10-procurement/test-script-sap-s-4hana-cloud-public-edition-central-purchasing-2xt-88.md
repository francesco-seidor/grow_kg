---
id: 10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchasing-2xt-88
title: Test Script SAP S/4HANA Cloud Public Edition - Central Purchasing (2XT) (2XT_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 2XT Central Purchasing (hub system 2608): prerequisites, roles, Fiori apps and step-by-step tests for central PR/PO processing, confirmations, automation."
cluster: 10-procurement
tags: [kb/procurement, topic/central-procurement]
aliases: [2XT_S4CLD2608_BPD_EN_XX]
keywords: ["Central Requisitioning, Purchasing and Purchase Contracts", central purchasing, purchase requisitions, purchase orders, flexible workflow, supplier confirmation, purchase requisition automation, central purchase contracts, mass changes, procurement analytics]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XT_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-886
topic: 10-procurement/central-procurement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Central Purchasing (2XT) (2XT_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XT_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Requisitioning, Purchasing and Purchase Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Purchasing (2XT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232839541)

[2 Prerequisites 5](#_Toc232839542)

[2.1 System Access 5](#_Toc232839543)

[2.2 Roles 5](#_Toc232839544)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232839545)

[2.4 Additional Manual Configuration 7](#_Toc232839546)

[2.5 Preliminary Steps 7](#_Toc232839547)

[2.5.1 Configure Flexible Workflow for Centrally Managed Purchase Requisition 7](#_Toc232839548)

[2.5.2 Configure Flexible Workflow for Centrally Managed Purchase Order 9](#_Toc232839549)

[2.5.3 Configure Flexible Workflow for Central Supplier Confirmations 10](#_Toc232839550)

[2.5.4 Manage Teams and Responsibilities 11](#_Toc232839551)

[2.5.5 Create Situation Type for Approaching Delivery Date of Centrally Managed Purchase Requisitions 12](#_Toc232839552)

[2.5.6 Create Situation Type for Overdue Items of Replicated Purchase Order 14](#_Toc232839553)

[2.5.7 Set Up Pro-Rata VAT New Tax Codes - Netherlands (Optional) 15](#_Toc232839554)

[3 Overview Table 17](#_Toc232839555)

[4 Test Procedures 20](#_Toc232839556)

[4.1 Create Purchase Requisition 20](#_Toc232839557)

[4.2 Import Purchase Requisitions 21](#_Toc232839558)

[4.3 Process Purchase Requisitions Centrally 23](#_Toc232839559)

[4.4 Approve Purchase Requisition (Optional) 24](#_Toc232839560)

[4.5 Block Purchase Requisition for Central Processing 26](#_Toc232839561)

[4.6 Refresh Purchase Requisitions 27](#_Toc232839562)

[4.7 Defer and Resume Deferred Purchase Requisition 27](#_Toc232839563)

[4.8 Reassign Purchasing Group 28](#_Toc232839564)

[4.9 Assign Source of Supply 30](#_Toc232839565)

[4.10 Create Purchase Order 31](#_Toc232839566)

[4.11 Import Purchase Orders 32](#_Toc232839567)

[4.12 Manage Purchase Orders Centrally 33](#_Toc232839568)

[4.13 Approve Purchase Order (Optional) 35](#_Toc232839569)

[4.14 Schedule Output for Centrally Managed Purchase Order (Optional) 36](#_Toc232839570)

[4.15 Add Open Purchase Requisition to Purchase Order 37](#_Toc232839571)

[4.16 Post Goods Receipt – In Connected System 38](#_Toc232839572)

[4.17 Create Supply Invoice – In Connected System 39](#_Toc232839573)

[4.18 Refresh Purchase Orders 40](#_Toc232839574)

[4.19 Import History for Purchase Orders 41](#_Toc232839575)

[4.20 Check Purchase Order Centrally 42](#_Toc232839576)

[4.21 Close Purchase Requisition Items 43](#_Toc232839577)

[4.22 Central Supplier Confirmation 44](#_Toc232839578)

[4.22.1 Create Purchase Order 44](#_Toc232839579)

[4.22.2 Manage Central Supplier Confirmation 45](#_Toc232839580)

[4.22.3 Approve Central Supplier Confirmation (Optional) 47](#_Toc232839581)

[4.22.4 Check Supplier Confirmation in Purchase Order 48](#_Toc232839582)

[4.23 Mass Changes to Centrally Managed Purchase Requisitions 49](#_Toc232839583)

[4.24 Central Purchasing Analytics 52](#_Toc232839584)

[4.24.1 Monitor Purchase Requistion Items Centrally (Optional) 52](#_Toc232839585)

[4.24.2 Monitor Purchase Order Items Centrally (Optional) 53](#_Toc232839586)

[4.25 Purchase Requisition Automation 55](#_Toc232839587)

[4.25.1 Configure Automation Rules for Business Processes 55](#_Toc232839588)

[4.25.2 Schedule Automation of Business Processes 57](#_Toc232839589)

[4.25.3 Check Purchase Requisition 58](#_Toc232839590)

[4.26 Integration with Central Purchase Contracts (Optional) 59](#_Toc232839591)

[4.26.1 Create Central Purchase Contracts from Process Purchase Requisitions Centrally 59](#_Toc232839592)

[4.26.2 Add Purchase Requisition to Central Purchase Contracts from Process Purchase Requisitions Centrally 62](#_Toc232839593)

[4.26.3 Create Central Purchase Contract Automation 63](#_Toc232839594)

[4.26.3.1 Configure Automation Rules for Business Processes 63](#_Toc232839595)

[4.26.3.2 Schedule Automation of Business Processes 65](#_Toc232839596)

[4.26.3.3 Check Central Purchase Contract 66](#_Toc232839597)

[5 Appendix 68](#_Toc232839598)

[5.1 Reworkable Flexible Workflow for Centrally Managed Purchase Requisition 68](#_Toc232839599)

[5.1.1 Configure Reworkable Flexible Workflow for Centrally Managed Purchase Requisition 68](#_Toc232839600)

[5.1.2 Request Rework of Centrally Managed Purchase Requisition 69](#_Toc232839601)

[5.1.3 Resubmit Centrally Managed Purchase Requisition 70](#_Toc232839602)

[5.2 Reworkable Flexible Workflow for Centrally Managed Purchase Order 71](#_Toc232839603)

[5.2.1 Configure Reworkable Flexible Workflow for Centrally Managed Purchase Order 71](#_Toc232839604)

[5.2.2 Request Rework Centrally Managed Purchase Order 73](#_Toc232839605)

[5.2.3 Resubmit Centrally Managed Purchase Order 73](#_Toc232839606)

[5.3 Recommend Material Group Centrally 74](#_Toc232839607)

[5.4 Detect and React to Situation 76](#_Toc232839608)

[5.4.1 Detect and React to Approaching Delivery Date of Centrally Managed Purchase Requisition Situation 76](#_Toc232839609)

[5.4.2 Detect and React to Overdue Items of Replicated Purchase Order Situation 77](#_Toc232839610)

## Purpose

Overview

Central Purchasing provides centralized access and visibility to processes across industries with a deep integration into the system landscape. It is connected to the customer’s ERP systems and exchanges purchasing documents (such as purchase requisitions and purchase orders) in the connected systems. It also offers central approval process, central portal, central output management, analytics, and responsibility management of product categories.

This scope item offers one platform where a procurement specialist can work centrally on purchase requisitions and purchase orders from different backend systems. Operational procurement processes are not the only tasks to profit from the hub approach. Strategic procurement tasks (such as Supplier Management) benefit from the transparency and the ability to initiate strategic activities from a central digital procurement control center.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2XT_S4CLD2602_BPD_EN_XX.docx)). |

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition Hub system | Identifies the SAP S/4HANA Cloud Public Edition system from release 2508 and higher. The SAP S/4HANA Cloud Public Edition system acts as a hub system when it is connected to multiple connected systems.Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP system from release ERP6.0 and EHP6 above with add-on HUBERPI is considered as the connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher, with add-on HUBS4IC is considered as the connected system.Any SAP S/4HANA Cloud Public Edition 2508 and higher is considered as the connected system. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code in connected system | 1000 |  |  |
| Plant in connected system | 1000 |  |  |
| Purchase Organization in connected system | 1000 |  |  |
| Purchase Group in connected system | 001 |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/e6c88328349f28ca9f9399e7b0fd51e5)

### Preliminary Steps

#### Configure Flexible Workflow for Centrally Managed Purchase Requisition

Purpose

In this procedure, you configure workflow for Centrally Managed Purchase Requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Centrally Managed Purchase Requisition | Choose Manage Workflows for Centrally Managed Purchase Requisitions (F3794).Note There are two kinds of Centrally Managed Purchase Requisition workflow: overall workflow and item level workflow.By default, Centrally Managed Purchase Requisition triggers item level workflow.If you want to use overall workflow, you can use SSCUI Activate Overall Release of Centrally Managed Purchase Requisitions to activate the overall workflow described in the Set-Up Instructions for this scope item. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Centrally Managed Purchase Requisition Overall | Choose Approve CentrallyManaged PR-Overall.Choose Create and make the following entries.Name: Workflow for Centrally Managed Purchase Requisition OverallIn the Start Conditions areaConnected system of centrally managed purchase requisition is: Your connected systemTotal value of centrally managed purchase requisition is greater than: 1000 EURIn Workflow Steps area, choose Create and make the following entries:Step Type: Release of Centrally Managed Purchase RequisitionAssignment By: Choose User and select MANAGER_PROCUREMENT from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created Workflow Item and choose Activate. | The Workflow is activated. |  |
| 5 | Create Workflow for Centrally Managed Purchase Requisition Item Level | Choose Workflow for Centrally Managed PR Item.Choose Create and make the following entries.Name: Workflow for Centrally Managed Purchase Requisition ItemIn the Start Conditions areaPurchasing Organization of centrally managed purchase requisition is: Your purchasing organization in connected systemTotal value of centrally managed purchase requisition item is greater than: 1000 EURIn Workflow Steps area, choose Create and make the following entries:Step Type: Release of Centrally Managed Purchase RequisitionAssignment By: Choose User and select MANAGER_PROCUREMENT from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 6 | Activate Workflow | Select the created Workflow Item and choose Activate. | The Workflow is activated. |  |

#### Configure Flexible Workflow for Centrally Managed Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Centrally Managed Purchase Order | Choose Manage Workflows for Centrally Managed Purchase Orders (F3316). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Choose Create and make the following entries.Name: Workflow for Centrally Managed Purchase OrderIn the Start Conditions area:Company Code Unique ID of Centrally Managed Purchase Order is: Your company code in connected systemTotal net amount of centrally managed purchase order is greater than: 1000 EURIn Workflow Steps section, choose Create and make the following entries:Step Type: Release of Centrally Managed Purchase OrderAssignment By: Choose User and select Purchasing_manager from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created Workflow and choose Activate. | The Workflow is activated. |  |

#### Configure Flexible Workflow for Central Supplier Confirmations

Purpose

In this procedure, you configure your release conditions for central supplier confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Workflows for Central Supplier Confirmations (F6635). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Choose Create and make the following entries.Name: Workflow for Central Supplier ConfirmationIn Start Conditions area:Purchasing organization of centrally managed purchase order is: Your purchasing organization in connected systemIn Workflow Steps section, choose Create and make the following entries:Step Type: Release of Central Supplier ConfirmationAssignment By: Choose User and select Purchasing_manager from search help.Step to be completed by: One of the recipientsChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created workflow and choose Activate. | The workflow is activated. |  |

#### Manage Teams and Responsibilities

Purpose

In this procedure, you create teams and responsibilities for central purchasing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Manage Teams and Responsibilities screen is displayed. |  |
| 3 | Create manage team and responsibilities | Choose Create and make the following entries:Name: CENTRAL_TEAM_PROCGlobal ID: CENTRAL_TEAM_PROCDescription: Central Procurement TeamStatus: EnabledType: SCPRCIn Team Members section, and choose Create and make the following entries on the next screen:Business Partner: <your business partner>, for example, search Last Name for Purchasing Manager to get the user IDFunctions: SCTPUR (Central Purchasing) |  |  |
| 4 | Save Team | Choose Create. | The team has been created. |  |
| 5 | Create Sub Team | On Central Procurement Team view, choose Create Subteam and make the following entries:Name: SUB_TEAM_PROCGlobal ID: SUB_TEAM_PROCSUB_TEAM_PROCDescription: Sub Procurement TeamStatus: EnabledType: SCPRCIn Responsibility Definitions section, make the following entries:Connected System ID: <your connected system ID>, for example, QIASCCIn Team Members section, choose Create and make the following entries on the next screen:Business Partner: <your business partner>, for example, search Last Name for Purchaser - Central Procurement to get the user IDFunctions: SCTPUR (Central Purchasing)Choose Create.Choose Back. | Sub team has been created. |  |
| 6 | Show Hierarchy | Back to Manage Teams and Responsibilities view, select team Central Procurement Team and choose Show Hierarchy to see the structure of a selected team, its sub teams and super teams.From the hierarchical view, you can see a team’s members, responsibility definitions, and additional details.Note If you choose Show Hierarchy before selecting a team, you can see the structure of all the teams, their sub teams and super teams. | Team hierarchy is displayed. |  |

#### Create Situation Type for Approaching Delivery Date of Centrally Managed Purchase Requisitions

Purpose

In this procedure, you create situation type for approaching delivery date of centrally managed purchase requisitions.

When a central purchaser logs on to the SAP Fiori launchpad, a notification Approaching Delivery Date Notification will display. The delivery date criteria can be maintained in custom situation types. The framework checks if the delivery date of purchase requisition item from the connected system is less than or equal to the delivery date that is configured in custom situation types. A situation is then triggered, and notification is sent. The central purchaser can navigate from the Fiori notification to situation page, and then choose to close the situation and take corrective actions. Closing a situation will ensure that no further situation message is triggered for the same situation type and purchase requisiton number. The central purchaser can choose from the one of the following reasons to close the situation message:

- Obsolete
- Resolve
- Invalid

|  |
| --- |
| Note 31N - Situation Handling is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Situation Types - Extended (F5437). | The Manage Situation Types - Extended screen is displayed. |  |
| 3 | Create New Situation Type | On the Manage Situation Types - Extended screen, choose Create > Create Situation Type.On the Create New Situation Type popup screen, make the following entries and choose Create.ID: for example, TEST_PROC_RPLD_PR_DEL_DATE_CHECKName: for example: Approaching Delivery Date of Centrally Managed Purchase RequisitionsDescription: for example, Inform central purchasers about the approaching delivery date of the centrally managed purchase requisition items.Situation Scenario: PROC_REPLPURCHASEREQNITEMSituation Template: PROC_RPLD_PR_DEL_DATE_CHECK |  |  |
| 4 | Create Situation Type Details | On the Header Information section, make the following entry:Status: EnabledGo to section Situation Triggers – Batch-Based Triggers, choose the item.On the Item screen, click Edit button on the Filters field in Conditions section.On the Define Filters popup screen, make the following entries and choose OK.Delivery date: for example, PREVIOUS14DAYSChoose Apply.Go to the section Batch Job Scheduling, and make the following entries.Time Zone: your time zoneRepeat Type: for example, DailyRepeat Interval: for example, 6 HrsStart Time: your scheduled start timeGo to section Recipients – Responsibility by Teams and make the following entries:Filter by Member Function: Central PurchasingChoose Create.Note You can choose Trigger Batch to trigger the situation immediately. | The situation type is created. |  |

#### Create Situation Type for Overdue Items of Replicated Purchase Order

Purpose

In this procedure, you can create situation type for overdue items of replicated purchase order.

When a central purchaser logs on to the SAP Fiori Launchpad, he or she will get a notification that says Overdue items in purchase order. The delivery date criteria can be maintained in custom situation types. The framework checks if the delivery date of purchase order from the connected system is less than or equal to the delivery date that is configured in custom situation types. A situation is then triggered, and a notification will be sent. The central purchaser can navigate from the Fiori notification to situation page, and then choose to close the situation and take corrective actions. Closing a situation will ensure that no further situation message is triggered for the same situation type and purchase order number. The central purchaser can choose from the one of the following reasons to close the situation message:

- Obsolete
- Resolve
- Invalid

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Situation Types - Extended (F5437). | The Manage Situation Types - Extended screen is displayed. |  |
| 3 | Create New Situation Type | On the Manage Situation Types - Extended screen, choose Create > Create Situation Type.On the Create New Situation Type popup screen, make the following entries and choose Create.ID: for example, TEST_PROC_RPLD_PO_OVERDUE_ITEMSName: for example: Overdue Items Of Replicated Purchase OrderDescription: for example, Notify on overdue items of procurement hub replicated purchase order.Situation Scenario: PROC_PRMTHB_RPLD_PO_SCHD_LINESituation Template: PROC_RPLD_PO_OVERDUE_ITEMS |  |  |
| 4 | Create Situation Type Details | On the Header Information section, make the following entry:Status: EnabledGo to section Situation Triggers – Batch-Based Triggers, choose your item.On the Item screen, click Edit button on the Filters field in Conditions section.On the Define Filters popup screen, make the following entry and choose OK.Delivery date: for example, PREVIOUS14DAYSChoose Apply.Go to the section Batch Job Scheduling, and make the following entries.Time Zone: your time zoneRepeat Type: for example, DailyRepeat Interval: for example, 6 HrsStart Time: your scheduled start timeGo to section Recipients – Responsibility by Teams and make the following entry:Filter by Member Function: Central PurchasingChoose Create.Note You can choose Trigger Batch to trigger the situation immediately. | The situation type is created. |  |

#### Set Up Pro-Rata VAT New Tax Codes - Netherlands (Optional)

Use

For the Netherlands, if it is relevant for you, you can configure tax codes especially for pro-rata VAT (partially deductible and non-deductible VAT). To achieve this, you must perform the following steps.

Procedure

1. Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration.

Navigate to Manage Your Solution (F1241) → Configure Your Solution. You can search for a configuration step. In the search result, select the configuration item and go to the next screen. Select the configuration step and choose Configure.

SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following configuration activities:

| Configuration Activity | Instruction | Comments |
| --- | --- | --- |
| Define Tax Codes for Sales and Purchases | Create pro-rata tax codes that can trigger the automatic split of deductible and non-deductible portion |  |
| Define Pro Rata Coefficients | Define pro rata coefficients | Based on this configuration, the system can then automatically split the input VAT into deductible and nondeductible portions when an incoming invoice is posted, using the coefficient that is valid for the company code and the tax code on the relevant date.The coefficient represents the portion of the input tax that can be deducted, for example, if the pro-rata coefficient is 90% and the standard VAT rate is 21%, then 18.9% is deductible and 2.1% is non-deductible. |
| Automatic Account Determination | Assign accounts for your new tax codes | Required when you create tax codes |
| Define Enhanced Tax Box Structure | Ensure your new tax codes are reported in the VAT return | Required when you create tax codes |

1. For each of the activities, choose Open Documentation to see more details about each configuration activity.
2. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system.
3. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration.

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_15) [page ] 20 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Import Purchase Requisitions](#unique_16) [page ] 21 | Configuration Expert - Business Process Configuration | Schedule Import of Purchasing Documents (F3268) |  |
| [Process Purchase Requisitions Centrally](#unique_17) [page ] 23 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Approve Purchase Requisition (Optional)](#unique_18) [page ] 24 | Manager - Procurement | My Inbox - All Items (F0862) |  |
| [Block Purchase Requisition for Central Processing](#unique_19) [page ] 26 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Refresh Purchase Requisitions](#unique_20) [page ] 27 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Defer and Resume Deferred Purchase Requisition](#unique_21) [page ] 27 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290)/ ECC |  |
| [Reassign Purchasing Group](#unique_22) [page ] 28 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Assign Source of Supply](#unique_23) [page ] 30 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Create Purchase Order](#unique_24) [page ] 31 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290)/ ECC |  |
| [Import Purchase Orders](#unique_25) [page ] 32 | Configuration Expert - Business Process Configuration | Schedule Import of Purchasing Documents (F3268) |  |
| [Manage Purchase Orders Centrally](#unique_26) [page ] 33 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Approve Purchase Order (Optional)](#unique_27) [page ] 35 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Add Open Purchase Requisition to Purchase Order](#unique_28) [page ] 37 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Post Goods Receipt – In Connected System](#unique_29) [page ] 38 | Warehouse Clerk | ECC |  |
| [Create Supply Invoice – In Connected System](#unique_30) [page ] 39 | Accounts Payable Accountant | ECC |  |
| [Refresh Purchase Orders](#unique_31) [page ] 40 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Check Purchase Order Centrally](#unique_32) [page ] 42 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Close Purchase Requisition Items](#unique_33) [page ] 43 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| Central Supplier Confirmation |  |  |  |
| [Create Purchase Order](#unique_34) [page ] 44 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Manage Central Supplier Confirmation](#unique_35) [page ] 45 | Purchaser - Central Procurement | Manage Central Supplier Confirmations (F6634) |  |
| [Approve Central Supplier Confirmation (Optional)](#unique_36) [page ] 47 | Purchasing Manager | My Inbox - All Items (F6012) |  |
| [Check Supplier Confirmation in Purchase Order](#unique_37) [page ] 48 | Purchaser - Central Procurement | Manage Purchase Orders Centrally (F3292) |  |
| [Mass Changes to Centrally Managed Purchase Requisitions](#unique_38) [page ] 49 | Purchaser - Central Procurement | Mass Changes to Centrally Managed Purchase Requisitions (F7377) |  |
| [Central Purchasing Analytics](#unique_39) [page ] 52 |  |  |  |
| [Monitor Purchase Requistion Items Centrally (Optional)](#unique_40) [page ] 52 | Purchaser - Central Procurement | Monitor Purchase Requisition Items Centrally (F3976) |  |
| [Monitor Purchase Order Items Centrally (Optional)](#unique_41) [page ] 53 | Purchaser - Central Procurement | Monitor Purchase Order Items Centrally (F3676) |  |
| Purchase Requisition Automation |  |  |  |
| [Configure Automation Rules for Business Processes](#unique_42) [page ] 55 | Purchaser - Central Procurement | Manage Rules for Automation of Business Processes (F4042) |  |
| [Schedule Automation of Business Processes](#unique_43) [page ] 57 | Configuration Expert - Business Process Configuration | Schedule Automation of Business Processes (F3983) |  |
| [Check Purchase Requisition](#unique_44) [page ] 58 | Purchaser | ECC |  |
| [Integration with Central Purchase Contracts (Optional)](#unique_45) [page ] 59 |  |  |  |
| [Create Central Purchase Contracts from Process Purchase Requisitions Centrally](#unique_46) [page ] 59 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Add Purchase Requisition to Central Purchase Contracts from Process Purchase Requisitions Centrally](#unique_47) [page ] 62 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| Create Central Purchase Contract Automation |  |  |  |
| [Configure Automation Rules for Business Processes](#unique_48) [page ] 63 | Configuration Expert - Business Process Configuration | Manage Rules for Automation of Business Processes (F4042) |  |
| [Schedule Automation of Business Processes](#unique_49) [page ] 65 | Configuration Expert - Business Process Configuration | Schedule Automation of Business Processes (F3983) |  |
| [Check Central Purchase Contract](#unique_50) [page ] 66 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create purchase requisition in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Create Purchase Requisition | On the Process Purchase Requisitions Centrally screen, choose Create Document > Create Purchase Requisition .On the Select Plant screen, select your connected Plant for example: 1000 and choose Create. | The Create Purchase Requisition screen in connected system is displayed. |  |
| 4 | Create Purchase Requisition in connected system | On the Create Purchase Requisition screen, make the following entries:Document Type: Your purchasing requisition document type. for example, CPR (Central PR)Material: Your material, for example, METAL01Val. Price: 15Quantity: 100Plant: Your Plant, for example, 1000Stor. Loc.: Your Storage, Location for example, 0001POrg: Your Purchasing Org, for example, 1000Choose Save.Note If purchase requisition requires central approval, the Requisition Processing State is set to In External Approval automatically.Central approval for purchase requisition is defined in customizing Maintain Central Settings for Purchase Requisitions in connected system. | The purchase requisition is created in connected system. |  |

### Import Purchase Requisitions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase requisition is created in the connected system, you can schedule import of the purchasing documents to import purchase requisition to hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Import of Purchasing Documents | Choose Schedule Import of Purchasing Documents (F3268). | The Application Jobs screen is displayed. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2:Job Template: Import Purchase Requisitions from Connected SystemsJob Name: Import Purchase Requisitions from Connected SystemsOn the Scheduling Options screen, make the following entries and choose Step 3:Start Immediately: checkOn the Parameters screen, make the following entries:Import Type: Ad-hoc ImportConnected System ID: Your Connected System ID, for example QIASCCDocument Type: Your Purchase Requisition Document Type in Connected System, for example CPRDocument Number From: Your Purchase Requisition Document Number created in Connected SystemDocument Number To: Your Purchase Requisition Document Number created in Connected System | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Import Purchase Requisitions from Connected Systems has been scheduled. |  |
| 5 | Check import job status | On the Application Jobs screen, choose Log for the job you scheduled.Check Log Details. | Purchase requisition extraction completed. |  |

### Process Purchase Requisitions Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase requisition is imported from connected system to hub system, you can manage the purchase requisition centrally in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Choose your purchase requisition, and then choose Assign Processor > Assign .On theAssign Processor popup screen, choose Assign to me.In Filter, choose Assign to me as ON and choose Go.Open your purchase requisition.Note You can set Responsibility Management as ON to set the filter value defined in [Manage Teams and Responsibilities](#unique_10) [page ] 11 automatically.On the Purchase Requisition Items list page, you can choose Assigned Supplier and Created By to display detailed supplier and creator contact information (Cell Phone, Telephone and E-mail). You can also choose Format to display and add comments to your purchase requisiton.By default, the Unified Key Mapping switch that enables the search and display of purchase requisition attributes is enabled. This search is based on the key mapping of suppliers and materials in the hub system. You can also disable the Unified Key Mapping switch to perform the regular search of purchase requisition items. To do this, click Adapt Filters, and disable the switch there. For details configuration for Unified Key Mapping Service for Central Procurement, you can check Set-Up Instructions for this scope item. | The Purchase Requisition screen is displayed. |  |
| 4 | Display your Purchase Requisitions | On the Purchase Requisition Item screen, now you can check the detail data of your purchase requisition.Note You can choose Open Document to display your purchase requisition in connected system on Webgui screen. |  |  |

### Approve Purchase Requisition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You approve the backend purchase order in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Manager - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Requisition | On the My Inbox screen, enter the purchase requisition number in the search area and choose Search. |  |  |
| 4 | Navigate to Process Purchase Requisition Centrally | On the Release of Centrally Managed Purchase Requistion screen, choose the purchase requisition number. | The Purchase Requisition Item screen is displayed. |  |
| 5 | Navigate to Purchase Requisiton in the Connected System | On the Purchase Requistion Item screen, choose Open Document. | The Display Purchase Requisition webgui screen is displayed. |  |
| 6 | Edit Purchase Requisiton in the Connected System | On the Display Requisition Item webgui screen, choose Display/Change.Change Quantity to 120, and choose Save.Close the Display Purchase Requisition webgui page in the connected system. | The purchase requisition is changed in connected system. |  |
| 7 | Refresh Purchase Requisiton | On the Purchase Requisition Item screen, choose Refresh. | Refresh successfully and workflow is re-triggered. |  |
| 8 | Search for Purchase Requisition | On the Purchase Requisition Item screen, choose Back.On the My Inbox screen, enter the purchase requisition number in the search area and choose Search. |  |  |
| 9 | Approve Purchase Requisition | Select the purchase requisition on the left side of the screen and choose Approve in the lower right corner. | The Submit Decision screen is displayed. |  |
| 10 | Enter Release Reason | Enter the approval reason if needed, then choose Submit.Note The note added in the submit decision is stored in purchase requisition text Approval Notes (ID:B08) in connected system. | The Purchase Requisition is approved. |  |

### Block Purchase Requisition for Central Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You process and block the purchase requisition centrally in hub system to prevent the purchase requisition to be converted in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Process Purchase Requisition Centrally | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Then select your purchase requisition and set Process Centrally as ON. |  |  |
| 4 | Display Purchase Requisition Item | On the Purchase Requisition Item screen, choose your purchase requisition. | The Purchase Requisition Item screen is displayed. |  |
| 5 | Check Purchase Requisition Block Status | On the Purchase Requisition Item screen, choose Open Document to display your purchase requisition in connected system on Webgui screen.Navigate to Item > Status tab and check Block ID.For Purchase Requisition that created from Realtime (manual) or Self Service Procurement, the Block ID is set to Block for Central Processing. Purchase Requisition is not allowed to be edited and follow on document creation is not allowed.For other Purchase Requisition, the Block ID is set to Blocked for Follow on Document Processing Centrally. Purchase Requisition can be edited and follow on document creation is not allowed. | The purchase requisition item is blocked for central processing. |  |

### Refresh Purchase Requisitions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You refresh the purchase requisition in the Process Purchase Requisitions Centrally app to update your purchaser requistion with latest data from the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Then choose your purchase requisition. | The Purchase Requisition Item screen is displayed. |  |
| 4 | Refrsh your Purchase Requisitions | On the Purchase Requisition Item screen, choose Refresh on the upper right corner to update your purchaser requisition item with latest data from the connected system. | Refreshing is successful. |  |

### Defer and Resume Deferred Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the Process Purchase Requisitions Centrally app, you can defer the purchase requisitions and resume the deferred purchase requisitions later.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Then select your purchase requisition and choose More Actions > Defer Purchase Requisitions . | The Defer Purchase Requisitions screen is displayed. |  |
| 4 | Defer Purchase Requisitions | On the Defer Purchase Requisition screen, make the following entries:Defer Until: Date before delivery dateChoose Defer. | The purchase requisitions have been deferred.The deferred purchase requisition is removed from the purchase requisitions list. |  |
| 5 | Search for Deferred Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria and change Show Deferred Items to ON to search your deferred purchase requisition. |  |  |
| 6 | Resume Deferred Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, select your deferred purchase requisition and choose More Actions > Resume Deferred Purchase Requisitions . | The deferred purchase requisitions are resumed. |  |

### Reassign Purchasing Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You reassign purchasing group for purchase requisition in the Process Purchase Requisitions Centrally app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your connected purchase requisition whose Open Quantity is greater than 0. |  |  |
| 4 | Select Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, select your purchase requisition and choose More Actions > Reassign Purchasing Group . | The Reassign Purchasing Group screen is displayed |  |
| 5 | Reassign Purchasing Group | On the Reassign Purchasing Group screen, make the following entries and choose Reassign.Purchasing Group: <your purchasing group in connected system>, for example 002Enter comments for reassignment: <your comments> | Purchase requisition items successfully reassigned. |  |
| 5 | Open Purchase Requisition Items | On the Process Purchase Requisitions Centrally screen, choose your purchase requisition item. | The Purchase Requisition Item screen is displayed. |  |
| 6 | Check Reassigned Purchasing Group | On the Purchase Requisition Item screen, choose Refresh.Navigate to Contact Person section, check reassigned purchasing group.Navigate to Notes, check comments for reassignment.Note To replicate notes from connected system, you need complete step Manage Key Mapping for Note Type in Purchase Requisition and Purchase Order that described in the setup instruction. |  |  |

### Assign Source of Supply

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign source of supply for purchase requisition in the Process Purchase Requisitions Centrally app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Then choose your purchase requisition. | The Purchase Requisition Item screen is displayed |  |
| 4 | Assign Source of Supply | On the Manage Purchase Requisitions Centrally Purchase Requisition Item screen, navigate to Source of Supply section.Choose Assign SoS. | The Assign Source of Supply screen is displayed. |  |
| 5 | Select Source of Supply | On the Assign Source of Supply screen, select one source and choose Assign.Note If the purchase requisition in the connected system requires central approval, you need to approve this purchase requisition in central hub system by repeating the two steps [Import Purchase Requisitions](#unique_16) [page ] 21 and [Approve Purchase Requisition (Optional)](#unique_18) [page ] 24. | Source of supply is assigned for purchase requisition. |  |

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create purchase order in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your connected purchase requisition. |  |  |
| 4 | Create Purchase Order | On the Process Purchase Requisitions Centrally screen, select your purchase requisition and choose Create Document > Create Purchase Order . | The Create Purchase Order Centrally screen is displayed |  |
| 5 | Save Purchase Order | On the Create Purchase Order Centrally screen, make the following entries and choose Order.Document Type: <your document type>, for example CPOQuantity: <your value>, for example 10Price: input a value if Price is emptyNote You can choose Expert Mode to create purchase order in connected system on Webgui screen.Note If purchase order requires central approval, the Purchasing Document Processing State is set to In External Approval automatically.Central approval for purchase order is defined in customizing Activate Central Settings for Purchase Orders in connected system. | Purchase order is created in connected system. |  |

### Import Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a purchase order is created in the connected system, you can schedule import of the purchasing documents to import purchase order to hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Import of Purchasing Documents | Choose Schedule Import of Purchasing Documents (F3268). | The Application Jobs screen is displayed. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2:Job Template: Import Purchase Orders from Connected SystemsJob Name: Import Purchase Orders from Connected SystemsNavigate to Scheduling Options screen, make the following entries and choose Step 3:Start Immediately: checkOn the Parameters screen, make the following entries:Import Type: Ad Hoc ImportConnected System ID: Your Connected System ID, for example QIASCCDocument Type: Your Purchase Order Document Type in Connected System, for example, CPOPurchase Order from: Your Purchase Order Document Number created in Connected SystemPurchase Order to: Your Purchase Order Document Number created in Connected System | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Import Purchase Orders from Connected Systems has been scheduled. |  |
| 5 | Check import job status | On the Application Jobs screen, choose Log for the job you scheduled.Check Log Details | Purchase Order Extraction is completed successfully. |  |

### Manage Purchase Orders Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase order is imported from connected system to hub system, you can manage the purchase order centrally in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders Centrally | Choose Manage Purchase Orders Centrally (F3292). | The Manage Purchase Orders Centrally screen is displayed |  |
| 3 | Search for Purchase Orders | On the Manage Purchase Orders Centrally screen, enter search criteria to search your purchase order.Then choose your purchase order.Note You can set Responsibility Management as ON to set the filter value defined in [Manage Teams and Responsibilities](#unique_10) [page ] 11 automatically.By default, the Unified Key Mapping switch that enables the search and display of purchase order attributes is enabled. This search is based on the key mapping of suppliers and materials in the hub system. You can also disable the Unified Key Mapping switch to perform the regular search of purchase orders. To do this, click Adapt Filters, and disable the switch there. For details configuration for Unified Key Mapping Service for Central Procurement, you can check Set-Up Instructions for this scope item. | The Central Purchase Order screen is displayed. |  |
| 4 | Display your Purchase Orders | On the Central Purchase Order screen, now you can check the detail data of your purchase order.Note You can choose Open Document to display your purchase order in connected system on Webgui screen. |  |  |
| 5 | Print Preview | On the Central Purchase Order screen, choose Print Preview on the upper right corner. | Print Preview screen is displayed. |  |
| 6 | Display Output Details | On the Central Purchase Order screen, navigate to Output Management section.You can check output details if purchase document processing status is Active or Release completed.Note If the Dispatch Time is Scheduled, you need use fiori app Schedule Output for Centrally Managed Purchase Order (F5471) to schedule the output.To enable output management, text extraction has to be mandatorily performed by fiori app Schedule Import of Purchasing Document job template Import Texts for Purchasing Documents from Connected Systems.If the Dispatch Time is Scheduled, you need use fiori app Schedule Output for Centrally Managed Purhase Order to schedule the output. |  |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You approve the purchase order in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Order | On the My Inbox screen, enter the purchase order number in the search area, then choose Search. |  |  |
| 4 | Approve Purchase Order | Select the purchase order on the left part of the screen and choose Approve in the lower right corner. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if needed, then choose Submit.Note The note added in submit decision is stored in purchase order text defined in customizing Determine Text Types to Save Release Information of Purchase Orders in connected system. | The Purchase Order is approved. |  |

### Schedule Output for Centrally Managed Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the purchase order is in Active or Release completed status, you can schedule output for centrally managed purchase order that dispatch time is scheduled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Import of Release Orders | Choose Schedule Output for Centrally Managed Purchase Order | The Application Jobs screen displays. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2.Job Template: Schedule Output for Centrally Managed Purchase OrderJob Name: Schedule Output for Centrally Managed Purchase OrderOn the Scheduling Options screen, make the following entries and choose Step 3.Start Immediately: checkOn the Parameters screen, make the following entries.Application Object Type: Procurement Hub Replicated Purchase Orders (PRMTHB_PRLD_PURCHASE_ORDER)Conneted System ID: Your Conneted System IDPurchasing Document: Your Purchase Order Number | The Application Jobs Detail screen displays. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Schedule Output for Centrally Managed Purchase Order has been scheduled. |  |
| 4 | Check schedule Job status | On the Application Job screen, choose Log for the job you scheduled.Check log details. |  |  |

### Add Open Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You add open purchase requisitions to existing purchase order in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Select your purchase requisition whose Open Quantity is great than 0 and choose Add to Documents > Add to Purchase Order . | The Add to Purchase Order screen is displayed. |  |
| 4 | Add to Purchase Order | On the Add to Purchase Order screen, enter search criteria to search your purchase order.Select your purchase order and choose Add.Note If you receive message Purchase order is outdated, you need follow the steps Refresh Purchase Orders to Refresh the purchase order first.If the purchase order in the connected system requires central approval, you need to approve the updated purchase order in central hub system by repeating the two steps [Import Purchase Orders](#unique_25) [page ] 32 and [Approve Purchase Order (Optional)](#unique_27) [page ] 35. | The Purchase Order is updated. |  |
| 5 | Open Process Purchase Orders Centrally | Choose Process Purchase Orders Centrally. | The Process Purchase Orders Centrally screen is displayed |  |
| 6 | Check updated Purchase Order | On the Process Purchase Orders Centrally screen, enter search criteria to search your updated purchase order.Select your purchase order to check added item from purchase requisition. |  |  |

### Post Goods Receipt – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You post goods receipt in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to ECC | Access the respective connected system to which employee belongs as a Warehouse Clerk. |  |  |
| 2 | Post Goods Receipt | Post goods receipt with Transaction MIGO | Goods Receipt is posted in connected system. |  |

### Create Supply Invoice – In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

|  |
| --- |
| Caution For Netherlands, in case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in Prerequisites. |

Purpose

You create supply invoice in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to ECC | Access the respective connected system to which employee belongs as an Accounts Payable Accountant. |  |  |
| 2 | Create Invoice Verification | Create supplier invoice with Transaction MIRO. | Invoice is created in the connected system. |  |

### Refresh Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You refresh the purchase requisition in the Process Purchase Requisitions Centrally app to update your purchaser requistion with latest data from the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders Centrally | Choose Manage Purchase Orders Centrally (F3292). | The Manage Purchase Orders Centrally screen is displayed |  |
| 3 | Search for Purchase Orders | On the Manage Purchase Orders Centrally screen, enter search criteria to search your purchase order.Then choose your purchase order. | The Central Purchase Order screen is displayed. |  |
| 4 | Refrsh your Purchase Order | On the Purchase Order screen, choose Refresh on the upper right corner to update your purchaser order with latest data from the connected system. | Refreshing is successful. |  |

### Import History for Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After follow on documents for purchase order is created in the connected system, you can schedule import of the purchasing documents to import purchase order history to hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Import of Purchasing Documents (F3268). | The Application Jobs screen is displayed. |  |
| 3 | Create New Import Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2:Job Template: Import History for Purchase Orders from Connected SystemsJob Name: Import History for Purchase Orders from Connected SystemsNavigate to Scheduling Options screen, make the following entries and choose Step 3:Start Immediately: checkOn the Parameters screen, make the following entries:Import Type: Ad Hoc ImportConnected System ID: Your Connected System ID, for example, QIASCCDocument Type: Your Purchase Order Document Type in Connected System, for example, CPOPurchase Order from: Your Purchase Order Document Number created in Connected SystemPurchase Order to: Your Purchase Order Document Number created in Connected System | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Import History for Purchase Orders from Connected Systems has been scheduled. |  |
| 5 | Check Import Job Status | On the Application Jobs screen, choose Log for the job you scheduled.Check Log Details. | Extraction of purchase order history completed successfully. |  |

### Check Purchase Order Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check the updated purchase order information in Manage Purchase Orders Centrally app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders Centrally | Choose Manage Purchase Orders Centrally (F3292). | The Manage Purchase Orders Centrally screen is displayed. |  |
| 3 | Search for Purchase Orders | On the Manage Purchase Orders Centrally screen, enter search criteria to search your purchase order.Then choose your purchase order. | The Central Purchase Order screen is displayed. |  |
| 4 | Display Purchase Orders Item | On the Central Purchase Order screen, choose one item. |  |  |
| 5 | Check Schedule Lines | On the Purchase Order Item screen, choose the Schedule Lines tab.You can check the Quantity Delivered information. |  |  |
| 6 | Display Follow-on Documents | On the Purchase Order Item screen, choose the Process Flow tab.You can check the Requirement Processing, Ordering, Goods Receiving and Invoicing information. |  |  |

### Close Purchase Requisition Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You close purchase requisition items in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Select your purchase requisition whose Open Quantity is great than 0 and choose More Actions > Close Purchase Requisition . | The Close screen is displayed. |  |
| 4 | Close Purchase Requisition Items | On the Close Purchase Requisition screen, enter a close note and choose Continue. | Purchase Requisition Item is closed. |  |
| 5 | Open Purchase Requisition Items | On the Process Purchase Requisitions Centrally screen, choose your purchase requisition item. | The Purchase Requisition Item screen is displayed. |  |
| 6 | Check Closed Purchase Requisition Items | On the Purchase Requisition Item screen, choose Open Document.On the Display Purchase Requisition screen, go to Item > Quantities/Dates tab and check if Closed is selected. |  |  |

### Central Supplier Confirmation

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create purchase order in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Orders Centrally | Choose Manage Purchase Orders Centrally(F3292). | The Manage Purchase Orders Centrally screen is displayed |  |
| 3 | Create Purchase Order | On the Manage Purchase Orders Centrally screen, choose Create.On the Select Plant screen, select your connected plant, for example: 1000 and choose Create. | The Create Purchase Order screen in connected system is displayed. |  |
| 4 | Create Purchase Order in Connected System | On the Create Purchase Order screen, make the following entries:Document Type: Your purchase order document type. for example, CPO (Central PO)Supplier: Your material, for example, VEND_SPROCHeader dataPurch. Org.: Your Purchasing Org, for example, 1000Purch. group.: Your purchasing org, for example, 001Company Code.: Your purchasing org, for example, 1000Item dataMaterial: Your material, for example, METAL01PO Quantity: 100Net Price: 15Plant: Your plant, for example, 1000Stor. Location: Your storage location, for example, 0001Choose Confirmations tab.Conf. Control: ConfirmationsChoose Save. | The purchase order is created in connected system. |  |
| 5 | Import Purchase Order | Repeat steps described in [Import Purchase Orders](#unique_25) [page ] 32 to import your purchase order from connected system to SAP S/4HANA Cloud Public Edition hub system. |  |  |

#### Manage Central Supplier Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create supplier confirmation for purchase order in hub system.

Procedure

Scenario A: Create Supplier Confirmation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Supplier Confirmations (F6634). | The Manage Central Supplier Confirmation screen is displayed. |  |
| 3 | Create Central Supplier Confirmation | On the Manage Central Supplier Confirmation screen, choose Create.On the Central Supplier Confirmation screen, make following entry:Reference Purchase Order: your purchase orderNote If you get message Cannot create supplier confirmation, the referenced PO has been modified, you can use Manage Purchase Orders Centrally app to refresh your purchase order in the hub system. |  |  |
| 4 | Create Confirmation Item | Navigate to Confirmation Item section, and input the purchase order item in the Purchase Order Item field. Click the chevron on the right to display the confrimation line details.On the Central Supplier Confirmation Item screen, make the following entry:Confirmed Net Order Price: 14Note If you want to change net order price, please make sure Adopt Price Change is set for your confirmation category in Confirmation Control in the connected system. |  |  |
| 5 | Create Confirmation Line | On the Central Supplier Confirmation Item screen, navigate to the Confirmation Line section, and make the following entries:Delivery Date: todayConfirmed Quantity: <your confirmed quantity>Choose Apply. |  |  |
| 6 | Create Supplier Confirmation | On the Central Supplier Confirmation screen, choose Create. | Supplier confirmation created successfully. |  |

Scenario B: Use Quick Create for Purchase Order Confirmation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central Supplier Confirmations (F6634). | The Manage Central Supplier Confirmation screen is displayed |  |
| 3 | Create Central Supplier Confirmation | On the Manage Central Supplier Confirmation screen, choose Quick Create.On the Quick Create popup screen, make following entries:Referance Purchase Order: your purchase orderConnected System: your connected systemChoose Quick Create. | The Central Supplier Confirmation screen is displayed. |  |
| 6 | Create Supplier Confirmation | On the Central Supplier Confirmation screen, choose Create. | Supplier confirmation is created successfully. |  |

#### Approve Central Supplier Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You approve the central supplier confirmation in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose My Inbox - All Items (F6012). | The My Inbox screen is displayed. |  |
| 3 | Search for Central Supplier Confirmation | On the My Inbox screen, enter your central supplier confirmation number in the search area, then choose Search. |  |  |
| 4 | Approve Central Supplier Confirmation | Select the central supplier confirmation on the left part of the screen and choose Approve in the lower right corner. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter approval reason if needed, then choose Submit. | The purchase order is approved. |  |

#### Check Supplier Confirmation in Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check the supplier confirmation information in app Manage Purchase Orders Centrally (F3292).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchase Orders Centrally (F3292). | The Manage Purchase Orders Centrally screen is displayed. |  |
| 3 | Search for Purchase Orders | On the Manage Purchase Orders Centrally screen, enter search criteria to search your purchase order.Then choose your purchase order. | The Central Purchase Order screen is displayed. |  |
| 4 | Refresh Purchase Orders Item | On the Central Purchase Order screen, choose Refresh. | Purchase order is refreshed. |  |
| 5 | Display Purchase Orders Item | On the Central Purchase Order screen, choose one item. |  |  |
| 6 | Check Supplier Confirmation | On the Purchase Order Item screen, choose the Supplier Confirmaion tab.You can check the supplier confirmation details. |  |  |

### Mass Changes to Centrally Managed Purchase Requisitions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can select multiple centrally managed purchase requisitions and apply changes to them in bulk.

Procedure

Table 1: Scenario 1: Use Mass Edit to Mass Change Centrally Managed Purchase Requisitions

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad with the Purchaser - Central Procurement role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Mass Changes to Centrally Managed Purchase Requisitions (F7377). | The Mass Changes to Centrally Managed Purchase Requisitions screen is displayed. |  |
| 3 | Search for Centrally Managed Purchase Requisitions | On the Mass Changes to Centrally Managed Purchase Requisitions screen, make the following entries:Connected System: Your connected systemCompany Code: Your connected company codePlant: Your connected plantPurch. Organization: Your connected purchasing organizationChoose Go. | The search results show the details with the respective filter criteria. |  |
| 4 | Set Centrally Managed Purchase Requisitions for Mass Edit | In the Central Requisition Items tab, select the purchase requisition item that you created and choose Mass Edit. | A dialog box displaying fields for mass edit opens. |  |
| 5 | Simulate Mass Changes | On the Mass Edit screen, make the following entries:Item Description: choose Replace Field Value and input your new item description.Choose Simulate Job, and then choose Simulate on popup screen.Choose View Job List on the Success popup screen. | Your simulate job has been scheduled. |  |
| 6 | Apply Mass Changes | On the Monitor Mass Changes screen, choose your simulate job and check detail messages.On the simuate job detail screen, choose Apply Mass Changes.Choose Apply on popup screen. | Mass change job has been scheduled. |  |
| 7 | Check Application Job | Choose View Job on the Success popup screen or on the Mass Changes to Centrally Managed Purchase Requisitions screen, choose Monitor Mass Changes.You can choose Mass Change Jobs to check the job log details.. | Verify whether the job is successful for the mass change of centrally managed purchase requisitions. |  |

Table 2: Scenario 2: Use Excel Download/Upload to Conduct Centrally Managed Purchase Requisitions Mass Change

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad with the Purchaser - Central Procurement role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Mass Changes to Centrally Managed Purchase Requisitions (F7377). | The Mass Changes to Centrally Managed Purchase Requisitions screen is displayed. |  |
| 3 | Search for Centrally Managed Purchase Requisitions | On the Mass Changes to Centrally Managed Purchase Requisitions screen, make the following entries:Connected System: Your connected systemCompany Code: Your connected company codePlant: Your connected plantPurch. Organization: Your connected purchasing organizationChoose Go. | The search results show the details with the respective filter criteria. |  |
| 4 | Download Centrally Managed Purchase Requisitions | In the Purchase Requisition Items tab, select the purchase requisition item and choose Download. | Purchase requisitions in Excel format are successfully downloaded. |  |
| 5 | Change Centrally Managed Purchase Requisitions in Excel File | Open the Excel file you downloaded, and make the following changes.Change your Purchase Requisition Description in Purchase Requisition Item sheet and save the Excel file. | Purchase requisitions are changed in Excel file. |  |
| 6 | Upload Excel File | On the Mass Changes to Centrally Managed Purchase Requisitions screen, choose Upload.On the popup Upload Spreadsheet screen, select your changed Excel file and choose Upload.Note You can choose Simulate Job to simulate changes for the selected purchase requisitions. | The mass change job has been scheduled. |  |
| 7 | Check Application Job | Choose View Job on the Success popup screen or on the Mass Changes to Centrally Managed Purchase Requisitions screen, and choose Monitor Mass Changes.You can choose Mass Change Jobs to check the job log details.. | You can check if the mass change job of centrally managed purchase requisitions is successful. |  |

### Central Purchasing Analytics

Central Purchasing Analytics provides users with centralized analyses and the necessary capabilities to better understand the procurement scenarios – both on a holistic level and on a more fine-granular level.

#### Monitor Purchase Requistion Items Centrally (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can use Monitor Purchase Requisition Items Centrally app to analyze the purchase orders centrally in SAP S/4HANA Cloud Public Edition hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Monitor Purchase Order Items Centrally | Choose Monitor Purchase Requisition Items Centrally (F3976). | The Monitor Purchase Requisition Items Centrally screen is displayed. |  |
| 3 | Use the Global Filter | On the Monitor Purchase Requisition Items Centrally screen, make the following entries:Display Currency: EURPurchasing Org.: 1000Purchasing Group: 001Material Group: L002Choose Go. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter in the upper right corner of the screen to toggle to the visual filter view. A donut chart that works as a visual filter and allows different filter options is displayed:Total Value by Purchasing GroupTotal Value by Requisition StatusItem Count by Delivery Date IntervalItem Count by Delivery StatusCheck if the content of the corresponding data is filtered accordingly. |  |  |
| 5 | Toggle to Different View on Content Part | Choose the Chart and Table View, Chart View, and Table View in the upper right part of the screen. | Check if Table View and Chart View are displayed correctly. |  |
| 6 | Drill Down by Dimension | Choose View By (the second icon on the icon bar). In the dialog box, choose one dimension to drill down to a more detailed level. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |

#### Monitor Purchase Order Items Centrally (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can use Monitor Purchase Order Items Centrally app to analyze the purchase orders centrally in SAP S/4HANA Cloud Public Edition hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Monitor Purchase Order Items Centrally | Choose Monitor Purchase Order Items Centrally (F3676). | The Monitor Purchase Order Items Centrally screen is displayed. |  |
| 3 | Use the Global Filter | On the Monitor Purchase Orders Items Centrally screen, make the following entries:Display Currency: EURPurchasing Org.: 1000Purchasing Group: 001Material Group: L002Choose Go. | The corresponding data is filtered accordingly. |  |
| 4 | Toggle to Visual Filter | Choose Visual Filter in the upper right corner of the screen to toggle to the visual filter view. A donut chart that works as a visual filter and allows three different filter options is displayed:Item Count by Next Delivery StatusItem Count by Next DeliveryTotal Value by Purchasing Org.Total Value by Material GroupTotal Value by SupplierCheck if the content of the corresponding data is filtered accordingly. |  |  |
| 5 | Toggle to Different View on Content Part | Choose the Chart and Table View, Chart View, and Table View in the upper right part of the screen. | Check if Table View and Chart View are displayed correctly. |  |
| 6 | Drill Down by Dimension | Choose View By (the second icon on the icon bar). In the dialog box, choose one dimension to drill down to a more detailed level. | Check if the drill-down function works correctly. |  |
| 7 | Change Chart Type | Choose Selected Chart Type. In the dialog box, choose one chart type. | Check if changing the chart type works correctly. |  |

### Purchase Requisition Automation

#### Configure Automation Rules for Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure automation rules for purchase requisition processes.

Following complex actions are pre-delivered for purchase requisition.

ASSIGN_SOS: Assign Source of Supply (The assignment works only if there is unique one source of supply for purchase requisition.)

CREATE_PO: Create Purchase Order from Purchase Requisition

CREATECCTR: Create Central Purchase Contract

You can use SSCUI Define Actions for Configuring the Automation of Business Processes to define your actions required for configuring the automation of business processes, such as assign Business Objects (optional), Action Type, Action Sub Type, and specify if the action is grouping enabled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Automation Rules for Business Processes | Choose Manage Rules for Automation of Business Processes (F4042). | The Manage Automation Rules for Business Processes screen is displayed. |  |
| 3 | Create Automation Rules for Business Processes | Choose Create.In the General Informationsection, make the following entries:Rule: <your rule ID>, for example: ZPR_RULERule Description: <your rule description>, for example: PR Automation RuleStatus: checkValid From: todayValid To: todayStarting Business Object: PrmtHbRpldPurchaseRequisitionIn the Connected Systemsection, choose Create and select your connected system.In the Selection Criteriasection, choose Create and make the following entries:Connected System ID: <your connected system ID>Node Type: PrmtHbRpldPurchaseReqnItemField Name: PROCMTHUBPURCHASEREQUISITIONOperator: EQValid From: your purchase requisition numberChoose Apply. |  |  |
| 4 | Create Activity | In the Activity section, choose Create and make the following entries:Activity ID: <your activity ID>, for example: ZPR_ACTActivity Description: <your activity description>, for example: PR Automation ActivitiesIn the Actions section, choose Create and make the following entries:Unique Action Name: <your action name>, for example: Assign SoSUnique Action ID: <your action ID >, for example: ZACT_01Action Definition: ASSIGN_SOSObject Type: PrmtHbRpldPurchaseRequisitionChoose Apply.In the Actions section, choose Create and make the following entries:Unique Action Name: <your action name >, for example: Create POUnique Action ID: <your action ID >, for example: ZACT_02Action Definition: CREATE_POObject Type: PrmtHbRpldPurchaseRequisitionIn the Status section, make the following entries:Set Status for Action with Passed Outcome: AutomatedSet Status for Action with Failed Outcome: Automation FailedIn the Prerequisite section, choose Create and select Action ZACT_01(Assign SOS).Choose Apply.Choose Apply. |  |  |
| 4 | Save Automation Rules for Business Processes | Choose Create. | The Automation Rules for Purchase Requisition is saved. |  |

#### Schedule Automation of Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You schedule automation of business processes in the hub system.

|  |
| --- |
| Note Before you start performing this step, you need to make sure that the purchase requisition has been imported to the hub system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Automation of Business Processes | Choose Schedule Automation of Business Processes (F3983). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2Job Template: Schedule Automation of Business ProcessesJob Name: Schedule Automation of Business ProcessesOn the Scheduling Options screen, make the following entries and choose Step 3:Start Immediately: Selected | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Schedule Automation of Business Processes has been scheduled. |  |
| 5 | Check import job status | On the Application Jobs screen, choose Log for the job you scheduled.Check Log Details. |  |  |

#### Check Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check purchase requisition details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access the respective connected system to which employee belongs as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Manage Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Search for Purchase Requisitions | On the Manage Purchase Requisitions Centrally screen, enter search criteria to search your purchase requisition.Choose Settings and check Automation Status in Columns.Choose Show Details and check Automation Status.Note For purchase requisition in Automation Failed status, you can choose More Actions > Display Automation Errors to show the error details. After error is fixed, in the Automation Error popup screen, you can select the purchase requisition or automation rule and choose Retrigger to restart the automation process for your purchase requisiton. | The Purchase Requisition Item screen is displayed. |  |
| 4 | Display your Purchase Requisitions | Choose your purchase requisition.On the Purchase Requisition Item screen, now you can check the detail data of your purchase requisition.You can choose Open Document to display your purchase requisition in connected system on Webgui screen.Go to Item > Source of Supply tab and check source of supplyGo to Item > Status tab and check if process status is PO Created. |  |  |

### Integration with Central Purchase Contracts (Optional)

To start this chapter, you need make sure the 2ME -Central Purchase Contracts scope item is activated in your system and you have completed the additional configuration steps that are described in the Set-Up Instructions for 2ME - Central Purchase Contracts scope item.

#### Create Central Purchase Contracts from Process Purchase Requisitions Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can create Central Purchase Contracts with the Process Purchase Requisitions Centrally app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, make the following entries:Company Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchasing organization in connected system, for example, 1000Material: Your material in connected system, for example, METAL01Processing Status: N (Not Edited)Choose Go.Note If there is no suitable purchase requistion, you can create a new purchase requisition by repeating the steps [Create Purchase Requisition](#unique_15) [page ] 20 and [Import Purchase Requisitions](#unique_16) [page ] 21. | The search results show the details with the respective filter criteria. |  |
| 4 | Create Central Purchase Contract | On the Process Purchase Requisitions Centrally screen, select the purchase requisition item and choose Create Document > Create Central Purchase ContractNote If you want to create a Central Purchase Contract Hierarchy, you can choose Create Document > Create Central Purchase Contract Hierarchy . | The Central Purchase Contract screen is displayed. |  |
| 5 | Maintain Central Purchase Contract Data | On the Central Purchase Contract screen, navigate to the General Information section and make the following entries:Contact Type: Quantity ContractValid from: for example, todayValid to: for example, today + 1 monthCentral Purchasing Organization: 1010Central Purchasing Group: 001Supplier: 10300001Currency: EURNavigate to the Items section and choose Central Purchase Contract item. | The Central Purchase Contract screen is displayed. |  |
| 6 | Maintain Central Contract Item Data | Navigate to Conditions section, choose Create.On the Central Condition Record screen, make the following entries:Condition Type: PPR0Valid From: todayValid Fromto: today + 1 monthChoose Create.On the Condition Amounts table, make the following entries:Default Gross Price (PPR0): 15 EURChoose Apply to save the Item. |  |  |
| 7 | Save Central Contract | On the Create Central Contract screen, choose Release. | Central purchase contract is created.Note For further central purchase contract process, you can refer to the test script 2ME - Central Purchase Contracts. |  |
| 8 | Open Purchase Requisition Item | Choose Back and choose your purchase requisition item.On the Purchase Requisition Item screen, choose Open Document. |  |  |
| 9 | Check Process Status | On the new Display Purchase Requisition screen, open Item > Status tab.Proc. Status is set to External Contract Created, if the central purchase contract is in In Distribution status.Proc. Status is set to Contract Created, if the central purchase contract is in Distributed status. |  |  |

#### Add Purchase Requisition to Central Purchase Contracts from Process Purchase Requisitions Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can add purchase requisiton to the existing Central Purchase Contracts with the Process Purchase Requisitions Centrally app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Process Purchase Requisitions Centrally | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, make the following entries:Company Code: Your company code in connected system, for example, 1000Plant: Your plant in connected system, for example, 1000Purchasing Organization: Your purchasing organization in connected system, for example, 1000Material: Your material in connected system, for example, METAL01Processing Status: N (Not Edited)Choose Go.Note If there is no suitable purchase requistion, you can create a new purchase requisition by repeating the steps [Create Purchase Requisition](#unique_15) [page ] 20 and [Import Purchase Requisitions](#unique_16) [page ] 21. | The search results show the details with the respective filter criteria. |  |
| 4 | Add to Central Purchase Contract | On the Process Purchase Requisitions Centrally screen, select the purchase requisition item and choose Add to Document > Add to Central Purchase Contract . | The Add to Central Purchase Contract screen is displayed. |  |
| 5 | Select Central Purchase Contract Data | On the Add to Central Purchase Contract screen, select a central purchase contract and choose Add. | Purchase requisition items added to Central Purchase Contract. |  |
| 6 | Open Central Purchase Contract | In the dialog box, choose the central purchase contract number to open the central purchase contract. | The Central Purchase Contract screen is displayed. |  |
| 7 | Check Central Purchase Contract | On the Central Purchase Contract screen, navigate to the General Information section and check if the Contract In Preparation is set to Yes.Navigate the Items section, check the last item which is added from the purchase requisition.Choose the added item. | The Central Purchase Contract Item screen is displayed. |  |
| 8 | Check Central Purchase Contract Item | On the Central Purchase Contract Item screen, navigate to the Distribution section, choose the distribution item.Check the Referenced Purchase Requistion and Referenced Purchase Requistion Item. | For further central purchase contract process, you can refer to the test script 2ME - Central Purchase Contracts. |  |

#### Create Central Purchase Contract Automation

##### Configure Automation Rules for Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure automation rules for create central purchase contract from purchase requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Automation Rules for Business Processes | Choose Manage Rules for Automation of Business Processes (F4042). | The Manage Automation Rules for Business Processes screen is displayed. |  |
| 3 | Create Automation Rules for Business Processes | Choose Create.In the General Information section, make the following entries:Rule: <your rule ID>, for example, ZCCTR_RULERule Description: <your rule description>, for example, CCTR Automation RuleStatus: checkValid From: todayValid To: todayStarting Business Object : PrmtHbRpldPurchaseRequisitionIn the Connected System section, choose Create and select your connected system.In the Selection Criteria section, choose Create and make the following entries:Connected System ID: <your connected system ID>Node Type: PrmtHbRpldPurchaseReqnItemField Name: PROCMTHUBPURCHASEREQUISITIONOperator: EQValid From: your purchase requisition numberChoose Apply.Note You can create a new purchase requisition by repeat steps [Create Purchase Requisition](#unique_15) [page ] 20 and [Import Purchase Requisitions](#unique_16) [page ] 21.In the Selection Criteria section, choose Create and make the following entries:Connected System ID: <your connected system ID>Node Type: PrmtHbRpldPurchaseReqnItemField Name: PROCESSINGSTATUSOperator: EQValid From: NChoose Apply. |  |  |
| 4 | Create Activity | In the Activity section, choose Create and make the following entries:Activity ID: <your activity ID>, for example, ZCCTR_ACTActivity Description: <your activity description>, for example, CCTR Automation ActivitiesIn the Actions section, choose Create and make the following entries:Unique Action Name: <your action name>, for example, Create CCTRUnique Action ID: <your action ID>, for example, ZACT_CCTRAction Definition: CREATECCTRChoose Apply.Choose Apply. |  |  |
| 5 | Save Automation Rules for Business Processes | Choose Save. | The automation rules for creating central purchase contract are saved. |  |

##### Schedule Automation of Business Processes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You schedule automation of business processes in the hub system.

Before you start performing this step, you need to make sure that the purchase requisition has been imported to the hub system.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction |  | Pass / Fail / Comment |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Automation of Business Processes | Choose Schedule Automation of Business Processes (F3983). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create.On the Template Selection screen, make the following entries and choose Step 2Job Template: Schedule Automation of Business ProcessesJob Name: Schedule Automation of Business ProcessesOn the Scheduling Options screen, make the following entries and choose Step 3:Start Immediately: Selected | The Application Jobs Detail screen is displayed. |  |
| 4 | Schedule the Job | Choose Schedule. | Job Schedule Automation of Business Processes has been scheduled. |  |
| 5 | Check import job status | On the Application Jobs screen, choose Log for the job you scheduled.Check Log Details. | Central contract creation was successful. |  |

##### Check Central Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check the central purchase contract that is created by the automation process in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed |  |
| 2 | Open Manage Central Purchase Contracts | Choose Manage Central Purchase Contracts (F3144). | The Manage Central Purchase Contracts screen is displayed |  |
| 3 | Search for Central Purchase Contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | The Central Purchase Contract screen is displayed. |  |
| 4 | Display your Central Purchase Contract | On the Central Purchase Contract screen, you can check the detail data of your central purchase contract. |  |  |

## Appendix

### Reworkable Flexible Workflow for Centrally Managed Purchase Requisition

#### Configure Reworkable Flexible Workflow for Centrally Managed Purchase Requisition

Purpose

In this procedure, you configure your release conditions for reworkable workflow for centrally managed purchase requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Workflows for Centrally Managed Purchase Requisitions (F3794). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Choose Approve Centrally Managed PR-Overall.Choose Create and make the following entry:Name: Reworkable Workflow for Centrally Managed Purchase RequisitionIn the Start Conditions area:Company Code Unique ID of centrally managed purchase requisition is: Your company code in connected systemTotal value of centrally managed purchase requisition is greater than: 2000 EURIn Workflow Steps section, choose Create and make the following entry:Step Type: Release of Reworkable Centrally Managed Purchase RequisitionIn Recipients section, make the following entries:Assignment By: Choose User and select manager_procurement from search help.Step to be completed by: One of the recipientsIn Rework Requested section, make the following entry:Required Action: Rework Centrally Managed Purchase RequisitionIn Recipients section, choose User and select your rework user from search help.Note Role: Determined is not automatically supported.Rework user need to have business catalog SAP_MM_BC_PR_WIAPPROVE_PC assigned.Action Result: Repeat stepChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created workflow and choose Activate. | The workflow is activated. |  |

#### Request Rework of Centrally Managed Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You request to rework the centrally managed purchase requisition in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Manager - Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Requisition | On the My Inbox screen, enter the purchase requisition number in the search area, then choose Search. |  |  |
| 4 | Request Rework Purchase Requisition | Select the purchase requisition on the left part of the screen and choose Request Rework. | The Submit Decision screen is displayed. |  |
| 5 | Enter Rework Reason | Enter the rework reason in the Submit Decision dialog, and then choose Submit. | The rework of centrally managed purchase requisition starts. |  |

#### Resubmit Centrally Managed Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You resubmit the purchase requisition in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Choose My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Requisition | On the My Inbox screen, enter the purchase requisition number in the search area, then choose Search. |  |  |
| 4 | Resubmit Purchase Requisition | Select the purchase requisition on the left part of the screen and choose Resubmit. | The Submit Decision screen is displayed. |  |
| 5 | Enter Resubmit Note | Enter the resubmit note in the Submit Decision dialog then choose Submit. | The purchase requisition is resubmitted for approval. |  |

### Reworkable Flexible Workflow for Centrally Managed Purchase Order

#### Configure Reworkable Flexible Workflow for Centrally Managed Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure your release conditions for reworkable workflow for centrally managed purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Workflows for Centrally Managed Purchase Orders (F3316). | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow | Choose Create and make the following entry:Workflow Name: Reworkable Workflow for Centrally Managed Purchase OrderIn the Start Conditions area:Choose Company Code Unique ID of Centrally Managed Purchase Order is from the dropdown list.Company Code: Your company code in connected systemChoose + (Create another condition)Choose Total net amount of centrally managed purchase order is greater than from the dropdown list.Amount: 2000Currency: EURIn Workflow Steps section, choose Create and make the following entries:Step Type: Release of Reworkable Centrally Managed Purchase OrderIn Recipients section, make the following entries:Assignment By: choose User from the dropdown listUser: select Purchasing_manager from search help.Step to be completed by: select One of the recipientsIn Rework Requested section, make the following entries:Required Action: Rework Centrally Managed Purchase OrderIn Recipients section, choose User and select your rework user from search help.Note Role: Determined automatically is not supported.Rework users need to have business catalog SAP_MM_BC_PO_WIAPPROVE_PC assigned to them.Action Result: select Repeat stepChoose Create.Choose Save. |  |  |
| 4 | Activate Workflow | Select the created workflow and choose Activate. | The workflow is activated. |  |

#### Request Rework Centrally Managed Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You request to rework the centrally managed purchase order in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open My Inbox | Choose My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Order | On the My Inbox screen, enter the purchase order number in the search area, then choose Search. |  |  |
| 4 | Request Rework | Select the purchase order on the left part of the screen and choose Request Rework. | The Submit Decision screen is displayed. |  |
| 5 | Enter Rework Reason | Enter the rework reason in the Submit Decision dialog, and then choose Submit. | The centrally managed purchase order rework starts. |  |

#### Resubmit Centrally Managed Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You resubmit the purchase order in hub system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Choose My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Search for Purchase Order | On the My Inbox screen, enter the purchase order number in the search area, then choose Search. |  |  |
| 4 | Resubmit Purchase Order | Select the purchase order on the left part of the screen and choose Resubmit. | The Submit Decision screen is displayed. |  |
| 5 | Enter Resubmit Note | Enter the resubmit note in the Submit Decision dialog then choose Submit. | The purchase order is resubmitted for approval. |  |

### Recommend Material Group Centrally

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can correct matrial group of purchase requisition according to material group recommendation from data attribute recommendation.

Prerequisites

To start this step, you must complete the recommend material group centrally configuration steps in the setup instructions of this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Process Purchase Requisitions Centrally screen is displayed |  |
| 3 | Search for Purchase Requisitions | On the Process Purchase Requisitions Centrally screen, swith on Items with Recommended Material Groups and search for your purchase requisition.Choose Show More per Row. | The Purchase Requisition with Material Group Recommandation Available is displayed. |  |
| 4 | Update Material Group based on Material Group Recommandation | On the Process Purchase Requisitions Centrally screen, choose Material Group Value on the purchase requisition list page.On the Material Group Recommendations popup screen, choose the material group base on the confidence percentage.Note The threshold for the confidence percentage can be defined in step Define Threshold for Confidence of Material Group Recommendations that described in the setup instruction. | Material group is updated. |  |
| 5 | Open Purchase Requisition Items | On the Process Purchase Requisitions Centrally screen, choose your purchase requisition item. | The Purchase Requisition Item screen is displayed. |  |
| 6 | Check Material Group | On the Purchase Requisition Item screen, choose Open Document.On the Display Purchase Requisition screen, check updated material group. |  |  |

### Detect and React to Situation

#### Detect and React to Approaching Delivery Date of Centrally Managed Purchase Requisition Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor overdue purchase requisition items through Notification.

Situation and notification are triggered according to the criteria you set in the preliminary steps. The SAP system automatically detects situations of approching delivery date of purchase requisition item on a daily basis, and informs critical situations with the notification function on the home screen. This enables team members to proactively react to approaching delivery date of purchase requisition items, and avoid potential adverse impact to company business processes.

|  |
| --- |
| Note You must perform the steps [Manage Teams and Responsibilities](#unique_10) [page ] 11 and [Create Situation Type for Approaching Delivery Date of Centrally Managed Purchase Requisitions](#unique_11) [page ] 12 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori Launchpad as a Purchaser - Central Procurement role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Choose the notifications | Choose Notifications on the upper right part of the screen.Choose the notification Approaching Delivery Date Notification, which is generated by the system batch job. | The My Situations - Extended screen is displayed. |  |
| 3 | Check Situation Message | On the My Situations - Extended screen, choose Open PR Item.On the Purchase Requisition Item screen, the detailed situation message is displayed on the Situations tab.You can choose Close and pick a reason for closing the situation.Note To use the My Situations - Extended (F4537) app, you need to assign business catalog SAP_CA_BC_SITN_MYSITUATION_PC to your user. | Situation message is shown and closed. |  |

#### Detect and React to Overdue Items of Replicated Purchase Order Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor overdue purchase requisition items through Notification.

Situation and notification are triggered according to the criteria you set in the preliminary steps. The SAP system automatically detects situations of approching delivery date of purchase requisition item on a daily basis, and informs critical situations with the notification function on the home screen. This enables team members to proactively react to approaching delivery date of purchase requisition items, and avoid potential adverse impact to company business processes.

|  |
| --- |
| Note You must perform the steps [Manage Teams and Responsibilities](#unique_10) [page ] 11 and [Create Situation Type for Overdue Items of Replicated Purchase Order](#unique_12) [page ] 14 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with a Purchaser - Central Procurement role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Choose the notifications | Choose Notifications on the upper right part of the screen.Choose the notification Overdue items in purchase order, which is generated by the system batch job. | The My Situations - Extended screen is displayed. |  |
| 3 | Check Situation Message | On the My Situations - Extended screen, choose Open PO Item.On the Purchase Order Item screen, the detailed situation message is displayed on the Situations tab.You can choose Close and pick a reason for closing the situation.Note To use the My Situations - Extended (F4537) app, you need to assign business catalog SAP_CA_BC_SITN_MYSITUATION_PC to your user. | Situation message is shown and closed. |  |

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
- related-to :: [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem]]
- related-to :: [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio]]
- related-to :: [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2XT_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 133,558 chars in the whole document
