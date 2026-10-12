---
id: 05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub
title: "Test Script: Basic Bank Account Management (BFA_AE) - SAP S/4HANA Cloud Public Edition (BFA_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for Basic Bank Account Management: prerequisites, config, bank account lifecycle, bank chains."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-account-management]
aliases: [BFA_S4CLD2608_BPD_EN_AE]
keywords: [Bank Account Management, basic bank account management, bank account master data, bank account creation, bank account closing, bank account status, bank chains, bank statement settings, bank master data, bank account import export]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFA_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1262
topic: 05-treasury-and-cash-management/bank-account-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Basic Bank Account Management (BFA_AE) - SAP S/4HANA Cloud Public Edition (BFA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bank Account Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Basic Bank Account Management (BFA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861418)

[2 Prerequisites 4](#_Toc232861419)

[2.1 System Access 4](#_Toc232861420)

[2.2 Roles 4](#_Toc232861421)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861422)

[2.4 Preliminary Steps 7](#_Toc232861423)

[2.4.1 G/L Account Created for Bank Account 7](#_Toc232861424)

[2.4.2 Basic Settings 7](#_Toc232861425)

[2.4.3 Change Message Control (Optional) 10](#_Toc232861426)

[2.4.4 Create Business Partners for Bank Account Management 13](#_Toc232861427)

[2.4.5 Manage Field Status Groups for Bank Account Master Data (Optional) 14](#_Toc232861428)

[2.4.6 Bank Statement Settings for Bank Account Management 17](#_Toc232861429)

[2.4.6.1 Define Settings for Bank Statements 17](#_Toc232861430)

[2.4.6.2 Define Bank Account Settings - Bank Statements 20](#_Toc232861431)

[3 Overview Table 23](#_Toc232861432)

[4 Test Procedures 26](#_Toc232861433)

[4.1 Bank Account Master Data Processing with Basic Bank Account Management 26](#_Toc232861434)

[4.1.1 Using Direct Revision Activate 26](#_Toc232861435)

[4.1.1.1 Create Bank Account 26](#_Toc232861436)

[4.1.1.1.1 Open Bank Account 26](#_Toc232861437)

[4.1.1.1.2 Create Bank Master Data 27](#_Toc232861438)

[4.1.1.1.3 Edit Bank Master Data 28](#_Toc232861439)

[4.1.1.1.4 Create Bank G/L Account 29](#_Toc232861440)

[4.1.1.1.5 Manage Banks Cash Management Data 30](#_Toc232861441)

[4.1.1.1.6 Create Bank Account 31](#_Toc232861442)

[4.1.1.1.7 Export Bank Accounts 33](#_Toc232861443)

[4.1.1.1.8 Import Bank Accounts 35](#_Toc232861444)

[4.1.1.2 Change Bank Account 37](#_Toc232861445)

[4.1.1.2.1 Notify Bank to Change 37](#_Toc232861446)

[4.1.1.2.2 Update Bank G/L Account 37](#_Toc232861447)

[4.1.1.2.3 Change Bank Account 40](#_Toc232861448)

[4.1.1.3 Close Bank Account and Cancel Closing 41](#_Toc232861449)

[4.1.1.3.1 Notify Bank to Close Account 41](#_Toc232861450)

[4.1.1.3.2 Close Bank Account and Cancel Closing 41](#_Toc232861451)

[4.1.1.4 Delete Bank Account (Optional) 45](#_Toc232861452)

[4.1.2 GL Account Reduction (Optional) 46](#_Toc232861453)

[4.1.3 Import Bank Data 47](#_Toc232861454)

[4.1.4 Fields Enhancement for Bank Account Master Data 49](#_Toc232861455)

[4.2 Maintain Bank Chain 51](#_Toc232861456)

[4.2.1 Create Bank Chain 52](#_Toc232861457)

[4.2.2 Change Bank Chain 53](#_Toc232861458)

[4.2.3 Delete Bank Chain 54](#_Toc232861459)

[4.2.4 Check Bank Chain Information In Business Partner (Optional) 55](#_Toc232861460)

[4.2.5 Schedule Delete Bank Chain Jobs 56](#_Toc232861461)

[5 Appendix 58](#_Toc232861462)

[5.1 Remove Inconsistent Data after Closing a Bank Account (Optional) 58](#_Toc232861463)

## Purpose

Overview

With Basic Bank Account Management, cash managers and bank accountants can centralize the management of bank accounts using bank account master data, using a table view of banks and bank accounts.

Bank account master processing includes creating or changing a bank account, closing an obsolete bank account, and reopening a closed bank account.

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Configuration Expert | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

|  |
| --- |
| Note During testing, cash management specialist and configuration expert can share the same user ID, but cash manager and cash management specialist must be separate user IDs due to segregation of duty: cash management specialist creates the change request, cash manager approves it, the creator could not be the approver. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Default ValuesYou can test the scope item with other SAP Best Practices default values that have the same characteristics. Review your SAP ECC system to find out which other material master data exists. |

Use your own master data to go through the test procedure.

|  |
| --- |
| Caution The following Sample Values assume that you are only implementing one of the four Basic Account Master Data Procedures described in the [Preliminary Steps](#unique_6) [page ] 7 section. If you are implementing and testing more than one, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must create additional Master Data values, such as bank account numbers, bank keys, and so on, and then use these different values in each procedure type. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| BANK ACCOUNT NUMBER | 000000069312345600000006931234560000000033108888 |  | Bank account number |
| BANK KEY | 181219761812198688800011 |  | Bank key |
| BANK NAME | Bank 3 |  | Bank name |
| G/L ACCOUNT | 1100100011003000 |  | If you want to use G/L Account 11003000 for bank accounts in foreign currency, you need to create it first in your company code. Otherwise, you can use G/L account 11001000 instead. |
| CHART OF ACCOUNTS | YCOA |  | Chart of accounts |
| COMPANY CODE | 3310 |  | Company code |
| HOUSE BANK | AEBK1AEBK2AEBK3 |  | House bank |
| HOUSE BANK ACCOUNT | AEAC1AEAC2AEAC3 |  | House bank account |
| SWIFT/BIC | NBADAEAADIR |  | SWIFT/BIC |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

### Preliminary Steps

If you choose to use the existing sample data and standard configuration, you can skip the following steps:

- (Note: using the Fiori App)

If you want to change the standard settings, you can configure it in company code level with configuration activity 104351 Define Settings for Bank Statements in bank account level with app Define Bank Account Settings - Bank Statements (F5488) and in bank statement level with configuration activity 103635 Define Parameter Set.

#### G/L Account Created for Bank Account

A general ledger (G/L) account is a chronological accounting record used to track financial transaction. The G/L account is a structure that records value movements in a company. As a prerequisite, you must have already created a G/L account 11001000.

|  |
| --- |
| Caution Instructions provided assume that you are only implementing one of the four Bank Account Master Data Procedures described in the [Purpose](#unique_1) [page ] 1 section. If you are implementing and testing more than one procedure, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must have additional Master Data values created, for example G/L account numbers, bank keys, and so on, and then use these different values in each procedure. |

#### Basic Settings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Within this Basic Bank Account Management scope item, the following Bank Account Master Data Procedure is documented:

Bank Account Master Data Processing with Basic Cash Management and Direct Revision Activate

If Full Cash Management has been configured, you can follow below procedures:

- Bank Account Master Data Processing with Full Cash Management and Direct Revision Activate
- Bank Account Master Data Processing with Full Cash Management and Dual Control Revision Activate
- Bank Account Master Data Processing with Full Cash Management and Two-Person Revision Activate
- Bank Account Master Data Processing with Full Cash Management and Workflow Revision Activate

In this preliminary step, you choose which one of these four Bank Account Master Data Processing Procedures to use for your implementation:

1. To use , use the following settings:
    - Cash Management Scope = 01
    - Basic Scope & Bank Account Revision = 01 Activate Directly
2. To use , use the following settings:
    - Cash Management Scope = 02
    - Full Scope & Bank Account Revision = 01 Activate Directly
3. To use , use the following settings:
    - Cash Management Scope = 02
    - Full Scope & Bank Account Revision = 02 Activate via Dual Control
4. To use Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Two-Person Revision Activate, use the following settings:
    - Cash Scope = 02
    - Bank Account Control Mode = 04 Two-Person Verification
5. To use , use the following settings:
    - Cash Management Scope = 02
    - Full Scope & Bank Account Revision = 03 Activate via Workflow

The check box Enable Snapshot is used for the snapshot of historic cash report. This check box can only be selected and saved when cash value is Full Scope. If the value of cash scope is Basic Scope, it can’t be saved once the check box of Enable Snapshot is selected. Once the check box of Enable Snapshot is selected and saved, the function of snapshot of historic cash report is activated.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution(F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the General Settings row, choose the arrow button at the right of the row.In the right pane, for the Basic Settings row, choose Configure.Note If the client is maintained as a customer system, the Basic Settings app is available; otherwise, the app is not available. | The Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Management Scope and Bank Account Revision for your implementation based on the previously described procedures. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Management Scope and Bank Account Revision for your implementation based on the previously described procedures. |  |  |

The check box Enable Snapshot is used for the snapshot of historic cash report. This check box can only be selected and saved when cash value is Full Scope. If the value of cash scope is Basic Scope, it can’t be saved once the check box of Enable Snapshot is selected. Once the check box of Enable Snapshot is selected and saved, the function of snapshot of historic cash report is activated.

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct in the SSCUI Define Basic Settings. |

#### Change Message Control (Optional)

Purpose

In general, a bank account with multiple house bank accounts and a different company code between bank account and house bank account are forbidden and an error message is raised when saving the bank account. But in some special case, if you want to maintain multiple house bank accounts or a different company code between bank account and house bank account, you can follow this instruction to customize the message from error to warning.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution(F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementItem Name: Bank Account ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Change Message Control for Bank Account Management (SSCUI 103894) row, choose Configure. | The Change View "Message Control by User": Overview screen displays. |  |
| 3 | Work Area | Enter FCLM_BAM_MAINT in the Area field, then choose Save. |  |  |
| 4 | Change Message Status for Multiple House Bank Accounts | Make the following entries:MsgNo: 537Message Text: You can link only one central house bank account to a bank account.User Name: (Blank)*Online: W*Batch Input: WStandard: E | You can create multiple house bank account connectivity with warning message displays. |  |
| 5 | Change Message Status for Different Company Codes between Bank Account and House Bank Account | Make the following entries:MsgNo: 466Message Text: Company code &1 is inconsistent with company code &2 of bank account.User Name: (Blank)*Online: W*Batch Input: WStandard: E | You can create different company codes between bank account general data and house bank account connectivity with warning message displays. |  |
| 6 | Change Message Status for Bank Account Descriptions in Different Language Environments | Make the following entries:MsgNo: 522Message Text: Description in language &1 is not maintained.User Name: (Blank)*Online: W*Batch Input: WStandard: E | Warning message displays if the bank account’s description is missing in different language environments. |  |
| 7 | Change Message Status for Non-Existing Payment Approver | Make the following entries:MsgNo: 187Message Text: Payment approver & does not exist.User Name: (Blank)*Online: W*Batch Input: WStandard: E | If non-existing user is maintained as the payment approver, you will only receive warning message for the following operation of the bank account. |  |
| 8 | Save | Save it. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Change Message Control | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Change Message Control.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change Message Control screen displays. |  |
| 3 | Work Area | Enter FCLM_BAM_MAINT in the Application Area field, then choose Continue. | The Change View “Message Control by User”: Overview screen displays. |  |
| 4 | Change Message Status for Multiple House Bank Accounts | Make the following entries:MsgNo: 537Message Text: You can link only one central house bank account to a bank account.User Name: (Blank)*Online: W*Batch Input: WStandard: E | You can create multiple house bank account connectivity with warning message displays. |  |
| 5 | Change Message Status for Different Company Codes between Bank Account and House Bank Account | Make the following entries:MsgNo: 466Message Text: Company code &1 is inconsistent with company code &2 of bank account.User Name: (Blank)*Online: W*Batch Input: WStandard: E | You can create different company codes between bank account general data and house bank account connectivity with warning message displays. |  |
| 6 | Change Message Status for Bank Account Descriptions in Different Language Environments | Make the following entries:MsgNo: 522Message Text: Description in language &1 is not maintainedUser Name: (Blank)*Online: W*Batch Input: WStandard: E | Warning message appears if the bank account’s description is missing in different language environments. |  |
| 7 | Change Message Status for Non-Existing Payment Approver | Make the following entries:MsgNo: 187Message Text: Payment approver & does not exist.User Name: (Blank)*Online: W*Batch Input: WStandard: E | If non-existing user is maintained as the payment approver, you will only receive warning message for the following operation of the bank account. |  |
| 8 | Save | Save it. |  |  |

#### Create Business Partners for Bank Account Management

Purpose

This step describes how to create Bank and Authorized Representative business partner master data for Bank Account Management. A bank is associated with a Risk Business Partner, Defaultable Business Partner and Bank Contact Person. Risk Business Partner and Defaultable Business Partner is represented with the BP role TR0703. Bank Contact Persons are external to the company and is represented by BP role BUP001. Authorized Representative is represented by BP role TR1000.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Business Partner Master Data (F3163). | The Manage Business Partner view displays. |  |
| 3 | Create Business Partner | Choose Create.Choose Person/ Organization/ Group.Note If you are creating BP Role TR0703 Bank, please choose Organization. If you are creating BP Role TR1000 Authorized Representative, please choose Person. |  |  |
| 4 | Enter Data | Make the following entries:Grouping: BP02BP Role: TR0703 BankName 1: Risk BPChoose OK.Choose Bank Accounts tab.Choose Create.Make the following entries：Bank Country/Region： AEBank Key：82080000Account Number：2580061Choose Create. | A New Business Partner is created and displayed in the Business Partner view. |  |

#### Manage Field Status Groups for Bank Account Master Data (Optional)

Purpose

With this Customizing SSCUI, you can define field status groups and special rules to control the appearance and status of the fields on the user interface (UI) screens of the Manage Bank Accounts app. For example, you may define a field to be mandatory, hidden, editable, or read-only.

|  |
| --- |
| Note This customizing activity is available in Bank Account Master Data mode for bank account management. You can go to test script Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)) 2.4.2 Define Basic Settings to check your system status. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241).Choose Configure Your Solution.Search and choose either Manage Field Status Groups or SSCUI ID 104059 in the search filter.Choose Configure for the Manage Field Status Groups Step Name. | The Manage Field Status Groups screen is displayed. |  |
| 3 | Maintain Field Status Groups | In the Dialog Structure panel, choose the Define Field Status Groups folder.Choose New Entries.Make the following entries and choose Save:Field Group: ZBAMACTDescription: BAM Activate Testing Mode.Select the check box of ZBAMACT.In the Dialog Structure panel, double-click the Define UI Field Status subfolder.Choose New Entries.Make the following entries:Object: BAMPress Enter.Note It is critical to press Enter after object input. You must press Enter before you can use the search help in the Field name panel. The search help function is linked to an object. Only after the object is confirmed may the search help value be populated in the Field name.Field name: ACC_NUMField Status: CChoose Save. |  |  |
| 4 | Assign Field Status Groups to Bank Acct Master Data | Choose Assign Field Status Grps to Bank Acct Master Data.Note The field status assignment applies to non-workflow scenario. For workflow scenario, the field status group assignment is hard coded.Locate to Scenario Activate Inactive Bank Accounts, update the Field Group to ZBAMACT.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 2 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 3 | Open Manage Field Status Groups | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage Field Status Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage Field Status Groups screen is displayed. |  |
| 4 | Maintain Field Status Groups | Choose Define Field Status Groups.Choose New Entries.Make the following entries and choose Save:Field.Grp: ZBAMACTDescription: BAM Activate Testing Mode.Select the check box of ZBAMACT. Choose Define UI Field Status.Choose New Entries.Make the following entries:Object: BAMPress Enter.Note It is critical to press Enter after object input. You must press Enter before you can use the search help in the Field name panel. The search help function is linked to an object. Only after the object is confirmed may the search help value be populated in the Field name.Field Name: ACC_NUMField Status: CChoose Save. |  |  |
| 5 | Assign Field Status Groups to Bank Acct Master Data | Choose Assign Field Status Grps to Bank Acct Master Data.Note The field status assignment applies to non-workflow scenario. For workflow scenario, the field status group assignment is hard coded.Locate to Scenario Activate Inactive Bank Accounts, update the Field Group to ZBAMACT.Choose Save. |  |  |

#### Bank Statement Settings for Bank Account Management

If you want to change the standard settings for bank statements, you can go to Define Settings for Bank Statements section to define it at company code level. You can also go to Define Bank Account Settings - Bank Statements section to define it at bank account level.

##### Define Settings for Bank Statements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this customizing, you can define settings for integrating bank statements or intraday bank statements with cash management at company code level.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

You can choose to activate the New Integration Strategy for Bank Statements and Cash Mgmt feature.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementItem Name: Bank Account Management | The Configure Your Solution – Bank Account Management screen is displayed. |  |
| 3 | Configuration | From the Configuration Steps area, select the Define Settings for Bank Statements step, choose Configure. |  |  |
| 4 | Define Bank Statement and Cash Balance Integration Configuration | Choose New Entries. Make the following entries and choose Save:Company Code: 3310Valid From: <current date>Posting Category (End of Day): posting to be processedNote If you choose no posting processing for a specific company code, then no FI posting document is generated during uploading bank statement for all bank accounts under the specific company code.Transfer Mode (End of Day): Balance and Bank Statement ItemsPosting Category (Intraday): Posting to Be ProcessedTransfer Mode (Intraday): Bank Statement Items OnlyManual Entry: <selected>Spreadsheet Import: <selected> |  | The Transfer Mode determines how cash management apps interact with imported bank statements (end-of-day or intraday):Balance Only: Transfers only account balances to cash management. Use the Manage Bank Account Balances (F5175) app to view balance updates.Bank Statement Items Only: Transfers only line items (no balances) to cash management. Applicable apps: Short-Term Cash Positioning (F5380), Cash Position - Today (F1737), Cash Flow Analyzer (F2332), Check Cash Flow Items (F0735). Balances must be imported separately via F5175 or calculated from cash flows.Balance and Bank Statement Items: Transfers both balances and line items. All above apps (F5380, F1737, F2332, F0735, F5175) are usable.No Update for Cash Management: Imports statements but does not update cash management apps. None of the listed apps (F5380, F1737, F2332, F0735) will reflect the data. |
| 5 | Back | Choose Back. | The Change View "Bank Statement and Cash Balance Integration Configuration view displays. |  |
| 6 | Save | Choose Save. | The integration configuration is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Settings for Integrate with End-of-Day Bank Statements | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Statements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Integrate with End-of-Day Bank Statements screen is displayed. |  |
| 3 | Define Bank Statement and Cash Balance Integration Configuration | Choose New Entries. Make the following entries and choose Save:Company Code: 3310Valid From: <current date>Posting Category (End of Day): posting to be processedNote If you choose no posting processing for a specific company code, then no FI posting document is generated during uploading bank statement for all bank account under the specific company code.Transfer Mode (End of Day): Balance and Bank Statement ItemsPosting Category (Intraday): Posting to Be ProcessedTransfer Mode (Intraday): Balance and Bank Statement ItemsManual Entry: <selected>Spreadsheet Import: <selected> |  | The Transfer Mode determines how cash management apps interact with imported bank statements (end-of-day or intraday):Balance Only: Transfers only account balances to cash management. Use the Manage Bank Account Balances (F5175) app to view balance updates.Bank Statement Items Only: Transfers only line items (no balances) to cash management. Applicable apps: Short-Term Cash Positioning (F5380), Cash Position - Today (F1737), Cash Flow Analyzer (F2332), Check Cash Flow Items (F0735). Balances must be imported separately via F5175 or calculated from cash flows.Balance and Bank Statement Items: Transfers both balances and line items. All above apps (F5380, F1737, F2332, F0735, F5175) are usable.No Update for Cash Management: Imports statements but does not update cash management apps. None of the listed apps (F5380, F1737, F2332, F0735) will reflect the data. |
| 4 | Back | Choose Back. | The Change View "Bank Statement and Cash Balance Integration Configuration view displays. |  |
| 5 | Save | Choose Save. | The integration configuration is created. |  |

##### Define Bank Account Settings - Bank Statements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can define settings for integrating end-of-day electronic bank statements with cash management for individual bank accounts.

Procedure

You can choose to activate the New Integration Strategy for Bank Statements and Cash Mgmt feature.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Define Bank Account Settings - Bank Statements (F5488). |  |  |
| 3 | Define Bank Account Setting for Bank Statement | Choose Create.Make the following entries and choose Create:Technical ID: <ID for your bank account>Note If field Technical ID is not visible, select Adapt Filters to include the field into the Filter bar.Valid From: <current date>Posting Category (End of Day): Posting to Be ProcessedNoteIf you choose no posting processing for a specific bank account, then no FI posting document is generated during uploading bank statement for the bank account.The setting you defined in this step has higher priority than the setting you defined in previous step [Define Settings for Bank Statements](#unique_13) [page ] 17.Transfer Mode (End of Day): Balance and Bank Statement ItemsPosting Category (Intraday): Posting to Be ProcessedTransfer Mode (Intraday): Bank Statement Items OnlyEnable Balance from Manual Entry: <Selected>Enable Balance from Spreadsheet Import: <Selected>Bank Statement Forwarding: No Forwarding | The Define Bank Account Settings – Bank Statements view displays. | The option you select from Transfer Mode impacts how cash management apps work with imported end-of-day and intraday bank statements:Balance Only: Transfer only the bank account balance to cash management.With this mode, you can use the Manage Bank Account Balances (F5175) app to view balance updates.Bank Statement Items Only: Transfer only line items of bank statements to cash management.With this mode, you can use the following apps:Short-Term Cash Positioning (F5380)Cash Position - Today (F1737)Cash Flow Analyzer (F2332)Check Cash Flow Items (F0735)The system transfers the line items to the above apps without balance information. To display bank account balances in the Short-Term Cash Positioning (F5380) app, you can use the Manage Bank Account Balances (F5175) app to import or enter bank account balances. For the Cash Position - Today (F1737) app and Cash Flow Analyzer (F2332) app, bank account balances are calculated based on actual and forecasted cash flows.Balance and Bank Statement Items: Transfer both balance and line items from bank statements to cash management.With this mode, you can use the following apps:Short-Term Cash Positioning (F5380)Cash Position - Today (F1737)Cash Flow Analyzer (F2332)Check Cash Flow Items (F0735)Manage Bank Account Balances (F5175)No Update for Cash Management: Import bank statements but without transferring the data to cash management.With this mode, the system does not update bank statement data in cash management apps. Therefore, none of the following app work with this mode:Short-Term Cash Positioning (F5380)Cash Position - Today (F1737)Cash Flow Analyzer (F2332)Check Cash Flow Items (F0735) |

## Overview Table

The Basic Bank Account Management (BFA) scope item consists of process steps in the table below, depending upon the which of the four procedures you will implement.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |
| --- |
| Caution Instructions provided assume that you are only implementing one of the four Bank Account Master Data Procedures. If you are implementing and testing more than one procedure, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must have additional Master Data values created, for example bank account numbers, bank keys, and so on, and then use these different values in each procedure. |

Table 2: Bank Account Master Data Processing With Basic Cash Management and Direct Revision Activate

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Using Direct Revision Activate |  |  |  |
| Create Bank Account |  |  |  |
| [Open Bank Account](#unique_16) [page ] 26 | Cash Management Specialist |  | The bank accountant goes to the bank and opens a new bank account in this bank. This step does not occur in the system. |
| [Create Bank Master Data](#unique_17) [page ] 27 | Cash Management Specialist | Manage Banks | A bank key that does not exist in production system is created. If the bank key already exists, skip this step. |
| [Edit Bank Master Data](#unique_18) [page ] 28 | Cash Management Specialist | Manage Banks | More bank information is input in production system. |
| [Create Bank G/L Account](#unique_19) [page ] 29 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user may create the G/L accounts of newly created bank account. |
| [Manage Banks Cash Management Data](#unique_20) [page ] 30 | Cash Management Specialist | Manage Banks | The bank accountant creates the house bank. If a new bank account is opened in an existing house bank in your system, skip this step. |
| [Create Bank Account](#unique_21) [page ] 31 | Cash Management Specialist | Manage Bank Accounts (F1366A) | A new bank account that does not exist in production system is created. |
| [Export Bank Accounts](#unique_22) [page ] 33 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are exported from production system. |
| [Import Bank Accounts](#unique_23) [page ] 35 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are imported into development system and consolidation system. |
| Change Bank Account |  |  |  |
| [Notify Bank to Change](#unique_24) [page ] 37 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system. |
| [Update Bank G/L Account](#unique_25) [page ] 37 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user updates the G/L account of bank only when it is necessary. However, modification of bank account does not result in G/L account modification every time. |
| [Change Bank Account](#unique_26) [page ] 40 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank accountant changes the attributes of this bank account in system. |
| Close Bank Account and Cancel Closing |  |  |  |
| [Notify Bank to Close Account](#unique_27) [page ] 41 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to close this bank account. This step does not occur in the system. |
| [Close Bank Account and Cancel Closing](#unique_28) [page ] 41 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The redundant bank account is closed in system. |
| [Delete Bank Account (Optional)](#unique_29) [page ] 45 | Cash Management Specialist | Manage Bank Accounts (F1366A) | GL Accounts are reduced and migrated. |
| [GL Account Reduction (Optional)](#unique_30) [page ] 46 | Cash Management Specialist | Manage Bank Accounts (F1366A) |  |
| [Import Bank Data](#unique_31) [page ] 47 | Cash Management Specialist | Import Bank Directories (BIC2S) | The bank data is imported. |
| [Fields Enhancement for Bank Account Master Data](#unique_32) [page ] 49 | Administrator | Custom Fields (F1481) | Fields are added. |

Table 3: Maintain Bank Chain

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Bank Chain](#unique_33) [page ] 52 | Accounts Payable Accountant | Manage Bank Chains (F4004) | Bank chain created. |
| [Change Bank Chain](#unique_34) [page ] 53 | Accounts Payable Accountant | Manage Bank Chains (F4004) | Bank chain changed. |
| [Delete Bank Chain](#unique_35) [page ] 54 | Accounts Payable Accountant | Manage Bank Chains (F4004) | Bank chain deleted. |
| [Check Bank Chain Information In Business Partner (Optional)](#unique_36) [page ] 55 | Accounts Payable Accountant. | Maintain Business Partner (BP) | Bank chain information checked in business partner. |
| [Schedule Delete Bank Chain Jobs](#unique_37) [page ] 56 | Accounts Payable Accountant | Schedule Bank Chain Jobs (F4503) | Bank chain information checked in business partner. |

## Test Procedures

These sections describe the test procedures for each process step that belongs to this scope item.

Follow the procedures in the Bank Account Master Data Processing With Basic Cash Management and Direct Revision Activate section when you use Basic Cash Management without an additional license for SAP Cash Management powered by SAP HANA.

When you have Full Cash Management, which requires an additional license for SAP Cash Management powered by SAP HANA, follow the procedures that apply to your implementation: Bank Account Master Data Processing With Full Cash Management and Direct Revision Activate, or Bank Account Master Data Processing With Full Cash Management and Dual Control Revision Activate, or Bank Account Master Data Processing With Full Cash Management and Workflow Revision Activate.

|  |
| --- |
| Caution Instructions provided assume that you are only implementing one of the four Bank Account Master Data Procedures described in the [Purpose](#unique_1) [page ] 1 section. If you are implementing and testing more than one procedure, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must have additional Master Data values created, such as bank account numbers, bank keys, and so on, and then use these different values in each procedure. |

### Bank Account Master Data Processing with Basic Bank Account Management

SAP has predelivered bank and bank account master data as demo data in START system. If you are using Solution Builder for activation, please don't copy these SAP predelivered master data from START system to Q or P system. Because ID Clash will not triggered, you may not be able to delete these entries in Q or P. But If you use SAP Central Business Configuration as your configuration environment, whether it is for 2 System Landscape or 3 System Landscape, you won't get such issue.

#### Using Direct Revision Activate

##### Create Bank Account

###### Open Bank Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and opens a new bank account in this bank. This step does not occur in the system.

###### Create Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create standard banks and internal banks master data with general information. For physical banks you should create it as standard banks, and for others you should create it as internal banks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Choose Create Bank | Choose Go for the banks to display in a list and choose Create Bank. | The Create Bank view displays. |  |
| 4 | Enter Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011Choose Create Bank. |  |  |
| 5 | Enter General Data | Make the following entries:Bank Name: AE Standard Bank for Basic Bank Account ManagementChoose Create. | The standard bank is created. |  |
| 6 | Create Internal Banks | Go to the initial page of app Manage Banks - Master Data (F6437).Choose the triangle button beside the Create.Choose Create Internal Bank. |  |  |
| 7 | Enter Control Data | Make the following entries:Bank Country/Region: AEBank Key: 88800011Internal Bank Category: Payment Service ProviderChoose Create Internal Bank.Note If the bank key created is used for an internal virtual bank, for example, PayPal,which is used as House Bank, please select Internal - Payment Service Provider.which is used to enable the maintenance of the business partner bank details with alias, please select the Payment system. For more details, please refer to SSCUIs 105361 - Define Alias Types and 105362 - Define Payment Systems. |  |  |
| 8 | Enter General Data | Make the following entries:Bank Name: AE Internal Bank for Basic Bank Account ManagementChoose Create. | The Internal bank is created. |  |

###### Edit Bank Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to edit bank and input more bank information in production system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Filter the Bank | Make the following entry in the filter and choose Go.Bank Key: 88800011 |  | If the system does not find the Bank Key, make the following entries, and choose Go:Bank Country/Region: AE |
| 4 | Choose the Bank | Select the arrow on the right of the bank key that you want to edit to go to the detail screen. |  |  |
| 5 | Edit Bank | Choose Edit.Make the following entries:SWIFT/BIC: DEUTDEFFXX1City: for example, 60040 Frankfurt, Main |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

###### Create Bank G/L Account

Purpose

The General Ledger Accountant may create the G/L accounts for a new bank account.

|  |
| --- |
| Note For cash management in this package, you can use the same G/L accounts (bank main account and bank subaccount) for different bank accounts when they use the same currency key. The balance of each bank account can be displayed in the cash management app, instead of checking balances of the relevant G/L account. Using this approach keeps the chart of accounts smaller. |

|  |
| --- |
| Note If you want to create a new G/L account for a new bank account, execute the following steps. Create the G/L accounts in production system, development system, and consolidation test system. |

|  |
| --- |
| Note This procedure is mentioned in the Accounting and Financial Close ([J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58)) test script. You can refer to the Manage G/L Account Master Data step and copy an existing G/L account to a new one (for example, copy 11001000 to 11003000). |

###### Manage Banks Cash Management Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can input banks data that is used for cash management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Cash Management (F1574A). |  |  |
| 3 | Enter Search Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011If the Bank Key field is not visible, choose Filters to unhide it.Choose Go.Go into the detail of the bank. | The Display Bank view appears. |  |
| 4 | Enter House Bank Data | Go to House Banks tab and choose Create.Make the following entries:Company Code: 3310House Bank: AEBK3Choose Continue.Choose Apply. |  |  |
| 5 | Enter Netting Business Partner | Go to Netting Business Partner tab.Make the following entries:Valid From: <Current Date>.Valid To: <Futrue Date>.Business Partner: <Choose one by using search help> |  |  |
| 6 | Save Bank | Choose Save. | New house bank is saved successfully. |  |

###### Create Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to create a new bank account by a bank accountant (Cash Management Specialist).

|  |
| --- |
| Note Since bank accounts are not transportable to the production system, they must be maintained manually there. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Account view displays. |  |
| 3 | Create Bank Account | Choose Create to add a new bank account.Make the following entries:Company Code: 3310Account Type: 01 |  |  |
| 4 | Enter Header Data | Make the following entries:Account Number: 0000000033108888Account Description: AE Bank Account for Basic Bank Account ManagementBank Country/Region: AEBank Key: 88800011Note To maintain the bank key in this step, the bank key must already exist in the system.Currency: AED |  |  |
| 5 | Enter General Data | Change the following entries:Opening Date: for example, <current date>Account Holder: for example, Company Code3310 (company code name is usually defaulted by system)IBAN: <Generate IBAN>Note Only perform this step if the country is using IBAN; if you do not use IBAN in your process, just skip this step.Bank Control Key: for example, PNote Bank Control Key is only used in some countries like France, Spain, Italy. If you don't use Bank Control Key, you should leave this field blank. |  |  |
| 6 | Bank Relationship Data | Pmnt Tran Type Group： CAMT053Note The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank Statements |  |  |
| 7 | Generate IBAN | Note Only perform this step if this country is using IBAN. If you do not use IBAN in your process, you can skip this step.Choose IBAN.When the warning dialog box appears, choose OK.The proposed IBAN is automatically entered. |  |  |
| 8 | Choose House Bank Account Connectivity | Choose House Bank Account Connectivity. | The Connectivity Path tab appears. |  |
| 9 | Enter Connectivity Criteria | Choose Create, and make the following entries:ID Category: for example, Central System: House Bank AccountRemote System: <leave blank>Company Code: 3310House Bank: AEBK3House Bank Account: AEAC3G/L Account: 11001000Choose Apply. |  |  |
| 10 | Save and Activate Bank Account | Ensure all necessary data have been entered and choose Save as Inactive.Choose Activate. | A new bank account is created. |  |
| 11 | Review History and Revision | Select the newly created bank account, and on the Bank Account view, the new bank account is active in the display mode. No revision button exists.Choose Account Histories and a history dialog box displays with the history list of the current bank account: Revision 1, activated. |  |  |

###### Export Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The new bank account (including house bank account) creation in production system is completed in the previous procedure. Some system configuration is based on the house bank and the house bank account. Because configuration is done in the development system, you must export the bank accounts from that system to the development and consolidation test system.

Prerequisites

|  |
| --- |
| NoteYou use Microsoft Office 2010 or higher that contains Microsoft Excel.The Developer tab in Microsoft Excel is enabled. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts view displays. |  |
| 4 | Export Data | In the Bank Accounts Export section, enter company code and choose Go. Select the check box of the bank accounts, and choose Export Bank Accounts to an XML File.In the File Download dialog box, choose Save As.In the Save As dialog box, identify a location to save the XML file.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The Bank_Accounts.xml file saved to the location you indicated.The file contains all the existing bank account master data in your system in XML format. |  |
| 5 | Download the Spreadsheet Template | In the Bank Accounts Export section, choose Download XML Spreadsheet Template.In the File Download dialog box, choose Save AsIn the Save As dialog box, identify a location to save the XML spreadsheet template.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The XML_Spreadsheet_Template.xml file is saved to the location you indicated |  |
| 6 | Import | Use Microsoft Excel to open XML_Spreadsheet_Template.xml.Using the Developer tab in Excel, choose Import, and then choose the Bank_Accounts.xml file in the Import XML dialog box and Import. | Bank accounts master data has been imported into the XML spreadsheet template.If message XML import error - Failed schema validation displays, but data has been imported from Bank_Accounts.xml, ignore this message by choosing OK. |  |
| 7 | Export Data to a New File | From the Developer tab in Microsoft Excel, choose Export, and enter the file name Bank_Accounts_Export.xml.Choose Export. | Bank accounts master data has been saved in the Bank_Account_Export.xml file. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This instruction guides you how to import the bank accounts into the target system. If you use Solution Builder environment with 2 system landscape, or use SAP Central Business Configuration with 2 system landscape, you may use this functinality to update your test system. If you use On-Premise system or use SAP Central Business Configuration with 3 system landscape, the development system can also be updated besides the test system.

|  |
| --- |
| Note You may only have one client for testing. You can test the function Export and Import the bank accounts in the same client. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts view displays. |  |
| 4 | Identify the Import Path | Choose Select File.On the Open dialog box, identify the XML (Bank_Accounts_Export.xml) to be uploaded.Choose Open. |  |  |
| 5 | Import with Test Run | Choose Import with Test Run, and verify the validation results.Note If the Bank Account "XXXXXXXXXX" is already in approval process notification displays, we recommend that you import the bank accounts at a different time, since those bank accounts are in process workflow.When the message displays, only execute a test run, or complete the workflow, before the production run.When the status of all validation results is OK, you can import bank accounts into production system. |  |  |
| 6 | Import with Production Run | Choose Select File again.In the Open dialog box, identify the XML (Bank_Accounts.xml) to be uploadedChoose Open.Choose Import and check the validation results. | Bank accounts are successfully imported into development system. |  |
| 7 | Import to Test System | Repeat the preceding steps to import bank accounts into consolidation test system. |  |  |

##### Change Bank Account

###### Notify Bank to Change

Procedure

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system.

|  |
| --- |
| Note Bank account master data modification does not always result in a notification to the bank (for example, the modification of payment signatories). |

###### Update Bank G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The key user updates the G/L account of the bank only when updating is required. For example, if the currency key of the bank account is changed, the user updates the currency of the G/L account. Not all bank account modifications result in a G/L account modification.

|  |
| --- |
| Note Update the G/L accounts in the production, development, and consolidation test systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241). |  |  |
| 3 | Search Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Choose the G/L Account to Update | Choose the G/L account link. |  |  |
| 6 | Open | Choose the arrow at the right of the column with the Chart of Accounts item. |  |  |
| 7 | Select Configuration Step | For the Manage G/L Account Master Data SSCUI 150001 step, choose Configure. |  |  |
| 8 | Edit the Account | Choose Edit. |  |  |
| 9 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 10 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 11 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 12 | Edit the Account | Choose Edit. |  |  |
| 13 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 14 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 15 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 16 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Manage G/L Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage G/L Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage G/L Account Master Data screen displays. |  |
| 3 | Edit the Account | Choose Edit. |  |  |
| 4 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
| 5 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 6 | Choose the G/L Account | Choose the triangle button on the right of the target G/L Account. |  |  |
| 7 | Edit the Account | Choose Edit. |  |  |
| 8 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 9 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 10 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 11 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

|  |
| --- |
| Note Changing the currency is not possible when there is an existing balance for the G/L account. |

###### Change Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to change a bank account by bank accountant (Cash Management Specialist).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts (F1366A) view displays. |  |
| 3 | Choose Account to Change | Choose the bank account to be changed from the account list view.Enter the filter and choose Go. | A new view displays. |  |
| 4 | Edit | Choose Edit. Modify fields according to your requirements. |  |  |
| 5 | Save | Choose Save to save the changes. | The bank account changes (updated) and a warning notification displays about bank statements. |  |

##### Close Bank Account and Cancel Closing

###### Notify Bank to Close Account

Procedure

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to close the bank account. This step does not occur in the system.

###### Close Bank Account and Cancel Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to close an obsolete bank account by bank accountant (Cash Management Specialist) and the process of canceling the closing if you want to reactivate it.

Prerequisite

There are five indicators to display the status of a bank account.

| Status | Comment |
| --- | --- |
| Active | This status indicates bank account is successfully created in sap system and can be normally used. |
| Inactive | This status displayed in full cash management, it indicates bank account is initially created without being approved. |
| Closing Request Sent to Bank | This status indicates you have planned and informed the bank to close the bank account in a future date. After initial closing button is triggered and approved, the bank account status will be display as Closing Request Sent to Bank. The function of bank account in status Closing Request Sent to Bank is the same with bank account status active, for example, you can still normally use it as review bank account, make bank transfer, run payment, posting etc. |
| Closed at Bank | This status indicates the bank account has been closed by the bank. You can’t make bank transfer, run payment, review bank account, maintain payment approver, import signatory cards, monitor intraday/end of day bank statement and being displayed in bank relationship overview in this status. If you set a posting block date for a bank reconciliation account in Start to Confirm Closing at Bank step, no posting is allowed after that specific date. However, you can still make postings for other G/L accounts, unless the G/L accounts has been blocked from General Ledger Accounting side. |
| Closed | This status indicates the bank account is completely closed in sap system, no posting is allowed for bank reconciliation accounts, you can find bank reconciliation accounts details in online help: [Define G/L Accounts for Payment Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/781544a06fc6476fa99755b96a3006be.html?locale=en-US). However, you can still make postings for other G/L accounts. Unless the G/L account has been blocked from General Ledger Accounting side, you can refer to online help: [Mark G/L Accounts as Not Used](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/2052bdb5d8fc4b6d9d787ea991e3613d.html?locale=en-US) and [G/L Accounts Blocked in P System Until Transport of Changes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/e392432f0b2041528a118f8373f2269d.html?locale=en-US). |

|  |
| --- |
| Caution Don't close sample bank accounts that are connected to house bank AEBK1/AEAC1 and AEBK2/AEAC2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Close | Choose the triangle button of the bank account to be closedFor example, account 0000000033108888 in AEBK3. |  |  |
| 4 | Mark for Closing | Choose Mark for Closing.Make the following entry and choose Mark for Closing.Planned Closing Date: <Current Date> |  |  |
| 5 | Send Closing Request to Bank | Choose Send Closing Request to Bank. | The Send Closing Request to Bank dialog box is displayed. |  |
| 6 | Start to Initial Closing | Make the following entries in the dialog box and choose Send Closing Request to Bank:Planned Closing Date: for example, <current date>+2days | The bank account’s status is changed to Closing Request Sent to Bank. |  |
| 7 | Confirm Closing at Bank | Choose Confirm Closing at Bank. | The Confirm Closing at Bank dialog box is displayed. |  |
| 8 | Start to Confirm Closing at Bank | Make the following entries in the dialog box and choose Confirm Closing at Bank.Closing Date: for example, <current date>Note If Bank Reconciliation Account is set in House Bank Account Connectivity, you can input a posting blocking date. You use posting block date to set a final date for marking financial postings to this bank account. After the specified posting block date, posting is no longer allowed for this bank account. This date allows you to add an additional check for financial postings and help you maintain correct data for Advanced Valuation in Financial Accounting. You set the posting block date when you change the bank account status to Closed at Bank. You can update the posting block date as needed before the bank account is set to the Close status. | The bank account’s status is changed to Closed at Bank. | You can choose confirm closing at bank without bank account initial closing. If you bypassing the initial closing procedure and choose confirm closing at bank, the bank account status will be changed to Closed at Bank directly. |
| 9 | Complete Closing | Choose Complete Closing. |  | The actual balance of the bank account will be checked. The checking logic is defined in step Basic Settings. You can go to step Basic Settings to configure the Balance Check for Closing Process field as following:Blank: Balance Check Method (Deprecated)With this option set, you use the deprecated balance check method controlled via the configuration activity Change Message Control for Bank Account Management.10: No validation and close immediately.You set this option if you don't want to perform any bank account balance check when bank accounts are closed.20: Validate against aggregated actuals for amount in bank account currency in One Exposure.With this option set, the system checks the aggregated actuals of a bank account in One Exposure before the account is closed.Users can view the aggregated actuals for your bank account in the Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) app. To do so, in this app, do the following:In the Account Dimension field, select Bank Account (House Bank/House Bank Account).Set the reconciliation date as your current local date.In the Data Source Selection field, select Acnt Bal in Cash Pos (Tran Dt).Run the report. The Acnt Bal in Cash Position (Tran. Dt) field to show the aggregated actuals for bank accounts.To adjust the aggregated actuals for your bank account to produce zero, users can create a memo record to offset the current amount. To do so, in the Manage Memo Records 2.0 (F2986A) app, create a memo record with the memo record category Actual Cash Memo. Please note that the value date of the memo record must not be later than the bank account closing date. After the bank account balance is adjusted to zero, the bank account will no longer be visible in the report above.30: Validate against ledger balance (from bank statement).With this option set, the system checks the ledger balance of a bank account in the Manage Bank Account Balances (F5175) app before the account is closed. Only bank accounts for which the ledger balance is zero or has never been updated before can be closed.When the balance check error is shown, users need to ensure the ledger balance reflects the real balance of the bank account. They can import the latest bank statement that confirms the ledger balance is zero, or enter a ledger balance for this bank account in the Manage Bank Statements (F1564) app.To use option 30: Validate against ledger balance (from bank statement), make sure that all of your bank accounts are not set with the transfer mode No Update for Cash Management for end-of-day bank statements as the method requires that balance data is saved for cash management. |
| 10 | Return to Closed at Bank | Choose Return to Preceding Status. | The bank account’s status is changed to Closed at Bank. |  |
| 11 | Return to Closing Request Sent to Bank | Choose Return to Preceding Status. | The bank account’s status is changed to Closing Request Sent to Bank. |  |
| 12 | Return to Active | Choose Return to Preceding Status. | The bank account’s status is changed to Active. |  |

##### Delete Bank Account (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to delete bank account by bank accountant (Cash Management Specialist).

|  |
| --- |
| Note Only the bank accounts in inactive status or active bank accounts that never involved in any business transaction or used in any configuration can be deleted. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Delete | Select the checkbox on the left of the bank account to be deletedChoose Delete.Choose Delete on the pop up window. | The Bank Account is deleted. |  |

#### GL Account Reduction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can reduce your GL account by using the reconciliation account and migrate your old GL account data to it.

|  |
| --- |
| Caution SAP S/4HANA Cloud Public Edition supports G/L reduction, but not G/L migration. If you want to do G/L reduction on the cloud, you can replace the house bank account connectivity with a new bank reconciliation account. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Change | Choose the bank account to be changed from the account list view.For example, account 1133698 in DEBK1.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Edit | Choose the triangle button of account 1133698.Choose Edit.Choose the triangle button of the connectivity path. | House Bank Account Connectivity screen displays. |  |
| 5 | Reduce and Migrate G/L Account | Choose Migrate G/L Account, and the Target Bank Reconciliation Account field displays.Choose the target bank reconciliation account through search help.Note If no old GL account exist, or you don’t have to migrate the data, you don’t have to use Migrate G/L Account button.Choose Apply. |  |  |
| 6 | SAVE | Choose Save. | The bank account is changed (updated). |  |

#### Import Bank Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you import bank master data into the SAP S/4HANA system.

Prerequisites

Download a copy of the [linked bank data template file](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/SWIFT_Sample_Data.txt). You can also get it from the SWIFT website.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Import Bank Directories (BIC2S). |  |  |
| 3 | Import Bank Data | In the Open dialog box, browse to the location of the bank data text file, and choose Open. |  |  |
| 4 | Enter Data | Make the following entries and choose Execute:File Structure: Bank Directory SAP (swiftrefdata.com), BDECountry/Region Key: <bank country>, for example, DETest Run: Select (for test run), or Deselect (for actual run)NoteThe Bank country selection option restricts the quantity of data imported from the file to the countries that you specify. For example you can use this to split the countries into groups for processing in multiple program runs with different import parameters. If you do not specify a country, the system processes all the data records from the file whose ISO country code matches the two-character ISO country code of a country set up in the SAP system.Test Run checkbox: If you select this checkbox, the system does not update the data in the database when you execute the report. In a test run, the system processes the data and displays the planned changes in a list. The database is not updated.Delta Upload checkbox: If you select this checkbox, the system imports only the delta file instead of the full file.The Bank Key in Type 4 parameter controls which data (fields) is used from the file as the bank key if the bank key type 4 (assigned externally) is set for the relevant country in the country-specific checksSEPA mode (IBAN BIC) check box: Select this checkbox if you plan to transfer funds to a country as a SEPA payment only.Use IBAN Country Code checkbox: If you select this checkbox, the system uses the IBAN country code for the bank assignment.Branch Code XXX for HQ checkbox: If you select this checkbox, the system uses the dummy branch code XXX from the file to increase the 8-character BIC to the full 11 characters, for example: NDEASESSXXX. If you do not select this checkbox, the system transfers the BIC without the branch identifier, for example, NDEASESS. This parameter does not affect the full 11-character BICs. These are always transferred in full, for example, NDEASESSA21. You can use this parameter, for example, to also import a national bank directory where the dummy ID XXX is not used. This avoids duplicate entries where one has the XXX ID and the other does not.Mark for Deletion checkbox: If you select this checkbox, the system flags banks for deletion that are no longer valid in the SAP system.For Own Data Records Only (BDE) checkbox: If you select this checkbox, you restrict the quantity of banks flagged for deletion to those that were created with this program and file format. | The Import and Export Bank Accounts screen displays. |  |

#### Fields Enhancement for Bank Account Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

This function only applies to extensive system.

Purpose

A BADI is provided to implement definition of custom fields and its default value. You can use this function to define your field and set its default value through BADI coding, implementation tutorial is attached on the online document help of Cash & Liquidity Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Extensibility Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Custom Fields (F1481). |  |  |
| 3 | Create a Custom Field | On the Custom Fields tab, choose Create.Make the following entries.Business Context：Bank Account Master DataLabel：Custom fieldIdentifier：YY1_ custom fieldTooltip：custom fieldType：<Select one type>Choose Create and Edit. |  |  |
| 4 | Enable Field Usage | Choose UIs and Reports tab.Choose Enable Usage. |  |  |
| 5 | Publish Fields | Log on to the SAP Fiori launchpad as a Cash Management Specialist.Note You need to assign Administrator Role to User Cash Management Specialist, otherwise you won't see Adapt UI option.Open Manage Bank Accounts (F1366A).Choose the (>) button to go into detail of a bank account.Choose Cash_Specialist Icon on the upper right of the screen.Choose Adapt UI.Select one area.Choose Add: Field.Select the checkbox of the newly added field.Choose OK.Choose Publish.Choose Save&Exit. |  |  |
| 6 | Create a custom logic | Choose the Custom Logic tab.Choose Create.Make the following entries and choose Create.Business Context: Bank Account Master DataBAdI Description: Field Status Control for Bank Accounts in Workflow ProcessesImplementation Description: Enable edition in workflow.Implementation ID: YY1_ WF_TESTChoose Create.Input BADI code which is used to define default value of the field(s).For more information, you can refer to the tutorial video attached on the online help of Cash and Liquidity Management > Bank Relationship Management > Apps > Manage Bank Accounts > App Extensibility: Manage Bank Accounts.Choose Publish. |  |  |

### Maintain Bank Chain

Bank chains are used to make payments that are transferred through up to three intermediary banks before going to the beneficiary bank.

Before the implementation of this function, when making a payment to a business partner abroad, you had to specify your house bank and the business partner’s bank when processing payments. These two banks represented the start and end of the payment cycle and it was down to the house bank to determine via which banks the payment should be made. Using the bank chain function, you can now specify this bank chain yourself, leading to faster payment transaction processing and considerable cost savings through reduced bank charges.

For each payment, the payment program can determine a combination of intermediary banks that you previously defined. The order of the banks in the bank chain can depend on the following factors:

- House bank
- Supplier’s bank details
- Customer’s bank details
- Currency
- Payment method supplement

The system uses bank chains only for payments with payment methods that require a bank chain.

Bank chains are transferred each time a payment medium is created. The following formats are supported in this process:

- S.W.I.F.T MT101
- S.W.I.F.T MT103

#### Create Bank Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The recipient’s bank key and recipient’s bank account number of the bank chain is maintained in the Maintain Business Partner app not Manage Bank Account app. The sender’s bank key is maintained in Manage Bank Account app, and the sender’s bank account is the house bank account you maintained for the bank key. Make sure you have created the business partner and maintained corresponding bank key and bank account before testing.

Purpose

The purpose of this step is to create a bank chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Chains (F4004). |  |  |
| 3 | Create Bank Chain | Choose Create. | The Create Bank screen displays. |  |
| 4 | Enter Bank Data | Make the following entries:Business Partner: <Select one business partner>Country/Region Key of Sender Bank: AEBank Key of Sender Bank: 18121976Currency: AED |  |  |
| 5 | Create Intermediary Banks | Choose Items tab.Choose Add. |  |  |
| 6 | Enter Intermediary Bank Data | Make the following entries and choose Create.Type of Bank in Bank Chain: for example, 2 (Intermediary bank)Country Key of a Correspondent Bank: AEBank Key of a Correspondent Bank: 82080000Account Number of a Correspondent Bank: 2580061 |  |  |

#### Change Bank Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to change a bank chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Chains (F4004). |  |  |
| 3 | Edit Bank Chain | Input the filter and choose Go.Choose the triangle button of the bank chain. |  |  |
| 4 | Start to Edit | Choose Edit. Modify fields to your requirements. |  |  |
| 5 | Save | Choose Save. |  |  |

#### Delete Bank Chain

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to delete a bank chain.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Chains (F4004). |  |  |
| 3 | Delete Bank Chain (Option 1) | Input the filter and choose Go.Select the check box of the bank chain.Choose Delete.Choose Delete. | The selected object has been deleted. |  |

#### Check Bank Chain Information In Business Partner (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The receiver’s bank account is associated with the business partner, you can find the bank chain information via business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). |  |  |
| 3 | Search Business Partner | Choose Open BP.Press F4.Note If you can't see the fields mentioned below, select Change search criteria category and choose Partner by bank details by selecting the little down arrow next to the displayed search criteria category. Then you will get all the search criteria categories displayed.Choose Partner by bank details tab.Enter the following data and select Start Search:Bank Key: 18121986Bank Account: 0000000693123456Note If the search does not find anything, check if the Bank Account is maintained in the Business Partner Master Data.Or leave Bank Account field empty and select Start Search.Choose the line item and press Enter.Choose Enter. | The Create Bank screen displays. |  |
| 4 | Recipient Bank Chain | Make the following entry:Display in BP role: Financial Services BPChoose Payment Transactions Tab.Choose the radio button of one line item in the Bank Details.Choose Recpnt Bank Chains.Note Sender Bank Chains function is not activated in this version. | The selection area displays the sender’s bank information. |  |
| 5 | Bank Chain Assignment | Choose the check box of one line item in the selection area.Double click Bank Chain Assignment. | Bank chain assignment area displays the intermediary bank information. |  |

#### Schedule Delete Bank Chain Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to schedule jobs to delete bank chain.

Prerequisite

Schedule Delete Bank Chain Jobs is only used for deleting unused bank chain, which means the recipient bank account of the bank chain are no longer related to any business partner. In addition, the intermediary banks data should exist before using this job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Bank Chain Jobs (F4503). |  |  |
| 3 | Start Schedule Delete Bank Chain Jobs | Choose Create. | The New Job: Delete Bank Chains screen displays. |  |
| 4 | Enter Job Parameters | Make the following entries:Job Template: Delete Bank ChainsJob Name: Delete Bank ChainsChoose Step 2Start Immediately: <Select>Choose Step 3Bank Key Recipient: for example, 18121986Bank Key Sender: for example, 18121976Bank Account/IBAN Recip.: 0000000693123456Bank Ctry Recipient: AEBank Ctry Sender: AE |  | Note If below mentioned data don't work, you can leave all General Selection Criteria empty, which means the delete job will apply to all the unused bank chain. |
| 5 | Schedule Delete Bank Chain Jobs | Choose Schedule. |  |  |

## Appendix

### Remove Inconsistent Data after Closing a Bank Account (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

There might be some inconsistent data for a closed bank account. These data includes, bank determination data for payment, account determination data for bank transfer, Clearing account for receiving banks and the remaining house bank account data in G/L account, which can cause inconsistent check error. You can fulfill this step to check and remove the inconsistent data.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access Bank Determination SSCUI | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Accounts PayableIn the Automatic Payments row, choose the arrow button at the right of the row.In the right pane, for the Set Up Bank Determination for Payment Transactions row, choose Configure. |  |  |
| 3 | Remove Bank Determination Data | Select the check box of the company code that the closed bank account belongs to.Choose Bank Accounts Tab.Select the check box of the inconsistent bank determination data.Choose Delete.Choose Save. |  |  |
| 4 | Access Account Determination SSCUI | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Accounts PayableIn the General Payment Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Account Determination row, choose Configure. |  |  |
| 5 | Remove Account Determination Data | Input the company code that the closed bank account belongs to.Choose Enter.Select the check box of the inconsistent account determination data.Choose Delete.Choose Save. |  |  |
| 6 | Access Acct Transfer: Determing Receiving Bank’s Clearing Account SSCUI | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Accounts PayableIn the General Payment Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Clearing Accts for Receiving Bank for Acct. Transfer row, choose Configure. |  |  |
| 7 | Remove Receiving Bank’s Clearing Account | Select the check box of the inconsistent clearing account data.Choose Delete.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Bank Determination for Payment Transactions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Bank Determination for Payment Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Remove Bank Determination Data | Select the check box of the company code that the closed bank account belongs to.Choose Bank Accounts Tab.Select the check box of the inconsistent bank determination data.Choose Delete.Choose Save. |  |  |
| 4 | Open Define Account Determination | Go to the Business Processes Configuration app and search for the following activity: Define Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Remove Account Determination Data | Input the company code that the closed bank account belongs to.Choose Enter.Select the check box of the inconsistent account determination data.Choose Delete.Choose Save. |  |  |
| 6 | Open Define Define Clearing Accts for Receiving Bank for Acct. Transfer | On the Configuration Activities tab, search for the following activity: Define Clearing Accts for Receiving Bank for Acct. Transfer.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 7 | Remove Receiving Bank’s Clearing Account | Select the check box of the inconsistent clearing account data.Choose Delete.Choose Save. |  |  |

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
> Flagged while digesting this document, not verified: Define Settings for Bank Statements: the Configure Your Solution variant sets Transfer Mode (Intraday) to Bank Statement Items Only, while the SAP Central Business Configuration variant of the same step sets Balance and Bank Statement Items.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Export/Import Bank Accounts: the Overview Table says accounts are exported from the production system and imported into development and consolidation systems, while the Export purpose says configuration is done in the development system and accounts are exported from that system, and the Import step reports success 'into development system'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table gives 'GL Accounts are reduced and migrated' as the expected result for Delete Bank Account, but the GL Account Reduction section states the Public Edition supports G/L reduction but not G/L migration.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BFA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 102,659 chars in the whole document
