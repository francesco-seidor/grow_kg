---
id: 04-tax-and-statutory-reporting/test-script-external-tax-audit-2oo-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: External Tax Audit (2OO_AE) - SAP S/4HANA Cloud Public Edition (2OO_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2OO_AE External Tax Audit: auditor roles, time restrictions, audit filters, Auditor Direct Access, tax reconciliation reports."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/external-tax-audit-and-auditor-access]
aliases: [2OO_S4CLD2608_BPD_EN_AE]
keywords: [External Tax Audit and Auditor Access, external tax audit, auditor direct access, external auditor role, time restrictions, generic audit filter, audit structures, professional service audit, sox compliance audit, audit journal]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-845
topic: 04-tax-and-statutory-reporting/external-tax-audit-and-auditor-access
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: External Tax Audit (2OO_AE) - SAP S/4HANA Cloud Public Edition (2OO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **External Tax Audit and Auditor Access** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | External Tax Audit (2OO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849685)

[2 Prerequisites 4](#_Toc232849686)

[2.1 System Access 4](#_Toc232849687)

[2.2 Roles 4](#_Toc232849688)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849689)

[2.4 Business Conditions 5](#_Toc232849690)

[3 Overview Table 6](#_Toc232849691)

[4 Test Procedures 8](#_Toc232849692)

[4.1 Timeframe and Data Restrictions 8](#_Toc232849693)

[4.1.1 External Auditor Restrictions 8](#_Toc232849694)

[4.1.1.1 Maintain Time Restrictions 8](#_Toc232849695)

[4.1.2 Generic Audit Filter (GAF) 10](#_Toc232849696)

[4.1.2.1 Configure Generic Audit Filter 10](#_Toc232849697)

[4.1.2.2 Manage Generic Audit Filter Users 12](#_Toc232849698)

[4.2 Auditor Direct Access 13](#_Toc232849699)

[4.2.1 Create Audit with Default Audit Structure 13](#_Toc232849700)

[4.2.2 Run Reports and Transactions Listed in Audit Structure 13](#_Toc232849701)

[4.2.3 Display Audit Log 15](#_Toc232849702)

[4.3 Auditor Direct Access for Professional Service 16](#_Toc232849703)

[4.3.1 Create Audit with Audit Structure for Professional Service 16](#_Toc232849704)

[4.3.2 Run Reports and Transactions Listed in Audit Structure 16](#_Toc232849705)

[4.3.3 Display Audit Log 18](#_Toc232849706)

[4.4 Auditor Direct Access for SOX Compliance Auditing 19](#_Toc232849707)

[4.4.1 Create Audit with Audit Structure for SOX Compliance 19](#_Toc232849708)

[4.4.2 Run Reports and Transactions Listed in Audit Structure 19](#_Toc232849709)

[4.4.3 Display Audit Log 20](#_Toc232849710)

[4.5 Periodic Activities 22](#_Toc232849711)

[4.5.1 Audit Journal 22](#_Toc232849712)

[4.5.2 Tax Reconciliation Account Balance 23](#_Toc232849713)

[4.5.3 Tax Declaration Reconciliation 24](#_Toc232849714)

## Purpose

Overview

The External Tax Audit functions enable external tax auditors to conduct detailed audits of a company's accounts using Auditor Direct Access. Auditors can access the data in read-only mode, meaning that they can select, filter, and sort using the taxpayer's hardware and software.

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
| External Auditor | SAP_BR_EXTERNAL_AUDITOR | External Auditing / External Auditing - Data Privacy | SAP_BR_EXTERNAL_AUDITOR / SAP_CA_SPT_EXTERNAL_AUDITOR_PC |  |

### Master Data, Organizational Data, and Other Data

Essential master and organizational data was created in your SAP S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code 3310 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2OO - External Tax Audit | At least one of the following business catalogs must be assigned:SAP_FIN_BC_GL_AUDIT_PCSAP_FIN_BC_GL_AUDIT_MASK_PCSAP_FIN_BC_GL_AUDIT_DSHBRD_PC |

|  |
| --- |
| Note At the beginning of an audit, you must select the required audit structure. Audit structures contain the information required to carry out the audit. The business catalogs determine which audit structure is available to the external auditor:Table 1:Business CatalogApp/TransactionAudit StructureSAP_FIN_BC_GL_AUDIT_PCAuditor Direct Access - External Tax Audit (S4H_AUDIT_TAX)S4H_AUDIT_TAXSAP_FIN_BC_GL_AUDIT_MASK_PCAuditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS)S4H_AUDIT_TAX_PSSAP_FIN_BC_GL_AUDIT_DSHBRD_PCAuditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD)S4H_AUDIT_DASHBOARD |

## Overview Table

The External Tax Audit scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Time Restrictions](#unique_8) [page ] 8 | Administrator | Maintain Business Roles (F1492) | Time restrictions are maintaineded for the new business role. |
| [Configure Generic Audit Filter](#unique_9) [page ] 10 | Administrator | Manage Generic Audit Filter (F7285) | The audit filter is created successfully. |
| [Manage Generic Audit Filter Users](#unique_10) [page ] 12 | Administrator | Manage Generic Audit Filter Users (F7503) | The audit filter is assigned to the user and is activated. |
| Auditor Direct Access with Default Audit Structure |  |  |  |
| [Create Audit with Default Audit Structure](#unique_11) [page ] 13 | External Auditor | Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX) | The cockpit transaction S4H_AUDIT_TAX (for navigation in the Audit Information System Workplace) opens and allows the auditor to create a new audit with check number. |
| [Run Reports and Transactions Listed in Audit Structure](#unique_12) [page ] 13 | External Auditor | Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX) | Reports and transactions are executed in display mode. Audit notes can be maintained. |
| [Display Audit Log](#unique_13) [page ] 15 | External Auditor | Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX) | An audit log is maintained for each audit. Audit steps can be displayed. |
| Auditor Direct Access for Professional Service |  |  |  |
| [Create Audit with Audit Structure for Professional Service](#unique_14) [page ] 16 | External Auditor | Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS) | The cockpit transaction S4H_AUDIT_TAX_PS (for navigation in the Audit Information System Workplace) opens and allows the auditor to create a new audit with check number. |
| [Run Reports and Transactions Listed in Audit Structure](#unique_15) [page ] 16 | External Auditor | Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS) | Reports and transactions are executed in display mode. Audit notes can be maintained. |
| [Display Audit Log](#unique_16) [page ] 18 | External Auditor | Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS) | An audit log is maintained for each audit. Audit steps can be displayed. |
| Auditor Direct Access for SOX Compliance Auditing |  |  |  |
| [Create Audit with Audit Structure for SOX Compliance](#unique_17) [page ] 19 | External Auditor | Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD) | The cockpit transaction S4H_AUDIT_DASHBOARD (for navigation in the Audit Information System Workplace) opens and allows the auditor to create a new audit with check number. |
| [Run Reports and Transactions Listed in Audit Structure](#unique_18) [page ] 19 | External Auditor | Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD) | Reports and transactions are executed in display mode. Audit notes can be maintained. |
| [Display Audit Log](#unique_19) [page ] 20 | External Auditor | Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD) | An audit log is maintained for each audit. Audit steps can be displayed. |
| Periodic Activities |  |  |  |
| [Audit Journal](#unique_20) [page ] 22 | External Auditor | Audit Journal (F0997) | The report displays all system terminations that occur within a given time period. |
| [Tax Reconciliation Account Balance](#unique_21) [page ] 23 | External Auditor | Tax Reconciliation Account Balance (F2095) | The Account Balances for Journal Entries with Tax Codes list is created. |
| [Tax Declaration Reconciliation](#unique_22) [page ] 24 | External Auditor | Tax Declaration Reconciliation (F2096) | The Tax Boxes and Tax Codes list is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Timeframe and Data Restrictions

#### External Auditor Restrictions

##### Maintain Time Restrictions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you set up the permissions for the restricted auditor role and maintain time restrictions. You can maintain key dates to restrict the visibility of data.

|  |
| --- |
| Caution Auditors can access data in read-only mode. For the time restriction and data redaction to function properly, you must not assign any additional business catalogs to the External Auditor. |

To view a list of reports which support the time restriction feature, please refer to [External Tax Audit](https://help.sap.com/viewer/fd849abf7f5441d9bcc148200b0d22fe/latest/en-US/4d72a7ce5ab546d5a5822efb63d190d2.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open Maintain Business Roles (F1492). | The Maintain Business Role screen displays. |  |
| 3 | Copy Role | Select the SAP business role template External Auditor (SAP_BR_EXTERNAL_AUDITOR) and choose Copy. | The Copy Business Role dialog box displays. |  |
| 4 | Create New Role | In the Copy Business Role dialog box, make the following entries and choose OK:New Business Role ID: for example, ZSAP_BR_EXTERNAL_AUDITOR_2OONew Business Role Description: for example, Z_EXTERNAL_AUDITOR_2OOAssigned Business Catalogs: SelectedRestrictions: Deselected | The new business role is created. |  |
| 5 | Remove Catalogs | On the Assigned Business Catalogs tab, select all business catalogs except for the following:External Audit - Tax Audit Masking (SAP_FIN_BC_GL_AUDIT_MASK_PC)Note Use the catalog above to enable time restrictions for Auditor Direct Access for Professional Service.For Auditor Direct Access, use External Audit - Tax Audit (SAP_FIN_BC_GL_AUDIT_PC).For Auditor Direct Access for SOX Compliance Auditing, use External Audit - Audit Dashboard (SAP_FIN_BC_GL_AUDIT_DSHBRD_PC).Master Data - Business Partner Masking Display (SAP_CMD_BC_BP_MASK_DSP_PC)Master Data - Customer Masking Display (SAP_CMD_BC_CUST_MASK_DSP_PC)Master Data - Supplier Masking Display (SAP_CMD_BC_SUPP_MASK_DSP_PC)Choose Remove. | The catalogs are removed from the Assigned Business Catalogs tab. |  |
| 6 | Add Business User | On the Assigned Business Users tab, choose Add. | The Add Business Users dialog box displays. |  |
| 7 | Assign Business User | Select the business users you would like to assign to the role from the list and choose OK. | The business users are assigned to the business role.Caution The business user should only be assigned the to External Auditor role.Do not assign additional roles to the business user. |  |
| 8 | Maintain Restrictions | At the top of the screen, choose Maintain Restrictions. |  |  |
| 9 | Maintain Restrictions | On the Write, Read, Value Help tab, set Write, Read, Value Help to No Access. |  |  |
| 10 | Maintain Restrictions | On the Read, Value Help tab, set Read, Value Help to Restricted.Select Restrictions and Values and choose Unrestricted Access.Choose Yes. |  |  |
| 11 | Edit Restrictions | On the Read, Value Help tab, locate the Key Date field and choose Edit. | The Edit Read Restrictions for Key Date dialog box displays. |  |
| 12 | Restrict Authorization | Choose Add.Make the following entries and choose OK:From: <start date>To: <end date> |  |  |
| 13 | Save | Choose Back and Save. | The time restriction is saved for the new business role. |  |

#### Generic Audit Filter (GAF)

##### Configure Generic Audit Filter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an audit filter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open Manage Generic Audit Filter (F7285). | The Configure Generic Audit Framework screen displays. |  |
| 3 | Create Filter | Choose Edit.Choose Create.Make the following entries and choose Continue:Audit Filter Name: <name>Filter Description: <description> | The Filter Value Definition Projection View screen displays. |  |
| 4 | Create Filter Fields | In the Filter Fields secction, choose Create.Make the following entries and choose Continue:Logical Field Name: COMPANY_CODEValue - Low: 3310Choose Apply. |  |  |
| 5 | Create Filter Fields | In the Filter Fields secction, choose Create.Make the following entries and choose Continue:Logical Field Name: AUDIT_PERIODValue - Low: <enter a date with the format YYYYMMDD>Choose Apply.For the AUDIT_PERIOD logical field, make the following entries:Value - High: <enter a date with the format YYYYMMDD> |  |  |
| 6 | Create Filter Fields | In the Filter Fields secction, choose Create.Make the following entries and choose Continue:Logical Field Name: LEDGERValue - Low: for example, 0LChoose Apply. |  |  |
| 7 | Save Audit Filter | At the bottom of the screen, choose Save.Note Whenever you save an audit filter, all other audit filters maintained by the application are saved. | The audit filter is created successfully. |  |

##### Manage Generic Audit Filter Users

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign a user to your audit filter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access App | Open Manage Generic Audit Filter Users (F7503). | The Manage Generic Audit Users screen displays. |  |
| 3 | Create Assignment | Choose Create.Make the following entries and choose Continue:User: <user>Audit Filter Name: <audit filter> | The Filter Assignment screen displays. |  |
| 4 | Assign Audit Filter | Choose Create.Choose Activate. | The audit filter is assigned to the user and is activated. |  |

### Auditor Direct Access

#### Create Audit with Default Audit Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you open the Audit Information System Workplace cockpit and create an audit with default audit structure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX). | The Audit Information System Workplace screen displays. |  |
| 3 | Create Audit | In the Audit Selection section, make the following entries and choose Audit (CTRL + F2):Check Number: Any numeric value (for example, 2021) | A new audit (with audit structure and check number) is created. The system displays the message Audit S4H_AUDIT_TAX XXXX created. |  |

#### Run Reports and Transactions Listed in Audit Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the reports and transactions defaulted from the audit structure S4H_AUDIT_TAX. You can also maintain audit notes, audit process status, and so on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_TAXCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_TAX – XXXX screen displays, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Report or Transaction Listed in Audit | Select a transaction or report from the left-hand side of the screen under the Audit Structure and double-click Execute (clock icon):As an example, if you choose Compact Document Journal, make the following entries and choose Execute:Company Code: 3310Fiscal Year: <fiscal year>Ledger: <ledger> | The selected transaction or report opens. Upon execution, it returns the information needed for the audit.For example, if you choose Compact Document Journal, the required information displays for the audit in a new session. |  |
| 5 | Maintain Audit Notes and Check Status in the Information Panel | Select a transaction or report from the left-hand side of the screen under the Audit structure. Double-click the relevant short text of the transaction or report to open an information panel in the work area on right-hand side. Make the following entries and choose Save Entry:Check Status: Check completed with warning messagesWeighting: Additional informationNotes on Check Step (in the work area): Re-test required in two weeks | If you double-click the short text of the transaction or report, an information panel displays in the work area on right-hand side.After saving, the Log for Check Step is updated along with date and timestamp information. |  |

#### Display Audit Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can check audit notes, audit process status, and so on for each audit check number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit (S4H_AUDIT_TAX). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_TAXCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_TAX – XXXX screen opens, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Log Display for Audit | On the Audit Cockpit toolbar, choose Log Display for Audit (F5). | The Audit Information System – Log Analysis screen displays. |  |
| 5 | View Audit Log | Make the following entries and choose Execute (F8) at the bottom of the screen to get a detailed audit log:Audit Structure: S4H_AUDIT_TAXCheck number: for example, 2021 | The Audit Information System – Log Display screen opens, showing all the audit activities for the audit status and notes that were saved in the prior step. |  |

### Auditor Direct Access for Professional Service

#### Create Audit with Audit Structure for Professional Service

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you open the Audit Information System Workplace cockpit and create an audit with the audit structure for Professional Services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS). | The Audit Information System Workplace screen displays. |  |
| 3 | Create Audit | In the Audit Selection section, make the following entries and choose Audit (CTRL + F2):Check Number: Any numeric value (for example, 2021) | A new audit (with audit structure and check number) is created. The system displays the message Audit S4H_AUDIT_TAX_PS XXXX created. |  |

#### Run Reports and Transactions Listed in Audit Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the reports and transactions defaulted from the audit structure S4H_AUDIT_TAX_PS. You can also maintain audit notes, audit process status, and so on.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_TAX_PSCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_TAX_PS – XXXX screen displays, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Report or Transaction Listed in Audit | Select a transaction or report from the left-hand side of the screen under the Audit Structure and double-click Execute (clock icon):As an example, if you choose Account Balances, make the following entries and choose Execute:Chart of Accounts: YCOAG/L account: for example, 10010000Company code: 3310Fiscal Year: <fiscal year>Ledger: <ledger> | The selected transaction or report opens. Upon execution, it returns the information needed for the audit. |  |
| 5 | Maintain Audit Notes and Check Status in the Information Panel | Select a transaction or report from the left-hand side of the screen under the Audit structure. Double-click the relevant short text of the transaction or report to open an information panel in the work area on right-hand side. Make the following entries and choose Save Entry:Check Status: Check completed with warning messagesWeighting: Additional informationNotes on Check Step (in the work area): Re-test required in two weeks | If you double-click the short text of the transaction or report, an information panel displays in the work area on right-hand side.After saving, the Log for Check Step is updated along with date and timestamp information. |  |

#### Display Audit Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can check audit notes, audit process status, and so on for each audit check number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - External Tax Audit with Professional Service (S4H_AUDIT_TAX_PS). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_TAX_PSCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_TAX_PS – XXXX screen opens, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Log Display for Audit | On the Audit Cockpit toolbar, choose Log Display for Audit (F5). | The Audit Information System – Log Analysis screen displays. |  |
| 5 | View Audit Log | Make the following entries and choose Execute (F8) at the bottom of the screen to get a detailed audit log:Audit Structure: S4H_AUDIT_TAX_PSCheck number: for example, 2021 | The Audit Information System – Log Display screen opens, showing all the audit activities for the audit status and notes that were saved in the prior step. |  |

### Auditor Direct Access for SOX Compliance Auditing

#### Create Audit with Audit Structure for SOX Compliance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you open the Audit Information System Workplace cockpit and create an audit with the audit structure for SOX compliance auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD). | The Audit Information System Workplace screen displays. |  |
| 3 | Create Audit | In the Audit Selection section, make the following entries and choose Audit (CTRL + F2):Check Number: Any numeric value (for example, 2021) | A new audit (with audit structure and check number) is created. The system displays the message Audit S4H_AUDIT_DASHBOARD XXXX created. |  |

#### Run Reports and Transactions Listed in Audit Structure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the reports and transactions defaulted from the audit structure S4H_AUDIT_DASHBOARD.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_DASHBOARDCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_DASHBOARD – XXXX screen displays, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Report or Transaction Listed in Audit | Select a transaction or report from the left-hand side of the screen under the Audit Structure and double-click Execute (clock icon):As an example, if you choose Monitor GR/IR Account Reconciliation, make the following entry in the Filter bar and press Enter:Company Code: 3310 | The selected transaction or report opens. Upon execution, it returns the information needed for the audit. |  |

#### Display Audit Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can check audit notes, audit process status, and so on for each audit check number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Auditor Direct Access - SOX Compliance Audit (S4H_AUDIT_DASHBOARD). | The Audit Information System Workplace screen displays. |  |
| 3 | Open New Audit | In the Audit Selection section, enter the following data and choose Execute (F8) at the bottom of the screen:Audit Structure: S4H_AUDIT_DASHBOARDCheck Number: Numeric value entered in prior step, for example, 2021 | The Audit Cockpit: S4H_AUDIT_DASHBOARD – XXXX screen opens, showing multiple reports and transactions in the audit structure on the left-hand side of the screen. |  |
| 4 | Open Log Display for Audit | On the Audit Cockpit toolbar, choose Log Display for Audit (F5). | The Audit Information System – Log Analysis screen displays. |  |
| 5 | View Audit Log | Make the following entries and choose Execute (F8) at the bottom of the screen to get a detailed audit log:Audit Structure: S4H_AUDIT_DASHBOARDCheck number: for example, 2021 | The Audit Information System – Log Display screen opens, showing all the audit activities for the audit status and notes that were saved in the prior step. |  |

### Periodic Activities

#### Audit Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With this app, the External Auditor user (with the Audit Journal (F0997) app) runs various auditing reports to ensure the correctness of your journal.

Prerequisite

Key features for this report:

- Run the Compact Journal report to provide an overview of journal entries that are entered within a given time period.
- Run the Journal report to list all journal entries that are entered within a given time period, and navigate to the Manage Journal Entry app.
- Run the Display Journal Entry Changes report to show logs for changes that are made to journal entries since they are posted.
- Run the Check Multireferenced Invoices report to list invoices if they are referenced in multiple journal entries.
- Run the Check Gaps in Document Numbers report to display all gaps that occur within a given time period.
- Run the Display Update Terminations report to display all system terminations that occur within a given time period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Audit Journal (F0997). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: 3310Fiscal Year: YYYYLedger: 0L for leading ledger with local GAAP | The Compact Journal report is displayed.Note You can switch to the Journal report to see the documents per posting date.Note If time restrictions have been maintained, data displayed by the report will be restricted to authorized periods only. |  |
| 4 | Display Changes to Journal Entries | Choose Display Journal Entry Changes.Check the report and go back. | The report shows logs for changes that are made to journal entries since they are posted |  |
| 5 | Check Multireferenced Invoices | Choose Check Multi-Referenced Invoices.Check the report and go back. | The report lists all documents in which the same reference was maintained. |  |
| 6 | Check Gaps in Journal Entry Numbering | Choose Check Gaps in Journal Entry Numbering.Check the report and go back. | The report displays all gaps that occur within a given time period. |  |
| 7 | Display Update Terminations | Choose Check Gaps in Journal Entry Numbering.On the next page, choose Display Update Terminations.Make the following entries:Creation Date: <creation date>Check the report and go back. | The report displays all system terminations that occur within a given time period.Note The Display Update Terminations button is enabled only if there are termination errors. |  |

#### Tax Reconciliation Account Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, the External Auditor user (with the Tax Reconciliation Account Balance app) checks that the tax-relevant G/L accounts are posted with tax. Additionally, you compare if there are differences between the calculated tax and posted tax.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Tax Reconciliation Account Balance (F2095). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: 3310Journal Entry: <posting document no.>Fiscal Year: <fiscal year>Posting Date: <date range>Tax Code: <tax code>G/L Account: <account number> | The Account Balances for Journal Entries with Tax Codes list is created. Look at the Difference Amount column, where the differences between Tax Amount (posted) and Calculated Tax are displayed. |  |
| 4 | Drilldown | To navigate to Information on line item level for one journal entry, choose one G/L account, then choose one Tax Code and select a Journal Entry. | When you choose the G/L account you can switch to other reports, for example, Display G/L Line Items. |  |
| 5 | Change Layout | Choose Settings.Select the Profit Center and Business Place and choose OK. | The new columns Profit Center and Business Place display. |  |

#### Tax Declaration Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, the External Auditor user (with the Tax Declaration Reconciliation app) checks that the tax base and reported (posted) tax per tax code are correct. A tax code is assigned to a tax box.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor. |  |  |
| 2 | Access App | Open Tax Declaration Reconciliation (F2096). | The Tax Declaration Reconciliation screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Company Code: for example, 3310Tax Code: <tax code>Posting Period: <posting period>Fiscal Year: <fiscal year> | The Tax Boxes and Tax Codes list is created. Check the Difference Amount column, where the differences between LC tax amount (posted) and Tax Calculated are displayed. |  |
| 4 | Drilldown | Choose any of the line items to get the relevant posting document numbers. |  |  |

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-contract-accounting-external-tax-audit-and-compliance-repo]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2OO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,022 chars in the whole document
