---
id: 10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed
title: "Test Script: Procurement of Services (22Z_AE) - SAP S/4HANA Cloud Public Edition (22Z_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for scope item 22Z (UAE, company code 3310): service PO, service entry sheet, supplier invoice, with prerequisites and workflow setup."
cluster: 10-procurement
tags: [kb/procurement, topic/procurement-of-services]
aliases: [22Z_S4CLD2608_BPD_EN_AE]
keywords: [Procurement of Services, service procurement, purchase requisitions, purchase orders, purchase contracts, item hierarchies, service entry sheets, flexible workflow, supplier invoices, multiple account assignment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22Z_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-803
topic: 10-procurement/procurement-of-services
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Procurement of Services (22Z_AE) - SAP S/4HANA Cloud Public Edition (22Z_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22Z_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Procurement of Services** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Procurement of Services (22Z_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232848893)

[2 Prerequisites 6](#_Toc232848894)

[2.1 System Access 6](#_Toc232848895)

[2.2 Roles 6](#_Toc232848896)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232848897)

[2.4 Additional Manual Configuration 9](#_Toc232848898)

[2.5 Business Conditions 9](#_Toc232848899)

[2.6 Ticket Component 9](#_Toc232848900)

[2.7 Preliminary Steps 10](#_Toc232848901)

[2.7.1 Create Purchasing Info Record 10](#_Toc232848902)

[2.7.2 Configure Flexible Workflow for Purchase Order 14](#_Toc232848903)

[2.7.2.1 Check Flexible Workflow for Purchase Order Approval 14](#_Toc232848904)

[2.7.2.2 Configure Flexible Workflow for Purchase Order 16](#_Toc232848905)

[2.7.3 Configure Flexible Workflow for Service Entry Sheets 17](#_Toc232848906)

[2.7.3.1 Configure Flexible Workflow for Service Entry Sheets 17](#_Toc232848907)

[2.7.4 Configure Import Service Entry Sheets for Specific Users (Optional) 18](#_Toc232848908)

[2.7.5 Configure Flexible Workflow for Supplier Invoice 20](#_Toc232848909)

[2.7.5.1 Activate Flexible Workflow for Supplier Invoice 20](#_Toc232848910)

[2.7.5.2 Check Workflow for Supplier Invoice 22](#_Toc232848911)

[2.7.5.3 Update Cost Center for User Responsible 23](#_Toc232848912)

[2.7.5.4 Update Profit Center for User Responsible 23](#_Toc232848913)

[2.7.6 Edit User-Specific Parameters for Supplier Invoices (Optional) 24](#_Toc232848914)

[2.7.7 Configure for Employee Self Services Procurement 25](#_Toc232848915)

[2.7.7.1 Maintain the Default Setting for Users 25](#_Toc232848916)

[2.7.7.2 Activate Flexible Workflow for Purchase Requisition 26](#_Toc232848917)

[2.7.7.2.1 Check Flexible Workflow for Purchase Requisition Approval 26](#_Toc232848918)

[2.7.7.2.2 Configure Flexible Workflow for Purchase Requisition (Optional) 28](#_Toc232848919)

[2.7.8 Update Master Data for Automatic Purchase Order Creation from Purchase Requisition 29](#_Toc232848920)

[2.7.8.1 Change Material (Services) Master Data - Purchasing Data 29](#_Toc232848921)

[2.7.8.2 Change Supplier Master Data - Purchasing Organization Data 30](#_Toc232848922)

[2.7.8.3 Generate Source List 31](#_Toc232848923)

[2.7.9 Item Hierarchies and Model Product Specification 33](#_Toc232848924)

[2.7.9.1 Activate Item Hierarchies in Purchasing 33](#_Toc232848925)

[2.7.9.2 Manage Model Product Specifications (Optional) 34](#_Toc232848926)

[3 Overview Table 39](#_Toc232848927)

[4 Test Procedures 43](#_Toc232848928)

[4.1 Standard Procurement of Service 43](#_Toc232848929)

[4.1.1 Option A: Create Purchase Requisition 43](#_Toc232848930)

[4.1.2 Option A: Convert Purchase Requisition to Purchase Order 49](#_Toc232848931)

[4.1.3 Option B: Create Purchase Order 52](#_Toc232848932)

[4.1.4 Option C: Create Purchasing Contract 58](#_Toc232848933)

[4.1.5 Option C: Create Purchase Order 60](#_Toc232848934)

[4.1.6 Option D: Create Contract with Item Hierarchy 61](#_Toc232848935)

[4.1.7 Option D: Create Purchase Order with Item Hierarchy from Contract 64](#_Toc232848936)

[4.1.8 Change Purchase Order 65](#_Toc232848937)

[4.1.9 Approve Purchase Order (Optional) 66](#_Toc232848938)

[4.1.10 Check Purchase Order Approval Details (Optional) 67](#_Toc232848939)

[4.1.11 Preview Purchase Order (Optional) 68](#_Toc232848940)

[4.1.12 Maintain Service Entry Sheet with Flexible Workflow 69](#_Toc232848941)

[4.1.13 Approve Service Entry Sheet with Flexible Workflow 72](#_Toc232848942)

[4.1.14 Check Service Entry Sheet Details(Optional) 73](#_Toc232848943)

[4.1.15 Create Supplier Invoice 74](#_Toc232848944)

[4.1.15.1 Option A: Create Supplier Invoice with PO/GR Relation 74](#_Toc232848945)

[4.1.15.2 Option B : Create Supplier Invoice with PO/GR relation – Save As Completed (Optional) 76](#_Toc232848946)

[4.1.15.2.1 Create Supplier Invoice with PO/GR Relation 76](#_Toc232848947)

[4.1.15.2.2 Release Completed Supplier Invoice 78](#_Toc232848948)

[4.1.16 Release Blocked Supplier Invoice (Optional) 81](#_Toc232848949)

[4.2 Multiple Account Assignment for Procurement of Services 82](#_Toc232848950)

[4.2.1 Option A: Create Purchase Requisition 82](#_Toc232848951)

[4.2.2 Option A: Convert Purchase Requisition to Purchase Order 85](#_Toc232848952)

[4.2.3 Option B: Create Purchase Order 86](#_Toc232848953)

[4.2.4 Change Purchase Order 89](#_Toc232848954)

[4.2.5 Approve Purchase Order (Optional) 90](#_Toc232848955)

[4.2.6 Check Purchase Order Approval Details (Optional) 91](#_Toc232848956)

[4.2.7 Preview Purchase Order (Optional) 92](#_Toc232848957)

[4.2.8 Maintain Service Entry Sheet with Flexible Workflow 93](#_Toc232848958)

[4.2.9 Approve Service Entry Sheet with Flexible Workflow 96](#_Toc232848959)

[4.2.10 Create Supplier Invoice 98](#_Toc232848960)

[4.2.11 Release Blocked Supplier Invoice (Optional) 100](#_Toc232848961)

[4.3 Automatic Purchase Order Creation from Purchase Requisition 100](#_Toc232848962)

[4.3.1 Create Purchase Requisition 100](#_Toc232848963)

[4.3.2 Automatic Creation of POs for Service Materials 102](#_Toc232848964)

[4.3.3 Change Purchase Order 104](#_Toc232848965)

[4.3.4 Approve Purchase Order (Optional) 105](#_Toc232848966)

[4.3.5 Check Purchase Order Approval Details(Optional) 106](#_Toc232848967)

[4.3.6 Preview Purchase Order (Optional) 106](#_Toc232848968)

[4.3.7 Maintain Service Entry Sheet with Flexible Workflow 107](#_Toc232848969)

[4.3.7.1 Option A: Maintain Service Entry Sheet Manually 108](#_Toc232848970)

[4.3.7.2 Option B: Import Service Entry Sheets 109](#_Toc232848971)

[4.3.8 Approve Service Entry Sheet with Flexible Workflow 111](#_Toc232848972)

[4.3.9 Create Supplier Invoice 113](#_Toc232848973)

[4.3.10 Check Service Entry Sheet Details(Optional) 114](#_Toc232848974)

[4.4 Employee Self Services Procurement 115](#_Toc232848975)

[4.4.1 Create Purchase Requisition 115](#_Toc232848976)

[4.4.2 Approve Purchase Requisition (Optional) 116](#_Toc232848977)

[4.4.3 Convert Purchase Requisition to Purchase Order 117](#_Toc232848978)

[4.4.4 Change Purchase Order (Optional) 118](#_Toc232848979)

[4.4.5 Approve Purchase Order (Optional) 119](#_Toc232848980)

[4.4.6 Check Purchase Order Approval Details(Optional) 120](#_Toc232848981)

[4.4.7 Preview Purchase Order (Optional) 121](#_Toc232848982)

[4.4.8 Maintain Service Entry Sheet with Flexible Workflow 122](#_Toc232848983)

[4.4.9 Approve Service Entry Sheet with Flexible Workflow 124](#_Toc232848984)

[4.4.10 Check Service Entry Sheet Details(Optional) 125](#_Toc232848985)

[4.4.11 Create Supplier Invoice 126](#_Toc232848986)

[5 Appendix 129](#_Toc232848987)

[5.1 Process Integration 129](#_Toc232848988)

[5.1.1 Preceding Processes 129](#_Toc232848989)

[5.1.2 Related Processes 129](#_Toc232848990)

[5.1.3 Succeeding Processes 129](#_Toc232848991)

[5.2 Set up Mail Notification for Service Entry Sheet Workflow 130](#_Toc232848992)

[5.3 Set up Mail Notification for Supplier Invoice Workflow 132](#_Toc232848993)

[5.4 Set up Mail Notification for Supplier Invoice Workflow with Factory Calendar 134](#_Toc232848994)

[5.5 Mass Change of Posting Date 135](#_Toc232848995)

[5.6 Upload Model Product Specification 136](#_Toc232848996)

[5.7 Test Automation Tool 137](#_Toc232848997)

## Purpose

Overview

This scope item contains the creation and approval of purchase orders for services. This process can also be triggered via the creation of a purchase requisition, which is later converted to a purchase order. The service fulfillment can be steered and monitored with the service entry sheet. Afterwards, the invoicing process is triggered.

The scope item comprises standard as well as limit items and can be conducted with different optional steps.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Employee - Procurement | SAP_BR_EMPLOYEE_PROCUREMENT | Self Services - Procurement | SAP_MM_SPT_EMPLOYEE_SERVICES_PC |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Supplier | 33300001 | Domestic UAE Supplier 1 |  |
| Supplier | 33300002 | Domestic UAE Supplier 2 |  |
| Purchase organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 | Group 001 |  |
| Purchasing group | 003 | Group 003 |  |
| Material | SM0001 | Service Material 01 |  |
| Material Group | YBMM01 | Non-Sto Mat. w. ID |  |
| Cost Center | 33101501 | R&D Cost center |  |
| Cost Center | 33101601 | Marketing Cost Center |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS - MDS |
| BHD | Create Purchasing Info Record - MDS - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/00a879805b412725dc12171b46beb401)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM posting Period master data script. Posting period is up to data. |
| 1NT - Project Control – Finance(Optional) | You can create WBS for Account Assignment Category P. |
| 35F - Project Control – Capital Projects(Optional) | You can create WBS for Account Assignment Category P. |

### Ticket Component

If you have some problems while using following App, please open an SAP support ticket with corresponding component.

| App | Component |
| --- | --- |
| Manage Purchase Orders (F0842A)Note This app also applies to item hierarchy cases. | MM-FIO-PUR-PO |
| Manage Purchase Requisitions - Professional (F2229)Note This app also applies to item hierarchy cases. | MM-FIO-PUR-REQ-PRF |
| Process Purchase Requisitions - Deprecated (F1048) | MM-FIO-PUR-REQ-SOC |
| My Inbox - All Items (F0862) | CA-INB-FIO |
| Manage Service Entry Sheets - Lean Services (F2027) | MM-PUR-SVC-SES |
| Create Supplier Invoice (F0859) | MM-FIO-IV |
| Create Supplier Invoice - Advanced (MIRO) | MM-IV-LIV |
| Schedule Purchasing Jobs - Advanced (F1702) | MM-FIO-PUR |
| Manage Purchase Contracts (F1600A)Note This app also applies to item hierarchy cases. | MM-FIO-PUR-SQ-CON |
| Manage Model Product Specifications (F5079) | MM-PUR-MPS |

### Preliminary Steps

#### Create Purchasing Info Record

Purpose

In this procedure, you create info records for procure process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Create Purchasing Info Record 1 | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Go to Header area, make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Material: SM0001Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: <Delivery Time>, for example, 5Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, 10Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, 10Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: <Order Unit>, for example, HStandard Order Quantity: <Standard Order Quantity>, for example, 1Select the following entries if required:Unlimited Delivery: DeselectedGoods-Receipt-Based Invoice Verification: DeselectedNo Evaluated Receipt Settlement : SelectedOrder Acknowledgement Requirement: Deselected | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To:12/31/9999Amount: 10Pricing Unit: <Pricing Unit>, for example, 1Currency: <Currency>, for example, AED | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create.Choose Back to go back to screen Manage Purchasing Info Records. | A purchasing info record is saved. |  |
| 11 | Create New info record 2 | Repeat step 1 to step 10 to create an new info record for below master data.Supplier: 33300002 withMaterial: SM0001Supplier: 33300001 withMaterial: TG11 |  |  |
| 12 | Create New Info record 3 | On the screen Manage Purchasing Info Records.Choose Create. |  |  |
| 13 | Enter Header Data | On the screen Purchasing Info record, go to Header area, make the following entries:Info Record Description: for example, Info record for 33300001 / P001Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Material Group: YBMM01Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 14 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999Sort Term: <enter the term here> | Purchasing Data is added. |  |
| 15 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDORMake the following entries:Delivery Time in Days: <Delivery Time>, for example, 5Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, 10Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, 10Tax Code: V0Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: <Order Unit>, for example, HStandard Order Quantity: <Standard Order Quantity>, for example, 1Select the following entries if required:Unlimited Delivery: DeselectedGoods-Receipt-Based Invoice Verification: DeselectedNo Evaluated Receipt Settlement : SelectedOrder Acknowledgement Requirement: Deselected | Delivery and Quantity Data is added. |  |
| 16 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: <Today>Valid To: 12/31/9999Amount: 30Pricing Unit: <Pricing Unit>, for example, 1Currency: AED | Condition Data is added |  |
| 17 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 18 | Save your data | Choose Create.Choose Back to go back to screen Manage Purchasing Info Records. | A purchasing info record is saved. |  |

Result

The Purchasing info records are created.

#### Configure Flexible Workflow for Purchase Order

##### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check flexible workflow for purchase order approval.

Make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to next screen.On the Configure Your Solution – Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBScenario based workflow:SelectNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Activate Flexible Workflow for PO Approval | Make sure the following entries are made:Document Type: NBScenario based workflow:XNote You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

##### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create and make following entries:Workflow Name: Test Workflow for Purchase OrderGo to the Start Conditions area and choose Purchasing group of purchase order isPurchasing Group: 003Choose Create Another Condition and make the following entries:Total net amount of purchase order is greater than, with Price10, and Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by： One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated.For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

#### Configure Flexible Workflow for Service Entry Sheets

##### Configure Flexible Workflow for Service Entry Sheets

Purpose

In this procedure, you make sure Flexible Workflow for Service Entry Sheets is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Service Entry Sheets - Lean Services (F3173). | The Manage Workflows screen is displayed. |  |
| 3 | Check Automatic Release of Service Entry Sheet | In Workflows list, choose Automatic Release of Service Entry Sheet item, make sure workflow Automatic Release of Service Entry Sheet is in active status. If not, select it and choose Activate. | The Workflow Item is activated. |  |
| 4 | Create Manage Workflow | Choose Create and make following entries:Workflow Name: Multi step approval (total net amount > 1000AED)Go to the Start Conditions area and choose Service entry sheet is external with NoChoose Create Alternative Predictions and make the following entries:Total net amount of service entry sheet is greater than, with Amount10, and Currency: AED | Release of Service Entry Sheet (Multi-step approval)Total net amount of service entry sheet is greater than 1000 AED is configured. |  |
| 5 | Set Approval | In the Steps area, choose Create and make the following entries:Step Type: Release Service Entry SheetGo to the RECIPIENTS area:Assignment By: UserUser: Select User with PROJECT_MANAGER_PROF from F4 help.Step to be completed by: One of the recipients.Choose Create. |  |  |
| 6 | Save Manage Workflow | Choose Save. | Release of Service Entry Sheet (multistep approval) and total net amount of service entry sheet is greater than 10 is configured |  |
| 7 | Activate Workflow Item | Back to Workflow Details Screen and choose Activate. | The Workflow Item is activated. |  |
| 8 | Maintain Email Templates(Optional) | Use the app Maintain Email Templates. It enables you to send an email notification to the recipients of a workflow item when the workflow item is available in the app My Inbox. For more information, see the chapter [Set up Mail Notification for Service Entry Sheet Workflow](#unique_13) [page ] 130. |  |  |

#### Configure Import Service Entry Sheets for Specific Users (Optional)

Purpose

In this procedure, you make sure that Import of Service Entry Sheets for Specific Users is activated.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate Import of Service Entry Sheets for Specific Users | On the Configure Your Solution screen, search Activate Import of Service Entry Sheets for Specific Users, then choose Go.Select the line of the item and go to the next screen.On the Configure Your Solution - Service Purchasing and Recordingscreen, choose Configure on the line of configuration step with name Activate Import of Service Entry Sheets for Specific Users.Choose Configure. | The Configure Your Solution - Service Purchasing and Recording screen is displayed. |  |
| 5 | Enter User | On the Change View “Active Import of Service Entry sheets for Specific Users” screen,Choose New Entries.User : <User ID>You can use the Search Help to find the User ID for User ID alias is Purchaser.Choose Enter. | User is added |  |
| 6 | Save Data | Choose Save. | A User is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Import of Service Entry Sheets for Specific Users.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Activate Import of Service Entry Sheets for Specific User screen displays. |  |
| 3 | Enter User | On the Change View “Active Import of Service Entry sheets for Specific Users” screen,Choose New Entries.User : <User ID>You can use the Search Help to find the User ID for User ID alias is Purchaser.Choose Enter. | User is added |  |
| 4 | Save Data | Choose Save. | A User is saved. |  |

Result

The Activate Import of Service Entry Sheets for Specific Users is saved.

#### Configure Flexible Workflow for Supplier Invoice

##### Activate Flexible Workflow for Supplier Invoice

Purpose

In this procedure, you activate flexible workflow for supplier invoice.

If you want to use the flexible workflow to approve the supplier invoice, you have to process the step: Activate Flexible Workflow for Supplier Invoice.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version . | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Supplier Invoice, on the screen of Configure Ypur Solution - Incoming Invoice, choose Configure on the right of configuration steps with name Activate Flexible Workflow for Supplier Invoices. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen is displayed. |  |
| 5 | Active Flexible Workflow for Supplier Invoices | Select checkbox of the following items :Payment Block: Flexible Workflow is Active,Select checkbox Release Completed Invoice: Flexible Workflow is ActiveSelect checkbox Check Authorizations for Flexible Workflow Steps (Optional)Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Flexible Workflow for Supplier Invoice.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Activate Flexible Workflow for Supplier Invoices": Detail screen displays. |  |
| 3 | Active Flexible Workflow for Supplier Invoices | Select checkbox Payment Block: Flexible Workflow is Active,Select checkbox Release Completed Invoice: Flexible Workflow is ActiveSelect checkbox Check Authorizations for Flexible Workflow Steps (Optional)Choose Save.Note You may be asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue. |  |  |

Result

The Scenario based workflow is activated for Supplier Invoices.

##### Check Workflow for Supplier Invoice

Purpose

In this procedure, you make sure Workflow for Supplier Invoice is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Supplier Invoices (F2873). | The Manage Workflows screen is displayed. |  |
| 3 | Check Workflow for Parked Invoice as Complete | In Workflows dropdown list, choose Workflow for Parked Invoice as Complete, make sure workflow Release completed invoice is in active status. If not, select it and choose Activate.Note Choose the line and go to the Workflow Details screen. Go to the Step Sequence tab, and check the column Recipients in Step Sequence defines the user who handles invoice in the particular step, for example Creator of Purchase Order, cost center responsible or profit center responsible. If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. | The Workflow Item is activated. |  |
| 4 | Check Workflow for Blocked Invoice | In Workflows dropdown list, choose Workflow for Blocked Invoice, make sure workflow Release blocked Invoice by Accounting Responsibles is in active status. If not, select it and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note For the Workflow and Step names, you can translate them to other languages, for example from English to German via the Workflow Content Translation app. |

##### Update Cost Center for User Responsible

Purpose

In this procedure, you configure your release conditions for Service Entry Sheets Approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Cost Centers - Old Version (F1443A) app. | The app is displayed. |  |
| 3 | Filter Cost Center | Make the following entry: Cost Center: <Cost Center>, for example, 33101501Choose Go and select the cost center in the search results. Then choose Edit. | The Cost Center Detail Information screen is displayed. |  |
| 4 | Input User Responsible | In the General Information section, make the following entries:User Responsible: Select from the F4 help. For example, search the user ID for the purchasing_manager: CB9XXXXXXXXX Purchasing Manager. The user with Purchasing Manager role.Person Responsible: For example Purchasing_Manager |  |  |
| 5 | Save Data | Choose Save. | The cost center is saved. |  |

##### Update Profit Center for User Responsible

Purpose

In this procedure, you configure your release conditions for invoice approval.

|  |
| --- |
| Note If you want to run the step [Option B : Create Supplier Invoice with PO/GR relation – Save As Completed (Optional)](#unique_19) [page ] 76 and precondition Account assignment category Profit Center is used in workflow, you have to assign a User Responsible to the Profit Center. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Divisional Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Profit Centers - Old Version (F3516). | The Manage Profit Centers screen is displayed. |  |
| 3 | Filter Profit Center | Profit Center: for example, < YB600>Choose Go, select profit center in search results, then choose Edit. | Profit center detail information screen is displayed. |  |
| 4 | Input User Responsible | In General Information tab, make the following entries:User Responsible: Select from F4. For example: search User ID for purchasing manager CB9980000120 Purchasing Manager.Person Responsible : For example Purchasing_Manager |  |  |
| 5 | Save Data | Choose Save. | Profit center is saved. |  |

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

#### Configure for Employee Self Services Procurement

|  |
| --- |
| Note If you want to perform the step [Employee Self Services Procurement](#unique_22) [page ] 115, you have to run the following configuration. |

##### Maintain the Default Setting for Users

Purpose

The default setting for an employee should be maintained by the Configuration Expert mandatorily.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Default Settings for Users - Purchase Requisitions (F1995). | The Default Settings for Users screen is displayed. |  |
| 3 | Enter the User ID | On the Default Settings for Users screen.User ID: <User ID>Note You can use the Search Help to find the User ID for User Name EmployeeProcurement.Choose Enter. |  |  |
| 4 | Edit the Default Setting for User | On the Default Settings for Users screen, choose EditMake the following entries:Plant: 3310Company Code: 3310Currency: AEDSource Determination: <Selected>Purchasing Doc. Type : NBChoose Save. | Default Settings are set for users. |  |

##### Activate Flexible Workflow for Purchase Requisition

###### Check Flexible Workflow for Purchase Requisition Approval

Purpose

In this procedure, you activate flexible workflow for purchase requisition approval.

If you want to use the flexible workflow to approve the purchase requisition by employee_procurement and order Type NBS, you have to process the following steps: [Check Flexible Workflow for Purchase Requisition Approval](#unique_24) [page ] 26 and [Configure Flexible Workflow for Purchase Requisition (Optional)](#unique_25) [page ] 28.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Active Flexible Workflow | Search Activate Flexible Workflow for Purchase Requisitions , choose configuration with name Requirements processing from search result, then choose Configure on the right of configuration steps with name Activate Flexible Workflow for Purchase Requisitions . | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 5 | Activate Flexible Workflow for PR Approval | Check if the following entry selected for NBS: scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NBS. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Activate Flexible Workflow for Purchase Requisitions .Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase Requisitions Change screen is displayed. |  |
| 3 | Activate Flexible Workflow for PR Approval | Check if the following entry selected for NBS: scenario based workflow: X | The Flexible workflow is active for Purchase Requisitions with Document Type: NBS. |  |

###### Configure Flexible Workflow for Purchase Requisition (Optional)

Purpose

In this procedure, you configure your release conditions for Purchase Requisition Approval.

SAP Note [2485779](https://me.sap.com/notes/2485779) - Configure Workflow using SAP Fiori in S/4HANA provides information on how to use the workflow framework in purchase requisition. Any question regarding this SAP note, please raise ticket to component MM-FIO-PUR-REQ-SSP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Fiori launchpad is displayed. |  |
| 2 | Open Manage Workflow for Purchase Requisition | Open Manage Workflows for Purchase Requisitions (F2705)． | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Workflows: Overall release of requisition. Choose Create and make the following entries:Workflow Name: Test Workflow for Purchase RequisitionPreconditions：<Total net amount is equal to or greater than 500 AED value>Go to Steps area, in Workflow Steps area, choose Create and make the following entries:Step Type: Overall release of Purchase RequisitionType: Overall release of Release Purchase Requisition HeaderRecipients: Assignment By: <User>Note If you can’t find User for approval, you need to check if the employee data has been maintained in the chapter [Maintain the Default Setting for Users](#unique_23) [page ] 25 for Users.Select User with Manager_procurement from F4 helpChoose Add.Choose Save. | The Workflow for Purchase Requisition is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |
| 5 | Define Order | Choose Define Order.On the Define Order screen, choose Test Workflow for Purchase Requisition and move the selected workflow one level up. | The priority for workflow is defined. |  |

#### Update Master Data for Automatic Purchase Order Creation from Purchase Requisition

|  |
| --- |
| Note If you want to perform the step [Automatic Purchase Order Creation from Purchase Requisition](#unique_27) [page ] 100, you have to run Master Data update. |

Prerequisite

By default, you have completed the creation of master data, including material master data, vendor master data and Info Record.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |

##### Change Material (Services) Master Data - Purchasing Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing material (Services) master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Change Material (MM02). | The Change Material (Initial Screen) is displayed. |  |
| 3 | Enter Material Basic Data | On the Change Material screen, make the following entries:Material: <Material>, for example, SM0001Choose Select View(s). | The Select View(s) screen is displayed. |  |
| 4 | Choose Views | On the Select View(s) screen, choose Purchasing and Continue. | The Organizational Levels is displayed. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, make the following entry in the Organizational level section:Plant: <Plant>, for example, 3310Choose Continue. | The Change Material XXXXX (Services) is displayed. |  |
| 6 | Select Autom.PO | Autom.PO: <selected> | Autom.PO is selected. |  |
| 7 | Save your data | Choose Save. | The material master data is updated. |  |

Result

The Autom.PO checkbox is selected.

##### Change Supplier Master Data - Purchasing Organization Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for changing supplier master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Business Partner | On the Maintain Business Partner screen, make the following entries.Business Partner: <Supplier>, for example, 33300001Choose Enter. | The Supplier information screen is displayed. And a list with one entry displayed. |  |
| 4 | Change BP Role | Choose Switch Between Display and Change from the list. In the Change in BP role field, choose the following value: FLVN01 Supplier. |  |  |
| 5 | Open Purchasing Organization Data | Choose Purchasing. | The Change Organization: XXXXXXXX, role Supplier screen is displayed. |  |
| 6 | Enter Purchasing Data | Choose Switch Organization.Make the following data and choose Enter:Purch. Organization: <Purchasing Organization>, for example, 3310 |  |  |
| 7 | Select Automatic PO Checkbox | Go the Purchasing Data tab page in the Additional Purchasing Data section, make the following data:Automatic Purchase Order: <selected> | The Automatic PO checkbox is selected. |  |
| 8 | Save Data | Choose Save. | The Supplier change is saved. |  |

##### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating source list.

|  |
| --- |
| Note If you have more than one suppliers, choose one fixed supplier in the source list. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Source Lists (F1859). | The Manage Source Lists screen is displayed. |  |
| 3 | Create Source List | Choose Create. | The Source List screen is displayed. |  |
| 4 | Enter General Information | Go to General Information area, make the following entries:Material: <Material>, for example, SM0001Plant: <Plant>, for example, 3310Choose Generate in Source lists area. |  |  |
| 5 | Search Sources for Material and Plant | On the Generated Sources screen, make the following entries:Valid From: <Correct Date>Valid To: <12/31/9999>Choose Go, | The Sources are displayed. |  |
| 6 | Choose Sources | Go to Sources (X) area.Choose these lines of items.Choose Add to Existing or Replace Existing.If you have warning message, choose OK. |  |  |
| 7 | Choose Fixed Source | Go to Supplier 33300001 and make the following entry:Status: Fixed Status (Fixed) | The Supplier has been assigned to Fixed Supplier. |  |
| 8 | Save Data | Choose Create. | The Source List is created. |  |

#### Item Hierarchies and Model Product Specification

##### Activate Item Hierarchies in Purchasing

Purpose

In this procedure, you activate item hierarchies in purchasing.

You can use item hierarchies in purchasing documents to structure and sort items, such as materials or services, in a hierarchy.

In this step, you can activate the item hierarchy function for purchase contracts, central purchase contracts, purchase requisitions, purchase orders and model product specifications.

Note that this activation controls the availability of app Manage Model Product Specifications (F5079). If turned on, Manage Model Product Specifications (F5079) app will be available including the item hierarchy function. If turned off, the app is unavailable.

|  |
| --- |
| Caution In a standard system, this configuration step is switched off by default. Once the switch is on, you cannot turn it off. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country or region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Configuration | Search Activate Item Hierarchies in Purchasing, choose the line from search result, then choose Configure on the right of configuration step Activate Item Hierarchies in Purchasing. | The Display/Change Switch State of Lightweight Business Function is displayed. |  |
| 5 | Activate Item Hierarchies in Purchasing | Choose Change State.Choose Back. | Business function switch state is changed successfully. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Activate Item Hierarchies in Purchasing.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display/Change Switch State of Lightweight Business Function screen is displayed. |  |
| 3 | Activate Item Hierarchies in Purchasing | Choose Change State.Choose Back. | Business function switch state is changed successfully. |  |

Result

The business function switch state is changed successfully.

##### Manage Model Product Specifications (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides instructions for creating model product specification.

A structured set of related services and materials that can be used as a template for procurement processes/ documents. You use model product specifications to group services and materials that are frequently ordered together to complete a particular task.

You can further categorize service and materials within a model product specification by grouping them into item sets. Then you can create contract with item set from the model product specification.

You may also refer to [Migration Object of Model Product Specification](https://help.sap.com/docs/SAP_S4HANA_CLOUD/cc9ecc5f5f6b400a98d10e930324f7ad/caf6bbc51a9842ea92f3c2363e8e24f9.html?state=DRAFT) and detail of application Manage Model Product Specification in [SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/8cbe62b1673d4c848c41dbc1ef62fda4.html?version=2208).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Model Product Specifications (F5079). | The Manage Model Product Specifications screen is displayed. |  |
| 3 | Create Model Product Specification | Choose Create.Tip You may upload model product specification by refering to [Upload Model Product Specification](#unique_33) [page ] 136. |  |  |
| 4 | Enter General Information | Go to section General Information , and make the following entries:Grouping Code: for example, Internal Number Arrangement (INT)Choose Enter.Name: enter your model product specification name. | The Maintain Additional Parameters screen is displayed |  |
| 5 | Create Item Set | In section Items, choose Create > Item Set .On Item line 1, make the entries:Description: <description>Select line 1, choose Create > Service , make the following entries:Plant: for example, 3310Product: for example, SM0001Quantity: <Your quantity>, for example, 20Select line 1, choose Create > Material , and make the following entries:Plant: for example, 3310Product: for example, TG11Quantity: XXSelect line 1, choose Create > Service , and make the following entries:Plant: for example, 3310Item Description: for example, ServiceMaterial Group: for example, YBMM01Quantity: XX, for example, 100Unit: for example, HYou may create less than 5 level of item hierarchy, the fifth level has to be functional item, such as service or material. You may insert, copy, delete items too. | In section Model Product Specifications Items, hierarchy number showed for the Item Set line. |  |
| 6 | Save Your Data | Choose Create. | Your model product specification is created. |  |
| 7 | Active MPS and Create Purchase Contract | Choose Activate.Choose Create Purchaser Contract(at the upper right corner). Select items from MPS and choose Add. Or:Choose Back, to manage model product specification screenSelect your MPS, and choose Create Purchaser Contract.On Purchaser Contract screen, make the following entries:Under section General Information ,Basic Data:Purchase Contract Name: for example, MPS contractContract Type: for example, Qty Contract-PSE(CMK)Supplier: for example, 33300001, and choose Enter.Organization:Purchasing Organization: for example, 3310Purchasing Group: for example, 001Valid From: <Today>Valid To: <Today+3 months>Further Information:Currency: AEDCompany Code: 3310 | Your model product specification is activated.Note For more information about contract, please refer to scope item BMD - Purchase Contract. |  |
| 8 | Edit Contract Items | On Items area, expand node for item setSelect item 2 for service material SM0001, choose Details, make the following entries in Purchase Contract Itemsscreen:Item Category: StandardAccount Assignment Category: KPlant:3310On the Quantity and Price tab:Net Order Price: for example, 20 AEDPrice Unit : 1 HOn the GR / IR Control tab:Goods Receipt: YesInvoice Receipt: YesGR-Based Invoice Verification: YesOn the Account Assignment tab:Choose the line and go to Account Assignment screen, make the following entry, then choose Apply.Cost Center: 33101501(G/L account will be automatically determined)On Purchase Contract Item screen, choose Apply.Select item 3 for material TG11, choose Details, make the following entries in Purchase Contract Items screen:Item Category: StandardAccount Assignment Category: KPlant: 3310Storage Location: BlankOn the Quantity and Price tab:Net Order Price: for example, 13 AEDPrice Unit : 1 pcOn the GR/ IR Control tab:Goods Receipt: YesInvoice Receipt: YesGR-Based Invoice Verification: YesOn the Account Assignment tab:Choose the line and go to Account Assignment screen, make the following entry, then choose Apply.Cost Center: 33101501(G/L account will be determined automatically)On Purchase Contract Item screen, choose Apply.Select the item 4 for servie item Service, choose Details, make the following entries in Purchase Contract Items screen:Item Category: StandardAccount Assignment Category: KPlant: 3310On the Quantity and Price tab:Net Order Price: for example, 100 AEDPrice Unit : 1 HOn the GR / IR Control tab:Goods Receipt: YesInvoice Receipt: YesGR-Based Invoice Verification: YesOn the Account Assignment tab:Choose the line and go to Account Assignment screen, make the following entry, then choose Apply.Cost Center: 33101501(G/L account will be determined automatically)On Purchase Contract Item screen, and choose Apply. |  |  |
| 9 | Save the Contract | Choose Create. | Your purchase contract is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below：

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Standard Procurement of Service

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Option A: Create Purchase Requisition](#unique_35) [page ] 43 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Purchase Requisition is created. |
| [Option A: Convert Purchase Requisition to Purchase Order](#unique_36) [page ] 49 | Purchaser | Process Purchase Requisitions (F1048A) | The Purchase Requisition is converted to Purchase Order. |
| [Option B: Create Purchase Order](#unique_37) [page ] 52 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for external services is created. |
| [Option C: Create Purchasing Contract](#unique_38) [page ] 58 | Purchaser | Manage Purchase Contracts (F1600A) | The purchase contract is created. |
| [Option C: Create Purchase Order](#unique_39) [page ] 60 | Purchaser | Manage Purchase Orders (F0842A) | Your purchase order is created. |
| [Option D: Create Contract with Item Hierarchy](#unique_40) [page ] 61 | Purchaser | Manage Purchase Contracts (F1600A) | The purchase contract is created. |
| [Option D: Create Purchase Order with Item Hierarchy from Contract](#unique_41) [page ] 64 | Purchaser | Manage Purchase Contracts (F1600A) | Your purchase order is created. |
| [Change Purchase Order](#unique_42) [page ] 65 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for external services is changed. |
| [Approve Purchase Order (Optional)](#unique_43) [page ] 66 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase order is approved. |
| [Check Purchase Order Approval Details (Optional)](#unique_44) [page ] 67 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order approval status is displayed. |
| [Preview Purchase Order (Optional)](#unique_45) [page ] 68 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed. |
| [Maintain Service Entry Sheet with Flexible Workflow](#unique_46) [page ] 69 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The Service Entry Sheet is created. |
| [Approve Service Entry Sheet with Flexible Workflow](#unique_47) [page ] 72 | Project Manager - Professional Services | My Inbox - All Items (F0862) | The Service Entry Sheet is posted. |
| [Create Supplier Invoice](#unique_48) [page ] 74 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is created. |
| [Release Blocked Supplier Invoice (Optional)](#unique_49) [page ] 81 | Purchasing Manager | My Inbox - All Items (F0862) | Blocked invoice is released. |

Table 3: Multiple Account Assignment for Procurement of Services

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Option A: Create Purchase Requisition](#unique_50) [page ] 82 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Purchase Requisition is created. |
| [Option A: Convert Purchase Requisition to Purchase Order](#unique_51) [page ] 85 | Purchaser | Process Purchase Requisitions (F1048A) | The Purchase Requisition is converted to Purchase Order. |
| [Option B: Create Purchase Order](#unique_52) [page ] 86 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for external services is created. |
| [Change Purchase Order](#unique_53) [page ] 89 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order for external services is changed. |
| [Approve Purchase Order (Optional)](#unique_43) [page ] 66 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Order is approved. |
| [Check Purchase Order Approval Details (Optional)](#unique_54) [page ] 91 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order approval status is displayed. |
| [Preview Purchase Order (Optional)](#unique_45) [page ] 68 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed. |
| [Maintain Service Entry Sheet with Flexible Workflow](#unique_55) [page ] 93 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The Service Entry Sheet is created. |
| [Approve Service Entry Sheet with Flexible Workflow](#unique_56) [page ] 96 | Project Manager - Professional Services | My Inbox - All Items (F0862) | The Service Entry Sheet is posted. |
| [Create Supplier Invoice](#unique_57) [page ] 98 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | Invoice is created. |
| [Release Blocked Supplier Invoice (Optional)](#unique_58) [page ] 100 | Purchasing Manager | My Inbox - All Items (F0862) | Blocked invoice is released. |

Table 4: Automatic Purchase Order Creation from Purchase Requisition

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_59) [page ] 100 | Purchaser | Manage Purchase Requisitions - Professional (F2229) | The Purchase Requisition is created. |
| [Automatic Creation of POs for Service Materials](#unique_60) [page ] 102 | Purchaser | Schedule Purchasing Jobs - Advanced (F1702) | Execute Job Schedule for PR create automatic PO. |
| [Change Purchase Order](#unique_61) [page ] 104 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed. |
| [Approve Purchase Order (Optional)](#unique_62) [page ] 105 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Order is approved. |
| [Check Purchase Order Approval Details(Optional)](#unique_63) [page ] 106 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order approval status is displayed. |
| [Preview Purchase Order (Optional)](#unique_45) [page ] 68 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed. |
| [Maintain Service Entry Sheet with Flexible Workflow](#unique_64) [page ] 107 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The Service Entry Sheet is created. |
| [Approve Service Entry Sheet with Flexible Workflow](#unique_65) [page ] 111 | Project Manager - Professional Services | My Inbox - All Items (F0862) | The Service Entry Sheet is posted. |
| [Check Service Entry Sheet Details(Optional)](#unique_66) [page ] 73 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet details are checked. |
| [Create Supplier Invoice](#unique_67) [page ] 113 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is created. |

Table 5: Employee Self Services Procurement

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Requisition](#unique_68) [page ] 115 | Employee - Procurement | Create Purchase Requisition - Deprecated (F1643) | The Purchase Requisition is created. |
| [Approve Purchase Requisition (Optional)](#unique_69) [page ] 116 | Manager - Procurement | My Inbox - All Items (F0862) | Purchase Requisition is approved. |
| [Convert Purchase Requisition to Purchase Order](#unique_70) [page ] 117 | Purchaser | Process Purchase Requisitions (F1048A) | Purchase Requisition is converted to Purchase Order. |
| [Change Purchase Order (Optional)](#unique_71) [page ] 118 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is edited. |
| [Approve Purchase Order (Optional)](#unique_72) [page ] 119 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Order is approved. |
| [Check Purchase Order Approval Details(Optional)](#unique_73) [page ] 120 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order approval status is displayed. |
| [Preview Purchase Order (Optional)](#unique_45) [page ] 68 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is previewed. |
| [Maintain Service Entry Sheet with Flexible Workflow](#unique_74) [page ] 122 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | The Service Entry Sheet is created. |
| [Approve Service Entry Sheet with Flexible Workflow](#unique_75) [page ] 124 | Project Manager - Professional Services | My Inbox - All Items (F0862) | The Service Entry Sheet is posted. |
| [Check Service Entry Sheet Details(Optional)](#unique_66) [page ] 73 | Purchaser | Manage Service Entry Sheets - Lean Services (F2027) | Service Entry Sheet details are checked. |
| [Create Supplier Invoice](#unique_76) [page ] 126 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Standard Procurement of Service

#### Option A: Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create purchase requisitions manually.

Prerequisite

For case 4, if you want to create purchase requisition with item hierarchy, [Activate Item Hierarchies in Purchasing](#unique_31) [page ] 33 in preliminary step needs to be executed to activate item hierarchy.

|  |
| --- |
| Caution After you switch to hierarchy view, you will not be able to change it back unless all items are deleted. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | On the screen, make the following entries:Go to the General Information area:Document Type: Pur. Requisition |  |  |
| 5 | Case 1: Purchase Service without Material Number | In the Items area, choose Create and choose Service. Make the following entries for each itemOn the Purchase Requisition Item screen.Go to the General Information area:Item Description: Purchase service without material numberPlant: 3310Acct Assignment Category: KNote Purchase RequisitionAccount Assignment Category P for account assignments to projects is also supported. In case budget availability control for a project is active you may run into warning / error messages along the requisition process in case budget thresholds are exceeded. For further details on the budget availability control for projects you can refer to 1NT - Project Control – Finance test script (component responsible: PPM-CNT).Material Group: YBMM01Service Performer: <employee user who is responsible for service performer> (Optional)Go to the Quantity and Date area:Quantity: <Quantity>, for example, 10Start Date: <Today>End Date: <Year-end>Requisition Date: <Today>Planned Delivery Time (in Days): for example, 90Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 10Price Unit: <Price Unit>, for example, 1Unit of Measure: <Unit of Measure>, for example, HPO Price Type : <PO Price Type>, for example, As net priceGo to Account Assignment area:Make the following entries: G/L Account: for example, 65100000 for material group YBMM01. The G/L Account will be determined automatically.Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Note If Account Assignment Category is P, enter your created WBS in test script 1NT - Project Control – Finance and 35F - Project Control – Capital Projects. For further support or issue reporting, you can create an incident under PPM-CNT component.WBS Element: <WBS Element>Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen. |  |  |
| 6 | Case 2: Purchase Service with Material Number | In the Items area, choose Create and choose Service. Make the following entries for each item:On the Purchase Requisition Item screen.Go to the General Information area:Material: SM0001Plant: 3310Acct Assignment Category: KGo to the Quantity and Date area:Quantity: <Quantity> for example, 20Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 20Price Unit: <Price Unit>, for example, 1Go to Account Assignment area:Make the following entries: G/L Account: for example, 51600000 for materials with a material number, The G/L account will be determined automatically.Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen. |  |  |
| 7 | Case 3: Purchase Service with Limits Item | In the Limit Items area, choose Create and choose Service. Make the following entries for each item:On the Purchase Requisition Limit item screen.Go to the General Information area:Item Description: <Item Description>, for example, Service ProcurementPlant: 3310Acct Assignment Category: KMaterial Group: YBMM01Expected Value: 200Overall Limit: 400Contract for Limits(optional): enter the contract number (A purchase requisition limit item can be optionally created with reference to a contract. The contract can be a a flat item contract or can contain item hierarchies (for example the contract created in [Manage Model Product Specifications (Optional)](#unique_32) [page ] 34. In case of contract with Item hierarchies, you can add item from contract when you create SES. Please refer to [Maintain Service Entry Sheet with Flexible Workflow](#unique_46) [page ] 69).Go to the Requisition Period area:Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen. |  |  |
| 8 | Case 4: Purchase Service and Material with Item Hierarchy | In Items area, switch to Hierarchy List view by choosing Hierarchy List button on the right.Choose Create, choose Item Set, and make the following entries:Item Description: for example, service item hierarchy level 1Select item set you just created and choose Create, choose Service. Item 20 will be created. And then make the following entries:On the Purchase Requisition Item screen, go to the General Information area:Plant: 3310Acct Assignment Category: Cost center(K)Material: for example, SM0001Go to Quantity and Date area:Quantity: <Quantity>， for example, 20Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 20 AED per 1HPO Price Type: As net pricePrice Unit: <Price Unit>, for example, 1Go to Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen.Select the item 10, choose Create, choose MaterialItem 30 will be created and you can make the following entries:On the Purchase Requisition Item screen.Go to the General Information area:Plant: 3310Acct Assignment Category: Cost center(K)Material: for example, TG11Go to Quantity and Date area:Quantity: <Quantity> for example, 5Start Date: Delivery DateRequisition Date: <today>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 300 AED per 1PCPrice Unit: <Price Unit>, for example, 1Go to Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen.Select the item 10, choose Create, choose Service.Item 40 will be created and you can make the following entries:On the Purchase Requisition Item screen.Go to the General Information area:Plant: 3310Acct Assignment Category: Cost center(K)Item description: for example, ServiceMaterial Group: for example, YBMM01Go to the Quantity and Date area:Quantity: <Quantity> for example, 50Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 100 AED per HPO Price Type: As net pricePrice Unit: <Price Unit>, for example, 1Unit of Measure: HGo to Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen.You may create up to 5 levels of item hierarchy, the fifth level has to be a functional item, such as service or material. |  |  |
| 9 | Save Purchase Requisition | Choose Create.Ignore warning Enter a service performer and choose Create. | The purchase Requisition is created. |  |

Result

The purchase requisition is created.

#### Option A: Convert Purchase Requisition to Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Case 1, 2 and 3: Convert Purchase Requisition without Item Hierarchy to Purchase Order

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions screen displays the purchase requisition list. |  |
| 3 | Filter Item List | Enter the purchase requisitions number in the Search area, then choose Go.Note Purchase requisition can also be generated from scope item 4RF - Project Control – Resourcing and Procurement. And if you encounter any account assignment P related issues, you can create an incident under PPM-CNT component. | The Purchase Requisition list is filtered to show result. |  |
| 4 | Assign Source of Supply | On the Process Purchase Requisitions screen, go to Purchase Requisitions (X) area. | The Purchaser Orders Preview is displayed. |  |
|  | Case 1: Purchase Service without Material Number | Go to the line of the purchase requisition item.Choose Show More per Rowl. (Right side of Create Contract if this button is not displayed. )Choose Assign Source of Supply, then choose Supplier tab, enter the following search criteria:Supplier: 33300001Purchasing Organization: 3310Choose Go.Select the item with your supplier and choose Assign.Message Purchase requisition updated successfully. pops up. Choose OK. |  |  |
|  | Case 2: Purchase Service with Material Number | Go to the line of the purchase requisitions item.Choose Assign Source of Supply.Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed.On Assign Source of Supply screen, under tab Info Record, choose the item with supplier 33300001 . Choose Assign.Message Purchase requisition updated successfully. pops up. Choose OK. |  |  |
|  | Case 3: Purchase Service with Limits Item | Go to the line of the purchase requisitions item.Choose Assign Source of Supply.Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed.On Assign Source of Supply screen, choose Supplier tab, and enter the following search criteria:Supplier: 33300001Purchasing Organization: 3310Choose Go, select the item with your supplier and choose Assign.Message Purchase requisition updated successfully. pops up. Choose OK. |  |  |
| 5 | Convert Purchase Requisition to Purchase Order | Select the line item that needs to convert to PO and choose Create Purchase Order. | The Process Purchase Requisitions screen displays. |  |
| 6 | Save Purchase Order | On the Purchase Order screen, make the following entry, then choose Order.Purchase Order Type: Standard PO | Standard PO created under the number 45xxxxxxxx. |  |

Case 4: Purchase Service and Material with Item Hierarchy

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions screen displays the purchase requisition list. |  |
| 3 | Filter Item List | Enter the Purchase Requisitions number in the Search are, then choose Go. | The Purchase Requisition list is filtered to show result. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition with Item Number of Purchase Requisition 20. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | If the Purchase Requisition has been assigned a source, then you don't have to assign source again for this step. If the Purchase Requisition hasn't been assigned a source, choose Assign Source of Supply, and then choose Info Record tab.Select the Source with your supplier and choose Assign.Message Purchase Requisition Updated Successfully pops up.Choose OK. | The assignment of one source to the requisition is done. |  |
| 6 | Assign Source for each item | Repeat step 4-5 for each item. | The assignment of one source maintained for each item. |  |
| 7 | Prepare the Purchaser Order | Select the Item Set (Item Number of Purchase Requisition 10) and choose Create Purchase Order.Note Item set is selected, subitems are already selected. | The Purchase Order Preview screen is displayed. |  |
| 8 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchase Order Type: Standard POSupplier: 10300001Currency:Purchasing Group: 001Purchasing Organization: 1010Choose Order. | The Purchase Order is created. |  |
| 9 | Maintain Purchase Order Item | Select item with material SM0001, then choose Details.On the Purchase Order Item screen, choose tab Process Flow and make the following entry:Goods-Receipt-Based Invoice Verification: Selected.Then choose Apply.Repeat above step for the item with Short Text Service. |  |  |
| 10 | Back to Process Purchase Requisition | Click Back to go to Process Purchase Requisitions (F1048A) | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changes to PO created. |  |

#### Option B: Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific service requirement from supplier by creating a purchase order.

Prerequisite

For case 4, if you want to create purchase requisition with item hierarchy, [Activate Item Hierarchies in Purchasing](#unique_31) [page ] 33 in preliminary step needs to be executed to activate item hierarchy.

|  |
| --- |
| Caution After you switch to hierarchy view, you will not be able to change it back unless all items are deleted. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Order | Choose Create．On the Purchase Order screen, make the following entries: screen displays.In the Basic Data area:Supplier: 33300001Currency: AEDPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Note If you want the purchase order to be assigned to an approver, then total PO amount should be higher than 500 AED for purchasing groups 003;You can choose one of the cases below. |  |  |
| Case 1: Purchase Service without Material Number | In the Items area, choose CreateMake the following entries for each item::Short Text: <Service Procurement>Material Group: YBMM01Plant: 3310Order Quantity: <Order Quantity> for example, 10 HNet Order Price: <Net Order Price>, for example, 10Choose the item and go to the Purchase Order Item screen.Go to the General Information area:Product Type Group: ServiceAcct Assignment Cat.: Cost centerGo to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Go to the Tax area:Tax Code: <Input Tax Code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply, then go back to Purchase order screen. |  |  |  |
|  | Case 2: Purchase Service with Material Number | In the Items area, choose Create and make the following entries for each item:Material: SM0001Plant: 3310Order Quantity: <Order Quantity> ,for example, 20 HChoose select the item and go to the Purchase order Item screen. Go to the General Information area:Acct Assignment Cat.: Cost centerNet Order Price: <Net Order Price> for example, 20Go to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Go to the Tax area:Tax Code: <Input Tax Code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply, then go back to Purchase order screen. |  |  |
|  | Case 3: Purchase Service with Limits Item | In the Limit Items area, choose Create and make the following entries for each item:Short Text: for example, <Service Procurement>Expected Value: 200Overall Limit: 400Acct Assignment Cat.: Cost center (K)Product Type Group: Service (2)Plant: 3310Choose the item and go to the Purchase Order Limit Item screen.Go to the General Information area:Material Group: YBMM01Go to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Go to the Tax area:Tax Code: <Input Tax Code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply, then back to Purchase order screen. |  |  |
|  | Case 4: Purchase Service and Material with Item Hierarchy | In Items area, switch to Hierarchy List view by choosing Hierarchy List button on the right.Choose Create, choose Item Set, and make the following entries:For Hierarchy Number 1/Item 10 :Short Text: For example, Item Hierachy level 1Select the item 10 and choose Create, choose Service. Item 20 will be created. Choose Details at the right side of item 20, make the following entries:Go to the General Information area:Material: for example, SM0001, and then choose EnterPlant: 3310Order Quantity: <Quantity> for example, 20 HNet Order Price: for example, 20AEDper 1HPrice Unit: 1HItem Category: StandardAccount Assignment Category: Cost center(K)Go to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Invoice Receipt: <Selected>Go to the Tax area:Tax Code: <your tax code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose the line and go to Purchase Order Item Account Assignment screen, make the following entry,Cost Center: 33101501Choose Apply, then back to New Purchase Order screen.Select the item 10, choose Create, choose MaterialItem 30 will be created and choose Details, you can make the following entries:On the Purchase Order Item screen.Go to the General Information area:Material: for example, TG11， choose Enter.Plant: 3310Order Quantity: <Quantity> for example, 10 PCNet Order Price: for example, 15 AED per 1PCItem Category: StandardAccount Assignment Category: Cost center(K)Go to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Invoice Receipt: <Selected>Go to the Delivery Details area:Storage Location: <Blank>Go to the Tax area:Tax Code: <your tax code>Go to Supplier Confirmation Control area,Confirmation Control: <Blank>Go to the Account Assignment area:Choose the line and go to Purchase Order Item Account Assignment screen, make the following entry,Cost Center: 33101501Choose Apply, then back to New Purchase orderscreen.Select the item 10, choose Create, choose ServiceItem 40 will be created and you can make the following entries:Go to the General Information area:Short Text: for example, ServicePlant: 3310Order quantity: <Quantity> for example, 5 HMaterial Group: for example, YBMM01Net Order Price: for example, 30AED per 1 HPrice Unit: 1 HItem Category: Standard,Account Assignment Category: Cost center(K)Go to Process Flow area:Goods Receipt: <Selected>Goods-Receipt Based Invoice Verification: <Selected>Invoice Receipt: <Selected>Go to the Tax area:Tax Code: <your tax code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose the line and go to Purchase Order Item Account Assignment screen, make the following entry,Cost Center: 33101501Choose Apply, then go back to New Purchase Orderscreen.You may create less than 5 level of item hierarchy, the fifth level has to be functional item, such as service or material. |  |  |
| 4 | Check Purchase Order for Completeness | On the Purchase Order screen, choose Message.If the system displays an error message, please correct the purchase order;If no error message appears, the purchase order can be submitted. |  |  |
| 5 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Option C: Create Purchasing Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create contract with free text.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Contracts (F1600A) | Manage Purchase Contracts screen is displayed. |  |
| 3 | Create Contract | Choose Create to create contract. | Purchase Contract screen is displayed. |  |
| 4 | Enter Contract Information | Make the following entries and Choose Create:On the Header Information tab:Contract Type: for example, CMKPurchasing Group: 001Supplier : 33300001Purchasing Organization: 3310On the General Information tab:Target Value: 500 AEDCompany Code: 3310Valid From: Start date of the contract, for example, TodayValid To: End date of the contract, for example, Today+30On Delivery and Payment Terms Tab:Payment Terms: for example, 0001On the Items Tab:Choose Create to create contract items, choose the line and go to next screen.Item Category: StandardAccount Assignment Category: KProduct Type Group: ServiceMaterial Description: Service ContractPlant: 3310Material Group: YBMM01On the Quantity and Price tab:Net Order Price: 10AEDPrice Unit : 1 HTarget Quantity: 50 HOn the GR / IR Control tab:Goods Receipt: selectInvoice Receipt: selectGR-Based Invoice Verification: selectOn the Account Assignment tab:Cost Center: 33101501Choose Apply, then choose Create on the main screen. | The purchase contract is created. |  |

#### Option C: Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create purchase order with limit items and then assign the contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create to create purchase order. | New Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Information | Make the following entries and Choose Save:On the General Information tab:Supplier: 33300001. Press Enter.Currency: AEDPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310On the Limit Items Tab:Choose Create to create purchase order itermsShort Text: for example, Service Contract POPlant: 3310Expected Value: 50AEDOverall Limit : 200.00AEDAcct Assignment Cat.:Cost Center (K)Product Type Group : Service (2)Plant： 3310Material Group： YBMM01Choose the limit items row for more details on tabs of Process Flow, Source of Supply, Tax and Account Assignment.Goods receipt : YesGoods-Receipt Based Invoice Verification :YesInvoice receipt: YesContract for Limit: Contract number created in previous steps.Tax Code: <Input Tax Code>Cost Center: 33101501Choose Apply and Order. | The purchase order is created. |  |

#### Option D: Create Contract with Item Hierarchy

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create contract with item hierarchy .

Prerequisite

You need to execute [Activate Item Hierarchies in Purchasing](#unique_31) [page ] 33 in preliminary step to activate item hierarchy.

|  |
| --- |
| Caution After you switch to hierarchy view, you will not be able to change it back unless all items are deleted. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Contracts (F1600A). | Manage Purchase Contracts screen is displayed. |  |
| 3 | Create Contract | Choose Create to create contract. | Purchase Contract screen is displayed. |  |
| 4 | Enter Contract Information | Make the following entries and choose Enter:On the Header Information tab:Contract Type : MKPurchasing Organization: 3310Supplier: 33300001On the General Information tab:Valid From: Start date of the contract, for example, TodayValid To: End date of the contract, for example, Today+30Purchasing Group: 001Target Value: 5000 AEDOn Delivery and Payment Terms Tab:Payment Terms: for example, 0001 | The purchase contract is created. |  |
| 5 | Enter Contract Item Details | In the Items tab, choose Hierarchy List button on the right.Choose Create, choose Item Set, and make the following entries:Item : 10Short Text: For example, Test HierarchySelect the item 10 (Hierarchy Number 1) and choose Create then choose Service. Item 20 will be created. Choose Details, make the following entries in Purchase Contract Item screen:Item Category: StandardAccount Assignment Category: KMaterial: for example, SM0001Plant: 3310On the Quantity and Price tab:Net Order Price: 20 AEDPrice Unit : 1 HTarget Quantity: 50 HOn the GR / IR Control tab:Goods Receipt: SelectedInvoice Receipt: SelectedGR-Based Invoice Verification: SelectedOn the Account Assignment tab:Choose the line and go to Account Assignment screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply twice.Select the item 10, choose Create, choose Material.Item 30 will be created, choose Details and you can make the following entries:Item Category: StandardAccount Assignment Category: KMaterial: for example, TG11Plant: 3310On the Quantity and Price tab:Net Order Price: for example, 13 AEDPrice Unit : 1 PCTarget Quantity: 50 PCOn the GR / IR Control tab:Goods Receipt: SelectedInvoice Receipt: SelectedGR-Based Invoice Verification: SelectedOn the Account Assignment tab:Choose the line and go to Account Assignment screen, make the following entry, then choose Apply.Cost Center: 33101501On Purchase Contract Item screen, Choose Apply. | The Purchase Contract created |  |
| 6 | Create Contract | Choose Create on the main screen to create contract. | Your contract is created. |  |

#### Option D: Create Purchase Order with Item Hierarchy from Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create purchase order with item hierarchy from contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Contracts (F1600A). | Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Select the contract created previously, choose Create Purchase Order.Go to Hierarchy Items area, choose Details for each service item, and make following entry:Order Quantity: Your order quantityUnder Tax tab, enter:Tax Code: <your tax code>For item of material TG11:Choose Details, and make following entry:Order Quantity : Your order quantityUnder Tax tab, enter:Tax Code: <your tax code>Go to Supplier Confirmations Control area:Confirmation Control: remove the valueOtherwise, you are not able to create service entry sheet for this item.Choose Apply.Choose Order. | Your purchase order is created. |  |

#### Change Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Search for Purchase Order | Enter your purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the purchase order you want to change, then go to Purchase Order screen.Choose Edit. | The Purchase Order screen displays.The purchase order is opened in change mode. |  |
| 5 | Change Purchase Order | Change certain field values of the purchase order.If you will maintain service entry sheet later on for the purchase order, it is necessary to set the indicators as Yes for Goods Receipt and Goods-Receipt-Based Invoice Verification on the Process Flow tab of the PO itemNote If you don’t need to maintain service entry sheet in the process, please make these two indicators blank, and skip service entry sheet related step [Maintain Service Entry Sheet with Flexible Workflow](#unique_46) [page ] 69 and [Approve Service Entry Sheet with Flexible Workflow](#unique_47) [page ] 72.For material items, such as material TG11, if you want to include this item in service entry sheet, you need to go to item details, and make sure the following fields are blank:Storage Location: <blank>Go to Supplier Confirmations Control area:Confirmation Control: <blank>For each item, go to Tax tab to check if tax code is correct, if not, please update it.For service, Tax code: <your tax code> .For material: Tax Code: <your tax code>.For service，go to Schedule Lines area of Purchase Order Item, check End of Performance Period, make change if necessary. | The purchase order values are changed. |  |
| 6 | Check Purchase Order for Completeness | On the Purchase order screen, choose the Mesage.If the system displays an error message, please correct the purchase order;If no error message occurs, the Purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchasing Manager releases a purchase order.

A prerequisite is the existence of a purchase order that can be released. Purchasing group is 003 and all purchase orders with a total value of 500 AED or more require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approve Reason | Enter approve reason if necessary, and then choose Submit. | The purchase order is approved. |  |

#### Check Purchase Order Approval Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing purchase order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Preview the Purchase Order | Go to the Output Management tab.In the Output Management (X) area, choose Display for a item..Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed. | The Purchase Order is opened in PDF format. |  |

#### Maintain Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you report the performed services in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Enter Field Values | Choose Create.On the Service Entry Sheet screen, make the following entries, then choose Enter:Name of Service Entry Sheet : <SES Name> , for example, ConsultingReference Purchase Order : <Purchase order you created>Select items you needed in Add Purchase Order Items and click Add.Note For purchase order with item hierarchy, you may select hierarchy item to include all functional items under this hierarchy, or expand node to select functional item per your need. |  |  |
| Option ACase 1: Purchase service without material numberCase 2: Purchase service with material number | Select the item line, make the following entries and choose Apply:Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example,10 |  |  |  |
| Option BCase 3: Purchase service with Limits item | Without Contract for Limit in Purchase OrderIn the Items area, make the following entries and choose Apply:Option 1:Product: <Blank>Option 2:Product: <Product>, for example, SM0001Note If you enter value for Product:The Product should be a service material.The material group of the product should be the same as purchase order limit items (product type group 2).Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example,10 HPrice Per Unit: 10Net Order Price: xxAEDPrice Unit: HWith Contract for Limit in Purchase OrderIn Items area, go to Item Details, and make the following entries under Source of Supply tab:Purchase Contract Item: press F4 to search your value, select the item and choose Enter.Under General Information tab:Performance Period: <Today>-<Today>Stated Quantity: <Stated Quantity>, for example,10 HOptionally, you may add item from purchase contract:Choose Add, then choose Item from Purchase Contract.Select items you needed on the pop-up window Add Purchase Contract Items and click Add.Note If you selected the item set as the reference contract item in purchase order, you may see the item hierarchy under this item set, you may choose child item, then choose AddMake the following entries for each item:Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity>, for example, 5 |  |  |  |
|  | Case 4: Purchase Service and Material with Item Hierarchy | In the Items area, make the following entries for each service item:Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example, 5For material items like material TG11, make following entries:Performance Period: delivery date is set as default date, you may change itStated Quantity: <Stated Quantity , for example, 5 |  |  |
|  | Add Attachments in the Service Entry Sheet (Optional) | You can upload files using the Upload or Add a Link to the service entry sheet and view the existing attachments.on the header level(go to tab Attachments) andon the item level(go to tab Items, open the details and go to tab Attachments).If no longer required you can delete the attachments.You can view the attachments and save them on your own device regardless of the status of the service entry sheet.But you can add and delete attachments only if you edit the service entry sheet.That means that the service entry sheet must be in status In Process. |  |  |
| 4 | Save the Service Entry Sheet | Choose Create.If there is any warning message pops up, update the service entry sheet according to the warning message or ignore them by choosing Create. | Service Entry Sheet is saved. |  |
| 5 | Send to Approval | Choose Send for Approval. | Service Entry Sheet is sent for approval. |  |
| 6 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen.Search for Service Entry Sheet created above.Check the status.If the status is Approved, please skip the step [Approve Service Entry Sheet with Flexible Workflow](#unique_47) [page ] 72.Note If the Total net amount of this service entry sheet smaller than the value set in step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 . The system will automatically release of Service Entry Sheet. | Check the Service Entry Sheet status. |  |

#### Approve Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the service entry sheet is approved by the company. When this is done, the vendor can send an invoice for the approved amount to the service provider.

These flexible workflows have been configured in Preliminary Step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 using the tile Manage Workflows for Service Entry Sheets.

|  |
| --- |
| NoteThe ordered amount will be converted using system exchange rate to the workflow currency. Then it will be compared with workflow condition.If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to the business role of the user. This is necessary in order to enable the user to process incoming approval requests in regards to the workflow for the service entry sheet. |

Table 6:

| Cases | Triggering conditions | Workflow sequence | Business role |
| --- | --- | --- | --- |
| Automatic Release of Service Entry Sheet | Total net amount of service entry sheet is smaller than or equal to 1000 AED. | Automatically by system | N/A |
| Release of Service Entry Sheet (multi-step approval) | Total net amount of service entry sheet is greater than 1000 AED. |  | Purchaser |
| Project Manager - Professional Services | Project Manager - Professional Services |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the role used in the above table. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Check Service Entry Sheet Status | A list of already created Service Entry Sheets is displayed.Search your created Service Entry Sheet with In Approval Status. | The List of Service Entry Sheets screen is displayed. |  |
| 4 | Approve or Reject Service Entry Sheet | On the Service Entry Sheet screen and confirm you created Service Entry Sheet XXXXX.Optional： Go to the Attachment section to check if the attachment is uploaded when the SES is created.Choose Release or choose Reject.On the Submit Decision screen, add note if necessary and choose Submit. | Service Entry Sheet is approved or rejected. |  |

#### Check Service Entry Sheet Details(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing Service Entry Sheet's approval and business process flow details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | Enter the Service Entry Sheet number in the Search area, then choose Go. |  |  |
| 4 | Choose Service Entry Sheet | Choose the row of the Service Entry Sheet you want to preview. | The Service Entry Sheet screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The Service Entry Sheet’s approval details are displayed. |  |
| 6 | Check Process Flow | Go to details of each item, and go to Process Flow area, then check the process flow information. | The Service Entry Sheet's process flow details are displayed. |  |

#### Create Supplier Invoice

In this activity, you create the supplier invoice with PO/GR relation. You have the below options to create the supplier invoice:

|  |
| --- |
| Note Follow below procedure to create an individual invoice. If need to mass upload supplier invoice, please refer to scope item Accounts Payable(J60) |

| Option | Option Name | Context |
| --- | --- | --- |
| Option A | [Option A: Create Supplier Invoice with PO/GR Relation](#unique_79) [page ] 74 | This function is used for direct posting of supplier invoice. |
| Option B | [Option B : Create Supplier Invoice with PO/GR relation – Save As Completed (Optional)](#unique_19) [page ] 76 | The supplier invoice is a legal document if you need it checked by defined set of approvers before posting. |

##### Option A: Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The supplier sends an invoice for the service delivered.

This invoice must be booked against the purchase order and verified with the entry sheet.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Now if you move the mouse to the Invoicing Party in the header of the supplier invoice, then click the Invoicing Party, the Company Data with Address and Contact Details are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the New Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : InvoiceCompany Code : 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number>Invoicing Party: for example, 33300001 |  |  |
| 4 | Enter Purchase Order Reference | Choose one of the below options to enter reference:Option 1:Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase Order you created>Choose Enter. |  |  |
| Option 2:Go to the Purchasing Document References area:Reference Document Category :Service Entry Sheet - Lean ServicesService Entry Sheet: <Service Entry Sheet you created>Note You can choose Assignment Options to select Multiple SES items.Choose Assignment Options. Then on the Assignment Options screen, you can select multiple Service Entry Sheets from the value help.Choose Enter. |  |  |  |  |
| 5 | Check Invoice Items | Go to Invoice Items, and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO > |  |  |
| 6 | Enter Gross Invoice Amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 8 | Post Invoice | Choose Post. | The system message is displayed. |  |

##### Option B : Create Supplier Invoice with PO/GR relation – Save As Completed (Optional)

The supplier invoice is a legal document if you need it checked by defined set of approvers before posting.

###### Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The vendor sends an invoice for the service delivered.

This invoice must be booked against the purchase order and verified with the entry sheet.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the New Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : InvoiceCompany Code : 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 4 | Enter Purchase Order Reference | Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase Order you created>Choose Enter. |  |  |
| 5 | Check Invoice Items | Go to Invoice Items/Standard, and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO> |  |  |
| 6 | Enter Gross Invoice Amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 8 | Post Invoice | Choose Messages.Note Please note whether the system have the message Price too high (tolerance limit of XXX exceeded)which will impact the following steps.Release Completed Supplier Invoice (Optional).Choose Save as Completed.Note You can choose Park to park the invoice first. After that, you can edit the created supplier invoice to choose Save as Completed. | The system message is displayed. |  |

###### Release Completed Supplier Invoice

Purpose

In this activity, if the system displays message Price too high (tolerance limit of XXX exceeded) when you run Save As Completed, please choose Option A, otherwise choose Option B.

|  |
| --- |
| Note Only choose either option A or B. |

Once the blocked supplier invoice is released, you could check details on the Approval Details tab of the corresponding supplier invoice via the Supplier Invoices List app.

Table 7: Option A

| No. | Workflow Sequence | Business Role |
| --- | --- | --- |
| 1 | Release by Purchaser | PurchaserNote If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. |
| 2 | Release by Cost Center Responsible | Approver is set in preliminary step [Update Cost Center for User Responsible](#unique_17) [page ] 23. |
| 3 | Release by Profit Center Responsible | Approver is set in preliminary step [Update Profit Center for User Responsible](#unique_18) [page ] 23. |

Table 8: Option B

| No. | Workflow sequence | Business Role |
| --- | --- | --- |
| 1 | Release by Cost Center Responsible | Approver is set in preliminary step [Update Cost Center for User Responsible](#unique_17) [page ] 23. |
| 2 | Release by Profit Center Responsible | Approver is set in preliminary step [Update Profit Center for User Responsible](#unique_18) [page ] 23. |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as approver set in [Release Completed Supplier Invoice](#unique_81) [page ] 78 | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F0862).Note If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Reject Supplier Invoice | On the Release of Completed Invoice XXXXXXXX screen, choose Reject at the bottom of the screen.On the Submit Decision screen, add note if necessary and choose Submit. | Task successfully processed. |  |

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
| 1 | Log On | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Search and Select for Supplier Invoice | Search for supplier invoice created above. Enter rejected Supplier invoice number into Invoice Document No and then choose Go. Select the invoice. | The Supplier Invoice is displayed. |  |
| 5 | Edit Supplier Invoice | Choose Edit to update invoice, for example Reference or correct Gross Invoice Amount.Then choose Save as Completed at the bottom of the screen. | Supplier Invoice is updated and saved as completed again. |  |

###### Release Completed Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If Save as Completed is chosen in the previous step, then the supplier invoice needs to be checked and posted.

Once the blocked supplier invoice is released, you could check details on the Approval Details tab of the corresponding supplier invoice via the Supplier Invoices List app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as approver set in [Release Completed Supplier Invoice](#unique_81) [page ] 78 | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862).Note If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_MM_BC_INV_WIAPPROVE_PC and SAP_MM_BC_INV_DOC_DSP_PC to the business role of the user. This action is also required for other invoice workflow. | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Approve Supplier Invoice | On the Release Completed Invoice XXXXXXXX screen, choose Release.On the Submit Decision screen, add note if necessary and choose Submit. | Task successfully processed. |  |

#### Release Blocked Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This step is to release the blocked supplier invoice. Once the blocked supplier invoice is released, you can check the details on the Approval Details tab of the corresponding supplier invoice via the Supplier Invoices List (F1060A) app.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log on to the SAP Fiori launchpad as approver set in preliminary step.Note The approver is set in preliminary step [Update Cost Center for User Responsible](#unique_17) [page ] 23. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862) | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for the supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Approve Supplier Invoice | On the Release Blocked Invoice XXXXXXXX screen, choose Release.On the Submit Decision screen, add note if necessary and choose Submit. | Task is successfully processed. |  |

### Multiple Account Assignment for Procurement of Services

#### Option A: Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisition can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | On the New Purchase Requisition screen, make the following entries:Go to the General Information area:Document Type: Pur. Requisition | The Purchase Requisition screen is displayed. |  |
|  | Case 1: Purchase Service with Single Account Assignment | In the Items area, choose Create and choose Service. Make the following entries for each item:On the Purchase Requisition Item screen.Go to the General Information area:Item Description: Purchase service without material numberMaterial: SM0001Plant: 3310Acct Assignment Category: KMaterial Group: YBMM01Choose Enter, then make the following entries:Distribut. Indicator: Single Account AssignmentGo to the Quantity and Date area:Quantity: <Quantity> for example, 10Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 10Price Unit: <Price Unit>, for example, 1Unit of Measure: <Unit of Measure>, for example, HGoods Receipt is Expected: <selected>Invoice Receipt is Expected: <selected>Go to Account Assignment area.Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen. |  |  |
|  | Case 2: Purchase Service with Multi-Account Assignment | In the Items area, choose Create and choose Service. Make the following entries for each item:On the Purchase Requisition Item screen.Go to the General Information area:Material: SM0001Plant: 3310Acct Assignment Category: KChoose Enter, then make the following entries:Distribut. Indicator: Distribution by percentageGo to the Quantity and Date area:Quantity: <Quantity> for example, 20Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 20Price Unit: <Price Unit>, for example, 1Goods Receipt is Expected: <selected>Invoice Receipt is Expected: <selected>Go to Account Assignment area: Choose Create.In the line of Assgnt No 1:Cost Center: 33101501Distribution (%):70In the line of Assgnt No 2:Cost Center: 33101601Distribution (%):30Go to Contact Information area:Purchasing Organization: 3310Purchasing Group: 001Choose Apply, then go back to Purchase Requisition screen. |  |  |
| 5 | Save Purchase Requisition | Choose Create.Ignore warning Enter a service performerChoose Create. | The purchase requisition is created. |  |

Result

The purchase requisition is created.

#### Option A: Convert Purchase Requisition to Purchase Order

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions screen displays the Purchase Requisition list. |  |
| 3 | Filter Item List | On the Process Purchase Requisitions screen, enter the purchase requisitions number in the Search area, then choose Go. | The Purchase Requisition list is filtered to show result. |  |
| 4 | Assign Source of Supply | On the Purchase Requisitions (X) area, select the purchase requisition item line.On the purchase requisition item area, choose Assign Source of Supply.Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed.On Assign Source of Supply screen, for item with material number, select the info record then choose Assign.For item without material number, on the Supplier tab, enter the following search criteria:Supplier: 33300001Purchasing Organization: 3310Choose Go, select the item with your supplier and choose Assign.Message Purchase requisition updated successfully. pops up. Choose OK. |  |  |
| 5 | Convert Purchase Requisition to Purchase Order | Select the line item that needs to convert to PO and choose Create Purchase Order. | The Manage Purchase Requisitions screen displays. |  |
| 6 | Save Purchase Order | On the Purchase Order screen, make the following entries, then choose Order.Purchase Order Type: Standard PONote If you want to purchase order to be assigned to an approver, then total PO amount higher than 500 AED for Purchasing Groups 003. | Standard PO created under the number 45xxxxxxxx. |  |

#### Option B: Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific requirement for a service from the vendor by creating a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen displays. |  |
| 3 | Create Purchase Order | Choose Create．On the Purchase order screen, make the following entries:In the General Information area:Supplier: 33300001Currency: AEDPurchasing Group: 001Purchasing Organization: 3310Company Code: 3310Note If you want the purchase order to be assigned to an approver, then the total PO amount should be higher than 500 AED for purchasing groups 003;You can choose one of the cases below. |  |  |
|  | Case 1: Purchase Service with Single Account Assignment | In the Items area, choose Create and make the following entries:Short Text: for example, <Service Procurement>Material Group: YBMM01Material: SM0001Plant: 3310Order Quantity: <Order Quantity> ,for example, 10 HNet Order Price: <Net Order Price> for example, 10Choose the item and go to the Purchase Order Item screen.Go to the General Information area:Acct Assignment Cat.: Cost centerGo to Process Flow area:Goods Receipt: <Selected>Goods-Receipt-Based Invoice Verification: <Selected>Invoice Receipt: <Selected>Go to the Tax area:Tax Code: <Input Tax Code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Cost Center: 33101501Choose Apply.Choose Apply, then back to Purchase order screen. |  |  |
|  | Case 2: Purchase Service with Multi-Account Assignment | In the Items area, choose Create and make the following entries:Material: SM0001Plant: 3310Order Quantity: <Order Quantity> ,for example, 20 HChoose the item and go to the Purchase order Item screen.Go to the General Information area:Acct Assignment Cat.: Cost centerNet Order Price: <Net Order Price> for example, 20Go to Process Control area:Goods Receipt: YesGoods-Receipt-Based Invoice Verification: YesGo to the Tax area:Tax Code: <Input Tax Code>Go to the Schedule Lines area:Start of Performance Period: <Today>End of Performance Period: <Today+30days>Go to the Account Assignment area:Choose Create. The second line displays.In the line of Account Assgnt No 1:Cost Center: 33101501Distribution (%):70In the line of Account Assgnt No 2:Cost Center: 33101601Distribution (%) : 30Choose Apply, then back to Purchase order screen. |  |  |
| 4 | Check Purchase Order Completeness | On the Purchase Order screen, choose Message to check the completeness of the information. |  |  |
| 5 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Change Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to change, then go to Purchase Order screen.Choose Edit. | The Purchase Order screen displays.The Purchase Order is opened in change mode. |  |
| 5 | Change Purchase Order | Change certain field values of the Purchase Order.If you will maintain Service Entry Sheet later on for the purchase order, it is necessary to set the indicators as Yes of Goods Receipt and Goods-Receipt-Based Invoice Verification on the Process Flow tab of the PO item | The Purchase Order values are changed. |  |
| 6 | Check Purchase Order Completeness | On the Purchase order screen, choose the Messages.If the system displays an error message, please correct the purchase order;If no error message appears, the purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the purchasing manager releases a purchase order.

As a prerequisite, you must have a purchase order that can be released. Purchasing group 003 and all purchase orders with a total value of 500 AED or larger require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

#### Check Purchase Order Approval Details (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing purchase order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter purchase order number in search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check approval information. | The purchase order's approval details are displayed. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Preview the Purchase Order | Go to the Output Management tab.In the Output Management (X) area, choose Display for a item..Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed. | The Purchase Order is opened in PDF format. |  |

#### Maintain Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you report the performed services in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Enter Field Values | Choose Create.On the Service Entry Sheets screen, make the following entries, then choose Enter:Name of Service Entry Sheet: <SES Name> , for example, ConsultingReference Purchase Order : <Purchase order you created>On the popup window Add Purchase Order Item, select items you needed in Add Purchase Order Items and click Add. |  |  |
|  | Case 1: Purchase Service with Single Account Assignment | In the Items area, make the following entries for each item:Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example,10Note If the single account assignment needs to be changed to Multi-accounting in service entry sheet, please run this step.Choose Apply.On the Service Entry Sheet screen, go to the Items area. Choose the line of Items.On the Service Entry Sheet Item screen, go to the General Information area. Choose one of the cases below for different account assignment distribution:Option 1:Account Assignment Distribution: Distribution by percentage.Choose Enter.Go to the Account Assignment area, and choose Create.In the line of Assgnt Assgmt No 1:Distribution (%) : 70Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101601In the line of Assgnt Assgmt No 2:Distribution (%) : 30Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply.Option 2:Account Assignment Distribution: Distrib. on quantity basis.Choose Enter.Go to the Account Assignment area, and choose Create.In the line of Assgnt Assgmt No 1:Quantity : <Quantity>, for example,5Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101601In the line of Assgnt Assgmt No 2:Quantity : <Quantity>, for example,5Choose the line and go to next screen, make the following entry, then choose Apply.Cost Center: 33101501Choose Apply. | The Single Account Assignment changed to Multi-Account Assignment on the Service Entry Sheet item level is updated. |  |
|  | Case 2: Purchase Service with Multi-account Assignment | In the Items area, make the following entries for each item:Performance Period: <Today>-<Today>Stated Quantity: <Stated Quantity>, for example, 10Note If the Multi-account assignment distribution needs to be updated in Service Entry Sheet, please run this step.On the Service Entry Sheet screen, go to the Items area. Choose the line of Items.On the Service Entry Sheet Item screen, go to the General Information area. Choose one of the cases below for different account assignment distribution:Option 1:Account Assignment Distribution: Distribution by percentage.Choose Enter.Go to the Account Assignment area:In the Distribution (%) column, update the distribution percentage value based on business requirement.Choose Apply.Option 2:Account Assignment Distribution: Distrib. on quantity basis.Choose Enter.Go to the Account Assignment area:In the Quantity column, update the Quantity value based on business requirement.Choose Apply. | The Account Assignment Distribution on the Service Entry Sheet item level is updated. |  |
|  | Add Attachments in Service Entry Sheet (Optional) | You can upload files using the Upload or Add a Link to the service entry sheet and view the existing attachments.on the header level(go to tab Attachments) andon the item level(go to tab Items, open the details and go to tab Attachments).If no longer required you can delete the attachments.You can view the attachments and save them on your own device regardless of the status of the service entry sheet.But you can add and delete attachments only if you edit the service entry sheet.That means that the service entry sheet must be in status In Process. |  |  |
| 5 | Save Service Entry Sheet | Choose Create. | Service Entry Sheet is saved. |  |
| 6 | Send to Approval | Choose Sent for Approval. | Service Entry Sheet is sent for approval. |  |
| 7 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen.Search for Service Entry Sheet created above.Check the status.If the status is Approved, please skip the step [Approve Service Entry Sheet with Flexible Workflow](#unique_56) [page ] 96.Note If the Total net amount of this service entry sheet smaller than the value set in step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 . The system will automatically release of Service Entry Sheet. | Check the Service Entry Sheet status. |  |

#### Approve Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the service entry sheet is approved by the company. When this is done, the vendor can send an invoice for the approved amount to the service provider.

These flexible workflows have been configured in Preliminary Step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 using the tile Manage Workflows for Service Entry Sheets.

|  |
| --- |
| NoteThe ordered amount will be converted using system exchange rate to the workflow currency. Then it will be compared with workflow condition.If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to the business role of the user. This is necessary in order to enable the user to process incoming approval requests in regards to the workflow for the service entry sheet. |

Table 9:

| Cases | Triggering conditions | Workflow sequence | Business role |
| --- | --- | --- | --- |
| Automatic Release of Service Entry Sheet | Total net amount of service entry sheet is smaller than or equal to 1000 AED. | Automatically by system | N/A |
| Release of Service Entry Sheet (multi-step approval) | Total net amount of service entry sheet is greater than 1000 AED. | 1st Creator of Purchase Order | Purchaser |
| 2nd Project Manager - Professional Services | Project Manager - Professional Services |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the role used in the above table. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Check Service Entry Sheet Status | A list of already created Service Entry Sheets is displayed.Search your created Service Entry Sheet with In Approval Status. | The List of Service Entry Sheets screen is displayed. |  |
| 4 | Approve or Reject Service Entry Sheet | On the Service Entry Sheet screen and confirm you created Service Entry Sheet XXXXX.Optional： Go to the Attachment section to check if the attachment is uploaded when the SES is created.Choose Release or choose Reject.On the Submit Decision screen, add note if necessary and choose Submit. | Service Entry Sheet is approved or rejected. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The vendor sends an invoice for the service delivered.

This invoice must be booked against the purchase order and verified with the entry sheet.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the NEW Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction: InvoiceCompany Code: 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 4 | Enter Purchase Order Reference | Choose one of the below options to enter reference:Option 1:Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase Order you created>Choose Enter. |  |  |
| Option 2:Go to the Purchasing Document References area:Reference Document Category :Service Entry Sheet - Lean ServicesService Entry Sheet: <Service Entry Sheet you created>Note You can choose Assignment Options to select Multiple SES items.Choose Assignment Options. Then on the Assignment Options screen, you can select multiple Service Entry Sheets from the value help.Choose Enter. |  |  |  |  |
| 5 | Check Invoice Items | Go to Invoice Items/Standard, and check the Amount, Quantity and Tax Code.Tax Code: <same with tax code in PO >You can choose invoice item to display multiple account assignment detail on the next screen. |  |  |
| 6 | Enter Gross Invoice Amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 8 | Post Invoice | Choose Post. | The system message is displayed. |  |

#### Release Blocked Supplier Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This step is to release the blocked supplier invoice. Once the blocked supplier invoice is released, you could check details on the Approval Details tab of the corresponding supplier invoice via app Supplier Invoices List.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as approver set in preliminary step.Note Approver is set in preliminary step [Update Cost Center for User Responsible](#unique_17) [page ] 23. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Check Supplier Invoice Status | Search for supplier invoice created above. | The List of Supplier Invoice is displayed. |  |
| 4 | Approve Supplier Invoice | On the Release Blocked Invoice XXXXXXXX screen, choose Release.On the Submit Decision screen, add note if necessary and choose Submit. | Task is successfully processed. |  |

### Automatic Purchase Order Creation from Purchase Requisition

#### Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Purchase Requisition can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Requisitions - Professional (F2229). | The Manage Purchase Requisitions – Professional screen is displayed. |  |
| 3 | Create Purchase Requisition | Choose Create. | The Purchase Requisition screen is displayed. |  |
| 4 | Enter Purchase Requisition Data | On the Purchase Requisition screen, make the following entries:Go to the General Information area:Document Type: Pur. RequisitionAutomatic Source Determination: <selected> | The Purchase Requisition screen is displayed. |  |
| 5 | Purchase Service with Material Number | In the Items area, choose Create and Service. Make the following entries:On the Purchase Requisition Item screen:Go to the General Information area:Material: <Material>, for Example, SM0001Plant: <Plant>, for example, 3310Acct Assignment Category: KGo to the Quantity and Date area:Quantity: <Quantity>, for example, 20Start Date: <Today>End Date: <Today + 3 months>Release Date: <Today>Go to Valuation area:Valuation Price: <Valuation Price>, for example, 20Price Unit: <Price Unit>, for example, 1Goods Receipt is Expected: <selected>Invoice Receipt is Expected: <selected>Go to Account Assignment area:Choose the line and go to the next screen. Make the following entries and choose Apply.Cost Center: <Cost Center>, for example, 33101501Go to Contact Information area:Purchasing Organization: <Purchasing Organization>, for example, 3310Purchasing Group: <Purchasing Group>, for example, 001Go to Source of Supply area and confirm one of sources has been assigned.If no source is assigned, choose Assign Source of Supply on Select Source of Supply screen, select one source from Proposed SoS or other tabs.Choose Apply, then go back to Purchase Requisition screen. |  |  |
| 6 | Create Purchase Requisition | Choose Create.Ignore warning Enter a service performerChoose Create. | The purchase requisition is created. |  |

Result

The Purchase Requisition is created.

#### Automatic Creation of POs for Service Materials

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
| 1 | Save Purchase Requisition | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Purchasing Jobs - Advanced (F1702). | The Application Jobs screen is displayed |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Define a Job | On the New Job screen, make the following entries:In 1.Template Selection area:Job Template: <Job Template>, for example, Automatic Creation of Purchase Orders from RequisitionsJob Name: <Job Name>, for example, Automatic Creation of Purchase Orders from RequisitionsChoose Step 2, in 2. Scheduling Options area, make the following entries:Start Immediately : <selected>Start <Current Time>Note If the job needs to be run on a regular basis, choose Define Recurrence Pattern.Choose Step 3, make the following entries in Parameter Section area:Per Requisition:<selected>Per Company Code: <selected>Note Set Parameter settings according to your needs.Choose Schedule. | The job is created. |  |
| 5 | Convert Purchase Requisition to Purchase Order | On the Application Jobs screen.Go to Jobs (X) area and check the status until it changes to Finished. | The Job automatically converts Purchase Requisition to Purchase Order. |  |
| 6 | Check Result | Choose Navigate to the job results. | The Purchase Order is created. |  |

#### Change Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen displays. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to change, then go to Purchase Order screen.Choose Edit. | The Purchase Order screen displays.The Purchase Order is opened in change mode. |  |
| 5 | Change Purchase Order | Change certain field values of the Purchase Order.If you will maintain Service Entry Sheet later on for the purchase order, it is necessary to set the indicators as Yes of Goods Receipt and Goods-Receipt-Based Invoice Verification on the Process Flow tab of the PO item | The Purchase Order values are changed. |  |
| 6 | Check Purchase Order Completeness | On the Purchase order screen, choose the Output Management.If the system displays an error message, please correct the purchase order;If no error message occurs, the Purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchasing Manager releases a purchase order.

A prerequisite is the existence of a purchase order that can be released. Purchasing group is 003 and all purchase orders with a total value of 500 AED or more require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approve Reason | Enter approve reason if necessary, and then choose Submit. | The purchase order is approved. |  |

#### Check Purchase Order Approval Details(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing purchase order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Preview the Purchase Order | Go to the Output Management tab.In the Output Management (X) area, choose Display for a item..Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed. | The Purchase Order is opened in PDF format. |  |

#### Maintain Service Entry Sheet with Flexible Workflow

Purpose

In this activity, you report the performed services in the service entry sheet.

You have two options when you maintain service entry sheets. You can either manually maintain them or import them by uploading excels.

##### Option A: Maintain Service Entry Sheet Manually

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
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Enter Field Values | Choose Create.On the Service Entry Sheets screen, make the following entries, then choose Enter:Name of Service Entry Sheet : <SES Name> , for example, Vincent SunReference Purchase Order : <Purchase order you created>In the Items area, make the following entries for each item:Performance Date: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example,10 |  |  |
| 4 | Add Attachments in Service Entry Sheet (Optional) | You can upload files using the Upload or Add a Link to the service entry sheet and view the existing attachments.on the header level(go to tab Attachments) andon the item level(go to tab Items, open the details and go to tab Attachments).If no longer required you can delete the attachments.You can view the attachments and save them on your own device regardless of the status of the service entry sheet.But you can add and delete attachments only if you edit the service entry sheet.That means that the service entry sheet must be in status In Process. |  |  |
| 5 | Save the Service Entry Sheet | Choose Create. | Service Entry Sheet is saved. |  |
| 6 | Send to Approval | Choose Send to Approval. | Service Entry Sheet is sent for approval. |  |
| 7 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen.Search for Service Entry Sheet created above.Check the status.If the status is Approved, please skip the step [Approve Service Entry Sheet with Flexible Workflow](#unique_47) [page ] 72.Note If the Total net amount of this service entry sheet smaller than the value set in step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 . The system will automatically release of Service Entry Sheet. | Check the Service Entry Sheet status. |  |

##### Option B: Import Service Entry Sheets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the authorized users can import service entry sheets from Microsoft Excel files.

|  |
| --- |
| Note As an authorized user, you can import service entry sheets from Microsoft Excel files using the app Manage Service Entry Sheets - Lean Services. For more information about the authorization of users, see the section in Preliminary Step[Configure Import Service Entry Sheets for Specific Users (Optional)](#unique_14) [page ] 18. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Choose Upload | Choose Import. |  |  |
| 4 | Download Template | On the Upload of Service Entry Sheets screen:Choose Download Template.If a dialog box appears, choose OK.Save Service Entry Sheet Upload template to the local machine.Note You can refer to the SAP Note [2249454](https://me.sap.com/notes/2249454) to know more about the list downloaded. | Excel Template download and consistency |  |
| 5 | Fill in Data on Excel Template | Open the file and input data according to instruction on the file.NoteOn the first tab of the template, you find an instruction on how to fill in the Excel file. Please note the following requirements:The language of the selected template and the logon language to the SAP system must be the same.You’re not allowed to change the naming or order of the sheets and columns of the template.A field name followed by an asterisk (*) is a mandatory field.A field name followed by two asterisks (**) is a conditionally required field.The number in brackets behind each field name indicates the maximum number of characters you can enter for the field.Date fields use the date format specified in the cell format settings of your MS Excel program.You can import up to 100 service entry sheet items. This means, for example, 100 service entry sheets with one item or one service entry sheet with a maximum of 100 items. |  |  |
| 6 | Select the File to upload | Choose Search Help to select the file you want to upload.If a dialog box appears, choose OK.In the dialog box, select the file you want to upload from your local computer. Choose Open. |  |  |
| 7 | Option A: Upload Excel in Foreground | Run In Background:<blank>Choose Import. Log Objects are displayed on the next screen. On the Display Log screen, check the application log.Log Object was created with message success. |  |  |
| 8 | Option B: Upload Excel Run in Background | Run In Background: <selected>Choose Import.If you need to monitor the background job status, you need to follow the steps below. |  |  |
| Open Monitor Service Entry Sheet Generation Log (F3495)Data From-To: <Today>Category:MMPUR_SESSubcategory:UPLOADChoose Go. |  |  |  |  |
| 9 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen, search for the Service Entry Sheet created above.Check the status. |  |  |

#### Approve Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the service entry sheet is approved by the company. When this is done, the vendor can send an invoice for the approved amount to the service provider.

These flexible workflows have been configured in Preliminary Step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 using the tile Manage Workflows for Service Entry Sheets.

|  |
| --- |
| NoteThe ordered amount will be converted using system exchange rate to the workflow currency. Then it will be compared with workflow condition.If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to the business role of the user. This is necessary in order to enable the user to process incoming approval requests in regards to the workflow for the service entry sheet. |

Table 10:

| Cases | Triggering conditions | Workflow sequence | Business role |
| --- | --- | --- | --- |
| Automatic Release of Service Entry Sheet | Total net amount of service entry sheet is smaller than or equal to 1000 AED. | Automatically by system | N/A |
| Release of Service Entry Sheet (multi-step approval) | Total net amount of service entry sheet is greater than 1000 AED. | 1st Creator of Purchase Order | Purchaser |
| 2nd Project Manager - Professional Services | Project Manager - Professional Services |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the role used in the above table. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Check Service Entry Sheet Status | A list of already created Service Entry Sheets is displayed.Search your created Service Entry Sheet with In Approval Status. | The List of Service Entry Sheets screen is displayed. |  |
| 4 | Approve or Reject Service Entry Sheet | On the Service Entry Sheet screen and confirm you created Service Entry Sheet XXXXX.Optional： Go to the Attachment section to check if the attachment is uploaded when the SES is created.Choose Release or choose Reject.On the Submit Decision screen, add note if necessary and choose Submit. | Service Entry Sheet is approved or rejected. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The vendor sends an invoice for the service delivered.

This invoice must be booked against the purchase order and verified with the entry sheet.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # |  | Instruction | Expected Result | Pass / Fail / Comment |
| 1 | Log on | Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : InvoiceCompany Code : 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 4 | Enter Purchase order Reference | Choose one of the below options to enter reference:Option 1:Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase Order you created>Choose Enter. |  |  |
| Option 2:Go to the Purchasing Document References area:Reference Document Category :Service Entry Sheet - Lean ServicesService Entry Sheet: <Service Entry Sheet you created>Note You can choose Assignment Options to select Multiple SES items.Choose Assignment Options. Then on the Assignment Options screen, you can select multiple Service Entry Sheets from the value help.Choose Enter. |  |  |  |  |
| 5 | Check Invoice items | Go to Invoice Items/Standard, and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO > |  |  |
| 6 | Enter Gross Invoice amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 8 | Post Invoice | Choose Post. | The system message is displayed. |  |

#### Check Service Entry Sheet Details(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing Service Entry Sheet's approval and business process flow details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | Enter the Service Entry Sheet number in the Search area, then choose Go. |  |  |
| 4 | Choose Service Entry Sheet | Choose the row of the Service Entry Sheet you want to preview. | The Service Entry Sheet screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The Service Entry Sheet’s approval details are displayed. |  |
| 6 | Check Process Flow | Go to details of each item, and go to Process Flow area, then check the process flow information. | The Service Entry Sheet's process flow details are displayed. |  |

### Employee Self Services Procurement

#### Create Purchase Requisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Employee creates shopping cart for service procurement.

Procedure

Refer to the step Create Purchase Requisition with Cost Center in the 18J Requisitioning scope item, with only adjustments to the following fields:

- Short Text: Service Procurement
- Material Group: YBMM01
- Product Type Group: Service

#### Approve Purchase Requisition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase requisition. If the total amount of PR is more than 500 AED and order type is NBS, then it should be approved. PR release amount is configured in AED in [Configure Flexible Workflow for Purchase Requisition (Optional)](#unique_25) [page ] 28 and will be converted to the country currency amount for purchase requisition approval. Order type is configured in [Maintain the Default Setting for Users](#unique_23) [page ] 25 .

If the approval user does not have My Inbox APP, you have to check whether business catalog SAP_CA_BC_MYINBOX has been assigned to the business role of the user.

Procedure

|  |
| --- |
| Note You can ignore this step if you did not perform the Preliminary Step - [Configure Flexible Workflow for Purchase Requisition (Optional)](#unique_25) [page ] 28. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as a Manager - Procurement . | The SAP Fiori launchpad is displayed. |  |
| 2 | Open My Inbox | Open My Inbox - All Items (F0862). | A list of already created Purchase Requisition is displayed. |  |
| 3 | Select Purchase Requisition | Select the Purchase Requisition and choose Approve. | The Submit Decision dialog box is displayed. |  |
| 4 | Enter Release Reason | Enter the approval reason if needed, then choose Submit. | The Purchase Requisition is approved. |  |

#### Convert Purchase Requisition to Purchase Order

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Purchaser role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions screen displays the purchase requisition list. |  |
| 3 | Filter Item List | Enter the purchase requisition number in the Search area, then choose Go.Note Purchase requisition can also be generated from scope item 4RF -Project Control - Procurement. And if you encounter any account assignment P related issues, you can create an incident under PPM-CNT component. | The Purchase Requisition list is filtered to show result. |  |
| 4 | Assign Source of Supply | On the Process Purchase Requisitions screen, go to Purchase Requisitions (X) area, and then choose Show More per Row. | The Purchaser Orders Preview is displayed. |  |
|  |  | Go to each line of the purchase requisitions item.Choose Assign Source of Supply.Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed.On Assign Source of Supply screen, enter the following search criteria:Supplier: 33300001Purchasing Organization: 3310Choose Go, select the item with your supplier and choose Assign.Message Purchase requisition updated successfully. pops up. Choose OK. |  |  |
| 5 | Convert Purchase Requisition to Purchase Order | Select the line item that needs to be converted to PO and choose Create Purchase Order. | The Purchase Order screen is displayed. |  |
| 6 | Save Purchase Order | On the Purchase Order screen, make the following entries and choose Order.Purchase Order Type: Standard POIf you want the purchase order to be assigned to an approver, then total PO amount higher than 500 AED for purchasing groups 003. | Standard PO is created under the number 45xxxxxxxx. |  |

#### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to change, then go to Purchase Order screen.Choose Edit. | The Purchase Order screen displays.The Purchase Order is opened in change mode. |  |
| 5 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 6 | Check Purchase Order Completeness | On the Purchase Order screen, choose the Output Management.If the system displays an error message, please correct the purchase order;If no error message occurs, the Purchase order can be submitted. |  |  |
| 7 | Save Purchase Order | Choose Order. | The purchase order is created. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, the Purchasing Manager releases a purchase order.

A prerequisite is the existence of a purchase order that can be released. Purchasing group is 003 and all purchase orders with a total value of 500 AED or more require an approval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Approve at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit.Note If attachment is uploaded during purchase order creation, in My Inbox App, the attachment can be found under Attachments tab of the purchase order. The attachment will be renamed with prefix 'H_'. | The Purchase Order is approved. |  |

#### Check Purchase Order Approval Details(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing purchase order's approval details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The purchase order's approval details display. |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to preview an existing purchase order form.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchase Orders (F0842A). | The Manage Purchase orders screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase order number in the search area, then choose Go. |  |  |
| 4 | Choose Purchase Order | Choose the row for the Purchase Order you want to preview, then go to Purchase Order screen. | The Purchase Order screen is displayed. |  |
| 5 | Preview the Purchase Order | Go to the Output Management tab.In the Output Management (X) area, choose Display for a item..Note Choose the Show More per Row button on the right side of Create Contract if this button is not displayed. | The Purchase Order is opened in PDF format. |  |

#### Maintain Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you report the performed services in the service entry sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Enter Field Values | Choose Create.On the Service Entry Sheets screen, make the following entries, then choose Enter:Name of Service Entry Sheet : <SES Name> , for example, Vincent SunReference Purchase Order : <Purchase order you created>Select items you needed in Add Purchase Order Items and click Add.In the Items area, make the following entries for each item:Performance Period: <Today>-<Today>Stated Quantity: < Stated Quantity >, for example,10 |  |  |
| 4 | Add Attachments in Service Entry Sheet (Optional) | You can upload files using the Upload or Add a Link to the service entry sheet and view the existing attachments.on the header level(go to tab Attachments) andon the item level(go to tab Items, open the details and go to tab Attachments).If no longer required you can delete the attachments.You can view the attachments and save them on your own device regardless of the status of the service entry sheet.That means that the service entry sheet must be in status In Process. |  |  |
| 5 | Save Service Entry Sheet | Choose Save . | Service Entry Sheet is saved. |  |
| 6 | Send to Approval | Choose Send to Approval. | Service Entry Sheet is sent for approval. |  |
| 7 | Check Service Entry Sheet Status | On the Manage Service Entry Sheets screen.Search for Service Entry Sheet created above.Check the status.If the status is Approved, please skip the step [Approve Service Entry Sheet with Flexible Workflow](#unique_47) [page ] 72.Note If the Total net amount of this service entry sheet smaller than the value set in step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 . The system will automatically release of Service Entry Sheet. | Check the Service Entry Sheet status. |  |

#### Approve Service Entry Sheet with Flexible Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the service entry sheet is approved by the company. When this is done, the vendor can send an invoice for the approved amount to the service provider.

These flexible workflows have been configured in Preliminary Step [Configure Flexible Workflow for Service Entry Sheets](#unique_12) [page ] 17 using the tile Manage Workflows for Service Entry Sheets.

|  |
| --- |
| NoteThe ordered amount will be converted using system exchange rate to the workflow currency. Then it will be compared with workflow condition.If this particular user doesn’t have My Inbox APP, you need to assign business catalog SAP_CA_BC_MYINBOX_PC and SAP_MM_BC_SES_WIAPPROVE_PC to the business role of the user. This is necessary in order to enable the user to process incoming approval requests in regards to the workflow for the service entry sheet. |

Table 11:

| Cases | Triggering conditions | Workflow sequence | Business role |
| --- | --- | --- | --- |
| Automatic Release of Service Entry Sheet | Total net amount of service entry sheet is smaller than or equal to 1000 AED. | Automatically by system | N/A |
| Release of Service Entry Sheet (multi-step approval) | Total net amount of service entry sheet is greater than 1000 AED. | 1st Creator of Purchase Order | Purchaser |
| 2nd Project Manager - Professional Services | Project Manager - Professional Services |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad using the role used in the above table. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - All Items (F0862). | The My Inbox screen is displayed. |  |
| 3 | Check Service Entry Sheet Status | A list of already created Service Entry Sheets is displayed.Search your created Service Entry Sheet with In Approval Status. | The List of Service Entry Sheets screen is displayed. |  |
| 4 | Approve or Reject Service Entry Sheet | On the Service Entry Sheet screen and confirm you created Service Entry Sheet XXXXX.Optional： Go to the Attachment section to check if the attachment is uploaded when the SES is created.Choose Release or choose Reject.On the Submit Decision screen, add note if necessary and choose Submit. | Service Entry Sheet is approved or rejected. |  |

#### Check Service Entry Sheet Details(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to check an existing Service Entry Sheet's approval and business process flow details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Service Entry Sheets - Lean Services (F2027). | The Manage Service Entry Sheets screen is displayed. |  |
| 3 | Search for Service Entry Sheet | Enter the Service Entry Sheet number in the Search area, then choose Go. |  |  |
| 4 | Choose Service Entry Sheet | Choose the row of the Service Entry Sheet you want to preview. | The Service Entry Sheet screen is displayed. |  |
| 5 | Check Approval Details | Go to the Approval Details area and check the approval information. | The Service Entry Sheet’s approval details are displayed. |  |
| 6 | Check Process Flow | Go to details of each item, and go to Process Flow area, then check the process flow information. | The Service Entry Sheet's process flow details are displayed. |  |

#### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The vendor sends an invoice for the service delivered.

This invoice must be booked against the purchase order and verified with the entry sheet.

Additionally, it is possible to insert a note in multiple languages when creating a supplier invoice via app Create Supplier Invoice. The note can be saved when holding, parking, saving, or posting the invoice, and it can be read when displaying the invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori launchpad as an Accounts Payable Accountant | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | On the Create Supplier Invoice screen, make the following entries:Go to the General Information area:Transaction : InvoiceCompany Code : 3310Invoice Date: <Today>Reference: <Fill the supplier Invoice Number> |  |  |
| 4 | Enter Purchasing Document References | Choose one of the below options to enter reference:Option 1:Go to the Purchasing Document References area:Reference Document Category :Purchase Order/Scheduling AgreementPurchase Order/Scheduling Agreement: <Purchase Order you created>Choose Enter. |  |  |
| Option 2:Go to the Purchasing Document References area:Reference Document Category :Service Entry Sheet - Lean ServicesService Entry Sheet: <Service Entry Sheet you created>Note You can choose Assignment Options to select Multiple SES items.Choose Assignment Options. Then on the Assignment Options screen, you can select multiple Service Entry Sheets from the value help.Choose Enter. |  |  |  |  |
| 5 | Check Invoice Items | Go to Invoice Items/Standard, and check the Amount, Quantity and Tax Code.Tax code: <same with tax code in PO > |  |  |
| 6 | Enter Gross Invoice Amount | Go to the General information area:Gross Invoice Amount: <Total amount in PO including Tax> |  |  |
| 7 | Add Notes (Optional) | Enter notes on Note tab if you want to add more detailed long text for the supplier invoice. |  |  |
| 8 | Post Invoice | Choose Post. | The system message is displayed. |  |

## Appendix

### Process Integration

The process to be test in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| <Scope Item ID> - <Scope Item Title> | <Enter business condition.> |

#### Related Processes

The following scope items cover other scenarios related to service procurement. More details can be found in these scope items.

| SI | Link |
| --- | --- |
| 4AZ-Contract Management with SAP Ariba Contracts | Please refer to 4AZ test script in [SAP Best Practice Explorer](https://rapid.sap.com/bp/#/browse/scopeitems/4AZ). |
| 42K-Automation of Source-to-Pay with SAP Business Network | Please refer to 42K test script in [SAP Best Practice Explorer](https://rapid.sap.com/bp/#/browse/scopeitems/42K). |
| 4R2-Service Procurement with SAP Business Network and SAP Fieldglass | Please refer to 4R2 test script in [SAP Best Practice Explorer](https://rapid.sap.com/bp/#/browse/scopeitems/4R2). |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Payable-(J60) |  |
| Real-Time Reporting and Monitoring for Procurement-(1JI) |  |

### Set up Mail Notification for Service Entry Sheet Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can configure the system to notify approvers via email about new work items in their inbox. By default, the approvers are informed by means of notifications in the SAP Fiori launchpad. Sending emails provides them with an additional notification channel. It is possible to send email notifications in the following cases:

- When a service entry sheet is created, the recipients of workflow items are informed about new items in their inbox. In such case, you can refer to the email template SWF_CRT_NOTIFY_RECIPIENTS.
- When a service entry sheet is approved or rejected, the workflow initiator receives an email. In such case, you can refer to the email template SWF_WORKFLOW_COMPLETE_NOTIFY.

|  |
| --- |
| Note You need to ensure that the user ID of the approver and the requester have been maintained the Email address. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Extensibility Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) . | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_CRT_NOTIFY_RECIPIENTS.Note Copy the pre-delivered e-mail template SWF_CRT_NOTIFY_RECIPIENTS into the custom name space. The custom template must follow this pattern: <YY1>_<ScenarioId>_CRT_ALL, or <YY1>_<ScenarioId>_<CRT>_<ACTIVITY_NODEID>Choose email template then choose Copy then make bellow entries:Email Template: _00800321_CRT_ALLName: Workflow for Release of Service Entry SheetChoose Copy. | Email Template copied. |  |
| On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_WORKFLOW_COMPLETE_NOTIFY .Note For the workflow approval, copy the predelivered e-mail template SWF_WORKFLOW_COMPLETE_NOTIFY into your namespace. The custom template must follow this pattern: YY1_<ScenarioId>_COMPLETE_POSITIVEChoose email template then choose Copy then make bellow entries:Email Template: _00800321_COMPLETE_POSITIVEName: Positive Workflow for Release of Service Entry SheetChoose Copy. |  |  |  |  |
| On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_WORKFLOW_COMPLETE_NOTIFY .Note For the workflow rejection, copy the predelivered e-mail template SWF_WORKFLOW_COMPLETE_NOTIFY into your namespace, The custom template must follow this pattern: YY1_<ScenarioId>_COMPLETE_NEGATIVEChoose email template then choose Copy then make bellow entries:Email Template: _00800321_COMPLETE_NEGATIVEName: Negative Workflow for Release of Service Entry SheetChoose Copy. |  |  |  |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example:YY1__00800321_CRT_ALLYY1_00800321_COMPLETE_POSITIVEYY1_00800321_COMPLETE_NEGATIVEGo to the Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save.Note You must not make any changes to the technical names of the following fields:{{TaskName}}{{WorfklowTaskInternalID}} | The Email Template adjusted. |  |

### Set up Mail Notification for Supplier Invoice Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Copy the predelivered email template to the exactly named custom template.

Procedure

|  |
| --- |
| Note Please check email address has already maintained for the approver. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad using the Extensibility Specialist role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) . | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: SWF_CRT_NOTIFY_RECIPIENTS.Choose email template then choose Copy then make bellow entries:Email Template: For example, YY1_00800251_CRT_ALLName: Release of Supplier InvoiceChoose Copy.Note For Release Blocked Invoice workflow, the custom template must follow these naming pattern:YY1_00800251_CRT_10 or YY1_00800251_CRT_ALL(Both work the same way, as there is only one relevant node in the workflow)For Parked Invoice as Complete workflow, the custom template must follow these naming pattern:YY1_00800303_CRT_19 Email is triggered in case of work item to approve invoiceYY1_00800303_CRT_30 Email is triggered in case of work item to rework invoiceYY1_00800303_CRT_ALL Email is triggered in case of work item to approve or rework invoice | Email Template copied. |  |
| 4 | Adjust the text of the mail template | Choose Custom tab.Choose Email template, for example YY1_00800251_CRT_ALL then go to Email Template screen. | Custom Email Template opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template adjusted. |  |

### Set up Mail Notification for Supplier Invoice Workflow with Factory Calendar

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Copy the predelivered email template to the exactly named custom template.

After finishing this step, in app Manage Workflows for Supplier Invoices (F2873), you will be able to add a deadline based on workday(s) in the Deadlilnes section when executing action Mark Step as Overdue or action Send Mail Notification. You can select any Email template created in app Maintain Email Templates - Deprecated (F1306) for action Send Mail Notification.

For more details, please refer to [How to Configure the Flexible Workflow for Supplier Invoices](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/ff92035b3da94a14a3d2d0faffad564c.html).

Procedure

|  |
| --- |
| Note Please check if email address has already been maintained for the approver. |

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fall/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Email Templates - Deprecated (F1306) | The templates displays. |  |
| 3 | Create Email Template | On the Maintain Email Templates screen, choose Predelivered (X), search Template: MRM_WF_DEADLINE.Choose email template then choose Copy then make bellow entries:Email Template: for example, YY1_ MRM_WF_DEADLINEName: Supplier Invoice NotificationChoose Copy. | Email template is copied. |  |
| 4 | Adjust the Text of the Mail Template | Choose Custom tab.Choose Email template, for example YY1_ MRM_WF_DEADLINE then go to Email Template screen. | Custom Email Template is opened. |  |
| 5 | Choose Language | Choose Language, for example English. Then go to Email Template Content screen.You can edit the Body HTML part and Body Plain Text part as your request then choose Save. | The Email Template is adjusted. |  |

### Mass Change of Posting Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this tile, the mass change of posting date is enabled in supplier invoices. You can use Mass Change of Posting Date app or schedule job Mass Change Posting Date in Schedule Supplier Invoice Jobs - Advanced app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open app Mass Change of Posting Date (MRM_MOVE_DATE). | The APP displays. |  |
| 3 | Change the Posting Date | On the Mass Change of Posting Date screen, make the following entries.In section Selection:Current Posting Date: For example, beginning date of last periodTo: For example, ending date of last periodCompany Code: For example, 3310Invoice Doc. Status: For example, AIn section Processing Options:New Posting Date: For example, todayIn section Processing:Choose Display or Change Posting Date. | Entries are made. |  |
| 4 | Execute | Choose Execute in the right corner to execute. | The selected action is executed. |  |

### Upload Model Product Specification

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Model Product Specifications (F5079). | The Manage Model Product Specifications screen is displayed. |  |
| 3 | Download Template | On the Manage Model Product Specifications screen,Choose Import > Download > Template . | Excel template is download. |  |
| 4 | Fill the Excel Template | Open the file and input data on Header and Item tab in the file by following the instructions in Legend sheet.Save the file. |  |  |
| 5 | Select the File to upload | Choose Import > Upload .On the popup screen Upload Spreadsheet for Data Exchange, choose Browse to choose speardsheet to upload.In the dialog box, select the file you want to upload from your local computer.Choose Open | Your file to be uploaded is selected. |  |
| 6 | Upload by Background Job | Choose Upload.On the pop up screen Define Information for Background Processing:Choose Upload.You will get a success message Upload Model Product Specification Information from xxxx.xlsx has been scheduled., and choose View Job. | Your background job is scheduled. |  |
| 7 | View Job Log | On the Application Jobs screen, choose Go to show jobs.Jobs are listed out with status.If your job is finished with error log, click on the red Error to navigate to job log.Check the log details.Update your data file according to the log, upload again.If your job is finished successfully, click on green Success log to check the log details, such as the model product specification numbers created.Choose Back. | Job is finished. |  |
| 8 | Check Model Product Specification | Choose Back to Manage Model Product Specifications screen.Search your model product specifications by name, search term, or ID.Select the model product specification and choose Activate if the activation status is Inactive, and click on the model product specification to check the details. | Model product specification detail displays. |  |

### Test Automation Tool

SAP S/4HANA Cloud Public Edition provides a test automation tool that allows customers to speed up all business process tests, which could be tests during the implementation phase, user acceptance tests, or regression tests after upgrades.

Please refer to SAP note [2129147](https://me.sap.com/notes/2129147) - Test Automation Tool for SAP S/4HANA Cloud Public Edition - Additional Info..

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
> Flagged while digesting this document, not verified: Prelim step Configure Flexible Workflow for Purchase Order sets condition total net amount greater than 10 AED for group 003, while later PO approval steps state 500 AED or more requires approval.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Prelim step Configure Flexible Workflow for Service Entry Sheets enters Amount 10 AED (and expected result says greater than 10), while workflow name and later approval tables state 1000 AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Case 4 convert PR to PO uses Supplier 10300001 and Purchasing Organization 1010, differing from sample data (supplier 33300001, org 3310).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964]]
- related-to :: [[10-procurement/test-script-service-and-material-procurement-project-based-services-j1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/22Z_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 220,727 chars in the whole document
