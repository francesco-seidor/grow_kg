---
id: 05-treasury-and-cash-management/test-script-treasury-workstation-cash-integration-34p-ae-sap-s-4hana-c
title: "Test Script: Treasury Workstation Cash Integration (34P_AE) - SAP S/4HANA Cloud Public Edition (34P_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (34P_AE) for replicating house banks, bank accounts and cash flows from subsidiary systems to a central treasury workstation."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-accounting-integration]
aliases: [34P_S4CLD2608_BPD_EN_AE]
keywords: [Treasury Workstation Accounting Integration, treasury workstation integration, cash flow replication, cash flow replication jobs, house bank replication, bank account replication, replication filter criteria, cash flow reconciliation, remote cash flow retrieval, cash flow release]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34P_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-916
topic: 05-treasury-and-cash-management/treasury-accounting-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Treasury Workstation Cash Integration (34P_AE) - SAP S/4HANA Cloud Public Edition (34P_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34P_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Treasury Workstation Accounting Integration** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Treasury Workstation Cash Integration (34P_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851950)

[2 Prerequisites 4](#_Toc232851951)

[2.1 System Access 4](#_Toc232851952)

[2.2 Roles 4](#_Toc232851953)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851954)

[2.4 Additional Manual Configuration 5](#_Toc232851955)

[2.5 Business Conditions 5](#_Toc232851956)

[2.6 Preliminary Steps 6](#_Toc232851957)

[2.6.1 Maintain Full Scope for Cash Management 6](#_Toc232851958)

[2.6.2 Work with Bank Account Unique IDs (Optional) 7](#_Toc232851959)

[2.6.3 Define Criteria for Manual Release (Optional) 8](#_Toc232851960)

[3 Overview Table 10](#_Toc232851961)

[4 Test Procedures 12](#_Toc232851962)

[4.1 Replicate Banks (Optional) 12](#_Toc232851963)

[4.2 Replicate House Banks, House Bank Accounts and Bank Accounts 12](#_Toc232851964)

[4.2.1 Define Filter Criteria (Optional) 13](#_Toc232851965)

[4.2.2 Replicate House Banks and House Bank Accounts 16](#_Toc232851966)

[4.2.3 Monitor Outbound Message for House Banks and House Bank Accounts Replication 17](#_Toc232851967)

[4.2.4 Monitor Inbound Message for House Banks and House Bank Accounts Replication 18](#_Toc232851968)

[4.2.5 Replicate Bank Accounts 20](#_Toc232851969)

[4.2.6 Monitor Outbound Message for Bank Accounts Replication in Sender System 21](#_Toc232851970)

[4.2.7 Monitor Inbound Message for Bank Accounts Replication in Receiver System 22](#_Toc232851971)

[4.3 Replicate Cash Flow 24](#_Toc232851972)

[4.3.1 Schedule Job for Replication Cash Flow Item 24](#_Toc232851973)

[4.3.1.1 Clean up Replicated Cash Flow 25](#_Toc232851974)

[4.3.1.2 Replicate Cash Flow with Aggregated Items 27](#_Toc232851975)

[4.3.1.3 Replicate Cash Flow with Line Items 29](#_Toc232851976)

[4.3.2 Reconcile Distributed Cash Flow Data 31](#_Toc232851977)

[4.3.3 Schedule Job for Retrieving Remote Cash Flow Data 33](#_Toc232851978)

[4.3.4 Monitor SOAP Error Log for Cash Flow Replication (Outbound) 36](#_Toc232851979)

[4.3.5 Monitor Inbound Message for Cash Flow Replication 37](#_Toc232851980)

[4.3.6 Release Cash Flows (Optional) 38](#_Toc232851981)

[5 Appendix 40](#_Toc232851982)

[5.1 Succeeding Processes 40](#_Toc232851983)

## Purpose

Overview

Treasury Workstation Cash Integration makes it possible for the treasury workstation in SAP S/4HANA Cloud Public Edition, normally set up in a group headquarters, to receive the cash flow data from any remote systems of the subsidiaries. This data is incorporated into the various cash reports (for example, Cash Position, Check Cash Flow Items, and Cash Flow Analyzer) for the cash disposition analysis.

With SAP S/4HANA Cloud Public Edition or SAP S/4HANA Cloud Private Edition on either side of the communication, the house bank and account master data can be replicated from one end to the other.

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. These master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/889d382cae91add0048b07b971bed17e)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| BFA - Basic Bank Account Management, J77 - Advanced Bank Account Management | House Banks, House Bank Accounts and Bank Accounts are created in sender system. |
| BFB - Basic Cash Operations, J78 - Advanced Bank Account Management | Cash flows are generated in sender system. |

### Preliminary Steps

#### Maintain Full Scope for Cash Management

Use

In this activity, you maintain Full Scope for cash management.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Select General Settings | Select the following row:Item Name: General Settings | The Configure Your Solution - General Settings view displays. |  |
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Basic Settings step, choose Configure. | The Change View "Define Basic Settings": Details view displays. |  |
| 7 | Select Full Scope | Make the following entries and choose Save.Cash Scope: Full Scope |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open General Settings for Cash Management | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select Full Scope | Make the following entries and choose Save.Cash Scope: Full Scope |  |  |

|  |
| --- |
| Remember Basic Settings must be reviewed following any system upgrade or improvement before continuing any business operation in the system. When differences are found from previous activations, you must correct them in the configuration activity Define Basic Settings. |

#### Work with Bank Account Unique IDs (Optional)

Purpose

Use bank account unique IDs to streamline data distribution and management across platforms.

Bank accounts defined in the Manage Bank Accounts (F1366A) app are identified by a logical key that typically comprises key attributes such as bank account contract type, bank account number, bank country/region, bank key, and currency. However, in data distribution across different systems and landscapes, the logical keys may undergo complex cross-system checks. To facilitate efficient data distribution across systems especially for two-tier scenarios, you can choose to implement bank account unique IDs to enable the unique identification of a bank account throughout your network of integrated systems. This facilitates efficient data management across platforms, reduces replication complexity, and enhances the consistency of bank account master data.

|  |
| --- |
| Caution Implement bank account unique IDs only if necessary. For more details, refer to [Working with Bank Account Unique IDs \| SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/1c14639ec0e74e20bab2472809b2e73d.html) |

Restriction:

Bank Account Master Data replication with Bank Account Unique IDs is currently supported only when both the sender and receiver systems are SAP S/4HANA Cloud Public Edition.

Procedure

Refer to [Working with Bank Account Unique IDs | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/1c14639ec0e74e20bab2472809b2e73d.html).

#### Define Criteria for Manual Release (Optional)

Use

This step is optional and only applicable for those cash flows generated from web service API.

In this step, you define the cash flows to be manually reviewed and released in the Release Cash Flows (F3446) app. Cash flows that fulfill the criteria are listed in the app with a status of unreleased. You can choose to release these cash flows or keep them unreleased. Cash flows that do not fulfill the criteria are automatically released and are not listed in the app.

You can filter the status of cash flows in the Cash Flow Analyzer (F2332) and Check Cash Flow Items (F0735) SAP Fiori apps.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Solution | Go to Configure Your Solution. | The Configure Your Solution: Realize Phase view is displayed. |  |
| 4 | Navigation | In the search box, enter Define Criteria for Manual Release, choose following item:Application Area: FinanceSub Application Area: Cash and Liquidity ManagementItem Name: Cash OperationsOn the Configuration Steps area, choose the Define Criteria for Manual Release step, choose Configure. | The Change View:"FQM: Define Criteria for Manual Release”: Overview displays. |  |
| 5 | Define Criteria for Manual Release | Choose New Entries, make the following entries and choose Save:Logical system: <logical system ID of subsystem that calls the Cash Flow web service>CoCd: <company code of the cash flow>, for example, 3310Level: <planning level of the cash flow> | You created and saved the criteria. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Criteria for Manual Release | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Criteria for Manual Release.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View:"FQM: Define Criteria for Manual Release”: Overview screen displays. |  |
| 3 | Define Criteria for Manual Release | Choose New Entries, make the following entries and choose Save:Logical system: <logical system ID of subsystem that calls the Cash Flow web service>CoCd: <company code of the cash flow>, for example, 3310Level: <planning level of the cash flow> | You created and saved the criteria. |  |

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Replicate House Banks, House Bank Accounts and Bank Accounts

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Define Filter Criteria (Optional)](#unique_12) [page ] 13 | Configuration Expert - Business Network Integration | Define Filter Criteria (F6519) | The filter criteria for the replication model is defined. |
| [Replicate House Banks and House Bank Accounts](#unique_13) [page ] 16 | Configuration Expert - Business Network Integration. | Replicate by Replication Model (DRF_ADHOC_REPLICATION) | The house bank and house bank accounts are replicated from SAP S/4HANA Cloud Public Edition to target system. |
| [Monitor Outbound Message for House Banks and House Bank Accounts Replication](#unique_14) [page ] 17 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | Outbound message displays in sender system. |
| [Monitor Inbound Message for House Banks and House Bank Accounts Replication](#unique_15) [page ] 18 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | Inbound message displays in receiver system. |
| [Replicate Bank Accounts](#unique_16) [page ] 20 | Administrator - Data ReplicationCash Management Specialist | Replicate by Replication Model (DRF_ADHOC_REPLICATION)Manage Bank Accounts (F1366A) | The bank accounts are replicated from SAP S/4HANA Cloud Public Edition to target system. |
| [Monitor Outbound Message for Bank Accounts Replication in Sender System](#unique_17) [page ] 21 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | Outbound message displays in sender system. |
| [Monitor Inbound Message for Bank Accounts Replication in Receiver System](#unique_18) [page ] 22 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | Inbound message displays in receiver system. |

Table 2: Replicate Cash Flow

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Job for Replication Cash Flow Item](#unique_19) [page ] 24 | Cash Management Specialist | Schedule Job for Replication Cash Flow Items (F7281) | One Exposure cash flows on the item flows or the amount aggregated flows with predefined dimensions are replicated from sender system. |
| [Reconcile Distributed Cash Flow Data](#unique_20) [page ] 31 | Cash Management Specialist | Reconcile Distributed Cash Flow Data (F7725) | the reconciled cash flow differences between the central and subsidiary cash systems display. |
| [Schedule Job for Retrieving Remote Cash Flow Data](#unique_21) [page ] 33 | Cash Management Specialist | Schedule Job for Retrieving Remote Cash Flow Data (F7751) | The replicated data from certain remote system is deleted, and request is sent to this system to trigger outbound cash flow. |
| [Monitor SOAP Error Log for Cash Flow Replication (Outbound)](#unique_22) [page ] 36 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005) | Outbound message displays in sender system. |
| [Monitor Inbound Message for Cash Flow Replication](#unique_23) [page ] 37 | Configuration Expert - Business Network Integration | Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005)/ | Inbound message displays in receiver system. |
| [Release Cash Flows (Optional)](#unique_24) [page ] 38 | Cash Management Specialist | Release Cash Flows (F3446) | Cash flows are released. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Replicate Banks (Optional)

Purpose

Bank replication steps are not included in this scope item. If you want to use the Bank Replication solution, please refer to [Bank Replication | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/8faf299951a9468ba868d1ea5378cd63.html).

### Replicate House Banks, House Bank Accounts and Bank Accounts

Purpose

Hybrid deployment of Cash and Liquidity Management is supported. In hybrid scenarios, you can maintain master data for house banks, house bank accounts, and bank accounts in your SAP S/4HANA Cloud Public Edition system where Cash and Liquidity Management is installed and serves as the treasury workstation system. You can then replicate the master data to other integrated business systems using IDoc (Intermediate Document). This way, you ensure that the master data is identical and in sync across all the systems in the landscape.

Replication using IDoc allows you to integrate your SAP S/4HANA Cloud Public Edition system with other business systems, including:

- SAP S/4HANA Cloud Public Edition
- SAP S/4HANA Cloud Private Edition (also including SAP S/4HANA)
- SAP ECC (ERP Central Component) systems

A bank account logical key typically comprises key attributes such as bank account contract type, bank account number, bank country/region, bank key, and currency. However, in data distribution across different systems and landscapes, the logical keys may undergo complex cross-system checks. For more information, see [Bank Account Logic Keys](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/28e8e9d52d2f4e81a1542b49206f98d5.html?version=2502.VAL#loio28e8e9d52d2f4e81a1542b49206f98d5__bank_account_logic_key.html).

|  |
| --- |
| Note You can also perform data replication based on bank account unique IDs, you must have implemented bank account unique IDs in your treasury workstation system which serves as the source system in data distribution. For more information about how to implement it, see [Working with Bank Account Unique IDs](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/1c14639ec0e74e20bab2472809b2e73d.html?version=2502.VAL.html).When you have deleted bank accounts in the origin system and need to synchronize these changes to receiver systems, it is recommended to use the Change mode for data replication.Currently, this approach is supported only for replications between SAP S/4HANA Cloud Public Edition systems. |

|  |
| --- |
| Note Overdraft types are not available in SAP S/4HANA systems but are required in SAP S/4HANA Cloud Public Edition systems. Therefore, please note the following when you perform data replication for bank accounts that contain overdraft limit entries:From a SAP SAP S/4HANA system to a SAP S/4HANA Cloud Public Edition system:A predelivered overdraft type SO01 will be assigned to overdraft limits replicated to the SAP S/4HANA Cloud Public Edition system.The default value depends on the latest content version. Please make sure you upgrade to the latest content version to use this feature.From a SAP S/4HANA Cloud Public Edition system to a SAP S/4HANA system:In SAP S/4HANA systems, you can only define one overdraft limit entry per currency for a bank account. However, there might be several entries available in the SAP S/4HANA Cloud Public Edition system due to the introduction of overdraft types.In this case, you can use the segment filter in the data replication tool to select one overdraft limit entry to replicate to the target SAP S/4HANA system. |

|  |
| --- |
| Note Make sure that the bank data and company code data exist and are identical in both the sender and receiver systems. |

|  |
| --- |
| Note The activation of the feature Manage Bank Accounts: Contract Type Validation (FTGL_BAM_BKACCT_CONTR_TYPE_VAL) in the configuration activity Activate Features enforces a check on bank account contract type assignments. If you have used contract types other than Current Account while the contract type is not enabled in the configuration activity Define Basic Settings (101025), the system will prompt errors for relevant bank accounts asking you to correct your bank account master data.Before replication, ensure Bank Account Contract Type Validation is consistent between the source system and target systems. For more information, see [link](https://help.sap.com/docs/SAP_S4HANA_CLOUD/ee9ee0ca4c3942068ea584d2f929b5b1/3bef4885289f4de18dda697c8b11b519.html). |

Restriction:

- The contract type “Pseudo Account for Working Capital” replication is currently supported only when both the sender and receiver systems are SAP S/4HANA Cloud Public Edition.

(Optional) You may use the following configuration activities to define system groups for bank account master data distribution scenarios. This feature allows you to group your systems based on shared attributes, such as country, region, and data replication rules. System groups can also be used to organize your development, test, and production systems within a single group. By organizing your systems into groups, you can simplify configuration activities for bank account master data distribution across multiple systems.

- Define System Groups (107199)

Define system groups according to your business needs. For each system group, you can decide whether to enable the Convert Remote House Bank Accounts function to ensure only relevant bank accounts and house bank accounts are replicated to target systems and these house bank accounts are properly converted in data replication. For more information, see the configuration help.

- Assign Logical System to System Groups (107199)

For each logical system, you can assign it to only one system group.

#### Define Filter Criteria (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can define the filter for the replication model in sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Define Filter Criteria (F6519). |  |  |
| 3 | Enter Replication Model Data | Make the following entries and choose Go:Replication Model: for example,RM_HBMXX - House Bank/House Bank AccountRM_BAMXX - Bank Account Master Data |  |  |
| 4 | Define Filter Criteria for Replication Model RM_HBMXX | Choose > for the replication model RM_HBMXX-House Bank/House Bank Account (with Business Object Type HBHBA_OBJ). | The Replication Model screen displays. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Check Main Filter Item | In the Main Filter section, choose > for House bank filter (HBANK_FO) | The Main Filter Item view displays. |  |
| 7 | Maintain Filter Criteria for Business Objects | In the Main Filters section, choose Create. Make the following entries and choose Apply:For example,Item 1Filed Name: Company Code （BUKRS）Filter: equal toValue: 3310Item 2Filed Name: Bank Key （BANKL）Filter: equal toValue: 18121976 |  |  |
| 8 | Save | Choose Save. | The filter criteria for the specific replication model is defined. |  |
| 9 | Back | Choose Back. |  |  |
| 10 | Define Filter Criteria for Replication Model RM_BAMXX | Repeat step 4-8, maintain the following filter criteria for replication model RM_BAMXX - Bank Account Master Data (with Business Object Type BAMMAST).For example,Item 1Filed Name: Company Code （BUKRS）Filter: equal toValue: 3310Item 2Filed Name: Bank Key （BANKL）Filter: equal toValue: 18121976Item 3Filed Name: Bank Account Number （ACC_NUM）Filter: equal toValue: 0000000693123456Segment Filters (Filter Object BAM_LIM) SectionItem 1)Filed Name: Bank Account Overdraft Category (OVERDRAFT_CATEGORY)Filter: for example, equal toValue: for example, 01 Overnight OverdraftItem 2)Filed Name: Bank Account Overdraft Category (OVERDRAFT_CATEGORY)Filter: for example, equal toValue: for example, <one overdraft type> |  |  |

#### Replicate House Banks and House Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can replicate House Banks and House Bank Accounts from SAP S/4HANA Cloud Public Edition to target system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION). | The Replicate by Replication Model view displays. |  |
| 3 | Replicate House Bank Master Data | Make the following entry and choose Replicate:Replication Model: for example, RM_HBMXX-House Bank/House Bank AccountSelect Target System: <as needed>Select Business Objects to be Replicated: <as needed>Replication Mode Section:Initialization: <as needed>Note Replicate existing house banks, house bank accounts, and bank accounts to receiver systems in one go.Change: <as needed>Note Replicate changes that occurred in the sender system during a specified time interval to receiver systems.Note Choose one replication mode.Select Replication Option Section:Test Run Only: <as needed> | Replication was started for the target system.Note Please be aware that Parallel Processing is not supported in this scenario. |  |
| 4 | Monitor Replication | Access the App Monitor Replication (DRF_WDA0475) to check replication logs. | The log for your replication model displays. |  |

#### Monitor Outbound Message for House Banks and House Bank Accounts Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor outbound message for House Banks and House Bank Accounts replication in sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). | The Interface monitor view displays. |  |
| 3 | Select Message Date Interval | In the Calendar Monitor section, enter the date of replication and choose Search. |  |  |
| 4 | Check Status | In the Result List section, check following Namespace / Interface:Namespace: /FINBA FIN: Bank Account ManagementInterface: Outbound Interface for IDOC HBHBAMAST02Note Replicate from SAP S/4HANA Cloud Public Edition to SAP ECC (ERP Central Component), interface is Outbound Interface for IDOC HBHBAMAST01.You can see [Message Monitoring \| SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/186460fdc35a4b64a713da9bb00deb1e/b95cd5a9f018411c9612d26a7567f8ae.html). | If the status of Outbound Interface for IDOC HBHBAMAST02 is green, the outbound replication execution succeeded. |  |
| 5 | Check Error Message (Optional) | Click the number of Errors (Application Errors) or Technical Errors. | The Monitoring and Error Handling screen displays. |  |
| 6 | Check Detailed Log | Expand the data message structure, find the message for your master data replication, check the application log or technical log in detail.Choose Reprocess after errors are corrected and choose Cancel to delete the messages that are no longer valid.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed log displays. |  |
| 7 | Check Bank Record | On the right panel, select the node Structure for bank record under Data Structure to view the bank record sent to the target system. | The bank record displays under Data Content. |  |

#### Monitor Inbound Message for House Banks and House Bank Accounts Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor inbound message for House Banks and House Bank Accounts replication in receiver system.

Prerequisites

Before monitoring inbound message in receiver system, you should perform the procedure [Replicate House Banks, House Bank Accounts and Bank Accounts](#unique_27) [page ] 12 in sender system. Make sure the outbound message has been transferred successfully in sender system. There are no errors in sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). | The Interface monitor view displays. |  |
| 3 | Select Message Date Interval | In the Calendar Monitor section, enter the date of replication and choose Search. |  |  |
| 4 | Check Status | In the Result List section, check following Namespace / Interface:Namespace: /FINBA FIN: Bank Account ManagementInterface: Inbound Interface for IDOC HBHBAMAST02 | If the status of Inbound Interface for IDOC HBHBAMAST02 is green, the inbound replication execution succeeded.Note Check the house bank master data via App Manage Banks - Cash Management (F1574A). |  |
| 5 | Check Error Message (Optional) | Click the number of Errors (Application Errors) or Technical Errors. | The Monitoring and Error Handling screen displays. |  |
| 6 | Check Detailed Log | Expand the data message structure, find the message for your master data, check the application log or technical log in detail.Choose Reprocess after errors are corrected and choose Cancel to delete the messages that are no longer valid.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed log displays. |  |
| 7 | Check Bank Record | On the right panel, select the node Structure for bank record under Data Structure to view the bank record received from the target system. | The bank record displays under Data Content. |  |

#### Replicate Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can replicate Bank Accounts from SAP S/4HANA Cloud Public Edition to the target systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate by Replication Model (DRF_ADHOC_REPLICATION). |  |  |
| 3 | Replicate Bank Account Master Data | Make the following entries and choose Replicate:Replication Model: choose for example, RM_BAMXX - Bank Account Master DataSelect Target System: <as needed>Select Business Objects to be Replicated : <as needed>Replication Mode Section:Initialization: <as needed>Change: <as needed>Note Choose one replication mode.Select Replication Option Section:Test Run Only: <as needed> | Replication was started for the target system.Note Please be aware that Parallel Processing is not supported in this scenario. |  |
| 4 | Monitor Replication | Access the App Monitor Replication (DRF_WDA0475) to check replication logs. | The log for your replication model displays. |  |

#### Monitor Outbound Message for Bank Accounts Replication in Sender System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor outbound message for Bank Accounts replication in sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Select Message Date Interval | In the Calendar Monitor section, enter the date of replication and choose Search. |  |  |
| 4 | Check Status | In the Result List section, check following Namespace / Interface:Namespace: /FINBA FIN: Bank Account ManagementInterface: Outbound Interface for IDOC BAMMAST03 | If the status of Outbound Interface for IDOC BAMMAST03 is green, the outbound replication execution succeeded. |  |
| 5 | Check Error Message (Optional) | Click the number of Errors (Application Errors) or Technical Errors. | The Monitoring and Error Handling screen displays. |  |
| 6 | Check Detailed Log | Expand the data message structure, find the message for your master data replication, check the application log or technical log in detail.Choose Reprocess after errors are corrected and choose Cancel to delete the messages that are no longer valid.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed log displays. |  |
| 7 | Check Bank Record | On the right panel, select the node Structure for bank record under Data Structure to view the bank record sent to the target system. | The bank record displays under Data Content. |  |

#### Monitor Inbound Message for Bank Accounts Replication in Receiver System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can monitor inbound message for Bank Accounts replication in receiver system.

Prerequisites

Before monitoring inbound message in receiver system, you should perform the procedure [Replicate Bank Accounts](#unique_16) [page ] 20 in sender system. Make sure the outbound message has been transferred successfully in sender system. There are no errors in sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Select Message Date Interval | In the Calendar Monitor section, enter the date of replication and choose Search. |  |  |
| 4 | Check Status | In the Result List section, check following Namespace / Interface:Namespace: /FINBA FIN: Bank Account ManagementInterface: In bound Interface for IDOC BAMMAST03 | If the status of Inbound Interface for IDOC BAMMAST03 is green, the inbound replication execution succeeded.Note Check the bank account master data via App Manage Bank Accounts (F1366A). |  |
| 5 | Check Error Message (Optional) | Click the number of Errors (Application Errors) or Technical Errors. | The Monitoring and Error Handling screen displays. |  |
| 6 | Check Detailed Log | Expand the data message structure, find the message for your master data, check the application log or technical log in detail.Choose Reprocess after errors are corrected and choose Cancel to delete the messages that are no longer valid.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed log displays. |  |
| 7 | Check Bank Record | On the right panel, select the node Structure for bank record under Data Structure to view the bank record received from the target system. | The bank record displays under Data Content. |  |

### Replicate Cash Flow

Purpose

This section describes the integration scenario which allows you to deploy your Treasury Workstation in SAP S/4HANA Cloud Public Edition with other distributed business systems (including SAP systems or third-party systems). You can receive cash flow data from integrated business systems via the services Cash Flow - Inbound Service (CASHFLOW_IN). And then you can use the Release Cash Flows (F3446) app to review and release the integrated cash flow data. You can also send cash flow data to integrated business system via Cash Flow - Outbound Service (CASHFLOW_OUT).

|  |
| --- |
| Note Outbound message for cash flow replication can not be monitored in Message Dashboard in sender system. You can only check the inbound message in target system. |

|  |
| --- |
| Note You may have enabled the automatic expiration function for memo records in your current system. However, when they are replicated to other systems through the Cash Flow - Inbound Service API (CASHFLOW_IN), the expiration information is not transferred. You can therefore use the app Schedule Jobs for Deactivating Memo Records 2.0 (F8915) to deactivate expired memo records to prevent them from being considered as valid memo records in the target system. |

#### Schedule Job for Replication Cash Flow Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can send out One Exposure cash flows on the item flows or the amount aggregated flows with predefined dimensions in sender system. Besides, the job can also send out cleanup messages with the company code, certainty level, transaction date selection to delete replicated flows in the receiver system.

|  |
| --- |
| Note The cash flow items can only be replicated to one target system. If one or more replication modes are created in the same sender/subsidiary system , an error message Invalid replication model or multiple replication models exist will occur. |

|  |
| --- |
| Note Ensure that the bank key, bank account, and/or IBAN are present in both the sender and receiver systems. |

##### Clean up Replicated Cash Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can clean up cash flows in the central system with the manual selection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Replication Cash Flow Items (F7281). | The Schedule Job for Replication Cash Flow Items screen displays. |  |
| 3 | Create a New Application Job | Choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: For example, Cleanup Replicated Cash FlowJob Name: for example, Cleanup Replicated Cash Flow | The New Job: Cleanup Replicated Cash Flow view displays. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, select the Start Immediately checkbox.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In Parameter section, make the following entries:Transfer Parameter Section:Replication Action: Mass Cleanup Replicated FlowsReplication Model: <select one replication mode via value help>Test Run: <as needed>Parallel Processing: <select>Server Group: for example, parallel_generatorsNo.work processes: for example, 3Cash Flow Selection Section:Company code: For example, 3310Certainty Level: for example, Memo Record(MEMO)Transaction Date: for example, <current week>Note Empty value means all cases will be included in the job. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run This Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. Or choose Results with Preview to check all results. | Job log displays. |  |

##### Replicate Cash Flow with Aggregated Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can replicate cash flow with aggregated items. The predefined aggregation dimensions are Company Code, Source Application, Certainty Level, Transaction Date, Bank Account ID, G/L Account, Liquidity Item, Planning Level, Planning Group, Flow Category.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Replication Cash Flow Items (F7281). | The Schedule Job for Replication Cash Flow Items screen displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: For example, Replicate Cash Flow with Aggregated ItemsJob Name: for example, Replicate Cash Flow with Aggregated Items | The New Job: Replicate Cash Flow with Aggregated Items view displays. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, select the Start Immediately checkbox.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In the Parameter section, make the following entries:Transfer Parameter Section:Replication Action: Aggregated Flow in Manual ModeReplication Model: <select one replication mode via value help>Test Run: <as needed>Parallel Processing: <select>Server Group: for example, parallel_generatorsNo.work processes: for example, 3Cash Flow Selection Section:Source Application: For example, <empty>Company code: For example, 3310Transaction Date: for example, <current week>Bank Account Internal ID: <maintain one bank account internal ID>Note You can find the bank account internal ID via App Manage Bank Accounts (F1366A).Note You can also maintain the parameter in the Additional section. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run This Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log navigate to the Job Log. Or choose Results with Preview to check all result. | Job log displays. |  |

##### Replicate Cash Flow with Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can replicate cash flow with line items (Item Flows in Manual Mode / Item Flows Update in Delta Mode).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Replication Cash Flow Items (F7281). | The Application Jobs view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: For example, Replicate Cash Flow with Line ItemsJob Name: for example, Replicate Cash Flow with Line Items | The New Job: Replicate Cash Flow with Line Items view displays. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, select the Start Immediately checkbox.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In the Parameter section, make the following entries:Transfer Parameter Section:Replication Action: for example: Item Flows in Manual ModeReplication Model: <select one replication mode via value help>Test Run: <as needed>Parallel Processing: <select>Server Group: for example, parallel_generatorsNo.work processes: for example, 3Cash Flow Selection Section:Source Application: For example, <empty>Company code: For example, 3310Transaction Date: for example, <current week>Bank Account Internal ID: <maintain one bank account internal ID>Note You can find the bank account internal ID via App Manage Bank Accounts (F1366A).G/L Account: <as needed>Planning Group: <as needed>Planning Level: <as needed>Transaction Currency: <as needed>Note You can also choose Replication Action: Item Flows Update in Delta Mode and maintain the parameter in Delta Extraction Time Frame. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log.Or choose Results with Preview to check all results. | Job log displays. |  |

#### Reconcile Distributed Cash Flow Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display the reconciled cash flow differences between the central and subsidiary cash systems. One Exposure Cash Flow in the subsidiary system is replicated to the central cash system on a regular basis. You can also trigger the synchronization process to get rid of cash flow differences between the connected systems.

Please be noted that all the diffenrent results are reconciled per dimensions in the central system, no matter what kind of original data are mapped from the source systems. The different result is in the aggregated amount, not in comparing each individual line.

|  |
| --- |
| Note The cash flow items can only be replicated to one target system. If one or more replication modes are created in the same sender/subsidiary system, an error message Replication model is not found will occur. |

|  |
| --- |
| Note This feature is currently supported only when both the sender and receiver systems are SAP S/4HANA Cloud Public Edition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Reconcile Distributed Cash Flow Data (F7725). |  |  |
| 3 | Maintainm Filters | Make the following entries and choose Go:Subsidiary System: <source system>Note Select the source system in which you want to compare the data.Replication Category: for example, Aggregated Item ModeNote Select the original cash flow replication mode.Currency Code: for example, Transaction CurrencyNote You can compare either the transaction currency amount or the company code currency amount of the cash flow.Transaction Date: for example, current weekCompany Code : 3310Note Maintain other fields as needed. | The reconciliation results displays. With the Overview Page, you can show the reconciled difference results per dimension Transaction Date, Company Code, Certainty Level, G/L Account.Note If the subsidiary system is defined after creating the communication arrangement with communication scenario SAP_COM_0824, the error message Subsidiary system is not correctly set up will occur. You need to reactivate the communication arrangement. |  |
| 4 | Check Details | Select one item, Choose > (Details). | The detail page displays. In the detail page, the difference result is compared with more dimensions like Bank Account Internal ID, Liquidity Item, Planning Level, Planning Group, which are crucial for Cash Management.Count Difference: cash flow count difference after reconciliation.Amount Difference: cash flow amount difference after reconciliation.Reconciliation Status: cash flow reconciliation status after comparison between systems with the following comparing priorities:Non-existentThis cash flow can be found in the sending system, but not found in the receiving system.UnexpectedThis cash flow can be found in the receiving system, but not found in the sending system.Different CountCash flows are available in both the sending and receiving systems, but the number of lines is inconsistent. The count number refers to the number of rows before aggregated reconciliation.Different AmountThe aggregated amount from the sending system is different from the aggregated amount from the receiving system.Different DimensionThe Amount and the Count of flows between sending and receiving system are consistent, but there are inconsistent on dimension fields. |  |
| 5 | Synchronize | Choose Synchronize to navigate to Schedule Job for Retrieving Remote Cash Flow Data. Check the detailed procedure in next step. | The new screen for Schedule Job for Retrieving Remote Cash Flow Data displays. |  |

#### Schedule Job for Retrieving Remote Cash Flow Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule jobs for Retrieve Cash Flow Data using the template and scheduling options provided. When you work on the central cash system, you can retrieve cash flow data from the individual subsidiary sytems. The retrieving process includes deleting replicated data from certain remote system, and sending request to this system to trigger outbound cash flow.

You can also schedule the cash flow replication job in the subsidiary system using the app Schedule Job for Replication Cash Flow Items (F7281) with the line item and/or aggregated item mode. According to the configuration in the source system, the retrieving process handles cash flow data in one of the modes or both of the modes.

|  |
| --- |
| Note The cash flow items can only be replicated to one target system. If one or more replication modes are created in the same sender/subsidiary system, an error message Replication model is not found will occur. |

|  |
| --- |
| Note This feature is currently supported only when both the sender and receiver systems are SAP S/4HANA Cloud Public Edition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist . |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Job for Retrieving Remote Cash Flow Data (F7751). | The Schedule Job for Retrieving Remote Cash Flow Data screen displays. |  |
| 3 | Create a New Application Job | Choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: For example, Retrieve Cash Flow DataJob Name: for example, Retrieve Cash Flow Data | The New Job: Retrieving Remote Cash Flow Data view displays. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, select the Start Immediately checkbox.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In the Parameter section, make the following entries:Subsidiary System: <source system>Note Select certain subsidiary cash system you want to retrieve cash flow data.Test Run: for example, DeseletedNote Select the original cash flow replication mode.Manual Selection: for example, selectedNote Enable the manual selection of cash flow with the condition Transaction Date to delete the local data and retrieve the remote data. Leave it empty in case you want the system to determine the cash flow transaction dates which contain differences between the central and subsidiary system.Transaction Date: for example, current weekNote Enter Transaction Date to delete and retrieve cash flows. Empty Transaction Date means deleting and retrieving full cash flow data without restriction. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays. |  |

#### Monitor SOAP Error Log for Cash Flow Replication (Outbound)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the web service API is called, if errors occur, you can check the SOAP error logs in the sender system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Monitoring: SOAP Error Log - SAP Application Interface Framework (F6961). |  |  |
| 3 | Select Message Date Interval | Make following entries and choose Go.Time: for example, Past 2 WeeksInterface Name: CashFlow_Out | The error logs displays.Note When there are no errors, no data is available. |  |
| 4 | Check Detailed Error Log | Find the message for your data, check Log Messages in detail.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed error log displays.Note You can also use the SAP Fiori App Message Monitoring: OData Error Log - SAP Application Interface Framework (F6961) to check the error logs for Inbound messsage with Interface Name CashFlow_In in receiver system. |  |

#### Monitor Inbound Message for Cash Flow Replication

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the web service API is called or one exposure cash flows are transferred, the inbound messages can be monitored in Message Dashboard in receiver system.

|  |
| --- |
| Note Outbound message for cash flow replication can not be monitored in Message Dashboard in sender system. |

Prerequisites

Make sure the outbound message has been transferred successfully in sender system. There are no errors in sender system.

|  |
| --- |
| NoteIntegration with SAP S/4HANA Cloud Private Edition, you use transaction FQM_CFOUTB to replicate One Exposure Cash Flow Items in the sender system.Integration with SAP S/4HANA Cloud Public Edition, you perform procedure in the sender system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. |  |  |
| 2 | Access the SAP Fiori App | Open Message Dashboard - SAP Application Interface Framework (/AIFX/WDA0005). |  |  |
| 3 | Select Message Date Interval | In the Calendar Monitor section, enter the date of replication and choose Search. |  |  |
| 4 | Check Status | In the Result List section, check following Namespace / Interface:Namespace: One Exposure - /FQM NamespaceInterface: Hybrid Cash – HYBRID_CSH/1 | If the status of Hybrid Cash – HYBRID_CSH/1 is green, the inbound replication execution succeeded.Note You can use App Check Cash Flow Items (F0735) to check the generated cash flows with Source Application RMTE (Cash Flows from Remote Systems). |  |
| 5 | Check Error Message (Optional) | Click the number of Errors (Application Errors) or Technical Errors. | The Monitoring and Error Handling screen displays. The listed hierarchy is Namespace > Interface > Source System > Company Code > Message . |  |
| 6 | Check Detailed Log | Expand the data message structure, find the message for your data, check the application log or technical log in detail.Choose Reprocess after errors are corrected and choose Cancel to delete the messages that are no longer valid.Note For each message, all the application/technical errors need to be fixed until the message is transferred to the system successfully. | The detailed log displays. |  |
| 7 | Check Cash Flow Request Content | On right panel, select the node CASH_FLOW_REQUEST_CONTENT under Data Structure to view the cash flows received from the target system. | The cash flows display under Data Content. |  |

#### Release Cash Flows (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can get an overview of memo records from your current system and cash flows from other integrated business systems. You can review cash flows with attributes such as company code, planning level, and source system. Based on your requirements, you can then manually release cash flows that you want to see in other cash management reports, such as Cash Flow Analyzer and Check Cash Flow Items.

Prerequisites

Make sure you have made configuration settings of the rules for manual release in the preliminary step [Define Criteria for Manual Release (Optional)](#unique_10) [page ] 8.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Release Cash Flows (F3446). |  |  |
| 3 | Select Cash Flows | In the upper filter area, enter the following data and choose Go:Release Status: UnreleasedValue Date: Current Week | A list of unreleased cash flows in a hierarchy with various filtering options is displayed. You can view cash flows from different source systems, including:Cash flows from integrated business systems, including SAP systems and third-party systemsMemo records from your current system |  |
| 4 | Release Cash Flows | Choose Release All. | A dialog box displays to confirm the action. |  |
| 5 | Confirm the Release | Choose Release. | Cash flows are released and not displayed. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Process | Business Condition |
| --- | --- |
| Advanced Cash Operations (J78) | Review the cash flow items you created by executing the Check Cash Flow Items procedure in this test script. |

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
- related-to :: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-treasury-workstation-paym]]
- related-to :: [[05-treasury-and-cash-management/test-script-treasury-workstation-accounting-integration-33e-ae-897]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34P_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 70,301 chars in the whole document
