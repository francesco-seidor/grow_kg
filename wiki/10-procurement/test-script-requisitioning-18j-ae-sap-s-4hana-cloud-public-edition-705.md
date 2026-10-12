---
id: 10-procurement/test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705
title: "Test Script - Requisitioning (18J_AE), SAP S/4HANA Cloud Public Edition (18J_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 18J (AE): requisition to PO, approval workflows, goods receipt, supplier invoice, reservation; prerequisites and sample data."
cluster: 10-procurement
tags: [kb/procurement, topic/requisitioning-and-consumable-purchasing]
aliases: [18J_S4CLD2608_BPD_EN_AE]
keywords: [Requisitioning and Consumable Purchasing, requisitioning, purchase requisitions, flexible workflow, purchase requisition approval, purchase order approval, purchase orders, supplier invoices, catalog purchasing, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/18J_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-705
topic: 10-procurement/requisitioning-and-consumable-purchasing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Requisitioning (18J_AE), SAP S/4HANA Cloud Public Edition (18J_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/18J_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Requisitioning and Consumable Purchasing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Requisitioning (18J_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232806762)

[2 Prerequisites 5](#_Toc232806763)

[2.1 Additional Manual Configuration 5](#_Toc232806764)

[2.2 System Access 5](#_Toc232806765)

[2.3 Roles 5](#_Toc232806766)

[2.4 Master Data and Organizational Data 6](#_Toc232806767)

[2.5 Preliminary Steps 8](#_Toc232806768)

[2.5.1 Configure Catalog 8](#_Toc232806769)

[2.5.1.1 Configure Open Catalog Interface Settings 8](#_Toc232806770)

[2.5.2 Maintain Requisitioning Groups 8](#_Toc232806771)

[2.5.3 Maintain the Default Setting for Users 10](#_Toc232806772)

[2.5.4 Mapping of Material Group to Purchasing Group 11](#_Toc232806773)

[2.5.5 Activate Flexible Workflow for Purchase Requisition 13](#_Toc232806774)

[2.5.5.1 Check Flexible Workflow for Purchase Requisition Approval 13](#_Toc232806775)

[2.5.5.2 Configure Flexible Workflow for Purchase Requisition 14](#_Toc232806776)

[2.5.5.3 Manage Conditions to Restart Flexible Workflow 15](#_Toc232806777)

[2.5.6 Activate Flexible Workflow for Purchase Order 17](#_Toc232806778)

[2.5.6.1 Check Flexible Workflow for Purchase Order Approval 17](#_Toc232806779)

[2.5.6.2 Configure Flexible Workflow for Purchase Order (Optional) 18](#_Toc232806780)

[2.5.7 Activate Flexible Workflow for Supplier Invoice 20](#_Toc232806781)

[2.5.7.1 Check Tolerance Limit for PP Tolerance Key 20](#_Toc232806782)

[2.5.7.2 Activate Flexible Workflow for Supplier Invoice 21](#_Toc232806783)

[2.5.7.3 Check Workflow for Supplier Invoice 23](#_Toc232806784)

[2.5.7.4 Update Cost Center for User Responsible (Optional) 23](#_Toc232806785)

[2.5.8 Edit User-Specific Parameters for Supplier Invoices (Optional) 24](#_Toc232806786)

[2.5.9 Manage Situation Types 25](#_Toc232806787)

[2.5.10 Settings for Creation of Reservation 26](#_Toc232806788)

[2.5.11 Check Material number 27](#_Toc232806789)

[2.5.12 Initializing Material Stock 27](#_Toc232806790)

[2.6 Business Conditions 28](#_Toc232806791)

[3 Overview Table 29](#_Toc232806792)

[4 Test Procedures 31](#_Toc232806793)

[4.1 Create Purchase Requisition 31](#_Toc232806794)

[4.1.1 Create Purchase Requisition with Cost Center 31](#_Toc232806795)

[4.1.1.1 Create Purchase Requisition with Cost Center- Single Account Assignment 31](#_Toc232806796)

[4.1.1.2 Create Purchase Requisition with Cost Center- Multiple Account Assignment Category 33](#_Toc232806797)

[4.1.2 Create Purchase Requisition with Unknown Product 35](#_Toc232806798)

[4.1.2.1 Create Purchase Requisition with Unknown 35](#_Toc232806799)

[4.1.2.2 Change Purchase Requisition 36](#_Toc232806800)

[4.1.3 Create Purchase Requisition with Enhanced Limit item 37](#_Toc232806801)

[4.1.4 Catalog Purchasing 38](#_Toc232806802)

[4.1.4.1 Manage Catalog Items 38](#_Toc232806803)

[4.1.4.2 Create Purchase Requisition with Catalog 39](#_Toc232806804)

[4.2 Check Purchase Requisition (Optional) 41](#_Toc232806805)

[4.3 Copy Purchase Requisition (Optional) 43](#_Toc232806806)

[4.4 Mass Changes to Purchase Requisitions (Optional) 44](#_Toc232806807)

[4.5 Monitor Purchase Requisition Items by Account Assignment (Optional) 45](#_Toc232806808)

[4.6 Approve Purchase Requisition 46](#_Toc232806809)

[4.7 Change Purchase Requisition 48](#_Toc232806810)

[4.8 Monitor Purchase Requisition Items (Optional) 49](#_Toc232806811)

[4.9 Redistribute Workload (Optional) 50](#_Toc232806812)

[4.10 Convert Purchase Requisition to Purchase Order 52](#_Toc232806813)

[4.11 Approve Purchase Order 53](#_Toc232806814)

[4.12 Change Purchase Order 54](#_Toc232806815)

[4.13 Confirm Receipt of Goods 55](#_Toc232806816)

[4.14 Create Supplier Invoice 56](#_Toc232806817)

[4.15 Release Blocked Supplier Invoice (Optional) 58](#_Toc232806818)

[4.16 Purchase Requisition with Reservation 59](#_Toc232806819)

[4.16.1 Create Purchase Requisition with Auto-Reservation 59](#_Toc232806820)

[4.16.2 Check My Purchase Requisition 60](#_Toc232806821)

[4.16.3 Post Goods Issue for Reservation 61](#_Toc232806822)

[5 Appendix 63](#_Toc232806823)

[5.1 Process Integration 63](#_Toc232806824)

[5.2 Succeeding Processes 63](#_Toc232806825)

[5.3 Set up Mail Notification for Purchase Requisition Workflow 63](#_Toc232806826)

[5.4 Configure Rework Flexible Workflow for Purchase Requisition 65](#_Toc232806827)

[5.5 Rework Purchase Requisition 67](#_Toc232806828)

## Purpose

Overview

This scope item describes employee requisitioning activities. An employee creates a shopping cart for free text material. A purchase requisition is generated and converted to a purchase order. If the value exceeds certain criteria, the purchase order must be approved. When the employee receives the goods, they perform a goods receipt confirmation. Invoice receiving can then be performed.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/829951d1257a2b96f22215cbf43aae7c)

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
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Payable Accountant - Procurement | SAP_BR_AP_ACCOUNTANT_PROCUREMT |  |  |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data and Organizational Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |
| Plant | 3310 | Plant 1 AE |  |
| Supplier | 33300002 | Domestic UAE Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchase group | 003 | Group 003 |  |
| Purchase group | 002 | Group 002 |  |
| Cost Center | 33101101 | Financials (AE) |  |
| Cost Center | 33101501 | R&D Cost center |  |
| G/L Account | 51600000 |  |  |
| Storage Location | 331A | Std. storage 1 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| 2SW | Create Tax Condition - MDS |

### Preliminary Steps

#### Configure Catalog

##### Configure Open Catalog Interface Settings

External process

Please refer to the document Setting UpRequisitioning (18J).

#### Maintain Requisitioning Groups

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Maintain Requisitioning Groups | On the Configure Your Solution: Realize Phases screen, search Maintain Requisitioning Groups, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Requirements Processing screen, choose Configure on the line of configuration step with name Maintain Requisitioning Groups. | The Change View "Maintenance View for Requisitioning Groups for Purchasing" screen is displayed. |  |
| 5 | Save new entry. | Choose New Entries, then make below data:RequisitioningGrpID: For example, Z001;Validity Start Date: <current data>;Validity End Date: <current data + 6 months>;RequisitionGrpName: for example, SOB testingChoose Save. | Requisition Group created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Requisitioning Groups | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Maintain Requisitioning Groups and create the following settings. | The Change View "Maintenance View for Requisitioning Groups for Purchasing" screen is displayed. |  |
| 3 | Save new entry. | Choose New Entries, then make below data:RequisitioningGrpID: For example, Z001;Validity Start Date: <current data>;Validity End Date: <current data + 6 months>;RequisitionGrpName: for example, SOB testingChoose Save. | Requisition Group created. |  |

#### Maintain the Default Setting for Users

Purpose

The default setting for an employee should be maintained by the Configuration Expert mandatorily. Plant and Company code needs to be presented a primary information in the user defaults screen．

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Default Settings for Users - Purchase Requisitions (F1995) . | The Default Settings for Users screen displays. |  |
| 3 | Enter the User ID | On the Default Settings for Users screen, enter the User ID and then choose Enter. |  | Please use the Search Help to find the User ID for User Name EmployeeProcurement . |
| 4 | Edit the Default Setting for User | On the Default Settings for Users screen, choose Edit on the right upper corner.Make the following entries:Requisitioning Group (Optional): <the number you define in previous chapter>, For example, Z001Shop on Behalf Type:Group Based: <You can only shop on behalf for the employee who belong to the same Requisitioning Group>Company Code based: <You can shop onbehalf for the employee who belong to the same company code>.No Shop on behalf based.Plant: 3310Company Code: 3310Currency: AEDSource Determination: <Selected>Purchasing Doc. Type : NBSPO Price Type: <Do not adopt>Choose Save.Note There are three types for PO Price Type:1. Do not apply: the price of SSPPR always copied to PO if fixed supplier maintained.2. As net price: the price of SSPPR will copied to PO as net price if no fixed supplier and info record maintained.3. As gross price: the price of SSPPR will copied to PO as gross price if no fixed supplier and info record maintained. | Default Settings are set for users. |  |

#### Mapping of Material Group to Purchasing Group

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phases screen, search Define Mapping of Material Groups to Purchasing Group, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Organization screen, choose Configure on the line of configuration step with name Define Mapping of Material Groups to Purchasing Group. | The Change ViewMaintain Mapping of Material Groups to Purchasing Group screen is displayed. |  |
| 5 | Save new entry. | Choose New Entries, then make below data:Plnt: 3310PGr: for example, 003Option: Equal To (=low)Material Group -From : for example, YBMM00Choose Save. | Material group and purchase group mapped. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Mapping of Material Groups to Purchasing Group | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Mapping of Material Groups to Purchasing Group and create the following settings. | The Change ViewMaintain Mapping of Material Groups to Purchasing Group screen is displayed. |  |
| 3 | Save new entry. | On the Change ViewMaintain Mapping of Material Groups to Purchasing Group screen, choose New Entries, then make below data:Plnt: 3310PGr: for example, 003Option: Equal To (=low)Material Group -From : for example, YBMM00Choose Save. | Material group and purchase group mapped. |  |

#### Activate Flexible Workflow for Purchase Requisition

##### Check Flexible Workflow for Purchase Requisition Approval

Purpose

In this procedure, you activate flexible workflow for purchase requisition approval.

If you want to use the flexible workflow to approve the purchase requisition, you have to process the steps: [Check Flexible Workflow for Purchase Requisition Approval](#unique_11) [page ] 13 and [Configure Flexible Workflow for Purchase Requisition](#unique_12) [page ] 14.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Purchase Requisitions , choose configuration with name Requirements processing from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Purchase Requisitions . | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for PR Approval | Check if the following entry selected for NB and NBS: scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NB and NBS. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Requisitions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 3 | Activate Flexible Workflow for PR Approval | Check if the following entry selected for NB and NBS: scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NB and NBS. |  |

##### Configure Flexible Workflow for Purchase Requisition

Purpose

In this procedure, you configure your release conditions for Purchase Requisition Approval.

|  |
| --- |
| Note For the Work flow Name and Steps Name, you can translate to other languages via app Workflow Content Translation (SWF_FLEX_I18N_TR_WEB), for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Purchase Requisition | Open Manage Workflow for Purchase Requisitions (F2705) | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Select Workflows: Overall Release of Purchase Requisition, then choose Create and make following entries:Workflow Name: Test Workflow for Purchase RequisitionStart Conditions：<Total net amount of purchase requisition is greater than or equal to10AED>Workflow Steps: CreateStep Type: Overall release of Purchase RequisitionStep Properties:Is Optional Step: NoRecipients: Assignment By: <User>Note Please check if the employee data has been maintained with the chapter [Maintain the Default Setting for Users](#unique_9) [page ] 10 for Users if you can’t find User for approval.Select User with Manager_procurement from F4 helpChoose Create.Choose Save. | The Workflow for Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |
| 5 | Define Order(optional) | Choose Define Order.On the Define Order screen, then choose Test Workflow for Purchase Requisition then move the selected workflow one level up. | Define the priority for workflow. |  |

##### Manage Conditions to Restart Flexible Workflow

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phases screen, search Manage Conditions to Restart Flexible Workflow for Purchase Requisitions, then choose Search.Select the line item Requirements Processing and go to the next screen.On the Configure Your Solution - Organization screen, choose Configure on the line of configuration step with name Manage Conditions to Restart Flexible Workflow for Purchase Requisitions. | The Change View Manage Conditions to Restart Flexible Workflow: Overview screen is displayed. |  |
| 5 | Save new entry. | In the SS Proc. field:X: <Remove>Seq. Key: for example, 18;Purchase Requisition Attributes: Purchasing Group;Choose Save. | Changes is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Manage Conditions to Restart Flexible Workflow for Purchase Requisitions and create the following settings. | The Change View Manage Conditions to Restart Flexible Workflow: Overview screen is displayed. |  |
| 3 | Save new entry. | In the SS Proc. field:X: <Remove>Seq. Key: for example, 18;Purchase Requisition Attributes: Purchasing Group;Choose Save. | Changes is saved. |  |

#### Activate Flexible Workflow for Purchase Order

##### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

##### Configure Flexible Workflow for Purchase Order (Optional)

Purpose

In this procedure, you configure release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

|  |
| --- |
| Note For the Workflow Name and Steps Name, you can translate to other languages via app Workflow Content Translation, for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created, and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Activate Flexible Workflow for Supplier Invoice

##### Check Tolerance Limit for PP Tolerance Key

Context

If you need to trigger Payment Block workflow for supplier invoice, please make sure the tolerance limit check for PP tolerance key has been maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the Fiori Launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | In the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Set Tolerance Limits, choose configuration with name Incoming Invoice from search result, then choose Configure on the right of configuration steps with name Set Tolerance Limits. | The Tolerance Limits for Invoice Postings screen displays. |  |
| 5 | Open Tolerance PP for company code | Select row with tolerance key PP, then choose Detail button. | Tolerance key PP details show. |  |
| 6 | Display Tolerance Limits for Invoice Postings display | Detail information of PP will be displayed. Make sure the Absolute Upper/Low Limit data or Percentage Lower/Upper Limit data maintained. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Set Tolerance Limits and create the following settings. | The Tolerance Limits for Invoice Postings screen displays. |  |
| 3 | Open Tolerance PP for company code | Select row with tolerance key PP. | Tolerance key PP details show. |  |
| 4 | Display Tolerance Limits for Invoice Postings display | Detail information of PP will be displayed. Make sure the Absolute Upper/Low Limit data or Percentage Lower/Upper Limit data maintained. |  |  |

##### Activate Flexible Workflow for Supplier Invoice

Purpose

In this procedure, you active flexible workflow for supplier invoice.

If you want to use the flexible workflow to approve the supplier invoice, you have to process this steps.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Your Solution | Choose Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | In the Manage Your Solution screen, open Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Supplier Invoice, choose item name Incoming Invoice from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Supplier Invoices. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen is displayed. |  |
| 5 | Active Flexible Workflow for Supplier Invoices | Select checkbox Payment Block: Flexible Workflow is Active.Select checkbox Release Completed Invoice: Flexible Workflow is Active.Select checkbox Check Authorizations for Flexible Workflow Steps (Optional).Choose Save. | Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for activity Activate Flexible Workflow for Supplier Invoices.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen displays. |  |
| 3 | Active Flexible Workflow for Supplier Invoices | Select checkbox Payment Block: Flexible Workflow is Active.Select checkbox Release Completed Invoice: Flexible Workflow is Active.Select checkbox Check Authorizations for Flexible Workflow Steps (Optional).Choose Save. | Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

Result

The Scenario based workflow is activated for Supplier Invoices.

##### Check Workflow for Supplier Invoice

Purpose

In this procedure, you make sure Workflow for Supplier Invoice is activated.

|  |
| --- |
| Note For the Work flow Name and Steps Name, you can translate to other languages via app Workflow Content Translation , for example translate it from English to German. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Supplier Invoices (F2873) . | The Manage Workflows screen displays. |  |
| 3 | Check Workflow for Blocked Invoice | In Workflows dropdown list, choose Workflow for Blocked Invoice, make sure workflow Release blocked Invoice by Accounting Responsibles is in active status. If not, select it and choose Activate.Note If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to business role of the user. | The Workflow Item is activated. |  |

##### Update Cost Center for User Responsible (Optional)

Purpose

In this procedure, you configure your release conditions for Invoice Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead . | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Cost center | Open Manage Cost Centers - Old Version (F1443A) .Note Choose OK if dialog TXT_WARNING_ERROR appears, then enter the Me area in the top-left corner of the homepage. Choose Settings and then choose Default Values and enter a value A000 in the Controlling Area field. Then choose OK. | The Manage Cost Centers screen is displayed. |  |
| 3 | Filter cost center | Cost Center: for example, 33101101Choose Go, select cost center in search results, select the item to check the detailed information of the item. | Cost Center detail information screen is displayed. |  |
| 4 | Input User Responsible | On the Manage Cost Centers screen, choose Edit:User Responsible: Select from F4. For example, search User ID for purchasing_manager |  |  |
| 5 | Save data | Choose Save. | Cost center is saved. |  |
| 6 | Cost center update | Repeat above steps for cost center 33101501. | Cost center is updated. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Edit Supplier Invoice Settings (F3813). | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice (F0859), it will take effective immediately. For APP Create Supplier Invoice - Advanced (MIRO) , user needs to logout and logon again to make it take effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Manage Situation Types

Prerequisite

|  |
| --- |
| Note Situation Handling (31N) is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Select the template to copy | Choose Standard Templates and choose Go to search the Standard Situation Templates:Choose Standard Situation Templates: PROC_OVERDUEPRITEMTOCONFIRM then choose Copy. | The Situation Type screen displays. |  |
| 4 | Create Custom Situation Type | On the New Situation Type screen, make the following entries:Make the following entries and choose Save:ID: Z_PROVERDUEPRITEMTOCONFIRMName: SSP PR Item Overdue for ConfirmationChoose Batch Job Scheduling :Time Zone: for example, UTC+1Start Batch Job At: for example: 22:00Choose Recipients. Choose Add Rule for Responsibility Rules. On the Add Rules screen, select Determine the owners responsible for the SSP PR , then choose Select. | The situation type is maintained. |  |
| 5 | Enable situation type | Choose Create. Choose Yes when dialog box Enable Situation Type is displayed. |  |  |

#### Settings for Creation of Reservation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the Fiori Launch Pad as aConfiguration Expert - Business Process Configuration. | The Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Settings for Creation of Reservation (F2278) . | The Settings for Creation of Reservation screen displays. |  |
| 3 | Configure Your settings for creation of Reservation | On Settings for Creation of Reservation, choose Edit to change your settings as following:Rules: Goods Issue(03)Movement Type: GI for cost center(201)Check Unrestricted Stock Only: <Selected >Choose Add and then make the following entries for automatic reservation:Purchasing Group: 002Material Group: L001You can also delete existing combination. |  |  |
| 4 | Save Your Entries | Choose Save. | Requisition Identifiers created. |  |

#### Check Material number

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Display Material (MM03) . | The Display Material(Initial Screen) display. |  |
| 3 | Check material number | Check material number TG0011 with plant 3310 . |  |  |

Please follow master Data scripts (MDS) BNF to create below material if material TG0011 doesn’t exist:

| Material number | Z001 |
| --- | --- |
| Plant | 3310 |
| Storage Location | 331A |
| Sales Organization | 3310 |
| Distribution Channel | 10 |
| Purchase Group | 002 |
| Material Group | L001 |

#### Initializing Material Stock

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open Manage Stock (F1062). | The Manage Stock (Original) screen display. |  |
| 3 | Enter Material | Make the following entries and choose Enter:Material (Original) : TG0011 (otherwise , Z001)Plant: 3310, Plant 1 AE | The stock overview for the material is displayed. |  |
| 4 | Select Stock | Select the icon next to the stock to add initial stock. For example:Storage Location: 331A Unrestricted Use Stock | A dialog box displays. The Storage Location, Stock Type, and Current Quantity fields are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document date: <Today>Posting date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the messageMaterial document XXX created. The stock is added. |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Must be run before this test script. |
| 31N - Situation Handling | Install this scope item for the situation handling steps. |

## Overview Table

This scope item consists of several process steps that are listed in the following table :

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition with Cost Center- Single Account Assignment](#unique_27) [page ] 31 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is created. |
| [Create Purchase Requisition with Cost Center- Multiple Account Assignment Category](#unique_28) [page ] 33 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is created. |
| [Create Purchase Requisition with Unknown](#unique_29) [page ] 35 | Employee - Procurement | My Purchase Requisitions (F1639A) | A new Purchase order is created. |
| [Change Purchase Requisition](#unique_30) [page ] 36 | Employee - Procurement | My Purchase Requisitions (F1639A) | A Purchase order is changed. |
| [Create Purchase Requisition with Enhanced Limit item](#unique_31) [page ] 37 | Employee - Procurement | My Purchase Requisitions (F1639A) | A new Purchase order is created. |
| [Manage Catalog Items](#unique_32) [page ] 38 | Purchaser | Manage Catalog Items (F3149) | Catalog item is maintained. |
| [Create Purchase Requisition with Catalog](#unique_33) [page ] 39 | Employee - Procurement | My Purchase Requisitions (F1639A) | The Purchase Requisition is created via catalog. |
| [Check Purchase Requisition (Optional)](#unique_34) [page ] 41 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is created. |
| [Copy Purchase Requisition (Optional)](#unique_35) [page ] 43 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is created. |
| [Mass Changes to Purchase Requisitions (Optional)](#unique_36) [page ] 44 | Purchaser | Mass Changes to Purchase Requisitions (F2594) (Optional) | Purchase Order for consumable material is created. |
| [Monitor Purchase Requisition Items by Account Assignment (Optional)](#unique_37) [page ] 45 | Accounts Payable Accountant | Purchase Requisition Items by Account Assignment (F2422) |  |
| [Approve Purchase Requisition](#unique_38) [page ] 46 | Manager - Procurement | My Inbox - All Items (F5331) | Purchase Requisition is approved. |
| [Change Purchase Requisition](#unique_39) [page ] 48 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | Purchase Requisition Item detail page is changed. |
| [Monitor Purchase Requisition Items (Optional)](#unique_40) [page ] 49 | Purchaser | Monitor Purchase Requisition Items (F2424) | Purchase Requisition Item detail page is dispalyed. |
| [Redistribute Workload (Optional)](#unique_41) [page ] 50 | Purchaser | Redistribute Workload (F2504) |  |
| [Convert Purchase Requisition to Purchase Order](#unique_42) [page ] 52 | Purchaser | Process Purchase Requisitions (F1048A) | Purchase Order is created. |
| [Approve Purchase Order](#unique_43) [page ] 53 | Purchasing Manager | My Inbox - All Items (F5331) | Purchase Order is approved. |
| [Change Purchase Order](#unique_44) [page ] 54 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is updated . |
| [Confirm Receipt of Goods](#unique_45) [page ] 55 | Employee - Procurement | Confirm Receipt of Goods (F4489) . | Goods Receipt is posted. |
| [Create Supplier Invoice](#unique_46) [page ] 56 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice Receipt is posted. |
| [Release Blocked Supplier Invoice (Optional)](#unique_47) [page ] 58 | Purchasing Manager | My Inbox - All Items (F5331) | Blocked supplier invoice is released. |
| [Create Purchase Requisition with Auto-Reservation](#unique_48) [page ] 59 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is created. |
| [Check My Purchase Requisition](#unique_49) [page ] 60 | Employee - Procurement | My Purchase Requisitions (F1639A) | Purchase Requisition is checked. |
| [Post Goods Issue for Reservation](#unique_50) [page ] 61 | Warehouse Clerk | Post Goods Movement (MIGO) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Requisition

#### Create Purchase Requisition with Cost Center

##### Create Purchase Requisition with Cost Center- Single Account Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Employee create shopping cart for free text material, generate a purchase requisition.

Procedure

|  |
| --- |
| Note Please raise BCP Incident to component CA-HR-S4 if you want to shop on behalf function. The ticket should include: creating a new generic user Employee _Procure_R which assigned the role of SAP_BR_EMPLOYEE_PROCUREMENT. Please refer chapter [Maintain the Default Setting for Users](#unique_9) [page ] 10 for User Employee_Procurement_R after user created. This is only for internal testing. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A) | The My Purchase Requisitions screen displays. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, choose Create Item . | The Purchase Requisition screen is shown. |  |
| 4 | Enter General Data | In the General Information section, make the following entries:Item Description: office supplyMaterial group: YBMM00Valuation Price: 100AEDPrice Unit: 1 EAQuantity Requested : 100EADelivery Date : <today +30>Purchasing Group : 003 (which comes from the step [Mapping of Material Group to Purchasing Group](#unique_10) [page ] 11)Purchasing Organization: 3310Plant : 3310Account Assignment Category: KDistribut. Indicator: Single Account AssignmentNote Account Assignment Category P for account assignments to projects is also supported. In case budget availability control for a project is active you may run into warning / error messages along the requisition process in case budget thresholds are exceeded. For further details on the budget availability control for projects you can refer to 1NT test script (component responsible: PPM-CNT)Choose Delivery Address section, make the following entry:Address Type: PlantChoose Account Assignments section, and make the following entries:G/L Account: for example, 51600000 for materials with a material number, The G/L account will be determined automatically.Go to the section Account Assignment and choose the corresponding line to go to Account Assignment screen and enter Cost Center: 33101101 in the appearing screen.Choose Apply.Choose Source of Supply section:Choose Add.Fixed Supplier: 33300002 then choose Add.Choose Apply. | The Purchase Requisition screen is displayed |  |
| 5 | Save Purchase Requisition | Choose Order to save the purchase Requisition.Choose Create to confirm any warning message. | A new Purchase order is created if no error is displayed in the dialog box. |  |

##### Create Purchase Requisition with Cost Center- Multiple Account Assignment Category

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
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A) | The My Purchase Requisitions screen displays. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, choose Create Item. | The Purchase Requisition screen is shown. |  |
| 4 | Enter Purchase Requisition Data | Enter all of the necessary data:General Information:Item Description: office supplyMaterial Group: YBMM00Valuation Price: 100AEDPrice Unit: 1 EAQuantity Requested: 100 EADelivery Date: <today +30>Purchasing Group : 003Purchasing Organization: 3310Plant : 3310Account Assignment Category: KChoose Delivery Address section, make the following entry:Address Type: PlantDistribut. Indicator: Distribution by PercentageChoose Account Assignments section, and make the following entries:G/L Account: for example, 65100000 for material without material number. The G/L account be determined automatically.Choose Create to add another account assignment line.Choose the Account Assgmt No. 1 item:Cost Center: 33101101Distribution (%) : for example: 40Choose the Account Assgmt No. 2Cost Center: 33101401Distribution (%) : for example: 60Choose Apply.Choose Source of Supply section:Choose Add.Fixed Supplier: 33300002Choose Add.Choose Apply. | The Purchase Requisition screen is displayed. |  |
| 5 | Save Purchase Requisition | Choose Order to save the purchase requisition.Choose Create to confirm any warning message. | A new Purchase order is created if no error is displayed in the dialog box. |  |

#### Create Purchase Requisition with Unknown Product

##### Create Purchase Requisition with Unknown

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
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A). | The My Purchase Requisitions screen displays. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, choose Create Item. | The Purchase Requisition screen is shown. |  |
| 4 | Enter Purchase Requisition Data | In the General Information section, make the following entries:Item Description: office supplyMaterial group: YBMM00Valuation Price: 100AEDPrice Unit: 1 EAQuantity Requested : 100EADelivery Date : <today +30>Purchasing Group : 003Purchasing Organization: 3310Plant : 3310Account Assignment Category: UChoose Apply. | The Purchase Requisition screen is displayed. |  |
| 5 | Save Purchase Requisition | Choose Order to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box. |  |

##### Change Purchase Requisition

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
| 1. | Log on | Logon to SAP Fiori launchpad as an Employee - Procurement . | The Fiori Launchpad is displayed. |  |
| 2. | Access the App | Open My Purchase Requisitions (F1639A). | The My Purchase Requisitions screen is displayed. A list of Purchase Requisition is displayed. If needed, you can enter search criteria to find your purchase requisition. |  |
| 3 | Select Purchase Requisition | Choose the line of the purchase requisition you want to change. | The purchase requisition is opened in the display mode. |  |
| 4 | change Purchase Requisition Data | Choose Edit.Select the item 00010 to item detail screen.Account Assignment Category: KDistribut. Indicator: Single Account AssignmentChoose Account Assignments section, make the following entries: G/L Account: for example, 51600000, for materials with a material number, The G/L account will be determined automatically.Go to the section Account Assignment and choose the corresponding line to go to Account Assignment screen:Cost Center: 33101101Choose Apply.Choose Source of Supply section:Choose Add.Fixed Supplier: 33300002 then choose Add.Choose Apply. | The Purchase Requisition screen is displayed. |  |
| 5 | Save Purchase Requisition | Choose Order to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box. |  |

#### Create Purchase Requisition with Enhanced Limit item

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A) . | The Create Purchase Requisition screen displays. |  |
| 3 | Create Purchase item | Choose Create Limit Item , if you want to create a free description item. | General Information |  |
| 4 | Enter General Data | In the General Information section, make the following entries:Item Description: office supplyMaterial group: YBMM00Overall Limit: 120AEDStart Date: <today>End Date: <today + 6months>Expected Value: 100AEDPurchasing Group : 003Purchasing Organization: 3310Plant : 3310Account Assignment Category: KChoose Account Assignments section, and make the following entries:G/L Account: for example, 51600000 for materials with a material number, The G/L account will be determined automatically.Go to the section Account Assignment and choose the corresponding line to go to Account Assignment screen and enter Cost Center: 33101101 in the appearing screen.Choose Apply.Choose Source of Supply section:Choose Add.Fixed Supplier: 33300002 then choose Add.Choose Apply. | The Purchase Requisition screen is displayed. |  |
| 5 | Save Purchase Requisition | Choose Order to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box.Note Enhance limit item PR don’t need do Confirm Receipt of Goods. |  |

#### Catalog Purchasing

##### Manage Catalog Items

Purpose

In this procedure, you define the catalog item for requisitioning.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto SAP Fiori launchpad as a Purchaser. | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Catalog Item | Open Manage Catalog Items (F3149) . | The Manage Catalog Items screen is displayed. |  |
| 3 | Create Catalog Item | On Manage Catalog Items screen, choose Create .On the Catalog Item screen, navigate to General Information section, and make the following entries:Item Description: <Your description>Material group, : YBMM00Base Unit of Measure: EACatalog: S4H_GLOBALCATALOGValid from :<today>Valid to: <today + 12 month>:Price per Unit: 1Order Unit: EAPrice: for example: 1AEDPlant: 3310Purchasing Organization: 3310Company Code: 3310Navigate to Text Management section. Except for the default description for language EN, you can maintain the item description for other language if it is necessary. | Catalog detail information screen is displayed. |  |
| 4 | Save Catalog Item | Choose Create to save the catalog item. |  | Catalog Item created. |

##### Create Purchase Requisition with Catalog

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Employee create shopping cart for catalog item, then generate a purchase requisition. .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A). | The Create Purchase Requisition screen displays. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, enter the description which you created in previous step [Manage Catalog Items](#unique_32) [page ] 38, then choose Search.Quantity: 10 EA, choose Add.Choose Purchase Requisition Overview at the top right of the screen to view the cart, and then choose View Cart.Note On the Cross-Catalog Search screen, if you want to create purchase requisition via External catalog, choose a catalog under Catalog section, and select products listed in the catalog, add to cart, and check out to add it to your Purchase Requisition.Please refer chapter [Configure Open Catalog Interface Settings](#unique_7) [page ] 8 for details. | Add catalog to view Cart. |  |
| 4 | Choose Purchase Requisition Item | Select the purchase Requisition Item then choose >. | The Purchase Requisition screen is displayed. |  |
| 5 | Enter Purchase Requisition Data | Enter all of the necessary data.General Information:Price Unit: 10 EAQuantity Requested: 10 EADelivery Date: <today +30>Purchasing Group : for example, 003 , (which comes from the step [Mapping of Material Group to Purchasing Group](#unique_10) [page ] 11)Purch. Organization: for example, 3310Plant: for example, 3310Acct Assignment Cat: KDistribut. Indicator: Single Account AssignmentNote Account Assignment Category P for account assignments to projects is also supported. In case budget availability control for a project is active you may run into warning / error messages along the requisition process in case budget thresholds are exceeded. For further details on the budget availability control for projects you can refer to 1NT test script (component responsible: PPM-CNT).Choose Account Assignment section, make the following entries:GL Account: for example, 65100000 for materials with a material number, The G/L account will be determined automatically.Go to the section Account Assignment and choose the corresponding line and enterCost Center: for example, 33101101Choose Apply.Choose Source of Supply section, choose Add, enter supplier 33300002 as Fixed, and then choose Add.Choose Apply. | The Purchase Requisition item screen is displayed. |  |
| 6 | Save Purchase Requisition | Choose Order to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box. |  |

### Check Purchase Requisition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check your Purchase Requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose My Purchase Requisitions (F1639A) . | The Create Purchase Requisition initial screen appears. |  |
| 3 | Check item details | Choose View All . Select Shop on Behalf if you want to check purchase requisition which created for Employee_Procure_R.Search your Requisition number in the Purchase Requisition list. Select the item to check the detailed information of the item.Note If there is draft information display, A draft Purchase Requisition already exists for the user.Choose Edit. | Detail information of the Purchase Requisition item displays. |  |
| 4 | Change Purchase Requisition(optional) | Choose Purchase Requisition item. On the Item Details screen, in the General Information section:Account Assignment Category: KIn the Account Assignment section:choose the item line serial no.acct.assgt 1.On the Accounting Details screen, make the following entries:GL Account : 65100000Cost center: 33101101ChooseApply and then choose Apply. |  |  |
| 5 | Add new Item (Optional) | On the My Purchase Requisition screen, choose Create.You can follow chapter [Create Purchase Requisition with Cost Center- Single Account Assignment](#unique_27) [page ] 31 for details. |  |  |
| 6 | Back to home | Choose Back and then choose Order.Note The purchase requisition also can be viewed / modified from App Manage Purchase Requisition Professional and role Purchaser. | Purchase requisition 1000XXXX changed. |  |

### Copy Purchase Requisition (Optional)

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
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access My Purchase Requisition | Choose My Purchase Requisitions (F1639A) . | The Create Purchase Requisition initial screen appears. |  |
| 3 | Copy Purchase requisition | Choose View All. Search your Requisition number in the Purchase Requisition list. Select the item then choose Copy. | Add to shopping cart. |  |
| 4 | Edit Purchase Requisition Items | On the Purchase Requisition screen:Note Choose Rejected, then you will see the Decision Note if the copied PR was rejected.Select the item created and enter the following data:Delivery Data: for example <today+30>.Choose Apply. | Detail information is maintained. |  |
| 5 | Order | Choose Order.Choose Create to confrim any warning message. | Purchase Requisition is created. |  |

### Mass Changes to Purchase Requisitions (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can apply changes to multiple Purchase Requisition Items at a time.

|  |
| --- |
| Note If the Purchase Requisition includes Enhanced Limit item, then some fields like Delivery Data, Valuation Price, Distribution Indicator, GR Processing Time, GR non-valuated, Purchase order price don't support by this app. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Purchaser. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Mass Changes to Purchase Requisitions (F2594). | The Mass Changes to Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition Items | Set values to some filters. For example:Purchase Requisition: the PR number created in previous Creating Purchase Requisition.Then choose Go. | The search results show the details with the respective filter Criteria.By default, all the Purchase Requisition Items are selected for Mass Change operation. |  |
| 4 | Display Purchase Requisition | Select an individual Purchase Requisition Item. | The Purchase Requisition Item detail page is shown. Review the details of the Purchase Requisition and choose Back. |  |
| 5 | Set new Values | Choose Mass Edit. | A dialog box will open displaying the fields where new values can be set. |  |
| 6 | Apply mass changes | Set new values to the desired fields which are displayed in the dialog box.For example: Delivery Date: <Replace Field Value> <today+20>After setting new values, choose Apply Mass Changes. | A confirmation dialog box would appear to confirm the mass change operation.After choosing Apply, a toast message would occur containing the job id of that particular mass change operation. Then choose View Job List. |  |
| 7 | Check application job | Choose Mass Change Jobs. | It will navigate to the Application Jobs page containing the list of Purchase Requisition jobs.Verify if the job is successful for the selected Purchase Requisition Items. |  |

### Monitor Purchase Requisition Items by Account Assignment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in Purchase Requisition Items based on account assignment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launch Pad displays. |  |
| 2 | Access the App | Open Purchase Requisition Items by Account Assignment (F2422) . | The Purchase Requisition Items by Account Assignment screen displays. |  |
| 3 | Search for Purchase Requisition | All basic filters are displayed,Purchasing RequisitionAcct Assignment Cat.Cost CenterWBS ElementAssetMaterial GroupFixed SupplierPurchasing OrganizationPurchasing GroupMake the above entries accordingly, then choose Go. | The search results show the details with the respective filter Criteria.By default data is filtered by Cost Center.You can choose Adapt Filter to list filters to add adapt filters. |  |
| 4 | Display Purchase Requisition | Select an individual line item of the Purchase Requisition Item you want to display the Purchase Requisition Items details.Choose Details to display. | The Purchase Requisition Item screen displays. |  |
| 5 | Verify data displayed on the object page | Verify data displayed on the object page. | The data should be logically in sync with Purchase Requisition Item. |  |
| 6 | Change grouping and Sorting | Choose Back (less than symbol) to come to app main view.Choose Setting and change the Grouping and Sorting options. And choose OK. | The data should reload in the app and Grouping and Sorting should be according selected options. |  |

### Approve Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase requisition. If the total amount of PR is more than 10AED and order type is NBS. Order type is configured in [Maintain the Default Setting for Users](#unique_9) [page ] 10.

Procedure

|  |
| --- |
| Note You can ignore this step if you did not set up the Preliminary Steps - [Configure Flexible Workflow for Purchase Requisition](#unique_12) [page ] 14. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Manager - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Open My Inbox - All Items (F5331) .Note Maybe you can find the value of Confidence Level for PR approval in the top right corner, that's because scope item 43E was activated. | A list of already created Purchase Requisition is displayed. |  |
| 3 | Edit Purchase Requisition | Option 1: Select the Purchase Requisition from the left screen. Choose the Purchase Requisition number then choose Edit and Approval purchase requisition. On the Edit and Approve Purchase Requisition screen, choose Edit. Then change quantity and choose Approve. Choose Approve after entering some comments.Option 2: Select the Purchase Requisition from the left screen and choose Approve at the bottom right of the screen.Enter the approval reason, if needed, then choose Submit. | The Purchase Requisition is approved. |  |
| 4 | Back to SAP Fiori launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

|  |
| --- |
| Note The purchaser requisition creator and requester will receive notification if purchase requisition is rejected. |

### Change Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

This step is mandatory if RITA is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Logon to SAP Fiori launchpad as an Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Manage Purchase Requisitions - Professional (F2229). | The Purchase Requisition is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go.Select the row for the Purchase Requisition you want to change and use the little arrow on the right side to enter the PR detail, then choose Edit. | The Purchase Requisition screen is shown.The purchase Requisition is open in change mode. |  |
| 4 | Maintain the Tax Code | Select the row of the item then go to the Purchase Requisition Item screen.Choose Valuation tab then maintain Tax Code : <Tax Code>.Choose Apply.Choose Save. | The Purchase Requisition tax code maintained. |  |

### Monitor Purchase Requisition Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

In this step you can Monitor your Purchase Requisition Items.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Purchase Requisition Items (F2424) . | The app opens up displaying only the filters in search bar. |  |
| 3 | Verify the columns displayed in output columns | To load data, choose Standard variant .Choose Go. | A list of Purchase Requisition is displayed.Following columns should be displayed by defaultPurchasing Requisition ItemMaterialPlantFixed SupplierQuantity RequestedValuation PriceNet ValueDelivery Date |  |
| 4 | Search Purchase Requisition | Search the Purchase Requisition by applying Purchase Requisition filter available on the top.Choose Go. | All Items for the Purchase Requisition are displayed as individual line items in the output list. |  |
| 5 | Display Purchase Requisition Item Detail | Choose individual line item of Purchase Requisition to display Purchase Requisition Item detail. | The Purchase Requisition Item detail page is displayed.The data should be logically in sync with the created Purchase Requisition. |  |
| 6 | Back to SAP Fiori launchpad | Choose the Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### Redistribute Workload (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To run through this, the relevant Purchasing Documents would be listed .On Selection of Purchasing Document/Documents the Reassign Purchasing Group Button shall get enabled . Thereafter, the user may select the Respective Purchasing Group from the list of respective Purchasing group fom F4. The user can then choose Simulate , this shall list the possibility whether the Purchasing Group would be Changed or not for the selected Purchasing documents. Henceforth the User can confirm (either Cancel or OK or Save) to get it updated accordingly.

You don't need to approve purchase requisition if you process chapter Manage Conditions to Restart Flexible Workflow, otherwise, you need to process the step Approve Purchase Requisition again, because workflow restart again after you reassign purchasing group.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Logon on to Fiori Launchpad | Logon on to Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Redistribute Workload (F2504) . | The redistribute Workload screen displays. |  |
| 3 | Search Purchasing Document Entry / Entries | Set values to some filters to search purchasing documents for which you want to redistribute workload, then choose GO.for example:Creation DateDocument NumberDocument TypePurchasing OrganizationPurchasing GroupDocument Category | The search results show the purchasing documents details with the respective filter Criteria.Note Purchase requisition is closed or data is completed, or status is Released Completed, then Purchase requisition can be listed. |  |
| 4 | Reassign Purchasing Group | Select Purchasing Document Entry / Entries you want to redistribute workload.Choose Reassign Purchasing Group and select a Purchasing Group from the list. | The Reassign Purchasing Group dialog box appears and new Purchasing Group shall get selected. |  |
| 5 | Simulate | Choose Simulate.Note If all the purchase documents have error on Simulation and Purchasing Group cannot be updated for the documents (For example purchase documents already have follow-on document or get locked), you need to choose Cancel and go back to previous step to select other purchase documents. It's only allowed you to assign the purchasing group which maintained in chapter [Mapping of Material Group to Purchasing Group](#unique_10) [page ] 11 . | This shall list the simulation messages as to whether the Reassignment is feasible or not. |  |
| 6 | Save the Reassignment | Choose Save. | The Purchasing Group shall get reassigned accordingly with system message Group has been assigned to documents to save the Reassignment when the simulation shows the Reassignment is feasible.. |  |
| 7 | Check Application Jobs Change Log | Choose Change Log. | It will navigate to Application Jobs page containing the list of Job IDs for all Purchase documents.Verify if the job is successful for the selected Purchase documents. |  |

### Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This step only supports the Purchase Requisitions with item category Standard, Consignment, Subcontracting, Third-party and Enhanced Limits, otherwise please use APP Create Purchase Order Advanced to create Purchase Order with reference to purchase requisition items. |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A) . | The Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for the Purchase Requisition which created in the section Create Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Prepare the Purchase Order | Choose Show More per Row button on the side of Create RFQ, then select the Purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The purchase order is created. |  |
| 5 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchasing Doc.Type: Standard PO (NB)Choose Order. | The purchase order is created. |  |

### Approve Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO is more than 10AED and purchase group is 003, then the PO should do the approval.

|  |
| --- |
| Note If the approval user does not have My Inbox app, you have to check whether business catalog SAP_PRC_BC_PURCHASING_MNGR has been assigned to the business role of the approval user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad as Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2. | Open Approve Purchase Orders | OpenMy Inbox - All Items (F5331). | A list of already created Purchase Orders is displayed. |  |
| 3. | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4. | Approve Purchase Order | Select the Purchase order in left of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5. | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

|  |
| --- |
| Note For printing handling and the processing of purchase orders, see the chapter Preview Puchase Order (optional) in the Procurement of Direct Materials (J45) test script. |

### Change Purchase Order

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
| 1 | Logon | Open the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A) . | The Manage Purchase Orders screen displays.A list of already created Purchase Orders display. |  |
| 3 | Search Purchase Order | Enter the Purchase Order number or some other content to search for the Purchase Order. | The Purchase Order will display. |  |
| 4 | Select Purchase Order | Select the row for the Purchase Order to be changed.Note You can enter some search criteria to find your Purchase Order. | The Edit Purchase Order xxx screen displays. The purchase order opens in change mode. |  |
| 5 | Changing Purchase Order | Choose Edit.Choose item which you want to change to Purchase Order Item screen.Choose Tax in part Items:Tax Code: <Tax Code> | The Purchase Order values are changed. |  |
| 6 | Submit Purchase Order | Choose Apply. Then choose Order to save the purchase order. | Purchase Order is updated.Note You need to do step[Approve Purchase Order](#unique_43) [page ] 53 if the purchase order needs to approval again. |  |

### Confirm Receipt of Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity posts the receipt of goods with reference to an existing Purchase requisition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the SAP Fiori launchpad | Open the SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Choose notification (Optional) | Choose the Notifications icon which is at the top right of the Home Screen.Choose the notifications which is generated by the system.Note This notification will be generated only in case the delivery data is in the past if delivery data in purchase order is compared with currently data.Please make sure the step [Edit User-Specific Parameters for Supplier Invoices (Optional)](#unique_20) [page ] 24 run successfully before you run this step. | A list of Notifications displays. |  |
| 3 | Confirm goods receipt quantity | Open Confirm Receipt of Goods (F4489) . | The Confirm Requisitions screen appears.A list of purchase orders display. |  |
| 4 | Finalize the delivery (Optional) | On the Confirm Requisitions screen , enter your PR number and choose Go.Choose your PR item in the list.On the right screen, choose Edit.Now you can make the following entries:In the General Information part:Document Date: <Date of creation of document>Posting Date: <Date of posting the document>Delivery Note: <Reference of the delivery note>Header Text: <Description of material document>In the Items part:Check or change the quantity in filed Delivered Quantity.Select the Final Delivery check box, if you want to close the purchase requisition. | The system displays the data for the goods receipt on the Confirm Requisitions screen. |  |
| 5 | Confirm the Goods Receipt | Choose the checkbox for the item and choose Confirm. |  |  |

### Create Supplier Invoice

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
| 1 | Logon | Logon to SAP Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | Make the following entries :Transaction: InvoiceCompany Code : For example, 3310Invoice date: <Today>Posting date : <Today>Gross Invoice Amount: Value in PO Calculate TaxInvoicing Party : For example, 33300002Reference: xxx (reference invoice number from invoicing party). |  |  |
| 4 | Enter Purchase Order References | In the Purchase Document References, check the references.Make the following entries, (using a purchase order you previously created):References Document Category: Purchase Order/ Scheduling Agreement : <XXX>Purchase Order |  |  |
|  | Check the Invoice Items data | If the invoice item is Limit, then enter the Amount is 100 AED , the Tax Code <Input Tax Code> (there may already be a tax code that was copied from the purchase order). | The Amount, Tax Code are consistent. |  |
| 5 | Check the Purchase Order Items data | Check the Amount Purchas, the Quantity, and the Tax Code.Note If the amount is more than 5.5% of the initial amount, it will trigger supplier invoice workflow, which means you need to do next step - [Release Blocked Supplier Invoice (Optional)](#unique_47) [page ] 58, and amount changes only work for single account assignment. You can choose invoice item to display multiple account assignment detail in next screen. |  |  |
| 6 | Post invoice | Choose Post. | The invoice is created. |  |

### Release Blocked Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the blocked supplier invoice is released, you could check details on the Approval Details Tab of the corresponding supplier invoice via Supplier Invoices List (F1060A)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an approver set in preliminary step, cost center responsible. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F5331) . | The My Inbox screen displays. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice displays. |  |
| 4 | Approve Supplier Invoice | On the Release Blocked Invoice XXXXXXXX screen, choose Release at the bottom of the screen.On the Submit Decision screen, add note if necessary and select Submit button. | Task successfully processed. |  |

### Purchase Requisition with Reservation

#### Create Purchase Requisition with Auto-Reservation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as an Employee - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Create Purchase Requisitions | Open My Purchase Requisitions (F1639A). | The My Purchase Requisitions screen displays. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, choose Create Item. | The Purchase Requisition screen is shown. |  |
| 4 | Enter General Data | Enter all of the necessary data:General Information:Material: TG0011Valuation Price: 10UAE DirhamPrice Unit: 1 PCQuantity Requested: 10 PCDelivery Date: <today +7>Purchasing Group : 002Purchasing Organization: 3310Plant : 3310Account Assignment Category : KDistribut. Indicator: Single Account AssignmentNote Account Assignment Category P for account assignments to projects is also supported. In case budget availability control for a project is active you may run into warning / error messages along the requisition process in case budget thresholds are exceeded. For further details on the budget availability control for projects you can refer to 1NT test script (component responsible: PPM-CNT)Choose Delivery Address section, make the following entry:Address Type: PlantChoose Account Assignment section:Choose a specific Account Assignment line and make the entries:GL Account: 51600000For materials with a material number, The G/L account will be determined automatically.Cost center: 33101101Choose Apply.Choose Source of Supply section:Fixed Supplier: 33300002Choose Add.Choose Apply. |  |  |
| 5 | Save Purchase Requisition | Choose Order.Choose Create to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box. |  |

#### Check My Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

On creation of a reservation, a Reservation document is created as a follow-on document for the purchase requisition item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori launchpad | Logon to SAP Fiori launchpad as an Employee - Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access My Purchase Requisition | Open My Purchase Requisitions (F1639A). | The My Purchase Requistions screen displays. |  |
| 3 | Check item details | Choose View All. Search your Requisition number in the Purchase Requisition list.Follow on Document Created: If the reservation document created, the status should be Follow on Document Created.On the screen My Purchase Requisitions, choose 1 item (or X items) in the line for your Purchase Requisition.In the dialog box Purchase Requisition Items, choose the item.Choose Zoom in button to check the Reservation number. | Detail information of the Purchase Requisition item displays.Note down Reservation number. |  |

#### Post Goods Issue for Reservation

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
| 1 | Log on | Open the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori launchpad | Open Post Goods Movement (MIGO). |  |  |
| 3 | Post Goods Issue for Reservation | On the screen, make the following entries:Trans./Event: Goods IssueReference Document : ReservationDocument Number: Your Reservation numberChoose Enter.Qty in UnE: 10 PCSLoC: 331AItem OK : <selected>Choose Post. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Description |
| --- | --- |
| Real-Time Reporting and Monitoring for Procurement(1JI) | The Procurement Overview Page gives the Purchaser the most important and relevant information at a glance – instead of navigating through many different transactions and reports.The Global Filter helps the Purchaser to focus the entire Procurement Overview Page to view all information according to specific suppliers, material groups, purchasing groups and more.Through contextual navigation the Purchaser can immediately act upon the displayed information by accessing the app or the object instance or get more detailed information in the corresponding KPI Drill-Downs. |

### Set up Mail Notification for Purchase Requisition Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Copy the predelivered email template to the exactly named custom template.

|  |
| --- |
| Note The email address has already been maintained for the approval. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to SAP Fiori launchpad as Administrator . | The SAP Fiori launchpad displays. |  |
| 2 | Access to Maintain Email Templates | Choose Maintain Email Templates. | The templatesdisplays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (XX) search Template: SWF_CRT_NOTIFY_RECIPIENTS.Choose email template then choose Copy then make bellow entries:Email Template: _02000458 _CRT_ALLName: Overall Release of Purchase RequisitionChoose Copy.Note Following templates are available for purchase requisition workflow:Workflow for Overall release of Purchase Requisition:02000458_CRT_ALL02000458_CRT_19Workflow for Release of Purchase Requisition Item:02000471 _CRT_ALL02000471 _CRT_20On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_WORKFLOW_COMPLETE_NOTIFY .Note For the workflow approval, copy the predelivered e-mail template SWF_WORKFLOW_COMPLETE_NOTIFY into your namespace. The custom template must follow this pattern: YY1_<ScenarioId>_COMPLETE_POSITIVEChoose email template then choose Copy, and then make the following entries:Email Template: _02000458_COMPLETE_POSITIVEName: Positive Workflow for Overall Release of Purchase RequisitionOrEmail Template: _02000471_COMPLETE_POSITIVEName: Positive Workflow for Release of Purchase Requisition itemChoose Copy.On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_WORKFLOW_COMPLETE_NOTIFY .Note For the workflow approval, copy the predelivered e-mail template SWF_WORKFLOW_COMPLETE_NOTIFY into your namespace. The custom template must follow this pattern: YY1_<ScenarioId>_COMPLETE_POSITIVEChoose email template, and then choose Copy, and then make the following entries:Email Template: _02000458_COMPLETE_NEGATIVEName: Negative Workflow for Overall Release of Purchase RequisitionOrEmail Template: _02000471_COMPLETE_NEGATIVEName:Negative Workflow for Release of Purchase Requisition itemChoose Copy. | Email Template copied. |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example,YY1__02000458_CRT_ALL, then go to Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example, English ,then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request, and then choose Save. | The Email Template adjusted. |  |

### Configure Rework Flexible Workflow for Purchase Requisition

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration。 | The SAP Fiori Launchpad displays. |  |
| 2 | Open Manage Workflow for Purchase Requisition | Open Manage Workflows for Purchase Requisitions (F2705). | The Manage Your Solution screen displays. |  |
| 3 | Create Rework Workflow | Select Workflows: Overall release of requisition . Then choose Add and make following entries:Name: Test Rework Workflow for Purchase RequisitionStart Conditions：Creation Indication of purchase requisition is STotal net amount of purchase requisition is greater than 500.00AEDStep Sequence: AddStep Type: Overall Release of Reworkable PRSTEP PROPERTIES:Is Optional Step: NoRecipients: Assignment By: <User>Note Please check if the employee data has been maintained with the chapter [Maintain the Default Setting for Users](#unique_9) [page ] 10 for Users if you can’t find User for approval.Select User with Manager_procurement from F4 helpException Handling:Rework Requested: Choose Rework PR for Required Action and choose Repeat step for Action Result.Note Action result should be (after re-work):Continue Workflow: Current Workflow shall move to next stepRepeat Step: repeat the current step of current workflowRestart workflow: restart the workflowChoose Add.Choose Save. | The Rework Workflow for Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

### Rework Purchase Requisition

Purpose

In this procedure, you rework a purchase requisition. If Creation Indication of purchase requisition is S, the total amount of PR is more than 500.00 AED and order type is NBS. Order type is configured in [Maintain the Default Setting for Users](#unique_9) [page ] 10

Procedure

You can ignore this step if you did not set up the Preliminary Steps [Configure Flexible Workflow for Purchase Requisition](#unique_12) [page ] 14.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Logon to SAP Fiori launchpad as a Manager - Procurement . | The SAP Fiori launchpad displays. |  |
| 2 | Open My Inbox | Open My Inbox - All Items (F5331) .Note Maybe you can find the value of Confidence Level for PR approval in the top right corner, that's because scope item 43E was activated. | A list of already created Purchase Requisition is displayed. |  |
| 3 | Rework purchase requisition | Select the Purchase Requisition from the left screen and choose Request Rework at the bottom right of the screen.Enter the rework reason in the Submit Decision dialog then choose Submit. | The Purchase Requisition is approved. |  |
| 4 | Back to SAP Fiori launchpad | Choose the Home button to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

After this step, the Purchase requisition should to be edited by the creator with the rework reason.

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
> Flagged while digesting this document, not verified: Rework Purchase Requisition step 3 (Request Rework) lists the expected result as 'The Purchase Requisition is approved', which contradicts the rework action.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Multiple account assignment test uses cost center 33101401, which is not in the sample master data list (33101101 and 33101501) nor in the cost center update step (33101101, 33101501).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/18J_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 106,114 chars in the whole document
