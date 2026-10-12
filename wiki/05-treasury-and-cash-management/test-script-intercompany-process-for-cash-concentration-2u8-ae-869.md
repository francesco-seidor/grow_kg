---
id: 05-treasury-and-cash-management/test-script-intercompany-process-for-cash-concentration-2u8-ae-869
title: "Test Script: Intercompany Process for Cash Concentration (2U8_AE) (2U8_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (AE) for cash pools and cash concentration under Advanced Cash Operations: prerequisites, config steps, test procedures."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/cash-pooling-and-concentration]
aliases: [2U8_S4CLD2608_BPD_EN_AE]
keywords: [Cash Pooling and Cash Concentration, cash concentration, cash pools, cash pool hierarchies, cash concentration jobs, cash concentration model, cash pool transfer report, bank account balance profile, authorization groups, concentration groups]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-869
topic: 05-treasury-and-cash-management/cash-pooling-and-concentration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Process for Cash Concentration (2U8_AE) (2U8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Cash Pooling and Cash Concentration** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Process for Cash Concentration (2U8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850358)

[2 Prerequisites 4](#_Toc232850359)

[2.1 System Access 4](#_Toc232850360)

[2.2 Roles 4](#_Toc232850361)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850362)

[2.4 Business Conditions 6](#_Toc232850363)

[2.5 Additional Manual Configuration 6](#_Toc232850364)

[2.6 Preliminary Steps 6](#_Toc232850365)

[2.6.1 Maintain Full Scope for Cash Management 6](#_Toc232850366)

[2.6.2 Enable New Cash Concentration Model 8](#_Toc232850367)

[2.6.3 Define Bank Account Balance Profile 10](#_Toc232850368)

[2.6.4 Define Authorization Groups for Cash Pools 12](#_Toc232850369)

[2.6.5 Define Concentration Group for Cash Concentration 14](#_Toc232850370)

[2.6.6 Create Bank Accounts (Optional) 16](#_Toc232850371)

[2.6.7 Set Up Bank Determination for Payment Transactions 16](#_Toc232850372)

[2.6.8 Define Clearing Accounts for Receiving Bank for Account Transfer 18](#_Toc232850373)

[2.6.9 Define Clearing Accounts for Outgoing Bank Transfers 20](#_Toc232850374)

[3 Overview Table 22](#_Toc232850375)

[4 Test Procedures 23](#_Toc232850376)

[4.1 Manage Cash Pools (Version2) 23](#_Toc232850377)

[4.2 Display Cash Pool Hierarchies 26](#_Toc232850378)

[4.3 Manage Cash Concentration 27](#_Toc232850379)

[4.3.1 Option 1: Perform Cash Concentration 28](#_Toc232850380)

[4.3.2 Option 2: Schedule Jobs for Cash Concentration (Optional) 31](#_Toc232850381)

[4.4 Cash Pool Transfer Report 34](#_Toc232850382)

[5 Appendix 35](#_Toc232850383)

[5.1 Process Chains 35](#_Toc232850384)

## Purpose

Overview

This scope item enables the cash manager to establish cash pools, execute cash concentration, and track cash pool concentration logs. Different reports are available to cash manager. Key cash concentration criteria can be defined. The cash manager can also define a profile to filter different planning levels for cash pools.

|  |
| --- |
| Caution These procedures are only required if you have adopted Advanced Cash Operations, which requires an additional license for SAP Cash Management powered by SAP HANA. If you use Basic Cash Operations, skip all steps in this document. |

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
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

|  |
| --- |
| Note The Cash Manager and Accounts Payable Manager roles are used as different approvers in the payment approval process. During testing, they must be separate user IDs. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. These master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Bank Key | 18121976,18121986 |  | Bank key |
| Country | AE |  | Country of bank key |
| Company Code | 3310 |  | Company code |
| G/L Account | 11001000, 11002000 and so on |  | G/L account for bank accounts |
| Chart of Accounts | YCOA |  | Chart of accounts |
| House Bank | AEBK1AEBK2 |  | House bank |
| House Bank Account | AEAC1 AEAC2 |  | House bank account is integrated in Bank account master data (BAM) |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J78 - Advanced Cash Operations | This scope item Advanced Cash Operations (J78) is the prerequisite for this test script. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9f5d1abf6a52a547efb42be8f8bc9538)

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

#### Enable New Cash Concentration Model

Use

You use this configuration activity to define the cash concentration model and bank account balance type you want to use in the Manage Cash Concentration (F3265) app. The balance type determines which type of balance is used as the opening balance of your cash pools in cash concentration.

|  |
| --- |
| CautionWhen the option Enable New Cash Concentration Model is set, you can use cash pools that have the service provider Company - Time - Dependent in cash concentration. You can define these cash pools in the Manage Cash Pools (Version 2) (F3266A) app.When the option Enable New Cash Concentration Model is not set, you can use cash pools that have the service provider Enterprise and Bank in cash concentration. You can define these cash pools in the Manage Cash Pools (Deprecated) app and the Manage Bank Accounts (F1366A) app. For cash pools with the service provider Enterprise, you can make transfers between the header account and subaccounts based on system proposals. For cash pools with the service provider Bank, you can simulate cash concentration by creating memo records. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 4 | Filter List | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | A list of Configuration Items display with the filter criteria. |  |
| 5 | Select General Settings | Select the following row:Item Name: Cash Operations | The Configure Your Solution - General Settings view displays. |  |
| 6 | Define Basic Settings | From the Configuration Steps area, on the Define Settings for Cash Concentration step, choose Configure. | The Define Settings for Cash Concentration: change view displays. |  |
| 7 | Enable New Cash Concentration Model | Enter the following data:Enable New Cash Concentration Model: <selected>Balance Type: for example, Value date balanceNote The following balance types are supported:Available BalanceThe available balance indicates the funds available to the account holder for immediate use. For bank statements that do not provide it, the system creates a data entry for the available balance by copying the amount of the value date balance.Value Date BalanceThe value date balance is the interest-bearing closing balance for a particular day. It is calculated based on the ledger balance of the day by excluding bank statement items whose value date comes after the bank statement date, including items from an earlier bank statement.Aggregated ActualsThe balance is calculated by aggregating actual flows from the One Exposure from Operations hub. Choose this option if you don't have electronic bank statements available, or if you use a custom program to import your bank statements. |  |  |
| 8 | Save | Choose Save. | New cash concentration model is enabled. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open General Settings for Cash Management | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Settings for Cash Concentration.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Settings for Cash Concentration: change screen displays. |  |
| 3 | Enable New Cash Concentration Model | Enter the following data:Enable New Cash Concentration Model: <selected>Balance Type: for example, Value date balanceNote The following balance types are supported:Available BalanceThe available balance indicates the funds available to the account holder for immediate use. For bank statements that do not provide it, the system creates a data entry for the available balance by copying the amount of the value date balance.Value Date BalanceThe value date balance is the interest-bearing closing balance for a particular day. It is calculated based on the ledger balance of the day by excluding bank statement items whose value date comes after the bank statement date, including items from an earlier bank statement.Aggregated ActualsThe balance is calculated by aggregating actual flows from the One Exposure from Operations hub. Choose this option if you don't have electronic bank statements available, or if you use a custom program to import your bank statements. |  |  |
| 4 | Save | Choose Save. | New cash concentration model is enabled. |  |

#### Define Bank Account Balance Profile

Purpose

In this step, you define bank account balance profile. With bank account balance profiles, you can define forecasted cash flows to be taken into consideration between the latest bank statement date and the value date of your cash concentration. This ensures that cash concentration is performed based on the most up-to-date balance data.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Application Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management |  |  |
| 5 | Cash Operations | Choose the arrow button at the right of the Cash Operations row. |  |  |
| 6 | Assign Planning Levels to Profiles | Find the Assign Planning Levels to Profiles row and choose Configure. |  |  |
| 7 | Define Profile | In the Dialog Structure pane, double click Define Profile.Choose New Entries.Enter the following data, and choose Save:Prof. Name: for example, ZCP_GENProf. Type: Cash PoolingBalance Calculation Profile Description: Cash Pool Balance Calculation Profile | A profile is created. |  |
| 8 | Assign Planning Level to Profile | Select the ZCP_GEN profile name, and in the Dialog Structure pane, double click Assign Planning Level to Profile.Choose New Entries.Enter the following data:Level: <the relevant planning levels as needed>Maintain the requirement planning levels, and choose Save. | The required planning levels are assigned to the profile for the calculation of bank account balance in cash concentration.Note To use additional profiles in multilevel cash pooling scheme, repeat steps 7 to 8 to create other profiles as needed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Assign Planning Levels to Profiles | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Planning Levels to Profiles.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Profile | In the Dialog Structure pane, double click Define Profile.Choose New Entries.Enter the following data, and choose Save:Prof. Name: for example, ZCP_GENProf. Type: Cash PoolingBalance Calculation Profile Description: Cash Pool Balance Calculation Profile | A profile is created. |  |
| 4 | Assign Planning Level to Profile | Select the ZCP_GEN profile name, and in the Dialog Structure pane, double click Assign Planning Level to Profile.Choose New Entries.Enter the following data:Level: <the relevant planning levels as needed>Maintain the requirement planning levels, and choose Save. | The required planning levels are assigned to the profile for the calculation of bank account balance in cash concentration.Note To use additional profiles in multilevel cash pooling scheme, repeat steps 7 to 8 to create other profiles as needed. |  |

#### Define Authorization Groups for Cash Pools

Purpose

If you want to restrict the access to cash pools of this category, you can define authorization groups. The authorization groups can be used to restrict the access to cash pools and cash position data in the following apps:

- Manage Cash Pools (Version 2) (F3266A)
- Short-Term Cash Positioning (F5380)
- Display Cash Pool Hierarchies (F6123)

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row:Step Name: Define Authorization Groups for Cash Pools. | The "Define Authorization Groups for Cash Pools": Change view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Create Authorization Group | Make the following entries and choose Save:Auth Group: For example, ZCP1Description: For example, Authorization group for cash pool | The authorization group for cash pool is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Authorization Groups for Cash Pools | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Authorization Groups for Cash Pools.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Authorization Groups for Cash Pools": Change view displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Create Authorization Group | Make the following entries and choose Save:Auth Group: For example, ZCP1Description: For example, Authorization group for cash pool | The authorization group for cash pool is created. |  |

#### Define Concentration Group for Cash Concentration

Purpose

In this activity, you define the cash concentration group according to your own business requirements, for example, you may use different cash concentration groups for different treasury centers, companies, or currencies. It is required for you to specify a cash concentration group when you create cash pools with the service provider Company - Time - Dependent. Only users who have been granted access to the assigned cash concentration group of a cash pool are authorized to perform cash concentration for this cash pool.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Search | Choose Configure Your Solution. |  |  |
| 4 | Application and Subapplication Area | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the following row:Item Name: Cash Operations | Configuration steps are displayed for the selected row. |  |
| 6 | Select Configuration Steps | Choose Configure to configure the following row.Step Name: Define Cash Concentration Groups for Cash Pools | The Define Cash Concentration Groups for Cash P..:Change view displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Create Concentration Group | Make the following entries and choose Save.Conc.Grp.: for example, ZCCADescription: for example, Concentration Group A | The concentration group for cash concentration is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Define Concentration Group for Cash Concentration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Cash Concentration Groups for Cash Pools.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Cash Concentration Groups for Cash P..:Change view displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Create Concentration Group | Make the following entries and choose Save.Conc.Grp.: for example, ZCCADescription: for example, Concentration Group A | The concentration group for cash concentration is defined. |  |

#### Create Bank Accounts (Optional)

Purpose

In this activity, you create bank accounts which are used in cash pools.

Procedure

For more information, see the Create Bank Account step in the Advanced Bank Account Management ([J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77)) test script.

|  |
| --- |
| Note To structure a multilevel cash pooling scheme, you need to create additional bank accounts (such as Bank Account A, Bank Account B, and so on). |

#### Set Up Bank Determination for Payment Transactions

Purpose

In this step, you make settings that the payment program uses to select the banks or bank accounts from which payment is to be made.

|  |
| --- |
| Note If you create new bank accounts, you need to perform this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Accounts Payable | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Automatic Payments. | The configuration steps for the selected row display. |  |
| 6 | Select Configuration Steps | In the Set Up Bank Determination for Payment Transactions row, choose Configure. | The Display View “Bank Selection”: Overview view displays. |  |
| 7 | Select Paying Company Code | Select the paying company code (for example, 3310 ), then in the Dialog Structure pane, double-click Bank Accounts. | The Change View“Bank Accounts”: Overview view displays. |  |
| 8 | New Entries | Choose New Entries. |  |  |
| 9 | Set Up Bank Determination | Make the following entries and choose Save:House bank: <house bank from previous step>Pymt Meth.: <payment method>Currency: for example, AEDAccount ID: <house bank account ID you created in previous step>Bank subaccount: <G/L account (existing or new)> | Bank determination for payment transactions has been defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Bank Determination for Payment Transactions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Bank Determination for Payment Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View“Bank Selection”: Overview screen displays. |  |
| 3 | Select Paying Company Code | Select the paying company code (for example, 3310), then in the Dialog Structure pane, double-click Bank Accounts. | The Change View“Bank Accounts”: Overview view displays. |  |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Set Up Bank Determination | Make the following entries and choose Save:House bank: <house bank from previous step>Payment method: <payment method>Currency: for example, AEDAccount ID: <house bank account ID you created in previous step>Bank subaccount: <G/L account (existing or new)> | Bank determination for payment transactions has been defined. |  |

#### Define Clearing Accounts for Receiving Bank for Account Transfer

Purpose

In this step, you define the clearing accounts for incoming bank transfers.

|  |
| --- |
| Note If you create new bank accounts, perform this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Cash Operations. | The Configuration Steps for the selected row display. |  |
| 6 | Select Configuration Steps | For the Define Clearing Accts for Receiving Bank for Acct.Transfer row, choose Configure. | The Change View“Acct Transfer:Determine Receiving Bank’s Clearing Account screen displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define Clearing Accounts | Make the following entries and choose Save.CoCode: for example, AEHouse Bk: <house bank ID you created in previous step>Clrg acct: <G/L account (existing or new)> | The clearing accounts for the receiving bank for account transfer is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Clearing Accts for Receiving Bank for Acct.Transfer | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Clearing Accts for Receiving Bank for Acct.Transfer.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View“Acct Transfer:Determine Receiving Bank’s Clearing Account screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define Clearing Accounts | Make the following entries and choose Save.CoCode: for example, AEHouse Bk: <house bank ID you created in previous step>Clrg acct: <G/L account (existing or new)> | The clearing accounts for the receiving bank for account transfer is defined.<G/L account (existing or new)> |  |

#### Define Clearing Accounts for Outgoing Bank Transfers

Purpose

In this step, you define the clearing accounts for outgoing bank transfers.

|  |
| --- |
| Note If you create a new bank accounts, you need to perform this step. |

Prerequisites

Bank accounts have been created in the system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Cash and Liquidity Management | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Cash Operations. | The Configuration Steps for the selected row display. |  |
| 6 | Define Account Determination | On the Define Account Determination for Bank Clearing Accounts row, choose Configure. | A dialog box displays. |  |
| 7 | Select Paying Company code | Make the following entries and press Enter:Paying company code: for example, 3310 | The Change View“Account Determination for G/L Account Payments”: Overview displays. |  |
| 8 | New Entries | Choose New Entries. |  |  |
| 9 | Define Account Determination | Enter the following data and choose Save.House Bk: <house bank from previous step>PM: <payment method>Crcy: for example, AEDAcct ID: <house bank account ID from previous step>Bank subacct: <G/L account (existing or new)> | The clearing accounts for outgoing bank transfers is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Account Determination for Bank Clearing Accounts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select Paying Company code | Make the following entries and press Enter:Paying company code: for example, 3310 | The Change View“Account Determination for G/L Account Payments”: Overview displays. |  |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Define Account Determination | Enter the following data and choose Save.House Bk: <house bank from previous step>PM: <payment method>Crcy: for example, AEDAcct ID: <house bank account ID from previous step>Bank subacct: <G/L account (existing or new)> | The clearing accounts for outgoing bank transfers is defined. |  |

## Overview Table

This test script consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Cash Pools (Version2)](#unique_18) [page ] 23 | Cash Management Specialist | Manage Cash Pools (Version 2) (F3266A) | Cash Pool is created successfully. |
| [Display Cash Pool Hierarchies](#unique_19) [page ] 26 | Cash Management Specialist | Display Cash Pool Hierarchies (F6123) | Cash Pools Hierarchies display. |
| [Option 1: Perform Cash Concentration](#unique_20) [page ] 28 | Cash Management Specialist | Manage Cash Concentration (F3265) | A cash concentration is generated. |
| [Option 2: Schedule Jobs for Cash Concentration (Optional)](#unique_21) [page ] 31 | Cash Management Specialist | Schedule Jobs for Cash Concentration (F3688) | Jobs for cash concentration are executed. |
| [Cash Pool Transfer Report](#unique_22) [page ] 34 | Cash Management Specialist | Cash Pool Transfer Reports (W0129) | Transfer amount between header accounts and sub-accounts displays. |

## Test Procedures

### Manage Cash Pools (Version2)

Purpose

In this step, you can define, display, change, and delete cash pools. A cash pool consists of a header account and one or more subaccounts. The assignment of the header account and subaccounts to the cash pool is always done for a specific validity period. You can assign bank accounts with currencies other than the header account currency as subaccounts to cash pools (multi-currency cash pool). In addition, it is possible to add a bank account as a header account to a cash pool, even if the account is already used as a subaccount in another cash pool. This allows you to create multi-level cash pool hierarchies.

You can define three kinds of cash pools, besides the classic cash pools managed by your bank, you can also create in-house cash pools for your in-house bank accounts of Advanced Payment Management application and cash pools managed by your company.

The different types of cash pools are used as follows:

- For cash pools managed by your bank and in-house cash pools, you can analyze the cash position calculated based on the cash position profiles in the Short-Term Cash Positioning (F5380) app using cash pool data as the data source.
- The in-house cash pools are also relevant for the internal cash pooling of the Advanced Payment Management application. For more information, see also [Internal Cash Pooling](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b8e68a90bfff4ff0906d5db5342bdece/9887ef90a39c40a1bbedaee389b50e33.html?state=DRAFT).
- For cash pools managed by your company, you can perform cash concentration using the Manage Cash Concentration Manage Cash Concentration (F3265) app.

Example Cash Pool Hierarchy with multi-level cash pools:

Cash pool 1: Header account = Bank account A with Subaccount = Bank account B

Cash pool 2: Header account = Bank account B with Subaccount = Bank account C

Cash pool 3: Header account = Bank account C with Subaccount = Bank account A -> This assignment is not allowed because bank account A is already the header account in cash pool 1.

|  |
| --- |
| Note There are two sample bank accounts provided:Bank account 0000000693123456 in bank key 18121976, corresponding house bank/account ID is AEBK1/AEAC1.Bank account 0000000693123456 in bank key 18121986, corresponding house bank/account ID is AEBK2/AEAC2.If you want to create multi-level cash pools, the related bank accounts need to be created. |

Prerequisite

You have defined authorization group for cash pool and assign to the relevant business role in the preliminary step. The authorization groups can be used to restrict the access to cash pools and cash position data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cash Pools (Version 2) (F3266A). | The Manage Cash Pools view displays.Note This app contains in-app help for key fields and concepts. To display the help while working in the app, press F1 or choose the question mark displayed in the app header. |  |
| 3 | Create Cash Pool | Choose Create. In the New Cash Pool dialog box, make the following entries and choose Create:Cash Pool Name: CP_1Service Provider: for example: Company - Time - DependentAuthorization Group: ZCP1 |  |  |
| 4 | Maintain General Information | Cash Pool Desc.: <cash pool description>, for example, Cash Pool 1 for companyTransfer Direction: for example, Both DirectionsNote This setting controls which transfers between the subaccounts and the header account in a cash pool are allowed.Profile Name: <Bank Account Balance profile created in Preliminary Steps>, for example, ZCP_GENNoteBank Account Balance profile only can be used in a cash pool with service provider Company - Time - Dependent.You assign a bank account balance profile to the cash pool that you want to use in cash concentration.Concentration Group: for example, ZCCANote Only users who have been granted access to the assigned cash concentration group of a cash pool are authorized to perform cash concentration for this cash pool. | The Cash Pool view displays. |  |
| 5 | Maintain Header Account Assignment | In the Header Account Assignment section, choose Create and enter the following data:Technical ID: <Technical ID for bank account> section, enter the following data:Account Number: for example, <Bank Account A>Valid From: <Current date>Valid To: <change as needed>In the Payment Method section, enter the data, for example, T | Header Account is maintained.NoteFor each cash pool, you assign one header account and one or more subaccounts.You cannot change the header account of a cash pool.A bank account can be assigned to both a cash pool as a header account and another cash pool as a subaccount at the same time.The currency of the subaccounts can differ from the currency of the header account. |  |
| 6 | Maintain Subaccount Assignment | In the Subaccount AssignmentItem 1) subaccount 1 for cash pool 1Technical ID: <Technical ID for bank account>Account Number: for example, <Bank Account B>Valid From: <Current date>Valid To: <change as needed>Target Balance: <as needed>Maximum Transfer Amount: <as needed>Minimum Transfer Amount: <as needed>Payment Method: for example, TItem 2) subaccount 2 for cash pool 1Technical ID: <Technical ID for bank account>Account Number: for example, <Bank Account D>Valid From: <Current date>Valid To: <change as needed>Target Balance: <as needed>Maximum Transfer Amount: <as needed>Minimum Transfer Amount: <as needed>Payment Method: for example, T | Subaccount is maintained.Note Note You can assign bank accounts with currencies other than the header account currency as subaccounts to cash pools (multi-currency cash pool). |  |
| 7 | Save | Choose Save. |  |  |
| 8 | Delete Cash Pool (Optional) | Choose Delete. | The cash pool is deleted. |  |
| 9 | Create Cash Pool - Service Provider Bank (Optional) | Note For single layer cash pool, skip this step.For multilevel cash pooling, repeat step 3-7 with the following information to create cash pools with service provider Bank - Time - Dependent:Cash Pool Name: for example, CP_2,CP_B,CP_3Service Provider: for example, Bank - Time - DependentCash Pool Desc.: <cash pool description>, for example, Cash Pool XX for BankNoteYou maintain the account assignment (Header account and Subaccount) per your business requirement.You can use the bank accounts assigned to a cash pool of service provider Company - Time - Dependent in other cash pools. No cross-cash pool checks are performed in this case.You must not assign a bank account as a subaccount that is already assigned as a header account in a cash pool within the same cash pool hierarchy. | One or more cash pools with service provider Bank are created. |  |

### Display Cash Pool Hierarchies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can view the cash pool hierarchies defined for cash pools with the service provider Bank - Time - Dependent and In-House Bank - Time - Dependent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Display Cash Pool Hierarchies (F6123). | The Display Cash Pool Hierarchies view displays. |  |
| 3 | Display Cash Pool Hierarchies | Enter the following data and choose Go:Key Date: <current date>Cash Pool Name: <empty>Company Code: <empty>Account Number: <empty> | Note Cash pools that have the service provider Company - Time - Dependent is not supported. |  |
| 4 | Navigate to Cash Pool | Choose the highlighted cash pool name to navigate to Manage Cash Pools (Version 2). | The Cash Pool view displays. |  |
| 5 | Export Cash Pool Hierarchies | Choose Export table to export cash pool hierarchies. | The Cash Pool hierarchies are exported. |  |

### Manage Cash Concentration

Purpose

You can perform cash concentration for cash pools with the service provider Company - Time - Dependent that are defined in the  Manage Cash Pools (Version 2) (F3266A) app. With this feature, you can move funds between the header account and subaccounts based on system proposals.

|  |
| --- |
| Note For cash pools that have the service provider Bank - Time - Dependent and In-House Bank - Time - Dependent, the balances of subaccounts are automatically aggregated to their header accounts to simulate the zero balancing cash pools operated by banks. For more information, see the Short Term Cash Positioning procedure in the Advanced Cash Operations (J78) test script. |

|  |
| --- |
| Note For multi-level cash pools, please perform cash concentration from the lowest level cash pools to the highest level cash pool. This ensures the best result of cash concentration.When you perform cash concentration for a multi-level cash pool, the following rules apply to the child cash pools:For child cash pools that have the service provider Bank - Time - Dependent, the system simulates cash concentration and uses the results in upper-level cash pools. The bank account balance profile defined for the highest level cash pool will be used for all child cash pools of that category.For child cash pools that have the service provider Company - Time - Dependent, the system does not take these child cash pools into consideration for cash concentration. |

Prerequisites

You have set the option Enable New Cash Concentration Model and selected a balance type in Preliminary Steps.

If you have selected available balance or value date balance as the balance type to use, ensure all the bank accounts involved already have balance data in the  Manage Bank Account Balances (F5175) app.

To ensure you use the most up-to-date balance data for cash concentration, perform cash flow reconciliations between intraday bank statement flows and forecasted cash flows for all involved bank accounts using the Reconcile Cash Flows app before you perform cash concentration. For more information, see the Reconcile Cash Flows step in the Advanced Cash Operations (J78) test script.

Make user the cash concentration group is assigned to a business role (for example, SAP_BR_CASH_SPECIALIST) in Preliminary Steps. Only the user with this business role can choose the relevant cash pools which is assigned to the concentration group to create cash concentration.

|  |
| --- |
| NoteCross-company code bank transfer is not supported in preconfigured content. You need to define clearing account between company codes via configuration activity: 100297Cross countries with different withholding tax is not supported. |

#### Option 1: Perform Cash Concentration

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cash Concentration (F3265). | Note This app contains in-app help for key fields and concepts. To display the help while working in the app, press F1 or choose the question mark displayed in the app header. |  |
| 3 | Create Cash Concentration | Choose Create. | The Cash Concentration view displays. |  |
| 4 | Specify Cash Pool | Choose Specify Cash Pool at the up right corner. Make the following entries and choose Specify Cash Pool in the dialog box.Cash Pool Name: for example, CP_1Note You can perform cash concentration for cash pools with the service provider Company - Time - Dependent that are defined in the Manage Cash Pools (Version 2) (F3266A) app.Exchange Rate Type: MPlan Date: <Today or future date> | The Cash pool attributes are automatically derived from cash pool master data. |  |
| 5 | View Header Information | Use Subaccount PM: for example, <selected>Note With this indicator set, the payment method of the subaccount is used to generate payment requests, irrespective whether the transfer is from the subaccount or to the subaccount. |  |  |
| 6 | View and Maintain Bank Accounts | In the Bank Accounts section, change following entries of a sub bank account per your needed:Transfer Amount: <default value or other value>NoteYou can use Clear Transfer Amount button to clear in one go all transfer amounts proposed by the system.Value Date: <default value or other value>Note Each Value Date indicates based on which date you are going to create a payment request for each of the sub bank accounts (sweeping upward or down) in the cash concentration. By default, it's populated as same as the Plan Date. You are allowed to manually change it. Header account doesn't have value date.Reference Text: <default>Single Payment: <selected as needed>Note This indicator specifies that the payment request is paid separately during automatic payment transactions.Enable Payments: <selected>Note By setting this option, the system will automatically make payments for payment requests generated from the cash concentration and clear the payment requests. You can use Enable Payments button to clear the payment in one go. | This section gives you an overview of the header account and all subaccounts of this cash pool. If a subaccount works also as the header account of a child cash pool, the cash pool information is displayed. |  |
| 7 | View Simulation Results | In the Simulation Results section, review the simulation results and adjust the transfer amounts where necessary. | If there are child cash pools under this pool, you can see simulated cash transfer logs in this section. The simulation results explain how the Balance Before figures of the child cash pools are calculated.NoteIn general, the system calculates and proposes transfer amounts following the equation below:Transfer Amount = Target Balance - Balance BeforeThe Balance Before field shows the current bank account balance before cash concentration. It is calculated as follows:Balance Before = Opening bank account balance + Forecasted cash flows |  |
| 8 | Create Payment Request | Choose Create. If dialog box appears, choose Create to confirm it. | The system creates payment requests accordingly and generates an ID for the cash concentration. |  |
| 9 | Review Application Log | In the Application Log section, check detailed log. | The log displays. |  |
| 10 | Check Payment Request status | In the Bank Accounts section, click the Payment Request number of a subaccount to navigate to Make Bank Transfers (F0691) app. In this app, you can check payment request status and view detailed information in Application Log.NoteIf Release and Pay is selected, the payment request should be Cleared. If payment request stays in Released status, meaning payment document is not successfully generated during the payment run. You can check payment run information in application log facet in Make Bank Transfer app, then further check the detailed payment log in Automatic Payment Transactions for Payment Requests (F111) app.If Release and Pay is not selected, the payment request status should be Released. You should pay the payment request in Make Bank Transfers (F0691) app. | The Make Bank Transfers view displays.Note The payment request should be cleared. If payment request stays in Released status, meaning payment document is not successfully generated during the payment run. You can check payment run information in application log facet in Make Bank Transfers (F0691) app, then further check the detailed payment log in Automatic Payment Transactions for Payment Requests (F111) app.Ater correction, you should pay the payment request in Make Bank Transfers (F0691) app. |  |

#### Option 2: Schedule Jobs for Cash Concentration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Alternatively, you can schedule jobs for cash concentration using the template and scheduling options provided. You can define jobs for each cash pool and check the status of your cash concentration jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Cash Concentration (F3688). |  |  |
| 3 | Create a New Application Job | Choose Create. | The New Job: Cash Concentration view displays. |  |
| 4 | Choose Job Template | Make the following entries:Job Template: Cash ConcentrationJob Name: Cash Concentration | Template is selected. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>Note If you choose start immediately, you don't need to maintain other parameters.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: OptionalOn Non-Working Day: OptionalCalendar: for example, Germany(Standard)Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Maintain Parameter | Choose Step 3. In the Parameter section, enter the following data:Cash Pool Name: <cash pool>Note Only the cash pool with service provider Company - Time - Dependent can be selected. If you keep parameters empty, that means all cases will be included in the job.Exchange Rate Type: For example, MEnable Payments: SelectedNote By setting this option, the system will automatically make payments for payment requests generated from the cash concentration job and clear the payment requests. | Parameters are maintained. |  |
| 7 | Check | Choose Check. |  |  |
| 8 | Schedule | Choose Schedule. |  |  |
| 9 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the job log. | Job log displays. You can check the cash concentraton ID and payment requests. |  |
| 10 | Check Cash Concentration | If a cash concentration is generated, you can use App Manage Cash Concentration (F3265) to check the relevant cash concentration. |  |  |
| 11 | Check Payment Request | If a payment request is generated, you can use App Make Bank Transfers (F0691) to check the relevant payment request. | Note The payment request status is Cleared when Make Payments is enabled in the parameters. Otherwise it remains Released and you must pay the payment request later. |  |

### Cash Pool Transfer Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can get a daily report of cash transfers in a cash pool. You can then track the concentration amounts between header accounts and sub-accounts in a specified period of time.

Prerequisites

You have performed cash concentration in the Manage Cash Concentration (F3265) app. After payments have been made, you are able to see the cash pool transfers in this report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Pool Transfer Reports (W0129). |  |  |
| 3 | Enter Filter | Make the following entries, and choose Go.Start Date: <Start Date>End Date: <End Date>Cash Pool Name: <Your cash pool name>Certainty Level: <Acutal or/and SI_CIT> | Transfer amount between header accounts and sub-accounts displays. |  |

## Appendix

### Process Chains

The process to be tested in this test case is part of a chain of integrated processes.

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
- see-also :: [[05-treasury-and-cash-management/test-script-liquidity-planning-3l5-ae-953]]
- see-also :: [[05-treasury-and-cash-management/test-script-advanced-bank-statement-automation-4x8-1056]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,719 chars in the whole document
