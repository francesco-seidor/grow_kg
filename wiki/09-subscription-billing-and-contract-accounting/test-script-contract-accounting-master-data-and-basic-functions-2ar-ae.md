---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-master-data-and-basic-functions-2ar-ae
title: "Test Script: Contract Accounting – Master Data and Basic Functions (2AR_AE) (2AR_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition test script for scope item 2AR (FI-CA, AE): business partner, contract account, provider contract, correspondence, privacy."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-master-data-and-basic-functions]
aliases: [2AR_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Master Data and Basic Functions, business partner, customer master data, contract accounts, provider contracts, account statements, correspondence printing, balance notifications, contract confirmation letters, external output management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2AR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-808
topic: 09-subscription-billing-and-contract-accounting/fi-ca-master-data-and-basic-functions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Master Data and Basic Functions (2AR_AE) (2AR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2AR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Master Data and Basic Functions** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Master Data and Basic Functions (2AR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849014)

[2 Prerequisites 4](#_Toc232849015)

[2.1 System Access 4](#_Toc232849016)

[2.2 Roles 4](#_Toc232849017)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232849018)

[2.4 Business Conditions 7](#_Toc232849019)

[2.5 Additional Manual Configuration 8](#_Toc232849020)

[2.6 Preliminary Steps 8](#_Toc232849021)

[2.6.1 Create Worker (Optional) 8](#_Toc232849022)

[2.6.2 Manage Teams and Responsibility (Optional) 8](#_Toc232849023)

[2.6.3 Set Event-Based Situation Types (Optional) 9](#_Toc232849024)

[2.6.4 Manage Event-Based Situation (Optional) 11](#_Toc232849025)

[2.6.5 Set Message-Based Situation Types (Optional) 11](#_Toc232849026)

[2.6.6 Manage Message-Based Situation (Optional) 12](#_Toc232849027)

[2.6.7 Monitor Notification (Optional) 14](#_Toc232849028)

[2.6.8 Email Notifications for Message-Based Situation (Optional) 15](#_Toc232849029)

[2.6.9 Create Provider Contract with Service Based Product 16](#_Toc232849030)

[3 Overview Table 20](#_Toc232849031)

[4 Test Procedures 22](#_Toc232849032)

[4.1 Master Data 22](#_Toc232849033)

[4.1.1 Create a Business Partner 22](#_Toc232849034)

[4.1.2 Create Customer Master Data 25](#_Toc232849035)

[4.1.3 Create a Contract Account 26](#_Toc232849036)

[4.1.4 Create Provider Contract Via API 28](#_Toc232849037)

[4.2 Correspondence 30](#_Toc232849038)

[4.2.1 Create Account Statement 30](#_Toc232849039)

[4.2.2 Print Account Statement 32](#_Toc232849040)

[4.2.2.1 Print Correspondence 32](#_Toc232849041)

[4.2.2.2 Display Correspondences 34](#_Toc232849042)

[4.2.3 Create Balance Notification 35](#_Toc232849043)

[4.2.4 Print Balance Notification 37](#_Toc232849044)

[4.2.4.1 Print Correspondence 37](#_Toc232849045)

[4.2.4.2 Display Correspondences 37](#_Toc232849046)

[4.2.5 Create Contract Confirmation Letter 37](#_Toc232849047)

[4.2.6 Print Contract Confirmation Letter 38](#_Toc232849048)

[4.2.6.1 Print Correspondence 38](#_Toc232849049)

[4.2.6.2 Display Correspondences 38](#_Toc232849050)

[4.2.7 Print by External Service Providers 38](#_Toc232849051)

[4.2.7.1 Create Account Statement 39](#_Toc232849052)

[4.2.7.2 Manage Output Queues for External Output Management 39](#_Toc232849053)

[4.2.7.3 Print Correspondence 40](#_Toc232849054)

[5 Appendix 43](#_Toc232849055)

[5.1 Process Integration 43](#_Toc232849056)

[5.1.1 Display and Change a Business Partner 43](#_Toc232849057)

[5.1.2 Display and Change a Contract Account 44](#_Toc232849058)

[5.1.3 Display Provider Contract 45](#_Toc232849059)

[5.1.4 Overview of Contracts and Contract Items 46](#_Toc232849060)

[5.1.5 Create Worker 47](#_Toc232849061)

[5.1.6 Data Privacy 48](#_Toc232849062)

[5.1.6.1 Analyze Business Partner Data 52](#_Toc232849063)

[5.1.6.2 Check Business Partner Can Be Blocked 53](#_Toc232849064)

[5.1.6.3 Block Business Partner 54](#_Toc232849065)

[5.1.7 Delete Test Data 55](#_Toc232849066)

[5.1.8 Display Processing Locks 56](#_Toc232849067)

## Purpose

Overview

Business partner and contract management allows you to create and manage master data of a business partner and a contract account for Contract Accounts Receivable and Payable (FI-CA). In addition, you can analyze whether business partner data can be deleted to satisfy data privacy constraints in SAP S/4HANA Cloud Public Edition. Furthermore, you can create and print correspondence.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2AR_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Data Privacy Specialist - Accounts Payable and Receivable (FI-CA) | SAP_BR_DATA_PRIVACY_SPEC_FICA | Contract Accounting - Data Privacy | SAP_BR_DATA_PRIVACY_SPEC_FICA |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Employee - Situation Handling | SAP_BR_EMPLOYEE_SITUATION | Employee - Situation Handling | SAP_BR_EMPLOYEE_SITUATION |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Accounts Payable and Receivable Manager (FI-CA) | SAP_BR_APR_MANAGER_FICA | Contract Accounting - Analytics | SAP_BR_APR_MANAGER_FICA |  |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Organizational Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Company Code Group | 3310 |  |  |

Table 2: Sales and Distribution Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |
| Plant | 3310 |  |  |

Table 3: Accounting Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Country | AE |  |  |
| Bank Key | 10020030 |  |  |
| SWIFT/BIC |  |  |  |

Table 4: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Account Determination ID | Y1 |  |  |
| Planning Group / Level | Domestic customers |  |  |
| Material Master | CBPTS002 |  |  |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

For more information about creating master data objects, see [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 5: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 31X | Create Product Master of type "Service Product" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 31N - Situation Handling | You install this scope item for the situation handling steps. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/d1e9108414caba2b1c68b7dbcc89d4ea)

### Preliminary Steps

#### Create Worker (Optional)

Procedure

In this activity, you can create worker and business users in your SAP S/4HANA Cloud Public Edition system. For detailed procedure, refer to Appendix > Create Worker.

#### Manage Teams and Responsibility (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can define who should receive notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access Fiori App | Open Manage Teams and Responsibilities (F2412).Choose Create. | The Team screen displays. |  |
| 3 | Maintain Team Details | Make the following entries and choose Save:On the General Information tab:Name: Team_ContractGlobal ID:<any ID>Description: Team of ContractStatus: EnabledType: SFICATOn the Team Owners tab:Choose Create and maintain the values below:Business Partner: <Select Business Partner>On the Team Members tab:Choose Create and maintain the values below:Business Partner: <Select Business Partner who receive notification, for example, the business partner ID in previous step>Functions: SFICAUSER(Contract Accounting User) |  |  |
| 4 | Save the Team | Choose Create. | The team is created. |  |

#### Set Event-Based Situation Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure the situation type by using a template. Situation types help you manage a large variety of circumstances that are critical to your business processes by automatically notifying the correct users either as soon as the situations occur or at a defined time with error rate and mass activity type.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947). | The Manage Situation Types screen displays. |  |
| 3 | Select the Template to Copy | Choose Go.Select Template FICA_MASSACT_ERROR_RATE_AND_TIME, then choose Copy. | The Situation Type screen displays. |  |
| 4 | Maintain the Situation | Make the following entries and choose Create:ID: ZFICA_MASSACT_ERROR_TESTName: Mass Activity Exception (Rate and Time)On the Conditions tab, maintain the following entry:Error Rate (%): <Error Rate value>Mass activity type: <Select Mass activity type, For example, PAYP Payment Run>Run Time (Seconds): <Run Time value>On the Notification Recipients tab, maintain the following entry:Team Category: <Select Contract Accounting>Responsibility Definition: <Select Mass Activity Type>Member Function: <Select Contract Accounting User>Choose Create. | The situation type is maintained. |  |
| 5 | Enable This Situation Type | Choose Enable. Status changes from NO to YES. | Go back to display the Manage Situation Types screen.Click on the Situation Types tab to see the new situation type in the list. |  |

#### Manage Event-Based Situation (Optional)

Purpose

After configuring event-based situation types and setting up teams and responsibilities, execute the mass activity job to view the situation notifications.

For example, create three open documents and execute payment run (with mass activity type PAYP). To do so, please refer to the test script of the scope item 2DP: Contract Accounting – Company Initiated Payments, step Execute Payment Run.

If one of the three documents cannot be processed for payment due to issues such as a payment lock or SEPA problems, the situation notification will indicate an error rate of 33.00%.

#### Set Message-Based Situation Types (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can set situation types with run type, message ID and actions based on a standard template. Template FICA_LOCK_MESSAGE_BASED is used for the example below.

|  |
| --- |
| Example Run type PAYP and message ID >2006 (if contract account is locked by lock key, payment cannot be made) |

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F5437). | The Manage Situation Types – Message-Based screen displays. |  |
| 3 | Choose Create | Choose Create > Create Situation Type. |  |  |
| 4 | Create Situation Type | Make the following entries and choose Create:ID: <Provide ID, for example, ZFICA_MSG_BASED>Name: <Provide name>Description: <Provide description>Situation Scenario: FICA_MASSACT_MSG_MONITORSituation Template: <Choose Situation Template, for example, FICA_LOCK_MESSAGE_BASED> |  |  |
| 5 | Edit Situation Type | In the Run Types section:Run Type Items should be enabled by default, for example, MAHN, PAYP, MAKT.Maintain Filters and Messages for each Run Type item if needed.Maintain the Aggregated and Threshold for each message if needed.In the Recipients section, make the following entries:Responsibility Definition: <Select Mass Activity Type and CAStandardCompanyCode>Member Function: <Select Contract Accounting User>Choose Save and Enable. |  |  |

#### Manage Message-Based Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain Business Roles (F1492). | The Maintain Business Roles screen displays. |  |
| 3 | Create Role | Choose New and input the following information:.Business Role ID: <Provide ID> for example, Z_ SAP_FICA_BC_SIT_HANDLING_PCBusiness Role Description:<Provide description>Choose Create.Choose the Assigned Business Catalogs tab, then choose Add.Search for SAP_FICA_BC_SIT_HANDLING_PC and select it.Choose Save. | The created business role is displays. |  |
| 4 | Access the App | Open Maintain Business Users (F1303). | The Maintain Business Users screen displays. |  |
| 5 | Search Role | Search role in the search field.For example: ADMIN_APR_FICAChoose Go. | The relevant role will be listed in business users list. |  |
| 6 | Select Role | Choose role in business users list by clicking the arrow button to the right of the row. | Details of selected role are displayed. |  |
| 7 | Assign Business Role | Choose Add.Search for SAP_BR_EMPLOYEE, Z_ SAP_FICA_BC_SIT_HANDLING_PC and select them.Choose Save. | Employee - Situation Handling is assigned to role ADMIN_APR_FICA. |  |

Purpose

After setting message-based situation types with run type, message ID and actions, execute relevant mass activity job and situation notification will be shown in SAP Fiori App My Situations – Message-Based.

Procedure

For example:

1. Set run type as PAYP and message ID > 2006 (if contract account is locked by lock key, payment cannot be made).
2. Maintain contract account with payment lock (refer to Appendix > Display and Change a Contract Account).
3. Execute payment run (refer to the test script of 2DP: Contract Accounting – Company Initiated Payments, step Execute Payment Run).

After that, situation notifications can be monitored in SAP Fiori App My Situations - Extended (F4537).

#### Monitor Notification (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can monitor notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad with your user credentials as Business Process Specialist role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Situations - Extended (F4537) | The My Situations - Extended screen displays. |  |
| 3 | View Situation Details | Click on the right arrow to view situation details. | Choose the Notifications icon which is on the top right of the Home screen to see information of the situation. |  |
| 4 | Choose Action | Choose Assign to Me to check based on situation message.Choose Close Situation and select a reason for closing this situation if it is resolved, invalid or obsolete. |  |  |

#### Email Notifications for Message-Based Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can enable e-mail notification for message-based situation.

Procedure

1. Set e-mail notification for specific message type.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad with your username or e-mail address (created in prerequisite step [Create Worker (Optional)](#unique_8) [page ] 8). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types (F5437) | The Application Jobs screen displays. |  |
| 3 | Search Situation Type | Make the following entries:Situation Template: General Business-Critical Errors in Application Jobs for Contract Accounting (FICA_MASSACT_MESSAGE_BASED)Situation Scenario: FICA_MASSACT_MSG_MONITORChoose Go. |  |  |
| 4 | Choose Situation Type | Select one situation type from the list, then click the right arrow. (For example, ZFI-CA_MSG_BASED which is created in step Set Message-Based Situation Types (Optional)) |  |  |
| 5 | Set Notifications/Life Cycle | Choose message-based triggers tab, then select one item (for example, payment run).Set notifications/life cycle as 1.Choose Apply. |  |  |
| 6 | Enable Email Notifications for a Situation Type | Choose the profile icon in the top right-hand corner, then select Settings.Under Settings, select Notifications from the panel on the left side.Check the E-Mail option for the Notification Type (situation type) for which you want to receive emails.Choose Save. |  |  |

1. You can receive email by proceeding with step [Manage Message-Based Situation (Optional)](#unique_13) [page ] 12.

#### Create Provider Contract with Service Based Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Before creating a provider contract to initiate the transfer to Revenue Accounting, ensure you have completed the following steps. You may skip this if you do not have the scope item 3L3 (Contract Accounting – Contract-Based Revenue Recognition) installed.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Provider Contract.Choose the configuration step Define Specifications for Derivation of Standard Account Assignment. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 4 | Add Entry for Profit Center | Make the following entry for Sale Org 3310.Profit Center: YB900 (For example)Save the entry. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Specifications for Derivation of Standard Account Assignment | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Derivation of Standard Account Assignment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Contract: Determine Standard Account Assignment: Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entry for Sale Org 3310.Profit Center: YB900 (For example)Save the entry. | Entry for Profit Center is added. |  |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Convergent InvoicingChoose the group Integration with Contract Based Revenue Recognition.Choose the configuration step Activate Provider Contract Items for Revenue Accounting.Make sure the following entries are maintained for Sale Org 3310.Sales OrganizationDistribution ChannelDivisionSales Area 1Sales Area 2Charge TypeRev.Acctg Relevance3310*****X | The Maintain Contract: Determine Relevance to Revenue Accounting: Overview screen is displayed.Note If the key Charge Type is invisible, you can select menu More, and then select Goto > Select Keys… to make sure the field Charge Type is enabled.Please note that once the new key is active, it cannot be deactivated any more. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Provider Contract Items for Revenue Accounting | Go to the Business Processes Configuration app and search for the following activity: Activate Provider Contract Items for Revenue Accounting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Contract: Determine Relevance to Revenue Accounting: Overview screen is displayed. |  |
| 3 | Input Parameters | Make sure the following entries are maintained for Sale Org 3310.Sales OrganizationDistribution ChannelDivisionSales Area 1Sales Area 2Charge TypeRev.Acctg Relevance3310*****X | If the key Charge Type is invisible, you can select menu More, and then select Goto > Select Keys… to make sure the field Charge Type is enabled.Please note that once the new key is active, it cannot be deactivated any more. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 6: Master Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create a Business Partner](#unique_18) [page ] 22 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Business Partner (BP) | Business partner can be created with BP role MKK (contract partner). |
| [Create Customer Master Data](#unique_19) [page ] 25 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) |  |
| [Create a Contract Account](#unique_20) [page ] 26 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Contract Account (CAA3) | Contract account can be created. |
| [Create Provider Contract Via API](#unique_21) [page ] 28 |  |  | Provider Contract can be created. |

Table 7: Correspondence

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Account Statement](#unique_22) [page ] 30 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Account Statements (F3544) | Account statement can be created periodically by mass run for selected business partners. |
| [Print Correspondence](#unique_23) [page ] 32 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | Correspondence can be printed by mass run. |
| [Display Correspondences](#unique_24) [page ] 34 | Administrator - Accounts Payable and Receivable (FI-CA) | Display Correspondences (F3693) | Correspondence details can be displayed. |
| [Create Balance Notification](#unique_25) [page ] 35 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Balance Notifications (F3818) | Balance notification can be created periodically by mass run for selected business partners. |
| Print by External Service Providers |  |  |  |
| [Create Account Statement](#unique_26) [page ] 39 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Account Statements (F3544) | Account statement can be created periodically by mass run for selected business partners. |
| [Manage Output Queues for External Output Management](#unique_27) [page ] 39 | Administrator | Manage Output Queues (F7127) | Output queue can be created for External Output Management. |
| [Print Correspondence](#unique_28) [page ] 40 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | Correspondence can be printed by mass run. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Master Data

#### Create a Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a business partner for a new FI-CA customer in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Create a Business Partner | Choose Person.Or select menu Menu > Business Partner > Create > Person. | The Create Person view is displayed. |  |
| 4 | Select BP Role | Make the following entry:Create in BP role: Contract Partner | The Change to another BP role in create mode view displays. |  |
| 5 | Create | Choose Create. | The view name changes as Create Person: Role Contract Partner. Contract Partner (New) is selected for Create in BP role. |  |
| 6 | Enter Basic Data | Make the following entries:Business Partner: <Enter a specific ID>, for example, BP_AE_01Grouping: External alpha-numeric numberingNote Choose Grouping: External numeric numbering (FICA) to create sales order in scope item 43Y, for example, 10000018. |  |  |
| 7 | Enter Address Data | Make the following entry on the Address tab:First Name/Last Name: <Your first/last name>Street/House Number: <Street/House Number>Postal Code/City: Postal Code/CityCountry: AE |  |  |
| 8 | Maintain Payment Data | Note Using Internet Explorer may result in a 'session has expired' issue. Google Chrome is recommended here. Add bank details and register payment card using app Manage Business Partner Master Data.Make the following entry on the Payment Transactions tab:In the Bank Details section:ID: 01Ctry: AEBank Key: 10020030Bank acct: <Bank Account>swift code (SWIFT/BIC) : DRESDEFF827Choose Define IBAN.Check the IBAN details and choose Continue.In the Payment Cards section, input ID:ID: For example, ID001Choose Enter and make the following entry in Register Payment Card view:NoteWhen registering the payment card, there are different payment service providers (PSP) you could choose by entering the company code and Routing String as the routing parameter in the Register New Payment Card view. In SAP internal testing system,1) If you use company code as the only routing parameter, the default settings are:i. Company Code 3310 will lead to Paymetric.ii. Company Code 1710 will lead to Stripe.2) If you use the Routing String as the routing parameter, the setting is:i. Routing string ‘Stripe’ will lead to Payment Service Provider Stripe.ii. Routing string ‘Paymetric’ will lead to Payment Service Provider Paymetric.Each PSP supports its own range of processes. Regarding the impact of E2E test of FICA’s payment card settlement processes, it is recommended to use Stripe as the PSP to register the payment card.Card Type: DPAM AMEXCard Number: <16-digital card number>Note In test systems, please use the Card type and Card number as below:American Express: 378282246310005Diners Club: 30569309025904Discover: 6011111111111117JCB: 3530111333300000MasterCard: 5555555555554444Visa: 4111111111111111Name: <Enter owner's name>Valid To: <Select a date>Card Security Code: <3-digital number>Choose Submit. | The Checking reconciliation key view appears. |  |
| 9 | Maintain Credit profile | Make the following entry on the Credit Profile tab:Risk Class: <Select a risk class> |  |  |
| 10 | Save | Choose Save. | A new business partner is created. |  |

#### Create Customer Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you extend a FI-CA business partner with BP role FLCU01 with sales area master data. It is used in 43Y - Contract Accounting – Integration with Sales Documents to create sales order.

Procedures

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Select Business Partner | Make the following entry:Business Partner: <Input the business partner number created> |  |  |
| 4 | Open Business Partner | Choose Enter. |  |  |
| 5 | Switch to Change Mode | Choose Switch Between Display and Change. |  |  |
| 6 | Change in BP role | In the Change in BP role field, select Customer from the drop-down list.Note The technical key of this BP role is FLCU01. |  |  |
| 7 | Input Information for Address | Make the following entry:Correspondence lang: <EN> |  |  |
| 8 | Open Sales Area | Choose Sales and Distribution at the top of the view. | The Sales Area view appears. |  |
| 9 | Enter Sales Area Data | Enter the following data:Sales Org.Distr. ChannelDivisionAfter entering these fields, press Enter and then choose Save.Note These three entries (Sales Organization, Distribution Channel, and Division) form the sales area. In many cases, the sales area sets the Purpose for sales processing, for example, within the sales order or pricing. | The changes are saved for the business partner. |  |
| 10 | Enter Shipping Data | On the Shipping tab page in the Shipping section, enter the following data:Delivering Plant |  |  |
| 11 | Enter Billing Data | On the Billing tab page in the Delivery and Payment Terms section, make the following entries:Incoterms: <EXW>Incoterms Location 1: <for example, Shanghai> |  |  |
| 12 | Enter Tax Data | On the Billing tab page, in the Output Tax section, enter the following data:tax classification: <1>For example, value <1> means that this customer is fully taxable. |  |  |
| 13 | Save Your Data | Save your entries. |  |  |

#### Create a Contract Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create contract account master data for an FI-CA customer in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account (CAA3).Note You can also use the SAP Fiori App Manage Contract Accounts - Deprecated (F5474) to create or change the contract accounts. | The Contract Account Display: Initial Screen displays. |  |
| 3 | Create a Contract Account | Choose Create.Or select menu Menu > Contract Account > Create . | The Contract Account Create: Initial Screen displays. |  |
| 4 | Enter Basic Data | Make the following entry:Contract Acct: <Enter a specific ID>, for example, CA_AE_01Business Partner: <Select business partner number created in step Create a Business Partner>Cont. Acct. Cat.: Y1Valid From: <Today's date> |  |  |
| 5 | Maintain Contract Account details | Choose Continue. | The Contract Account Create: General Data screen displays. |  |
| 6 | Enter General Data | Make the following entry on the General tab:Cont. Acct Name: <Contract account name>Acct. Relation.: Account HolderTolerance Group: Y001 Tolerance not permittedPlanning Group: Domestic customersNote With Maintain Planning Group, you can use cash reports for cash daily operation. (see the Advanced Cash Operations (J78) test script for more information).Payment cond.: YN01Act Determ. ID: Y1 |  |  |
| 7 | Enter Payments/Taxes Data | Make the following entry on the Payments/Taxes tab:Company Code Gp: 3310Standard CoCode: 3310Business Place: <select value from the drop-down list> |  |  |
| 8 | Enter Dunning/Correspondence | Make the following entry on the Dunning/Correspondence tab:Corresp. Variant: <only printout, immediately> |  |  |
| 9 | Save | Choose Save. | A new contract account is created. |  |

#### Create Provider Contract Via API

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a provider contract for a new FI-CA customer in SAP S/4HANA Cloud Public Edition. You would create provider contract either with billing plan or without billing plan. In this chapter, we introduce an example of creating a provider contract without billing plan via SAP API.

Prerequisite

Make sure you have set up communication SAP_COM_0167. After that, you can create a provider contract via API by sending an http request. For more information about communication scenario SAP_COM_0167, please refer to the set-up guide of 2AR: Contract Accounting – Master Data and Basic Functions.

Procedure

In this step, you create provider contracts by invoking the SOAP API for provider contract.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API hub home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API Package | Choose SAP S/4HANA Cloud Public Edition as Source to locate the SAP S/4HANA Cloud Public Edition API package. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search Out Provider Contract SOAP API | Make Provider Contract as search key to locate the API packages that are relevant to Provider Contract. Then choose Provider Contract - Manage.Note You can follow the detailed instructions and generate your specific http request for your provider contract creation, below is one example http request for the scenario: create a provider contract. You may exchange variables in curly brackets based on your environment. | The create Provider Contracts SOAP API is displayed. |  |

|  |
| --- |
| Sample CodePOST / HTTP/1.1 Host: {{host}}{{serviceURL}} <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:glob="http://sap.com/xi/SAPGlobal20/Global"> <soapenv:Header/> <soapenv:Body> <glob:ProviderContractCreateRequest_sync> <MessageHeader> <CreationDateTime>2020-11-17T07:49:56.921Z</CreationDateTime> </MessageHeader> <ProviderContract> <Header> <Identification> <InternalID>API1605599220999</InternalID> </Identification> <BusinessPartner> <InternalID>{{BusinessParter}}</InternalID> </BusinessPartner> <CAProviderContractName>PCNAME</CAProviderContractName> <CAPrvdrContrStartDateTime timeZoneCode="CET">2018-11-17T07:47:00.996Z</CAPrvdrContrStartDateTime> <CAPrvdrContrEndDateTime timeZoneCode="CET">9999-12-31T23:59:59Z</CAPrvdrContrEndDateTime> <CAPrvdrContrActivationDateTime timeZoneCode="CET">2018-11-17T07:47:00.996Z</CAPrvdrContrActivationDateTime> <CAPrvdrContrChangedDateTime timeZoneCode="CET">2020-11-17T07:49:56.921Z</CAPrvdrContrChangedDateTime> <CAProviderContractStatus/> </Header> <ProviderContractItem> <CAProviderContractItemUUID>12080AD4DC804190B156F127A4BDBFA0</CAProviderContractItemUUID> <CAPrvdrContrItmValidToDateTime timeZoneCode="CET">9999-12-31T23:59:59Z</CAPrvdrContrItmValidToDateTime> <CAProviderContractItemText>TEST Text</CAProviderContractItemText> <SalesOrganisation>3310</SalesOrganisation> <DistributionChannelCode>10</DistributionChannelCode> <Product>CBPTS001</Product> <CABillgCycle/> <ServiceRecipient> <InternalID/> </ServiceRecipient> <EndOfDurationDateTime timeZoneCode="CET">2022-11-17T07:47:00.998Z</EndOfDurationDateTime> <ContractAccount> <InternalID>{{ContractAccount}}</InternalID> </ContractAccount> </ProviderContractItem> </ProviderContract> </glob:ProviderContractCreateRequest_sync> </soapenv:Body> </soapenv:Envelope> |

### Correspondence

#### Create Account Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you prepare account statement correspondence for FI-CA business partners in SAP S/4HANA Cloud Public Edition.

Prerequisite

Before you create account statement, execute Post Document first (refer to the test script of the scope item 2UJ: Contract Accounting – Open Item Management-Preliminary Steps-Post Documents).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Account Statements (F3544). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Generate Account StatementsJob Name: FI-CA: Generate Account Statements |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select> |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0Simulation Run: <Unselect>In the Selection Criteria section:Business Partner: <Select business partner number>Cont.Account: <Select contract account number>Company Code: 3310In the Further Settings section:Date of Issue: <Issue date of document, today's date by default>Posting Date: <Posting date of document, today's date by default>Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays. One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Print Account Statement

##### Print Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you print FI-CA correspondence in SAP S/4HANA Cloud Public Edition, for example, a business partner account statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select>Define Recurrence Pattern:Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle. |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0In the Selection Criteria section:Business Partner: <Select business partner number>Cont.Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0002 Account Statement>In the Print Parameter section:Actual Print: <Select> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Display Correspondences

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display correspondence details in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Correspondences (F3693). | The Display Correspondences screen displays. |  |
| 3 | Search Criteria | Enter required parameters. |  |  |
| 4 | Execute | Choose Go. | The correspondence details are listed. |  |
| 5 | Display | Select an entry. | The details for this entry are shown. |  |

#### Create Balance Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you prepare balance notification correspondence for FI-CA business partners in SAP S/4HANA Cloud Public Edition.

Prerequisite

Before you execute Create Balance Notification, execute Post Document first (refer to the test script of the scope item 2UJ: Contract Accounting – Open Item Management, step Post Documents under Preliminary Steps).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Balance Notifications (F3818). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Create Balance NotificationJob Name: FI-CA: Create Balance Notification |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select> |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0Simulation Run: <Unselect>In the Selection Criteria section:Company Code: 3310Business Partner: <Select business partner number>Cont.Account: <Select contract account number> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays. One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Print Balance Notification

##### Print Correspondence

Context

In this activity, you print the balance notification correspondence. For detailed procedures, see [Print Correspondence](#unique_23) [page ] 32.

|  |
| --- |
| Note For Correspondence Type, select 0026 Balance Notification. |

##### Display Correspondences

Context

In this activity, you print the balance notification correspondence. For detailed procedures, see [Display Correspondences](#unique_24) [page ] 34.

|  |
| --- |
| Note For Correspondence Type, select 0026 Balance Notification Display Correspondence. |

#### Create Contract Confirmation Letter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, contract confirmation letter is created by creating provider contract.

Prerequisite

Before you create contract confirmation letter, maintain FIN_CA_CONTRACT_CONFIRMATION as form template ID/email template ID for correspondence type 0050 via configuration activity: Define Form Template for Correspondence (102223).

Procedure

Create provider contract to trigger contract confirmation letter (refer to the test script of the scope item 2AR Contract Accounting – Master Data and Basic Functions, chapter [Create Provider Contract via API](#unique_21).)

#### Print Contract Confirmation Letter

##### Print Correspondence

Context

In this activity, you print the contract confirmation letter. For detailed procedures, see [Print Correspondence](#unique_23) [page ] 32.

|  |
| --- |
| Note For Correspondence Type, select 0050 Contract Confirmation. |

##### Display Correspondences

Context

In this activity, you print the contract confirmation correspondence. For detailed procedures, see [Display Correspondences](#unique_24) [page ] 34.

|  |
| --- |
| Note For Correspondence Type, select 0050 Contract Confirmation. |

#### Print by External Service Providers

Context

In this activity, you can provide raw data for correspondence printing to external service providers.

Prerequisite

1. Configure the communication scenario SAP_COM_0466 (refer to the set-up instruction of the scope item 2AR Contract Accounting – Master Data and Basic Functions).
2. Create a print queue in PDF format and install SAP Cloud Print Manager for Pull Integration (refer to the set-up instruction of the scope item 1LQ Output Management for steps Maintaining a Print Queue and Installing and Setting Up SAP Cloud Print Manager for Pull Integration).
3. Configuration activity Configure Correspondence Variants (107026): Change send control YOMS on Correspondence Variant S001 and Correspondence Type 0002 Account Statement.
4. Maintain Contract Account with Correspondence Variant S001 (refer to step Display and Change a Contract Account in Appendix)

Procedure

Execute Create Account Statement and Print Account Statement (refer to the test script of the scope item 2AR Contract Accounting – Master Data and Basic Functions, chapter Print Account Statement.)

##### Create Account Statement

Procedure

In this activity, you can create account statement. To do so, refer to the test script of the scope item 2AR Contract Accounting – Master Data and Basic Functions, step Create Account Statement.

##### Manage Output Queues for External Output Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create the output queue for External Output Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Output Queues (F7127). |  |  |
| 3 | Create Queue | On the Manage Output Queues screen, choose Create and make bellow entries:Queue: Queue_EXTOMDescription: for EXTOM channelChoose Continue. |  |  |
| 4 | Create Queue Settings | On the Manage Output Queues screen, go to the Queue Settings and make the following entries:Transfer Type: Single TransferQueue Owner: Select from F4 to choose the valueRetention Period (Days): 30 (for example) |  |  |
| 5 | Choose Create | Choose Create. | The queue has been created successfully. |  |

##### Print Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can print FI-CA correspondence in SAP S/4HANA Cloud Public Edition, for example, a business partner account statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Print Correspondence (F3537). |  |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select>Define Recurrence Pattern:Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle. |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0In the Selection Criteria section:Business Partner: <Select business partner number>Cont.Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0002 Account Statement>In the Print Parameter section:Output Channel: <Select External Output Management>Print Queue Name: <Select print queue>Output Queue: <Select Output Queue created in step Print by External Service Providers - Create Account Statement>Actual Print: <Select> |  |  |
| 7 | Check Job | Choose Check. | System message: You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

## Appendix

### Process Integration

Process included in this document is part of a chain of integrated processes.

#### Display and Change a Business Partner

Context

In this activity, you can display and change an existing business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen displays. |  |
| 3 | Enter Business Partner Number | Make the following entry and choose Enter:Business Partner: <business partner number in step Create a Business Partner> | The Display Person : Business Partner Number screen displays. |  |
| 4 | Switch to Change | Choose Switch Between Display and Change. | The Change Person : Business Partner Number screen displays. |  |
| 5 | Enter Change | Make the following entry:Search Term 1/2: Change BP |  |  |
| 6 | Save | Choose Save. | The change has been saved. |  |

#### Display and Change a Contract Account

Context

In this activity, you display and change an existing contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Contract Account (CAA3). | The Contract account Display: Initial Screen displays. |  |
| 3 | Enter Contract Account Number | Make the following entry and choose Continue:Contract Acct: <contract account number in step Create a Contract Account> | The Contract account Display: General Data screen displays. |  |
| 4 | Back | Choose Back. | The Contract account Display: Initial Screen displays again. |  |
| 5 | Switch to Change | Choose Change and check the following entry:Contract Acct: <contract account number> | The change mode is on. |  |
| 6 | Continue | Choose Continue. | The Contract account Change: General Data screen displays. |  |
| 7 | Enter Change | Make the following entry:Cont. acct name: Change CA |  |  |
| 8 | Save | Choose Save. | The change has been saved. |  |

Alternatively, you can display or change an existing contract account, or create a new contract account by using the SAP Fiori app Manage Contract Accounts (F5474A).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract Accounts (F5474A). | The Manage Contract Accounts: Initial Screen displays. |  |
| 3 | Enter Contract Account Number | Make the following entry:Contract Acct: <contract account number> |  |  |
| 4 | Go | Choose Go. | The corresponding contract account is listed in the Contract Accounts section.Click the right arrow icon to view or edit the specific contract account details.You can also create a new contract account by clicking the New button or by using the reference.Note You can create or edit the contract account and save it as draft. |  |
| 5 | Edit Contract Account Details as Future Planned Change (Optional) | Click the right arrow icon to view or edit the specific contract account details. | Click the Edit as Planned Change button in the upper-right corner. In the dialog box that appears, select the appropriate validity date.You can view planned changes to this contract account by clicking the Display Planned Changes button, which appears when planned changes are available. |  |

#### Display Provider Contract

Context

In this activity, you display or change a provider contract for a new FI-CA customer in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Provider Contract (FP_VT3). | The Provider Contract Display: Initial Screen is displayed. |  |
| 3 | Enter Basic Data | Make the following entries:Provider Contract: <Enter a specific ID>Business Partner: <Enter a specific ID> for example, BP_AE_01 |  |  |
| 4 | Execute | Choose Display/Change in Display/Change mode, then choose Continue. | The Provider Contract Display/Change screen is displayed. |  |

#### Overview of Contracts and Contract Items

Context

In this activity, you display overview of contracts and contract items for a new FI-CA customer in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Provider Contracts (FP_VT0). | The Overview of Contracts and Contract Items screen is displayed. |  |
| 3 | Enter Basic Data | Make the following entries:Provider Contract: <Enter a specific ID>Business Partner: <Enter a specific ID> for example, BP_AE_01 |  |  |
| 4 | Execute | Choose Execute. | A contract overview is displayed. |  |

#### Create Worker

Context

In this activity, you can create workers and business users in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Service Level Agreements (F6183A). |  |  |
| 3 | Download Templete | Choose the Import button and choose Import Worker and Work Agreement Data (Basic Import).Select Delimiter: CommaChoose link Download Templates to download template.csv. |  |  |
| 4 | Fill Values in Downloaded Templete | Fill in the template with the following values:WorkerID: <your user ID>User Name: <your user ID>WorkerType: BUP003First Name: <your first name>Last Name: <your last name>Email Address: <your email address>Company Code: 3310Cost Center: 33101501Start Date: <20160805>End Date: <99991231> |  |  |
| 5 | Upload Template | Choose Import > Import Worker and Work Agreement Data (Basic Import).Select Delimiter: CommaImport Data(.csv): <choose filled template>Import Name: <enter the name> |  |  |
| 6 | Import | Choose Import. | Application logs is displayed. |  |
| 7 | Search Worker | Input user ID and choose Go.Note Note down the Business Partner ID. | Worker is listed. |  |
| 8 | Maintain Business User to Selected Worker | Assign role to selected worker by clicking the Maintain business user button.Choose the Assigned Business roles tab, click Add and search the following Business Role ID:SAP_BR_ADMIN_APR_FICASAP_BR_ADMINISTRATORSAP_BR_APR_ACCOUNTANT_FICASAP_BR_BPC_EXPERTSAP_BR_BUSINESS_PROCESS_SPECSAP_BR_EMPLOYEEChoose OK. |  |  |

#### Data Privacy

Prerequisite

1. Maintian Audit Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: Application Platform and InfrastractureSub Application Area: Retention ManagementSelect the row with Item Name: SettingsChoose the configuration step Maintain Audit Area.Choose Configure. | The Change View "Maintain Audit Area": screen displays. |  |
| 4 | Choose Audit Area | Make the following entries:Audit Area: BUPA_DP with Policy Category: RSTAudit Area: BUPA_DP with Policy Category: RTP |  |  |
| 5 | Save | Choose Save. | System message Data has been saved is displayed. |  |

1. Assign ILM Object to Audit Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: Application Platform and InfrastractureSub Application Area: Retention ManagementSelect the row with Item Name: SettingsChoose the configuration step Assign ILM Object to Audit Area.Choose Configure. | The Change View"Assign ILM Objects to Audit Area": screen displays. |  |
| 4 | Choose Policy Category and Audit Area | Make the following entries:Policy Category: RST Residence RulesAudit Area: BUPA_DPChoose Run. | The Change View "Assign ILM Objects to Audit Area": screen displays, ILM Object in Audit Area section is shown below. |  |
| 5 | Active ILM Object | In ILM Object in the Audit Area section, add ILM object:ILM Object: CA_BUPAStatus: ActiveChoose Save. | System message Data has been saved is displayed. |  |
| 6 | Choose Policy Category and Audit Area | Click on Back arrow to go back to screen Assign ILM Objects to Audit Area.Make the following entries:Policy Category: RTP Retention RulesAudit Area: BUPA_DPChoose Run. | The Change View "Assign ILM Objects to Audit Area": screen displays. |  |
| 7 | Active ILM Object | In ILM Object in the Audit Area section, add ILM object:ILM Object: CA_BUPAStatus: Active | The Change View "Assign ILM Objects to Audit Area": screen displays, ILM Object in the Audit Area section is shown below. |  |
| 8 | Save | Choose Save. | System message Data has been saved is displayed. |  |

1. Maintain ILM Policies and Rules

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: Application Platform and InfrastractureSub Application Area: Retention ManagementSelect the row with Item Name: SettingsChoose the configuration step Maintain ILM Policies and Rules.Choose Configure. | The Change View "Maintain ILM Policies and Rules": screen displays. |  |
| 4 | Choose Policy Category and Audit Area | Make the following entries:Policy Category: RST Residence RulesAudit Area: BUPA_DPILM Object: CA_BUPAChoose Run. | The Change View "Maintain ILM Policies and Rules" screen displays. Polices section is shown below. |  |
| 5 | Add Policies | In the Policies section, add policies by choosing New entries in the upper left corner:Policy: FICA_TEST1Status: Not LiveChoose Save. | System message Data has been saved is displayed. |  |
| 6 | Add Condition Fields | Choose Condition Field in the Dialog Structure on the left panel and add:Position: 0001Condition Field: APPL_NAMEPosition: 0002Condition Field: APPL_RULE_VARIANTChoose Save. | System message Data has been saved is displayed. |  |
| 7 | Add Residence Rules | Choose Residence Rules in the Dialog Structure on the left panel and add Residence Rules:Number: 000001Residence Period: 1Time Unit: DAYTime Reference: START_RET_DATETime Offset: END_OF_MONTHChoose Save. | System message Data has been saved is displayed. |  |
| 8 | Add Condition Field Values | Choose Condition Field Values in the Dialog Structure on the left panel and add Condition Field Values:Condition Field: APPL_NAMEFrom: MKKCondition Field: APPL_RULE_VARIANTFrom: FICA_NO_BUSIChoose Save. | The Change View "Assign ILM Objects to Audit Area": screen displays. |  |
| 9 | Set Live on Policy | Change policy FICA_TEST1 Status to Live. |  |  |
| 10 | Add Policies | In the Policies section, add policies by choose New entries in the upper left corner:Policy: FICA_TEST2Status: Not LiveChoose Save. | System message Data has been saved is displayed. |  |
| 11 | Add Condition Fields | Choose Condition Field in the Dialog Structure on left panel and add condition fields:Position: 0001Condition Field: APPL_NAMEPosition: 0002Condition Field: APPL_RULE_VARIANTChoose Save. | System message Data has been saved is displayed. |  |
| 12 | Add Residence Rules | Choose Residence Rules in the Dialog Structure on left panel and add Residence Rules:Number: 000001Residence Period: 1Time Unit: DAYTime Reference: START_RET_DATETime Offset: END_OF_MONTHChoose Save. | System message Data has been saved is displayed. |  |
| 13 | Add Condition Field Values | Choose Condition Field Values in the Dialog Structure on left panel and add Condition Field Values:Condition Field: APPL_NAMEFrom: BUPChoose Save. | System message Data has been saved is displayed. |  |
| 14 | Set Live on Policy | Change policy FICA_TEST2 Status to Live. |  |  |
| 15 | Create Two More Policies | Click on Back arrow to go back to screen Maintain ILM Policeis and Rules.Make the following entries:Policy Category: RTP Retention RulesAudit Area: BUPA_DPILM Object: CA_BUPAChoose Run.Follow step 5-14 to add two policies and set status to Live. | System message Data has been saved is displayed. |  |

##### Analyze Business Partner Data

Context

In this activity, you analyze whether business partner data can be deleted to satisfy data privacy constraints in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Data Privacy Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Simulate Bus.Partner Can Be Blocked (FPDPR_BP_SIM_ALL). | The Data Protection: Analysis of Business Partner Data screen displays. |  |
| 3 | Enter Required Parameters | Make the following entries:Business Partner: <Select business partner number>Action: <Select action type for check>Note Possible actions are End of Open Business Transactions and Determination of End of Purpose. |  |  |
| 4 | Execute | Choose Execute. | The Display Logs screen displays. Details of the result are displayed for analysis. |  |

##### Check Business Partner Can Be Blocked

Context

In this activity, you check whether business partner data can be blocked in SAP S/4HANA Cloud Public Edition.

Prerequisite

Access configuration activity: Specify Determination of Rule Variants for Data Protection in FI-CA (102286): maintain application object *, company code * and rule variant FICA_NO_BUSI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Data Privacy Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Check Business Partner Can Be Blocked (F3543). | The Application Jobs screen displays. |  |
| 3 | Choose New | On the Application Jobs screen, choose Create. | The New Job screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries:Start Immediately: <Select>Run ID Prefix: For example, ID0Simulation: <Unselect>Chk on Threshhold Val. or Bef.: <retention start date or later>Business Partner: <Select business partner number>Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 7 | Execute Job | Navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Block Business Partner

Context

In this activity, you block the business partner data in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Data Privacy Specialist role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Block Master Data - Business Partner (BUPA_PRE_EOP) |  |  |
| 3 | Enter Required Parameters | Make the following entries:Partner: <Select business partner number>Check End of Purpose: <Select>Overall: <Select>Consider next check date: <Unselect>Test Mode: <Unselect> |  |  |
| 4 | Execute | Choose Execute. | Blocking process starts. |  |

#### Delete Test Data

Context

In this activity, you can only delete test data in testing system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access the SAP Fiori App | Open Delete Test Data (F7691). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Delete Test DataJob Name: Delete Test Data |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Selection Criteria section:Company Code: 3310or choose All Company codes.Simulation: <Unselect> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Execute Job | Navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no error. |  |

#### Display Processing Locks

Context

In this activity, you can view processing locks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access the SAP Fiori App | Open Display Processing Locks (F8302). | The Processing Locks screen displays. |  |
| 3 | Enter Basic Parameters | Make the following entries:Lock Object Category: <Choose any Lock Object Category> |  |  |
| 4 | Execute | Choose Go. | The Processing Locks are shown in the list. |  |
| 5 | Display Details | Choose the right arrow button to the right of the Processing Locks line item. | The Processing Locks details are displayed. |  |

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
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-integration-with-sales-documents-43y-a]]
- see-also :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2AR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 85,533 chars in the whole document
