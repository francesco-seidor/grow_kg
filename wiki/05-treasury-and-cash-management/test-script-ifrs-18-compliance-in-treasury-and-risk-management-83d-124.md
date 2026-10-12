---
id: 05-treasury-and-cash-management/test-script-ifrs-18-compliance-in-treasury-and-risk-management-83d-124
title: "Test Script: IFRS 18 Compliance in Treasury and Risk Management (83D) (83D_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP scope item 83D: configure IFRS 18 AAR substitution rules and functional areas in TRM, then check position indicator and posting journal."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/ifrs-18-in-treasury]
aliases: [83D_S4CLD2608_BPD_EN_XX]
keywords: [IFRS 18 Presentation in Treasury and Risk Management, ifrs 18 compliance, treasury and risk management, account assignment references, substitution rules, functional area, position indicator, treasury posting journal, exposure subitems, scope item activation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/83D_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1245
topic: 05-treasury-and-cash-management/ifrs-18-in-treasury
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: IFRS 18 Compliance in Treasury and Risk Management (83D) (83D_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/83D_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **IFRS 18 Presentation in Treasury and Risk Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | IFRS 18 Compliance in Treasury and Risk Management (83D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232792190)

[2 Prerequisites 3](#_Toc232792191)

[2.1 System Access 3](#_Toc232792192)

[2.2 Roles 3](#_Toc232792193)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232792194)

[2.4 Business Conditions 4](#_Toc232792195)

[2.5 Preliminary Steps 5](#_Toc232792196)

[2.5.1 Define Account Assignment Reference Substitution Rules for OTC Transactions 5](#_Toc232792197)

[2.5.2 Define Account Assignment Reference Substitution Rules for Securities 8](#_Toc232792198)

[2.5.3 Define Account Assignment Reference Substitution Rules for Exposure Subitems 14](#_Toc232792199)

[2.5.4 Maintain Additional Account Assignments to Account Assignment References 15](#_Toc232792200)

[3 Overview Table 19](#_Toc232792201)

[4 Test Procedures 20](#_Toc232792202)

[4.1 Check Position Indicator 20](#_Toc232792203)

[4.2 Check Posting Journal 22](#_Toc232792204)

## Purpose

Overview

IFRS 18 becomes effective on 1 January 2027. Under IFRS 18, profit and loss postings, including those from Treasury and Risk Management (TRM), should be classified into Operating, Investing, or Financing to meet the new subtotals and categorization requirements. Please refer to SAP Note [3694359](https://me.sap.com/notes/3694359) for guidance on implementing IFRS 18 Financial Reporting in SAP S/4HANA Cloud Public Edition, with particular attention to the Treasury and Risk Management (TRM) .

To accelerate your journey to IFRS 18 compliance for managing treasury and risk management transactions, this Central Business Configuration (CBC) only scope item is designed.

By activating this scope item, you can leverage the refence configurations for IFRS 18 compliance based on the functional area approach, which include:

- New Account Assignment References (AARs) that carry IFRS 18 categorization.
- Account determination entries that map existing account symbols to existing G/L accounts via those new AARs.

Before activating this scope item, a careful evaluation of your TRM customization extent and project timeline is highly recommended. You can leverage this scope item when one of the following conditions applies:

- Existing TRM Environment: TRM is already in productive use and predominantly based on SAP TRM reference content, for example, account assignment references (AAR), G/L accounts, and account determinations are consistent with or closely aligned with the reference content.
- New or In-Progress Implementation: The TRM implementation (including non-IFRS 18 settings) has not yet started, or is in progress but is not yet live at the time of the scope item release, and with a clear intention to predominantly use SAP reference content.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |
| Valuation Area | 002 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |
| 1X7 - Debt and Investment Management – Group Ledger IFRS or1X9 - Foreign Currency Risk Management – Group Ledger IFRS or1XB - Interest Rate Derivatives Management – Group Ledger IFRS or1XD - Hedge Accounting for FX Forward – Group Ledger IFRS or2HU - Intercompany Foreign Exchange – Group Ledger IFRS or2OI - Intercompany Debt and Investment Mgmt – Group Ledger IFRS or2O2 - Bank Guarantee Management – Group Ledger IFRS or2RW - Hedge Accounting for FX Option – Group Ledger IFRS or2UF - Hedge Accounting for FX Swap – Group Ledger IFRS or2UO - Money Market Mutual Fund Management – Group Ledger IFRS or3WZ - Bond Management – Group Ledger IFRS or49E - Letter of Credit Management – Group Ledger IFRS or5OE - Stock Management – Group Ledger IFRS or5WG - Shareholding Management – Group Ledger IFRS or6B6 - Asset-Backed Securities Management – Group Ledger IFRS or6NE - Securities Option Management – Group Ledger IFRS | At least one of the TRM scope items for group ledger IFRS should be activated before you can choose to activate scope item 83D - IFRS 18 Compliance in Treasury and Risk Management. |

### Preliminary Steps

#### Define Account Assignment Reference Substitution Rules for OTC Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the Account Assignment Reference (AAR) substitution rules for OTC Transactions. Choose the IFRS 18 specific reference AARs that include the category in their IDs and descriptions depending on the economic nature of the transactions.

|  |
| --- |
| Note The following procedure describes the steps for maintaining account assignment reference substitution rule for money market transactions of product category 550 as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Account Assignment References - OTC Transactions (F7683). | The Manage Substitution and Validation Rules screen displays. |  |
| 3 | Create Rule | Choose Create Rule, enter the following data in the dialog box and choose Create:Business Context: OTC Transaction – Account Assignment ReferencesEvent: OTC Transaction – Account Assignment ReferencesRule Type: Substitution Rule | The New Substitution Rule screen displays. |  |
| 4 | Enter General Information | In the General Information subarea, enter the following data:Rule Name: for example, Z550_IFRS18Description: for example, IFRS 18 AAR for 550 |  |  |
| 5 | Enter Precondition | In the Precondition subarea, enter the following data:Field/FunctionOperatorValueFinancialInstrProductCategoryEqual To550FinancialInstrTransactionTypeEqual To100TreasuryValuationAreaEqual To002TreasuryValuationClassBetween10 And 18BPCoCodeCompanyRelationshipEqual To3 |  |  |
| 6 | Enter Substitution | In the Substitution subarea, enter the following data, and choose Save:Target Field: TreasuryGLAccountAssignmentRefSubstitution Type: Substitute with ConstantSource: for example, 201101000000 |  |  |
| 7 | Activate Rule | Choose Activate on the up right side of the screen to activate the rule. | The status of the rule becomes Active. |  |

Continue to maintain AAR substitution rules for other OTC transactions based on the scope items activated in your system.

Below are the configuration examples with pre-delivered content.

| Rule Name | Description | Field/Function | Operator | Value | Target Field | Substitution Type | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Z76JIFRS18 | IFRS 18 AAR for 76J | FinancialInstrumentProductType | Equal To | 76J | TreasuryGLAccountAssignmentRef | Substitute with Constant | 217001000000 |
| FinancialInstrTransactionType | Equal To | 100 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |
| Z60AIFRS18 | IFRS 18 AAR for 60A | FinancialInstrumentProductType | Equal To | 60A | TreasuryGLAccountAssignmentRef | Substitute with Constant | 004001000000 |
| FinancialInstrTransactionType | Equal To | 101 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |
| Z62AIFRS18 | IFRS 18 AAR for 62A | FinancialInstrumentProductType | Equal To | 62A | TreasuryGLAccountAssignmentRef | Substitute with Constant | 006001000000 |
| FinancialInstrTransactionType | Equal To | 301 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |
| Z85AIFRS18 | IFRS 18 AAR for 85A | FinancialInstrumentProductType | Equal To | 85A | TreasuryGLAccountAssignmentRef | Substitute with Constant | 012113000000 |
| FinancialInstrTransactionType | Equal To | 100 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |
| Z86AIFRS18 | IFRS 18 AAR for 86A | FinancialInstrumentProductType | Equal To | 86A | TreasuryGLAccountAssignmentRef | Substitute with Constant | 009103000000 |
| FinancialInstrTransactionType | Equal To | 100 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |
| ZHAIFRS18 | IFRS 18 AAR for Hedge Accounting Operat. | FinancialInstrumentProductType | Equal To | 60A | TreasuryGLAccountAssignmentRef | Substitute with Constant | 004103000000 |
| HedgingClassification | Equal To | YFC00 |  |  |  |  |  |
| TreasuryValuationArea | Equal To | 002 |  |  |  |  |  |

#### Define Account Assignment Reference Substitution Rules for Securities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the Account Assignment Reference (AAR) substitution rules for securities transactions. Choose the IFRS 18 specific reference AARs that include the category in their IDs and descriptions depending on the economic nature of the transactions.

|  |
| --- |
| Note The following procedure describes the steps for maintaining account assignment reference substitution rule for money market fund transactions of product category 020 as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Account Assignment References - Securities (F7684). | The Manage Substitution and Validation Rules screen displays. |  |
| 3 | Create Rule | Choose Create Rule, enter the following data in the dialog box and choose Create:Business Context: Securities – Account Assignment ReferencesEvent: Securities – Account Assignment ReferencesRule Type: Substitution Rule | The New Substitution Rule screen displays. |  |
| 4 | Enter General Information | In the General Information subarea, enter the following data:Rule Name: for example, Z020_IFRS18Description: for example, IFRS 18 AAR for 020 |  |  |
| 5 | Enter Precondition | In the Precondition subarea, maintain the enter the following data:Field/FunctionOperatorValueFinancialInstrProductCategoryEqual To020TreasuryValuationAreaEqual To002SecurityClassFundTypeEqual To1 |  |  |
| 6 | Enter Substitution | In the Substitution subarea, enter the following data, and choose Save:Target Field: TreasuryGLAccountAssignmentRefSubstitution Type: Substitute with ConstantSource: for example, 210101000000 |  |  |
| 7 | Activate Rule | Choose Activate on the up right side of the screen to activate the rule. | The status of the rule becomes Active. |  |

Continue to maintain AAR derivations for other Securities transactions based on the scope items activated in your system.

Below are the configuration examples with pre-delivered content.

| Rule Name | Description | Field/Function | Operator | Value | Target Field | Substitution Type | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Z04A_IFRS18_L_3 | Bond Invest., LT, Unaff.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAc-countAssignmentRef | Substitute with Constant | 211101000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 3 |  |  |  |  |  |
| Z04A_IFRS18_L_2 | Bond Invest., LT, Aff. no con.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 211121000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 2 |  |  |  |  |  |
| Z04A_IFRS18_L_1 | Bond Invest., LT Aff. con.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 211111000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 1 |  |  |  |  |  |
| Z04A_IFRS18_S_3 | Bond Invest., ST, Unaff.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 211201000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 3 |  |  |  |  |  |
| Z04A_IFRS18_S_2 | Bond Invest., ST, aff. no con.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 211221000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 2 |  |  |  |  |  |
| Z04A_IFRS18_S_1 | Bond Invest., ST, aff. con.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 211211000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 1 |  |  |  |  |  |
| Z04L_IFRS18_L_3 | IL Bond Invest., LT, Unaff.(IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218101000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 3 |  |  |  |  |  |
| Z04L_IFRS18_L_2 | IL Bond Invest., LT, Affil, no con. (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218121000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 2 |  |  |  |  |  |
| Z04L_IFRS18_L_1 | IL Bond Invest., LT, Affil, con. (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218111000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 1 |  |  |  |  |  |
| Z04L_IFRS18_S_3 | IL Bond Invest., ST, Unaffil. (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218201000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 3 |  |  |  |  |  |
| Z04L_IFRS18_S_2 | IL Bond Invest., ST, Affil. no con. (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218221000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 2 |  |  |  |  |  |
| Z04L_IFRS18_S_1 | IL Bond Invest., ST, Affil. con. (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 218211000000 |
| FinancialInstrumentProductType | Equal To | 04L |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 1 |  |  |  |  |  |
| Z04A_IFRS18_S_IS | Bond Issuance, LT (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 111102000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 15 and 19 |  |  |  |  |  |
| Z04A_IFRS18_l_IS | Bond Issuance, ST (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 111202000000 |
| FinancialInstrumentProductType | Equal To | 04A |  |  |  |  |  |
| TreasuryValuationClass | Between | 25 and 29 |  |  |  |  |  |
| ZABS_IFRS18_L | ABS Investment, LT (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 216101000000 |
| FinancialInstrumentProductType | Equal To | 042 |  |  |  |  |  |
| TreasuryValuationClass | Between | 10 and 14 |  |  |  |  |  |
| ZABS_IFRS18_S | ABS Investment, ST (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 216201000000 |
| FinancialInstrumentProductType | Equal To | 042 |  |  |  |  |  |
| TreasuryValuationClass | Between | 20 and 24 |  |  |  |  |  |
| ZSTOCK_IFRS18_OCI | Stock investment, Inv, others (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 212201000000 |
| FinancialInstrumentProductType | Equal To | 010 |  |  |  |  |  |
| TreasuryValuationClass | Equal To | 62 |  |  |  |  |  |
| ZSTOCK_IFRS18_PL | Stock investment, Inv, trading (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 212101000000 |
| FinancialInstrumentProductType | Equal To | 010 |  |  |  |  |  |
| TreasuryValuationClas | Equal To | 63 |  |  |  |  |  |
| ZSR_03A_IFRS18 | Subscription rights, Inv, (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 214001000000 |
| FinancialInstrumentProductType | Equal To | 030 |  |  |  |  |  |
| ZSH_16A_IFRS18_1 | Investment in subsidiary, Inv, (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 213001000000 |
| FinancialInstrumentProductType | Equal To | 160 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 1 |  |  |  |  |  |
| ZSH_16A_IFRS18_2 | Investment in Assoc./JV, Inv, (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 213101000000 |
| FinancialInstrumentProductType | Equal To | 160 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 2 |  |  |  |  |  |
| ZSH_16A_IFRS18_3 | Investment in non-aff. , Inv, (IFRS 18) | TreasuryValuationArea | Equal To | 002 | TreasuryGLAccountAssignmentRef | Substitute with Constant | 213201000000 |
| FinancialInstrumentProductType | Equal To | 160 |  |  |  |  |  |
| BPCompanyRelationship | Equal To | 3 |  |  |  |  |  |

#### Define Account Assignment Reference Substitution Rules for Exposure Subitems

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the Account Assignment Reference (AAR) substitution rules for Exposure Subitems.

|  |
| --- |
| Note The following procedure describes the steps for maintaining account assignment reference substitution rule for EX_SUBITEM_O Exposure Subitems, Operating (IFRS 18) as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Account Assignment References - Exposure Subitems (F7682). | The Manage Substitution and Validation Rules screen displays. |  |
| 3 | Create Rule | Choose Create Rule, enter the following data in the dialog box and choose Create:Business Context: Exposure Subitem - Account Assignment ReferencesEvent: Exposure Subitem - Account Assignment ReferencesRule Type: Substitution Rule | The New Substitution Rule screen displays. |  |
| 4 | Enter General Information | In the General Information subarea, enter the following data:Rule Name: for example, ZHASUBITEMIFRS18Description: for example, IFRS18 Hedge Accounting Exposure Subitem |  |  |
| 5 | Enter Precondition | In the Precondition subarea, maintain the enter the following data:Field/FunctionOperatorValueFinancialInstrumentProductTypeEqual To91ATreasuryValuationAreaEqual To002 |  |  |
| 6 | Enter Substitution | In the Substitution subarea, enter the following data, and choose Save:Target Field: TreasuryGLAccountAssignmentRefSubstitution Type: Substitute with ConstantSource: for example, EX_SUBITEM_O |  |  |
| 7 | Activate Rule | Choose Activate on the up right side of the screen to activate the rule. | The status of the rule becomes Active. |  |

#### Maintain Additional Account Assignments to Account Assignment References

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the functional area as the additional account assignment to account assignment reference for IFRS 18 compliance.

Through the mapping of the functional areas to new AARs at company code level, the functional area is populated in the Position Indicator and then propagated to the Universal Journal at the time of posting. The functional area from TRM takes precedence over that derived from G/L account master data or account assignments (e.g., cost center, WBS element).

|  |
| --- |
| Note The following procedure describes the steps for maintaining additional account assignments to account assignment reference for money market transactions of product category 550 as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Source Application Accounting | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Allocate Additional Account Assignments to Account Assignment References.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define New Additional Account Assignment | On the Allocate Additional Account Assignments to..:Change screen, choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter Details | On the New Entries: Details of Added Entries screen, enter the following entries, and choose Save:Company Code: for example, 1010Acct Assignment Ref.: for example, 201101000000Functional Area: for example, YB61 |  | 6 |

Continue to maintain additional account assignments for other account assignment references derived from TRM transactions or security positions based on the scope items activated in your system.

Below are the configuration examples with pre-delivered account assignment references and functional areas.

| Company Code | Acct Assignment Ref. | Functional Area |
| --- | --- | --- |
| 1010 | 201101000000 | YB61 |
| 1010 | 210101000000 | YB61 |
| 1010 | 217001000000 | YB61 |
| 1010 | 004001000000 | YB61 |
| 1010 | 006001000000 | YB61 |
| 1010 | 012113000000 | YB61 |
| 1010 | 216101000000 | YB61 |
| 1010 | 216201000000 | YB61 |
| 1010 | 211101000000 | YB61 |
| 1010 | 211111000000 | YB61 |
| 1010 | 211121000000 | YB61 |
| 1010 | 211201000000 | YB61 |
| 1010 | 211211000000 | YB61 |
| 1010 | 211221000000 | YB61 |
| 1010 | 218101000000 | YB61 |
| 1010 | 218111000000 | YB61 |
| 1010 | 218121000000 | YB61 |
| 1010 | 218201000000 | YB61 |
| 1010 | 218211000000 | YB61 |
| 1010 | 218221000000 | YB61 |
| 1010 | 111102000000 | YB62 |
| 1010 | 111202000000 | YB62 |
| 1010 | 212101000000 | YB61 |
| 1010 | 212201000000 | YB61 |
| 1010 | 214001000000 | YB61 |
| 1010 | 213001000000 | YB61 |
| 1010 | 213101000000 | YB61 |
| 1010 | 213201000000 | YB61 |
| 1010 | 009103000000 | YB60 |
| 1010 | 004103000000 | YB60 |
| 1010 | EX_SUBITEM_O | YB60 |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Check Position Indicator](#unique_12) [page ] 20 | Treasury Specialist - Back Office | Manage Financial Transactions (F6157) | Correct functional area is filled in the position indicator. |
| [Check Posting Journal](#unique_13) [page ] 22 | Treasury Specialist - Back Office | Display Treasury Posting Journal (F1755) | Interest income/expenses are accrued in valuation area 002 for ledger of IFRS. |

## Test Procedures

### Check Position Indicator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Through the mapping of the functional areas to new AARs (at company code level), the functional area is automatically filled in the Position Indicator and then propagated to the Universal Journal at the time of posting.

In this activity, you check in the Position Indicator of the transaction to see if the right functional area is automatically filled.

Prerequisites

You’ve created and settled the transactions with attributes that derive IFRS 18 AARs and functional areas.

Please refer to the relevant steps in the test script of the scope item below to create and settle transactions.

| Scope Items | Steps |
| --- | --- |
| 1WV - Debt and Investment Management | Create Debt or Investment ContractSet Settlement Status (Manual) |
| 1X1 - Foreign Currency Risk Management | Create Foreign Exchange ContractCreate FX Option ContractSet Settlement Status (Manual) |
| 1X3 - Interest Rate Derivatives Management | Create Interest Rate Swap ContractCreate Cross-Currency Interest Rate Swap ContractCreate Swaption ContractSet Settlement Status (Manual) |
| 2F2 - Intercompany Foreign Exchange Management |  |
| 2NZ - Bank Guarantee Management | Issue Bank GuaranteeReceive Bank GuaranteeSet Settlement Status |
| 1YI - Intercompany Process for Debt and Investment Mgmt |  |
| 2UN - Money Market Mutual Fund Management | Create Fund Purchase Transaction for Money Market FundSet Settlement Status (Manual) |
| 3WY - Bond Management | Create Placement TransactionCreate Bond Purchase TransactionSet Settlement Status (Manually) |
| 49D - Letter of Credit Management | Issue Normal Letter of CreditReceive Normal Letter of CreditIssue Standby Letter of CreditReceive Standby Letter of CreditSet Settlement Status |
| 5OD - Stock Management | Create Stock Purchase TransactionSet Settlement Status |
| 5WF - Shareholding Management | Create Shareholding Purchase TransactionSet Settlement Status (Manual) |
| 6B5 - Asset-Backed Securities Management | Create ABS/MBS Purchase TransactionSet Settlement Status (Manually) |
| 6ND - Securities Option Management | Create Securities Option ContractSet Settlement Status (Manually) |
| 1XD - Hedge Accounting for FX Forward – Group Ledger IFRS |  |

Procedure

Below are the steps for checking the position indicator for Money Market transactions, provided as an example.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Details:Key Date: <the current date>Company Code: for example, 1010Transaction: for example, <the money market transaction you created according to test script of 1WV> | The Display Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Check Position Indicator | On the Display Interest Rate Instrument: Structure screen, expand the menu list on the left side of the screen. Choose Environment > Position Indicator . | The Display Position Indicator view is displayed. |  |
| 5 | Confirm Functional Area | In the Subledger Position Indicator subarea, check the functional area in the Functional Area column. | The correct functional area is automatically filled in. |  |

### Check Posting Journal

Purpose

The functional area in the Position Indicator is propagated to the corresponding posting journals generated from TRM transactions and security positions.

In this activity, you check in the posting journal of the TRM transactions and security positions to see if the right functional area is automatically propagated.

Prerequisites

You have posted flows to parallel valuation area 002 for IFRS.

Refer to the test scripts of the following IFRS scope items for posting flows to parallel valuation area 002.

| Scope Item |
| --- |
| 1X7​ - Debt and Investment Management – Group Ledger IFRS​ |
| 1X9​ - Foreign Currency Risk Management – Group Ledger IFRS​ |
| 1XB​ - Interest Rate Derivatives Management – Group Ledger IFRS |
| 2HU​ - Intercompany Foreign Exchange – Group Ledger IFRS​ |
| 2O2 - Bank Guarantee Management – Group Ledger IFRS |
| 2OI​ - Intercompany Debt and Investment Mgmt – Group Ledger IFRS​ |
| 2UO​ - Money Market Mutual Fund Management – Group Ledger IFRS |
| 3WZ​ - Bond Management – Group Ledger IFRS |
| 49E​ - Letter of Credit Management – Group Ledger IFRS |
| 5OE​ - Stock Management – Group Ledger IFRS​ |
| 5WG​ - Shareholding Management – Group Ledger IFRS​ |
| 6B6​ - Asset-Backed Securities Management – Group Ledger IFRS |
| 6NE - Securities Option Management – Group Ledger IFRS |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, OTC TransactionsCompany Code: for example, 1010Valuation Area : 002Transaction: for example, <the transaction posted to 002>Note If the Transaction filter is not displayed, choose Adapt Filters to add it. | All documents posted to 002 related to the transaction are displayed. |  |
| 4 | Check Journal Entry | Click on one document number and choose Display Journal Entries – New Version to navigate to the details of the document. |  |  |
| 5 | Check Line Item | In the Line Items subarea, select one journal entry item to check its details. | The Line Item in Ledger View is displayed. |  |
| 6 | Check Functional Area | On the General Information tab, check the value in the Functional Area field. | The correct functional area is automatically filled in. |  |

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
- see-also :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/83D_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 38,842 chars in the whole document
