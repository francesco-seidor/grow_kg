---
id: 03-financial-accounting-and-close/test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e
title: "Test Script: Advanced Payment Management (4MT) - SAP S/4HANA Cloud Public Edition (4MT_S4CLD2608_BPD_EN_XX)"
description: "S/4HANA Cloud 2608 test script for 4MT Advanced Payment Management: config prerequisites and tests for payments, bank statement forwarding, watch list screening"
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/basic-payment-management]
aliases: [4MT_S4CLD2608_BPD_EN_XX]
keywords: [Basic and Advanced Payment Management, advanced payment management, payment agreements, payment approval, multi-bank connectivity, bank rejection handling, csv payment files, bank statement forwarding, watch list screening, payment monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MT_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1037
topic: 03-financial-accounting-and-close/basic-payment-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Advanced Payment Management (4MT) - SAP S/4HANA Cloud Public Edition (4MT_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MT_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Basic and Advanced Payment Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Advanced Payment Management (4MT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232836134)

[2 Prerequisites 4](#_Toc232836135)

[2.1 System Access 4](#_Toc232836136)

[2.2 Roles 4](#_Toc232836137)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232836138)

[2.4 Additional Manual Configuration 6](#_Toc232836139)

[2.5 Business Conditions 6](#_Toc232836140)

[2.6 Preliminary Steps 7](#_Toc232836141)

[2.6.1 Maintain Routing Settings (Optional) 7](#_Toc232836142)

[2.6.2 Maintain DMEE Outbound Settings for MBC Connector 9](#_Toc232836143)

[2.6.3 Maintain Payment Agreements 10](#_Toc232836144)

[2.6.4 Manage Workflow for Payment Agreement 12](#_Toc232836145)

[2.6.5 Set Up Outgoing Payment in Contract Accounting 14](#_Toc232836146)

[2.6.6 Manage Teams and Responsibility (Optional) 14](#_Toc232836147)

[2.6.7 Assign Exception Handling Reaction to Bank Rejection 15](#_Toc232836148)

[2.6.8 Define Settings for Forwarding Bank Statements 18](#_Toc232836149)

[2.6.9 Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages 19](#_Toc232836150)

[3 Overview Table 23](#_Toc232836151)

[4 Test Procedures 27](#_Toc232836152)

[4.1 Payment Processes for SAP Systems 27](#_Toc232836153)

[4.1.1 Configure Situation Types 27](#_Toc232836154)

[4.1.2 Create Payments 28](#_Toc232836155)

[4.1.3 Monitor Batch and Payment 28](#_Toc232836156)

[4.1.4 Update of Cash Management 30](#_Toc232836157)

[4.1.5 (Partial) Approval / Reject by Approver 30](#_Toc232836158)

[4.1.6 Rejected Payments 31](#_Toc232836159)

[4.1.7 Check Notification 31](#_Toc232836160)

[4.1.8 Process Payment 31](#_Toc232836161)

[4.1.9 Accepted Payments 32](#_Toc232836162)

[4.1.10 Payment Format Management Outbound 33](#_Toc232836163)

[4.1.11 Update Payment Management Monitor 33](#_Toc232836164)

[4.1.12 Send Payment File 33](#_Toc232836165)

[4.1.13 Payment File Received by Bank 34](#_Toc232836166)

[4.1.14 Payment Instruction with Accepted Status Sent by Bank 34](#_Toc232836167)

[4.1.15 Payment Instruction Received 34](#_Toc232836168)

[4.2 Payment Processes for non-SAP Systems 34](#_Toc232836169)

[4.2.1 Prepare CSV Payment File 34](#_Toc232836170)

[4.2.2 Import CSV Payment File 37](#_Toc232836171)

[4.2.3 Upload Payment File 38](#_Toc232836172)

[4.2.4 Monitor Batch and Payment 38](#_Toc232836173)

[4.2.5 Update of Cash Management 39](#_Toc232836174)

[4.2.6 (Partial) Approval / Reject by Approver 39](#_Toc232836175)

[4.2.7 Rejected Payments 40](#_Toc232836176)

[4.2.8 Inform User via Notification 40](#_Toc232836177)

[4.2.9 Accepted Payments 40](#_Toc232836178)

[4.2.10 Payment Format Management Outbound 41](#_Toc232836179)

[4.2.11 Update Payment Management Monitor 41](#_Toc232836180)

[4.2.12 Send Payment File 41](#_Toc232836181)

[4.2.13 Payment File Received by Bank 42](#_Toc232836182)

[4.2.14 Payment Instruction with Accepted Status Sent by Bank 42](#_Toc232836183)

[4.2.15 Payment Instruction Received 42](#_Toc232836184)

[4.3 Forwarding of Bank Statement 42](#_Toc232836185)

[4.3.1 Import Electronic Bank Statement 42](#_Toc232836186)

[4.3.2 Check Upload Results 49](#_Toc232836187)

[4.3.3 Check Cash Update 50](#_Toc232836188)

[4.3.4 Check Bank Statement 50](#_Toc232836189)

[4.3.5 Check Multi-Bank Connectivity Messages 50](#_Toc232836190)

[4.4 Watch-List Screening 50](#_Toc232836191)

[4.4.1 Create Payment 51](#_Toc232836192)

[4.4.2 Monitor Payments (Status Before WLS) 57](#_Toc232836193)

[4.4.3 Screening of Payment 58](#_Toc232836194)

[4.4.4 Monitor Payments (Status After WLS) 59](#_Toc232836195)

## Purpose

Overview

Advanced Payment Management supports the monitoring and approval of payments for both SAP systems and non-SAP systems. In the overall process, there’s a seamless integration with cash management. The conversion of various payment formats is also supported (for example, converting CSV or TXT files to XML).

|  |
| --- |
| Note There is a limitation on supported formats. Only a valid standard ISO format can be consumed by Advanced Payment Management. Consequently, the integration with 2DP Contract Accounting – Company Initiated Payments supports DE but not US. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/4MT_S4CLD2602_BPD_EN_XX.docx)). |

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
| Payment Specialist | SAP_BR_PAYMENT_SPECIALIST | Payment Management | SAP_BR_PAYM_SPECIALIST |  |
| Business Integration Specialist - Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Bank Integration | SAP_BR_BANK_INT_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Compliance Specialist - Screening (GRC) |  |  |  | Please refer to this link[http://help.sap.com/wls](http://help.sap.com/wls) and refer to the Chapter 6 User Management in the file Administration Guide for SAP Watch List Screening to create test users. |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/97316a8bd3ed147a234d8bba800b0763)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J77 - Advanced Bank Account Management | Payment approvers are maintained per bank account to enable payment approvals. |
| 2DP - Contract Accounting – Company Initiated Payments | When a payment run is conducted, a payment media file is generated.The mandatory manual configuration is conducted to integrate Contract Accounting with Multi-Bank Connectivity. |
| 16R - Bank Integration with SAP Multi-Bank Connectivity | 16R - Multi-Bank Connectivity is in scope and a connection is set up.After payment run is conducted in 2DP - Contract Accounting – Company Initiated Payments, the payment media file is transmitted into Multi-Bank Connectivity and displayed in the 4MT - Advanced Payment Management Payment Monitor list.After the payment is transmitted to Multi-Bank Connectivity, a pain.002 status report with status code RJCT is received. |
| J78 - Advanced Cash Operations | After payment processing in 4MT - Advanced Payment Management, the outgoing payment is approved in J78 - Advanced Cash Operations. |
| 31N - Situation Handling | You install this scope item for the situation handling steps. |

### Preliminary Steps

#### Maintain Routing Settings (Optional)

Use

In this activity, you enable the local routing for payments originated from FI-CA (Convergent Contract Accounting) or FI (Accounts Payable, Accounts Receivable). After configuring the following setting, the payment can be processed and approved.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution. |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | A list of Configuration Items displays with the filter criteria. |  |
| 5 | Select Multi-Bank Connectivity Connector | Select the following row:Item Name: Multi-Bank Connectivity Connector | The Configuration Your Solution - Multi-Bank Connectivity Connector view displays. |  |
| 6 | Maintain Routing Settings for Outbound Messages | From the Configuration Steps area, on the Maintain Routing Settings for Outbound Messages step, choose Configure. | The "Maintain Routing Settings for Outbound Mess.." : Change view displays. |  |
| 7 | Maintain Local Routing for Origin FICA | Choose New Entries, make the following entries in the New Entries: Overview of Added Entries view and choose Save:Origin: FICARouting: LOCALIf payments originated from FI are to be processed in Advanced Payment Management for your scenario, repeat the step to create a new entry with Origin FIPMW, Routing LOCAL and a specific message type.Note In case of FIPMW origin, the message type must not be blank.If no message type is assigned or wrong message type is assigned, messages that are supposed to be sent out of SAP S/4HANA Cloud Public Edition could be wrongly routed internally.Check the test script of Accounts Receivable ([J59](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J59)) and Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) to figure out whether the payments are processed in Advanced Payment Management, and which message type are relevant. | A local routing for FICA is added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Routing Settings for Outbound Messages | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Routing Settings for Outbound Messages.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Maintain Routing Settings for Outbound Mess.." : Change view displays. |  |
| 3 | Maintain Local Routing for Origin FICA | Choose New Entries, make the following entries in the New Entries: Overview of Added Entries view and choose Save:Origin: FICARouting: LOCALIf payments originated from FI are to be processed in Advanced Payment Management for your scenario, repeat the step to create a new entry with Origin FIPMW, Routing LOCAL and a specific message type.Note In case of FIPMW origin, the message type must not be blank.If no message type is assigned or wrong message type is assigned, messages that are supposed to be sent out of SAP S/4HANA Cloud Public Edition could be wrongly routed internally.Check the test script of Accounts Receivable ([J59](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J59)) and Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) to figure out whether the payments are processed in Advanced Payment Management, and which message type are relevant. | A local routing for FICA is added. |  |

#### Maintain DMEE Outbound Settings for MBC Connector

Use

In this activity, you maintain the Outgoing Mapping Format setting for MBC Connector.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access App | Open Manage Your Solution. |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | A list of Configuration Items displays with the filter criteria. |  |
| 5 | Select Advanced Payment Management | Select the following row:Item Name: Advanced Payment Management | The Configuration Your Solution - Advanced Payment Management view displays. |  |
| 6 | Define DMEE Outbound Settings for MBC Connector | From the Configuration Steps area, on the Define DMEE Outbound Settings for Multi-Bank Connectivity Connector step, choose Configure. | The Define DMEE Outbound Settings for Multi-Ban..:Change view displays. |  |
| 7 | Maintain Message Type for Format Tree | Choose New Entries, make the following entries in the New Entries: Details of Added Entries view and choose Save:Clearing Area: PFFormat Tree: CGI_XML_CTMessage Type: PAIN.001.001.03 | A new message type is added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define DMEE Outbound Settings for MBC Connector | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define DMEE Outbound Settings for Multi-Bank Connectivity Connector.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define DMEE Outbound Settings for Multi-Ban..:Change screen displays. |  |
|  | Maintain Message Type for Format Tree | Choose New Entries, make the following entries in the New Entries: Details of Added Entries view and choose Save:Clearing Area: PFFormat Tree: CGI_XML_CTMessage Type: PAIN.001.001.03 | A new message type is added. |  |

#### Maintain Payment Agreements

Use

In this activity, you maintain the Advanced Payment Management master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payment Agreements. |  |  |
| 3 | Payment Agreements | Choose the Payment Agreements tab. |  |  |
| 4 | Create Agreement | Enter the Clearing Area: For example, Payment Factory Default Configuration (PF). Choose Create Agreement.Make the following entries and choose Save and Release:Agreement ID: for example, BANK_CTDescription: for example, Bank Credit TransferCompany Code: <the company code that the payment, for example FI-CA, belongs to>Processing Option: Forward the entire Incoming Order (B)Converter ID: MBDMEOFormat Tree: CGI_XML_CT | A payment agreement is created.Note If there is no workflow defined which matches the payment agreement, the payment agreement will not be released. An error message will pop up and the payment agreement will remain in processing status.Refer to preliminary step Manage Workflow for Payment Agreement for more information. |  |
| 5 | Maintain Payment Grouping Close Times (Optional) | After a payment agreement is saved, choose Add.In the dialog box appears, enter the following entry and choose Save:Close Time: for example, 09:00:00Note If an entry is maintained for payment grouping, it means payment grouping mechanism is enabled for the payment agreement. Those payment orders applied to the payment rule created later will be collected into one batch, only until the grouping close time has been reached.Note Multiple close time can be added for grouping.Note For internal testing purpose, it is recommended that more conditions are added to restrict the payment rule to some specific OPR Account. | Payment grouping close times are maintained. |  |
| 6 | Create Payment Rule for Payment Agreement | Choose Go and a list of payment agreements is displayed.Choose the payment agreement you created and choose Create Payment Rule for Payment Agreement.On the Payment Rule PF screen, make the following entries and choose Save:Description: for example, Rule for Bank Credit Transfer | A payment rule is created and Manage Payment Agreements is displayed. |  |
| 7 | Create Condition | Choose Go and a list of payment agreements is displayed.Navigate to the payment agreement you created and choose >.On the Payment Rule PF screen, navigate to the payment rule you created and choose >.Choose Edit and choose Create New Condition.Make the following entries and choose Save:Field Name: PI_KINDInclusive/exclusive: IOption: EQValue Low: 01Field Name: DEBCREDInclusive/exclusive: IOption: EQValue Low: DNote It is recommended that the conditions are more specific to determine the right payment rule if there are multiple agreements in one company code. For example, INPUTFOR can be used for a specific format. | Conditions are maintained for the payment rule.A new payment ruleset is automatically created for the payment rule.Note The payment rule is automatically grouped into a payment rule set. The rule set ID is the same as the company code of the payment agreement. |  |
| 8 | Release Payment Ruleset | Go back to the initial screen of Manage Payment Agreements. Choose Go and a list of payment rulesets are displayed under tab Payment Rulesets.Navigate to the payment ruleset and choose >.On the Payment Ruleset screen, choose Edit and Release. | The payment rule set is in Approved status and the payment rules assigned to is now valid. |  |

#### Manage Workflow for Payment Agreement

Use

In this activity, you manage workflows for payment agreement. Before a payment agreement can be created, a related workflow has to be set up.

|  |
| --- |
| Note You can define one dummy workflow to release payment agreements. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Workflows for Payment Agreement. | The Manage Workflows view displays. |  |
| 3 | Create a Dummy Workflow | On the Manage Workflows screen, choose Create.On the New Workflow screen, make the following entries and choose Save:In the Header sectionWorkflow Name: for example, Dummy workflow | The Workflow Details view is displayed. A new workflow is created. |  |
| 4 | Activate Workflow | On the existing Workflow Details screen, choose Activate. | The Manage Workflows screen displays. The new workflow is activated and ready for use. All payment agreements fulfill the condition will be automatically released without approval. |  |
| 5 | Create a Workflow with Condition (Optional) | On the Manage Workflow screen, choose Create.On the New Workflows screen, make the following entries and choose Save:In the Header sectionWorkflow Name: for example, Payment agreement workflowIn the Start Conditions sectionOnly start the workflow if all of the following preconditions are met: for example, Clearing Area and Route IDClearingArea: for example, PFRouteId: for example, 9010In the Steps section, choose Create. | The New Step -- Approval view displays. An approval step sequence is to be maintained. |  |
| 6 | Maintain Step Sequence | On the New Step screen, make the following entries and choose Create.In the Header section:Step Type: ApprovalIn the Recipients section,Assignment By: for example, UserUser: a user with App My Inbox for example, CB9980011105Step to be completed by: for example, One of the recipients | A new Workflow Step is created for a Clearing Agreement Workflow Scenario. |  |
| 7 | Activate Workflow | On the New Workflow screen, choose Save, then choose Activate. | The new workflow is activated and ready for use. All payment agreements fulfill the condition need to be approved before they can be released.Note If there are multiple workflows, the order determines the priority. |  |

#### Set Up Outgoing Payment in Contract Accounting

Use

Currently, Advanced Payment Management supports limited payment media formats. If there is no default setting for a supported format, such as pain.001.001.03, you should set up outgoing payment for payment media formats in this activity. For testing purpose, payment method T is used for DE and I is used for US.

Conduct the following configuration as a Configuration Expert - Business Process Configuration.

1. (Optional) SSCUI 101952 Define Payment Methods.

You define a new payment method and assign the <CC>_CGI_XML_CT format to the payment method (<CC> represents the country code). The payment method needs to be added into the payment method list and an Additional Details entry is necessary for application area Convergent FI-CA.

1. (Optional) SSCUI 101251 Define Specifications for Paying Company Code.

You assign the payment method and the <CC>_CGI_XML_CT format to the company code in which your contact accounting is running.

1. (Optional) SSCUI 102217 Define Accounts for Payment Program.

You maintain the account determination for the new payment method.

1. (Optional) SSCUI 101956 Maintain Bank Selection.

You maintain the ranking order for the new payment method.

1. SSCUI 101276 Define Variants for Payment Medium Program.

You select the checkbox Send Message for the payment format used to integrate Contract Accounting with Multi-Bank Connectivity.

You can check the payment format assigned to the payment method in SSCUI 101952.

#### Manage Teams and Responsibility (Optional)

Use

In this activity, you define who should receive notifications.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Teams and Responsibilities - Asset Management (F4988) and choose Create. | The Manage Teams and Responsibilities view displays. |  |
| 3 | Maintain the Team Details | Make the following entries and choose Create:Name: for example, APM Payment RejectGlobal ID: for example, T_APMType: for example, SAPMIn Team Owners tab, maintain the following entries:Business Partner: <Select Business Partner>In Team Members tab, maintain the following entries:Business Partner: <Select Business Partner who receives notifications>, for example, Payment SpecialistFunctions: Payment Monitoring (S_APMMON_F)In the dialog box, choose Yes to enable the team. | A team is created and enabled. |  |

#### Assign Exception Handling Reaction to Bank Rejection

Use

In this activity, you configure how the system should react if a bank sends a pain.002 status report with a reject status, and also prepare a sample pain.002 file. After the rejection message is received, the outgoing payment order will be set to Manual Repair status for postprocessing. Depending on the different response you selected, the outgoing payment order will either be rejected or reprocessed.

Prerequisites

An outgoing payment order is in approved status.

A pain.002 status report message is created. In a text editor, paste the sample code:

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="UTF-8"?> <!--> Reject of a message, which should lead to a postprocessing -> OrgnlGrpInfAndSts containts the Reject information <!--> <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.03" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <CstmrPmtStsRpt> <GrpHdr> <MsgId>ABC_AR_10232020</MsgId> <CreDtTm>2020-12-03T14:09:00</CreDtTm> <InitgPty> <Nm>CORPORATE NAME</Nm> <PstlAdr> <Dept>FINANCE</Dept> <StrtNm>Dietmar-Hopp-Allee</StrtNm> <BldgNb>1</BldgNb> <PstCd>69190</PstCd> <TwnNm>Walldorf</TwnNm> <Ctry>DE</Ctry> </PstlAdr> <Id> <OrgId> <Othr> <Id>WOWIDESXXX</Id> <SchmeNm> <Cd>BIC</Cd> </SchmeNm> <Issr>SWIFT</Issr> </Othr> </OrgId> </Id> </InitgPty> <DbtrAgt> <FinInstnId> <BIC>DRESDEFF827</BIC> </FinInstnId> </DbtrAgt> </GrpHdr> <OrgnlGrpInfAndSts> <OrgnlMsgId>0000000090011202</OrgnlMsgId> <OrgnlMsgNmId>pain.001.001.03</OrgnlMsgNmId> <OrgnlCreDtTm>2020-12-03T10:07:00</OrgnlCreDtTm> <GrpSts>RJCT</GrpSts> <StsRsnInf> <Rsn> <Cd>AC01</Cd> </Rsn> <AddtlInf>Details about the File reason code</AddtlInf> </StsRsnInf> </OrgnlGrpInfAndSts> </CstmrPmtStsRpt> </Document> |

Save the file to a folder on your PC as pain.002.001.03_AB1234_01.xml.

The sample code is for internal test only. If the file is to be tested more than once, it is recommended that you change the file name, message ID (MsgId) and date slightly for every single test.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution. |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | A list of Configuration Items displays with the filter criteria. |  |
| 5 | Select Advanced Payment Management | Select the following row:Item Name: Advanced Payment Management | The Configuration Your Solution - Advanced Payment Management view displays. |  |
| 6 | Assign Exception Handling Reaction to Bank Reject | From the Configuration Steps area, on the Assign Exception Handling Reaction to Bank Reject step, choose Configure. | The Change View "Assign Exception Handling Reaction to Bank Reject": Overview view displays. |  |
| 7 | Maintain Response Type | Choose New Entries.Make the following entries and choose Save:Clrng Area: PFExternal Status Identifier: RJCTReason Code: for example, AC01Response Type: MANUAL | An exception handling reaction is created.Note Only by assigning response type MANUAL, the payment order can be found and post-processed manually in App Repair Payments.Response type RJC_01 rejects the payment order automatically.Response type Reproc reprocesses the payment order automatically. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Exception Handling Reaction to Bank Reject | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Exception Handling Reaction to Bank Reject.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Assign Exception Handling Reaction to Bank Reject": Overview view displays. |  |
| 3 | Maintain Response Type | Choose New Entries.Make the following entries and choose Save:Clrng Area: PFExternal Status Identifier: RJCTReason Code: for example, AC01Response Type: MANUAL | An exception handling reaction is created.Note Only by assigning response type MANUAL, the payment order can be found and post-processed manually in App Repair Payments.Response type RJC_01 rejects the payment order automatically.Response type Reproc reprocesses the payment order automatically. |  |

#### Define Settings for Forwarding Bank Statements

Use

In a typical two-tier Cash Management scenario, the Cash Management and Financial Accounting are processed in separate landscapes. Bank statements are imported into the Cash Management landscape and update cash flows centrally. After that, bank statements are forwarded to the other landscape for posting. In this scenario, the processes within the central Cash Management landscape are covered in this test script.

In this activity, you configure settings for integrating electronic bank statements with cash management at company code level. No postings are processed, and bank statements will be forwarded to external systems.

You can then retrieve company-level settings in the Define Bank Account Settings - Bank Statements app and make account-specific settings there.

Prerequisites

An exclusive company code for this test procedure is ready.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution. |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items displays with the filter criteria. |  |
| 5 | Select Bank Account Management | Select the following row:Item Name: Bank Account Management | The Configuration Your Solution - Bank Account Payment Management view displays. |  |
| 6 | Define Settings for Bank Statements | From the Configuration Steps area, on the Define Settings for Bank Statements step, choose Configure. | The Change View "Define Settings for Bank Statements: Change": view displays. |  |
| 7 | Maintain Integration Setting | Choose New Entries.Make the following entries and choose Save:Company Code: for example, 1090 for DE, 1790 for USPosting Category (End of Day): No Posting ProcessingTransfer Mode (End of Day): Balance and Bank Statement ItemsPosting Category (Intraday): No Posting ProcessingBank Statement Forwarding: Forwarding |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Settings for Bank Statements | Go to the Business Processes Configuration app and search for the following activity: Define Settings for Bank Statements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View " Define Settings for Bank Statements: Change": Overview view displays. |  |
| 3 | Maintain Integration Setting | Choose New Entries.Make the following entries and choose Save:Company Code: for example, 1090 for DE, 1790 for USPosting Category (End of Day): No Posting ProcessingTransfer Mode (End of Day): Balance and Bank Statement ItemsPosting Category (Intraday): No Posting ProcessingBank Statement Forwarding: Forwarding |  |  |

#### Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages

Use

In this activity, you configure how the receiver IDs used for SAP Multi-Bank Connectivity outbound connector is determined, sender/receiver ID mapping for bank forwarding scenario, the determination of receiver IDs for outbound Multi-Bank Connectivity messages.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution. |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | A list of Configuration Items displays with the filter criteria. |  |
| 5 | Select Advanced Payment Management | Select the following row:Item Name: Advanced Payment Management | The Configuration Your Solution - Advanced Payment Management view displays. |  |
| 6 | Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages | From the Configuration Steps area, on the Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages step, choose Configure. | The Change View “Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages" view displays. |  |
| 7 | Maintain Mapping of Receiver IDs | Choose New Entries.Make the following entries and choose Save:Message Type: STATEMENT_FWDCoCd: 1090 for DE, 1790 for USReceiver ID: SUB4 | A mapping is created. |  |
| 8 | Maintain Multi-Bank Connectivity – Connector Outbound Settings | Exit the step, from the Configuration Steps area, on the Maintain Multi-Bank Connectivity Connector Outbound Settings step, choose Configure. | The Multi-Bank Connectivity – Connector Outbound Settings view displays. |  |
| 9 | Maintain Outbound Setting | Choose New Entries.Make the following entries and choose Save:Note Use the search help of the Format, select converter ID OSTMTF to derive the format, medium, channel and direction.Format: /STMTFWDMedium: /MBCChannel: /SUBDirection: OUTMessage Type: STATEMENT_FWD | The setting is created. |  |
| 10 | Select Multi-Bank Connectivity Connector | Go back to the list of Configuration Items, select the following row:Item Name: Multi-Bank Connectivity Connector | The Configuration Your Solution - Multi-Bank Connectivity Connector view displays. |  |
| 11 | Maintain Sender/Receiver ID Mappings | From the Configuration Steps area, on the Maintain Sender/Receiver ID Mappings step, choose Configure. | The Maintenance of Sender IDs view displays. |  |
| 12 | Maintain Mapping | Choose New Entries.Make the following entries and choose Save:Message Type: STATEMENT_FWDReceiver ID: SUB4Origin: PFSender ID: Payment Factory | A mapping is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Exception Handling Reaction to Bank Reject | Go to the Business Processes Configuration app and search for the following activity: Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages": view displays. |  |
| 3 | Maintain Mapping of Receiver IDs | Choose New Entries.Make the following entries and choose Save:Message Type: STATEMENT_FWDCoCd: 1090 for DE, 1790 for USReceiver ID: SUB4 | A mapping is created. |  |
| 4 | Maintain Multi-Bank Connectivity – Connector Outbound Settings | Go to the Business Processes Configuration app and search for the following activity: Maintain Multi-Bank Connectivity Connector Outbound Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Multi-Bank Connectivity – Connector Outbound Settings view displays. |  |
| 5 | Maintain Outbound Setting | Choose New Entries.Make the following entries and choose Save:Note Use the search help of the Format, select converter ID OSTMTF to derive the format, medium, channel and direction.Format: /STMTFWDMedium: /MBCChannel: /SUBDirection: OUTMessage Type: STATEMENT_FWD | The setting is created. |  |
| 6 | Maintain Sender/Receiver ID Mappings | Go to the Business Processes Configuration app and search for the following activity: Maintain Sender/Receiver ID Mappings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configuration Your Solution - Multi-Bank Connectivity Connector view displays. |  |
| 7 | Maintain Mapping | Choose New Entries.Make the following entries and choose Save:Message Type: STATEMENT_FWDReceiver ID: SUB4Origin: PFSender ID: Payment Factory | A mapping is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Payment Processes for SAP Systems

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
| [Configure Situation Types](#unique_18) [page ] 27 | Business Process Specialist | Manage Situation Types (F2947) | A situation type is created. |
| [Create Payments](#unique_19) [page ] 28 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Pending Approval, the Release Status set to In Approval. |
| [Monitor Batch and Payment](#unique_20) [page ] 28 | Payment Specialist | Manage Payments (F3647) | The name and address of the creditor in Advanced Payment Management payment orders are screened against the sanctioned-party list. |
| [Update of Cash Management](#unique_21) [page ] 30 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | A payment batch is approved. |
| [(Partial) Approval / Reject by Approver](#unique_22) [page ] 30 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Payment Media Created, the Release Status set to Approved. |
| [Rejected Payments](#unique_23) [page ] 31 | Payment Specialist | Repair Payments (F3651) | A payment rejection status report is sent by the bank after payment. The payment order is then sent to postprocessing. Depending on the different options: Resubmit, Reject and Reprocess, the outgoing order is either rejected or reprocessed. |
| [Check Notification](#unique_24) [page ] 31 |  |  |  |
| [Process Payment](#unique_25) [page ] 31 |  |  |  |
| [Accepted Payments](#unique_26) [page ] 32 |  |  |  |
| [Payment Format Management Outbound](#unique_27) [page ] 33 |  |  |  |
| [Send Payment File](#unique_28) [page ] 33 |  |  |  |
| [Payment File Received by Bank](#unique_29) [page ] 34 |  |  |  |
| [Payment Instruction with Accepted Status Sent by Bank](#unique_30) [page ] 34 |  |  |  |
| [Payment Instruction Received](#unique_31) [page ] 34 |  |  |  |
| [Update Payment Management Monitor](#unique_32) [page ] 33 |  |  |  |

Table 2: Payment Processes for non-SAP Systems

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
| [Prepare CSV Payment File](#unique_33) [page ] 34 | Payment Specialist | Create Payments (F3648) | An order is created. |
| [Import CSV Payment File](#unique_34) [page ] 37 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Pending Approval, the Release Status set to In Approval. |
| [Upload Payment File](#unique_35) [page ] 38 | Payment Specialist | Manage Payments (F3647) | The name and address of the creditor in Advanced Payment Management payment orders are screened against the sanctioned-party list. |
| [Monitor Batch and Payment](#unique_36) [page ] 38 |  |  |  |
| [Update of Cash Management](#unique_21) [page ] 30 | Accounts Payable Manager | Manage Your Solution (F1241) | A payment batch is approved. |
| [(Partial) Approval / Reject by Approver](#unique_22) [page ] 30 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Payment Media Created, the Release Status set to Approved. |
| [Rejected Payments](#unique_23) [page ] 31 | Payment Specialist | Repair Payments (F3651) | A payment rejection status report is sent by the bank after payment. The payment order is then sent to postprocessing. Depending on the different options: Resubmit, Reject and Reprocess, the outgoing order is either rejected or reprocessed. |
| [Inform User via Notification](#unique_37) [page ] 40 |  |  |  |
| [Accepted Payments](#unique_26) [page ] 32 |  |  |  |
| [Payment Format Management Outbound](#unique_27) [page ] 33 |  |  |  |
| [Send Payment File](#unique_28) [page ] 33 |  |  |  |
| [Payment File Received by Bank](#unique_29) [page ] 34 |  |  |  |
| [Payment Instruction with Accepted Status Sent by Bank](#unique_30) [page ] 34 |  |  |  |
| [Payment Instruction Received](#unique_31) [page ] 34 |  |  |  |
| [Update Payment Management Monitor](#unique_32) [page ] 33 |  |  |  |

Table 3: Forwarding of Bank Statement

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
| [Import Electronic Bank Statement](#unique_38) [page ] 42 | Payment Specialist | Create Payments (F3648) | An order is created. |
| [Check Upload Results](#unique_39) [page ] 49 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Pending Approval, the Release Status set to In Approval. |
| [Check Cash Update](#unique_40) [page ] 50 | Payment Specialist | Manage Payments (F3647) | The name and address of the creditor in Advanced Payment Management payment orders are screened against the sanctioned-party list. |
| [Check Bank Statement](#unique_41) [page ] 50 |  |  |  |
| [Check Multi-Bank Connectivity Messages](#unique_42) [page ] 50 | Accounts Payable Manager | Manage Your Solution (F1241) | A payment batch is approved. |

Table 4: Watch-List Screening

| Process Step, Report or Item | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
|  |  |  |  |
| [Create Payment](#unique_43) [page ] 51 | Payment Specialist | Create Payments (F3648) | An order is created. |
| [Monitor Payments (Status Before WLS)](#unique_44) [page ] 57 | Payment Specialist | Manage Payments (F3647) | The processing status of the order set to Pending Approval, the Release Status set to In Approval. |
| [Screening of Payment](#unique_45) [page ] 58 | Payment Specialist | Manage Payments (F3647) | The name and address of the creditor in Advanced Payment Management payment orders are screened against the sanctioned-party list. |
| [Monitor Payments (Status After WLS)](#unique_46) [page ] 59 |  |  |  |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Payment Processes for SAP Systems

Purpose

Advanced Payment Management supports XML ISO 20022 format for payments integrated with Contract Accounting – Company Initiated Payments ([2DP](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/2DP)).

Prerequisite

The preliminary step [Maintain Routing Settings (Optional)](#unique_8) [page ] 7 and [Set Up Outgoing Payment in Contract Accounting](#unique_12) [page ] 14 are conducted for payments originated from FICA.

#### Configure Situation Types

Use

In this activity, you configure the situation type by using a template. Situation types help you manage a large variety of circumstances that are critical to your business processes by automatically notifying the right users as soon as the situations occur.

There are situation templates available for Advanced Payment Management:

- Payment rejected: This situation is triggered when a pain.002 status report with reject of file or batch is received via Multi-Bank Connectivity (The test step Pull Status Message from MBC (Optional) is described in Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)) ).
- Payment in status Manual Postprocessing: This situation is triggered when an outgoing payment order is rejected and needs manual repair as per settings of bank rejection exception handling reaction. Refer to preliminary step Assign Exception Handling Reaction to Bank Rejection for the setting and test step Postprocess Payment Orders (Optional) for the follow-up process.

You can use the above described situations as templates.

|  |
| --- |
| Note Please make sure 31N is activated if you want to execute this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access App | Open Manage Situation Types (F2947). | The Manage Situation Types view displays. |  |
| 3 | Select the Template to Copy | Choose Go.Search and select Template FIN_APM_PAYMENT_REJECT, then choose Copy. | The Situation Type view displays. |  |
| 4 | Maintain the Situation Type | Make the following entries and choose Save:ID: for example, ZFIN_APM_PAYMENT_REJECTName: for example, Payment RejectOn the Recipients tab, maintain the following entries:Team Category: BCMMember Function: Payment Monitoring | A situation type is maintained. |  |
| 5 | Enable the Situation Type | In the Situation Type view, choose Enable. | The status of the situation type is changed to Enabled. |  |
| 6 | Create Situation Types | Repeat step 3-5 to create situation type based from following situation template:FIN_APM_PAYMENT_REPAIR | Situation type ZFIN_APM_PAYMENT_REPAIR is created. |  |

#### Create Payments

Purpose

After payment run is conducted in 2DP, the payment media file is routed to Advanced Payment Management via Multi-Bank Connectivity automatically.

|  |
| --- |
| Note To integrate the payment with Advanced Payment Management, the user who runs the payment run must have the SAP_BR_PAYMENT_SPECIALIST role. |

#### Monitor Batch and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a payment message is routed by Multi-Bank Connectivity to Advanced Payment Management, an inbound payment order with one originator item and several recipient items is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Incoming Payment Orders | On the entry screen of the Manage Payments (F3647) app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. The processing status of the new incoming order should be Inbound Processing Completed (128). An outgoing order is created.A memo record is created in Cash Management of active status. The absolute value of the amount in memo record equals the one in the payment order.Note Navigating to the memo record in Cash Management is supported by clicking the memo record.Note The detailed test step is described in test step Memo Record List of BFB Basic Cash Operations. |  |
| 4 | Display Incoming Payment Order | Choose one incoming payment order, for example 10.02.2020/000000001002. | The detail screen of the Incoming Payment Order is displayed. |  |
| 5 | Navigate to Outgoing Payment Order | Choose the output order on the tab of ORIGINATOR, for example 10.02.2020/000000003001.Note Down the BCM Batch ID, for example, 10300 | The detail screen of the Outgoing Payment Order is displayed. The processing status of the order should be Pending Approval, the Release Status should be In Approval. |  |

#### Update of Cash Management

Purpose

Integrated with Cash Management, payment orders can generate memo records to reflect the cash flow changes. Check the cash flows directly in respective Cash Management app or navigate by clicking the memo record within the payment order.

The detailed test step is described in test step Memo Record List of Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)) in previous test procedure.

#### (Partial) Approval / Reject by Approver

Purpose

A payment batch is to be approved or rejected.

|  |
| --- |
| Note The approval of a payment batch is enabled in Bank Communication Management. The batch of an outgoing payment approval is described in step Approval and Bank Integration in test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78)).Depending on the automatic approval/rejection settings, a batch can be automatically approved or rejected if there is no approvers/ approval pattern maintained. More detailed information is described in Preliminary Step Define Automatic Approval/Rejection for Bank Account Master Data. |

|  |
| --- |
| Note The approvers and approval pattern are determined in Bank Account Management. The approvers can be maintained individually in each bank account or collectively for multiple bank accounts.Depending on the bank account revision setting, the test step for multiple bank accounts is described in step Maintain Payment Approver for Multiple Bank Accounts (Direct Revision Activate), Maintain Payment Approver for Multiple Bank Accounts (Dual Control Revision Activate) and Maintain Payment Approver for Multiple Bank Accounts (Workflow Revision Activate) in test script Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)). |

|  |
| --- |
| Note Partial approval is not possible in case the the convertor is defined as “Forwarding the entire Incoming Order (B)”. |

|  |
| --- |
| Note To approve the APM payment batch, payment specialist role must be assigned to the final approver, otherwise the approval will fail with error message. Refer to the [Roles](#unique_4) [page ] 4 to find the payment specialist role. |

#### Rejected Payments

Purpose

The payment batch is rejected by one of the approvers. The test procedures from Check Notification to Process Payment are for processing rejected payments.

#### Check Notification

Purpose

This process step shows you how notifications for rejected payments send to the selected responsible team member. The detection process is automatically triggered by the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Check Notifications | On the home screen, choose the Notification icon in the upper right corner. | The payment reject notification is listed. |  |

#### Process Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A payment rejection status report is sent by the bank after payment. The payment order is then sent to postprocessing. Depending on the different options: Reject and Reprocess, the outgoing order is either rejected or reprocessed.

|  |
| --- |
| Note The optional status report is described in step Pull Status Message from MBC (Optional) in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)). |

Prerequisites

Preliminary step Assign External Reaction to Bank Rejection is configured.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Repair Payments (F3651). |  |  |
| 3 | Start Selection for Outgoing Payment Orders | On the entry screen of the app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. |  |
| 4 | Postprocess the Outgoing Payment Order | On the right section of the payment order to be postprocessed, choose >.Note The order will be automatically reserved by the user after navigating to the details of the order. The reserved status can also be manually reserved by choosing Set Reservation and can be removed by choosing Remove Reservation. | The detail screen of the Outgoing Payment Order is displayed. |  |
| 5 | Reject the Order (Optional) | In the detail view, choose Reject.In the dialog box, make the following entries and choose Reject.Response Type: REJ_01 | The status of the order will be Rejected and the amount of the memo record created in Cash Management will be zero. |  |
| 6 | Reprocess the Order (Optional) | In the detail view, choose Process. | The status of the order will be Payment Media Created. The order will be resubmitted and a new MBC message will be created. |  |

#### Accepted Payments

Purpose

The payment batch is accepted by all the approvers. The test procedures from [Payment Format Management Outbound](#unique_27) [page ] 33 to [Update Payment Management Monitor](#unique_32) [page ] 33 are for processing accepted payments.

#### Payment Format Management Outbound

Purpose

This step is automatically conducted after the payment batch is approved. A payment media file will be created and sent to Multi-Bank Connectivity.

#### Update Payment Management Monitor

Purpose

Once the payment batch is approved, the outgoing payment order is also approved. A payment message will be sent to Multi-Bank Connectivity only after the order is processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Outgoing Payment Orders | On the entry screen of the app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. |  |
| 4 | Display Outgoing Payment Order | Choose the outgoing payment order, for example 10.02.2020/000000003001. | The detail screen of the Outgoing Payment Order is displayed.The processing status of the order should be Payment Media Created. The Release Status should be Approved. |  |

#### Send Payment File

Purpose

This step is automatically conducted by Multi-Bank Connectivity outside S/4HANA system. The payment media file is sent to the bank.

#### Payment File Received by Bank

Purpose

This step is conducted by the bank outside S/4HANA system. The bank receives the payment media file successfully.

#### Payment Instruction with Accepted Status Sent by Bank

Purpose

This step is conducted by the bank outside S/4HANA system. The bank validates and accepts the payment media file by sending back a payment instruction with accepted status.

#### Payment Instruction Received

Purpose

This step is automatically conducted by Multi-Bank Connectivity and described in Pull Status Message from MBC (Optional) in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)).

### Payment Processes for non-SAP Systems

Purpose

Advanced Payment Management supports files, such as CSV/TXT, for payments initiated by non-SAP systems.

#### Prepare CSV Payment File

Purpose

Advanced Payment Management supports files, such as CSV/TXT, for payments initiated by non-SAP systems.

Prerequisites

Download a copy of the payment file template [https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/IFME_TESTFILE_P1.xlsx](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/General/IFME_TESTFILE_P1.xlsx).

|  |
| --- |
| Note For testing purpose, two payments are prepared. Delete the entries which are not applicable. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Modify the Payer Information | Open the payment file template and make the following entries for payer:ID: <unique ID of the payment>, for example, File1 for DE or File 2 for USCountry: <the country code of the payer bank account>, for example, DE or USBank key: <the bank key of the payer bank account>, for example, 82080000 for DE or 820800001 for USBIC: <the bank BIC code of the payer bank account>, for example, DRESDEFF827 for DE or CITIUS33MIA for USAccount: <the bank account number of the payer>, for example, 2580061 for DE or 2580611 for US |  |  |
| 2 | Modify the Payee Information | Make the following entries for payer and save the change:ID: <unique ID of the payment item>, for example, TX1 for line item 1Country: <the country code of the payee bank account>, for example, DE or USBank key: <the bank key of the payee bank account>, for example, 82080000 for DE or 820800001 for USBIC: <the bank BIC code of the payee bank account>, for example, DRESDEFF827 for DE or CITIUS33MIA for USAccount: <the bank account number of the payee>, for example, 1234567899Amount: for example, 10Currency: for example, EUR for DE or USD for USReferenceID: for example, E2E-TX1-10€ for DE or E2E-TX1-10$ for USPayment Note: for example, Invoice 12345-1-20Note If there are multiple recipients, the respective payee information is maintained in respective rows. | The change is successfully saved. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | Access App | Open Manage Your Solution (F1241). |  |  |
| 5 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 6 | Filter List | Application Area: FinanceSub Application Area: Payments and Bank Communications | A list of Configuration Items displays with the filter criteria. |  |
| 7 | Select Payment Medium Formats | Item Name: Advanced Payment Management | The Configuration Your Solution – Advanced Payment Management view displays. |  |
| 8 | Check Payment Format Data | From the Configuration Steps area, on the Map Format Data for Advanced Payment Management step, choose Configure. | The Map Format Data view displays. |  |
| 9 | Check Format Mapping Detail | From the Incoming tab, Format Mappings area, choose >on the row of format to check, for example SAP_APM_DEMO_CSV_CT.Note down the Field Delimiter in the Attributes area of header node Format Mapping Properties. |  |  |
| 10 | Save as csv File | Save the payment file as a csv file and make sure the delimiter is the same as the delimiter defined for the message type. If the delimiter is not the same, you can edit the csv file in a file editor and replace the delimiter. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Modify the Payer Information | Open the payment file template and make the following entries for payer:ID: <unique ID of the payment>, for example, File1 for DE or File 2 for USCountry: <the country code of the payer bank account>, for example, DE or USBank key: <the bank key of the payer bank account>, for example, 82080000 for DE or 820800001 for USBIC: <the bank BIC code of the payer bank account>, for example, DRESDEFF827 for DE or CITIUS33MIA for USAccount: <the bank account number of the payer>, for example, 2580061 for DE or 2580611 for US |  |  |
| 2 | Modify the Payee Information | Make the following entries for payer and save the change:ID: <unique ID of the payment item>, for example, TX1 for line item 1Country: <the country code of the payee bank account>, for example, DE or USBank key: <the bank key of the payee bank account>, for example, 82080000 for DE or 820800001 for USBIC: <the bank BIC code of the payee bank account>, for example, DRESDEFF827 for DE or CITIUS33MIA for USAccount: <the bank account number of the payee>, for example, 1234567899Amount: for example, 10Currency: for example, EUR for DE or USD for USReferenceID: for example, E2E-TX1-10€ for DE or E2E-TX1-10$ for USPayment Note: for example, Invoice 12345-1-20Note If there are multiple recipients, the respective payee information is maintained in respective rows. | The change is successfully saved. |  |
| 3 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 4 | Open Map Payment Format Data | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Map Format Data for Advanced Payment Management.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Map Payment Format Data screen displays. |  |
| 5 | Check Format Mapping Detail | From the Incoming tab, Format Mappings area, choose > on the row of format to check, for example SAP_APM_DEMO_CSV_CT.Note down the Field Delimiter in the Attributes area of header node Format Mapping Properties. |  |  |
| 6 | Save as csv File | Save the payment file as a csv file and make sure the delimiter is the same as the delimiter defined for the message type. If the delimiter is not the same, you can edit the csv file in a file editor and replace the delimiter. |  |  |

#### Import CSV Payment File

Purpose

This step is automatically conducted by Multi-Bank Connectivity and described in Route Payment Files Initiated by non-SAP Systems in test script Bank Integration with Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)).

#### Upload Payment File

Purpose

For non-SAP initiated payments, the payment files are automatically routed to Advanced Payment Management in backend via Multi-Bank Connectivity.

#### Monitor Batch and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a payment message is routed by Multi-Bank Connectivity to Advanced Payment Management, an inbound payment order with one originator item and several recipient items is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Incoming Payment Orders | On the entry screen of the Manage Payments (F3647) app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. The processing status of the new incoming order should be Inbound Processing Completed (128). An outgoing order is created.A memo record is created in Cash Management of active status. The absolute value of the amount in memo record equals the one in the payment order.Note Navigating to the memo record in Cash Management is supported by clicking the memo record.Note The detailed test step is described in test step Memo Record List of BFB Basic Cash Operations. |  |
| 4 | Display Incoming Payment Order | Choose one incoming payment order, for example 10.02.2020/000000001002. | The detail screen of the Incoming Payment Order is displayed. |  |
| 5 | Navigate to Outgoing Payment Order | Choose the output order on the tab of ORIGINATOR, for example 10.02.2020/000000003001.Note Down the BCM Batch ID, for example, 10300 | The detail screen of the Outgoing Payment Order is displayed. The paying account used is supposed to be without payment approvers maintained. If the processing status of the order is Pending Approval and the Release Status is In Approval, manual approval is expected. For more details, refer to Approval and Bank Integration in test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78)). |  |

#### Update of Cash Management

Purpose

Integrated with Cash Management, payment orders can generate memo records to reflect the cash flow changes. Check the cash flows directly in respective Cash Management app or navigate by clicking the memo record within the payment order.

The detailed test step is described in test step Memo Record List of Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)) in previous test procedure.

#### (Partial) Approval / Reject by Approver

Purpose

A payment batch is to be approved or rejected.

|  |
| --- |
| Note The approval of a payment batch is enabled in Bank Communication Management. The batch of an outgoing payment approval is described in step Approval and Bank Integration in test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78)).Depending on the automatic approval/rejection settings, a batch can be automatically approved or rejected if there is no approvers/ approval pattern maintained. More detailed information is described in Preliminary Step Define Automatic Approval/Rejection for Bank Account Master Data. |

|  |
| --- |
| Note The approvers and approval pattern are determined in Bank Account Management. The approvers can be maintained individually in each bank account or collectively for multiple bank accounts.Depending on the bank account revision setting, the test step for multiple bank accounts is described in step Maintain Payment Approver for Multiple Bank Accounts (Direct Revision Activate), Maintain Payment Approver for Multiple Bank Accounts (Dual Control Revision Activate) and Maintain Payment Approver for Multiple Bank Accounts (Workflow Revision Activate) in test script Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)). |

|  |
| --- |
| Note Partial approval is not possible in case the the convertor is defined as “Forwarding the entire Incoming Order (B)”. |

|  |
| --- |
| Note To approve the APM payment batch, payment specialist role must be assigned to the final approver, otherwise the approval will fail with error message. Refer to the [Roles](#unique_4) [page ] 4 to find the payment specialist role. |

#### Rejected Payments

Purpose

The payment batch is rejected by one of the approvers. The test procedures from Check Notification to Process Payment are for processing rejected payments.

#### Inform User via Notification

Purpose

This process step is conducted offline once the payment is rejected.

#### Accepted Payments

Purpose

The payment batch is accepted by all the approvers. The test procedures from [Payment Format Management Outbound](#unique_27) [page ] 33 to [Update Payment Management Monitor](#unique_32) [page ] 33 are for processing accepted payments.

#### Payment Format Management Outbound

Purpose

This step is automatically conducted after the payment batch is approved. A payment media file will be created and sent to Multi-Bank Connectivity.

#### Update Payment Management Monitor

Purpose

Once the payment batch is approved, the outgoing payment order is also approved. A payment message will be sent to Multi-Bank Connectivity only after the order is processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Outgoing Payment Orders | On the entry screen of the app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. |  |
| 4 | Display Outgoing Payment Order | Choose the outgoing payment order, for example 10.02.2020/000000003001. | The detail screen of the Outgoing Payment Order is displayed.The processing status of the order should be Payment Media Created. The Release Status should be Approved. |  |

#### Send Payment File

Purpose

This step is automatically conducted by Multi-Bank Connectivity outside S/4HANA system. The payment media file is sent to the bank.

#### Payment File Received by Bank

Purpose

This step is conducted by the bank outside S/4HANA system. The bank receives the payment media file successfully.

#### Payment Instruction with Accepted Status Sent by Bank

Purpose

This step is conducted by the bank outside S/4HANA system. The bank validates and accepts the payment media file by sending back a payment instruction with accepted status.

#### Payment Instruction Received

Purpose

This step is automatically conducted by Multi-Bank Connectivity and described in Pull Status Message from MBC (Optional) in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)).

### Forwarding of Bank Statement

Purpose

In this scenario, the Cash Management and Financial Accounting can be processed in separate landscapes. In some cases, bank statements are imported into the Cash Management landscape and update cash flows centrally. After that, bank statements are forwarded to the other landscape for posting. The processes within the central Cash Management landscape are covered in this test script.

#### Import Electronic Bank Statement

Use

In this activity, you configure settings for integrating electronic bank statements with cash management at company code level. No postings are processed, and bank statements will be forwarded to external systems.

You can then retrieve company-level settings in the  Define Bank Account Settings - Bank Statements (F5488) app and make account-specific settings there.

Prerequisites

An exclusive bank account is ready for this test procedure. In this test case, bank account 4711 is created in company code 1790 for US. Open a house bank 1790 USBK9 with bank key CHASUS33XXX, and use house bank account ID USAC9 for the bank account 4711. You can refer to create bank account section in test script Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)).

|  |
| --- |
| Note Customer Number must be maintained as the Sender ID Payment Factory. For more details, refer to Preliminary Step [Determine Receiver IDs for Outbound Multi-Bank Connectivity Messages](#unique_16) [page ] 19. |

A camt.053 electronic bank statement file is created. In a text editor, paste the sample code:

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="utf-8"?> <Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.02"> <BkToCstmrStmt> <GrpHdr> <MsgId>2023042000000001</MsgId> <CreDtTm>2023-04-20T16:47:47</CreDtTm> <MsgPgntn> <PgNb>1</PgNb> <LastPgInd>true</LastPgInd> </MsgPgntn> </GrpHdr> <Stmt> <Id>CAMSLINK01000249</Id> <ElctrncSeqNb>00001</ElctrncSeqNb> <CreDtTm>2023-04-20T00:00:00</CreDtTm> <Acct> <Id> <Othr> <Id>4711</Id> </Othr> </Id> <Svcr> <FinInstnId> <BIC>CHASUS33XXX</BIC> </FinInstnId> </Svcr> </Acct> <Bal> <Tp> <CdOrPrtry> <Cd>PRCD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="USD">0.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2023-04-20</Dt> </Dt> </Bal> <Bal> <Tp> <CdOrPrtry> <Cd>CLBD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="USD">30900.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2023-04-20</Dt> </Dt> </Bal> <TxsSummry> <TtlNtries> <NbOfNtries>4</NbOfNtries> <Sum>30900.00</Sum> <TtlNetNtryAmt>30900.00</TtlNetNtryAmt> <CdtDbtInd>CRDT</CdtDbtInd> </TtlNtries> </TxsSummry> <Ntry> <Amt Ccy="USD">900.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2023-04-20</Dt> </BookgDt> <ValDt> <Dt>2023-04-20</Dt> </ValDt> <AcctSvcrRef>2010AEF-4CA3-1EED-ADEF-E6315F0B9FDE</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>051</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>0815</ChqNb> </Refs> <AmtDtls> <TxAmt> <Amt Ccy="USD">900.00</Amt> </TxAmt> </AmtDtls> <RltdPties> <Dbtr> <Nm>X</Nm> </Dbtr> <DbtrAcct> <Id> <Othr> <Id>DEBTACCT123</Id> </Othr> </Id> </DbtrAcct> </RltdPties> <RltdAgts> <DbtrAgt> <FinInstnId> <Othr> <Id>DEUBAXXX</Id> </Othr> </FinInstnId> </DbtrAgt> </RltdAgts> <AddtlTxInf>4711</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>4711</AddtlNtryInf> </Ntry> <Ntry> <Amt Ccy="USD">3000.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2023-04-20</Dt> </BookgDt> <ValDt> <Dt>2023-04-20</Dt> </ValDt> <AcctSvcrRef>2010AEF-4CA3-1EED-ADEF-E6315F0B9FDE</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>051</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>0815</ChqNb> </Refs> <AmtDtls> <TxAmt> <Amt Ccy="USD">3000.00</Amt> </TxAmt> </AmtDtls> <RltdPties> <Dbtr> <Nm>X</Nm> </Dbtr> <DbtrAcct> <Id> <Othr> <Id>DEBTACCT456</Id> </Othr> </Id> </DbtrAcct> </RltdPties> <RltdAgts> <DbtrAgt> <FinInstnId> <Othr> <Id>DEUBAXXX</Id> </Othr> </FinInstnId> </DbtrAgt> </RltdAgts> <AddtlTxInf>Test3535</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>Test3434</AddtlNtryInf> </Ntry> <Ntry> <Amt Ccy="USD">25000.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2023-04-20</Dt> </BookgDt> <ValDt> <Dt>2023-04-20</Dt> </ValDt> <AcctSvcrRef>2010AEF-4CA3-1EED-ADEF-E6315F0B9FDE</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>051</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>0815</ChqNb> </Refs> <AmtDtls> <TxAmt> <Amt Ccy="USD">25000.00</Amt> </TxAmt> </AmtDtls> <RltdPties> <Dbtr> <Nm>X</Nm> </Dbtr> <DbtrAcct> <Id> <Othr> <Id>DEBTACCT123</Id> </Othr> </Id> </DbtrAcct> </RltdPties> <RltdAgts> <DbtrAgt> <FinInstnId> <Othr> <Id>DEUBAXXX</Id> </Othr> </FinInstnId> </DbtrAgt> </RltdAgts> <AddtlTxInf>Test35599</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>Test9999</AddtlNtryInf> </Ntry> <Ntry> <Amt Ccy="USD">2000.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2023-04-20</Dt> </BookgDt> <ValDt> <Dt>2023-04-20</Dt> </ValDt> <AcctSvcrRef>2010AEF-4CA3-1EED-ADEF-E6315F0B9FDE</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>051</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>0815</ChqNb> </Refs> <AmtDtls> <TxAmt> <Amt Ccy="USD">2000.00</Amt> </TxAmt> </AmtDtls> <RltdPties> <Dbtr> <Nm>X</Nm> </Dbtr> <DbtrAcct> <Id> <Othr> <Id>DEBTACCT456</Id> </Othr> </Id> </DbtrAcct> </RltdPties> <RltdAgts> <DbtrAgt> <FinInstnId> <Othr> <Id>DEUBAXXX</Id> </Othr> </FinInstnId> </DbtrAgt> </RltdAgts> <AddtlTxInf>Test3535</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>Test3434</AddtlNtryInf> </Ntry> <AddtlStmtInf>Unittest</AddtlStmtInf> </Stmt> </BkToCstmrStmt> </Document> |

Save the file to a folder on your PC as camt.053_forwarding_AB1234_01.xml.

The sample code is for internal test only. If the file is to be tested more than once, it is recommended that you change the file name, sequential number of the statement (ElctrncSeqNb), message ID (MsgId) and date slightly for every single test.

The user to import the bank statement is described in the test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)). To support the bank statement forward, the user must have the additional user role SAP_BR_PAYMENT_SPECIALIST assigned.

Procedure

This step is described in step Pull Status Message from MBC of test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)). For testing purpose, the manual upload is described in step camt.053 in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)).

#### Check Upload Results

Use

After the bank statement is uploaded, you can check the status of the bank statement imported.

Procedure

Check the result in step camt.053 in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1EG)).

#### Check Cash Update

Use

After the bank statement is uploaded, the corresponding cash flows are generated.

Procedure

Check the cash flow items described in step Check Cash Flow Items in test script Advanced Cash Operation ([J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78)).

#### Check Bank Statement

Use

After the bank statement is uploaded, you can also find the bank statement information centrally.

Procedure

Check the bank statement in Fiori App Manage Bank Statements (F1564). For more details, you can refer to step Bank Statement in test script Basic Cash Operations ([BFB](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/BFB)).

#### Check Multi-Bank Connectivity Messages

Use

After the bank statement is forwarded, a Multi-Bank Connectivity message will be generated.

Procedure

Check the Multi-Bank Connectivity message described in step MBC Message Monitor in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/16R)).

### Watch-List Screening

Purpose

With SAP Watch List Screening, the name and address of the creditor in Advanced Payment Management payment orders can be screened against the sanctioned-party list.

Prerequisite

An additional license is needed for Watch List Screening. Advanced Payment Management can only be integrated with Watch List Screening after the set-up of the service and the related integration scenario. For more information, refer to the 4MT set-up instructions.

#### Create Payment

Use

In this activity, you prepare a payment media file for Watch List Screening.

|  |
| --- |
| Note The file is required for internal test purpose to simulate the business process. |

Procedure

In a text editor, paste the following sample code:

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="UTF-8"?> <!--> Used for Watch List Screening -> Receiver should be found, but later in a subsequent step be identified as a false positive <!--> <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.003.03" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <CstmrCdtTrfInitn> <GrpHdr> <MsgId>0000990101</MsgId> <CreDtTm>2020-08-27T07:13:50</CreDtTm> <NbOfTxs>2</NbOfTxs> <CtrlSum>120.00</CtrlSum> <InitgPty> <Nm>Company Code 1010</Nm> </InitgPty> </GrpHdr> <PmtInf> <PmtInfId>0000000101-000001</PmtInfId> <PmtMtd>TRF</PmtMtd> <BtchBookg>true</BtchBookg> <NbOfTxs>2</NbOfTxs> <CtrlSum>120.00</CtrlSum> <PmtTpInf> <SvcLvl> <Cd>SEPA</Cd> </SvcLvl> </PmtTpInf> <ReqdExctnDt>2020-08-27</ReqdExctnDt> <Dbtr> <Nm>Company Code 1010</Nm> <PstlAdr> <Ctry>DE</Ctry> <AdrLine>Walldorf</AdrLine> </PstlAdr> </Dbtr> <DbtrAcct> <Id> <IBAN>DE28820800000258006100</IBAN> </Id> </DbtrAcct> <DbtrAgt> <FinInstnId> <BIC>DRESDEFF827</BIC> </FinInstnId> </DbtrAgt> <ChrgBr>SLEV</ChrgBr> <CdtTrfTxInf> <PmtId> <InstrId>02-910000000010</InstrId> <EndToEndId>B910000000010</EndToEndId> </PmtId> <Amt> <InstdAmt Ccy="EUR">100.00</InstdAmt> </Amt> <CdtrAgt> <FinInstnId> <BIC>DEUTDE5M</BIC> </FinInstnId> </CdtrAgt> <Cdtr> <Nm>Obiedinennaya Promyshlennaya</Nm> <PstlAdr> <Ctry>RU</Ctry> <AdrLine>Main Street 10</AdrLine> <AdrLine>12345 Moscow</AdrLine> </PstlAdr> </Cdtr> <CdtrAcct> <Id> <IBAN>DE32100200300234556777</IBAN> </Id> </CdtrAcct> <RmtInf> <Ustrd>ACCAPM01</Ustrd> </RmtInf> </CdtTrfTxInf> <CdtTrfTxInf> <PmtId> <InstrId>02-910000000011</InstrId> <EndToEndId>B910000000011</EndToEndId> </PmtId> <Amt> <InstdAmt Ccy="EUR">20.00</InstdAmt> </Amt> <CdtrAgt> <FinInstnId> <BIC>DEUTDE5M</BIC> </FinInstnId> </CdtrAgt> <Cdtr> <Nm>Herbert APM2</Nm> <PstlAdr> <Ctry>DE</Ctry> <AdrLine>Churchstreet 1</AdrLine> <AdrLine>23456 Hannover</AdrLine> </PstlAdr> </Cdtr> <CdtrAcct> <Id> <IBAN>DE48100200300567899123</IBAN> </Id> </CdtrAcct> <RmtInf> <Ustrd>ACCAPM02</Ustrd> </RmtInf> </CdtTrfTxInf> </PmtInf> </CstmrCdtTrfInitn> </Document> |

Save the file to a folder on your PC as pain.001.003.03_AB1234_01.xml.

|  |
| --- |
| Note The sample code is for internal test only. If the file is to be tested more than once, it is recommended that you change the file name, message ID (MsgId) and amount slightly. ReqdExctnDt is the due date of the payment. Always change the date to today's date or a date later than today. Otherwise, the payment order will be automatically rejected or in repair status depending on the setting. |

|  |
| --- |
| Note If the name that is screened in watch list screening does not create a hit in below test step Screening of Payment, you can change the first creditor’s information to one of the following name and address in the list.The list is only for internal test purpose. Check with the watch list provider for the list. |

| Name | City | Street | Zip Code | Country |
| --- | --- | --- | --- | --- |
| PSA Holdings LLC | Miami | 80 SW 8th Street Suite 2000 | 33130 | USA |
| Obiedinennaya Promyshlennaya Korporatsiya Oboronprom OAO | Moscow | Str. 141 29 m Vereiskaya ul. | 121357 | Russia |
| Stroytransgaz Holding | Nicosia |  |  | Cyprus |
| Fleurette Holdings Netherlands B.V. |  | Industrieweg 5 Nieuwkoop 2421 LK Zuid-Holland |  | Netherlands |
| Technology and Development Group Ltd | London | Centric House 390/391 Strand |  | United Kingdom |
| Red Sea Barakat Company Limited | Dubai |  |  | UAE |
| Barako Trading Company LLC | Dubai |  |  | UAE |
| Benevolence International Foundation | Oak Lawn | 8820 Mobile Avenue, 1A | 60453 | USA |
| Rabita Trust | Lahore | Wares Colony |  | Pakistan |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist with the additional role SAP_BR_CASH_SPECIALIST.Note You can assign business roles to business user in Fiori App Maintain Business User. The role for Cash Specialist is SAP_BR_CASH_SPECIALIST and the role for Payment Specialist is SAP_BR_PAYMENT_SPECIALIST. |  |  |
| 2 | Access App | Open Manage Incoming Payment Files (F1680). |  |  |
| 3 | Import File | Choose Import. | A dialog for import is displayed. |  |
| 4 | Import Payment File for Advanced Payment Management | Choose Payment File for Advanced Payment Management. | A dialog for importing Advanced Payment Management payment files is displayed. |  |
| 5 | Upload File | Choose Add to upload the sample ISO XML payment file from your local PC and make following entries:Converter ID: ISO Inbound MBCChoose Process.Check the log of the import file. You will find a log saying Object list MM/DD/YYYY/ XXXXXXXXXXX created in advanced payment management. Note down the incoming payment order number for example 06/07/2022 / 000000007002, for the test step Approve Payment Batch File. | The file is successfully uploaded and an incoming payment order is created. |  |

#### Monitor Payments (Status Before WLS)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the payments that have not yet been processed by Watch List Screening.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Incoming Payment Orders | On the entry screen of the Manage Payments app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. The processing status of the new incoming order should be Inbound Processing Completed (128). An outgoing order is created. |  |
| 4 | Display Incoming Payment Order | Choose one incoming payment order, for example 20.08.2020/000000001002. | The detail screen of the Incoming Payment Order is displayed. |  |
| 5 | Navigate to Outgoing Payment Order | Choose the output order on the tab of ORIGINATOR, for example 20.08.2020/000000003001.Note down the BCM Batch ID, for example, 10300 | The detail screen of the Outgoing Payment Order is displayed. The processing status of the order should be Resubmission. |  |

#### Screening of Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the name and address of the creditor in Advanced Payment Management payment orders are screened against the sanctioned-party list, and the Compliance Specialist decides whether the information hits the list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Compliance Specialist - Screening (GRC) role. |  |  |
| 2 | Access App | Choose Process Address Screening Hits.To make this Screening Hits app available in S/4HANA Fiori Launchpad, please refer SAP Watch List Screening Onboarding section in set-up instruction for this scope item to create the corresponding custom tile in S/4HANA Fiori Launchpad.The Screening Hits app will not be available in internal validation system, but it will be available in productive system. | The Process Address Screening Hits screen displays. |  |
| 3 | Display the Hits Item | Make the following entries and choose Enter:Status: OpenCreated On: for example, Today | A list of hits is displayed. |  |
| 4 | Select the Hits Item | Select the hits item caught by Watch List Screening, choose >. | The Screening Hits screen displays and possible hits items are listed. |  |
| 5 | Submit the Decision | Check the list of the hits, choose YES or NO for each hit item and choose Submit. | After screening, the decision is made on whether the payment hits the list. |  |

#### Monitor Payments (Status After WLS)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the payments that have been processed by Watch List Screening.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Start Selection for Incoming Payment Orders | On the entry screen of the Manage Payments app, make the following entries and choose Go:Clearing Area: Payment Factory Default ConfigurationCreated On: for example, Today | A list of orders is displayed. The processing status of the new incoming order should be Inbound Processing Completed (128). An outgoing order is created. |  |
| 4 | Display Incoming Payment Order | Choose one incoming payment order, for example 20.08.2020/000000001002. | The detail screen of the Incoming Payment Order is displayed. |  |
| 5 | Navigate to Outgoing Payment Order | Choose the output order on the tab of ORIGINATOR, for example 20.08.2020/000000003001.Note down the BCM Batch ID, for example, 10300 | The detail screen of the Outgoing Payment Order is displayed.Depending on the check decision made, the outgoing order will be set to different status as following:False positive hit: all the hits are set as NO. A regular job is scheduled for resubmission. The status of the order will be changed to Pending Approval.Positive hit:If there is only one recipient item hits ( the hits item is set as YES) in the outgoing order, both status of the item and the outgoing payment order will be changed to Rejected.If there is more than one recipient item in the outgoing order and not all the recipient item hits, the status of the item will be changed to Rejected, and the status of the order will be changed to Pending Approval. |  |

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
> Flagged while digesting this document, not verified: The Purpose note says 2DP Contract Accounting integration supports DE but not US, yet 'Set Up Outgoing Payment in Contract Accounting' states payment method I is used for US for testing.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The automatic-reject response type is called RJC_01 in the Assign Exception Handling Reaction note but REJ_01 in the Process Payment test step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-basic-payment-management-7mj-1221]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4MT_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 98,433 chars in the whole document
