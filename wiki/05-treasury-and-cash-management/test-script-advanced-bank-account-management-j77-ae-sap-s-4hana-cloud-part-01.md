---
id: 05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01
title: "Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "SAP test script for J77_AE Advanced Bank Account Management: prerequisites, configuration and test steps for bank accounts, approvals and powers of attorney."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-account-management]
aliases: []
keywords: [Bank Account Management, advanced bank account management, bank account revision activation, bank account master data, payment approvers, powers of attorney, bank account contract types, bank account lifecycle, bank account closing, bank account applications]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx#lines-1-2888"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1308
topic: 05-treasury-and-cash-management/bank-account-management
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–2888 of the extracted text), extracted with `mammoth`. Grouped under **Bank Account Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Bank Account Management (J77_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 7](#_Toc232864111)

[2 Prerequisites 8](#_Toc232864112)

[2.1 System Access 8](#_Toc232864113)

[2.2 Roles 8](#_Toc232864114)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232864115)

[2.4 Business Conditions 11](#_Toc232864116)

[2.5 Preliminary Steps 11](#_Toc232864117)

[2.5.1 G/L Account Created for Bank Account 11](#_Toc232864118)

[2.5.2 Define Basic Settings 12](#_Toc232864119)

[2.5.3 Define Account Type (Optional) 15](#_Toc232864120)

[2.5.4 Notifications for Bank Account and Powers of Attorney 16](#_Toc232864121)

[2.5.5 Manage Workflows 19](#_Toc232864122)

[2.5.5.1 Manage Workflows for Bank Account 19](#_Toc232864123)

[2.5.5.2 Manage Workflow for Powers of Attorney and Email Notification 22](#_Toc232864124)

[2.5.6 Configure Sensitive Fields (Optional) 24](#_Toc232864125)

[2.5.7 Assign Form Template 27](#_Toc232864126)

[2.5.8 Define Output Parameter Determination 28](#_Toc232864127)

[2.5.9 Payment Approval Customizing 30](#_Toc232864128)

[2.5.10 Situation Handling Setting Up 34](#_Toc232864129)

[2.5.10.1 Situation Handling for Bank Account Activation in Dual Control 34](#_Toc232864130)

[2.5.10.1.1 Create a Team for Situation Monitoring 34](#_Toc232864131)

[2.5.10.1.2 Create Situation Types 35](#_Toc232864132)

[2.5.11 Powers of Attorney Customizing 37](#_Toc232864133)

[2.5.11.1 Define Activities for Powers of Attorney 37](#_Toc232864134)

[2.5.11.2 Define Authorization Groups for Powers of Attorney 38](#_Toc232864135)

[2.5.11.3 Define Channels for Powers of Attorney 40](#_Toc232864136)

[2.5.11.4 Profile Creation for Powers of Attorney 41](#_Toc232864137)

[2.5.11.5 Define Purpose for Powers of Attorney 43](#_Toc232864138)

[2.5.11.6 Assign Form Templates to Powers of Attorney Types 45](#_Toc232864139)

[2.5.12 Bank Account Contract Type 46](#_Toc232864140)

[2.5.12.1 Enable Bank Account Contract Type 46](#_Toc232864141)

[2.5.12.2 Define Account Type and Contract Type 48](#_Toc232864142)

[2.5.12.3 Define Repair Action for Bank Accounts 50](#_Toc232864143)

[2.5.12.4 Configure Origination Process and Manual Creation 52](#_Toc232864144)

[2.5.12.5 Configure Status and Bank Account Control Modes 55](#_Toc232864145)

[2.5.12.6 Configure Actions and Bank Account Control Modes 59](#_Toc232864146)

[2.5.12.7 Hide Tabs in Bank Account Master Data 61](#_Toc232864147)

[2.5.13 Manage Field Status Groups to Origination Process 63](#_Toc232864148)

[2.5.14 Disable Email Notification 69](#_Toc232864149)

[2.5.15 Manage My Substitutes 71](#_Toc232864150)

[2.5.16 Set Up Instant Balances (Optional) 72](#_Toc232864151)

[2.5.16.1 Enable Instant Balances 72](#_Toc232864152)

[2.5.16.2 Define Bank Accounts Settings – Instant Balances 72](#_Toc232864153)

[2.5.17 Set Rating Procedures and Ratings (Optional) 73](#_Toc232864154)

[3 Overview Table 76](#_Toc232864155)

[4 Test Procedures 87](#_Toc232864156)

[4.1 New Bank Account Application 87](#_Toc232864157)

[4.1.1 Submit Bank Account Applications 87](#_Toc232864158)

[4.1.2 Approve Bank Account Applications 88](#_Toc232864159)

[4.1.3 Create Bank Account for New Bank Account Application 89](#_Toc232864160)

[4.1.4 Withdraw Bank Account Application 90](#_Toc232864161)

[4.1.5 Confirm Bank Account Application Withdrawal 91](#_Toc232864162)

[4.2 Bank Account Master Data Processing with Advanced Bank Account Management 91](#_Toc232864163)

[4.2.1 Using Direct Revision Activation 92](#_Toc232864164)

[4.2.1.1 Create Bank Account 92](#_Toc232864165)

[4.2.1.1.1 Open Bank Account 92](#_Toc232864166)

[4.2.1.1.2 Create Bank Master Data 92](#_Toc232864167)

[4.2.1.1.3 Edit Bank Master Data 94](#_Toc232864168)

[4.2.1.1.4 Create Bank G/L Account 95](#_Toc232864169)

[4.2.1.1.5 Manage Banks Cash Management Data 95](#_Toc232864170)

[4.2.1.1.6 Create Bank Account 97](#_Toc232864171)

[4.2.1.1.7 Export Bank Account 102](#_Toc232864172)

[4.2.1.1.8 Import Bank Accounts 104](#_Toc232864173)

[4.2.1.2 Change Bank Account 105](#_Toc232864174)

[4.2.1.2.1 Notify Bank to Change 105](#_Toc232864175)

[4.2.1.2.2 Change Bank Account 105](#_Toc232864176)

[4.2.1.2.3 Update Bank G/L Account 106](#_Toc232864177)

[4.2.1.3 Repair Bank Accounts 110](#_Toc232864178)

[4.2.1.4 Close Bank Account and Cancel Closing 111](#_Toc232864179)

[4.2.1.4.1 Notify Bank to Close Account 111](#_Toc232864180)

[4.2.1.4.2 Close Bank Account and Cancel Closing 111](#_Toc232864181)

[4.2.1.5 Maintain Payment Approver for Multiple Bank Accounts (Direct Revision Activate) 116](#_Toc232864182)

[4.2.1.5.1 Add Payment Approver for Multiple Bank Accounts 116](#_Toc232864183)

[4.2.1.5.2 Change Payment Approver for Multiple Bank Accounts 118](#_Toc232864184)

[4.2.1.6 Upload Attachments for Bank Account 119](#_Toc232864185)

[4.2.2 Using Dual Control Revision Activation 121](#_Toc232864186)

[4.2.2.1 Create Bank Account 121](#_Toc232864187)

[4.2.2.1.1 Open Bank Account 121](#_Toc232864188)

[4.2.2.1.2 Create Bank Master Data 121](#_Toc232864189)

[4.2.2.1.3 Edit Bank Master Data 123](#_Toc232864190)

[4.2.2.1.4 Create Bank G/L Account 124](#_Toc232864191)

[4.2.2.1.5 Manage Banks Cash Management Data 124](#_Toc232864192)

[4.2.2.1.6 Create Bank Account 125](#_Toc232864193)

[4.2.2.1.7 Export Bank Account 131](#_Toc232864194)

[4.2.2.1.8 Import Bank Accounts 133](#_Toc232864195)

[4.2.2.2 Change Bank Account 134](#_Toc232864196)

[4.2.2.2.1 Notify Bank to Change 134](#_Toc232864197)

[4.2.2.2.2 Change Bank Account 134](#_Toc232864198)

[4.2.2.2.3 Update Bank G/L Account 135](#_Toc232864199)

[4.2.2.3 Close Bank Account and Cancel Closing 139](#_Toc232864200)

[4.2.2.3.1 Notify Bank to Close Account 139](#_Toc232864201)

[4.2.2.3.2 Close Bank Account and Cancel Closing 139](#_Toc232864202)

[4.2.2.4 Maintain Payment Approver for Multiple Bank Accounts (Dual Control Revision Activate) 144](#_Toc232864203)

[4.2.2.4.1 Add Payment Approver for Multiple Bank Accounts 145](#_Toc232864204)

[4.2.2.4.2 Change Payment Approver for Multiple Bank Accounts 147](#_Toc232864205)

[4.2.2.5 Upload Attachments for Bank Account 148](#_Toc232864206)

[4.2.2.6 Activate the Bank Account via Dual Control 149](#_Toc232864207)

[4.2.3 Using Two-Person Verification Revision Activation 151](#_Toc232864208)

[4.2.3.1 Create Bank Account 151](#_Toc232864209)

[4.2.3.1.1 Open Bank Account 151](#_Toc232864210)

[4.2.3.1.2 Create Bank Master Data 151](#_Toc232864211)

[4.2.3.1.3 Edit Bank Master Data 153](#_Toc232864212)

[4.2.3.1.4 Create Bank G/L Account 154](#_Toc232864213)

[4.2.3.1.5 Manage Banks Cash Management Data 154](#_Toc232864214)

[4.2.3.1.6 Create Bank Account 155](#_Toc232864215)

[4.2.3.1.7 Export Bank Account 161](#_Toc232864216)

[4.2.3.1.8 Import Bank Accounts 163](#_Toc232864217)

[4.2.3.1.9 Approve Bank Account Request for Two-Person Verification 164](#_Toc232864218)

[4.2.3.2 Change Bank Account 166](#_Toc232864219)

[4.2.3.2.1 Notify Bank to Change 166](#_Toc232864220)

[4.2.3.2.2 Change Bank Account 166](#_Toc232864221)

[4.2.3.2.3 Withdraw Bank Account Request (Optional) 167](#_Toc232864222)

[4.2.3.2.4 Update Bank G/L Account 168](#_Toc232864223)

[4.2.3.3 Repair Bank Accounts 172](#_Toc232864224)

[4.2.3.4 Close Bank Account and Cancel Closing 173](#_Toc232864225)

[4.2.3.4.1 Notify Bank to Close Account 173](#_Toc232864226)

[4.2.3.4.2 Close Bank Account and Cancel Closing 173](#_Toc232864227)

[4.2.3.5 Maintain Payment Approver for Multiple Bank Accounts (Two-Person Verification Revision Activate) 178](#_Toc232864228)

[4.2.3.5.1 Add Payment Approver for Multiple Bank Accounts 179](#_Toc232864229)

[4.2.3.5.2 Change Payment Approver for Multiple Bank Accounts 181](#_Toc232864230)

[4.2.3.5.3 Verify the Bank Account after Payment Approver Maintenance 182](#_Toc232864231)

[4.2.3.6 Upload Attachments for Bank Account 183](#_Toc232864232)

[4.2.3.7 Approve Bank Account Request via Two-Person Verification 184](#_Toc232864233)

[4.2.3.7.1 Check Bank Account Change Request 184](#_Toc232864234)

[4.2.3.7.2 Option 1: Approve Bank Account Request by Using Manage Bank Account 185](#_Toc232864235)

[4.2.3.7.3 Option 2: Approve Bank Account Request by Using Approve Bank Account Changes App 186](#_Toc232864236)

[4.2.3.8 Bank Account Change Request Overview – Two-Person Verification 186](#_Toc232864237)

[4.2.4 Using Workflow Revision Activation 187](#_Toc232864238)

[4.2.4.1 Create Bank Account 188](#_Toc232864239)

[4.2.4.1.1 Open Bank Account 188](#_Toc232864240)

[4.2.4.1.2 Create Bank Master Data 188](#_Toc232864241)

[4.2.4.1.3 Edit Bank Master Data 190](#_Toc232864242)

[4.2.4.1.4 Create Bank G/L Accounts 191](#_Toc232864243)

[4.2.4.1.5 Manage Banks Cash Management Data 191](#_Toc232864244)

[4.2.4.1.6 Create Bank Account Request 193](#_Toc232864245)

[4.2.4.1.7 Export Bank Accounts 199](#_Toc232864246)

[4.2.4.1.8 Import Bank Accounts 200](#_Toc232864247)

[4.2.4.1.9 Change Bank Account During Workflow (Optional) 202](#_Toc232864248)

[4.2.4.2 Change Bank Account 203](#_Toc232864249)

[4.2.4.2.1 Receive Change Request from Requester 203](#_Toc232864250)

[4.2.4.2.2 Create Bank Account Change Request 203](#_Toc232864251)

[4.2.4.2.3 Change Bank Account During Workflow (Optional) 205](#_Toc232864252)

[4.2.4.2.4 Notify Bank to Change 206](#_Toc232864253)

[4.2.4.2.5 Update Bank G/L Account 207](#_Toc232864254)

[4.2.4.3 Repair Bank Accounts 210](#_Toc232864255)

[4.2.4.4 Close Bank Account and Cancel Closing 211](#_Toc232864256)

[4.2.4.4.1 Receive Bank Account Closing Request from Requester 211](#_Toc232864257)

[4.2.4.4.2 Notify Bank to Close Account 211](#_Toc232864258)

[4.2.4.4.3 Close Bank Account and Cancel Closing 212](#_Toc232864259)

[4.2.4.4.4 Change Bank Account During Workflow (Optional) 217](#_Toc232864260)

[4.2.4.5 Maintain Payment Approver in Multiple Bank Accounts (Workflow Revision Activate) 217](#_Toc232864261)

[4.2.4.5.1 Add Payment Approver for Multiple Accounts 219](#_Toc232864262)

[4.2.4.5.2 Change Payment Approver in Multiple Bank Accounts 221](#_Toc232864263)

[4.2.4.6 Upload Attachments for Bank Account 222](#_Toc232864264)

[4.2.4.7 Cancel Bank Accounts Requests 223](#_Toc232864265)

[4.2.4.8 Approve Bank Account Request via Workflow 224](#_Toc232864266)

[4.2.4.9 Create Bank Account with Bank Correspondence 226](#_Toc232864267)

[4.3 Create In-House Bank Account via eBAM 226](#_Toc232864268)

[4.4 Powers of Attorney 231](#_Toc232864269)

[4.4.1 Manage Payment Approval Rules 231](#_Toc232864270)

[4.4.2 Create Powers of Attorney 233](#_Toc232864271)

[4.4.3 Approve Powers of Attorney 236](#_Toc232864272)

[4.4.3.1 Approve Powers of Attorney via Dual Control 236](#_Toc232864273)

[4.4.3.2 Approve Powers of Attorney via Workflow 237](#_Toc232864274)

[4.4.3.3 Approve Powers of Attorney with Basic Bank Account Management User (Optional) 238](#_Toc232864275)

[4.4.4 Create PDF for Powers of Attorney 240](#_Toc232864276)

[4.4.5 Revoke Powers of Attorney 240](#_Toc232864277)

[4.4.6 Implement Powers of Attorney 241](#_Toc232864278)

[4.4.7 Compare Powers of Attorney 244](#_Toc232864279)

[4.4.8 Start Data Collection 245](#_Toc232864280)

[4.4.9 Process Data Collection 246](#_Toc232864281)

[4.4.10 Destruct and Block Powers of Attorney 247](#_Toc232864282)

[4.4.10.1 Destruct Powers of Attorney 247](#_Toc232864283)

[4.4.10.2 Block Powers of Attorney 248](#_Toc232864284)

[4.5 Manage Bank Account Hierarchies 249](#_Toc232864285)

[4.5.1 Create Bank Account Group 250](#_Toc232864286)

[4.5.2 Edit Bank Account Group 251](#_Toc232864287)

[4.5.3 Delete Bank Account Group 252](#_Toc232864288)

[4.6 Review Bank Account and Destruct Bank Account Reviews (Workflow Mode) 253](#_Toc232864289)

[4.6.1 Initiate Review Bank Account 253](#_Toc232864290)

[4.6.2 Review Bank Accounts (Workflow) 255](#_Toc232864291)

[4.6.3 Destruction of Bank Account Reviews 256](#_Toc232864292)

[4.6.4 Set Up Email Notifications 257](#_Toc232864293)

[4.6.5 Set Up More Review Steps (Optional) 259](#_Toc232864294)

[4.7 Assign Rating Procedures and Ratings to Business Partner 262](#_Toc232864295)

[4.8 Bank Account Report and Fact Sheet 263](#_Toc232864296)

[4.8.1 Foreign Bank Account Report 263](#_Toc232864297)

[4.8.2 Bank (Fact Sheet) 265](#_Toc232864298)

[4.8.3 House Bank (Fact Sheet) 266](#_Toc232864299)

[4.8.4 House Bank Account (Fact Sheet) 267](#_Toc232864300)

[5 Appendix 269](#_Toc232864301)

[5.1 Split Technical Bank Accounts (Optional) 269](#_Toc232864302)

[5.2 Migrate Bank Control Keys (Optional) 270](#_Toc232864303)

[5.3 Import Existing Bank Account Group (Optional) 270](#_Toc232864304)

[5.4 Bank Relationship Overview 272](#_Toc232864305)

[5.5 Succeeding Processes 273](#_Toc232864306)

[5.6 Configuration 273](#_Toc232864307)

## Purpose

Overview

With Advanced Bank Account Management, the cash managers and the bank accountants can manage the bank and account master data centrally and maintain signatories in multiple bank accounts. The result of the maintenance can be activated with different control patterns. They can also view the bank and bank account related master data with reports and fact sheets and look at an annual review.

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
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Data Privacy Specialist | SAP_BR_DATA_PRIVACY_SPECIALIST | Data Protection and Privacy - Master Data / Data Protection and Privacy | SAP_CA_SPT_DPP_PC / SAP_BR_DATA_PRIVACY_SPECIALIST |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |
| Payment Specialist - In-House Banking | SAP_BR_PAYM_SPECIALIST_IHB | In-House Bank | SAP_FIN_SPT_FSCM_PF_IHB_PC | Suggested sample user PAYM_SPECIALIST_IHB representing the business role Payment Specialist in-house banking. |

|  |
| --- |
| Note During testing, cash management specialist and configuration expert can share the same user ID, but cash manager and cash management specialist must be separate user IDs due to segregation of duty: cash management specialist creates the change request, cash manager approves it, the creator should not be the approver. |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data table below. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default Values You can test the scope item with other SAP Best Practices default values that have the same characteristics. Review your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master Data You can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |
| Chart of Accounts | YCOA |  | Chart of accounts |
| Bank Account Number | 000000069312345600000006931234560000000033108888 |  | Bank account number |
| Bank Key | 181219761812198688800011 |  | Bank key |
| Bank Name | Bank 3 |  | Bank name |
| House Bank | AEBK1/AEAC1AEBK2/AEAC2 |  | House bank |
| House Bank ID | AEBK3 |  | House bank ID |
| House Bank Account | AEAC3 |  | House bank account |
| G/L Account | 1100100011003000 |  | G/L account for bank account |
| SWIFT/BIC | NBADAEAADIR |  | SWIFT/BIC |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 31N - Situation Handling | You install this scope item for the situation handling steps. |

### Preliminary Steps

If you choose to use the existing sample data and standard configuration, you can skip the following steps:

- (Note: using the Fiori App)

If you want to change the standard settings, you can configure it in company code level with configuration activity 104351 Define Settings for Bank Statements in bank account level with app Define Bank Account Settings - Bank Statements (F5488) and in bank statement level with configuration activity 103635 Define Parameter Set.

#### G/L Account Created for Bank Account

A general ledger (G/L) account is a chronological accounting record used to track financial transaction. The G/L account is a structure that records value movements in a company. As a prerequisite, you must have already created a G/L account 11001000.

|  |
| --- |
| Caution Instructions provided assume that you are only implementing one of the four Bank Account Master Data Procedures described in the [Purpose](#unique_1) [page ] 1 section. If you are implementing and testing more than one procedure, especially in a single environment, you cannot use the same Master Data values for more than one procedure type. You must have additional Master Data values created, for example G/L account numbers, bank keys, and so on, and then use these different values in each procedure. |

#### Define Basic Settings

Purpose

Within the Advanced Bank Account Management scope item, the following four procedures are described:

1. Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Direct Revision Activate
2. Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate
3. Maintian Payment Approver in Multiple Bank Accounts with Full Cash Management and Two-Person Verification Revision Activate
4. Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Workflow Revision Activate

|  |
| --- |
| Note Change Bank Account During Workflow If you are going to change the mode from "workflow" to others, you need to make sure all bank account requests have been approved. |

|  |
| --- |
| Caution All of the Full Cash Management versions require an additional license for SAP Cash Management powered by SAP HANA.If you activate Full Cash Management and Central Business Configuration, you must execute the Define Basic Settings step to manually set the mode to full cash mode. |

In this preliminary activity, you choose which one of the following procedures to use for your implementation:

1. To use Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Direct Revision Activate, use the following settings:
    - Cash Scope = 02
    - Bank Account Control Mode = 01 Direct Change
2. To use Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate, use the following settings:
    - Cash Management Scope = 02
    - Full Scope & Bank Account Revision = 02 Activate via Dual Control
3. To use Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Two-Person Revision Activate, use the following settings:
    - Cash Scope = 02
    - Bank Account Control Mode = 04 Two-Person Verification
4. To use Maintaining Payment Approver in Multiple Bank Accounts with Full Cash Management and Workflow Revision Activate, use the following settings:
    - Request Grouping = 01

|  |
| --- |
| Note Group into a Single Change Request. |

-
    - Full Scope & Bank Account Revision = 03 Workflow

|  |
| --- |
| Note Request Grouping is used in activate via workflow mode. You group the change requests by selecting the following: |

-
    -
        - Group into a Single Change Request

Change requests for each bank account with Payment Approver update are grouped into a single mass change request. Once the workflow is enabled, the single mass change request is sent to all the users who are authorized to process mass change requests. With this setting, we recommend that you define the approvers' responsibilities to include all the company codes and account types.

-
    -
        - Group by Company Code

company codes.

-
    -
        - Group by Account Type

Change requests for each bank account with Payment Approver updates are grouped by account type into multiple mass change requests. Once the workflow is enabled, the multiple mass change requests are sent to users who are assigned to a certain account type. With this setting, we recommend that you define the approvers' responsibilities to include all company codes, but only specific account types.

-
    -
        - Group by Company Code and Account Type

Change requests for each bank account with Payment Approver updates are grouped by company code and account type into multiple mass change requests. Once the workflow is enabled, the multiple mass change requests are sent to users who are assigned to the exact combination of company code and account type.

With this setting, you can define the approvers' responsibilities to include only specific company codes and account types.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the General Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Basic Settings row, choose Configure. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Scope and Bank Acct Activation for your implementation based on the previously described procedures.Note The default setting is option 2: Maintaining Signatory in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate. To use Maintaining Signatory in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate, use the following settings:Cash Management Scope = 02Full Scope & Bank Account Revision = 02 Activate via Dual Control |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Management Scope and Bank Account Revision for your implementation based on the previously described procedures.Note The default setting is option 2: Maintaining Signatory in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate. To use Maintaining Signatory in Multiple Bank Accounts with Full Cash Management and Dual Control Revision Activate, use the following settings:Cash Management Scope = 02Full Scope & Bank Account Revision = 02 Activate via Dual Contro |  |  |

The check box Enable Snapshot is used for the snapshot of historic cash report. This check box can only be selected and saved when cash value is Full Scope. If the value of cash scope is Basic Scope, it can’t be saved once the check box of Enable Snapshot is selected. Once the check box of Enable Snapshot is selected and saved, the function of snapshot of historic cash report is activated.

|  |
| --- |
| Remember Define Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct in the SSCUI Define Basic Settings. |

#### Define Account Type (Optional)

Purpose

This activity describes the approach to define account type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Search for and choose Define Settings for Bank Account Master Data or SSCUI ID 102336 on the search filter.Choose Configure for the Define Settings for Bank Account Master Data Step Name. | The Change View "Account Type Definition": Overview screen is displayed. |  |
| 3 | Maintain Account Type Definition | Select the Account Type Definition pane.Make the following entries and choose Save:Type: 10Account Type Description: Current Account |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Settings for Bank Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Settings for Bank Account Master Data screen is displayed. |  |
| 3 | Maintain Account Type Definition | Choose Account Type Definition.Choose New Entries.Make the following entries and choose Save:Type: 10Account Type Description: Current Account |  |  |

#### Notifications for Bank Account and Powers of Attorney

Purpose

Notification is used to notify responsible person to process of information or problems that might be encountered in the business processes of your company. In Advanced Bank Account Management, Provider ID BAM_NOTIFICATION_PROVIDER and SAP_BUSINESS_WORKFLOW are predelivered and activated by default in the Cloud system.

- BAM_NOTIFICATION_PROVIDER

This notification provider object is used to create, change, and close bank account in dual control mode and to review bank account. When Cash Manager triggers the bank account review process, a notification will be sent out to notify Cash Specialist to review the bank account. On condition that you have set the Define Basic Settings to Dual Control. When you create, change or close a bank account, a notification will be sent out to notify the responsible person to activate the bank account.

- SAP_BUSINESS_WORKFLOW

This notification provider object is used to create, change, and close bank account in workflow mode. As long as workflow is triggered, notification will be sent out to Cash Manager to approve the bank account.

In the on-premise system, if you want to deactivate the notification, you can go to IMG path: ABAP Platform > Notification Channel > Notification Channel Provider Enablement > Administration > Notification Provider Setting > Manage Notification Provider, and deselect the Is Active checkbox.

To check the notification, you can log on to SAP Fiori as the responsible user, for example, Cash Manager. Choose the Notifications button on the top right of the screen, you can find the notifications. Choose the notification by detail, it will navigate to the process page. For example, by choosing the review bank accounts notification, it will navigate to Review Bank Accounts app to review and process the bank account.

For Email Notification, it requires the extensibility test system to perform its functionality. The following table below lists the predefined email templates for bank account and powers of attorney.

| Scenario | Send Email When | Recipient | Template ID |
| --- | --- | --- | --- |
| Flexible Workflow | A workflow change request has been triggered. | Authorized approversApprovers are defined in the Manage Workflows - For Bank Accounts app. | SWF_CRT_NOTIFY_RECIPIENTS |
| An approver has approved the change request. | Change submitter | FCLM_BAM_REQ_APPROVED_EMAIL |  |
| An approver has rejected the change request. | Change submitter | FCLM_BAM_REQ_REJECTED_EMAIL |  |
| Dual Control | A bank account has been submitted for activation. | Users who are authorized to activate bank accounts (authorization object F_CLM_BAM) , activity 63 Activate) | FCLM_BAM_REV_SUBMITTED_EMAIL |
| A bank account has been activated. | Change submitter | FCLM_BAM_REV_ACTIVATED_EMAIL |  |
| Two-Person Verification | An approver has approved the change. | Change submitter | FCLM_BAM_REV_APPROVED_EMAIL |
|  | An approver has rejected the change. | Change submitter | FCLM_BAM_REV_REJECTED_EMAIL |
| Bank Account Review | A bank account review has been started. | Users who are authorized to review bank accounts (authorization object F_CLM_BAM) , activity 31 Confirm) | FCLM_BAM_INI_REVIEW_EMAIL |
|  | A bank account review has been completed. | Review submitter | FCLM_BAM_REQ_REVIEWED_EMAIL |
| Bank Account Application | A bank account application has been approved. | Applicant | FCLM_BAM_BAOR_ACT_APPROVED |
|  | A bank account application has been rejected. | Applicant | FCLM_BAM_BAOR_ACT_REJECTED |
|  | A withdrawal of bank account application has been submitted. | Applicant | FCLM_BAM_BAOR_CANCEL_REQ |
|  | A withdrawal of bank account application has been confirmed by an approver. | Applicant | FCLM_BAM_BAOR_CANC_REQ_APR |
|  | A bank account application has been submitted for approval. | Applicant | FCLM_BAM_BAOR_ACTIVATION_REQ |
|  | A withdrawal of bank account application can't be performed because the bank account has already been created and activated. | Applicant | FCLM_BAM_BAOR_CANC_REQ_REJ |
|  | A withdrawal of bank account application has been automatically confirmed because the application has not yet been approved. | Applicant | FCLM_BAM_BAOR_REQ_CANCELLED |
| Powers of Attorney | A powers of attorney pass the deadline | Change Submitter | FCLM_POA_DEADLINE |
|  | A powers of attorney has been approved | Change Submitter | FCLM_POA_WF_RESULT_APPROVED |
|  | A powers of attorney has been rejected | Change Submitter | FCLM_POA_WF_RESULT_REJECTED |

You can customize predefined email templates by following steps:

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Extensibility Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates - Deprecated (F1306).Note This App is only availabe for extensibility test system. | The Maintain Email Templates view displays. |  |
| 3 | Copy Email Template | Search for the Email Template, for example: SWF_CRT_NOTIFY_RECIPIENTS |  |  |
| 4 | Copy Email Template | Select the Email Template radio button.Choose Copy.In the dialog box, enter the name: YY1_78500050_CRT_10Choose Copy. | Email Template is copied on the Custom tab. |  |
| 5 | Customize Email Template | Choose the Custom tab.Choose the Email Template you've copied.You can customize it with your own settings. |  |  |

|  |
| --- |
| Note Once you have copied and saved a custom email template, the system uses the copied template for sending emails. If no custom email template exists, the system will use the predefined email templates. |

#### Manage Workflows

This activity describes the approach to configure workflows for Bank Account Management, Powers of Attorney and Powers of Attorney Notifications.

##### Manage Workflows for Bank Account

Purpose

This activity describes the approach to begin the bank account management workflow process.

Prerequisite

If you are using the SAP S/4HANA system, ensure that the basic Customizing for workflow is complete. To review your on-premise workflow configuration, access IMG > SAP NetWeaver > Application Server > Business Management > SAP Business Workflow > Maintain Standard Settings or use transaction code SWU3.

If the basic Customizing for workflow is not complete, contact your system administrator to make the necessary modification. For more information, see the SAP Help Portal.

Teams need to be created in the Manage Teams and Responsibilities (F2412) app via the user Business_Process_Spec to specify the responsibilities for Review Process. Refer to test script Responsibility Management (1NJ) for a step-by-step description. Choose Create to enter the following values to create the new Team.

Name: Change to Team for BAM

Status: Enabled

Type: SFCLM0

On the Team Owners tab, use the Create button to add:

Business Partner: <user ID>, for example, Configuration Expert - Business Process Configuration

On the Team Members tab, use the Create button to add:

Business Partner: <Enter the User Id as the Approver, for example Cash Manager>

Business Partner: <Enter the User Id as the Approver, for example Cash Specialist>

|  |
| --- |
| Note The business user should be the business partner associated with an SAP user, if you are not able to find the user, please follow the [link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/3d8bfb472fce49d2a776a353f4d201b3.html) to create it. |

|  |
| --- |
| Note To display the connection between Business Partner, Cash Manager and User ID, please refer to the search help. Generic users are described in the Last Name field. |

Functions: SFCLM_APR

|  |
| --- |
| Note SAP delivers initial content Type: FCLM0 and Function: FCLM_APR. Due to the naming convention conflict, SAP now delivers the new content of Type: SFCLM0 and Function: SFCLM_APR.FCLM0 and FCLM_APR have been removed from our content. Existing customers who have implemented FCLM0 and FCLM_APR are unable to remove the entry from their customer system. We recommend existing customers use an alternate prefix. For example, SFCLM0 and SFCLM_APR.Don't use FCLM_APR, if you selected the team type SFCLM0. Use the same prefix for both Type and Function. |

Company Code: <Enter the company code the team is responsible for>

Account Type: <Enter the account type the team is responsible for>

|  |
| --- |
| Note If you leave Company Code and Account Type blank, you need to set the request grouping to 00; If you have set restriction on Company Code, and leave Account Type blank, you need to set the request grouping to 01; If you leave Company Code blank and have set restriction on Account Type, you need to set the request grouping to 02; If you have set both restriction on Company Code and Account Type, you need to set request grouping to 03. You can refer to [Define Basic Settings](#unique_9) [page ] 12 part for request grouping setting. |

After the Team is created, you should follow the below procedures to create one workflow template per bank account management workflow process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Workflows - For Bank Accounts (F2796). | The Manage Workflows view displays. |  |
| 3 | Create Workflow Template | On the current page, choose Create.Workflow Name: BAM_TeamIn the Start Conditions tab, make the following entries:Only start the workflow if all of the following preconditions are met: NoneNote This field is used to define preconditions to trigger workflow process.Other precondition selections are:Noneworkflow process will be triggered for all situationsAccount Action: workflow process is restricted to the account action you choose. For example, if you choose 01, trigger workflow process can only be triggered by creating a new bank account.Account Type: workflow process is restricted to the account type you choose. For example, if you choose 01 workflow process can only be triggered for current account.Company Code: workflow process is restricted to the company code you choose. For example, if you choose 3310 workflow process can only be triggered by the bank accounts that belong to company code 3310.Change Request Creator: workflow process is restricted to the selected request creator.Choose the Steps tab and choose Create. | A Process Request of Changing Bank Accounts view displays. |  |
| 4 | Enter Criteria | In the New Step dialog box, in the Header section, make the following entries:Step Name: Bank Account Manage workflow request ProcessStep Type: Process Request of Changing Bank AccountsNote Type Process Request of Changing Bank Accounts is used for normal workflow approval process. If you choose type Automatically approve bank account change request. The system will automatically approve the bank account.In the Recipients section, make the following entry:Role: for example, Function for Approving Bank Account RequestsStep to be completed by: <Choose One of the recipients>Note You can select this field on condition you have chosen the Step Type as Process Request of Changing Bank AccountOne of the recipients: Bank account can be approved by one of the approvers.All of the recipients: Bank account have to be approved by all the approvers.In the Exception Handling section, make the following entries:Required Action： Do NothingAction Result：Cancel WorkflowNote If you choose Cancel Workflow, the workflow will be cancelled after the workflow request is rejected by the approver. If you choose Restart Workflow, the workflow request will repeat pop up in the approver’s My Inbox App, until the workflow requester cancelled the workflow request.Choose Create.Choose Save. | Workflow successfully created notification appears and the Workflow Details view displays. |  |
| 5 | Activate the Workflow Template | Choose Activate on the top right of the view. | Workflow is activated successfully and the Manage Workflow view displays. |  |
| 6 | Adjust the Order | On the Workflow template list page, choose Define Order.On the Define Order dialog box, select the newly created workflow and choose the Moves the selected workflow to the top icon and Save. | Order is saved successfully. |  |

##### Manage Workflow for Powers of Attorney and Email Notification

Purpose

This activity describes the approach to begin the powers of attorney workflow and Email Notification process.

Prerequisite

If the basic Customizing for workflow is not complete, contact your system administrator to make the necessary modification. For more information, see the SAP Help Portal.

Teams need to be created in the Manage Teams and Responsibilities (F2412) app via the user Business_Process_Spec to specify the responsibilities for Review Process. Refer to test script Responsibility Management (1NJ) for a step-by-step description. Choose Create to enter the following values to create the new Team.

Name: POA Workflow

Description: Powers of Attorney Workflow

Status: Enabled

Type: SFCLM_POA

On the Team Owners tab, use the Create button to add:

Business Partner: <user ID>, for example, Configuration Expert - Business Process Configuration

On the Team Members tab, use the Create button to add:

Business Partner: <Enter the User Id as the Approver, for example Cash Manager>

Business Partner: <Enter the User Id as the Approver, for example, Cash Specialist>

|  |
| --- |
| Note The business user should be the business partner associated with an SAP user, if you are not able to find the user, please follow the [link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/3d8bfb472fce49d2a776a353f4d201b3.html) to create it. |

|  |
| --- |
| Note To display the connection between Business Partner, Cash Manager and User ID, please refer to the search help. Generic users are described in the Last Name field. |

Functions: SFCLM_POAA;SFCLM_POAN

After the Team is created, you should follow the below procedures to create one workflow template per powers of attorney workflow process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Workflows - For Bank Accounts (F2796). | The Manage Workflows view displays. |  |
| 3 | Create Workflow Template | On the current page, choose the triangle button beside the workflow.On the dropdown list, choose Power of Attorney Approval.Choose Create.Workflow Name: POA_Team | A Process Request of Changing Bank Accounts view displays. |  |
| 4 | Enter Criteria | On Steps tab, choose Create.In the New Step dialog box, in the Header section, make the following entries:Step Name: Powers of Attorney workflow request ProcessStep Type: Approve POAIn the Recipients section, make the following entry:Role: for example, Powers of Attorney ApprovalOne of the recipients: Bank account can be approved by one of the approvers.All of the recipients: Bank account have to be approved by all the approvers.In the Exception Handling section, make the following entries:Required Action: Do NothingAction Result: Cancel WorkflowNote If you choose Cancel Workflow, the workflow will be cancelled after the workflow request is rejected by the approver. If you choose Restart Workflow, the workflow request will repeatly pop up in the approver’s My Inbox App, until the workflow requester cancel the workflow request.Choose Create.Choose Save. | Workflow successfully created notification appears and the Workflow Details view displays. |  |
| 5 | Activate the Workflow Template | Choose Activate on the top right of the view. | Workflow is activated successfully and the Manage Workflow view displays. |  |
| 6 | Adjust the Order | On the Workflow template list page, choose Define Order.On the Define Order dialog box, select the newly created workflow and choose the Moves the selected workflow to the top icon and Save. | Order is saved successfully. |  |
| 7 | Create Workflow for POA Email Notification | Repeat step 2-6 to create a workflow with Role: Power of Attorney NotificationNote Step Notification for Bank Account and Powers of Attorney should be performed to copy powers of attorney related templates: FCLM_POA_DEADLINE, FCLM_POA_WF_RESULT_APPROVED, and FCLM_POA_WF_RESULT_REJECTED. |  |  |

#### Configure Sensitive Fields (Optional)

Purpose

This activity describes the approach to configure the sensitive fields for workflow process. Only the bank account sensitive fields can trigger a workflow process.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241).Choose Configure Your Solution.Search and choose Define Settings for Bank Account Master Data or SSCUI ID 102336 on the search filter.Choose Configure on the Define Settings for Bank Account Master Data item. | The Define Settings for Bank Account Master Data screen is displayed. |  |
| 3 | Maintain Selection Variant | In the Dialog Structure panel, double-click Define Selection Variants for Sensitive Fields.Choose New Entries.Make the following entries and choose Save:Selection ID: Z001Field Name: Account TypeSign: IncludeOption: Equal: Single ValueLow: 01High: 03 |  |  |
| 4 | Maintain Sensitive Field | Double-click Sensitive Fields for Activated Bank Accounts.Choose New Entries.Make the following entries and choose Save:Object: <Choose an object>Field Name: <a field by search help>Restriction: Selection VairantRestriction Value: Choose the selection ID you previously created, for example, Z001Inactive: <Unchecked>Note SAP supports the restriction settings of account type and company code. You set the restriction criteria in Maintain Selection Variant step, then you assign the selection variant to the sensitive field. Take the above parameters as an example, selection ID Z001 restrict the sensitive field to account type with value 01 to 03. If you choose the Restriction as selection variant and Restriction value as Z001, the sensitive field valid for account type 01 to 03. If you leave the Restriction and RestrictionValue fields blank, the sensitive field will be valid for all situation. The Inactive button is used for deactivating the restriction setting, you can deactivate this sensitive restrictions by select the check box of Inactive. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Settings for Bank Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Settings for Bank Account Master Data screen displays. |  |
| 3 | Maintain Selection Variant | Choose Define Selection Variants.Choose New Entries.Make the following entries and choose Save:Selection ID: Z001Field Name: Account TypeSign: IncludeOption: Equal: Single ValueLow: 01High: 03 |  |  |
| 4 | Maintain Sensitive Field | Choose Sensitive Fields for Activated Bank Accounts.Choose New Entries.Make the following entries and choose Save:Object: <Choose an object>Field Name: <a field by search help>Restriction: Selection VairantRestriction Value: Choose the selection ID you previously created, for example, Z001Inactive: <Uncheck>Note SAP supports the restriction settings of account type and company code. You set the restriction criteria in Maintain Selection Variant step, then you assign the selection variant to the sensitive field. Take the above parameters as an example, selection ID Z001 restrict the sensitive field to account type with value 01 to 03. If you choose the Restriction as selection variant and Restriction value as Z001, the sensitive field valid for account type 01 to 03. If you leave the Restriction and RestrictionValue fields blank, the sensitive field will be valid for all situation. The Inactive button is used for deactivating the restriction setting, you can deactivate this sensitive restrictions by select the check box of Inactive. |  |  |
| 5 | Maintain Sensitive Field | Choose Sensitive Fields for Bank Accounts Opened at Bank.Choose New Entries.Make the following entries and choose Save:Object: <Choose an object>Field Name: <a field by search help>Restriction: Selection VairantRestriction Value: Choose the selection ID you previously created, for example, Z001Inactive: <Deselect>Note SAP supports the restriction settings of account type and company code. You set the restriction criteria in Maintain Selection Variant step, then you assign the selection variant to the sensitive field. Take the above parameters as an example, selection ID Z001 restrict the sensitive field to account type with value 01 to 03. If you choose the Restriction as selection variant and Restriction value as Z001, the sensitive field valid for account type 01 to 03. If you leave the Restriction and RestrictionValue fields blank, the sensitive field will be valid for all situation. The Inactive button is used for deactivating the restriction setting, you can deactivate this sensitive restrictions by select the check box of Inactive. |  |  |

#### Assign Form Template

Prerequisites

A form template has been predefined by your Output Management team.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241).Click Configure Your Solution.Search Assign Form Template on the search filter.Choose the configuration item Output Control.Choose Configure button on the Assign Form Templates step. | The Change View "Form Template": Overview screen is displayed. |  |
| 3 | Add Form Template | Choose New Entries.Make the following entries and choose Save:Application Object Type: Bank_AccountOutput Type: Bank_CorrespondenceForm Type: 01Form Template: FCLM_BAM_ACCOUNT_CLOSERepeat these steps for the FCLM_BAM_SIGNATORY_UPDATE form template. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Form Templates | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Form Templates.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Form Templates screen displays. |  |
| 3 | Add Form Template | Choose New Entries.Make the following entries and choose Save:Appl.Object Type: Bank_AccountOutput Type: Bank_CorrespondenceForm Template: FCLM_BAM_ACCOUNT_CLOSERepeat these steps for the FCLM_BAM_SIGNATORY_UPDATE form template. |  |  |

#### Define Output Parameter Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

Relevant output parameters have been configured in the background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen is displayed. |  |
| 3 | Choose Show Rules for | Show Rules for: Bank Correspondence |  |  |
| 4 | Choose the Determination Step | Choose Output Type in the Determination Step field, and maintain the following entries in Table Contents.Output Type: Bank_CorrespondenceDispatch Time: 1 (Immediately)Choose Receiver in the Determination Step field, and maintain the following entries in Table Contents:Role: EXExclusive Indicator: X (true)Choose Channel in the Determination Step field, and maintain the following entries in Table ContentsChannel: EMAIL (Email)Choose Print Settings in the Determination Step field, and maintain the following entries in Table Contents:Print Queue: DEFAULTChoose Email Settings in the Determination Step field, and maintain the following entries in Table Contents:For Action = 04 (Change Signatory)Note If necessary, expand the Maintain Business Rules section.Choose Edit.In the Table Contents section, choose (Insert New Row) and make or verify the following entries:#: <next higher number>From the dropdown in each column, choose Direct Value Input.After making your entries, choose the Display button and choose Yes in the dialog box to save.Choose OK.Email Template: FCLM_BAM_OM_SIGN_UPDATESender Email: noreply@sap.com.For Action = 03 (Close Bank Account)Email Template: FCLM_BAM_OM_ACCOUNT_CLOSESender Email: noreply@sap.com.Choose Form template in the Determination Step field, and maintain the following entries in Table Contents:Maintain the following entries in Table Contents.For Action = 04 (Change Signatory)Form Template: FCLM_BAM_SIGNATURE_UPDATEForm Language: E (English)For Action = 03 (Close Bank Account)Form Template: FCLM_BAM_ACCOUNT_CLOSEForm Language: E (English)Output Relevance in the Determination Step field, and maintain the following entries in Table Contents:Relevance Indicator: X (true) |  |  |

#### Payment Approval Customizing

Purpose

The approval patterns and the payment approver group have to be defined and assigned to a company code if you are going to use the bank communication management for the payment approval management. Below steps describes the procedure to define the payment approver groups.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access Define Define Settings for Bank Account Master Data SSCUI | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementIn the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Define Settings for Bank Account Master Data row, choose Configure. |  |  |
| 3 | Define Payment Approver Groups | On the Dialog Structure panel, double-click the Define Payment Approver Groups node.Choose New Entries.Make the following entries:Appr. Grp: G001Account Description: Two Steps Approval - 1st StepAppr. Grp: G002Account Description: Two Steps Approval - 2nd StepAppr. Grp: ZG01Account Description: Non-sequential signatory group 1Appr. Grp: ZG02Account Description: Non-sequential signatory group 2Choose Save. |  |  |
| 4 | Define Approval Patterns | Double-click the Define Approval Patterns node.Choose New Entries.Make the following entries:Pattern: Z001Non Seq.: Leave blankAppr. Seq.: First stepAppr.Grp: G001Pattern: Z001Non Seq.: Leave blankAppr. Seq.: Second stepAppr.Grp: G002Pattern: Z002Non Seq.: <Select the check box>Appr. Seq.: Leave blankAppr.Grp: ZG01Pattern: Z002Non Seq.: <Select the check box>Appr. Seq.: <Leave blank>Appr.Grp: ZG02Choose Save. |  |  |
| 5 | Assign Approval Patterns | Double-click the Assign Approval Patterns node.Choose New Entries.Make the following entries:Company Code: for example, 3310Account Type: <Leave blank>.Pattern: Z001Priority: 1Company Code: for example, 3310Account Type: Leave blank.Pattern: Z002Priority: 2Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Settings for Bank Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Payment Approver Groups | On the Dialog Structure panel, double-click the Define Payment Approver Groups node.Choose New Entries.Make the following entries:Appr. Grp: G001Account Description: Two Steps Approval - 1st StepAppr. Grp: G002Account Description: Two Steps Approval - 2nd StepAppr. Grp: ZG01Account Description: Non-sequential signatory group 1Appr. Grp: ZG02Account Description: Non-sequential signatory group 2Choose Save. |  |  |
| 4 | Define Approval Patterns | Double-click the Define Approval Patterns node.Choose New Entries.Make the following entries:Pattern: Z001Non Seq.: Leave blankAppr. Seq.: First stepAppr.Grp: G001Pattern: Z001Non Seq.: Leave blankAppr. Seq.: Second stepAppr.Grp: G002Pattern: Z002Non Seq.: <Select the check box>Appr. Seq.: Leave blankAppr.Grp: ZG01Pattern: Z002Non Seq.: <Select the check box>Appr. Seq.: <Leave blank>Appr.Grp: ZG02Choose Save. |  |  |
| 5 | Assign Approval Patterns | Double-click the Assign Approval Patterns node.Choose New Entries.Make the following entries:Company Code: for example, 3310.Account Type: <Leave blank>.Pattern: Z001Priority: 1Company Code: for example, 3310.Account Type: Leave blank.Pattern: Z002Priority: 2Choose Save. |  |  |

#### Situation Handling Setting Up

Situation handling is a framework that automatically detects important issues and brings them to the attention of specific groups of users. This sections explaines how to set up situation handling for Bank Account Activation for Dual Control and for Closing Bank Account. For more information about situation handling, you can refer to test script 31N and [SAP help](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/516c8ecb7462453ca430a42481cc33ec.html?version=2021.002).

##### Situation Handling for Bank Account Activation in Dual Control

###### Create a Team for Situation Monitoring

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management ([1NJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1NJ) ) test script with the following information:

Team Name: Monitor Situation Team

Team Status: Ready to Use

Type: SFCLM0

Company Code: 3310

Account Type: <account type the team is responsible for>

|  |
| --- |
| Note If the last two fields are left blank, the team is responsible for all company codes and account types. |

Team Owners tab:

Business Partner: <user ID>, for example, Business Process Specialist

Team Members tab:

Business Partner: <user ID>, for example, Cash Manager

Functions: SFCLM_DC

|  |
| --- |
| Note To display the connection between the business partner, cash manager, and user ID, see the search help. Generic users are described in the Last Name field. |

###### Create Situation Types

Purpose

In this activity, you create a situation type to receive the notification. You can restrict the notification by bank account type and company code.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist (SAP_BR_BUSINESS_PROCESS_SPEC). |  |  |
| 2 | Access the SAP Fiori app | Open Manage Situation Types (F2947). |  |  |
| 3 | Copy Situation Types template | Search for the standard template FIN_BANKACCOUNTREVTOBEPROCESSED.Select the FIN_BANKACCOUNTREVTOBEPROCESSED checkbox and choose Copy. | The Situation Type screen displays. |  |
| 4 | Input Situation Type Parameters | Make the following entries:Admin Information tab:ID: Z_Situation_DualControlConditions tab:Not Processed For (Days): 01The value of Not Processed For (Days) indicates the number of days that situation handling message will be sent to. For example, Not Processed For (Days) is set to 01, and Cash Specialist created a bank account request, if the Cash Manager hasn't activated the bank account for 1 day, then situation handling message will be triggered 1 day later.Revision Status: 02Batch Job Scheduling tab:Time Zone: CET (for example)Start Batch Job At: 08:00 |  |  |
| 5 | Notification Recipients | Choose the Recipients tab. |  |  |
| 6 | Add Team Category | Choose Add Team Category. |  |  |
| 7 | Bank Account Management | Select the FCLM0 Bank Account Management checkbox and choose Select. |  |  |
| 8 | Responsibility Definition | In the Filter by Responsibility Definition field, select the search help button at the right of the entry field. | The Select: Responsibility Definitions dialog box displays. |  |
| 9 | Responsibility Definition | Select the BankAccountType and CompanyCode checkboxes and choose OK. |  |  |
| 10 | Add Rule | Make the following entries:Filter by Member Function: Function for Dual Control SituationIn the Responsibility Rules area, choose Add Rule. |  |  |
| 11 | Add Rules | Select FI_BAM_ACTIVATE Authorized user for activating revision and choose Select. |  |  |
| 12 | Situation Monitoring | Select the Monitor Instances checkbox. |  |  |
| 13 | Enable Situation Type | Choose Create.In the Enable Situation Type dialog box, choose Yes.Note Situation handling will be triggered, and it depends on the Batch Job Schedule time. If you want to trigger the situation handling immediately, you can choose the button Trigger Now on the up-right of the screen. | The situation type is created and saved. |  |

#### Powers of Attorney Customizing

Powers of attorney manages the banking transactions authorizations, you use this activity to Define the Authorization Group for Bank Account Transactions and Define Activities for Powers of Attorney.

##### Define Activities for Powers of Attorney

You can define your own additional activities for which authorization can be granted.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementChoose the arrow button at the right of the Bank Account Management row.In the right pane, for the Define Activities for Powers of Attorney row, choose Configure. | The Define Activities for Powers of Attorneyscreen displays. |  |
| 3 | Define Activities for Powers of Attorney | Choose New Entries.Make the following entries and choose Save.Activity: Z100Description: Execute Payments |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Activities for Powers of Attorney | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Activities for Powers of Attorney.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Activities for Powers of Attorney screen displays. |  |
| 3 | Define Activities for Powers of Attorney | Choose New Entries.Make the following entries and choose Save.Activity: Z100Description: Execute Payments |  |  |

##### Define Authorization Groups for Powers of Attorney

The authorization group for powers of attorney controls access to powers of attorney for banking transactions. Each powers of attorney must be assigned to an authorization group.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementChoose the arrow button at the right of the Bank Account Management row.In the right pane, for the Define Authorization Groups for Powers of Attorney row, choose Configure. |  |  |
| 3 | Define Authorization Group | Choose New Entries.Make the following entries and choose Save.Authoriz. : Z_TSDescription: Authorization Group for POA Testing |  |  |
| 4 | Define Company Code for Authorization Group | Select the checkbox of Z_TS.Choose the Company Code tab.Choose New Entries.Make the following entry and choose Save.Company Code: 3310 |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Authorization Groups for Powers of Attorney | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Authorization Groups for Powers of Attorney.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Authorization Group | Choose New Entries.Make the following entries and choose Save.Pass / Fail /Authoriz. : Z_TSDescription: Authorization Group for POA Testing |  |  |
| 4 | Define Company Code for Authorization Group | Select the checkbox of Z_TS.Choose the Company Code tab.Choose New Entries.Make the following entry and choose Save.Company Code: 3310 |  |  |

##### Define Channels for Powers of Attorney

This activity is to define the channels through which the power of attorney for banking transactions can be exercised. A channel is managed either by the bank or by you. You assign the channels to the implementation.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementChoose the arrow button at the right of the Bank Account Management row.In the right pane, for the Define Channels for Powers of Attorney row, choose Configure. |  |  |
| 3 | Define Channels | Choose New Entries.Make the following entries and choose Save.Channel ID : ZC01Description: Channel for POA Testing |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Authorization Groups for Powers of Attorney | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Authorization Groups for Powers of Attorney.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Channels | Choose New Entries.Make the following entries and choose Save.Channel ID : ZC01Description: Channel for POA Testing |  |  |

##### Profile Creation for Powers of Attorney

This activity is to define the profile through which the data collection can be exercised.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SSCUI | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Data ProtectionChoose the arrow button at the right of the Data Protection Settings row.In the right pane, for the Personalize Data Collection via Profiles row, choose Configure. |  |  |
| 3 | Create Profile | Enter the following entries and choose Create.Profile: Z_POA_ATTACH | Profile created successfully. |  |
| 4 | Edit Profile | Choose Edit.On detail tab, make the following entry:Description: Powers of Attorney data collection profileChoose the General Settings tab.Choose Yes to save the changes.Select the check box of Attachments.Choose Save.Choose the Download Settings tab.Select the check box of Attachments.Choose Save.Choose Activate. | The profile status changed to active. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SSCUI | In the Realize phase, navigate to the Configuration Activities tab and search for the following activity: Personalize Data Collection via Profiles.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create Profile | Enter the following entries and choose Create.Profile: Z_POA_ATTACH | Profile created successfully |  |
| 4 | Edit Profile | Choose Edit.On detail tab, make the following entry:Description: Powers of Attorney data collection profileChoose the General Settings tab.Choose Yes to save the changes.Select the check box of Attachments.Choose Save.Choose the Download Settings tab.Select the check box of Attachments.Choose Save.Choose Activate. | The profile status changed to active. |  |

##### Define Purpose for Powers of Attorney

This activity is to define purpose through which the data collection can be exercised.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SSCUI | Open Manage Your Solution (F1241)(F1241).Choose Configure Your Solution.Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Retention ManagementChoose the arrow button at the right of the Rule Generator row.In the right pane, for the Define Purpose row, choose Configure. |  |  |
| 3 | Define Purpose | Choose New Entries.Enter the following entries and choose Save.Purpose ID: Z_POA_PurposeDescription: Purpose for Powers of Attorney | Purpose created successfully. |  |
| 4 | Assign ILM Objects to Purpose | Choose the purpose created.Choose the tab Assign IML Object to Purpose.Choose New Entries.Make the following entry:ILM Object: FCLM_POAChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SSCUI | In the Realize phase, navigate to the Configuration Activities tab and search for the following activity: Define Purpose.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Purpose | Choose New Entries.Enter the following entries and choose Save.Purpose ID: Z_POA_PurposeDescription: Purpose for Powers of Attorney | Purpose created successfully. |  |
| 4 | Assign ILM Objects to Purpose | Choose the purpose created.Choose the tab Assign IML Object to Purpose.Choose New Entries.Make the following entry:ILM Object: FCLM_POAChoose Save. |  |  |

##### Assign Form Templates to Powers of Attorney Types

Prerequisites

A form template has been predefined by your Output Management team.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Search for Assign Form Template to POA Types via the search filter.Choose the configuration item Bank Account Management.Choose the Configure button in the Assign Form Templates to POA Types step. |  |  |
| 3 | Add Form Template | Choose New Entries.Make the following entries and choose Save:POA Type: SGBMForm: FCLM_BAM_POA |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Assign Form Templates | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Form Templates to POA Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Add Form Template | Choose New Entries.Make the following entries and choose Save:POA Type: SGBMForm: FCLM_BAM_POA |  |  |

#### Bank Account Contract Type

Bank Account Contract Types are subdivision dimensions for refined management of bank accounts. You use this activity to define what statuses are relevant in the bank account lifecycle, how should bank accounts be activated in each status and what tabs are visible in the bank account master data for a certain type of bank account. You can define different settings for different bank account contract types, account types and company codes.

##### Enable Bank Account Contract Type

Purpose

Bank Account Contract Types are available for full cash management with Bank Account Control Mode of Direct Change, Two Person Verification and Workflow. If you want to use this functionality to manage your bank account, you can follow below steps to enable it.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the General Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Basic Settings row, choose Configure. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Scope and Bank Acct Activation for your implementation based on the previously described procedures. |  |  |
| 4 | Enable the Bank Account Contract Types | Select the Enable Bank Account Contract Types checkbox.Choose Save.Note Bank Account Contract Types only support full cash management with Activate Directly, Two-Person Verification and Activate via Workflow, you can not select this checkbox under full cash management with dual control activation and basic cash management. | If the feature Manage Bank Accounts: Contract Type Validation (FTGL_BAM_BKACCT_CONTR_TYPE_VAL) has been activated in the configuration activity Activate Features. Users can only create bank accounts for the contract type Current Account when the contract type function is not enabled. Contract types such as In-House Bank Account, Payment Service Provider Account, and Technical Account can only be used after the contract type function is enabled in the configuration activity 101025: Define Basic Settings. For more information, refer to the [online help](https://help.sap.com/docs/) via SAP S/4HANA Cloud Public Edition > Preliminary What's New in SAP S/4HANA Cloud Public Edition 2602 > Finance > Treasury Management > Cash and Liquidity Management > Enhancement for Bank Account Contract Type Validation. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify your choices for Cash Management Scope and Bank Account Revision for your implementation based on the previously described procedures. |  |  |
| 4 | Enable the Bank Account Contract Types | Select the Enable Bank Account Contract Types checkbox.Choose Save.Note Bank Account Contract Types only support full cash management with Activate Directly and Activate via Workflow, you can not select this checkbox under full cash management with dual control activation and basic cash management. | If the feature Manage Bank Accounts: Contract Type Validation (FTGL_BAM_BKACCT_CONTR_TYPE_VAL) has been activated in the configuration activity Activate Features. Users can only create bank accounts for the contract type Current Account when the contract type function is not enabled. Contract types such as In-House Bank Account, Payment Service Provider Account, and Technical Account can only be used after the contract type function is enabled in the configuration activity 101025: Define Basic Settings. For more information, refer to the [online help](https://help.sap.com/docs/) via SAP S/4HANA Cloud Public Edition > Preliminary What's New in SAP S/4HANA Cloud Public Edition 2602 > Finance > Treasury Management > Cash and Liquidity Management > Enhancement for Bank Account Contract Type Validation. |  |

##### Define Account Type and Contract Type

Purpose

This activity describes the approach to define account type and contract type.

Prerequisite

You need to complete the step Enable to Bank Account Contract, otherwise the Contract Type field won’t display.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241).Choose Configure Your Solution.Search Bank Account Management or SSCUI ID 102336 on the search filter.Choose Configure on the Define Settings for Bank Account Master Data item. | The Define Settings for Bank Account Master Data screen displays. |  |
| 3 | Maintain Account Type Definition | Choose the Account Type Definition node.Choose New Entries.Make the following entries and choose Save:Type: 01Account Type Description: Current AccountContract Type: Current Account |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Settings for Payment Approval Processes | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Settings for Bank Account Master Datascreen displays. |  |
| 3 | Maintain Account Type Definition | Choose Account Type Definition.Choose New Entries.Make the following entries and choose Save:Type: 01Account Type Description: Current AccountContract Type: Current Account |  |  |

##### Define Repair Action for Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this steps you can define the bank accounts’ repair action modes. There are two modes available, Reture to Preceding Status and Restore Predecessor Versionare available for full cash management with Direct Revision Activate, Two-Person Verification Revision Activate and Workflow Revision Activate.

With Reture to Preceding Status mode, you can change a bank account to the preceding status in the bank account lifecycle using the Return to Preceding Status button. You select this option when you only allow the restore action in bank account status changes, and this is the default setting. To use this mode, make sure you have defined the Change Mode to Preceding Status setting in the Configure Statuses and Bank Account Change Modes tab of SSCUI Define Settings for Bank Account Contract Types.

With Restore Predecessor Version mode, you can restore a bank account to its predecessor version using the Restore button. This way you allow the restore action for both bank account status changes and data changes.

A bank account version is created in the following situations:

- A bank account is newly created with the inactive bank account status
- The status of the bank account is changed
- Sensitive data of the bank account is changed

To use this mode, make sure you define the following settings in SSCUI Define Settings for Bank Account Contract Types:

- On the Configure Statuses and Bank Account Change Modes tab, define the Change Mode to Preceding Status setting.
- On the Configure Actions and Bank Account Change Modes tab, define the Change Mode for Restore Action for action Change.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution(F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the General Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Basic Settings row, choose Configure. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify that Full Scope has been selected for Cash Scope, the Check Box of Enable Bank Account Contract Types has been selected. |  |  |
| 4 | Define Repair Action for Bank Account | Choose Back.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Define Settings for Bank Account Contract Types row, choose Configure.Choose Define Repair Actions for Bank Accounts tab.Choose One of the Repair Action.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify that Full Scope has been selected for Cash Scope, the Check Box of Enable Bank Account Contract Types has been selected. |  |  |
| 4 | Define Repair Action for Bank Account | On the Configuration Activities tab, search for the following activity: Define Settings for Bank Account Contract Types.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose Define Repair Actions for Bank Accounts tab.Choose One of the Repair Action.Choose Save. |  |  |

##### Configure Origination Process and Manual Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you enabled the Origination Process, the Inactive status in Bank Account Management will be extended to four new status (application approved, Pre-Opening Preparation, In Opening Process, Opened at Bank), to better serve account opening process.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the General Settings row, choose the arrow button at the right of the row.In the right pane, for the Define Basic Settings row, choose Configure. | The Define Basic Settings screen displays. |  |
| 3 | Define Basic Settings | Verify that Full Scope has been selected for Cash Scope, the Check Box of Enable Bank Account Contract Types has been selected. |  |  |
| 4 | Enable the Bank Account Origination Proceess | Choose Back.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Define Settings for Bank Account Contract Types row, choose Configure.Choose Configure Origination Process and Manual Creation tab.Choose New Entries.Make the following entries:Contract Type: Current Account.Company Code: 3310Enable Origination Process: <Select the check box>Disable Manual Creation: <Deselect>Note If you select this check box, you should follow the New Bank Account Application section to submit an application to request a new ban account.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Define Basic Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Basic Settingsscreen displays. |  |
| 3 | Define Basic Settings | Verify that Full Scope has been selected for Cash Scope, the Check Box of Enable Bank Account Contract Types has been selected. |  |  |
| 4 | Enable the Bank Account Origination Proceess | On the Configuration Activities tab, search for the following activity: Define Settings for Bank Account Contract Types.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose Enable Bank Account Origination Process tab.Choose New Entries.Make the following entries:Contract Type: Current Account.Company Code: 3310Enable Origination Process: <Select the check box>Disable Manual Creation: <Deselect>Note If you select this check box, you should follow the New Bank Account Application section to submit an application to request a new ban account.Choose Save. |  |  |

##### Configure Status and Bank Account Control Modes

Purpose

SAP has predefined bank account lifecycle statuses. Mandatory statuses are always enabled, regardless whether there is an entry for these statuses in this activity. For optional statuses they are enabled by default, unless you create an entry and deselect the Enable Status option.

- Active (mandatory)
- Inactive (mandatory)
- Closed (mandatory)
- Marked for Closing (optional)
- Closing Request Sent to Bank (optional)
- Closed at Bank (optional)

For each entry, you can specify the relevant bank account contract type, account type and company code. The following combinations are supported (priority from high to low):

a) Contract type + account type + company code

b) Contract type + account type

c) Contract type

Prerequisite

You have to complete [Enable Bank Account Contract Type](#unique_30) [page ] 46 and [Configure Origination Process and Manual Creation](#unique_33) [page ] 52 steps.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Define Settings for Bank Account Contract Types row, choose Configure. | The Change View "Define Settings for Bank Account Contract Types": Overview screen displays. |  |
| 3 | Configure Statuses and Bank Account Control Modes | Select the Configure Statuses and Bank Account Control Modes node.Choose New Entries.Make the following entries and choose SAVE.Account Type : For example, 03Company Code: <Leave Blank>Status: InactiveEnable Status: <Select>Control Mode to Next Status: Direct ChangeControl Mode to Preceding Status: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: ActiveEnable Status: <Select>Control Mode to Next Status: Activate via WorkflowControl Mode to Preceding Status: WorkflowAccount Type: For example, 03Company Code: <Leave Blank>Status: Marked for ClosingEnable Status: <Select>Activation Mode: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: Closing Request Sent to BankEnable Status: <Select>Control Mode to Next Status: Two-Person VerificationControl Mode to Preceding Status: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: Closed at BankEnable Status: <Select>Control Mode to Next Status: Direct ChangeControl Mode to Preceding Status: Two-Person VerificationNote Contract type syncs with step Define Account Type and Contract Type. You can't change the Account Type and Contract Type combination in this view. If you want to change it, please go to the step Define Account Type and Contract Type. |  |  |
| 4 | Simulate the Bank Account Lifecycle | Choose the Display button to change to Display Mode.Choose Simulate.Note Simulate button can only be find in Display Mode. | The statuses in lifecycle and Activation Modes for Status Changes displays. |  |
| 5 | Verify the Activation Mode | Refer to Using Direct Revision Activate, Using Two-Person Verification Revision Activate and Using Workflow Revision Activate to create a bank account -> Marked for Closing > Send Closing Request to Bank > Confirm Closing at Bank > Complete Closing.The changeover Mode set here takes a higher priority than the activation mode defined in Define Basic Settings step. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Contract Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Configure Statuses and Activation Modes | Select the Configure Status and Activation Modes node.Choose New Entries.Make the following entries and choose SAVE.Account Type : For example, 03Company Code: <Leave Blank>Status: InactiveEnable Status: <Select>Control Mode to Next Status: Direct ChangeControl Mode to Preceding Status: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: ActiveEnable Status: <Select>Control Mode to Next Status: Activate via WorkflowControl Mode to Preceding Status: WorkflowAccount Type: For example, 03Company Code: <Leave Blank>Status: Marked for ClosingEnable Status: <Select>Activation Mode: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: Closing Request Sent to BankEnable Status: <Select>Control Mode to Next Status: Two-Person VerificationControl Mode to Preceding Status: Direct ChangeAccount Type: For example, 03Company Code: <Leave Blank>Status: Closed at BankEnable Status: <Select>Control Mode to Next Status: Direct ChangeControl Mode to Preceding Status: Two-Person Verification |  |  |
| 4 | Simulate the Bank Account Lifecycle | Change to Display Mode.Choose Simulate.Note Simulate button can only be find in Display Mode. | The statuses in lifecycle and Activation Modes for Status Changes displays. |  |
| 5 | Verify the Activation Mode | Refer to Using Direct Revision Activate, Using Two-Person Verification Revision Activate and Using Workflow Revision Activate to create a bank account -> Marked for Closing > Send Closing Request to Bank > Confirm Closing at Bank > Complete Closing.The changeover Mode set here takes a higher priority than the activation mode defined in Define Basic Settings step. |  |  |

##### Configure Actions and Bank Account Control Modes

Purpose

This activity enables you to set Changeover Mode for changing and deleting bank account master data. The Changeover Mode set here takes a higher priority than the activation mode defined in the Define Basic Settings step.

Prerequisite

You have to complete the step [Enable Bank Account Contract Type](#unique_30) [page ] 46 before using this functionality.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Open Manage Your Solution (F1241).Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementChoose the arrow button at the right of the Bank Account Management row.In the right pane, for the Define Settings for Bank Account Contract Types row, choose Configure. | The Customizing: Execute Project screen displays. |  |
| 3 | Configure Actions and Bank Account Control Modes | Select the Configure Actions and Bank Account Control Modes tab.Choose New Entries.Make the following entries and choose SAVE.Contract Type: CurrentAccountAccount Type: For example, 03Company Code: LeaveBlankAction: ChangeControl Mode: WorkflowControl Mode for Restore: WorkflowContract Type: CurrentAccountAccount Type: For example, 03Company Code: LeaveBlankAction: DeleteControl Mode: Direct ChangeControl Mode for Restore: Direct Change |  |  |
| 4 | Verify the Activation Mode | Refer to Using Direct Revision Activate, Using Two-Person Verification Revision Activate and Using Workflow Revision Activate to change and delete a bank account to verify its activation mode. | The change of bank account should be Activate via Workflow, Delete Bank Account should be Activate Directly. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Contract Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Customizing: Execute Project screen displays. |  |
| 3 | Configure Actions and Bank Account Control Modes | Select the Configure Actions and Bank Account Control Modes tab.Choose New Entries.Make the following entries and choose SAVE.Contract Type: Current AccountAccount Type: For Example, 03Company Code: Leave BlankAction: ChangeControl Mode: WorkflowControl Mode for Restore: WorkflowContract Type: Current AccountAccount Type: For Example, 03Company Code: Leave BlankAction: DeleteControl Mode: Direct ChangeControl Mode for Restore: Direct Change |  |  |
| 4 | Verify the Activation Mode | Refer to Using Direct Revision Activate, Using Two-Person Verification and Using Workflow Revision to change and delete a bank account to verify its activation mode. | The change of bank account should be Activate via Workflow, Delete Bank Account should be Activate Directly. |  |

##### Hide Tabs in Bank Account Master Data

Purpose

You define the tabs that are visible in the bank account master data.

Prerequisite

You have to complete the step Enable Bank Account Contract Type before using this functionality.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Define Settings for Bank Account Contract Types row, choose Configure. | The Customizing: Execute Project screen displays. |  |
| 3 | Hide Tabs in Bank Account Master Data | Double-click the Hide Tabs in Bank Account Master Data node.Choose New Entries.Make the following entries and choose SAVE.Contract Type: For example, Current AccountAccount Type: For example, 03Cash Pool: <Select> |  |  |
| 4 | Verify the Technique Account | Create a bank with type technical, then create a bank account by assigning the technical bank key.According to above example, the Cash Pool tab will not be displayed for the technical bank account. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Define Settings for Bank Account Contract Types | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Settings for Bank Account Contract Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Customizing: Execute Project screen displays. |  |
| 3 | Hide Tabs in Bank Account Master Data | Select the Hide Tabs in Bank Account Master Data node.Choose New Entries.Make the following entries and choose SAVE.Contract Type: For example, Current AccountAccount Type: For Example, 03Cash Pool: <Select> |  |  |
| 4 | Verify the Technique Account | Create a bank with type technical, then create a bank account by assigning the technical bank key.According to above example, the Cash Pool tab will not be displayed for the technical bank account. |  |  |

#### Manage Field Status Groups to Origination Process

Purpose

With this Customizing SSCUI, you can assign the field status groups to the Origination Process to control the appearance and status of the fields on the user interface (UI) screens of the Manage Bank Accounts app during Origination Process status. For example, you may define a field to be mandatory, hidden, editable, or read-only. This setting is only available after the Origination Process is enabled.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution(F1241).Choose Configure Your Solution.Search and choose either Manage Field Status Groups or SSCUI ID 104059 in the search filter.Choose Configure for the Manage Field Status Groups Step Name. | The Manage Field Status Groups screen is displayed. |  |
| 3 | Maintain Field Status Groups | In the Dialog Structure panel, choose the Define Field Status Groups folder.Choose New Entries.Make the following entries:Field Group: Z_APPAPDescription: Application Approved.Select the check box of Z_APPAP. In the Dialog StructureDefine Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Note It is critical to press Enter after object input. You must press Enter before you can use the search help in the Field name panel, under. The search help function is linked to an object. Only after the object is confirmed may the search help value be populated in the Field name.Field Name: BENEFICIALField Status: HObject: BAMPress Enter.Field Name: IBANField Status: HField Group: Z_PREOPDescription: Pre-Opening Preparation.Select the check box of Z_PREOP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Field Name: BENEFICIALField Status: MObject: BAMPress Enter.Field Name: IBANField Status: HField Group: Z_INOPPDescription: In-Opening ProcessSelect the check box of Z_INOPP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Field Name: BENEFICIALField Status: MObject: BAMPress Enter.Field Name: IBANField Status: C.Field Group: Z_OPATBNKDescription: Opened at Bank.Select the check box of Z_PREOP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Field Name: BENEFICIALField Status: MObject: BAMPress Enter .Field Name: IBANField Status: MChoose Save. |  |  |
| 4 | Assign Field Status Groups to Origination Process | Choose Assign Field Status Grps to Origination Process.Choose New Entries.Make the following entries:Contract Type: Current AccountAccount Status: Application ApprovedField Group: Z_APPAPContract Type: Current AccountAccount Status: Pre-Opening PreparationField Group: Z_PREOPContract Type: Current AccountAccount Status: In Opening ProcessField Group: Z_INOPPContract Type: Current AccountAccount Status: Opened at BankField Group: Z_OPATBNKChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Settings for Manage Field Status Groups | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage Field Status Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Settings for Payment Approval Processes screen is displayed. |  |
| 3 | Maintain Field Status Groups | Choose Define Field Status Groups.Choose New Entries.Make the following entriesField Group: Z_APPAPDescription: Application Approved.Select the check box of Z_APPAP. In the Dialog StructureDefine Field Status Groups, double-click the Define UI Field Status panel, under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Note It is critical to press the Enter after input a object. Only if you have input Enter, you can use the search help for the field of Field Name. Because search help is linked to a object, only if object is confirmed the search help value can be pop up for Field Name.Field Name: BENEFICIALField Status: H.Object: BAM.Press Enter.Field Name: IBANField Status: H.Field Group: Z_PREOPDescription: Pre-Opening Preparation.Select the check box of Z_PREOP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAMPress Enter.Field Name: BENEFICIALField Status: MObject: BAMPress Enter.Field Name: IBANField Status: HField Group: Z_INOPPDescription: In-Opening ProcessSelect the check box of Z_INOPP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Field Name: BENEFICIALField Status: MObject: BAMPress Enter.Field Name: IBANField Status: C.Field Group: Z_OPATBNKDescription: Opened at Bank.Select the check box of Z_PREOP. In the Dialog Structure Define Field Status Groups, double-click the Define UI Field Status panel under subfolder.Choose New Entries.Make the following entries:Object: BAM.Press Enter.Field Name: BENEFICIALField Status: MObject: BAM.Press Enter.Field Name: IBANField Status: MChoose Save. |  |  |
| 4 | Assign Field Status Groups to Origination Process | Choose Assign Field Status Grps to Origination Process.Choose New Entries.Make the following entries:Contract Type: Current AccountAccount Status: Application ApprovedField Group: Z_APPAPContract Type: Current AccountAccount Status: Pre-Opening PreparationField Group: Z_PREOPContract Type: Current AccountAccount Status: In Opening ProcessField Group: Z_INOPPContract Type: Current AccountAccount Status: Opened at BankField Group: Z_OPATBNKChoose Save. |  |  |

#### Disable Email Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP has predefined email notifications for different scenarios in the bank account management processes. You can disable these email notifications in this activity.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Disable Email Notification row, choose Configure. |  |  |
| 3 | Disable Email Notification | Choose NewEntries.Make the following entries and choose Save.Email Template ID: for example, FCLM_BAM_REV_VERIFIED_EMAILNote Do not select the Enable button if you want to disable the email notification. If you removed the entry or selected the Enable button, the email notification can be activated. | The Email Notification is disabled for bank account activation via Two-Person mode. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Disable Email Notification | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Disable Email Notification.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Disable Email Notification | Choose NewEntries.Make the following entries and choose Save.Email Template ID: for example, FCLM_BAM_REV_VERIFIED_EMAILNote Do not select the Enable button if you want to disable the email notification. If you removed the entry or selected the Enable button, the email notification can be activated. | The Email Notification is disabled for bank account activation via Two-Person mode. |  |

#### Manage My Substitutes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use app My Inbox - For Bank Accounts (F2797) to create substitution rules to manage your tasks in your absence. The substitution rules can be created for planned and unplanned absences.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox - For Bank Accounts (F2797). | The worklist displays. |  |
| 3 | Use Substitutes | Choose Manage My Substitutes in your user settings in the upper screen corner. |  |  |
| 4 | Add New Substitutes | Choose Add New Substitute.Search CashManagerCN as an example.Choose CashManagerCn.Choose All Task Groups.Choose Save. | Substitution rule is created. |  |

#### Set Up Instant Balances (Optional)

Purpose

To monitor instant balances for bank accounts, you need to enable instant balances for the relevant house bank in the Manage Banks - Cash Management (F1574A) app. After enabling the feature for the house bank, you can then use the Define Bank Accounts Settings - Instant Balances (F7805) app to switch instant balances on for the relevant bank accounts.

You can select one or multiple accounts and update the instant balance data by choosing Update Balances. When you choose Update Balances, an update request is sent to the corresponding bank and the Current Update Status field is set to In Process. When the update is completed, the status is changed to Completed, and the instant balance is displayed in the Last Available Balance field.

The following house banks support instant balances:

- Deutsche Bank
- JP Morgan & Co

##### Enable Instant Balances

Purpose

You enable instant balances for the relevant house bank in the Manage Banks - Cash Management (F1574A) app.

Procedure

Refer to the Manage Banks Cash Management Data procedure, find the House Bank and select the Instant Balances Enabled indicator.

##### Define Bank Accounts Settings – Instant Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can switch instant balances on for the relevant bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Bank Accounts Settings - Instant Balances (F7805). | The Define Bank Account Settings - Instant Balances view displays. |  |
| 3 | Enter Selection Criteria | In the filter area, enter the following data and choose Go:House Bank Enablement: <Enabled> | The bank account list displays. |  |
| 4 | Switch On Instant Balances | Choose a bank account, and choose Switch On. On the screen appears, choose Switch On to confirm it. | The account switch status is updated. |  |

#### Set Rating Procedures and Ratings (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity descrbes how to create rating procedures for bank account management and assign ratings to them.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241).Open Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementFor the Bank Account Management row, choose the arrow button at the right of the row.In the right pane, for the Set Rating Procedures and Ratings row, choose Configure. |  |  |
| 3 | Create Rating Procedure | Choose New Entries.Make the following entries and choose Save.Rating Procedure: for example, BRMBP Role: TR0703 |  |  |
| 4 | Create Ratings | Choose the Rating Procedure created in previous step.Choose Ratings.Make the following entries and choose Save.Rating: AAA+Rank: 1Description: AAA+Rating: AAARank: 2Description: AAARating: AAA-Rank: 3Description: AAA- |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays |  |
| 2 | Open Set Rating Procedures and Ratings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Rating Procedures and Ratings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create Rating Procedure | Choose New Entries.Make the following entries and choose Save.Rating Procedure: for example, BRMBP Role: TR0703 |  |  |
| 4 | Create Ratings | Choose the Rating Procedure created in previous step.Choose Ratings.Make the following entries and choose Save.Rating: AAA+Rank: 1Description: AAA+Rating: AAARank: 2Description: AAARating: AAA-Rank: 3Description: AAA- |  |  |

## Overview Table

The Advanced Bank Account Management (J77) scope item consists of several process steps described in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

New Bank Account Application

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Submit Bank Account Applications](#unique_45) [page ] 87 | Cash Management Specialist | Submit Bank Account Applications (F5861) | The bank account application is created. |
| [Approve Bank Account Applications](#unique_46) [page ] 88 | Cash Manager | Approve Bank Account Applications (F5859) | The bank account application is approved or rejected. |
| [Create Bank Account for New Bank Account Application](#unique_47) [page ] 89 | Cash Management Specialist | Bank Account Applications (F5860) | The bank account according to the new bank account application is created. |
| [Withdraw Bank Account Application](#unique_48) [page ] 90 | Cash Management Specialist | Submit Bank Account Applications (F5861) | The bank account application is withdrawn. |
| [Confirm Bank Account Application Withdrawal](#unique_49) [page ] 91 | Cash Manager | Approve Bank Account Applications (F5859) | The withdrawal of bank account application is confirmed. |

Bank Account Master Data Processing With Full Cash Management

Using Direct Revision Activation

Table 2: Create Bank Account

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Open Bank Account](#unique_50) [page ] 92 | Cash Management Specialist |  | The bank accountant goes to the bank and opens a new bank account in this bank. This step does not occur in the system. |
| [Create Bank Master Data](#unique_51) [page ] 92 | Cash Management Specialist | Manage Banks | A bank key that does not exist in production system is created. If the bank key already exists, skip this step. |
| [Edit Bank Master Data](#unique_52) [page ] 94 | Cash Management Specialist | Manage Banks | Bank information is edited. |
| [Create Bank G/L Account](#unique_53) [page ] 95 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user may create the G/L accounts of newly created bank account. |
| [Manage Banks Cash Management Data](#unique_54) [page ] 95 | Cash Management Specialist | Manage Banks | The bank accountant creates the house bank. If a new bank account is opened in an existing house bank in your system, skip this step. |
| [Create Bank Account](#unique_55) [page ] 97 | Cash Management Specialist | Manage Bank Accounts (F1366A) | A new bank account that does not exist in production system is created. |
| [Export Bank Account](#unique_56) [page ] 102 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are exported. |
| [Import Bank Accounts](#unique_57) [page ] 104 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are imported into development system and consolidation system. |

Table 3: Change Bank Account

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Change](#unique_58) [page ] 105 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system. |
| [Change Bank Account](#unique_59) [page ] 105 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank accountant changes the attributes of this bank account in system. |
| [Update Bank G/L Account](#unique_60) [page ] 106 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user updates the G/L account of bank only when it is necessary. However, modification of bank account does not result in G/L account modification every time. |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Repair Bank Accounts](#unique_61) [page ] 110 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The redundant bank account is closed in system. |

Table 4: Close Bank Account and Cancel Closing

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Close Account](#unique_62) [page ] 111 | Cash Management Specialist |  | The bank account is closed. |
| [Close Bank Account and Cancel Closing](#unique_63) [page ] 111 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The redundant bank account is closed in system. |

Table 5: Maintain Payment Approver for Multiple Bank Accounts (Direct Revision Activation)

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Add Payment Approver for Multiple Bank Accounts](#unique_64) [page ] 116 | Cash Management Specialist | Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)) | Payment Approver added. |
| [Change Payment Approver for Multiple Bank Accounts](#unique_65) [page ] 118 | Cash Management Specialist | Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) | Payment Approver maintained. |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Attachments for Bank Account](#unique_66) [page ] 119 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Attachments for the bank account are uploaded. |

Using Dual Control Revision Activation

Table 6: Create Bank Account

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Open Bank Account](#unique_67) [page ] 121 | Cash Management Specialist |  | The bank accountant goes to the bank and opens a new bank account in this bank. This step does not occur in the system. |
| [Create Bank Master Data](#unique_68) [page ] 121 | Cash Management Specialist | Manage Banks | A bank key that does not exist in production system is created. If the bank key already exists, skip this step. |
| [Edit Bank Master Data](#unique_69) [page ] 123 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user may create the G/L accounts of newly created bank account. |
| [Create Bank G/L Account](#unique_70) [page ] 124 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | The G/L accounts for a new bank account are created. |
| [Manage Banks Cash Management Data](#unique_71) [page ] 124 | Cash Management Specialist | Manage Banks | The bank accountant creates the house bank. If a new bank account is opened in an existing house bank in your system, skip this step. |
| [Create Bank Account](#unique_72) [page ] 125 | Cash Management Specialist | Manage Bank Accounts (F1366A) | A new bank account that does not exist in production system is created. |
| [Export Bank Account](#unique_73) [page ] 131 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are exported from production system. |
| [Import Bank Accounts](#unique_74) [page ] 133 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank accounts are imported into development system and consolidation system. |

Table 7: Change Bank Account

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Change](#unique_75) [page ] 134 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system. |
| [Change Bank Account](#unique_76) [page ] 134 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank accountant changes the attributes of this bank account in system. |
| [Update Bank G/L Account](#unique_77) [page ] 135 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | FIN master data key user updates the G/L account of bank only when it is necessary. However, modification of bank account does not result in G/L account modification every time. |

Table 8: Close Bank Account and Cancel Closing

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Close Account](#unique_78) [page ] 139 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to close this bank account. This step does not occur in the system. |
| [Close Bank Account and Cancel Closing](#unique_79) [page ] 139 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The redundant bank account is closed in system. |

Table 9: Maintain Payment Approver for Multiple Bank Accounts (Dual Control Revision Activation)

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Add Payment Approver for Multiple Bank Accounts](#unique_80) [page ] 145 | Cash Management Specialist | Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)) | Payment Approver added. |
| [Change Payment Approver for Multiple Bank Accounts](#unique_81) [page ] 147 | Cash Management Specialist | Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) |  |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Attachments for Bank Account](#unique_82) [page ] 148 | Cash Management Specialist | Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) | Payment Approver maintained. |
| [Activate the Bank Account via Dual Control](#unique_83) [page ] 149 | Cash Manager | Manage Bank Accounts (F1366A) | Activation approved. |

Using Two-Person Verification Revision Activation

Table 10: Create Bank Account

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Open Bank Account](#unique_84) [page ] 151 | Cash Management Specialist | This step does not occur in the system |  |
| [Create Bank Master Data](#unique_85) [page ] 151 | Cash Management Specialist | Manage Banks | The Manage Banks - Basic screen displays Banks are displayed in a list. |
| [Edit Bank Master Data](#unique_86) [page ] 153 | Cash Management Specialist | Manage Banks | Bank information is edited. |
| [Create Bank G/L Account](#unique_87) [page ] 154 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | The Search: G/L Accounts screen displays. |
| [Manage Banks Cash Management Data](#unique_88) [page ] 154 | Cash Management Specialist | Manage Banks | A house bank is created. |
| [Create Bank Account](#unique_89) [page ] 155 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Bank Hierarchy: Active Accounts (X Account) screen displays. |
| [Export Bank Account](#unique_90) [page ] 161 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Import and Export Bank Accounts screen displays. |
| [Import Bank Accounts](#unique_91) [page ] 163 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The exported bank accounts are imported into the development system and consolidation test system. |
| [Option 1: Approve Bank Account Request by Using Manage Bank Account](#unique_92) [page ] 164 | Cash Manager | Manage Bank Accounts (F1366A) | The new bank account can be approved. |
| [Option 2: Approve Bank Account Request by Using Approve Bank Account Changes](#unique_93) [page ] 165 | Cash Manager | Approve Bank Account Changes - Two-Person Verification (F6264) | The new bank account can be approved. |

Table 11: Change Bank Account

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Change](#unique_94) [page ] 166 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system. |
| [Change Bank Account](#unique_95) [page ] 166 | Cash Management Specialist | Manage Bank Accounts (F1366A) | A bank account is changed. |
| [Withdraw Bank Account Request (Optional)](#unique_96) [page ] 167 | Cash Management Specialist | Manage Bank Accounts (F1366A) | Bank account changes are withdrawed. |
| [Update Bank G/L Account](#unique_97) [page ] 168 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | The G/L account is updated. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Repair Bank Accounts](#unique_61) [page ] 110 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank accounts are changed back to preceding status. |

Table 12: Close Bank Account and Cancel Closing

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Notify Bank to Close Account](#unique_98) [page ] 173 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to close this bank account. This step does not occur in the system. |
| [Close Bank Account and Cancel Closing](#unique_99) [page ] 173 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Bank Hierarchy: Active Accounts (X Account) screen displays. |

Table 13: Maintain Payment Approver for Multiple Bank Accounts (Two-Person Verification Revision Activation)

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Add Payment Approver for Multiple Bank Accounts](#unique_100) [page ] 179 | Cash Management Specialist | Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)) | Payment Approver added. |
| [Change Payment Approver for Multiple Bank Accounts](#unique_101) [page ] 181 | Cash Management Specialist | Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)) | Payment Approver maintained. |
| [Verify the Bank Account after Payment Approver Maintenance](#unique_102) [page ] 182 | Cash Manager | Manage Bank Accounts (F1366A) | Activation approved. |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Attachments for Bank Account](#unique_103) [page ] 183 | Cash Manager | Manage Bank Accounts (F1366A) | Payment Approver maintained. |

Table 14: Approve Bank Account Request via Two-Person Verification

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check Bank Account Change Request](#unique_104) [page ] 184 | Cash Manager | Bank Account Change Requests - Two-Person Verification (F6265) | Payment Approver added. |
| [Option 1: Approve Bank Account Request by Using Manage Bank Account](#unique_105) [page ] 185 | Cash Manager | Manage Bank Accounts (F1366A) | Payment Approver maintained. |
| [Option 2: Approve Bank Account Request by Using Approve Bank Account Changes App](#unique_106) [page ] 186 | Cash Manager | Approve Bank Account Changes - Two-Person Verification (F6264) | A second operator can approve the changes. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Bank Account Change Request Overview – Two-Person Verification](#unique_107) [page ] 186 | Cash Management Specialist | Bank Account Change Requests - Two-Person Verification (F6265) | An overview of all the bank account change requests display. |

Using Workflow Revision Activation

Table 15: Create Bank Account

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Open Bank Account](#unique_108) [page ] 188 | Cash Management Specialist | This step does not occur in the system. | A new bank account in this bank is opened. |
| [Create Bank Master Data](#unique_109) [page ] 188 | Cash Management Specialist | Manage Banks | The Manage Banks - Basic screen displays Banks are displayed in a list. |
| [Edit Bank Master Data](#unique_69) [page ] 123 | Cash Management Specialist | Manage Banks | Bank information is edited. |
| [Create Bank G/L Accounts](#unique_110) [page ] 191 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | The Search: G/L Accounts screen displays. |
| [Manage Banks Cash Management Data](#unique_111) [page ] 191 | Cash Management Specialist | Manage Banks | The house bank is created. |
| [Create Bank Account Request](#unique_112) [page ] 193 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Bank Hierarchy: Active Accounts (X Account) screen displays. |
| [Export Bank Accounts](#unique_113) [page ] 199 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Import and Export Bank Accounts screen displays. |
| [Import Bank Accounts](#unique_114) [page ] 200 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The bank accounts are imported into the target system. |
| [Change Bank Account During Workflow (Optional)](#unique_115) [page ] 202 | Cash Manager | My Inbox - For Bank Accounts (F2797) | The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. |

Table 16: Change Bank Account

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Receive Change Request from Requester](#unique_116) [page ] 203 | Cash Management Specialist |  | The bank accountant receives a change request from other colleagues. |
| [Create Bank Account Change Request](#unique_117) [page ] 203 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Bank Hierarchy Active Accounts screen displays. |
| [Change Bank Account During Workflow (Optional)](#unique_115) [page ] 202 | Cash Manager | My Inbox - For Bank Accounts (F2797) | The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. |
| [Notify Bank to Change](#unique_118) [page ] 206 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system. |
| [Update Bank G/L Account](#unique_119) [page ] 207 | General Ledger Accountant | Manage G/L Account Master Data (F0731A) | The G/L account of bank is updated. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Repair Bank Accounts](#unique_61) [page ] 110 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The requester receives a request to close an existing bank account from other colleagues. |

Table 17: Close Bank Account and Cancel Closing

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Receive Bank Account Closing Request from Requester](#unique_120) [page ] 211 | Cash Management Specialist |  | The requester receives a request to close an existing bank account from other colleagues. |
| [Notify Bank to Close Account](#unique_121) [page ] 211 | Cash Management Specialist |  | The bank accountant goes to the bank and asks the bank employee to close this bank account. This step does not occur in the system. |
| [Close Bank Account and Cancel Closing](#unique_122) [page ] 212 | Cash Management Specialist | Manage Bank Accounts (F1366A) | The Bank Hierarchy: Active Accounts (X Account) screen displays. |
| [Change Bank Account During Workflow (Optional)](#unique_115) [page ] 202 | Cash Manager | My Inbox - For Bank Accounts (F2797) | The new bank account request is sent to the bank account worklist (inbox) for the Cash Manager. |

Table 18: Maintain Payment Approver in Multiple Bank Accounts (Workflow Revision Activation)

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Add Payment Approver for Multiple Accounts](#unique_123) [page ] 219 | Cash Management Specialist | Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)) | Payment Approver added. |
| [Change Payment Approver in Multiple Bank Accounts](#unique_124) [page ] 221 | Cash Management Specialist | Manage Bank Accounts (WDA_FCLM_BAM_HIERARCHY) | Payment Approver maintained. |

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Upload Attachments for Bank Account](#unique_125) [page ] 222 | Cash Manager | Manage Bank Accounts (F1366A) | Payment Approver maintained. |
| [Cancel Bank Accounts Requests](#unique_126) [page ] 223 | Cash Management Specialist | My Sent Requests - For Bank Accounts (F1371A) | Change request canceled. |
| [Approve Bank Account Request via Workflow](#unique_127) [page ] 224 | Cash Manager | My Inbox - For Bank Accounts (F2797) | The change request is approved or rejected. |

Powers of Attorney

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Manage Payment Approval Rules](#unique_128) [page ] 231 | Cash Management Specialist | Manage Payment Approval Rules (F6959) |  |
| [Create Powers of Attorney](#unique_129) [page ] 233 | Cash Management Specialist | Manage Powers of Attorney for Banking Transactions (F5742) | A Power of Attorney is created. |
| [Approve Powers of Attorney](#unique_130) [page ] 236 |  |  |  |
| [Approve Powers of Attorney via Dual Control](#unique_131) [page ] 236 | Cash Manager | Manage Powers of Attorney for Banking Transactions (F5742) | Powers of attorney can be approved. |
| [Approve Powers of Attorney via Workflow](#unique_132) [page ] 237 | Cash Manager | My Inbox - All Items (F0862) | Powers of attorney can be approved. |
| [Approve Powers of Attorney with Basic Bank Account Management User (Optional)](#unique_133) [page ] 238 | Administrator | Manage Workforce (F6097A) | Powers of attorney can be approved. |
| [Create PDF for Powers of Attorney](#unique_134) [page ] 240 | Cash Management Specialist | Manage Powers of Attorney for Banking Transactions (F5742) | You can create PDF as attachment for the powers of attorney. |
| [Revoke Powers of Attorney](#unique_135) [page ] 240 | Cash Management Specialist | Manage Powers of Attorney for Banking Transactions (F5742) | Powers of attorney is revoked. |
| [Implement Powers of Attorney](#unique_136) [page ] 241 | Cash Management Specialist | Implement Powers of Attorney for Banking Transactions (F6374) | Powers of attorney is submitted for approval. |

Manage Bank Accounting Hierarchies

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Bank Account Group](#unique_137) [page ] 250 | Cash Management Specialist | Manage Bank Account Hierarchies (F4973) | You created a bank account group. |
| [Edit Bank Account Group](#unique_138) [page ] 251 | Cash Management Specialist | Manage Bank Account Hierarchies (F4973) | You edited the bank account group. |
| [Delete Bank Account Group](#unique_139) [page ] 252 | Cash Management Specialist | Manage Bank Account Hierarchies (F4973) | You deleted the bank account group. |

Bank Account Report and Fact Sheet

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Foreign Bank Account Report](#unique_140) [page ] 263 | Cash Manager | Foreign Bank Account Report (F1575) | This report displays the bank accounts that are opened in foreign countries. |
| [Bank (Fact Sheet)](#unique_141) [page ] 265 | Cash Manager | Magnifier Icon | The search box displays. |
| [House Bank (Fact Sheet)](#unique_142) [page ] 266 | Cash Manager | Magnifier Icon | The search box displays. |
| [House Bank Account (Fact Sheet)](#unique_143) [page ] 267 | Cash Manager | Magnifier Icon | The search screen displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### New Bank Account Application

Bank Account Application is used for some departments of a organization who don’t have the authorization to create bank account by using app Manage Bank Accounts. If you want to apply a new bank account, you can assign the business catalog SAP_FIN_BC_CM_BAA_SUBMIT_PC to your user. The users who have been assigned the business catalog SAP_FIN_BC_CM_BAA_APPROVE_PC will have the authorization to approve the new bank account application request. For testing purpose, we use cash specialist to create bank account application request and use cash manager to approve it.

#### Submit Bank Account Applications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a bank account application. You can input Application Reason and some general information about the account to be created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Submit Bank Account Applications (F5861). |  |  |
| 3 | Create Applications | Choose Create. |  |  |
| 4 | Enter Application Data | Make the following entries and choose Create:Application Title: Request to Create a new Bank Account 22333Company Code (Requested): 3310Currency (Requested): AEDBank Country/Region (Requested): AEApplication Reason: Department Reorganization.Choose Submit for Approval.Note If the error message pops up that no approver can be found, please refer to [Online Help Submit Bank Account Application](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/082aa2dd415c4b679bff05fade2775d9.html) part. | The maintenance UI displays your new nodes. |  |

#### Approve Bank Account Applications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can approve or reject the bank account application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Approve Bank Account Applications (F5859). |  |  |
| 3 | Approve Applications | Select the application.Choose Approve.In the pop up window, enter: ApprovedChoose Approve. | Bank Account Application has been approved. |  |

#### Create Bank Account for New Bank Account Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a bank account according to the new bank account application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Bank Account Applications (F5860). |  |  |
| 3 | Locate the Bank Account | Choose Go.Select the application.Choose the hyperlink of the Technical ID. |  |  |
| 4 | Create Bank Account | In this step, you can refer to [Bank Account Master Data Processing with Advanced Bank Account Management](#unique_146) [page ] 91 to create the bank account. | The maintenance UI displays your new nodes. |  |

#### Withdraw Bank Account Application

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you initiate the withdraw process of the bank account application. If the bank account hasn't been approved, the bank account application can be withdrawn after you finished this step. If the bank account application already been approved, you have to perform the [Confirm Bank Account Application Withdrawal](#unique_49) [page ] 91 step to finish the withdraw process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Submit Bank Account Applications (F5861). |  |  |
| 3 | Locate the Bank Account | Choose Go.Select the application.Choose Withdraw. |  |  |

#### Confirm Bank Account Application Withdrawal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You need to perform this step to withdraw a bank account application that is with active status. If the bank account application hasn't been approved yet, please perform the [Withdraw Bank Account Application](#unique_48) [page ] 90 step and skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cash Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Approve Bank Account Applications (F5859). |  |  |
| 3 | Locate the Bank Account | Select the application.Choose Confirm Withdrawal. |  |  |

### Bank Account Master Data Processing with Advanced Bank Account Management

SAP has predelivered bank and bank account master data as demo data in START system. If you are using Solution Builder for activation, plesse don't copy these SAP predelivered master data from START system to Q or P system. Because ID Clash will not triggered, you may not be able to delete these entries in Q or P. But If you use SAP Central Business Configuration as your configuration environment, whether it is for 2 System Landscape or 3 System Landscape, you won't get such issue.

#### Using Direct Revision Activation

##### Create Bank Account

###### Open Bank Account

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and opens a new bank account at that bank. This step does not occur in the system.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Banks - Master Data (F6437). |  |  |
| 3 | Choose Create Bank | Choose Go for the banks to display in a list and choose Create Bank. | The Create Bank view displays. |  |
| 4 | Enter Criteria | Make the following entries:Bank Country/Region: AEBank Key: 88800011Choose Create Bank. |  |  |
| 5 | Enter General Data | Make the following entries:Bank Name: AE Standard Bank for Advanced Bank Account Management Direct ModeChoose Create. | The standard bank is created. |  |
| 6 | Create Internal Banks | Go to the initial page of app Manage Banks - Master Data (F6437).Choose the triangle button beside the Create.Choose Create Internal Bank. |  |  |
| 7 | Enter Control Data | Make the following entries:Bank Country/Region: AEBank Key: 88888889Internal Bank Category: Payment Service ProviderChoose Create Internal Bank.Note If the bank key created is used for an internal virtual bank, for example, PayPal,which is used as House Bank, please select Internal - Payment Service Provider.which is used to enable the maintenance of the business partner bank details with alias, please select the Payment system. For more details, please refer to SSCUIs 105361 - Define Alias Types and 105362 - Define Payment Systems. |  |  |
| 8 | Enter General Data | Make the following entries:Bank Name: AE Internal Bank for Advanced Bank Account Management Direct ModeChoose Create. | The Internal bank is created. |  |

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
| 3 | Filter the Bank | Make the following entry in the filter and choose Go.Bank Key: 88800011 |  |  |
| 4 | Choose the Bank | Choose the Bank in the list. |  |  |
| 5 | Edit Bank | Choose Edit.Make the following entries:SWIFT/BIC: DEUTDEFFXX1City: for example, 60040 Frankfurt, Main |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

###### Create Bank G/L Account

Purpose

In this activity, the G/L accountant creates the G/L accounts for a new bank account. You can refer to test script Accounting and Financial Close ([J58](https://me.sap.com/processnavigator/SolP/J58)) for G/L accounts creation. It is described in Manage G/L Account Master Data step

|  |
| --- |
| Note In cash management in this package, you can use the same G/L accounts (bank main account and bank subaccount) for different bank accounts if they use the same currency key. The balance of each bank account can be displayed in the Cash Management SAP Fiori app, instead of checking balances of the relevant G/L account. Using this approach keeps the chart of accounts smaller. |

|  |
| --- |
| Note The Manage G/L Account Master Data (F0731A) app can be executed by either the Configuration Expert - Business Process Configuration role or the General Ledger Accountant role. You can only make changes in the Q system. In the P system, you can only display content. The two procedures are shown in test script Accounting and Financial Close (J58) . |

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
| 4 | Enter Risk Business Partner | Choose Edit.Make the following entry:Risk Business Partner: for example, 55555Note If you can't find Business Partner, please refer to test script [BFA](https://me.sap.com/processnavigator/SolP/BFA) preliminary step Create Bank Business Partner to create it. | The Manage Banks view displays. |  |
| 5 | Enter House Bank Data | Go to House Banks tab and choose Create.Make the following entries:Company Code: 3310House Bank: AEBK3Choose Continue.Choose Apply. |  |  |
| 6 | Enter Netting Business Partner | Go to Netting Business Partner tab.Make the following entries:Valid From: <Current Date>.Valid To: <Futrue Date>.Business Partner: <Choose one by using search help>. |  |  |
| 7 | Save Bank | Choose Save. | New house bank is saved successfully. |  |

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
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Create Bank Account | Choose Create.Make the following entries and choose Create.Company Code: 3310Account Type: 01 | The Bank Account screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Account Number: 0000000033108888Account Description: AEBank Account for Advanced Bank Account Management Direct ModeBank Country/Region: AEBank Key: 88800011Currency: AED |  |  |
| 5 | Enter General Data | Change the following entries:Opening Date: for example, <current date>Account Holder: Company Code3310 (company code name is usually defaulted by system)Bank Control Key: for example, PNote Bank Control Key is only used in some countries like France, Spain, Italy. If you don't use Bank Control Key, you should leave this field blank.IBAN: <Generate IBAN>Note Only perform this step if the country is using IBAN; if you do not use IBAN in your process, just skip this step. |  |  |
| 6 | Bank Relationship Data | Pmnt Tran Type Group: CAMT053Note The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank StatementsNote If you are going to upload camt.054 format bank statement for supplier financing, which is described in test script 1EG, the field Pmnt Tran Type Group has to be maintained as camt053, otherwise camt054 bank statement can't be uploaded. |  |  |
| 7 | Maintain Internal Bank Account Contact | In the Bank Relationship pane, in the Contact Persons area, make the following entries:Internal Bank Account Contact: ID assigned to the Cash Management Specialist roleInternal Bank Account Supervisor: ID assigned to the Cash Manager role |  |  |
| 8 | Choose Bank Relationship Tab | In the Bank Relationship pane, in the Bank Statement Data area, make the following entries:Processing Status: <selected>Interval: for example, 01Interval Unit: for example, MonthsFactory Calendar ID: for example, 01Note The Processing Status field indicates whether to monitor this bank account at the end of the day in the Bank Statement Monitor. You can specify the import frequency with the Interval and Interval Unit fields. The Factory Calendar ID field distinguishes between working days and non-working days. |  |  |
| 9 | Choose House Bank Account Connectivity | Choose House Bank Account Connectivity. |  | House Bank Account Connectivity allows you to associate a bank account with its house bank account in the central system where SAP S/4HANA Cloud Public Edition Finance for Cash Management is installed. It also enables connections to accounts in remote SAP or third-party systems. For additional information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US). |
| 10 | Enter House Bank Account Connectivity | Choose Create. Make the following entries:ID Category: for example, Central System: House Bank AccountNote If the house bank account only exist in the local system you can specify the ID Category as Central System: House Bank Account; If the house bank account exist in remote system, and need to be migrated to local system, you can specify the ID Category to Remote System: House Bank Account.Remote System: <Leave blank>Note If you have enabled the Convert Remote House Bank Accounts functionality in the configuration activity Define System Groups (107199), please ensure that all necessary attributes for the remote house bank accounts to be replicated are properly maintained prior to their conversion to the ID category Central System: House Bank Account. These accounts are then replicated back to the originating target system. Incorrect or missing attributes may result in validation errors in the target systems. For further information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US) and [Outbound Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/9b57a8997a02462989f2d0b168dac811.html?version=LATEST&locale=en-US).Company Code: 3310House Bank: AEBK3House Bank Acct ID: AEAC3Use Bank Reconciliation Account: <Leave the check box blank>G/L Account: 11001000Note If you select the check box of Use Bank Reconciliation Account, you need to input a reconciliation G/L account through the search help. The purpose of this function is to reduce the G/L account usage.Use in Cash Pooling: SelectNote The Use in Cash Pooling field determines if the house bank account is used for cash pooling. If the checkbox is selected, this house bank account can be used for cash pooling. If there are multiple house bank accounts for one bank account, only one house bank account can be used for cash pooling. |  |  |
| 11 | Save and Activate Bank Account for Origination Process Enabled Scenario | Note This step can be executed if Bank Account Origiantion Process has been enabled, otherwise skip this step.Ensure all necessary data have been entered and choose Save.You can choose edit and enrich the data if necessary, then choose Start Opening.Choose Confirm Opening at Bank.Note The step of choosing Start Opening and choosing Confirm Opening at Bank is depending on the Preliminary step Enable Bank Account Origination Process setting. Only if the status 24 Pre-Opening Preparation has been configured and its enable status check box has been selected, you can execute the step Send Open Request to Bank. And only if the status 26 In Opening Process has been configured and its enable status check box has been selected, you can execute the step Confirm Opening at Bank. |  |  |
| 12 | Choose Payment Approvers tab | Choose the Payment Approvers tab. |  |  |
| 13 | Maintain Payment Approver for Payment Approver Group G001 | Make the following entries:Note Make sure you have finished the prerequisite step of Payment Approval Customizing, before you start maintain approver.Payment Approver Group: for example, G001 (the first step of two-step approval)Payment Approver: for example, the user ID assigned with the Accounts Payable Manager business roleCurrency: AEDMax. Amount for Payment: for example, 10,000,000.00Max. Amount for Batch Payment: for example, 50,000,000.00Note If the Unlimited Approval check box is selected, the payment approver can approve unlimited amount.Valid From: for example, <current date>.Valid To: for example, 31.12.9999 | The Payment Approver Group G001 is maintained. |  |
| 14 | Maintain Payment Approver for Payment Approver Group G002 | Repeat the previous step to create a User ID to Payment Approver group G002 (The second step for two-step approval).Use the same values in previous step, except that Payment Approver Group is (G002).For Payment Approver, enter the user ID assigned with the Cash Manager business role. The user ID assigned MUST be different from the user ID assigned to G001. | The Payment Approver Group G002 is maintained. |  |
| 15 | Check Approval Information | Choose Show Approval Step.You can find the detail information about approval sequence, approval amount for each approver. |  |  |
| 16 | Overdraft Limits | Make the following entries:Overdraft Type: SO01Overdraft Type Description: Overnight OverdraftOverdraft Category: Overnight OverdraftAmount: 10000 AEDValid From: Current DateValid To: 12/31/9999Note The valid period for the same overdraft type cannot overlap. You can maintain Overdraft Type in SSCUI 107092 Define Bank Account Overdraft Limit Types. |  | Overdraft Limit Type is controlled by Customer Control Feature Toggle FTGL_BAM_BKACCT_OVERDRAFT_TYPE, the feature toggle is deactivated by default. You can activate the feature toggle in SSCUI 106573 Activate Features. If the feature toggle is not activated, fields Overdraft Type, Overdraft Type Description and Overdraft Category will be hidden, SSCUI 107092 Define Bank Account Overdraft Limit Types will also be invisible. |
| 17 | Save and Activate Bank Account | Ensure all necessary data have been entered and choose Save as Inactive.Choose Activate. | A new bank account is created. |  |
| 18 | Review History and Revision | Select the new bank account. On the Bank Account screen, the new bank account is active in the display mode. No revision button exists.Choose Account Histories. A history dialog box displays with the history list of the current bank account: Revision 1, activated. |  |  |

###### Export Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank account modification in the production system is completed in the previous step. Because some system configuration is based on house bank and house bank account, after a bank account’s attribute is changed, you may need to update the configuration in the development system or consolidation test system. You can use Export/Import Bank Accounts functionality to faciliate your bank accounts' update.

Prerequisites

|  |
| --- |
| Note Use Microsoft Office 2010 or higher that includes Microsoft Excel.You must enable the Developer tab in Microsoft Excel. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Upload/download Account | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Export Bank Master Data XML file | In the Bank Accounts Export section, enter company code and choose Go. Select the check box of the bank accounts, and choose Export Bank Accounts to an XML File.In the File Download dialog box, choose Save As.In the Save As dialog box, identify a location to save the XML file.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The file is saved at the location you indicated. |  |
| 5 | Download XML Spreadsheet template | In the Bank Accounts Export section, choose Download XML Spreadsheet Template.In the Save As dialog box, identify a location to save the XML spreadsheet template.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The XML_Spreadsheet_Template.xml file is saved at the location you indicated. |  |
| 6 | Open XML Spreadsheet Template and Import Bank Account Master Data | Using Microsoft Excel to open XML_Spreadsheet_Template.xml.In the Microsoft Excel Developer tab, choose Import.Choose the Bank_Accounts.xml file in the Import XML dialog box.Choose Import. | Bank accounts master data have been imported into the XML spreadsheet template.If the system displays the message XML import error-Failed schema validation displays, but data have been imported from Bank_Accounts.xml, ignore this message and choose OK. |  |
| 7 | Export Data to a New XML File | In the Developer tab in Microsoft Excel, choose Export.Enter the file name Bank_Accounts_Export.xml and then choose Export. | Bank accounts master data is saved in Bank_Accounts_Export.xml. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This instruction guides you how to import the bank accounts into the target system, if you use Solution Builder environment with 2 system landscape, or use SAP Central Business Configuration with 2 system landscape, you may use this functinality to update your test system. If you use On-Premise system or use SAP Central Business Configuration with 3 system landscape, the development system can also be updated besides the test system.

|  |
| --- |
| Note You may only have one client for testing. You can test the function Export and Import the bank accounts in the same client. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Identify the Import Path | Choose Select File.In the Open dialog box, identify the XML (Bank_Accounts_Export.xml) to be uploaded.Choose Open. |  |  |
| 5 | Import with Test Run | Choose Import with Test Run and check the validation results.Note If the message Bank Account "1XXXXXXXXX" is already in approval process displays, we recommend that you import bank accounts next time, since some bank accounts are still in process workflow.When the message displays, only execute a test run, or complete the workflow before the production run.When the status of all validation results is OK, you can import bank accounts into production system. |  |  |
| 6 | Import XML file with Production Run | Choose Select File again.In the Open dialog box, identify the XML (Bank_Accounts.xml) to be uploaded.Choose Open.Choose Import and check the validation results. | Bank accounts are successfully imported into development system. |  |
| 7 | Import to Test System | Repeat the preceding steps to import bank accounts into consolidation test system. |  |  |

##### Change Bank Account

###### Notify Bank to Change

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system.

|  |
| --- |
| Note Bank account master data modification does not always result in a notification to the bank (for example, the modification of payment signatories). |

###### Change Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change a bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Change | Choose the bank account to be changed from the account list view.For example, account 0000000033108888.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Edit | Choose Edit. Modify fields to your requirements. |  |  |
| 5 | Save | Choose Save. | The bank account is changed (updated). |  |

|  |
| --- |
| Remember Define Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct this in the Define Basic Settings app , using the generic user Configuration Expert - Business Process Configuration in the Manage Your Solution (F1241) app. |

###### Update Bank G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update the G/L account of the bank (for example, if the currency key of the bank account is changed). However, not all bank account modifications result in a G/L account modification.

|  |
| --- |
| Note Update the G/L accounts in the production, development, and consolidation test systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241). |  |  |
| 3 | Search Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area : FinanceSub Application Area: General Ledger |  |  |
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
| 4 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note You can also complete the test by logging on as General Ledger Accountant and use Manage G/L Account Master Data (F0731A). |  |
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

|  |
| --- |
| Note You can access and use Manage G/L Account Master Data (F0731A) as a General Ledger Accountant to display master data. However, changes can only be made and saved via SSCUI (log on as Configuration Expert - Business Process Configuration and use the Manage G/L Account Master Data (F0731A) app).If the SSCUI in the Manage G/L Account Master Data (F0731A) app is only accessible in Display mode, you can still use the Manage G/L Account Master Data (F0731A) app with the General Ledger Accountant role to maintain master data. |

##### Repair Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can change back the bank accounts to preceding status or preceding versions with following steps.

Prerequisite

You have finished the [Define Repair Action for Bank Accounts](#unique_32) [page ] 50 configuration.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Repair | Choose the bank account to be repaired from the account list view.For example, account 0000000033108888 in AEBK3.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Repairing | Choose Return to Preceding Status or Restore Predecessor Version.Note The button appear as Return to Preceding Status or Restore Predecessor Version are depend on the settings of preliminary step [Define Repair Action for Bank Accounts](#unique_32) [page ] 50. |  |  |
| 5 | Save | Make a note and Choose Return to Preceding Status or Restore Predecessor Version. |  |  |

##### Close Bank Account and Cancel Closing

###### Notify Bank to Close Account

Purpose

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

This step describes how to close an obsolete bank account by bank accountant (Cash Management Specialist) and the process of cancel the closing if you want to activate it.

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
| Caution Do not close sample bank accounts that are connected to house bank AEBK1/AEAC1 and AEBK2/AEAC2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable ([J60](https://me.sap.com/processnavigator/SolP/J60)) and Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolP/J78)). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Close | Choose the triangle button of the bank account to be closed.For example, account 0000000033108888. |  |  |
| 4 | Mark for Closing | Choose Mark for Closing.Make the following entry in the dialog box and choose Mark for Closing.Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box. |  |  |
| 5 | Send Closing Request to Bank | Choose Send Closing Request to Bank. | The Send Closing Request to Bank dialog box is displayed. |  |
| 6 | Start to Initial Closing | Make the following entries in the dialog box and choose Send Closing Request to Bank:Planned Closing Date: for example, <current date>+2daysChoose OK in the success dialog box. | The bank account’s status is changed to Closing Request Sent to Bank.If the email address is properly maintained, an e-mail is sent out to the relevant person in charge automatically.For more information on maintaining the e-mail address, see the Advanced Bank Account Management (J77) test script, Prerequisites > Preliminary Steps > Define Output Parameter Determination.The e-mail address maintained here takes precedence as the sender if it is valid. If it is not valid, the sender's e-mail address defaults to the company code's email address.In the Manage Bank Accounts (F1366A) app, find the 8765432188 bank account . Choose the account to access its master data page. A log entry is created in Bank Correspondence tab.Note The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the e-mail address maintained in the Bank. |  |
| 7 | Confirm Closing at Bank | Choose Confirm Closing at Bank. | The Confirm Closing at Bank dialog box is displayed. |  |
| 8 | Start to Confirm Closing at Bank | Make the following entries in the dialog box and choose Confirm Closing at Bank:Closing Date: for example, <current date>Note If Bank Reconciliation Account is set in House Bank Account Connectivity, you can input a posting blocking date. You use posting block date to set a final date for marking financial postings to this bank account. After the specified posting block date, posting is no longer allowed for this bank account. This date allows you to add an additional check for financial postings and help you maintain correct data for Advanced Valuation in Financial Accounting. You set the posting block date when you change the bank account status to Closed at Bank. You can update the posting block date as needed before the bank account is set to the Close status. | The bank account’s status is changed to Closed at Bank. | You can choose confirm closing at bank without bank account initial closing. If you bypassing the initial closing procedure and choose confirm closing at bank, the bank account status will be changed to Closed at Bank directly. Output correspondence will be triggered, an e-mail is sent out to the relevant person in charge automatically, If the email address is properly maintained. |
| 9 | Complete Closing | Choose Complete Closing. |  | The actual balance of the bank account will be checked. The checking logic is defined in step Basic Settings. You can go to step Basic Settings to configure the Balance Check for Closing Process field as following:Blank: Balance Check Method (Deprecated)With this option set, you use the deprecated balance check method controlled via the configuration activity Change Message Control for Bank Account Management.10: No validation and close immediately.You set this option if you don't want to perform any bank account balance check when bank accounts are closed.20: Validate against aggregated actuals for amount in bank account currency in One Exposure.With this option set, the system checks the aggregated actuals of a bank account in One Exposure before the account is closed.Users can view the aggregated actuals for your bank account in the Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) app. To do so, in this app, do the following:In the Account Dimension field, select Bank Account (House Bank/House Bank Account).Set the reconciliation date as your current local date.In the Data Source Selection field, select Acnt Bal in Cash Pos (Tran Dt).Run the report. The Acnt Bal in Cash Position (Tran. Dt) field to show the aggregated actuals for bank accounts.To adjust the aggregated actuals for your bank account to produce zero, users can create a memo record to offset the current amount. To do so, in the Manage Memo Records 2.0 (F2986A) app, create a memo record with the memo record category Actual Cash Memo. Please note that the value date of the memo record must not be later than the bank account closing date. After the bank account balance is adjusted to zero, the bank account will no longer be visible in the report above.30: Validate against ledger balance (from bank statement).With this option set, the system checks the ledger balance of a bank account in the Manage Bank Account Balances (F5175) app before the account is closed. Only bank accounts for which the ledger balance is zero or has never been updated before can be closed.When the balance check error is shown, users need to ensure the ledger balance reflects the real balance of the bank account. They can import the latest bank statement that confirms the ledger balance is zero, or enter a ledger balance for this bank account in the Manage Bank Statements (F1564) app.To use option 30: Validate against ledger balance (from bank statement), make sure that all of your bank accounts are not set with the transfer mode No Update for Cash Management for end-of-day bank statements as the method requires that balance data is saved for cash management. |
| 10 | Start to Confirm Closing at Bank | Choose Close in the Complete Closing dialog box. | The bank account’s status is changed to Closed. |  |
| 11 | Return to Closed at Bank | Choose Return to Preceding Status. | The bank account’s status is changed to Closed at Bank. |  |
| 12 | Return to Closing Request Sent to Bank | Choose Return to Preceding Status. | The bank account’s status is changed to Closing Request Sent to Bank. |  |
| 13 | Return to Active | Choose Return to Preceding Status. | The bank account’s status is changed to Active. |  |

##### Maintain Payment Approver for Multiple Bank Accounts (Direct Revision Activate)

Prerequisites

Approval patterns and and payment approve group have to be defined and assigned to company code before you start following procedures. Make sure you have finished the prerequisite step of Payment Approval Customizing before you start to maintain payment approver. SAP has predelivered the sequential pattern P001 with payment approver group G001 and G002, and the nonsequential pattern s001 with payment approver group SG01 and SG02 as Demo data in Start system.

Use

This step describes how to maintain the Payment Approver for multiple bank accounts with Full Cash Management and Direct Revision Activate.

|  |
| --- |
| Note SAP supports sequential and nonsequential signatories for payment approval.Sequential Payment Approver: The payment approval should obey the approver sequence. For example, if the Accounts Payable Manager is set as the first approver, the Cash Manager is set as the second approver. The Cash Manager cannot approve the payment before the Accounts Payable Manager in sequential Payment Approver case.Nonsequential Payment Approver: No sequence exists for the approvers. The Payment Approver Group field decides the Payment Approver case you can choose. |

|  |
| --- |
| Caution The following procedure assumes that you are only maintaining the Payment Approver for multiple accounts with full cash procedures management using the Direct Revision Activate procedure. If you are implementing and testing additional full cash management options, especially in a single environment, you cannot use the same master data values for more than one procedure type. You must create additional master data values (for example G/L accounts) and use these different values in each procedure type. |

###### Add Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank accountant (Cash Management Specialist) triggers the maintenance of the Payment Approver in multiple bank accounts collectively, instead of individually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). |  |  |
| 3 | Select Company Code | Make the following entries and choose Go:Company Code: For example, 3310 | Multiple bank accounts of the company code display in the Results List. |  |
| 4 | Select Bank Accounts | Select the row for your bank accounts and choose Add Payment Approver:For example, bank account 0000000693123456 of bank key 18121976and bank account 0000000693123456 of bank key 18121986. | The Add Payment Approver screen displays. |  |
| 5 | Add Payment Approver to Payment Approver Group G001 | Make the following entries and choose OK:New Payment Approver: For example, <the user ID (CB*) assigned to the Accounts Payable Manager role>Valid From: For example, <current date>.Valid To: For example, 12/31/9999Payment Approver Group: G001Note Payment Approver Group G001 is used for sequential Payment Approver. To use nonsequential Payment Approver, use SG01.Max. Amount for Payment: For example, 100,000.00Max. Amount for Batch: For example, 1,000,000.00Note The check box of Unlimited Approval is used for grant the authorization of approving unlimited amount. When you select this check box, the value of Maximum Amount for Payment and Maximum Amount for Batch will be invalid, the Payment Approver can approve an unlimited amount.Currency: AED | The bank account is changed (updated). |  |
| 6 | Add Payment Approver to Payment Approver Group G002 | Make the following entries and choose OK:New Approver: For example, the user ID (CB*) of business user Cash Manager has business role Cash Manager assignedValid From: For example, <current date>Valid To: For example, 12/31/9999Payment Approver Group: For example, G002Note Payment Approver Group G002 is used for sequential Payment Approver. To use nonsequential Payment Approver, use SG02.Max. Amount for Payment: For example, 100,000.00Max. Amount for Batch: For example, 1,000,000.00Currency: AEDTitle: For example, Add Payment ApproverNote: <Enter a note> | The bank account is changed (updated).Note When using workflow mode and restricting the approver to a specific company code and account type (company code 3310 and account type 01) in the step [Manage Workflows](#unique_12) [page ] 19, refer to step [Define Basic Settings](#unique_9) [page ] 12 and check if the request grouping has been set as Goup by Company Code and Account Type. |  |

###### Change Payment Approver for Multiple Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can make mass maintenance of Payment Approver for multiple bank accounts. An individual approve and confirm process is required for change Payment Approver requests to one Payment Approver group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Open SAP Fiori App | Open Maintain Payment Approver (WDA_FCLM_BAM_ADAPT_SIGN (APP_CFG_FCLM_BAM_ADAPT_SIGN)). |  |  |
| 3 | Select Company Code | Make the following entries and choose Go:Company Code: For example, 3310Note You may need to add the field to the visible filters. | Multiple bank accounts of the company code are displayed in the Results List. |  |
| 4 | Select Bank Accounts | Select the row for your bank accounts and choose Change Payment Approver:For example, bank account 0000000693123456 of bank key 18121976 and bank account 0000000693123456 of bank key 18121986. | The Change Payment Approver screen is displayed. |  |
| 5 | Change Approver | Make the following entries and choose OK:New Payment Approver: For example, the user ID (CB*) assigned to the Cash Manager Specialist roleValid From: For example, current dateValid To: For example, 31.12.9999(New Payment Approver Section)Note Keep the Valid To date in Old Payment Approver section as current date. | The Payment Approver is changed for the bank account in the Manage Bank Account app. An entry is created in Bank Correspondence tab. An e-mail is sent out to the person in charge.Note The sender is the e-mail address maintained in Output Parameter Determination if the e-mail address is valid. For more information, see Preliminary Steps > Define Output Parameter Determination.The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the e-mail address maintained in the bank that the bank account belongs to.If the email address is invalid in Output Parameter Determination. Sender's e-mail address is defaulted as the company code’s email address.As long as the Payment Approver user, Valid From date or Valid To date fields are changed, an entry is created on the Bank Correspondence tab of the bank account and an e-mail is out. |  |

##### Upload Attachments for Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can upload attachments for the bank account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Binding Cash Pools as Leading Account | Make the following entries and choose Go:Account Number: An active account. For example, 1133698 | Note If the basic setting is Direct Revision Activate, the bank account is activated. |  |
| 4 | Bank Account View | In the data table, choose the arrow icon at the right of the row for the account. | The Bank Account view displays. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Upload Attachments | Navigate to Attachments tab.Select Doc.Type to Upload: AttachmentsChoose Upload.Select a document to upload.Choose Save. |  |  |

#### Using Dual Control Revision Activation

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
| 5 | Enter General Data | Make the following entries:Bank Name: AE Standard Bank for Advanced Bank Account Management Dual Control ModeChoose Create. | The standard bank is created. |  |
| 6 | Create Internal Banks | Go to the initial page of app Manage Banks - Master Data (F6437).Choose the triangle button beside the Create.Choose Create Internal Bank. |  |  |
| 7 | Enter Control Data | Make the following entries:Bank Country/Region: AEBank Key: 88888889Internal Bank Category: Payment Service ProviderChoose Create Internal Bank.Note If the bank key created is used for an internal virtual bank, for example, PayPal,which is used as House Bank, please select Internal - Payment Service Provider.which is used to enable the maintenance of the business partner bank details with alias, please select the Payment system. For more details, please refer to SSCUIs 105361 - Define Alias Types and 105362 - Define Payment Systems. |  |  |
| 8 | Enter General Data | Make the following entries:Bank Name: AE Internal Bank for Advanced Cash Management Dual Control ModeChoose Create. | The Internal bank is created. |  |

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
| 3 | Filter the Bank | Make the following entry in the filter and choose Go.Bank Key: 88800011 |  |  |
| 4 | Choose the Bank | Choose the Bank in the list. |  |  |
| 5 | Edit Bank | Choose Edit.Make the following entries:SWIFT/BIC: DEUTDEFFXX1City: for example, 60040 Frankfurt, Main |  |  |
| 5 | Save Your Entries | Choose Save. |  |  |

###### Create Bank G/L Account

Purpose

The G/L accountant may create the G/L accounts for a new bank account.

|  |
| --- |
| Note In cash management in this package, you can use the same G/L accounts (bank main account and bank subaccount) for different bank accounts if they use the same currency key. The balance of each bank account can be displayed in the Cash management app, instead of checking balances of the relevant G/L account. Using this approach keeps the chart of accounts smaller. |

|  |
| --- |
| Note If you want to create a G/L account for a new bank account, execute the following steps. Create G/L accounts in production system, development system, and consolidation test system. |

|  |
| --- |
| Note This procedure is mentioned in the Accounting and Financial Close ([J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58)) test script. Refer to the step Manage G/L Account Master Data and copy an existing G/L Account to a new one, for example, copy 11001000 to 11003000. |

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
| 4 | Enter Risk Business Partner | Choose Edit.Make the following entry:Risk Business Partner: for example, 55555 | The Manage Banks view displays. |  |
| 5 | Enter House Bank Data | Go to House Banks tab and choose Create.Make the following entries:Company Code: 3310House Bank: AEBK3Choose Continue.Choose Apply. |  |  |
| 6 | Enter Netting Business Partner | Go to Netting Business Partner tab.Make the following entries:Valid From: <Current Date>.Valid To: <Futrue Date>.Business Partner: <Choose one by using search help> |  |  |
| 7 | Save Bank | Choose Save. | New house bank is saved successfully. |  |

###### Create Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a bank account.

|  |
| --- |
| Note Since bank accounts are not transportable to the production system, they must be maintained manually there. |

|  |
| --- |
| Remember The [Define Basic Settings](#unique_9) [page ] 12 topic in the Prerequisites section must be reviewed following any system upgrade or improvement before continuing any business operations. When differences are found from previous activations, you have to correct in the SSCUI 101025 Define Basic Settings. In this setting, set the Cash Scope field to Full Scope and the Bank Account Control Mode field to Dual Control. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Add | Choose Create to add a new bank account.Make the following entries.Company Code: 3310Account Type: 01 | The Bank Account screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Account Number: 0000000033108888Account Description: AEBank Account for Advanced Bank Account Management Dual Control ModeBank Country/Region: AEBank Key: 88800011Currency:AED |  |  |
| 5 | Enter General Data | Change the following entries:Opening Date: for example, <current date>Account Holder: Company Code3310 (company code name is usually defaulted by system)Bank Control Key: for example, PNote Bank Control Key is only used in some countries like France, Spain, Italy. If you don't use Bank Control Key, you should leave this field blank.IBAN: <Generate IBAN>Note Only perform this step if the country is using IBAN; if you do not use IBAN in your process, just skip this step. |  |  |
| 6 | Bank Relationship Data | Pmnt Tran Type Group: CAMT053Note The field Transaction Type is not available for on premise. To assign the Transaction Type to your Bank Account use the IMG Menu Path: Financial Accounting > Bank Accounting > Business Transactions > Payment Transactions > Electronic Bank Statement > Make Global Settings for Electronic Bank StatementsNote If you are going to upload camt.054 format bank statement for supplier financing, which is described in test script 1EG, the field Pmnt Tran Type Group has to be maintained as camt053, otherwise camt054 bank statement can't be uploaded. |  |  |
| 7 | Maintain Internal Bank Account Contact | In the Contact Persons area (in the Bank Relationship section), enter a system user ID, for example, the ID assigned with the business role of Cash Management Specialist.Enter the ID in the Internal Bank Account Contact field. |  |  |
| 8 | Maintain Internal Bank Account Supervisor | In the Contact Persons area, enter a system user ID, for example, the ID assigned with the business role of Cash ManagerEnter the user ID in the Maintain Internal Bank Account Supervisor field. |  |  |
| 9 | Choose Bank Relationship Tab | In the Bank Statement Data area, make the following entries:Processing status: SelectedInterval: for example, 01Interval Unit: for example, MonthsFactory Calendar ID: for example, 01Note Processing status: Indicates whether to monitor this bank account at the end of the day in Bank Statement Monitor.Interval: Specifies how often the bank statements for a bank account are imported to your system.Interval Unit: Specifies the unit of measurement for an interval.Factory Calendar ID: Distinguishes between working days and non-working days. |  |  |
| 10 | Choose House Bank Account Connectivity | Choose the House Bank Account Connectivity tab. | The House Bank Account Connectivity tab displays. | House Bank Account Connectivity allows you to associate a bank account with its house bank account in the central system where SAP S/4HANA Cloud Public Edition Finance for Cash Management is installed. It also enables connections to accounts in remote SAP or third-party systems. For additional information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US). |
| 11 | Enter House Bank Account Connectivity | Choose Create.Make the following entries:ID Category: for example, Central System: House Bank AccountNote If the house bank account only exist in the local system you can specify the ID Category as Central System: House Bank Account; If the house bank account exist in remote system, and need to be migrated to local system, you can specify the ID Category to Remote System: House Bank AccountRemote System: <Leave blank>Note If you have enabled the Convert Remote House Bank Accounts functionality in the configuration activity Define System Groups (107199), please ensure that all necessary attributes for the remote house bank accounts to be replicated are properly maintained prior to their conversion to the ID category Central System: House Bank Account. These accounts are then replicated back to the originating target system. Incorrect or missing attributes may result in validation errors in the target systems. For further information, please refer to the online help [Define House Bank Account Connectivity](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/2abbcf54a14a713be10000000a44176d.html?version=LATEST&locale=en-US) and [Outbound Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/9b57a8997a02462989f2d0b168dac811.html?version=LATEST&locale=en-US).Company Code: 3310House Bank: AEBK3House Bank Acct ID: AEAC3G/L Account: 11001000Use in Cash Pooling: <Deselected>Note The Use in Cash Pooling field determines if the house bank account is used for cash pooling. If the checkbox is selected, this house bank account can be used for cash pooling. If there are multiple house bank accounts for one bank account, only one house bank account can be used for cash pooling. |  |  |
| 12 | Choose Payment Approvers tab | Choose the Payment Approvers tab. |  |  |
| 13 | Maintain Payment Approver for Payment Approver Group G001 | Make the following entries:Note Make sure you have finished the prerequisite step of Payment Approval Customizing, before you start maintain approver.Payment Approver Group: for example, G001 (the first step of two-step approval)Payment Approver: for example, the user ID assigned with the Accounts Payable Manager business roleCurrency: AEDMax. Amount for Payment: for example, 10,000,000.00Max. Amount for Batch Payment: for example, 50,000,000.00Note If the Unlimited Approval check box is selected, the payment approver can approve unlimited amount.Valid From: for example, <current date>.Valid To: for example, 31.12.9999 | The Payment Approver Group G001 is maintained. |  |
| 14 | Maintain Payment Approver for Payment Approver Group G002 | Repeat the previous step to create a User ID to Payment Approver group G002 (The second step for two-step approval).Use the same values in previous step, except that Payment Approver Group is (G002).For Payment Approver, enter the user ID assigned with the Cash Manager business role. The user ID assigned MUST be different from the user ID assigned to G001. | The Payment Approver Group G002 is maintained. |  |
| 15 | Check Approval Information | Choose Show Approval Step.You can find the detail information about approval sequence, approval amount for each approver. |  |  |
| 16 | Overdraft Limits | Make the following entries:Overdraft Type: SO01Overdraft Type Description: Overnight OverdraftOverdraft Category: Overnight OverdraftAmount: 10000 AEDValid From: Current DateValid To: 12/31/9999Note The valid period for the same overdraft type cannot overlap. You can maintain Overdraft Type in SSCUI 107092 Define Bank Account Overdraft Limit Types. |  | Overdraft Limit Type is controlled by Customer Control Feature Toggle FTGL_BAM_BKACCT_OVERDRAFT_TYPE, the feature toggle is deactivated by default. You can activate the feature toggle in SSCUI 106573 Activate Features. If the feature toggle is not activated, fields Overdraft Type, Overdraft Type Description and Overdraft Category will be hidden, SSCUI 107092 Define Bank Account Overdraft Limit Types will also be invisible. |
| 17 | Save as inactive and submit for Activation | Ensure all necessary data have been entered and choose Save as Inactive.Choose Submit for Confirmation. | A new bank account is created in an inactive revision. |  |
| 18 | Review History and Revision | Select the new bank account in the Bank Account view. The new bank account is To Be Active in the display mode.Choose View History and the Revision Number and Revision Status displays for the current bank account.Proceed to the next step to activate the account. |  |  |

###### Export Bank Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The bank account modification in the production system is completed in the previous step. Because some system configuration is based on house bank and house bank account, after a bank account’s attribute is changed, you may need to update the configuration in the development system or consolidation test system. You can use Export/Import Bank Accounts functionality to faciliate your bank accounts' update.

Prerequisites

|  |
| --- |
| Note Use Microsoft Office 2010 or higher that includes Microsoft Excel.You must enable the Developer tab in Microsoft Excel. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Upload/download Account | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Export Bank Master Data XML file | In the Bank Accounts Export section, enter company code and choose Go. Select the check box of the bank accounts, and choose Export Bank Accounts to an XML File.In the File Download dialog box, choose Save As.In the Save As dialog box, identify a location to save the XML file.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The file is saved at the location you indicated. |  |
| 5 | Download XML Spreadsheet template | In the Bank Accounts Export section, choose Download XML Spreadsheet Template.In the Save As dialog box, identify a location to save the XML spreadsheet template.Choose Save.Note Download processing steps varies on different browser, above steps apply to IE. If you are using Chrome, the file will be directly saved in C:\Users\[your user ID]\Downloads | The XML_Spreadsheet_Template.xml file is saved at the location you indicated. |  |
| 6 | Open XML Spreadsheet Template and Import Bank Account Master Data | Using Microsoft Excel to open XML_Spreadsheet_Template.xml.In the Microsoft Excel Developer tab, choose Import.Choose the Bank_Accounts.xml file in the Import XML dialog box.Choose Import. | Bank accounts master data have been imported into the XML spreadsheet template.If the system displays the message XML import error-Failed schema validation displays, but data have been imported from Bank_Accounts.xml, ignore this message and choose OK. |  |
| 7 | Export Data to a New XML File | In the Developer tab in Microsoft Excel, choose Export.Enter the file name Bank_Accounts_Export.xml and then choose Export. | Bank accounts master data is saved in Bank_Accounts_Export.xml. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This instruction guides you how to import the bank accounts into the target system, if you use Solution Builder environment with 2 system landscape, or use SAP Central Business Configuration with 2 system landscape, you may use this functinality to update your test system. If you use SAP Central Business Configuration with 3 system landscape, you can use it to update development and test system.

|  |
| --- |
| Note You may only have one client for testing. You can test the function Export and Import the bank accounts in the same client. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Import and Export Accounts | Choose Import and Export Bank Accounts. | The Import and Export Bank Accounts screen displays. |  |
| 4 | Identify the Import Path | Choose Select File.In the Open dialog box, identify the XML (Bank_Accounts_Export.xml) to be uploaded.Choose Open. |  |  |
| 5 | Import with Test Run | Choose Import with Test Run and check the validation results.Note If the message Bank Account "1XXXXXXXXX" is already in approval process displays, we recommend that you import bank accounts next time, since some bank accounts are still in process workflow.When the message displays, only execute a test run, or complete the workflow before the production run.When the status of all validation results is OK, you can import bank accounts into production system. |  |  |
| 6 | Import XML file with Production Run | Choose Select File again.In the Open dialog box, identify the XML (Bank_Accounts.xml) to be uploaded.Choose Open.Choose Import and check the validation results. | Bank accounts are successfully imported into development system. |  |
| 7 | Import to Test System | Repeat the preceding steps to import bank accounts into consolidation test system. |  |  |

##### Change Bank Account

###### Notify Bank to Change

Purpose

The bank accountant (Cash Management Specialist) goes to the bank and asks the bank employee to change the attributes of this bank account. This step does not occur in the system.

|  |
| --- |
| Note Bank account master data modification does not always result in a notification to the bank (for example, the modification of payment signatories). |

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Change | Choose the bank account to be changed from the account list view.For example, account 0000000033108888 in AEBK3.Enter the filter and choose Go. | A new window displays. |  |
| 4 | Start to Edit | Choose Edit. Modify fields to your requirements. |  |  |
| 5 | Save Your Changes | Choose Save to save the changes. | The bank account is changed (Inactive). |  |

|  |
| --- |
| Remember [Define Basic Settings](#unique_9) [page ] 12 must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you have to correct in the SSCUI Define Basic Settings. |

###### Update Bank G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The key user updates the G/L account of the bank only when required. For example, if the currency key of the bank account is changed, the user updates the currency of G/L account. However, not all bank account modifications result in a G/L account modification.

|  |
| --- |
| Note Update the G/L accounts in the production, development, and consolidation test systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Your Solution (F1241). |  |  |
| 3 | Search Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries and choose Go:Application Area: FinanceSub Application Area: General Ledger |  |  |
| 5 | Choose the G/L Account to Update | Choose the G/L account link. |  |  |
| 6 | Open | Choose the arrow at the right of the column with the Chart of Accounts item. |  |  |
| 7 | Select Configuration Step | For the Manage G/L Account Master Data step, choose Configure. |  |  |
| 8 | Edit the Account | Choose Edit. |  |  |
| 9 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note If you cannot find the SSCUI, you can complete the test with the Manage G/L Account Master Data (F0731A) app. |  |
| 10 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 11 | Choose the G/L Account | Choose the G/L Account from the search results.Note Click the blue account number link. | The G/L account is updated successfully. |  |
| 12 | Edit the Account | Choose Edit. |  |  |
| 13 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 14 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 15 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 16 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Manage G/L Account Master Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage G/L Account Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Edit the Account | Choose Edit. |  |  |
| 4 | Choose Company Code | If prompted, choose the company code 3310 in which to change the G/L account. | The Manage G/L Account Master Data screen displays.Note If you cannot find the SSCUI, you can complete the test with the Manage G/L Account Master Data (F0731A) app. |  |
| 5 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 11001000View: Chart of Accounts View | Relevant bank subaccounts are updated. |  |
| 6 | Choose the G/L Account | Choose the G/L Account from the search results.Note Click the blue account number link. | The G/L account is updated successfully. |  |
| 7 | Edit the Account | Choose Edit. |  |  |
| 8 | Choose Company Code | Choose the company code 3310 in which to change the G/L account. | A screen showing the account parameters at the company code level displays. |  |
| 9 | Maintain the attributes of the G/L account at Company Code Level | Update the attributes of the account.For example, change Account Currency to a different currency from the one you used when creating a bank account in the previous step Create Bank Account Change Request, and deselect the checkbox of Only Balance in Local Currency. |  |  |
| 10 | Save the G/L Account | Choose Save. | The G/L account is updated successfully. |  |
| 11 | Update Bank Subaccount | Repeat the preceding steps to change bank subaccounts.For example, from 11001010 to 11001099. | Relevant bank subaccounts are updated. |  |

|  |
| --- |
| Note Changing the currency is not possible when there is an existing balance for the G/L account. |

##### Close Bank Account and Cancel Closing

###### Notify Bank to Close Account

Purpose

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

This step describes how to close an obsolete bank account by bank accountant (Cash Management Specialist) and the process of cancel the closing if you want to reactivate it.

Prerequisite

There are five indicators to display the status of a bank account.

| Status | Comment |
| --- | --- |
| Active | This status indicates bank account is successfully created in sap system and can be normally used. |
| Inactive | This status displayed in full cash management, it indicates bank account is initially created without being approved. |
| Closing Request Sent to Bank | This status indicates you have planned and informed the bank to close the bank account in a future date. After initial closing button is triggered and approved, the bank account status will be display as To be Closed. The function of bank account in status To be Closed is the same with bank account status active, for example, you can still normally use it as review bank account, make bank transfer, run payment, posting etc. |
| Closed at Bank | This status indicates the bank account has been closed by the bank. You can’t make bank transfer, run payment, review bank account, maintain payment approver, import signatory cards, monitor intraday/end of day bank statement and being displayed in bank relationship overview in this status. If you set a posting block date for a bank reconciliation account in Start to Confirm Closing at Bank step, no posting is allowed after that specific date. However, you can still make postings for other G/L accounts, unless the G/L accounts has been blocked from General Ledger Accounting side. |
| Closed | This status indicates the bank account is completely closed in sap system, no posting is allowed for bank reconciliation accounts, you can find bank reconciliation accounts details in online help: [Define G/L Accounts for Payment Processes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/781544a06fc6476fa99755b96a3006be.html?locale=en-US). However, you can still make postings for other G/L accounts. Unless the G/L account has been blocked from General Ledger Accounting side, you can refer to online help: [Mark G/L Accounts as Not Used](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/2052bdb5d8fc4b6d9d787ea991e3613d.html?locale=en-US) and [G/L Accounts Blocked in P System Until Transport of Changes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/e392432f0b2041528a118f8373f2269d.html?locale=en-US). |

|  |
| --- |
| Caution Do not close sample bank accounts that are connected to house bank AEBK1/AEAC1 and AEBK2/AEAC2 in the Connectivity Path tab for the bank master data (bank account 0000000693123456 of bank key 18121976, and bank account 0000000693123456 of bank key 18121986). The sample bank accounts are used when testing other scope items, for example, Accounts Payable (J60) and Advanced Cash Operations (J78). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Accounts (F1366A). |  |  |
| 3 | Choose the Bank Account to Close | Choose the triangle button of the bank account to be closedFor example, account 0000000033108888 in AEBK3. |  |  |
| 4 | Mark for Closing | Choose Mark for Closing.Make the following entry in the dialog box and choose Mark for Closing.Planned Closing Date: for example, <current date + 2 days>Choose OK in the success dialog box.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. |  |  |
| 5 | Send Closing Request to Bank | Choose Send Closing Request to Bank. | The Send Closing Request to Bank dialog box is displayed. |  |
| 6 | Start to Initial Closing | Make the following entries in the dialog box and choose Send Closing Request to Bank:Planned Closing Date: for example, <current date + 2days>Choose OK in the Information dialog box.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to To be Closed.If the email address is properly maintained, an e-mail is sent out to the relevant person in charge automatically.For more information on maintaining the e-mail address, see the Advanced Bank Account Management (J77) test script, Prerequisites > Preliminary Steps > Define Output Parameter Determination.The e-mail address maintained here takes precedence as the sender if it is valid. If it is not valid, the sender's e-mail address defaults to the company code's email address.In the Manage Bank Accounts (F1366A) app, find the 0000000033108888 bank account . Choose the account to access its master data page. A log entry is created in Bank Correspondence tab.Note The receiver is the Bank Contact Person. If Bank Contact Person is not maintained, the receiver is Bank Relationship Manager. If Bank Relationship Manager is not maintained, the receiver is the e-mail address maintained in the Bank. |  |
| 7 | Confirm Closing at Bank | Choose Confirm Closing at Bank. | The Confirm Closing at Bank dialog box is displayed. |  |
| 8 | Start to Confirm Closing at Bank | Make the following entries in the dialog box and choose Confirm Closing at Bank:Closing Date: for example, <current date>Note If Bank Reconciliation Account is set in House Bank Account Connectivity, you can input a posting blocking date. You use posting block date to set a final date for marking financial postings to this bank account. After the specified posting block date, posting is no longer allowed for this bank account. This date allows you to add an additional check for financial postings and help you maintain correct data for Advanced Valuation in Financial Accounting. You set the posting block date when you change the bank account status to Closed at Bank. You can update the posting block date as needed before the bank account is set to the Close status.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to Closed at Bank. | You can choose confirm closing at bank without bank account initial closing. If you bypassing the initial closing procedure and choose confirm closing at bank, the bank account status will be changed to Closed at Bank directly. Output correspondence will be triggered, an e-mail is sent out to the relevant person in charge automatically, If the email address is properly maintained. |
| 9 | Complete Closing | Choose Complete Closing. |  | The actual balance of the bank account will be checked. The checking logic is defined in step Basic Settings. You can go to step Basic Settings to configure the Balance Check for Closing Process field as following:Blank: Balance Check Method (Deprecated)With this option set, you use the deprecated balance check method controlled via the configuration activity Change Message Control for Bank Account Management.10: No validation and close immediately.You set this option if you don't want to perform any bank account balance check when bank accounts are closed.20: Validate against aggregated actuals for amount in bank account currency in One Exposure.With this option set, the system checks the aggregated actuals of a bank account in One Exposure before the account is closed.Users can view the aggregated actuals for your bank account in the Bank Account Balance Reconciliation with Drill Down (FCLM_BANK_RECONCIL) app. To do so, in this app, do the following:In the Account Dimension field, select Bank Account (House Bank/House Bank Account).Set the reconciliation date as your current local date.In the Data Source Selection field, select Acnt Bal in Cash Pos (Tran Dt).Run the report. The Acnt Bal in Cash Position (Tran. Dt) field to show the aggregated actuals for bank accounts.To adjust the aggregated actuals for your bank account to produce zero, users can create a memo record to offset the current amount. To do so, in the Manage Memo Records 2.0 (F2986A) app, create a memo record with the memo record category Actual Cash Memo. Please note that the value date of the memo record must not be later than the bank account closing date. After the bank account balance is adjusted to zero, the bank account will no longer be visible in the report above.30: Validate against ledger balance (from bank statement).With this option set, the system checks the ledger balance of a bank account in the Manage Bank Account Balances (F5175) app before the account is closed. Only bank accounts for which the ledger balance is zero or has never been updated before can be closed.When the balance check error is shown, users need to ensure the ledger balance reflects the real balance of the bank account. They can import the latest bank statement that confirms the ledger balance is zero, or enter a ledger balance for this bank account in the Manage Bank Statements (F1564) app.To use option 30: Validate against ledger balance (from bank statement), make sure that all of your bank accounts are not set with the transfer mode No Update for Cash Management for end-of-day bank statements as the method requires that balance data is saved for cash management. |
| 10 | Start to Confirm Closing at Bank | Choose Close in the Complete Closing dialog box.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to Closed. |  |
| 11 | Return to Closed at Bank | Choose Return to Preceding Status.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to Closed at Bank. |  |
| 12 | Return to Closing Request Sent to Bank | Choose Return to Preceding Status.Refer to Activate the Bank Account Request via Dual Control step to activate the change request. | A bank account change request has been created. Follow the steps in Activate the Bank Account Request via Dual Control to activate this request. Once completed, the bank account status will be updated to Closing Request Sent to Bank. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Enable Bank Account Contract Type: the Configure Your Solution note says contract types support full cash management with Activate Directly, Two-Person Verification and Activate via Workflow, but the SAP Central Business Configuration note lists only Activate Directly and Activate via Workflow.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Request grouping value 01 means Group into a Single Change Request in Define Basic Settings (workflow procedure), but the Manage Workflows team note says 01 applies when only Company Code is restricted (00 none, 02 account type only, 03 both).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Dual control closing section: status Closing Request Sent to Bank is described as showing as To be Closed in the status table and step 6, while later steps and the lifecycle list use Closing Request Sent to Bank.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-02]]
- related-to :: [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J77_S4CLD2608_BPD_EN_AE.docx` — lines 1–2888 of the extracted text · extracted with `mammoth` · 466,078 chars in the whole document
