---
id: 03-financial-accounting-and-close/test-script-travel-expense-processing-with-sap-concur-1m1-734
title: "Test Script: Travel Expense Processing with SAP Concur (1M1) (1M1_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 1M1: testing SAP S/4HANA Cloud and SAP Concur integration (cost object export, cash advances, expense reports, payment, budget)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/travel-expense-integration-sap-concur]
aliases: [1M1_S4CLD2608_BPD_EN_XX]
keywords: [Travel Expense Integration with SAP Concur, sap concur integration, travel expense processing, cost object export, master data export, cash advances, expense reports, financial posting, payment status, budget integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1M1_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-734
topic: 03-financial-accounting-and-close/travel-expense-integration-sap-concur
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Travel Expense Processing with SAP Concur (1M1) (1M1_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1M1_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Travel Expense Integration with SAP Concur** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Travel Expense Processing with SAP Concur (1M1) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850308)

[2 Prerequisites 4](#_Toc232850309)

[2.1 Additional Manual Configuration 4](#_Toc232850310)

[2.2 System Access 4](#_Toc232850311)

[2.3 Roles 4](#_Toc232850312)

[2.4 Master Data, Organizational Data, and Other Data 7](#_Toc232850313)

[2.5 Business Conditions 7](#_Toc232850314)

[3 Overview Table 9](#_Toc232850315)

[4 Test Procedures 12](#_Toc232850316)

[4.1 Cost Object Export from SAP S/4HANA Cloud (Manual Replication) 12](#_Toc232850317)

[4.1.1 Export Cost Center (Initial and Delta Replication) 12](#_Toc232850318)

[4.1.2 Export Project WBS Element (Initial and Delta Replication) 14](#_Toc232850319)

[4.1.3 Export Maintenance Order (Initial and Delta Replication) 16](#_Toc232850320)

[4.1.4 Export Service Order (Initial and Delta Replication) 19](#_Toc232850321)

[4.2 Export Exchange Rate from SAP S/4HANA Cloud Public Edition (Initial and Delta Replication) 22](#_Toc232850322)

[4.3 Export G/L Accounts from SAP S/4HANA Cloud Public Edition 23](#_Toc232850323)

[4.4 Export Tax Code from SAP S/4HANA Cloud Public Edition 25](#_Toc232850324)

[4.5 Financial Posting - Cash Advance 26](#_Toc232850325)

[4.5.1 Create Cash Advance 26](#_Toc232850326)

[4.5.2 Approve Cash Advance 27](#_Toc232850327)

[4.5.3 Automatically Process the Financial Posting Document Cash Advance 28](#_Toc232850328)

[4.5.4 Manually Process the Financial Posting Document Cash Advance (Optional) 29](#_Toc232850329)

[4.5.5 Check Cash Advance Status 31](#_Toc232850330)

[4.6 Financial Posting - Expense Report 32](#_Toc232850331)

[4.6.1 Create Expense Report 32](#_Toc232850332)

[4.6.2 Approve Expense Report as Expense Approver (Optional) 35](#_Toc232850333)

[4.6.3 Approve Expense Report as Expense Processor (Optional) 36](#_Toc232850334)

[4.6.4 Automatically Process the Financial Posting Document Expense Report 37](#_Toc232850335)

[4.6.5 Manually Process the Financial Posting Document Expense Report (Optional) 39](#_Toc232850336)

[4.6.6 Pay the Invoice in SAP S/4HANA Cloud Public Edition 41](#_Toc232850337)

[4.6.7 Manually Send the Payment Status to SAP Concur 43](#_Toc232850338)

[4.6.8 Check Payment Status 44](#_Toc232850339)

[4.6.9 Edit Expense Report 45](#_Toc232850340)

[4.6.10 Process Financial Posting and Pay Again 47](#_Toc232850341)

[4.7 Budget Integration 47](#_Toc232850342)

[4.7.1 Create Travel Request 48](#_Toc232850343)

[4.7.2 Manually Process Travel Request (Funds Check) 50](#_Toc232850344)

[4.7.3 Approve Travel Request as Request Approver (Optional) 51](#_Toc232850345)

[4.7.4 Manually Process Travel Request (Funds Reservation) 52](#_Toc232850346)

[4.7.5 Create Expense Report Obligation via Transport Request 54](#_Toc232850347)

[4.7.6 Manually Process Expense Report Obligation (Funds Check) 55](#_Toc232850348)

[4.7.7 Approve Expense Report Obligation as Expense Approver (Optional) 56](#_Toc232850349)

[4.7.8 Manually Process Expense Report Obligation (Funds Reservation) 57](#_Toc232850350)

[4.7.9 Manually Process Expense Report Obligation 59](#_Toc232850351)

[4.7.10 Close Travel Request 60](#_Toc232850352)

[4.7.11 Manually Process Closed Travel Request 61](#_Toc232850353)

[4.8 Tips and Error Handling 62](#_Toc232850354)

[4.8.1 Fix Errors in SAP S/4HANA Cloud Public Edition 63](#_Toc232850355)

[4.8.2 Fix Errors in SAP Concur 63](#_Toc232850356)

## Purpose

Overview

Cloud-based travel and expense solutions enable users to plan trips and create expense reports. This information is typically transferred to financial systems for posting. Integrate SAP S/4HANA Cloud Public Edition with SAP Concur to export cost objects, import expense reports and cash advances ready for posting, and export posting confirmations. The integration can be performed as a direct connection or through the SAP Cloud Integration service.

Based on the additional country/region-specific posting functionality, ensure that the corresponding country/region is supported and has no limitations. For more information, see the release information and restriction note for local versions updated with every release.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7a1ffe307efe000f76a3276ddd148dbb)

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) |
| SAP S/4HANA Cloud Public Edition | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Roles in SAP Concur

| Name | Description | ID | Log On |
| --- | --- | --- | --- |
| Expense Processor User | An employee who needs to create an expense report. |  | Example Test user: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |
| Expense Approver | A manager who needs to approve an expense submitted by employees. |  | Example Test user: ATTESTER.RDS@SAP.COMPassword: <Manually set in SAP Concur> |
| Expense Processor | A system administrator who needs to run a batch process. |  | Example Test user: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |
| Administrator | An administrator who has the administrator role. |  | Example Test user: <Administrator user role>Password: <Manually set in SAP Concur> |

Roles in SAP S/4HANA Cloud Public Edition

The following business roles are relevant for the end-to-end tests:

| Role Name | Role ID | Space Description | Space ID | Logon Information |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Internal Sales Representative - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV | Internal Sales - Professional Services | SAP_BR_INTERNAL_SALES_REP_PRSV |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Project Manager - Commercial Services | SAP_BR_PROJ_MANAGE_COMM |  |  |  |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Budget Specialist - Funds Management | SAP_BR_BUDGET_SPECIALIST | Budgeting | SAP_BR_BUDGET_SPECIALIST |  |
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |

|  |
| --- |
| Note To log in to the SAP system from the Concur system for the Enhanced WBS Element Search functionality, all employees must have business catalog Concur – Employee Self-Service(SAP_CON_BC_CTE_ESS_PC) assigned to their user in the SAP system. This business catalog also gives the necessary authorizations to view staffed projects where postings are eligible. |

To view all projects with posting-eligible WBS elements, the following business catalogs are required:

- Master Data - Business Partner Display(SAP_CMD_BC_BP_DISP_PC)
- Master Data - Customer Display(SAP_CMD_BC_CUSTOMER_DSP_PC)
- HCM - Employee Self Service(SAP_HCM_BC_EMP_PC)
- Project Management - Project Timesheet(SAP_HCM_BC_PRJ_TIMESHEET_PC)
- Project Management - Customer Project Display(SAP_PSP_BC_CUST_PROJ_DISP_PC)
- Project - Customer Project Setup(SAP_PSP_BC_CUSTOMER_PROJ_BC)
- Project Management - Internal Project Display(SAP_PSP_BC_INT_PROJ_DISP_PC)
- Project Internal Project Setup(SAP_PSP_BC_INTERNAL_PROJ_PC)

|  |
| --- |
| Note These business catalogs provide Read authorization only for projects that the employee is the Project Manager, Project Controller, Project Accountant, or Project Partner for. |

Alternatively, you can view all posting-eligible projects with business role Project Manager - Professional Services(SAP_BR_PROJECT_MANAGER_PROF).

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |
| Cost Center | 10101101 |  |  |
| Project WBS Element | TEST WBS A |  |  |
| Vendor | 9980000400 |  | Vendor ID should be assigned to the user in Concur. |
| Employee | 1(Dr. ATtester1 RDS)2(Dr. ATtester2 RDS) |  | The reporting line manager must be exported first. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 4RF - Project Control – Resourcing and Procurement | To use the enhanced WBSElement search feature, scope item [Project Control – Resourcing and Procurement (4RF)](https://me.sap.com/processnavigator/SolP/4RF) has to be active and its configuration has to be completed. Complete the project role assignment of an SAP Concur user to a project WBS element. |
| J11 - Customer Project Management – Project-Based Services | To use the enhanced WBSElement search feature, scope item [Customer Project Management – Project-Based Services (J11)](https://me.sap.com/processnavigator/SolP/J11) has to be active and its configuration has to be completed. Complete the project role assignment of an SAP Concur user to a project WBS element. |

## Overview Table

| Process Step | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Export Cost Center (Initial and Delta Replication)](#unique_9) [page ] 12 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | Cost centers are exported to the SAP Concur system. Changes in the cost centers are replicated to the SAP Concur system. |
| [Export Project WBS Element (Initial and Delta Replication)](#unique_10) [page ] 14 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | Project WBS elements are exported to the SAP Concur system. Changes in the Project WBS elements are replicated to the SAP Concur system. |
| [Export Maintenance Order (Initial and Delta Replication)](#unique_11) [page ] 16 | Maintenance Planner | Concur Integration Setup (CTE_SETUP) | Maintenance orders are exported to the SAP Concur system. Changes in the maintenance orders are replicated to the SAP Concur system. |
| [Export Exchange Rate from SAP S/4HANA Cloud Public Edition (Initial and Delta Replication)](#unique_12) [page ] 22 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | Exchange Rate is exported to the SAP Concur system. Changes in the Exchange Rate are replicated to the SAP Concur system. |
| [Create Cash Advance](#unique_13) [page ] 26 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | A cash advance is created and submitted to the Administrator for approval. |
| [Approve Cash Advance](#unique_14) [page ] 27 | Administrator in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The cash advance submitted by an Expense Processor is approved by an Administrator. |
| [Automatically Process the Financial Posting Document Cash Advance](#unique_15) [page ] 28 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The financial posting document cash advance is automatically processed from the SAP Concur financial posting queue and transfered to the SAP S/4HANA Cloud Public Edition system. |
| [Manually Process the Financial Posting Document Cash Advance (Optional)](#unique_16) [page ] 29 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | You manually processed the financial posting document cash advance from the SAP Concur financial posting queue and transfered it to the SAP S/4HANA Cloud Public Edition system. |
| [Check Cash Advance Status](#unique_17) [page ] 31 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The status of an issued cash advance is checked. |
| [Create Expense Report](#unique_18) [page ] 32 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | An expense report is created and submitted for approval. |
| [Approve Expense Report as Expense Approver (Optional)](#unique_19) [page ] 35 | Expense Approver in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The expense report submitted by the Expense Processor is approved by the Expense Approver. |
| [Approve Expense Report as Expense Processor (Optional)](#unique_20) [page ] 36 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The expense report submitted by the Expense Processor is approved by the Expense Processor. |
| [Automatically Process the Financial Posting Document Expense Report](#unique_21) [page ] 37 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The financial posting document expense report is automatically processed from the SAP Concur financial posting queue and transfered to the SAP S/4HANA Cloud Public Edition system. |
| [Manually Process the Financial Posting Document Expense Report (Optional)](#unique_22) [page ] 39 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | You manually processed the financial posting document expense report from the SAP Concur financial posting queue and transfered it to the SAP S/4HANA Cloud Public Edition system. |
| [Pay the Invoice in SAP S/4HANA Cloud Public Edition](#unique_23) [page ] 41 | Accounts Payable Accountant | Post Outgoing Payments (F1612) | The invoice is paid. |
| [Manually Send the Payment Status to SAP Concur](#unique_24) [page ] 43 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The payment status is sent from SAP S/4HANA Cloud Public Edition to the SAP Concur system. |
| [Check Payment Status](#unique_25) [page ] 44 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The expense report’s status is changed to paid. |
| [Edit Expense Report](#unique_26) [page ] 45 | Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | An expense entry of an expense report is added, edited, or deleted. |
| [Process Financial Posting and Pay Again](#unique_27) [page ] 47 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The expense report is imported to the SAP S/4HANA Cloud Public Edition system and is paid again. |
| [Create Travel Request](#unique_28) [page ] 48 | Request Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | A new travel request with status Submitted & Pending external approval is created. |
| [Manually Process Travel Request (Funds Check)](#unique_29) [page ] 50 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful (Check). |
| [Approve Travel Request as Request Approver (Optional)](#unique_30) [page ] 51 | Request Approver in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | Your travel request has been approved and is in status Pending External Validation. |
| [Manually Process Travel Request (Funds Reservation)](#unique_31) [page ] 52 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful (Obligate). |
| [Create Expense Report Obligation via Transport Request](#unique_32) [page ] 54 | Request and Expense Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | A new expense report with status Submitted & Pending approval is created. |
| [Manually Process Expense Report Obligation (Funds Check)](#unique_33) [page ] 55 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful (Check). |
| [Approve Expense Report Obligation as Expense Approver (Optional)](#unique_34) [page ] 56 | Expense Approver in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | Your expense report has been approved and is in status Approved & in Accounting review. |
| [Manually Process Expense Report Obligation (Funds Reservation)](#unique_35) [page ] 57 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful (Obligate). |
| [Manually Process Expense Report Obligation](#unique_36) [page ] 59 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful. |
| [Close Travel Request](#unique_37) [page ] 60 | Request Processor in SAP Concur Certified Expense Professional | [https://www.concursolutions.com/nui/signin](https://www.concursolutions.com/nui/signin) | The travel request is closed. |
| [Manually Process Closed Travel Request](#unique_38) [page ] 61 | Configuration Expert - Business Network Integration | Concur Integration Setup (CTE_SETUP) | The document status is changed to Successful (Released). |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Cost Object Export from SAP S/4HANA Cloud (Manual Replication)

#### Export Cost Center (Initial and Delta Replication)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually export a cost center to SAP Concur for financial posting. Only cost center code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all cost centers regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Cost Center > Manual Export. | The Export Cost Centers to Concur screen is displayed. |  |
| 4 |  | On the Export Cost Centers to Concur screen, enter the following data:ExampleControlling Area: <A00>Tip You can use the Search ( to search for a specific controlling area.Cost Center: <Cost Center>Tip You can use the Search ( to search for a specific cost center.Choose Execute. | The cost center is manually replicated.The Display logs screen and the system message Cost Center: export finished with <Number> successful objects. is displayed. |  |
| 5 |  | Choose Exit twice. | You’re redirected back to the Setting up the integration with Concur screen. |  |
| 6 | Logon | Log on to the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access App | Open the Manage Cost Centers - Old Version (F1443A) app. | The Manage Cost Centers screen is displayed. |  |
| 8 | Manage Cost Center | Choose Go. | All Cost Centers are displayed. |  |
| 9 |  | Select the cost center previously replicated and choose Edit to change the cost center description. Choose Save. | The cost center description is changed. |  |
| 10 | Cost Center Delta Replication | Repeat the steps described for the initial replication of the cost center. |  |  |
| 11 | Logon | Log on to the SAP Concur system as System Administrator.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 12 |  | Choose Administration > Expense. |  |  |
| 13 |  | Choose List Management. |  |  |
| 14 |  | Double click Cost Objects. |  |  |
| 15 |  | Choose the SAP S/4HANA Cloud Public Edition system from which you export the cost object. |  |  |
| 16 |  | Choose the company code from which you export the cost object. |  |  |
| 17 |  | Choose the Cost Object to display the detailed cost center export to SAP Concur. |  |  |

#### Export Project WBS Element (Initial and Delta Replication)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually export a project WBS element to SAP Concur for financial posting. Only project WBS element code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all project WBS elements regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Configuration Expert - Business Network Integration. |  |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Project WBS Element > Manual Export. | The Export Project WBS Elements to Concur screen is displayed. |  |
| 4 |  | On the Export Project WBS Elements to Concur screen, enter the following data:ExampleControlling Area: <A00>Tip You can use the Search () to search for a specific controlling area.WBS Element: <WBS Element>Tip You can use the Search () to search for a specific cost center.Choose Execute. | The Project WBS Element is manually replicated.The Display logs screen and the system message Project WBS Element: export finished with <Number> successful objects. is displayed.Tip If you've selected the Do not export billing WBS elements during the configuration, only nonbilling WBS elements are exported. For example, Test-WBSA01.1.1 is for nonbilling WBS elements, Test-WBSA01.0.1 is for billing WBS elements. |  |
| 5 |  | Choose Exit twice. | You’re redirected back to the Setting up the integration with Concur screen. |  |
| 6 | Logon | Log on to SAP Fiori launchpad as Project Financial Controller. |  |  |
| 7 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control - Enterprise Projects screen is displayed. |  |
| 8 | Update Project WBS Element | If you want to update a specific project, enter the required search criteria and choose Go. | A search results list is displayed. |  |
| 9 |  | From the search results list, select the project. |  |  |
| 10 |  | To update the project, choose Edit. Enter the required changes and choose Save. | The project WBS element is updated. |  |
| 11 | Project WBS Element Delta Replication | Repeat the steps described for the initial replication of the project WBS element. |  |  |
| 12 | Logon | Log on to the SAP Concur system as System Administrator.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 13 |  | Choose Administration > Expense. |  |  |
| 14 |  | Choose List Management. |  |  |
| 15 |  | Double click Cost Objects. |  |  |
| 16 |  | Choose the SAP S/4HANA Cloud Public Edition system from which you export the cost object. |  |  |
| 17 |  | Choose the company code from which you export the cost object. |  |  |
| 18 |  | Choose the Cost Object to display the detailed project WBS element export to SAP Concur. | Tip If you've selected the Do not export billing WBS elements during the configuration, only nonbilling WBS elements are exported. For example, Test-WBSA01.1.1 is for nonbilling WBS elements, Test-WBSA01.0.1 is for billing WBS elements. |  |

#### Export Maintenance Order (Initial and Delta Replication)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually export a maintenance order to SAP Concur for financial posting. Only the maintenance code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all cost centers regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Configuration Expert - Business Network Integration. |  |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Other Cost Objects > Maintenance Order > Manual Export . | The Export Maintenance Orders to Concur screen is displayed. |  |
| 4 |  | On the Export Maintenance Order to Concur screen, enter the following data:ExampleControlling Area: <A00>Tip You can use the Search (  ) to search for a specific controlling area.Company Code: <1010>Tip You can use the Search (  ) to search for a specific company code.Maintenance Order: <4000120>Tip You can use the Search (  ) to search for a specific maintenance order.Receiving System: <receiving system>Tip You can use the Search (  ) to search for a specific receiving system.Test Mode: Deselect the checkbox.Delete Maintenance Orders: Deselect the checkbox.Note If you want to delete existing maintenance orders from SAP Concur, select the checkbox.Choose Run.Note Only the following status of maintenance orders can be replicated:ReleasedCompleted, subphase is not closed | The maintenance order is manually replicated.The Display logs screen and the system message Maintenance Order: export finished with <Number> successful objects. is displayed. |  |
| 5 |  | Choose Exit twice. | You’re redirected back to the Setting up the integration with Concur screen. |  |
| 6 | Logon | Log on to SAP Fiori launchpad as Maintenance Planner. |  |  |
| 7 | Access App | Open the Manage Maintenance Notifications and Orders (F4604) app. | The Manage Maintenance Notifications and Orders screen is displayed. |  |
| 8 | Manage Maintenance Orders | If you want to manage maintenance orders, enter the required search criteria and choose Go. | A search results list is displayed. |  |
| 9 |  | From the search results list, select the maintenance order that you've previously replicated. |  |  |
| 10 |  | To update the maintenance order, choose Edit. Enter the required changes and choose Save.Note You can only change the description for maintenance orders in status Released. | The maintenance order is updated. |  |
| 11 | Maintenance Order Delta Replication | Repeat the steps described for the initial replication of the maintenance order. |  |  |
| 12 | Logon | Log on to the SAP Concur system as System Administrator.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 13 |  | Choose Administration > Expense . |  |  |
| 14 |  | Choose List Management. |  |  |
| 15 |  | Double click Cost Objects. |  |  |
| 16 |  | Select the SAP S/4HANA Cloud Public Edition system from which you export the cost object. |  |  |
| 17 |  | Select the company code from which you export the cost object. |  |  |
| 18 |  | Select the Cost Object to display the detailed maintenance order export to SAP Concur. |  |  |

#### Export Service Order (Initial and Delta Replication)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually export a service order to SAP Concur for financial posting. Only the service order code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all cost centers regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Configuration Expert - Business Network Integration. |  |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Other Cost Objects > Service Order > Manual Export . | The Export Service Order Items to Concur screen is displayed. |  |
| 4 |  | On the Export Service Order to Concur screen, enter the following data:ExampleControlling Area: <A000>Tip You can use the Search (  ) to search for a specific controlling area.Company Code: <1710>Tip You can use the Search (  ) to search for a specific company code.Transaction Type: <>Tip You can use the Search (  ) to search for a specific transaction type.Service Doc: <8000006010>Tip You can use the Search (  ) to search for a specific service order.Service Item: <000003>Tip You can use the Search (  ) to search for a specific service order item.Receiving System: <receiving system>Tip You can use the Search (  ) to search for a specific receiving system.Test Mode: Deselect the checkbox.Delete Service Orders: Deselect the checkbox.Note If you want to delete existing service orders from SAP Concur, select the checkbox.Choose Run.Note You can replicate service orders only when they're in the Released status. | The service order is manually replicated.The Display logs screen and the system message Service Order: export finished with <Number> successful objects. is displayed. |  |
| 5 |  | Choose Exit twice. | You’re redirected back to the Setting up the integration with Concur screen. |  |
| 6 | Logon | Log on to SAP Fiori launchpad as Customer Service Manager. |  |  |
| 7 | Access App | Open the Manage Service Orders - To-Do List (F3571A) app. | The Manage Service Orders screen is displayed. |  |
| 8 | Manage Service Orders | If you want to manage service orders, enter the required search criteria and choose Go. | A search results list is displayed. |  |
| 9 |  | From the search results list, select the service order that you've previously replicated. |  |  |
| 10 |  | To update the service order, choose Edit. Enter the required changes and choose Save.Note You can only change the description for service orders in status Released. | The service order is updated. |  |
| 11 | Service Order Delta Replication | Repeat the steps described for the initial replication of the service order. |  |  |
| 12 | Logon | Log on to the SAP Concur system as System Administrator.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 13 |  | Choose Administration > Expense . |  |  |
| 14 |  | Choose List Management. |  |  |
| 15 |  | Double click Cost Objects. |  |  |
| 16 |  | Select the SAP S/4HANA Cloud Public Edition system from which you export the cost object. |  |  |
| 17 |  | Select the company code from which you export the cost object. |  |  |
| 18 |  | Select the Cost Object to display the detailed service order export to SAP Concur. |  |  |

### Export Exchange Rate from SAP S/4HANA Cloud Public Edition (Initial and Delta Replication)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to export exchange rate to SAP Concur for financial posting. Only exchange rate code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all exchange rates regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as General Ledger Accountant or Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Exchange Rate > Manual Export. | The Export Exchange Rate screen is displayed. |  |
| 4 |  | On the Export Exchange Rate screen, enter the following data:ExampleExchange Rate Date: <03/01/2022>Tip Be aware that the meaning of the entered date differs depending on the settings that you've made on the Currency Exchange Rate screen. The following two options are possible:Exchange Rates Valid for this DateExchange Rates Valid from this DateTo Currency: <USD>Tip You can use the Search () to search for a specific currency.Choose Execute. | The exchange rate is manually replicated.The Display logs screen and the system message Exchange Rate: export finished with <Number> successful objects. is displayed. |  |
| 5 |  | Choose Exit twice. | You’re redirected back to the Setting up the integration with Concur screen. |  |

### Export G/L Accounts from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to export G/L accounts to SAP Concur for financial posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as General Ledger Accountant or Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Configuration > Manual Export . | The Export Financial Configuration to Concur screen is displayed. |  |
|  |  | Choose G/L Accounts checkbox. | The G/L Accounts configured in Configuration > Setup Configuration are replicated.The Display Logs screen and the system messageG/L Accounts: export finished with <Number> successful objects.is displayed. |  |
| 5 |  | Click Exit twice. | You’re redirected back to the Setting up Integration with Concur screen. |  |
| 6 | Logon | Log on to the SAP Concur system as System Administrator.Example Username: wsadmin@rds_sap_at-connect.com, Password: Welcome1 |  |  |
| 7 |  | Choose Administration > Expense |  |  |
| 8 |  | Under Expense Configurations, choose Accounting Administration. |  |  |
| 9 |  | Choose ERP Integration Ledger.Choose an Expense Type. | The exported G/L Accounts are list under ERP Account Code or Name. |  |

### Export Tax Code from SAP S/4HANA Cloud Public Edition

Purpose

This procedure describes how to export tax code to SAP Concur for financial posting. Only exchange rate code and its description can be exported from SAP S/4HANA Cloud Public Edition to SAP Concur. You can create a background job to export all exchange rates regularly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as General Ledger Accountant or Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Configuration > Manual Export . | The Export Business Configuration Objects screen is displayed. |  |
| 4 |  | Choose the Tax checkbox.Choose Execute. | The Tax Codes configured in Financial Configuration > Setup Configuration are replicated.The Display Logs screen and the system message Tax Codes export finished with <Number> successful objects. is displayed. |  |
| 5 |  | Choose Exit. | You’re redirected back to the Setting up the integration with Concur screen. |  |
| 6 | Logon | Log on to the SAP Concur system as System Administrator.For example:Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 7 |  | Choose Administration > Expense . |  |  |
| 8 |  | Under Expense Admin, choose Tax Administration. |  |  |
| 9 |  | Choose Tax & Reclaim Groups. |  |  |
| 10 |  | Choose one Group line and update. | The Tax code input from SAP S/4HANA Cloud Public Edition can be selected from the drop-down list of column ERP Tax Code and ERP Reclaim Tax Code. |  |

### Financial Posting - Cash Advance

|  |
| --- |
| Note If you've connected SAP Concur Standard with SAP S/4HANA Cloud Public Edition, only SAP Concur administrators can issue a cash advance, employees can’t do it themselves. |

To use an issued cash advance in an expense report, select an expense report, and choose Report Details > Manage Cash Advances > Add. In the Available Cash Advances dialog box, select a cash advance and choose Add To Report > Close.

Depending on your business requirements, you have the following options to use cash advance in expense reports:

- Employees can have a remaining balance on a cash advance and are able to apply the cash advance’s remaining balance to other expense reports until no balance remains.
- Employees are required to use the entirety of a cash advance when they submit their expense report and can return the unused amount with the expense type Cash Advance Return.
- If you've configured budget integration, cash advances are not supported as postings are done without specifying a cost or budget object. For more information, refer to [SAP Integration with Concur Solutions - Setup Guide - Connecting SAP S/4HANA Cloud Public Edition with SAP Concur](https://help.sap.com/doc/9f392802e456495c85618955c948c614/2402/en-US/SAP%20Concur%20Integration%20-%20Setup%20Guide.pdf).

For more information, refer to [Travel-to-Reimburse: SAP S/4HANA Cloud Public Edition & SAP Concur - Master Guide](https://help.sap.com/doc/9e03212489384bb09d7e579f31ea4d56/2011/en-US/T2R_Master_Guide_2011.pdf), chapter 2.1.1 Cash Advances & Remaining Balances.

|  |
| --- |
| Note To use cash advance, you need to configure the cash advance account code in your user account. |

#### Create Cash Advance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a cash advance in the SAP Concur system and submit it to the Administrator for approval.

Prerequisites

Before starting the following procedure, make sure that SAP S/4HANA Cloud Public Edition and SAP Concur have the identical employee data.

|  |
| --- |
| Caution If the data in the two systems mismatch, the financial posting fails. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Processor.Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Request Cash Advance | Choose Home > Expense > Cash Advances > Request Cash Advance. |  |  |
| 3 |  | Enter the following data according to your business requirements:ExampleCash Advance Name: Business Trip to BJCash Advance Amount: 100Currency: EuroChoose Submit. | A new cash advance is submitted and in status Pending Approval by Admin. |  |

#### Approve Cash Advance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how an Administator approves the cash advance submitted by an Expense Processor.

Prerequisites

As Expense Processor you have created and submitted a new cash advance (chapter [Create Cash Advance](#unique_13) [page ] 26).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Administrator.Username: <Administrator user role>Password: <Manually set in SAP Concur> |  |  |
| 2 | Approve Report | Choose Administration > Tools > Cash Advance Admin > Cash Advances .Select the following search options:And Belong to Group: All Groups I can AccessCash Advance Status: All Cash AdvancesChoose Search.Select the relevant cash advance from the search result list. Choose Issue.Note If the Reimbursement Currency in your account is different from the currency applied in the cash advance, the exchange rate is required to issue a cash advance. | In the Cash Advance Issued dialog box the system message Business Trip to BJ has been issued is displayed. |  |

#### Automatically Process the Financial Posting Document Cash Advance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to automatically process the financial posting document cash advance from the SAP Concur financial posting queue and transfer it to the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note If one of the following steps fails, you can also trigger the document processing manually. For more information, see [Manually Process the Financial Posting Document Cash Advance (Optional)](#unique_16) [page ] 29. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as General Ledger Accountant and Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Set Up the Automatic Import of Concur Documents | Choose Feedback Loop > Start Automatically. | The Feedback Loop screen is displayed. |  |
| 5 |  | On the Feedback Loop screen, enter a system key in the Concur System field.Choose Execute. | If the feedback loop completed successfully, the following steps in the document processing are completed:The document is automatically retrieved from the SAP Concur financial posting queue by the SAP S/4HANA Cloud Public Edition system. The document status is New.An acknowledgment is sent to the SAP Concur system that the document arrived and was accepted by the SAP S/4HANA Cloud Public Edition system.The document is posted - either successfully or it fails. A confirmation is sent accordingly. If an error occurs, the employee or administrator can correct the expense report in the SAP Concur system and resubmit it in which case it’s forwarded to the financial posting queue again. |  |
| 6 | View Successfully Posted Documents | On the Concur Documents screen, choose Display > Posted Document. | Successfully posted documents are displayed. |  |

#### Manually Process the Financial Posting Document Cash Advance (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually process the financial posting document cash advance from the SAP Concur financial posting queue and transfer it to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as General Ledger Accountant and Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Set Up the Manual Import of Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Expense Report from the dropdown list.All Documents: Select the radio button.Choose Enter. | The expense report is imported from SAP Concur to SAP S/4HANA Cloud Public Edition. |  |
| 5 | Send Acknowledgment to SAP Concur | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Send Acknowledgement. | The acknowledgment is sent to notify SAP Concur that the document arrived in the SAP S/4HANA Cloud Public Edition system with the status New. |  |
| 6 | Post Document | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Post. | The expense report is posted. |  |
| 7 | Send Confirmation to SAP Concur | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Send Confirmation. | The confirmation is sent to notify SAP Concur about whether the documents were posted successfully or not. For failed postings, additional details are included in the notification. |  |
| 8 | View Successfully Posted Documents | On the Concur Documents screen, choose Display > Posted Document. | Successfully posted documents are displayed. |  |

#### Check Cash Advance Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the status of an issued cash advance in the SAP Concur system.

Prerequisites

Before starting the following procedure, make sure that SAP S/4HANA Cloud Public Edition and SAP Concur have the identical employee data.

|  |
| --- |
| Caution If the data in the two systems mismatch, the financial posting will fail. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Processor.Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Check Payment Status | Choose Expense > Cash Advances.In the View field, choose Issued Cash Advances. | The status of your cash advance is updated to Issued. |  |

### Financial Posting - Expense Report

#### Create Expense Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an expense report in the SAP Concur system and submit it to the approver.

Prerequisites

To select a specific project WBS element as cost object through the enhanced WBS element search, you need to ensure that the SAP Concur user is staffed as employee for the WBS element.

|  |
| --- |
| Note If you've connected SAP Concur Standard with SAP S/4HANA Cloud Public Edition, enhanced WBS element search is not supported. You can then skip step 4 Change Cost Object to Project WBS Element (Optional).For more information about how to assign the project role of an SAP Concur user to a project WBS element in scope item [Project Control – Resourcing and Procurement (4RF)](https://me.sap.com/processnavigator/SolP/4RF) or in scope item [Customer Project Management – Project-Based Services (J11)](https://me.sap.com/processnavigator/SolP/J11). |

Make sure that SAP S/4HANA Cloud Public Edition and SAP Concur have the identical employee data.

|  |
| --- |
| Caution If the data in the two systems mismatch, the financial posting fails. |

If you've enabled the business place and want to enter it during the creation of an expense report, refer to the [SAP Integration with Concur Solutions - Setup Guide](https://help.sap.com/doc/c08ca38642004005b5e562095a1baf94/2105/en-US/2105%20SAP%20Concur%20Integration%20-%20Setup%20Guide.pdf), section 7.8 Change Business Place for Expense Reports.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Create Expense Report | Choose Home > Expense > Create New Report. |  |  |
| 3 |  | Enter the following data:ExampleReport Name: Business Trip to BJPolicy: Global Expense PolicyComment: Business TripLogical System: <Logical System>Company Code: <Company Code>Cost Object Type: <Cost Center> or <(PJ) Project WBS Element> or <(MO) Maintenance Order> or <(SO) Service Order>Cost Object ID: <Cost Center for your request> or <(PJ) Project WBS Element for your request> or <(MO) Maintenance Order for your request> or <(SO) Service Order for your request>Choose Create Report. |  |  |
| 4 | Change Cost Object to Project WBS Element (Optional) | In the Enhanced WBS Element Search field, choose Open. | The Report Saved system message is displayed.The SAP S/4HANA Cloud System Logon screen is displayed. |  |
| 5 |  | On the SAP S/4HANA Cloud System Logon screen, enter your logon information. | The Enhanced WBS Element Search screen is displayed. |  |
| 6 |  | Choose one of the available options of WBS Element Search Type: All Elements That I can View or Only My Assignments (Staff)To search for projects, enter the relevant data. Choose Go. | A search results list with related WBS elements is displayed. |  |
| 7 |  | Select a specific WBS Element ID and choose Select WBS Element. Close the Enhanced WBS Element Search dialog box. | The system message Project “XXXXXXXXX” has been taken over successfully. Please close window. is displayed.The project information (company code, cost object type, cost object ID) is reflected in the expense report.Note Depending on the configuration in SAP Concur, the cost object can be changed to a WBS element on the expense entry level and allocation. |  |
| 8 |  | Choose Create Report. |  |  |
| 9 |  | Choose Add Expense and enter the following data:ExampleExpense Type: BreakfastTransaction Date: 2016-09-05Business Purpose: Visit CustomerEnter Vendor Name: KFCCity of Purchase: Select a city of purchase from the dropdown list.Payment Type: <Payment Type>Amount: 30 EURReceipt Status: ReceiptInvoice in company name: Don’t select the checkbox.Choose Attach Receipt.To select the picture you want to attach, choose Browse.Choose Attach.Note If you want to change the default value of the Cost Object Type to a project WBS element, choose Open in the Search WBS Elements section and repeat step 4 to step 8.Choose Save. |  |  |
| 10 |  | To add more expenses, repeat step 9. |  |  |
| 11 |  | Choose Submit Report > Accept & Submit. | A new expense report with status Submitted & Pending approval is created. |  |

#### Approve Expense Report as Expense Approver (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how an Expense Approver can approve the expense report submitted by the Expense Processor.

|  |
| --- |
| Note This procedure is only relevant, if the manager approval is configured in the SAP Concur system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Approver.Example Username: ATTESTER.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Approve Report | Choose Approvals and select an expense report from the list.Choose Approve.On the Confirmation screen, choose Accept. | Your expense report has been approved and is in status Approved & in Accounting review. |  |

#### Approve Expense Report as Expense Processor (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how an Expense Processor approves the cash advance submitted by an Expense Processor.

|  |
| --- |
| Note This procedure is only relevant, if the manager approval is configured in the SAP Concur system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as Expense Processor.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 2 | Process Report | Choose Expense > Processor > Process Reports . |  |  |
| 3 |  | Choose Run Query. From the dropdown list, choose Reports Ready for Processing. |  |  |
| 4 |  | Choose Report > Approve . | The report approval status changes from Approved & in accounting review to Approved & processing payment. |  |

#### Automatically Process the Financial Posting Document Expense Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to automatically process the financial posting document expense report from the SAP Concur financial posting queue and transfer it to the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note If one of the following steps fails, you can also trigger the document processing manually. For more information, see [Manually Process the Financial Posting Document Expense Report (Optional)](#unique_22) [page ] 39. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant and Configuration Expert - Business Network Integration. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Set Up the Automatic Import of Concur Documents | Choose Feedback Loop > Start Automatically. | The Feedback Loop screen is displayed. |  |
| 5 |  | On the Feedback Loop screen, enter a system key in the Concur System field.Choose Execute. | If the feedback loop completed successfully, the following steps in the document processing are completed:The document is automatically retrieved from the SAP Concur financial posting queue by the SAP S/4HANA Cloud Public Edition system. The document status is New.An acknowledgment is sent to the SAP Concur system that the document arrived and was accepted by the SAP S/4HANA Cloud Public Edition system.The document is posted - either successfully or it fails. A confirmation is sent accordingly. If an error occurs, the employee or administrator can correct the expense report in the SAP Concur system and resubmit it in which case it’s forwarded to the financial posting queue again. |  |
| 6 | Retrieve Attachment | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Retrieve Attachment. | The attachment of the imported expense report is retrieved. |  |
| 7 | View Successfully Posted Documents | Select a document and choose Display > Posted Document. | Successfully posted documents are displayed. On the Posted Document screen, you can download the attachment to view it.Depending on how the Reference Key Type has been defined in the Additional Posting Settings, the following data is displayed:Reference: <Report/Document Key or Report/Document Number> <Revision Number>Header Text: <Employee ID/Vendor ID>/<Report/Document Key or Report/Document Number>/<Revision Number>Note For more information about the additional posting settings, refer to the set-up instructions of the scope item [Travel Expense Processing with SAP Concur (1M1)](https://me.sap.com/processnavigator/SolP/1M1), chapter Set Up Financial Posting Configuration. |  |
|  |  | Optionally, select a line item number in the Line Items table. | The line item is displayed.The line item text is displayed as the login ID for the SAP Concur system, for example, <test@p0015904rcka.com>.Note The result depends on how the substitution rules have been set up for Concur documents. |  |
| 9 | View Attachments | On the Concur Documents screen, choose Display > Attachments. | The attachment is displayed. To view the attachment, double-click on the attachment file name. |  |
| 10 | View Customer Modifications (Optional) | On the Concur Documents screen, choose Display > Customer Modifications. | On the Customer Modification screen, the original and modified fields are displayed. |  |

#### Manually Process the Financial Posting Document Expense Report (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually process the financial posting document expense report from the SAP Concur financial posting queue and transfer it to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant and Configuration Expert - Business Network Integration. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Set Up the Manual Import of Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Expense Report from the dropdown list.All Documents: Select the radio button.Choose Enter. | The expense report is imported from SAP Concur to SAP S/4HANA Cloud Public Edition. |  |
| 5 | Send Acknowledgment to SAP Concur | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Send Acknowledgement. | The acknowledgment is sent to notify SAP Concur that the document arrived in the SAP S/4HANA Cloud Public Edition system with the status New. |  |
| 6 | Post Document | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Post. | The expense report is posted. |  |
| 7 | Send Confirmation to SAP Concur | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Send Confirmation. | The confirmation is sent to notify SAP Concur about whether the documents were posted successfully or not. For failed postings, additional details are included in the notification. |  |
| 8 | Retrieve Attachment | On the Concur Documents screen, select the newly imported expense report. Choose Feedback Loop > Step-by-Step > Retrieve Attachment. | The attachment of the imported expense report is retrieved. |  |
| 9 | View Successfully Posted Documents | On the Concur Documents screen, choose > Posted Document. | Successfully posted documents are displayed. On the Posted Document screen, you can download the attachment to view it.Depending on how the Reference Key Type has been defined in the Additional Posting Settings, the following data is displayed:Reference: <Report/Document Key or Report/Document Number> <Revision Number>Header Text: <Employee ID/Vendor ID>/<Report/Document Key or Report/Document Number>/<Revision Number>Note For more information about the additional posting settings, refer to the set-up instructions of the scope item [Travel Expense Processing with SAP Concur (1M1)](https://me.sap.com/processnavigator/SolP/1M1), chapter Set Up Financial Posting Configuration. |  |
|  |  | Optionally, select a line item number in the Line Items table. | The line item and the reference key 1, for example, Test_SubRule are displayed.Note The result depends on how the substitution rules have been set up for SAP Concur documents. |  |
| 11 | View Attachments | On the Concur Documents screen, choose Display > Attachments. | The attachment is displayed. To view the attachment, double-click on the attachment file name. |  |
| 12 | View Customer Modifications (Optional) | On the Concur Documents screen, choose Display > Customer Modifications. | On the Customer Modification screen, the original and modified fields are displayed. |  |

#### Pay the Invoice in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post and clear a single outgoing payment for the invoice transferred from the SAP Fieldglass system to the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Outgoing Payments (F1612) app. | The Post Outgoing Payments screen is displayed. |  |
| 3 | Enter Payment Data | In the General Information section, enter the following data:ExampleCompany Code: 1010 (DE)Posting Date: <today's date>Journal Entry Date: <today's date>Value Date: <today's date>Journal Entry Type: KZIn the Bank Data section, enter the following data:ExampleHouse Bank/Account: DEBK1/DEAC1 (DE)G/L Account: 11001000Amount: <amount to pay on existing invoice>In the Open Item Selection section, enter the following data:ExampleAccount Type: SupplierAccount ID: 10300080Choose Show Items. | In the Open Items/Standard section, a list of open items is displayed. |  |
| 4 | Select Item | To select the retrieved invoice to pay, choose Clear. | The invoice to pay is transferred to the Items to the Cleared (Standard) section. |  |
| 5 | Post Item | Choose Post. | The system message Journal entry xxxxxxxxxx (Year, Company Code) posted is displayed. |  |
| 6 | Confirm | To confirm the Information dialog box, choose OK. |  |  |
| 7 | Navigate Back | Choose Back. | The system message Journal entry has already been posted. You can now post a new payment. is displayed. |  |
| 8 | Dismiss Message | To dismiss the message, choose OK. |  |  |

#### Manually Send the Payment Status to SAP Concur

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to send the payment status for expense reports to the SAP Concur system to conclude the notification process.

Prerequisites

The payment notification in the Financial Posting wizard is enabled.

The payment status is synchronized in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Network Integration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Synchronize Payment Status | To verify that the status of successfully posted documents reflects the result of the current payment run, select the document. Choose Document > Synchronize Payment Status.Note This step and the following steps have to be repeated and completed for every document type. | If the status in the Payment Status column differs from the current status of the payment run, it’s updated accordingly. |  |
| 5 | Send Payment Status | Select the document and choose Feedback Loop > Step-by-Step > Send Payment Status. | The payment status was sent to the SAP Concur system. |  |

#### Check Payment Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the payment status of a document in the SAP Concur system.

Prerequisites

Before starting the following procedure, make sure that SAP S/4HANA Cloud Public Edition and SAP Concur have the identical employee data.

|  |
| --- |
| Caution If the data in the two systems mismatch, the financial posting will fail. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Check Payment Status | In the View section, select the last 90 days. | The status of your expense report is updated to Payment Confirmed. |  |

#### Edit Expense Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add, edit, or delete an expense entry of an expense report in the SAP Concur system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Edit Expense Report | Choose Expense. | The Manage Expenses screen is displayed. |  |
| 3 |  | On the Manage Expenses screen, choose the Last 90 Days view. | A search result list with all relevant reports is displayed. |  |
| 4 |  | From the search result list, select the expense report you want to edit.Choose Reopen Report. In the Reopen Report dialog box, choose Reopen Report.Choose Report Details > Report Header . | The Report Header screen is displayed. |  |
| 5 |  | On the Report Header screen, you can perform the following actions depending on your business requirements:Delete an expense entry.Edit an expense entry.In the expense report, select an expense entry. Choose Edit and enter the following data according to your business requirements:ExampleAmount: 50 EURTransaction Date: 2016-09-10Attached Receipt Image: Upload an image.Add an expense entry.In the expense report, choose Add Expense and enter the following data according to your business requirements:ExampleExpense Type: BreakfastTransaction Date: 2016-09-05Business Purpose: Visit CustomerEnter Vendor Name: KFCCity of Purchase: From the dropdown list, select an entry.Payment Type: <Default Value>Amount: 100 EURReceipt Status: ReceiptChoose Save > Submit Report . | The updated expense report is submitted to the SAP Concur financial posting queue. |  |

#### Process Financial Posting and Pay Again

To process financial posting and pay again, repeat the procedure from [Manually Process the Financial Posting Document Expense Report (Optional)](#unique_22) [page ] 39 to [Check Payment Status](#unique_25) [page ] 44.

|  |
| --- |
| Note To import the updated attachments, complete the following steps:Log on to SAP Fiori launchpad as a Configuration Expert - Business Network Integration.SAP Fiori launchpad is displayed.Open the Concur Integration Setup (CTE_SETUP) app.The Setting Up the Integration with SAP Concur screen is displayed.In the Communication Arrangement column, select a communication arrangement and choose Financial Posting > Concur Documents .The Concur Documents screen is displayed.Select an expense report with revision number 1.Choose Document > Retry Attachment Retrieval . |

### Budget Integration

|  |
| --- |
| Note Budget checks and reservations are done within SAP’s Public Sector Management (PSM) functionality.Budget management is a basic user scenario. To run it within SAP’s Public Sector Management, derivation rules need to be defined. For more information about creating or increasing budgets, refer to the [Government Budget Management (US/CA) (3QE)](https://me.sap.com/processnavigator/SolP/3QE) test script (for US/CA).The workflow configured in the SAP Concur system will dictate in which order the steps are done and which SAP Concur document types are expected.If you've connected SAP Concur Standard with SAP S/4HANA Cloud Public Edition, the budget integration scenario is not supported. |

#### Create Travel Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a travel request in the SAP Concur system and submit it to the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Request Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Create Travel Request | Choose Home > Request > Create New Request. |  |  |
| 3 |  | Enter the following data according to your business requirements:ExampleReport Name: TR for Business TripRequest Policy: Travel Request Check and ObligatePurpose: <Purpose>System: <Connected SAP S/4HANA Cloud Public Edition system>Company Code: <Company Code>Cost Object Type: <Cost Center>Cost Object ID: <Cost Center for your Request>Start Date: <Start Date for Travel Request>End Date: <End Date for Travel Request>Choose Create Request. |  |  |
| 4 |  | In the Expected Expenses section, choose Add and enter the following data according to your business requirements:ExampleExpense Type: AirfareTransaction Date: <Transaction Date>Description: <Description>Amount: 30Currency: <USD>Choose Save. |  |  |
| 5 |  | To add more expenses, repeat the previous step. |  |  |
| 6 |  | Choose Submit Request. | A new travel request with status Submitted & Pending external approval is created. |  |

#### Manually Process Travel Request (Funds Check)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to import a travel request document from SAP Concur to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 |  | In the Commmunication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Manual Import SAP Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Travel Request from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful (Check).If you choose this option, you don't have to complete the next step. | The travel request is imported from SAP Concur to SAP S/4HANA Cloud Public Edition with the status New (Check). |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful (Check). |  |

#### Approve Travel Request as Request Approver (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve a travel request in SAP Concur as request approver.

|  |
| --- |
| Note Depending on the SAP Concur configuration, this procedure is optional. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as a Request Approver.Example Username: ATTESTER.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Approve Request | Choose Approvals > Request and select a travel request from the list.Choose Approve. | Your travel request has been approved and is in status Pending External Validation. |  |

#### Manually Process Travel Request (Funds Reservation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to import a travel request document from SAP Concur to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 |  | In the Commmunication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Manual Import SAP Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Travel Request from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful (Obligate).If you choose this option, you don't have to complete the next step. | The status of the travel request that was imported from SAP Concur to SAP S/4HANA Cloud Public Edition in [Manually Process Travel Request (Funds Check)](#unique_29) [page ] 50is changed to New (Obligate). |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful (Obligate). |  |

#### Create Expense Report Obligation via Transport Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an expense report obligation via a transport request in the SAP Concur system and submit it to the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as a Request and Expense Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Create Expense Report | Choose Requests > Active Requests .Select the approved travel request created in [Create Travel Request](#unique_28) [page ] 48.On the <Travel Request> detail page, choose Create Expense Report.On the <Expense Report> detail page, select the configured policy for budget integration, for example, <Global expense policy after budget check> and choose Save Expense. |  |  |
| 3 |  | Choose Submit Report > Accept & Submit . | A new expense report with status Pending External Validation is created. |  |

#### Manually Process Expense Report Obligation (Funds Check)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to import an expense report obligation document from SAP Concur to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 |  | In the Commmunication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Manual Import SAP Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Expense Report from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful (Check).If you choose this option, you don't have to complete the next step. | The expense report obligation is imported from SAP Concur to SAP S/4HANA Cloud Public Edition with the status New (Check). |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful (Check). |  |

#### Approve Expense Report Obligation as Expense Approver (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how an Expense Approver can approve the expense report obligation submitted by the Expense Processor.

|  |
| --- |
| Note This procedure is only relevant, if the manager approval is configured in the SAP Concur system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Expense Approver.Example Username: ATTESTER.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Approve Report | Choose Approvals and select an expense report from the list.Choose Approve.On the Confirmation screen, choose Accept. | Your expense report has been approved and is in status Approved & in Accounting review. |  |

#### Manually Process Expense Report Obligation (Funds Reservation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to manually process an obligate expense report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 | Set Up the Integration with SAP Concur | In the Communication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Set Up the Manual Import of Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Expense Report Obligation from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful (Obligate).If you choose this option, you don't have to complete the next step. | The status of the expense report obligation that was imported from SAP Concur to SAP S/4HANA Cloud Public Edition in [Manually Process Expense Report Obligation (Funds Check)](#unique_33) [page ] 55 is changed to New (Obligate). |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful (Obligate). |  |

#### Manually Process Expense Report Obligation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to import an expense report obligation document from SAP Concur to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 |  | In the Commmunication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Manual Import SAP Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Expense Report from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful.If you choose this option, you don't have to complete the next step. | The expense report is imported from SAP Concur to SAP S/4HANA Cloud Public Edition with the status New. |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful. |  |

#### Close Travel Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to close a travel request in the SAP Concur system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as an Request Processor.Example Username: ATTESTER2.RDS@SAP.COMPassword: <Manually set in SAP Concur> |  |  |
| 2 | Select Travel Request | Choose Requests > Active Requests .Select the approved travel request created in [Create Travel Request](#unique_28) [page ] 48. |  |  |
| 3 | Close Travel Request | Choose Request > More Actions > Close Request . | The travel request is closed. |  |

#### Manually Process Closed Travel Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to import a closed travel request document from SAP Concur to SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as General Ledger Accountant, Configuration Expert - Business Network Integration, and Budget Specialist - Funds Management. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Concur Integration Setup (CTE_SETUP) app. | The Setting Up the Integration with SAP Concur screen is displayed. |  |
| 3 |  | In the Commmunication Arrangement column, select a communication arrangement and choose Budget Integration > Concur Documents. | The Concur Documents screen is displayed. |  |
| 4 | Manual Import SAP Concur Documents | On the Concur Documents screen, choose Feedback Loop > Step-by-Step > Import Documents from Queue.Note The following steps have to be repeated and completed for every document type.In the Import Documents from Queue dialog box, configure the following settings:ExampleDocument Type: Select Travel Request from the dropdown list.All Documents: Select the radio button.Choose Enter.Note Alternatively, choose Feedback Loop > Start Automatically > Execute.The document status is changed to Successful (Released).If you choose this option, you don't have to complete the next step. | The travel request is imported from SAP Concur to SAP S/4HANA Cloud Public Edition with the status New (Released). |  |
| 5 | Process Document | On the Concur Documents screen, select a document and continue with one of the following options:Option 1:Choose Feedback Loop > Step-by-Step > Send Acknowledgement.Choose Feedback Loop > Step-by-Step > Post.Choose Feedback Loop > Step-by-Step > Send Confirmation.Option 2:Alternatively, choose Feedback Loop > Start for Selected. | The document status is changed to Successful (Released). |  |

### Tips and Error Handling

Generally, if you strictly follow the test steps above, the financial posting should be successful. However, if it fails, you can follow the procedure below to recall the expense report and post it again.

#### Fix Errors in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Due to various possible errors that might occur in SAP S/4HANA Cloud Public Edition, not all of these errors are listed here.

However, before starting the following procedure, review the configuration errors in SAP S/4HANA Cloud Public Edition first.

Procedure

To complete the financial posting after figuring out the errors in SAP S/4HANA Cloud Public Edition, repeat the procedure from chapter [Create Expense Report](#unique_18) [page ] 32 to chapter [Manually Process the Financial Posting Document Expense Report (Optional)](#unique_22) [page ] 39.

#### Fix Errors in SAP Concur

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Due to various possible errors that might occur in SAP Concur, not all of these errors are listed here.

However, before starting the following procedure, review the configuration errors in SAP Concur first.

Procedure

To complete the financial posting after figuring out the errors in SAP Concur, repeat the procedure from chapter [Create Expense Report](#unique_18) [page ] 32 to chapter [Manually Process the Financial Posting Document Expense Report (Optional)](#unique_22) [page ] 39.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Concur system as Expense Processor User.Example Username: wsadmin@rds_sap_at-connect.comPassword: Welcome1 |  |  |
| 2 | Process Expense Report | Choose Expense. | The Manage Expenses screen is displayed. |  |
| 3 |  | On the Manage Expenses screen, choose Processor > Process Reports .Set the relevant search filters to find the expense report and choose Go. | The eligible expense reports are displayed. |  |
| 4 |  | Choose Report. |  |  |
| 5 |  | Choose Recall to Processor. | The report approval status changes from Approved & Processing Payment to Approved & In Accounting Review. |  |

To post the expense report again after recalling it, repeat the procedure in chapter [Manually Process the Financial Posting Document Cash Advance (Optional)](#unique_16) [page ] 29.

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
> Flagged while digesting this document, not verified: Overview Table and procedures disagree on resulting statuses: Create Expense Report Obligation via Transport Request is listed as 'Submitted & Pending approval' but its procedure gives 'Pending External Validation'; Check Payment Status is listed as 'changed to paid' but its procedure gives 'Payment Confirmed'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Pay the Invoice procedure describes the invoice as 'transferred from the SAP Fieldglass system', although the rest of this script has invoices originating from SAP Concur expense reports.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042]]
- see-also :: [[03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1M1_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 104,498 chars in the whole document
