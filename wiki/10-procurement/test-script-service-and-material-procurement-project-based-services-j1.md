---
id: 10-procurement/test-script-service-and-material-procurement-project-based-services-j1
title: "Test Script: Service and Material Procurement – Project-Based Services (J13_AE) (J13_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item J13: service, consumable and third-party procurement for project-based services, with prerequisites and steps."
cluster: 10-procurement
tags: [kb/procurement, topic/procurement-of-services, topic/customer-project-management]
aliases: [J13_S4CLD2608_BPD_EN_AE]
keywords: [Procurement of Services, service procurement, third-party order processing, consumable material procurement, service entry sheets, supplier invoices, flexible workflow, purchase contracts, limit items, situation handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J13_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1298
topic: 10-procurement/procurement-of-services
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service and Material Procurement – Project-Based Services (J13_AE) (J13_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J13_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Procurement of Services** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service and Material Procurement – Project-Based Services (J13_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232862715)

[2 Prerequisites 5](#_Toc232862716)

[2.1 System Access 5](#_Toc232862717)

[2.2 Roles 5](#_Toc232862718)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232862719)

[2.4 Additional Manual Configuration 8](#_Toc232862720)

[2.5 Business Conditions 8](#_Toc232862721)

[2.6 Preliminary Steps 8](#_Toc232862722)

[2.6.1 Open New MM Period 8](#_Toc232862723)

[2.6.2 Create Purchasing Info Record 9](#_Toc232862724)

[2.6.3 Activate Flexible Workflow for Purchase Order Approval 11](#_Toc232862725)

[2.6.4 Check Flexible Workflow for Purchase Order 13](#_Toc232862726)

[2.6.5 Check Flexible Workflow for Service Entry Sheets 13](#_Toc232862727)

[2.6.6 Configure Flexible Workflow for Supplier Invoice 14](#_Toc232862728)

[2.6.6.1 Activate Flexible Workflow for Supplier Invoice 14](#_Toc232862729)

[2.6.6.2 Check Flexible Workflow for Supplier Invoice 16](#_Toc232862730)

[2.6.6.3 Update Profit Center for User Responsible 17](#_Toc232862731)

[2.6.7 Create Ready-to-Use Situation Type for Cash Discount at Risk (Optional) 18](#_Toc232862732)

[2.6.8 Create Ready-to-Use Situation Type for Due Date Reach Soon (Optional) 19](#_Toc232862733)

[2.6.9 Create Team and Responsibilities (Optional) 21](#_Toc232862734)

[3 Overview Table 22](#_Toc232862735)

[4 Test Procedures 26](#_Toc232862736)

[4.1 Create a Basic Agreement (Quantity Contract)(Optional) 26](#_Toc232862737)

[4.1.1 Option One: Create Purchase Contract with Reference to Purchase Requisition 26](#_Toc232862738)

[4.1.1.1 Create Purchase Requisition (Outline Agreement Requisition) 26](#_Toc232862739)

[4.1.1.2 Create Purchase Contract with Reference to Purchase Requisition 27](#_Toc232862740)

[4.1.2 Option Two: Create Purchase Contract with Reference to the Contract Template 29](#_Toc232862741)

[4.2 Service Procurement 31](#_Toc232862742)

[4.2.1 Post Expenses for External Employees 31](#_Toc232862743)

[4.2.1.1 Create Purchase Order for Expenses with Text Items 31](#_Toc232862744)

[4.2.1.2 Monitor Purchase Order Items(Optional) 33](#_Toc232862745)

[4.2.1.3 Create Supplier Invoice with PO Relation (With Item Block) 34](#_Toc232862746)

[4.2.1.4 Check Blocked Supplier Invoice with Notification (Optional) 36](#_Toc232862747)

[4.2.2 Purchase External Services with Service Material Item 38](#_Toc232862748)

[4.2.2.1 Create Purchase Order for Service Items 38](#_Toc232862749)

[4.2.2.2 Option One: Automatic Creation of Service Entry Sheet by Time Recording 40](#_Toc232862750)

[4.2.2.2.1 Review Service Entry Sheets from Time Recording 40](#_Toc232862751)

[4.2.2.2.2 Review Error Logs for Service Entry Sheets Processing(Optional) 41](#_Toc232862752)

[4.2.2.2.3 Schedule Automatic Creation of Service Entry Sheets from Time Recording(Optional) 42](#_Toc232862753)

[4.2.2.3 Option Two: Manual Creation of Service Entry Sheet 43](#_Toc232862754)

[4.2.2.3.1 Maintain Service Entry Sheet 43](#_Toc232862755)

[4.2.2.4 Option Three: Import Service Entry Sheets 45](#_Toc232862756)

[4.2.2.4.1 Configure Import Service Entry Sheets for Specific Users 45](#_Toc232862757)

[4.2.2.4.2 Import Service Entry Sheets 47](#_Toc232862758)

[4.2.2.5 Create Supplier Invoice with SES Relation 48](#_Toc232862759)

[4.2.3 Procurement of Limits Item for a Project 50](#_Toc232862760)

[4.2.3.1 Create Purchase Requisition for Limits Item 50](#_Toc232862761)

[4.2.3.2 Convert Purchase Requisition into Purchase Order 52](#_Toc232862762)

[4.2.3.3 Create Service Entry Sheet with Flexible Workflow 53](#_Toc232862763)

[4.2.3.4 Create Supplier Invoice with PO Relation 54](#_Toc232862764)

[4.2.4 Post Expenses for Internal Employees w/o PO Relation 56](#_Toc232862765)

[4.2.4.1 Create Supplier Invoice without PO/GR 56](#_Toc232862766)

[4.3 Third-Party Order Processing 57](#_Toc232862767)

[4.3.1 Procurement of General Material for a Project With Multiple Account Assignment 57](#_Toc232862768)

[4.3.1.1 Create Purchase Order for Material Items With Multiple Account Assignment (Third-Party Order Processing for all Countries) 57](#_Toc232862769)

[4.3.1.2 Process Goods Receipt of Third-Party Order 59](#_Toc232862770)

[4.3.1.3 Create Supplier Invoice with PO/GR Relation 60](#_Toc232862771)

[4.3.2 Procurement of Text Based Material for a Project 62](#_Toc232862772)

[4.3.2.1 Create Purchase Order for Text Items 62](#_Toc232862773)

[4.3.2.2 Post Goods Receipt of Material Items 64](#_Toc232862774)

[4.3.2.3 Create Supplier Invoice with PO/GR Relation (with Invoice Reduction) 65](#_Toc232862775)

[4.3.2.4 Print Complaint Letter 67](#_Toc232862776)

[4.4 Procurement of Consumable Material 68](#_Toc232862777)

[4.4.1 Procurement of Consumable Material for a project 68](#_Toc232862778)

[4.4.1.1 Maintain the Default Setting for Users 68](#_Toc232862779)

[4.4.1.2 Create Purchase Requisition for Consumable Material Items 69](#_Toc232862780)

[4.4.1.3 Convert Purchase Requisition into Purchase Order 71](#_Toc232862781)

[4.4.1.4 Optional Step: Change Purchase Order 71](#_Toc232862782)

[4.4.1.5 Print Purchase Order 72](#_Toc232862783)

[4.4.1.6 Optional Step: Check Purchasing Document List 73](#_Toc232862784)

[4.4.1.7 Post Goods Receipt of Material Items 74](#_Toc232862785)

[4.4.1.8 Optional Step: Check Goods Receipt Details 75](#_Toc232862786)

[4.4.1.9 Optional Step: Reverse Goods Receipt 76](#_Toc232862787)

[4.4.1.10 Create Supplier Invoice with PO/GR Relation 77](#_Toc232862788)

[4.4.2 Procurement of Text Based Consumable Material for a project 79](#_Toc232862789)

[4.4.2.1 Create Purchase Order for Consumable Text Items 79](#_Toc232862790)

[4.4.2.2 Post Goods Receipt of Material Items 81](#_Toc232862791)

[4.4.2.3 Create Supplier Invoice with PO/GR Relation 81](#_Toc232862792)

[4.4.2.4 Release Completed Supplier Invoice 83](#_Toc232862793)

[4.4.2.4.1 Reject Supplier Invoice (Optional) 83](#_Toc232862794)

[4.4.2.4.2 Rework Supplier Invoice (Optional) 84](#_Toc232862795)

[4.4.2.4.3 Release Completed Supplier Invoice 85](#_Toc232862796)

[4.5 Purchase Document Processing (Optional Steps) 85](#_Toc232862797)

[4.5.1 Release Supplier Invoice (Optional) 86](#_Toc232862798)

[4.5.2 Workflow for Approving Supplier Invoice (Optional) 86](#_Toc232862799)

[4.5.3 Reverse Invoice (Optional) 87](#_Toc232862800)

[4.5.4 Clear GR / IR Clearing Account 88](#_Toc232862801)

[4.5.5 Cancel Accounting Document (Optional) 89](#_Toc232862802)

[4.5.6 Map G/L Account with Resource and Key Figure (Optional) 90](#_Toc232862803)

[4.5.7 Edit User-Specific Parameters for Supplier Invoices (Optional) 92](#_Toc232862804)

[5 Appendix 93](#_Toc232862805)

[5.1 Process Chains 93](#_Toc232862806)

[5.1.1 Succeeding Processes 93](#_Toc232862807)

[5.1.2 Preceding Processes 93](#_Toc232862808)

[5.2 Relevant Features 93](#_Toc232862809)

[5.3 Import Work Data 94](#_Toc232862810)

[5.4 Creating Supplier Master Data – Company Code Data for Worker 95](#_Toc232862811)

## Purpose

Overview

This scope item covers all relevant procurement processes for the professional services scenario. It includes several possible subprocesses:

- Service procurement: The company orders an external service. The external service provider confirms the purchase order and performs the service. The supplier then posts the expenses back, and the company creates and processes a supplier invoice.
- Material procurement for consumption: A customer or internal project requests a consumption material. The company creates a purchase order and sends it to the supplier. The supplier sends the material to the company, and the company checks the goods receipt. Finally, the company creates a supplier invoice and pays it.
- Procurement for third-party order processing: The purchaser at the ordering company orders a material from a supplier for an end customer. The supplier ships the material directly to the end customer.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | NS0001 | Material Type NLAG |  |
| Material | HW0001, LI0001 | Material Type MAT |  |
| Material | T001 | Material Type SERV |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Chart of Accounts | YCOA | Industry Chart of Accounts |  |
| Work Package | Realization | belonging to Customer Project I-1000 | For account assignment in purchase orders. |
| Cost Center | 33101902 |  |  |
| G/L Account | 61007000 | Airfare | For supplier invoices with internal travel costs. |
| Customer | 33100001 | Domestic UAE Customer 1 | For supplier invoices with internal travel costs. |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS– MDS |
| BNE | Create Supplier Master - MDS– MDS |
| BNG | Create G/L Account and Cost Element - MDS– MDS |
| BNM | Create Cost Center and Cost Center Group - MDS– MDS |
| BHD | Create Purchasing Info Record - MDS – MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/56de04b0853944471e2e281f2496e1d9)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | An active customer project with a work package for time and expenses must exist in the test client for you to be able to assign a valid account to the purchase order item. Project is in status ‘in execution’. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| 31N - Situation Handling (Optional) | This scope item must be installed for situation handling steps. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

Closing MM Period and Opening New Posting Period

#### Create Purchasing Info Record

Purpose

In this procedure, you create info records for procure process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Organization: 3310Purchasing Info Record Category: StandardSupplier: 33300001Material: T001Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: for example, 5Under Delivery Tolerance in %: for example, 10Over Delivery Tolerance in %: for example, 10Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: for example, HStandard Order Quantity: for example, 1Unlimited Delivery: DeselectedGoods-Receipt-Based Invoice Verification: DeselectedNo Evaluated Receipt Settlement: SelectedOrder Acknowledgment Requirement: Deselected | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To:12/31/9999Amount: for example, 600Pricing Unit: for example, 1Currency: for example, AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | A purchasing info record is created. |  |
| 11 | Repeat entire steps and create an new info record | Repeat the above steps to create a new info record for materials HW0001 and NS0001. |  |  |

Result

The Purchasing info records are created.

#### Activate Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you activate flexible workflow for purchase order approval.

If you want to use the flexible workflow to approve the purchase order, you have to process the steps: Activate Flexible Workflow for Purchase Order Approval and Check Flexible Workflow for Purchase Order.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Purchase Orders, choose item name Purchase Order Processing from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase Order Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are checked. If not, select them and choose Save:Document Type: NBScenario based workflow:X | The Scenario based workflow is active for Purchase Orders with Document Type: NBNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Flexible Workflow for Purchase Orders | Go to the Business Processes Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are checked. If not, select them and choose Save:Document Type: NBScenario based workflow:X | The Scenario based workflow is active for Purchase Orders with Document Type: NBNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Check Flexible Workflow for Purchase Order

Purpose

In this procedure, you make sure that the workflow for Purchase Order is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Check Workflow for Purchase Order | Make sure only the workflow Automatic Release of Purchase Order is Active. If not, select it and choose Activate.System check workflow with Active status by defined Order. The first workflow whose preconditions are met will be executed. | Workflow is activated. |  |

|  |
| --- |
| Note For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

#### Check Flexible Workflow for Service Entry Sheets

Purpose

In this procedure, you make sure Flexible Workflow for Service Entry Sheets is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Service Entry Sheets - Lean Services (F3173). | The Manage Workflows screen is displayed. |  |
| 3 | Check Automatic Release of Service Entry Sheet | In Workflows list, choose Automatic Release of Service Entry Sheet. Make sure only Automatic Release of Service Entry Sheet is activated. If not, select it and choose Activate, then deactivate other workflows.Note After you choose workflow name, you can view Workflow Details with Steps. Recipients in Workflow Steps defines the user who handles service entry sheet in the particular step, for example cost center responsible or project responsible. If this particular user doesn't have My Inbox APP, you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to role of the user. | The Workflow Item is activated. |  |

|  |
| --- |
| Note For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

#### Configure Flexible Workflow for Supplier Invoice

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

##### Check Flexible Workflow for Supplier Invoice

Purpose

In this procedure, you make sure workflow for Supplier Invoice activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Supplier Invoice | Choose Manage Workflows for Supplier Invoices (F2873). | The Manage Workflows screen is displayed. |  |
| 3 | Check Workflow for Blocked Invoice | In Workflows dropdown list, choose Workflow for Blocked Invoice, make sure workflow Release blocked Invoice by Accounting Responsibles is Active. If not, select it and choose Activate.Note Note: After you choose workflow name, you can view Workflow Details with Step Sequence. Recipients in Step sequence defines the user who handles invoice in the particular step, for example cost center responsible or WBS responsible. If this particular user doesn't have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to role of the user. This action is also required for other invoice workflow below.You may also choose Create Alternative Preconditions, add preconditions, such as: Invoice amount is equal or greater than , for example, 500 AED | Workflow is activated |  |
| 4 | Check Workflow for Parked Invoice as Complete | In Workflows dropdown list, choose Workflow for Parked Invoice as Complete, make sure workflow Release completed invoice is Active. If not, select it and choose Activate. | The Workflow Item is activated. |  |
|  | Option: Set User Project_Manager_PROF as WBS Element Approver | Select the Release Completed Invoice line, choose Copy.Change the workflow name as you want, and make the following entries:Valid From: <today>Valid To:< today 1 year>Under Start Conditions, make the following entry:Account Assignment Category 'WBS element': YesClick on Create, select Release of Complete Invoice as Step Type.Under Recipients For Assignment By, select User.User: PROJECT_MANAGER_PROF(Select from F4 help.)Under Exception Handling For Required Action, select Rework Invoice.For Recipients Role, select User: PROJECT_MANAGER_PROF(Select from F4 help.)Choose Create.Choose Save.Choose Activate. |  |  |

|  |
| --- |
| Note For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

##### Update Profit Center for User Responsible

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If precondition account assignment category Profit Center is used in workflow, you need to update your profit center user responsible for Invoice workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Profit Centers | Open Manage Profit Centers - Old Version (F3516). | The Manage Profit Centers screen is displayed. |  |
| 3 | Filter profit center | Input Profit Center to be used in invoice item. For example, YB101Choose Go, select profit center in search results, and then choose Edit | Profit center detail information screen is displayed. |  |
| 4 | Input User Responsible | In General Information tab make the following entires:User Responsible: Select from F4. Search User ID for PROJECT_MANAGER_PROF. For example, input CB998000XXXX in user responsible fieldPerson Responsible: For example PROJECT_MANAGER_PROF |  |  |
| 5 | Save data | Choose Save | Profit center is saved. |  |

#### Create Ready-to-Use Situation Type for Cash Discount at Risk (Optional)

Purpose

In this procedure, you create ready-to-use situation type for cash discount at risk.

|  |
| --- |
| Note Situation Handling (31N) is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Copy Standard Template | In Situation Templates tab, choose standard template with ID: MM_CASHDISCOUNTATRISK and choose Copy. | The Situation Type screen displays. |  |
| 4 | Create Custom Situation Type | On the Situation Type screen, make the following entries:Under the Admin Information section:ID: for example, Z_MM_CASHDISCOUNTATRISK.Go to section Situation Display.Under subsection In-App Situation Message:Message Details: Please enter details about the situation.Under subsection Notification and do the following:Aggregate Notifications: Selected.Resend Notifications: Selected.Go to section Conditions and make sure that processing order 1 is set as Open, and box for Send Notification is checked.Under tab Used Filters, remove all values for name Cash Discnt Due Date, and ensure it is blank.Go to section Situation Monitoring and select box for Monitor Instances.Go to section Batch Job Scheduling, make the following entries:Time Zone: Any Data (select a time zone from input help based on your location)Start Batch Job At: Any DataGo to section Recipients.Filter by Member Function: Select Operational Purchasing from the dropdown list. |  |  |
| 5 | Save Situation Type | Choose Create. | The situation type is created. |  |
| 6 | Enable Situation Type | Choose Yes for dialog box Do you want to enable the situation type? | The Situation Type is enabled. |  |

#### Create Ready-to-Use Situation Type for Due Date Reach Soon (Optional)

Purpose

In this procedure, you create ready-to-use situation type for due date reach soon.

|  |
| --- |
| Note Situation Handling (31N) is required to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Business Process Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Situation Types (F2947) . | The Manage Situation Types screen displays. |  |
| 3 | Copy standard template | In Situation Templates tab, choose standard template with ID: MM_DUEDATEREACHSOON and choose Copy. | The Situation Type screen displays. |  |
| 4 | Create Custom Situation Type | On the Situation Type screen:Under the Admin Information section:ID: for example, Z_MM_DUEDATEREACHSOONGo to section Situation Display, under subsection In-App Situation Message, make the following entry:Message Details: Please enter details about the situation.Under subsection Notification, make the following entries:Aggregate Notifications: Yes.Resed Notifications: Yes.Go to section Conditions and make sure that processing order 1 is set as Open, and box Send Notification is checked.For Used Filters, remove all values for name Net Due Date, and ensure it is blank.Go to section Situation Monitoring, check the box of Monitor Instances.Go to section Batch Job Scheduling, and make the following entries:Time Zone: Any Data (select a time zone from input help based on your location)Start Batch Job At: Any DataGo to section Recipients, and make the following entries:Filter by Member Function: Select Operational Purchasing from the dropdown list. |  |  |
| 5 | Save Situation Type | Choose Create. | The situation type is saved. |  |
| 6 | Enable Situation Type | Choose Yes for dialog box Do you want to enable the situation type? | The situation type is enabled. |  |

#### Create Team and Responsibilities (Optional)

Purpose

In this procedure, you create team and responsibilities for Cash Discount at Risk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the Configuration Expert - Business Process Configuration role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities - Procurement (F2412). | The Manage Teams and Responsibilities screen is displayed. |  |
| 3 | Create Team and Responsibilities | Choose Create and make following entries:Name: Z_MM_CASHDISCOUNTATRISKDescription: for Cash Discount at RiskStatus: EnabledGlobal ID: Z_MM_CASHDISCOUNTATRISKType: OPPURGo to Team Members area, choose Create and make the following entries:Business Partner: Select from F4 help, for example: search Last Name for *accountant* to get the user ID.Functions: Select OP_PURCH from F4 help |  |  |
| 4 | Save Team | Choose Create. | The team has been created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create a Basic Agreement (Quantity Contract)(Optional)](#unique_20) [page ] 26 | Purchaser | Manage Purchase Contracts (F1600A) | The Manage Purchase Contracts screen is displayed. |

Table 2: Service Procurement - Posting Expenses for External Employee

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order for Expenses with Text Items](#unique_21) [page ] 31 | Purchaser | Manage Purchase Orders (F0842A) | The Create Purchase Order screen is displayed. |
| [Create Supplier Invoice with PO Relation (With Item Block)](#unique_22) [page ] 34 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |

Table 3: Service Procurement - Purchase External Services with Service Material Item

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order for Service Items](#unique_23) [page ] 38 | Purchaser | Manage Purchase Orders (F0842A) | The Create Purchase Order screen is displayed. |
| Option One: Automatic Creation of Service Entry Sheet by Time Recording |  |  |  |
| [Review Service Entry Sheets from Time Recording](#unique_24) [page ] 40 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The service entry sheet list is displayed. |
| [Review Error Logs for Service Entry Sheets Processing(Optional)](#unique_25) [page ] 41 | Purchaser | Monitor Service Entry Sheet Generation Log (F3495) | The logs details display. |
| [Schedule Automatic Creation of Service Entry Sheets from Time Recording(Optional)](#unique_26) [page ] 42 | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | The New Jobs Screen is displayed. |
| [Maintain Service Entry Sheet](#unique_27) [page ] 43 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The New Service Entry Sheet screen is displayed. |
| [Create Supplier Invoice with SES Relation](#unique_28) [page ] 48 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice screen is displayed. |

Table 4: Service Procurement - Procurement of Limits Item for a Project

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition for Limits Item](#unique_29) [page ] 50 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Process Purchase Requisition screen is displayed. |
| [Convert Purchase Requisition into Purchase Order](#unique_30) [page ] 52 | Purchaser | Process Purchase Requisitions (F1048A) | The Process Purchase Requisition screen is displayed. |
| [Create Service Entry Sheet with Flexible Workflow](#unique_31) [page ] 53 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The New Service Entry Sheet screen is displayed. |
| [Create Supplier Invoice with PO Relation](#unique_32) [page ] 54 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice screen is displayed. |

Table 5: Service Procurement - Posting Expenses for Internal Employees w/o PO Relation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Supplier Invoice without PO/GR](#unique_33) [page ] 56 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |

Table 6: Third-Party Order Processing - Procurement of General Material for a Project

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order for Material Items With Multiple Account Assignment (Third-Party Order Processing for all Countries)](#unique_34) [page ] 57 | Purchaser | Manage Purchase Orders (F0842A) | The Create Purchase Order screen is displayed. |
| [Process Goods Receipt of Third-Party Order](#unique_35) [page ] 59 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt screen is displayed. |
| [Create Supplier Invoice with PO/GR Relation](#unique_36) [page ] 60 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Supplier Invoice screen is displayed. |

Table 7: Third-Party Order Processing - Procurement of Text Based Material for a Project

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order for Text Items](#unique_37) [page ] 62 | Purchaser | Manage Purchase Orders (F0842A) | Standard PO is created. |
| [Post Goods Receipt of Material Items](#unique_38) [page ] 64 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Post Goods Receipt screen is displayed. |
| [Create Supplier Invoice with PO/GR Relation (with Invoice Reduction)](#unique_39) [page ] 65 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |
| [Print Complaint Letter](#unique_40) [page ] 67 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice List screen is displayed. |

Table 8: Procurement of Consumable Material - Procurement of Consumable Material for a Project

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain the Default Setting for Users](#unique_41) [page ] 68 | Configuration Expert - Business Process Configuration | Default Settings for Users - Purchase Requisitions (F1995) | Default Settings are set for users. |
| [Create Purchase Requisition for Consumable Material Items](#unique_42) [page ] 69 | Project Manager - Professional Services | My Purchase Requisitions (F1643A) | The Create Own Item screen is displayed. |
| [Convert Purchase Requisition into Purchase Order](#unique_43) [page ] 71 | Purchaser | Process Purchase Requisitions (F1048A) | The Process Purchase Requisitions screen is displayed. |
| [Optional Step: Change Purchase Order](#unique_44) [page ] 71 | Purchaser | Manage Purchase Orders (F0842A) | The purchase order was changed. |
| [Optional Step: Change Purchase Order](#unique_44) [page ] 71 | Purchaser | Manage Purchase Orders (F0842A) | The system displays a list of purchase orders. |
| [Print Purchase Order](#unique_45) [page ] 72 | Purchaser | Manage Purchase Orders (F0842A) | The system displays a list of purchase orders. |
| [Optional Step: Check Purchasing Document List](#unique_46) [page ] 73 | Purchaser | My Purchasing Document Items - Professional (F0547B) | The My Purchasing Document Items screen displays the Purchasing Document Items list |
| [Post Goods Receipt of Material Items](#unique_47) [page ] 74 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The Material Document XX posted screen is displayed. |
| [Optional Step: Check Goods Receipt Details](#unique_48) [page ] 75 | Warehouse Clerk | Material Documents Overview (F1077) | The material Documents Overview screen is displayed. |
| [Optional Step: Reverse Goods Receipt](#unique_49) [page ] 76 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Documents Overview screen is displayed. |
| [Create Supplier Invoice with PO/GR Relation](#unique_50) [page ] 77 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |

Table 9: Procurement of Consumable Material - Procurement of Text Based Consumable Material for a project

| Process Step, Report or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order for Consumable Text Items](#unique_51) [page ] 79 | Purchaser | Manage Purchase Orders (F0842A) | The Create Purchase Order screen is displayed. |
| [Optional Step: Check Purchasing Document List](#unique_46) [page ] 73 | Purchaser | My Purchasing Document Items - Professional (F0547B) | The My Purchasing Document Items screen displays the Purchasing Document Items list. |
| [Post Goods Receipt of Material Items](#unique_52) [page ] 81 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | The material Document XX posted screen is displayed. |
| [Update Profit Center for User Responsible](#unique_15) [page ] 17 | Cost Accountant - Overhead | Manage Profit Centers - Old Version (F3516) | The Manage Profit Centers screen is displayed. |
| [Create Supplier Invoice with PO/GR Relation](#unique_53) [page ] 81 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The Create Supplier Invoice screen is displayed. |
| [Reject Supplier Invoice (Optional)](#unique_54) [page ] 83 | Project Manager - Professional Services | My Inbox - All Items (F5331) | The My Inbox screen is displayed. |
| [Rework Supplier Invoice (Optional)](#unique_55) [page ] 84 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice List screen is displayed. |
| [Release Completed Supplier Invoice](#unique_56) [page ] 85 | Project Manager - Professional Services | My Inbox - All Items (F5331) | The My Inbox screen is displayed. |

Table 10: Purchase Document Processing (Optional Steps)

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Release Supplier Invoice (Optional)](#unique_57) [page ] 86 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoice screen is displayed. |
| [Workflow for Approving Supplier Invoice (Optional)](#unique_58) [page ] 86 | Project Manager - Professional Services | My Inbox - All Items (F5331) | Supplier Invoice is released. |
| [Reverse Invoice (Optional)](#unique_59) [page ] 87 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Supplier Invoices List screen is displayed. |
| [Clear GR / IR Clearing Account](#unique_60) [page ] 88 | Accounts Payable Accountant | Clear GR/IR Clearing Account (MR11) | The Maintain GR / IR Clearing Account screen is displayed. |
| [Cancel Accounting Document (Optional)](#unique_61) [page ] 89 | Accounts Payable Accountant | Display/Cancel Account Maintenance Document (MR11SHOW) | The Display / Cancel Account Maintenance Document screen is displayed. |
| [Map G/L Account with Resource and Key Figure (Optional)](#unique_62) [page ] 90 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | G/L Account is mapped with Resource and Key Figure. |
| [Edit User-Specific Parameters for Supplier Invoices (Optional)](#unique_63) [page ] 92 | Accounts Payable Accountant | Edit Supplier Invoice Settings (F3813) | G/L Account is mapped with Resource and Key Figure. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The following supplier invoice postings have to be achieved in this process:

- Posting of supplier invoice for consumption material (PO with material NS0001> goods receipt > supplier invoice)
- Posting of supplier invoice for third party order (PO with material HW0001> goods receipt> supplier invoice)
- Posting of supplier invoice for text-based material (PO with text item and material group > goods receipt> supplier invoice) for material groups: L007 (Licenses),L008 (Hardware)
- Posting of supplier invoice for a time-based external service with material T00X (PO with material and time entry > supplier invoice)
- Posting of supplier invoice for travel costs from external employees (PO with text item and material group > supplier invoice) for material groups: E001 (Accommodation), E002 (Airfare), E003 (Ground Transportation), E004 (Travel Expenses misc.)
- Posting of supplier invoice for travel costs of internal employees (employee is supplier) with supplier invoice only for the accounts: 61003000 (Travel Expenses - Hotel and Accommodation), 61007000 (Travel Expenses - Airfare, Rail, Mileage), 61008000 (Travel Expenses – Miscellaneous)

### Create a Basic Agreement (Quantity Contract)(Optional)

Purpose

A quantity contract is an agreement between a purchasing organization and a supplier to decrease or increase a certain quantity of a product in an indicated period. The purchasing organization fulfills a contract by placing purchase orders against it. These purchase orders are called now as release orders (or call-offs). The supplier fulfills the contract by supplying the released quantity.

When you create a call-off, you refer to the relevant contract. The system automatically updates the released quantities in the contract.

Procedure

A Quantity Contract can be created as a reference to either an existing Purchase Requisition or an existing Contract Template. Choose any of the following procedures to create a quantity contract.

#### Option One: Create Purchase Contract with Reference to Purchase Requisition

##### Create Purchase Requisition (Outline Agreement Requisition)

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions Professional screen is displayed. |  |
| 3 | Create Purchase Requisition | On the Manage Purchase Requisitions – Professional screen, choose Create to create new purchase requisition. | New Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | Make the following entries and choose Enter.Document Type: Outline Agrmt. Reqn.(RV) |  |  |
| 5 | Enter detail data | In Items area, choose Create.Choose Material .In the Purchase Requisition Item page, make the following entries:Material: NS0001Plant: 3310Item Category: StandardAccount Assignment Category: UQuantity: For example, 50 |  |  |
| 6 | Save your entries. | Choose Apply to go to Purchase Requisition page, then choose Create. | A purchase requisition is created. |  |

##### Create Purchase Contract with Reference to Purchase Requisition

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser, | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions displays |  |
| 3 | Convert Purchase Requisition to Contract | Choose Go, if no purchase requistions show up:Select a purchase requisition created in the previous step for which the contract has to be created.You can also filter down the results by applying appropriate filters.For example:Purchasing Group: 001Plant: 3310Material: NS0001Choose Create Contract. |  |  |
| 4 | Purchase Contract Preview | Enter the following information in the preview screen of a contract:Contract Type: Qty Contract-PSE(CMK)Note Only the contract type CMK and CWK is used in this test script.Supplier: 33300001Valid From: Start date of the contractValid To: End date of the contractPurchasing Organization: 3310Target Value: Enter target value for document type CMK, for example, 100 AED. | The Purchase Contract data is contained in the preview screen. |  |
| 5 | Create Contract | Choose Create. | A purchase contract is created. |  |

#### Option Two: Create Purchase Contract with Reference to the Contract Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Contracts (F1600A). | The Manage Purchase Contracts screen is displayed. |  |
| 3 | Create Contract Template | On the Manage Purchase Contracts screen, choose Manage Templates. In the Templates popup screen, choose Create Template. |  |  |
| 4 | Enter Purchase Contract Data | Make the following entries and choose Enter.In Header Information section:Purchase Contract Name: for example, Contract template for Office SuppliesContract Type： CMK (Qty Contract-PSE)Purchasing Organization： 3310Supplier ： 33300001In General Information section,Target Value: XXPurchasing Group：001Company Code: 3310Valid From：TodayValid To：Today + 6 monthsIn section Delivery and Payment:Payment Terms：0001In section Items:Choose Create to add a new item.Account Assignment Category：Unknown (U)Material：NS0001Plant： 3310Choose Purchase Contract Item to go to Purchase Contract Item page.Quantity and Price:Net Order Price: XXPrice Unit: 1Order Price Unit: PCTarget Quantity: 50Order Unit : PCGR/IR ControlGR-Based Invoice Verification: SelectedInvoice Receipt: SelectedChoose Apply. | The Contract Template is created. |  |
| 5 | Save the Template | Choose Save as Template. | The Contract Template is saved. |  |
| 6 | Create Contract | Choose Manage Templates. In the pop up screen Template, select the template created in previous step and choose Create Contract. | Purchase Contract screen appears and the data from the template gets copied in this screen. |  |
| 7 | Save Contract | Choose Create. | A purchase contract is created. |  |
| 8 | Create Purchase Order from Contract (Optional) | Choose Back to return to Manage Purchase Contracts page.Filter the purchase contract created above, and select it. Then choose Create Purchase Order to open New Purchase Order pageChoose purchase order item to go to Purchase Order Item page.Order Quantity: XAccount Assignment Category: change from UnKnown(U) to Project(P)Go to Account Assignment section, select account assignment item, then input:WBS Element: search via Input Help, for example RealizationNote If you get error messageUser status PL&P is active.after selecting WBS element from value help, you can select another WBS element. You can refer to scope item J11 - Customer Project Management – Project-Based Services to select a project with In Execution status to avoid this error message (Open app Project Control - Professional Services Projects (F6869) with user Project Manager - Professional Services, choose Current Stage: In Execution then choose Go.)Choose Apply.Choose Apply.Choose Order. | A purchase order is created with reference to purchase contract. |  |

### Service Procurement

In the following chapters, we focus on the creation of a Purchase Order with Account Assignment Category P (Project). With this, the project will be debited with the hourly price of the purchase order. It only supports the intracompany process.

Alternatively, Account Assignment Category K (Cost Center) can be used. It can be used in intracompany as well as intercompany processes (see SAP Note [2424847](https://me.sap.com/notes/2424847)). Within the contingent worker process, the BADI Business Context: HCM – Timesheet Subcontractor Services with service type 02 is part of standard and therefore deprecated. A specific logic and implementation with service type 01 is not taken into consideration. Therefore, the project will be debited with the internal cost rate. If it is needed to get the full purchase price also as cost of the project, the personal cost rate of the contingent worker for this project can be set to the same amount as the purchase price of the related order.

You need to make sure that you use the Business Partner Role Service Performer when creating a contingent worker. The role Freelancer is currently not supported.

A purchase order item with multiple account assignment objects such as WBS element and cost center is not supported. Please use only one account assignment object.

#### Post Expenses for External Employees

##### Create Purchase Order for Expenses with Text Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Order | Choose Create. | The Purchase Orders screen appears. |  |
| 4 | Enter Field Values Within the Purchase Order | Make the following entries:Supplier: 33300001Purchasing group: 001Purchasing Organization: 3310Company Code: 3310Items:Choose Create to create an item, then choose Details to go to item detail.Short Text: For example,FlightMaterial Group: E004 (Travel Expenses Misc)Plant: 3310Order Quantity: For example, 1Unit of Measure: AUNet Order Price: For example, AEDAccount Assignment Category: P ProjectItems – Account Assignment:Select account assignment item, then input:WBS Element: search via Input Help, for example RealizationNote If you get error message User status PL&P is active after selecting WBS element from value Help, you can select another WBS element. You can refer to J11 - Customer Project Management – Project-Based Services scope item to select a project with In Execution status to avoid this error message.Choose Apply to go to Purchase Order Item screenItems – TaxTax Code: <Input Tax Code>Items - Process ControlGoods Receipt: <Deselect>Invoice Receipt: <Select>Goods-Receipt-Based Invoice Verification: <Deselect> | The purchase order is populated.Note For EU country, there are four Intrastat related fields: Intrastat Relevance field and Intrastat Exclusion field under Delivery and Invoice tab of PO header, Commodity Code field and Intrastat Srvc. Code field under Delivery Details tab of PO item. Please refer to BDT process for Intrastat related details. |  |
| 5 | Return to Purchase Order Header page | Choose Apply to return to Purchase Order header page. |  |  |
| 6 | Check Purchase Order for Completeness | Choose Messages (if possible).If the system displays a message, you must correct the purchase order. If no message occurs, the purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | To save the purchase order, choose Order. | The purchase order has been saved. |  |

##### Monitor Purchase Order Items(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can monitor each item in purchase orders, but by default only overdue items would be listed in the app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Monitor Purchase Order Items | Open Monitor Purchase Order Items (F2358). | The Monitor Purchase Order Items screen is displayed. Also numbers of current overdue PO items are listed. |  |
| 3 | Search for Purchase Orders | Below are frequently used filters:Purchase OrderDisplay CurrencyMaterial GroupMaterialSupplierPlantMake the above entries accordingly, then choose Go. | The search results show the details with the respective filter Criteria.You can set OVERDUE in filter Next Delivery Status and run the report by filtering on particular material/supplier, etc. to display the purchasing document accordingly. Overdue item should be mark in red.You can choose Adapt Filters to list filters to add adapt filters. |  |
| 4 | Display Purchase Order | Choose an individual line item of the Purchase Order you want to display the PO details. | The Purchase Order Item screen is displayed. |  |
| 5 | Verify data displayed on the object page | Verify data displayed on the object page. | The data should be logically in sync with Purchase Order. |  |

##### Create Supplier Invoice with PO Relation (With Item Block)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859).Note Choose Create Supplier Invoice (F0859), not Create Supplier Invoice - Advanced (MIRO) for the whole test script. | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries: General Information:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: Current datePosting Date : Current dateReference : Fill the Supplier Invoice Number(Length 10), for example: AV54674642 | Note If you want to change to other currency, you can maintain the exchange rate manually. Change Gross Invoice Amount currency to other currency, for example EUR. Choose See More. Then exchange rate appears according to the customizing settings. You can change the exchange rate manually. Then choose See Less to go back. |  |
| 4 | Enter Purchase Order References | In the Purchasing Document References area, make the following entries:Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase order number>Choose Enter and check below entries:Invoicing Party: 33300001 |  |  |
| 5 | Enter Payments Information | In the Payment area, make the following entries:Baseline Date: Current date |  |  |
| 6 | Check the Invoice Item Data | In the Invoice Item table, check the amount, quantity, and tax code.Amount: For example,Tax Code: <Input Tax Code> | Amount and quantity correspond to the values of the purchase order. |  |
| 7 | Change Item Amount to Block Invoice on Item Level (Optional) | If item amount in supplier invoice is different from PO amount, the item amount can be changed and the invoice will be blocked on item level with a blocking reason.Amount: For example, change to XXX AED (exceeding tolerance limit for price difference).Choose Arrow at the right side of the item to navigate to the item details. In the lower part of the detail screen, Blocking Reasons section shows the text “Price Variance”. |  |  |
| 8 | Enter Gross Invoice Amount | In the upper General Information screen area, make the following entry: |  |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.Choose Messages. If the system displays a message, you must correct the supplier invoice. If no message occurs, the supplier invoice is complete. |  |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. A dialog box displays the message: Invoice XX posted (blocked for payment). |  |

##### Check Blocked Supplier Invoice with Notification (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, supplier invoices with payment block are displayed. Blocked for Payment is a dynamic link which is visible only in invoice header when the invoice is blocked for payment. The link contains data relevant for explaining the block situation and its possible resolution, for example Actions to contact supplier/purchaser, Block related statistics and so on.

Situation and Notification will be triggered according to Selection Criteria set in preliminary steps. System automatically detects cash discount situations by daily job, and indicates critical situations using the notification functionality on the home screen. This enables Team Member to proactively react to potential overdue cash discount and avoid negative implications to the business processes of the company.

|  |
| --- |
| Note You must perform the two steps [Create Ready-to-Use Situation Type for Cash Discount at Risk (Optional)](#unique_16) [page ] 18 and [Create Team and Responsibilities (Optional)](#unique_18) [page ] 21 before testing this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoice List screen is displayed. |  |
| 3 | Search for Supplier Invoices | Make the following entries and choose Go.Invoice Document No.: invoice created above | The relevant supplier invoice is displayed. |  |
| 4 | Check Supplier Invoice Detail | In the list of the Supplier Invoices, select an Invoice Document by clicking the entire row.If the invoice is blocked for payment, choose Blocked for Payment link to go to Payment status page. You can check the information below.Information:You can see the message: This invoice is blocked for payment and its status is Open.Actions:Choose Contact Supplier to display supplier contact information.Choose Contact Purchaser to display purchaser contact information.Blocked Invoice Items:You can see the blocking reason on line item level.Invoice Timeline:You can see dates, such as invoice document date, invoice posting date, invoice payment due date and cash discount deadline(if there is any discount).Charts with statisticsBlocked Invoices Amount by Reason:You can see the amount of invoices blocked for the supplier and particular company codeBlocked Invoices Count by Reason:You can see the count of invoices blocked for the supplier and particular company codePayment Blocks by Reason:You can see the percentage of block reasons/occurrences | The Payment block tab is displayed. |  |
| 5 | Check Supplier Invoices with Cash Discount Notification | Choose the Notifications icon on the upper right part of the screen.Choose notification, under Discount at Risk - Payment Block, the example notification is as follows:Supplier invoices are blocked for payment. | The two supplier invoices which are at cash discount risk are displayed in Supplier Invoices List. |  |
| 6 | Check Situation Message in Supplier Invoice | Select one invoice in the above list to go to Supplier Invoice page. If notification is triggered for invoice, Situations tab will be added in supplier invoice. You can choose Close Situation, pick a reason for dismissing the situation and then confirm. | Situation Message is shown and dismissed. |  |

#### Purchase External Services with Service Material Item

##### Create Purchase Order for Service Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A), and choose Create. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Enter Field Values Within the Purchase Order | Make the following entries:Supplier: 33300001Company Code: 3310Purchasing Organization: 3310Purchasing Group: 001Currency: AEDItems: Choose Create to create an item, then choose the item to go to Purchase Order Item page.Material: For example, T001Plant: 3310Order Quantity: For example, 10Unit of Measure: HNet Order Price: For example, AEDService Performer: Select from F4. For example, JOHN EXTSERVPERF3310 (generic user for external service performer in company code 3310.Account Assignment Category: P projectIn Schedule Lines area:Start of Performance Period: Current DateEnd of Performance Period: Current Date + 6 MonthsIn Delivery Details area:Unlimited OverDelivery Allowed: SelectIn the Tax area:Tax Code: <Input Tax Code>In Process Control area:Invoice Receipt: SelectGoods Receipt: SelectGoods-Receipt-Based Invoice Verification: SelectSelect account assignment item, then input:WBS Element: for example RealizationChoose Apply twice to return to Purchase Order page | The purchase order is populated. |  |
| 4 | Add Material Item (Optional) | Items: Choose Create to create an item, then choose the item to go to Purchase Order Item page.Material: For example, NS0001Plant: 3310Order Quantity: For example, 10Unit of Measure: PCNet Order Price: For example, 10Account Assignment Category: P projectUnlimited OverDelivery Allowed: SelectTax Code: <Input Tax Code>Invoice Receipt: SelectGoods Receipt: SelectGoods-Receipt Based Invoice Verification: SelectSelect Account Assignment Item, then input:WBS Element: for example, RealizationChoose Apply twice to return to Purchase Order page | Note It is possible to maintain service item and material item in service entry sheet at same time.Materials allowed in the SES should meet following conditions: Materials with and without material master are allowed.No batch managed materials.No materials with classification.No materials with serial number.No materials with split valuation.No materials with manufacturer part numbers.No materials where the revision level is filled.No retail articles (with subitems in the PO). |  |
| 5 | Check Purchase Order for Completeness | Choose Messages (if possible).If the system displays a message, you must correct the purchase order. If no message occurs, the purchase order can be submitted. |  |  |
| 6 | Save Purchase Order | To save the purchase order, choose Order. | The purchase order is saved. |  |

##### Option One: Automatic Creation of Service Entry Sheet by Time Recording

###### Review Service Entry Sheets from Time Recording

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You must perform scope item Time Recording – Project-Based Services before testing this step. After time recording is approved, the service entry sheet is created automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Service Entry Sheets - Lean Services (F2027) and choose Go. | The service entry sheet list is displayed. |  |
| 3 | Review the service entry sheet | In the Manage Service Entry Sheets page, a new line of service entry sheet appears with status Approved(30).You may also select Timesheet from the dropdown list of Origin field, then choose Go, to filter service entry sheets that were generated from time recording.You can select the line and check details.Note For each time-recording, one SES will be created with one item. Bundling multiple time-recordings within one SES is not supported.An SES will be deleted automatically when the corresponding time-recording is deleted and approved.If a time recording is updated and approved, the existing SES will be deleted and a new SES will be created automatically. | The detail of service entry sheet is created. |  |

###### Review Error Logs for Service Entry Sheets Processing(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If errors occur during the creation or deletion of Service Entry Sheet, an error log will be written.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Monitor Service Entry Sheet Generation Log (F3495). | The Application Logs screen is displayed. The default value for Category is MMPUR_SES and for Subcategory is TIME_SHEET. |  |
| 3 | Review Error Log | Choose > on the right side of the log item. | The Logs Details screen is displayed. |  |

###### Schedule Automatic Creation of Service Entry Sheets from Time Recording(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you schedule an automatic Creation of Service Entry Sheets from Time Recording. This procedure is used for error handling, such as reprocessing of the failed time-recordings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Purchasing Jobs - Advanced (F1702) and choose Create. | The New Job screen is displayed. |  |
| 3 | Enter General Data | Make the following entries.General Information:Job Template: Automatic Creation of Service Entry Sheets from Time RecordingJob Name: For example, Automatic Creation of Service Entry Sheets from Time RecordingScheduling Options:Start Immediately: SelectedYou can also choose Define Recurrence Pattern to set other timing and determine its Recurrence.Posting Date: <Today’s date>Selection Parameters:Purchase Order: <Purchase order number>You can also choose other parameters.Choose Schedule in the bottom. | New application Job is scheduled. |  |
| 4 | Review the Application job | In the Application Jobs page，a new line of Application Job appears with status Finished. | The job is scheduled. |  |

##### Option Two: Manual Creation of Service Entry Sheet

###### Maintain Service Entry Sheet

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Service Entry Sheets - Lean Services (F2027) and choose Create. | The New Service Entry Sheet screen is displayed. |  |
| 3 | Enter field values | Make the following entries:SES Name: Service for Junior ConsultantReference PO: Purchase order numberSelect items you needed in Add Purchase Order Items and click Add.Items:Ref.PO item: 10Please choose Show More per Row if below fields are not visible.Performance Period: <today>-<today>Service Performer: Copy from reference POStated Quantity: for example, 5 | The purchase order is populated. | Note You can add material items in SES only if there is at least one service item. |
| 4 | Save the Service Entry Sheet | Choose Create to save the service entry sheet. | Service entry sheet is saved. | Note Additionally, it is possible to insert notes for header and item in multiple languages on Note tab. |
| 5 | Send for Approval | Choose Send for Approval to get approval. | Service Entry Sheet is sent for approval, and It should be automatically approved, because workflow Automatic Release of Service Entry Sheet is activated-only in step Configure Flexible Workflow for Service Entry Sheets.If other workflow is activated, it might need relevant receipt’s approval. |  |
| 6 | Check Process Flow (Optional) | Choose Navigation to item details, in Process Flow area, check the process flow information for the item; Process flow for item is displayed. |  |  |

##### Option Three: Import Service Entry Sheets

###### Configure Import Service Entry Sheets for Specific Users

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you make sure that Import of Service Entry Sheets for Specific Users is actived.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate Import of Service Entry Sheets for Specific Users | On the Configure Your Solution screen, search Activate Import of Service Entry Sheets for Specific Users, then choose Go.Select the line of the item and go to the next screen.On the Configure Your Solution - Service Purchasing and Entry screen, choose Configure on the line of configuration step with name Activate Import of Service Entry Sheets for Specific Users.Choose Configure. | The Configure Your Solution - Service Purchasing and Entry screen is displayed. |  |
| 5 | Enter User | On the Change View “Active Import of Service Entry sheets for Specific Users” screen,Choose New Entries.User : <User ID>You can use the Search Help to find the User ID for User ID alias is Purchaser.Choose Enter. | User is added |  |
| 6 | Save your data | Choose Save. | A User is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Import of Service Entry Sheets for Specific Users.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Active Import of Service Entry sheets for Specific Users” screen displays. |  |
| 3 | Enter User | On the Change View “Active Import of Service Entry sheets for Specific Users” screen,Choose New Entries.User : <User ID>You can use the Search Help to find the User ID for User ID alias is Purchaser.Choose Enter. | User is added |  |
| 4 | Save your data | Choose Save. | A User is saved. |  |

Result

The Activate Import of Service Entry Sheets for Specific Users is saved.

###### Import Service Entry Sheets

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
| 1 | Log on to Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Choose Upload | Choose Import.Note If you can't find the Import button, you need to carry out the step [Configure Import Service Entry Sheets for Specific Users](#unique_71) [page ] 45 first. |  |  |
| 4 | Download Template | On the Import Service Entry Sheets screen:Choose Download Template.If a dialog box appears, choose OK.Save Service Entry Sheet Upload template to the local machine.Note You can refert to the SAP Note [2249454](https://me.sap.com/notes/2249454) to know more about the list downloaded. | Excel Template download and consistency |  |
| 5 | Fill in Data on Excel template | Open the file and input data according to instruction on the file. |  |  |
| 6 | Select the file to upload | Choose Search Help to select the file you want to upload.If a dialog box appears, choose OK.In the dialog box, select the file you want to upload from your local computer. Choose Open. |  |  |
| 7 | Option A: Upload Excel in the foreground | Run In Background:<blank>Choose Import. Log Objects are displayed on the next screen. On the Display Log screen, check the application log.Log Object was created with message success. |  |  |
| 8 | Option B: Upload Excel Run in the background | Run In Background: <selected>Choose Import.If you need to monitor the background job status, you need to follow the steps below.Open Monitor Service Entry Sheet Generation LogData From-To: <Today>Category:MMPUR_SESSubcategory:UPLOADChoose Go. |  |  |
| 9 | Check Service Entry Sheet status | On the Manage Service Entry Sheets screen, search for the Service Entry Sheet created above.Check the status. |  |  |

##### Create Supplier Invoice with SES Relation

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries:Check the selection of purchase order items.Basic Information:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: Current dateInvoicing Party: 33300001Posting Date : Current dateReference : For example, Supplier Invoice Number |  |  |
| 4 | Enter Purchase Order References | In the Purchasing Document References area, make the following entries:Reference Document Category: Service Entry Sheet - Lean ServicesService Entry Sheet: <Service Entry Sheet number>Choose Enter and check below entries:Note As soon as an invoice exists, the corresponding time record will not be changeable any longer. If changes are required, the invoice must be cancelled first. | Note You can choose Assignment Options to select Multiple SES items.Choose Assignment Options. Then on the Assignment Options screen, you can either select multiple Service Entry Sheets from the value help or select multiple items by filtering them based on Service Performer and Performance Date in the value help. |  |
| 5 | Enter Payments Information | In the Payment area, make the following entries:Baseline Date: Current date |  |  |
| 6 | Check the Invoice Item Data | In the Invoice Item table, check the amount, quantity, and tax code.Tax Code: <Input Tax Code> | Amount and quantity correspond to the values of the purchase order. |  |
| 7 | Enter Tax Information | Make the following entries: |  |  |
| 8 | Enter Gross Invoice Amount | In the upper General Information screen area, make the following entries:Gross Invoice Amount: For example, AED |  |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate.Choose Messages. If the system displays a message, you must correct the supplier invoice. If no message occurs, the supplier invoice is complete. |  |  |
| 10 | Post Invoice | Choose Post. | The invoice is posted. A dialog box displays the message: Invoice XX posted. |  |

#### Procurement of Limits Item for a Project

##### Create Purchase Requisition for Limits Item

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | Choose Pur. Requisition (NB) from Document Type dropdown list.Check Automatic Source Determination checkboxChoose Create in Limit Items section, then choose Service.Item Description: Service with LimitsPlant: 3310Acct Assignment Category : PDesired Supplier: 33300001Expected Value: 200 AEDOverall Limit: 400 AEDStart Date: Today's dateEnd Date: Today's date + 1 monthGoods Receipt is Expected: CheckedInvoice Receipt is Expected: CheckedAccount AssignmentG/L Account: for example, 65001000Note Make sure G/L account used is already mapped with resource and key figure. If not, there would be an error during purchase document creation: G/L account is not assigned to an expense type.You can refer to the step [Map G/L Account with Resource and Key Figure (Optional)](#unique_62) [page ] 90Choose account assignment item, and input WBS Element: RealizationChoose Apply to return to Purchase Requisition Limit ItemPurchasing Organization: 3310Purchasing Group: 001 | The purchase Requisition is populated. |  |
| 5 | Return to Purchase Requisition Header page | Choose Apply to return to the header page of purchase requisition. |  |  |
| 6 | Save Purchase Requisition | Ignore warning Enter a service performer and choose Create to create a purchase requisition. | The purchase Requisition is saved. |  |

##### Convert Purchase Requisition into Purchase Order

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A) | The Process Purchase Requisitions screen displays the purchase requisition list. |  |
| 3 | Filter Item List | Search for the purchase requisition created before. | The Purchase Requisition list is filtered to show result. |  |
| 4 | View the Purchasing | Choose Assign Source of Supply.Note Choose Show More per Row on the right side of Create RFQ if this button is not displayed.On Assign Source of Supply screen, in the Supplier tab, enter the following search criteria:Supplier: 33300001Purchasing Organization: 3310Choose Go, select the item with supplier 33300001 and choose Assign.Message Purchase requisition updated successfully pops up. Choose OK. | The Purchaser Orders Preview is displayed. |  |
| 5 | Create Purchase Order | Select the purchase requisition, then choose Create Purchase Order.Choose the purchase order type Standard PO and choose Order. | Standard PO created under the number 45xxxxxxxx. |  |

##### Create Service Entry Sheet with Flexible Workflow

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027) and choose Create. | The New Service Entry Sheet screen is displayed. |  |
| 3 | Enter field values | Make the following entries:Under tab General Information:Name of Service Entry Sheet: Service for Limits ItemReference Purchase Order: Purchase order numberSelect items you need in screen Add Purchase Order Items and click Add.Under tab Items:Ref.PO Item: 10Please choose Show Details if below fields are not visible and make the following entries:Performance Period: <Today>-<Today>Service Performer: Select from F4. For example, JOHN EXTSERVPERF 3310 (generic user for external service performer in company code 3310.Stated Quantity: For example, 5Unit for Stated Quantity: For example, HNet Order Price: for example, 40 AEDPrice per Unit: for example, HIf purchase order with limit item is created from contract, Contract for Limit and Purchase Contract Item will be displayed on the Source of Supply tab. | The purchase order is populated. |  |
| 4 | Return to Service Entry Sheet header page | Choose Apply to return to Service Entry Sheet header page |  |  |
| 5 | Save the Service Entry Sheet | Choose Create to save the service entry sheet. | Service entry sheet is saved. |  |
| 6 | Send to Approval | Choose Send for Approval to get approval. | Service Entry Sheet is sent for approval, and It should be automatically approved, because workflow Automatic Release of Service Entry Sheet is activated-only in step Configure Flexible Workflow for Service Entry Sheets.If other workflow is activated, it might need relevant receipt’s approval. |  |

##### Create Supplier Invoice with PO Relation

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable Accountant . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | General Information:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: Current datePosting Date : Current dateReference : For example, Supplier Invoice Number |  |  |
| 4 | Enter Purchase Order References | In the Purchasing Document References area, make the following entries:Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: Purchase order numberChoose Enter and check below entries: |  |  |
| 5 | Enter Payments Information | In the Payment area, make the following entries:Baseline Date: Current date |  |  |
| 6 | Check the Invoice Items Data | In the Invoice Items table, check the amount, quantity, and tax code.Amount: For example, XX AEDTax Code: <Input Tax Code> | Amount and quantity correspond to the values of the purchase order. |  |
| 7 | Enter Gross Invoice Amount | In the upper General Information screen area, make the following entries:Gross Invoice Amount: For example, <amount>AED |  |  |
| 8 | Simulate Supplier Invoice and Check Messages | Choose Simulate.Choose Messages. If the system displays a message, you must correct the supplier invoice. If no message occurs, the supplier invoice is complete. |  |  |
| 9 | Post Invoice | Choose Post. | The invoice is posted. A dialog box displays the message: Invoice XX posted.. |  |

#### Post Expenses for Internal Employees w/o PO Relation

##### Create Supplier Invoice without PO/GR

Follow below procedure to create an individual invoice. If need to mass upload supplier invoice, please refer to scope item Accounts Payable (J60)

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2. | Open Create Supplier Invoice tile | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3. | Enter General Information | Make the following entries:General Information:Transaction: InvoiceCompany Code: 3310Invoicing Party: for example, JOHN INTSERVPERF 3310 (generic user for internal employee in company code 3310)Gross Invoice Amount:Only select currency AED in 2nd Input field, amount is entered later.Currency: AEDInvoice Date: TodayPosting Date: TodayReference: Fill in the Supplier Invoice Number(Length 10), for example: AV54674642Note Travel Expenses of Intercompanies Resources, make the following entries:Choose See More.Document Type: ER – Manual Expense Travel |  |  |
| 4. | Add Account Item | Choose Add to expand the G/L Account Items screen. |  |  |
| 5. | Enter G/L Account Item | Make the following entries and choose the black arrow next to Debit/Credit field to expand the Account Assignment subscreen.Debit/Credit: DebitGL/ Account: 61007000Amount: xxx AEDTax Code:WBS Element:For example: Realization (Choose Input Help and enter Realization in the Select: WBS element dialog box)Personnel Number: Choose an Employee ID | A new row for a GL/ Account Item displays with entry fields for the side of the Account, the G/L Account, and the Amount |  |
| 6. | Enter Tax Information | Make the following entries:Tax Amount: xxx AED |  |  |
| 7. | Enter Gross Invoice Amount | Go back to the upper General Information screen area.Gross Invoice Amount: xxx AED |  |  |
| 8. | Simulate Supplier Invoice | Choose Simulate.Choose Post. | The invoice is posted. A dialog box displays the message: Invoice XX posted. |  |

### Third-Party Order Processing

#### Procurement of General Material for a Project With Multiple Account Assignment

##### Create Purchase Order for Material Items With Multiple Account Assignment (Third-Party Order Processing for all Countries)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | New Purchase Orders screen is displayed. |  |
| 4 | Enter Purchase Order Data | Make the following entries and choose Enter.Supplier: 33300001Currency: AEDCompany Code: 3310Purchasing Organization: 3310Purchasing Group: 001Choose Create to add a new item.Navigate to the details of selected item by choosing Chevron (>), and make the following entries:Items – General Information:Item Category: Third-Party (S)Material: HW0001Order Quantity: 1 PCNet Order Price: x AEDCurrency: AEDPer: 1Plant: 3310Unit of measure: PCAccout Assignment Category: Third-Party Project (S)Customer: for example, 33100001Directly delivery to end customer)Items – Schedule Lines:Delivery date: current dateItems – Account Assignment:Choose Create to create new account assignment item.Note If you can't find Distribution (%) column and WBS Element column on Account Assignment Tab, you have to choose Settings to select Distribution (%) and WBS Element on the View Settings screen. Then you should choose OK to confirm.Choose the Account Assgmt No. 1 itemWBS Element : for example, RealizationDistribution (%): for example, 20Choose the Account Assgmt No. 2 itemWBS Element : for example, MaintenanceDistribution (%): for example, 80Items – TaxTax Code:<Input Tax Code>Items - Process ControlGoods Receipt: SelectInvoice Receipt: SelectGoods-Receipt Based Invoice Verification: Select | The purchase order is populated. |  |
| 5 | Check Purchase Order for Completeness | Choose Messages.If the system displays a message, you must correct entries in the purchase order.If no message occurs, the purchase order is complete. | The purchase order is complete. |  |
| 6 | Save Purchase Order | Choose Order to save the purchase order. | The purchase order is saved. |  |

##### Process Goods Receipt of Third-Party Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt screen is displayed. |  |
| 3 | Search for Purchase Order | Make the following entries:Purchasing Document: Enter a purchase order number. | The purchase order is displayed. |  |
| 4 | Select Purchase Order | Choose your purchase order. | The goods receipt is displayed. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. Select an item with a quantity of two or more pieces. Input Delivered quantity. |  |  |
| 6 | Post | Choose Post. | The Post Goods Receipt screen is displayed. The system message confirms that the goods receipt was posted successfully. |  |

##### Create Supplier Invoice with PO/GR Relation

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries:General Information:Transaction: InvoiceCompany Code: 3310Invoicing Party: 33300001Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: TodayPosting Date : TodayReference: Fill in the Supplier Invoice Number(Length 10), for example: AV54674642 | The general data for the invoice has been entered. |  |
| 4 | Enter Purchaing Document References | In the Purchasing Document References section, make the following entries.Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <purchase order number>Choose Enter and check the selection of the purchase order Items. | References to the purchase orders have been added to the invoice. |  |
| 5 | Check the Invoice Items Data | In the Invoice Items table, check the amount, quantity, and tax code for material.Note You can choose invoice item to display multiple account assignment detail on the next screen. | Amount and quantity correspond to the values of the goods receipt(s). |  |
| 6 | Enter Payments Information | In the Payment screen area, make the following entries.Baseline Date: Current date | The payments information has been entered. |  |
| 7 | Check Tax Data | In the Tax screen area, check the Tax Code. | The tax data has been entered. |  |
| 8 | Enter Gross Invoice Amount | In the upper General Information screen area, make the following entries and choose Simulate.Gross Invoice Amount: For example, AED | The gross amount of the invoice has been entered. |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose Simulate (if possible).If the system displays a message asking you to correct entries, you must change the supplier invoice. If no message occurs, you can post the supplier invoice. |  |  |
| 10 | Post Invoice | To post the supplier invoice, choose Post. | The invoice is posted. A dialog box displays the messageInvoice xxx postedNote If invoice is blocked, please refer to chapter [Workflow for Approving Supplier Invoice (Optional)](#unique_58) [page ] 86 to release supplier invoice. |  |

#### Procurement of Text Based Material for a Project

In this test case you create a text item assigned to a specific material group. L007 for Licenses or L008 for Hardware. Based on the material group the account determination will be processed.

##### Create Purchase Order for Text Items

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | On the Manage Purchase Orders screen, choose Create. | New Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Make the following entries and choose Enter.General Data:Supplier: 33300001Currency: AEDCompany Code: 3310Purchasing Organization: 3310Purchasing Group: 001:Items – General DataChoose Create to add the first text item.Short Text: Windows 10 (license)Choose Create to add the second text itemShort Text: PC (Hardware)Enter item details for each item.Item Category: Third PartyMaterial Group:L007 (Licenses)L008 (Hardware)Order Quantity: X PC (for L008), X AU (for L007)Net Order Price: XAEDCurrency: AEDPlant : 3310Unit of measure: PC (for L008), AU (for L007)Schedule LinesDelivery date: current date (for testing purposes)Customer: 33100001 (Directly delivery to end customer)Account Assignment Category: S Third-Party ProjectSelect account assignment item, then input:WBS Element:Realization (search via Input Help)Items – TaxTax Code: <Input Tax Code>The automatic account assignment is triggered by this step and messages are shown in case of issues.Goods Receipt: SelectInvoice Receipt: SelectGoods-Receipt-Based Invoice Verification: Select | The purchase order is populated. |  |
| 5 | Check Purchase Order for Completeness | Choose Messages.If the system displays a message, you must correct entries in the Purchase Order.If a message does not display, the Purchase Order is complete. |  |  |
| 6 | Save Purchase Order | Choose Order to save the Purchase Order. | The Purchase Order is saved. |  |

##### Post Goods Receipt of Material Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Receipt for Purchasing Document (F0843). | The Material Document XX posted screen is displayed. |  |
| 3 | Search for Purchase Order | On Purchasing Document: Enter a purchase order number. | The purchase order is displayed. |  |
| 4 | Select Purchase Order | Choose your purchase order. | The goods receipt is displayed. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. Select an item with a quantity of two more pieces. Input Delivered quantity. |  |  |
| 6 | Post | Choose Post. | The Post Goods Receipt screen is displayed. The system message confirms that the goods receipt was posted successfully. |  |

##### Create Supplier Invoice with PO/GR Relation (with Invoice Reduction)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries:General Information:Transaction: InvoiceCompany Code: 3310Invoicing Party: 33300001Bank: Enter a bank.Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: TodayPosting Date: TodayReference : Fill the Supplier Invoice Number(Length 10), for example: AV54674642 | The general data for the invoice has been entered. |  |
| 4 | Enter Purchasing Document References | In the Purchasing Document References screen, make the following entries.Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <purchase order number>Choose Enter and check the selection of the purchase order Items. | References to the purchase orders have been added to the invoice. |  |
| 5 | Check the Invoice Items Data | In the Invoice Item table, check the amount, quantity, and tax code.Tax Code: <Input Tax Code> | Amount and quantity correspond to the values of the goods receipt(s). Ensure that the tax code is <Input Tax Code> . |  |
| 6 | Deselect Non-Relevant Items | In the Invoice Item table, deselect the items that you do not want to post (if necessary).Deselect items that you do not want to post. |  |  |
| 7 | Enter Payments Information | In the Payment screen, make the following entries.Baseline Date: Current date | The payments information has been entered. |  |
| 8 | Enter Tax Data | In the Tax screen, enter the tax amount. | The tax data has been entered. |  |
| 9 | Reduce Invoice | Choose the item to navigate to the details screen. Choose Reduce invoice in the bottom. On the pop up Reduce Invoice page, make the following entries:Amount from Supplier: XX (Larger than amount in PO)Quantity from Supplier: XX .Choose OK to close the popup dialog and choose Back to Supplier Invoice to Main Page. | Supplier Invoice amount is reduced |  |
| 10 | Enter Gross Invoice Amount | In the upper General Information screen, make the following entries and choose Simulate. | The gross amount of the invoice has been entered. |  |
| 11 | Simulate Supplier Invoice and Check MessagesSimulate Accounting, check Messages and Nota Fiscal | Choose Messages (if possible).Choose Simulate. If there are no differences (or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Overview and Details area. The Supplier Invoice is complete to post. Check the Gross Invoice Amount against the items plus tax amount. |  |  |
| 12 | Post Invoice | To post the supplier invoice, choose Post. | The invoice is posted. A dialog box displays the message Invoice xxx posted |  |

##### Print Complaint Letter

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
| 1. | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoice List screen is displayed. |  |
| 3. | Search for Supplier Invoice | Make the following entry and choose Go.Invoicing Number: XXXXXXXX (created in step above) | The relevant supplier invoice is displayed. |  |
| 4 | Complaint Letter Overview | Click on the invoice document from the list and in the Output tab , choose Display Document under Display for the line of output type Letter of complaint (COMPLAINT). | The complaint letter opens as a PDF file. |  |
| 5 | Print Complaint Letter | On the Display page, you can select Print from menu by clicking right mouse. | The output items are sent to the printer queue. |  |

### Procurement of Consumable Material

#### Procurement of Consumable Material for a project

##### Maintain the Default Setting for Users

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The default setting for an employee should be maintained by the Administrator mandatorily.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Default Settings for Users - Purchase Requisitions (F1995). | The Default Settings for Users screen is displayed. |  |
| 3 | Enter the User ID | On the Default Settings for Users screen, enter the User ID and then choose Enter. | Note Please use the Search Help to find the User ID for User Name PROJECT_MANAGER_PROF. |  |
| 4 | Edit the Default Setting for User | On the Default Settings for Users screen, choose Edit on the upper right corner.Make the following entries:Plant: for example, 3310Currency: for example, AEDSource Determination: SelectedChoose Save. | Default Settings are set for users. |  |

##### Create Purchase Requisition for Consumable Material Items

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Purchase Requisitions (F1643A). | The My Purchase Requisitions screen is displayed. |  |
| 3 | Start Purchase Requisition creation | Without marking any selection, choose Create Item. | The Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | In the General Information section, make the following entries: | The Purchase Requisition screen is displayed. |  |
| 5 | Purchase Consumable Material with Material Number | Material: NS0001Quantity Requested: 100 PCDelivery Date: <today +30>Purchasing Group: 001Purchasing Organization: 3310Plant: <Plant>, for example, 3310Account Assignment Category: PChoose Account Assignments section, and make the following entries:G/L Account: for example, 51600000 for materials with a material number, The G/L account will be determined automatically.Select the right arrow in the Account Assignment area to navigate to the detailed account assignment page.WBS Element：Realization (- search via input help)Choose Apply.Choose Source of Supply section:Agreement/Item:46xxxxxxxxx/00xx：Assign(You can assign other source in the list, or find a supplier in the supplier list by choosing Add. Then you select F4 to choose a supplier. Then choose Fixed)Note Make sure G/L account used is already mapped with Resource and Key Figure. If not, there would be an error during purchase document creation: G/L account is not assigned to an expense type.You can refer to the step [Map G/L Account with Resource and Key Figure (Optional)](#unique_62) [page ] 90Choose Apply. | Check and maintain details. |  |
| 6 | Save Purchase Requisition | Choose Order to save the purchase Requisition. | A new Purchase order is created if no error is displayed in the dialog box. |  |

Result

The purchase requisition is created.

##### Convert Purchase Requisition into Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions screen displays the Purchase Requisition list. |  |
| 3 | Filter Item List | Make the following entries and choose Go.Choose Filter.Plant ： 3310Purchasing Group ：001Purchasing Organization： 3310 | The Purchase Requisition list is filtered to show fewer results. |  |
| 4 | View the Purchasing | Choose an itemand choose Create Purchase Order. | The New Purchase Order is displayed. | You can only convert a purchase requisition if a source is assigned. You have to check first and if no supplier is assigned you have to do so. |
| 5 | Create Purchase Order | For field Purchase Order Type, choose Standard PO and choose Order. | Standard PO created under the number 45xxxxxxxx. |  |

##### Optional Step: Change Purchase Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The system displays a list of purchase orders. |  |
| 3 | Choose a Purchase Order | Choose a purchase order from the list, then choose Edit. | The purchase order opens in edit mode. |  |
| 4 | Change Field Values of Purchase Order | Change certain field values of the purchase order created before.You can change any of these fields:Company codePurchasing groupPurchasing organizationMaterial on item levelQuantityNet price |  |  |
| 5 | Check Purchase Order for Completeness | Choose Messages.If the system displays a message, you must correct entries in the purchase order.If no message occurs, the purchase order is complete. | The purchase order is complete. |  |
| 6 | Save Purchase Order | To save the purchase order, choose Order. | The purchase order is saved. |  |

##### Print Purchase Order

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The system displays a list of purchase orders. |  |
| 3 | Choose a Purchase Order | Choose a purchase order from the list. | The purchase order opens in edit mode. |  |
| 4 | View Output Items | In the Output Management area, choose Display Document under Display | The purchase order document opens as a PDF file.All saved purchase orders with output status In Preparation can be viewed. |  |
| 5 | Print Output Items | On the PDF file Display page, you can select Print from menu by right-clicking mouse. | The output items are sent to the printer queue. |  |

##### Optional Step: Check Purchasing Document List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you check purchase orders for stock material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Purchasing Document Items - Professional (F0547B) | The My Purchasing Document Items screen displays the Purchasing Document Items list. |  |
| 3 | Filter Item List | Make the following entries and choose Go.Supplier: 33300001Purchasing Group: 001Plant: 3310 | The Purchasing Document Items list is filtered to show fewer results. |  |
| 4 | Switch to Purchase Orders View | Choose the Purchase Orders tab. | The Purchasing Document Items list displays only purchase orders. |  |
| 5 | Optional: Switch to Goods Receipts View or Supplier Invoices View | Choose the Goods receipts tab, or the Supplier Invoices tab. | The Purchasing Document Items list displays either material documents for goods receipts or supplier invoices. |  |
| 6 | Check Purchasing Document Details | Choose one of the Purchase Requisitions and Purchase Orders tabs,Note It is unable to view Goods Receipts, and Supplier Invoices document with Purchaser role. |  |  |
| 7 | View the Purchasing Document | Choose a Purchase Document Item. | The Detail screen (Fact Sheet) of the selected Purchase Document Item is displayed. |  |

##### Post Goods Receipt of Material Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Receipt for Purchasing Document (F0843). | The Material Document XX posted screen is displayed. |  |
| 3 | Search for Purchase Order | On Purchasing Document: Enter a purchase order number. | The purchase order is displayed. |  |
| 4 | Select Purchase Order | Choose your purchase order. | The goods receipt is displayed. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. Select an item with a quantity of two more pieces. Input Delivered quantity. |  |  |
| 6 | Post | Choose Post. | The Post Goods Receipt screen is displayed. The system message confirms that the goods receipt was posted successfully. |  |

##### Optional Step: Check Goods Receipt Details

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Material Documents Overview (F1077). | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts | Make the following entries and choose Go.Material: <Material Number> | The material document is displayed. |  |
| 4 | Select Goods Receipts | Choose your goods receipt. | The relevant data for the goods receipt is displayed. |  |

##### Optional Step: Reverse Goods Receipt

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Material Documents Overview (F1077).Purchase Order: <purchase order number> | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Documents | Make entries and choose Go. | The material document list is shown. |  |
| 4 | Select Material Document for Goods Receipt | Choose your Goods receipt.Note Alternatively, in the Material Document field, enter the material document number. | The relevant data for the goods receipt is displayed. |  |
| 5 | Post Reverse | Choose Reverse. |  |  |
| 6 | Confirm Reversal | In the Reverse Goods Movement dialog box, select the Material Document Item, and then choose OK. | The goods receipt has been reversed. |  |

##### Create Supplier Invoice with PO/GR Relation

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the Fiori App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries:General Information:Transaction: InvoiceCompany Code: 3310Invoicing Party: 33300001Bank: Enter a bank.Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: TodayPosting Date: TodayReference: Fill the Supplier Invoice Number(Length 10), for example: AV54674642 | The general data for the invoice has been entered. |  |
| 4 | Enter Purchasing Document References | In the Purchasing Document References screen, make the following entries.Reference Document Category:: Purchase order/Scheduling AgreementPurchase order/Scheduling Agreement: <purchase order number>Choose Enter and check the selection of the purchase order Items. | References to the purchase orders have been added to the invoice. |  |
| 5 | Check the Invoice Items Data | In the Invoice Item table, check the amount, quantity, and tax code.Tax Code: <Input Tax Code> | Amount and quantity correspond to the values of the goods receipt(s). |  |
| 6 | Deselect Non-Relevant Items | In the Invoice Item table, deselect the items that you do not want to post (if necessary).Deselect items that you do not want to post. |  |  |
| 7 | Enter Payments Information | In the Payment screen, make the following entries.Baseline Date: Current date | The payments information has been entered. |  |
| 8 | Check Tax Data | In the Tax section, check if there is tax code information and enter the tax amount if the tax rate is greater than zero.In the Tax area, you should see the same tax codes as in the items. If there is no tax, specify that the tax code is <Input Tax Code>. | The tax data has been entered. |  |
| 10 | Enter Gross Invoice Amount | In the upper General Information screen, make the following entries and choose Simulate.Gross Invoice Amount: <amount> AED . | The gross amount of the invoice has been entered. |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Messages (if possible).Choose Simulate. If there are no differences(or if the value is within the defined tolerance), a new screen Simulation appears. You can check the simulation results in Simulation Overview and Simulation Details area. the Supplier Invoice is complete to post. | The supplier invoice is posted. |  |
| 12 | Post Invoice | To post the supplier invoice, choose Post. | The invoice is posted. A dialog box displays the message :Invoice xxx has been posted successfully. |  |

#### Procurement of Text Based Consumable Material for a project

##### Create Purchase Order for Consumable Text Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The New Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Basic DataCurrency: AEDSupplier: 33300001Company Code: 3310Purchasing Organization: 3310Purchasing Group: 001In Items section, choose Create and then choose the new item and choose the Details(>). Enter the following data.Item Category: StandardShort Text: Consumable MaterialMaterial Group: YBMM01 (Non-Stock Material)Order Quantity: 100 PCNet Order Price: x AEDCurrency: AEDPrice Unit: 1 PCPlant: 3310Unit of measure: PCDelivery date: current date (for testing purposes)Account Assignment Category: P ProjectItems – Account Assignment:Choose the line and go to the next screen. Make the following entry and choose Apply.WBS Element：Realization (- search via input help)Under Supplier Confirmation Control tab, make the following entry:Confirmation Control: BlankItems – TaxTax Code:<Input Tax Code>Items – Process FlowGoods Receipt: SelectInvoice Receipt: SelectGoods-Receipt-Based Invoice Verification: SelectNote Make sure G/L account used is already mapped with Resource and Key Figure. If not, there would be an error during purchase document creation: G/L account is not assigned to an expense type.You can refer to the step [Map G/L Account with Resource and Key Figure (Optional)](#unique_62) [page ] 90 | The purchase order is populated. |  |
| 5 | Check Purchase Order for Completeness | If the system displays a message, you must correct entries in the purchase order.If no message occurs, the purchase order is complete. | The purchase order is complete. |  |
| 6 | Save Purchase Order | Choose Apply to return, then choose Order. | The purchase order is saved. |  |

##### Post Goods Receipt of Material Items

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Receipt for Purchasing Document (F0843). | The Material Document XX posted screen is displayed. |  |
| 3 | Search for Purchase Order | On Purchasing Document: Enter a purchase order number. | The purchase order is displayed. |  |
| 4 | Select Purchase Order | Choose your purchase order. | The goods receipt is displayed. |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted. Select an item with a quantity of two more pieces. Input Delivered quantity. |  |  |
| 6 | Post | Choose Post. | The Post Goods Receipt screen is displayed. The system message confirms that the goods receipt was posted successfully. |  |

##### Create Supplier Invoice with PO/GR Relation

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Information | Make the following entries:General Information:Transaction: InvoiceCompany Code: 3310Invoicing Party: 33300001Bank: Enter a bank.Gross Invoice Amount: Only select currency AED in the second input field. The amount is entered later.Invoice Date: TodayPosting Date : TodayReference: Fill the Supplier Invoice Number(Length 10), for example: AV54674642 | The general data for the invoice has been entered. |  |
| 4 | Enter Purchasing Document References | In the Purchasing Document References screen area, make the following entries.Reference Document Category: Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <purchase order number>Choose Create Items and check the selection of the Purchase Order Items . | References to the purchase orders have been added to the invoice. |  |
| 5 | Check the Invoice Items Data | In the Invoice Item table, check the amount, quantity, and tax code. | Amount and quantity correspond to the values of the goods receipt(s). |  |
| 6 | Deselect Non-Relevant Items | In the Invoice Item table, deselect the items that you do not want to post (if necessary).Deselect items that you do not want to post. |  |  |
| 7 | Enter Payments Information | In the Payment screen, make the following entries.Baseline Date: Current date | The payments information has been entered. |  |
| 8 | Check Tax Code | In the Tax section, check if there is tax code information and enter the tax amount if the tax rate is greater than zero.In the Tax area, you should see the same tax codes as in the items. If there is no tax, specify that the tax code is <Input Tax Code> . | The tax data has been entered. |  |
| 9 | Enter Gross Invoice Amount | In the upper General Information screen, make the following entries and choose the Simulate button.Gross Invoice Amount: For example, <amount>AED. | The gross amount of the invoice has been entered. |  |
| 10 | Post Invoice or Save as CompletedOption A: Post Invoice | Choose Post. Please skip step [Reject Supplier Invoice (Optional)](#unique_54) [page ] 83 to [Release Completed Supplier Invoice](#unique_56) [page ] 85 . | Your invoice is posted. |  |
|  | Option B: Save as Completed | Choose Back and then choose Save as Completed.Note You can choose Park to park the invoice first. After that, you can edit the created supplier invoice to choose Save as Completed.If Invoice triggers Workflow for Parked Invoice as Complete, Approval Details tab will be shown in supplier invoice with workflow steps and processor. | The invoice is saved as completed. A dialog box displays the messageInvoice xxx saved as completed.. |  |

##### Release Completed Supplier Invoice

###### Reject Supplier Invoice (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as approver set in preliminary step, such as Project Manager - Professional Services. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Reject Supplier Invoice | On the Release of Completed Invoice screen, choose Reject at the bottom of the screen.On the Submit Decision screen, select Decision Reason from dropdown list, add note if necessary and choose Submit. | Task successfully processed. |  |

###### Rework Supplier Invoice (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoice List screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above, and then select the invoice. | The Supplier Invoice is displayed. |  |
| 5 | Edit Supplier Invoice | Choose Edit to update invoice, for example Reference field.Then choose Save as Completed at the bottom of the screen. | Supplier Invoice is updated and saved as completed again. |  |

###### Release Completed Supplier Invoice

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
| 1 | Log On | Log on to the SAP Fiori launchpad as approver set in preliminary step, such as Project Manager - Professional Services. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Approve Supplier Invoice | On the Release of Completed Invoice screen, choose Release at the bottom of the screen.On the Submit Decision screen, add note if necessary and choose Submit.Note You need to perform this step twice, because both WBS Element and Profit Cen-ter are used in supplier invoice. | Task successfully processed. |  |

### Purchase Document Processing (Optional Steps)

These steps can be executed for purchase document posted for material and service procurement.

#### Release Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoices list screen is displayed. |  |
| 3 | Check Supplier Invoice Detail | In the supplier invoice list, select an invoice document that is blocked for payment. | The invoice document is displayed. |  |
| 4 | Release the Invoice | Choose Release. | The invoice is released. |  |

#### Workflow for Approving Supplier Invoice (Optional)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as approver set in preliminary step，such as Project Manager - Professional Services | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F5331). | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Approve Supplier Invoice | On the Release of Blocked Invoice screen, choose Release at the bottom of the screen.On the Submit Decision screen, add note if necessary and choose Submit.Note If attachment is uploaded during invoice creation, the attachment can be found in My Inbox APP under Attachments tab of the invoice. The attachment will be renamed with prefix “H_”. | Task is successfully processed. |  |

#### Reverse Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as an Accounts Payable Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the Fiori App | Open Supplier Invoices List. | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for Supplier Invoices | On the Supplier Invoice List screen, make the following entries and choose Go.Invoicing party: 33300001 | The relevant supplier invoices are displayed; grouped by status Posted and Reversal. |  |
| 4 | Check Supplier Invoice Detail | In the Supplier Invoices list, select the invoice created in the previous step. | The invoice document is displayed. |  |
| 5 | Reverse the Invoice | Choose Reverse. | The Reverse Invoice screen is displayed. |  |
| 6 | Enter Reason for Reversal | On the Reverse Invoice screen, choose OK. | The invoice is reversed. |  |

#### Clear GR / IR Clearing Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, one or more postings are cleared.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Clear GR/IR Clearing Account (MR11). | The Maintain GR / IR Clearing Account screen is displayed. |  |
| 3 | Search for Purchasing Documents | On the Maintain GR/IR Clearing Account screen, make the following entries and choose Execute (F8).Company : 3310Plant: 3310Purchase Order Date to: today | The relevant purchased orders are displayed. |  |
| 4 | Post Clearing | If purchase orders exist and need to be cleared, select one and choose Post (Ctrl + F12). | The clearing document is created. |  |
| 5 | Write Down Clearing Document Number | The clearing document is created. Write down its number as it is required for the next step. | One or more postings are cleared. |  |

#### Cancel Accounting Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the GR/IR clearing posting is reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display/Cancel Account Maintenance Document (MR11SHOW). | The Display / Cancel Account Maintenance Document screen is displayed. |  |
| 3 | Search for Accounting Maintenance Document | On the Display / Cancel Account Maintenance Document screen, enter the Account maintenance document / fiscal year that you created in the previous step and then choose Overview .Account maintenance document / fiscal year: <from previous step> | The accounting maintenance document is displayed. |  |
| 4 | Reverse Accounting Document | On the Display / Cancel Account Maintenance Document screen, select the Line Item that you have created previously and then choose Reverse Document(Shift + F5). | The Reversal Document Post Date screen opens. |  |
| 5 | Reverse Accounting Document | On the Reversal Document Post Date screen, choose Reverse. | The accounting maintenance document is reversed, the reversal document number is displayed. |  |

#### Map G/L Account with Resource and Key Figure (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you will Map G/L Account with Resource and Key Figure. Please make sure G/L account used is already mapped with Resource and Key Figure. If not, during purchase document creation, there would be error: G/L account is not assigned to an expense type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Your Solution | Choose Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | In the Manage Your Solution screen, open Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Resources | Search Define Expenses. Choose configuration with name Customer and Internal Project Management from search result, then choose Configure on the right side of configuration steps with name Define Expenses. | The "Define Expenses": Change screen is displayed. |  |
| 5 | Map G/L Account with Resource and Key Figure | Choose a Resource ID checkbox, for example S000 Purchased Services. Double click Map Expenses with Key Figures, then choose COST. Double click Map Key Figure with G/L Account, then choose New Entries. For example, input YCOA in ChAc and 65001000 in GLAcc. Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | G/L Account is mapped with Resource and Key Figure. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Define Expenses.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Expenses": Change screen displays. |  |
| 3 | Map G/L Account with Resource and Key Figure | Choose a Resource ID checkbox, for example S000 Purchased Services. Double click Map Expenses with Key Figures, then choose COST. Double click Map Key Figure with G/L Account, then choose New Entries. For example, input YCOA in COA and 65001000 in GLAcc. Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one. Then choose Continue. | G/L Account is mapped with Resource and Key Figure. |  |

Result

G/L Account is mapped with Resource and Key Figure.

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Edit Supplier Invoice Settings (F3813). | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, the system message contains invoice and journal entry number when invoice is created.If parameter is unchecked, the system message contains invoice number only when invoice is created.When this parameter is changed, it will be effective immediately for the APP Create Supplier Invoice. However, for the APP Create Supplier Invoice - Advanced, user needs to logout and login again to make it effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

## Appendix

### Process Chains

The process to be tested in this test case is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test case, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Customer Project Management – Project-Based Services (J11) | This is the main end-to-end business process. |

#### Preceding Processes

You may first have completed the following business processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Customer Project Management – Project-Based Services (J11) | Employee must be assigned to a project created in J11. |
| Time Recording – Project-Based Services (J12) | This process should be run to have time recording for external employee. |

### Relevant Features

Listed here are some important application functionalities related to Purchase Order outputs, which are not covered in the above test procedures.

| Function Area | Function | Detailed Information | Comment |
| --- | --- | --- | --- |
| Determination of Account Assignment Category | WebGUI: Determination of Account Assignment Category (S_ER9_52000307) | To determine the account assignment category that is required in the item in a service entry sheet. |  |

### Import Work Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Service Level Agreements (F6183A) | The Manage Workforce screen displays.The app is used to create and update workers (employees and contingent workers), including work agreements and change employment situations.Record the Business Partner ID for next step. |  |
| 3 | Import Worker Data | Refer to the following document to create a worker or perform mass import of worker data:[How to Import Worker Data](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fhelp.sap.com%2Fdocs%2FSAP_S4HANA_CLOUD%2F0bebd08dffca45afa67b1f751199afd0%2Fdca109e887a745e0ba61593b230e4f20.html%3Fstate%3DDRAFT%26version%3D2502.VAL)More details about managing workforce can be found at [Manage Workforce](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fhelp.sap.com%2Fdocs%2FSAP_S4HANA_CLOUD%2F0bebd08dffca45afa67b1f751199afd0%2Fbcbc2126696f422f844d5c631ff9cc03.html%3Fstate%3DDRAFT%26version%3D2502.VAL). | Record the Business Partner ID for next step. |  |

### Creating Supplier Master Data – Company Code Data for Worker

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data (MDG Cloud). |  |  |
| 2 | Access the App | Open Manage Supplier Master Data (F1053A) |  |  |
| 3 | Enter Supplier Details | Enter Business Partner ID which recorded in step[Import Work Data](#unique_79) [page ] 94.Additionally, you can select more details such as Street.Choose Go.From the results list, select a Supplier.Choose Edit.Note This step assumes that you are continuing from the previous step and are already navigated to Master Data - Manage Supplier Master Data (F1053A). After you have saved your general data from the previous section, the system is in display mode. To continue, you must be in edit mode.On the Manage Supplier screen, choose Company Codes. In the Company Codes section, choose Create.In the Company Codes section, choose an entry to open a details view. Make the following entries:On the General Data tab:Company Code: Enter the company code, for example, 3310.On the Finance tab:Finance - Accounting:Reconciliation Account: For example, 21100000 - Payables Domestic.Choose Create, and then choose Apply.Note Make sure that the system messageDraft saveddisplays at the bottom of the screen before you return to the main screen. | The data of Supplier are entered. |  |
| 4 | Save Your Data | Choose Save. | System message displays that the object is saved. |  |

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
- related-to :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]
- related-to :: [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J13_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 162,102 chars in the whole document
