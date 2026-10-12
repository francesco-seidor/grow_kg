---
id: 17-leasing-and-real-estate/intercompany-process-for-sublease-accounting-2o9-test-script-sap-s-4ha
title: "Intercompany Process for Sublease Accounting (2O9) - Test Script, SAP S/4HANA Cloud Public Edition (2O9_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 2O9: intercompany sublease accounting (lease-out) under local GAAP (2SB), IFRS (2SA) and US GAAP (34O), with prerequisites and test steps."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/lease-out-sublease-and-sales-based-rent]
aliases: [2O9_S4CLD2608_BPD_EN_XX]
keywords: ["Lease-Out, Sublease and Sales-Based Rent Accounting", sublease accounting, intercompany lease-out, lease contract creation, valuation rules, periodic valuation posting, periodic posting, reverse contract postings, group ledger ifrs, group ledger us gaap]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O9_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-842
topic: 17-leasing-and-real-estate/lease-out-sublease-and-sales-based-rent
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Process for Sublease Accounting (2O9) - Test Script, SAP S/4HANA Cloud Public Edition (2O9_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O9_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Lease-Out, Sublease and Sales-Based Rent Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Process for Sublease Accounting (2O9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232842533)

[2 Prerequisites 5](#_Toc232842534)

[2.1 System Access 5](#_Toc232842535)

[2.2 Roles 5](#_Toc232842536)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232842537)

[2.4 Additional Manual Configuration 8](#_Toc232842538)

[2.5 Business Conditions 8](#_Toc232842539)

[2.6 Preliminary Steps 9](#_Toc232842540)

[2.6.1 Default Value for Tax Rate per Contract Type 9](#_Toc232842541)

[2.6.2 Assign Tax Codes 10](#_Toc232842542)

[2.6.3 Assign Tax Code (for FI Document) 12](#_Toc232842543)

[2.6.4 Prerequisites – Valuation Rule 13](#_Toc232842544)

[2.6.5 Prerequisites – Enter Index Level 15](#_Toc232842545)

[2.6.6 Prerequisites – Maintain Residence Time 18](#_Toc232842546)

[2.6.7 Define Question Catalogs 19](#_Toc232842547)

[2.6.8 Control Parameters Question Catalog 21](#_Toc232842548)

[2.6.9 Prerequisites – Define Output Parameter Determination – Invoice 23](#_Toc232842549)

[2.6.10 Prerequisites – Define Output Parameter Determination – General Letter 25](#_Toc232842550)

[2.6.11 Define Output Parameter Determination – Adjustment Letter 26](#_Toc232842551)

[2.6.12 Prerequisites – Define Permitted Superordinate Architecture Object Types 28](#_Toc232842552)

[3 Overview Table 30](#_Toc232842553)

[4 Test Procedures 34](#_Toc232842554)

[4.1 (2SB) Lease-Out for Sublease Accounting 34](#_Toc232842555)

[4.1.1 Contract Management 35](#_Toc232842556)

[4.1.1.1 Create Contract 35](#_Toc232842557)

[4.1.2 Contract Valuation 40](#_Toc232842558)

[4.1.2.1 Maintain Valuation Rule 40](#_Toc232842559)

[4.1.2.2 Valuation Posting 42](#_Toc232842560)

[4.1.2.2.1 Periodic Valuation Posting 42](#_Toc232842561)

[4.1.2.2.2 Reverse Valuation Posting 46](#_Toc232842562)

[4.1.3 Accounting 49](#_Toc232842563)

[4.1.3.1 Periodic Posting 49](#_Toc232842564)

[4.1.3.1.1 Periodic Posting - Simulation 49](#_Toc232842565)

[4.1.3.1.2 Periodic Posting - Update Run 50](#_Toc232842566)

[4.1.3.2 Reverse Contract Postings 52](#_Toc232842567)

[4.1.3.2.1 Reverse Contract Postings - Simulation 52](#_Toc232842568)

[4.1.3.2.2 Reverse Contract Postings - Update 54](#_Toc232842569)

[4.2 (2SA) Lease-Out for Sublease Accounting – Group Ledger IFRS 55](#_Toc232842570)

[4.2.1 Contract Management 55](#_Toc232842571)

[4.2.1.1 Create Contract 55](#_Toc232842572)

[4.2.2 Contract Valuation 60](#_Toc232842573)

[4.2.2.1 Maintain Valuation Rule 60](#_Toc232842574)

[4.2.2.2 Valuation Posting 62](#_Toc232842575)

[4.2.2.2.1 Periodic Valuation Posting 62](#_Toc232842576)

[4.2.2.2.2 Reverse Valuation Posting 66](#_Toc232842577)

[4.2.3 Accounting 69](#_Toc232842578)

[4.2.3.1 Periodic Posting 69](#_Toc232842579)

[4.2.3.1.1 Periodic Posting - Simulation 69](#_Toc232842580)

[4.2.3.1.2 Periodic Posting - Update Run 70](#_Toc232842581)

[4.2.3.2 Reverse Contract Postings 72](#_Toc232842582)

[4.2.3.2.1 Reverse Contract Postings - Simulation 72](#_Toc232842583)

[4.2.3.2.2 Reverse Contract Postings - Update 74](#_Toc232842584)

[4.3 (34O) Lease-Out for Sublease Accounting – Group Ledger US GAAP 75](#_Toc232842585)

[4.3.1 Contract Management 75](#_Toc232842586)

[4.3.1.1 Create Contract 75](#_Toc232842587)

[4.3.2 Contract Valuation 80](#_Toc232842588)

[4.3.2.1 Maintain Valuation Rule 80](#_Toc232842589)

[4.3.2.2 Valuation Posting 82](#_Toc232842590)

[4.3.2.2.1 Periodic Valuation Posting 82](#_Toc232842591)

[4.3.2.2.2 Reverse Valuation Posting 86](#_Toc232842592)

[4.3.3 Accounting 89](#_Toc232842593)

[4.3.3.1 Periodic Posting 89](#_Toc232842594)

[4.3.3.1.1 Periodic Posting - Simulation 89](#_Toc232842595)

[4.3.3.1.2 Periodic Posting - Update Run 90](#_Toc232842596)

[4.3.3.2 Reverse Contract Postings 92](#_Toc232842597)

[4.3.3.2.1 Reverse Contract Postings - Simulation 92](#_Toc232842598)

[4.3.3.2.2 Reverse Contract Postings - Update 94](#_Toc232842599)

## Purpose

Overview

This scope item allows the company to assign or give certain rights to the sublessee – an affiliate company – that are held under the terms of the own original lease with the landlord.

The company handles the sublease contract and related valuation under local GAAP, IFRS or US GAAP.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Contract Specialist - Leasing | SAP_BR_RECM_SPECIALIST | Leasing Contract Management / Leasing Contract Management - Sales-Based Rent | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |
| Contract Valuation Specialist - Leasing | SAP_BR_RECM_VALSPECIALIST | Leasing Valuation | SAP_BR_RECM_VALSPECIALIST |  |
| Accounts Receivable Accountant - Leasing | SAP_BR_RECM_AR_ACCOUNTANT | Accounts Receivable - Leasing | SAP_BR_RECM_AR_ACCOUNTANT |  |
| Administrator - Leasing | SAP_BR_RECM_ADMINISTRATOR | Administration - Leasing | SAP_BR_RECM_ADMINISTRATOR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

If the company code is generated through the Flex-Org tool as the lessee company code (1020), the related company should also be created and assigned to company code through the Flex-Org tool as a trading partner for consolidation. If the lessee company is generated by activation, the company is already created and assigned.

To create intercompany Business Partners manually, see Create Customer Master – MDS (BND) and Create Supplier Master – MDS (BNE) and also maintain Trading Partner in Control tab in Business Partner master data.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |
| Chart of Depreciation | 1010 |  |  |
| Customer | for example, 10401020 |  | 10401020: Customer in lessor Germany company code, for example 1010, representing the lessee Germany company code (for example, 1020). |
| Vendor | for example, 10401010 |  | Vendor in lessee Germany company code, for example 1020, representing the lessor Germany company code (for example, 1010). |
| Cost Center | any available cost center with company code relation, for example, CTR A000/10101101 |  |  |
| Profit Center | any available profit center, for example, YB600 |  |  |
| Functional Area | any available functional location, for example, YB40 |  |  |

To create intercompany Business Partner 10401020 manually, see Create Customer Master – MDS (BND) to maintain General Data view and Company Code view with below additional data.

| Tab: Field | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Control: Trading Partner | 1020 |  |  |
| Customer: Account Management: Reconciliation Acct | 12300000 |  |  |

To create intercompany Business Partner 10401010 manually, see Create Supplier Master – MDS (BNE) to maintain General Data view and Company Code view with below additional data.

| Tab: Field | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Control: Trading Partner | 1010 |  |  |
| Vendor: Account Management: Reconciliation Acct | 21300000 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNH | Create Profit Center - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| 7AD | Create Rental Object – MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/7314af0bd9f56fd7cfb099a63e8be14a)

### Business Conditions

Before this scope item can be tested, one of the following business conditions must be met.

If local GAAP is used, to execute inter-company scenario for sublease, scope item Lease-Out for Sublease Accounting (2SB) must be activated.

Please refer to chapter (2SB) Lease-Out for Sublease Accounting for the operations.

If group ledger IFRS is used, to execute inter-company scenario for sublease, scope item Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA) must be activated.

Please refer to chapter (2SA) Lease-Out for Sublease Accounting – Group Ledger IFRS for the operations.

If group ledger US GAAP is used, to execute inter-company scenario for sublease, scope item Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O) must be activated.

Please refer to chapter (34O) Lease-Out for Sublease Accounting – Group Ledger US GAAP for the operations.

To execute Lease-Out for Sublease Accounting (2SB), Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA) and Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O), the following business condition must be met respectively.

| Scope Item ID | Business Condition |
| --- | --- |
| 1T6 - Lease-In Accounting | Lease-in contract with external party must exist for (2SB) Lease-Out for Sublease Accounting. |
| 21P - Lease-In Accounting – Group Ledger IFRS | Lease-in contract with external party must exist for (2SA) Lease-Out for Sublease Accounting – Group Ledger IFRS. |
| 34N - Lease-In Accounting – Group Ledger US GAAP | Lease-in contract with external party must exist for (34O) Lease-Out for Sublease Accounting – Group Ledger US GAAP. |

For countries that do not deliver all these three scope items (Lease-Out for Sublease Accounting (2SB), Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA) and Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O)), please ignore the scope items that are not delivered.

### Preliminary Steps

#### Default Value for Tax Rate per Contract Type

Purpose

For each contract type, you specify the tax group and tax type that are proposed by the system when a contract is created. For contract types that aren't relevant for tax (internal contracts, G/L account contracts), you can also specify that these contract types are treated as tax exempt.

If you set the Tax Exempt indicator, the tax type and tax group aren't entered during the processing of contracts with this contract type. In that case, leave the Tax Type and Tax Group fields blank in this view. Otherwise, the cash flow generation would incorrectly use the tax type and tax group entered here.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Accounting Integration |  |  |
| 5 | Configure | In the Default Value for Tax Rate per Contract Type row, choose Configure. |  |  |
| 6 | Assign Tax Type and Tax Group | In the Default Tax Group column, verify or change your default tax group (for example, ).Choose Save.Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Default Value for Tax Rate per Contract Type | Go to the Business Processes Configuration app and search for the following activity: Default Value for Tax Rate per Contract Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Default Values for Tax Type/Group": Overview view is displayed. |  |
| 3 | Assign Tax Type and Tax Group | In the Default Tax Group column, verify or change your default tax group (for example, ).Choose Save.Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. |  |  |

#### Assign Tax Codes

Purpose

In this SSC-UI, you assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country-dependent and time-dependent.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Assign Tax Code | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Accounting Integration.Choose Configure in Assign Tax Codes row.Enter a tax code if it is blank.Choose Save.Note To change the Tax Code, choose the Display/Edit button, then select the magnifying glass in the cell you wish to change. | The tax code has been assigned to company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Tax Code Assignment | Go to the Business Processes Configuration app and search for the following activity: Tax Code Assignment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Code | Enter a tax code if it is blank.Choose Save.Note To change the Tax Code, choose the Display/Edit button, then select the magnifying glass in the cell you wish to change. | The tax code has been assigned to company code. |  |

#### Assign Tax Code (for FI Document)

Purpose

In this SSC-UI, you assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country-dependent and time-dependent.

You have to make this assignment in order for FI documents to be read correctly in RE. This assignment is relevant, for example, for service charge settlement and input tax distribution.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Assign Tax Type and Tax Group | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Accounting Integration.Choose Configure in Assign Tax Code (for FI Document) row.Enter Tax Type and Tax Group if they are blank (for example, Y2 and Y-NONE).Choose Save. | The tax code has been assigned to the company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Tax Code (for FI Document) | Go to the Business Processes Configuration app and search for the following activity: Assign Tax Code (for FI Document).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Type and Tax Group | Enter Tax Type and Tax Group if they are blank (for example, Y2 and Y-NONE).Choose Save. | The tax code has been assigned to the company code. |  |

#### Prerequisites – Valuation Rule

Purpose

Rental and lease contracts can be valuated according to different accounting principles. The accounting principles contain different rules regarding the way contracts are represented in accounting, and how the various contract conditions (periodic payments, one-time payments, service costs) are included in the valuation.

Multiple valuation rules are possible for each accounting principle. The valuation rules determine how the valuation for the respective accounting principle is calculated and to which ledgers or accounts the postings are made.

- Define how you want to model your valuation rules.
- Specify for which contract types the valuation rules are relevant.
- Define the company code in which valuation rules are to be applied.

You require separate valuation rules for vendor contracts (lease-in) and customer contracts (lease-out, including subletting).

If the accounting principle requires classification according to finance lease and operating lease, you need different valuation rules for these valuations.

If there is accounting principle not being used any more after ledger switch in General Ledger Accounting, the related valuation rule should be set as obsolete.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Set Valuation Rule to Obsolete | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Contract Valuation.Choose Configure in Valuation Rule row.Double-click the valuation rule whose assigned accounting principle is not used any more.Choose Obsolete.Choose Save.Note You may be prompted to enter a customizing request number. Select an existing customizing request or create a new one, then choose Continue. | The valuation rule has been set as obsolete. |  |
| 5 | Assign Ledger (Optional) | Enter the following field for the valuation rule whose assigned accounting principle is applied to multiple ledgers.Ledger: <Your Ledger>, for example, 0LChoose Save.Note You may be prompted to enter a customizing request number. Select an existing customizing request or create a new one, then choose Continue.Note You can check whether the accounting principle is assigned to more than one ledger via configuration activity: Assign Accounting Principles to Ledgers and Company Codes (103556). | The ledger has been assigned to the valuation rule. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Valuation Rule | Go to the Business Processes Configuration app and search for the following activity: Valuation Rule.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Set Valuation Rule to Obsolete | Double-click the valuation rule whose assigned accounting principle is not used any more.Choose Obsolete.Choose Save.Note You may be prompted to enter a customizing request number. Select an existing customizing request or create a new one, then choose Continue. | The valuation rule has been set as obsolete. |  |
| 4 | Assign Ledger (Optional) | Enter the following field for the valuation rule whose assigned accounting principle is applied to multiple ledgers.Ledger: <Your Ledger>, for example, 0LChoose Save.Note You may be prompted to enter a customizing request number. Select an existing customizing request or create a new one, then choose Continue.Note You can check whether the accounting principle is assigned to more than one ledger via configuration activity: Assign Accounting Principles to Ledgers and Company Codes (103556). | The ledger has been assigned to the valuation rule. |  |

#### Prerequisites – Enter Index Level

Purpose

In this SSC-UI, you can create:

1. Index class as the basis for further defining indexes for rent adjustments
2. Index series used in your organization for rent adjustments, including index series with base year
3. Index points for the index series

Standard Settings

SAP supplies the index classes 6 for real estate objects and 5 for maintenance and operating costs index (Switzerland).

Activities

1. Check whether you have to make changes to the standard setting. The Real Estate component requires the following index classes:

a) An index class for rent adjustment with the following settings:

-
    - Details on indexing frequency (monthly: entry 2)
    - Details on base year

b) Applies only for Switzerland: a class for maintenance and operating costs index with the following settings:

-
    - Details of an indexing frequency (monthly: entry 2)
    - No base year: Check if changes to the standard setting are necessary.

1. Index series

First maintain per index class the required index series and, for index series with base year, the required base years for the respective index series.

1. Index data

Create the required index data for the index series.

To do so, navigate over the required entry (index series with or without base year.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Search and Open Enter Index Levels | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Open Recurring settings.Click Configure in Enter Index Levels row.Select Index Classes(for example 6)Double-click Index Series and select an Index Series (for example S_DE)Double-click Base years for index series and select abase year(click New Entries to add a new base year if there has no data displayed)Double-click Index points for index series with base yearClick New Entries, input Year, Month, Day and Index, then save it.Note The index points maintained here are related to chapter Index Adjustment. Make sure the index points are maintained for the contract adjustment period and the next period so that adjustment can be calculated. For example, the contract start date is 01.11.2018 and there is no additional adjustment parameters are set, then index point must be maintained for 11. 2018 and 12. 2018. | The Index points have been added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Enter Index Levels | Go to the Business Processes Configuration app and search for the following activity: Enter Index Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Enter Index Levels | Select Index Classes(for example 6)Double-click Index Series and select an Index Series (for example S_DE)Double-click Base years for index series and select abase year (click New Entries to add a new base year if there has no data displayed)Double-click Index points for index series with base yearClick New Entries, input Year, Month, Day and Index, then save it.Note The index points maintained here are related to chapter Index Adjustment. Make sure the index points are maintained for the contract adjustment period and the next period so that adjustment can be calculated. For example, the contract start date is 01.11.2018 and there is no additional adjustment parameters are set, then index point must be maintained for 11. 2018 and 12. 2018. | The Index points have been added. |  |

#### Prerequisites – Maintain Residence Time

Purpose

Data archiving reduces the data volume in your production system by removing data that is no longer needed for current work, but must be available in case of inquiries.

In this SSC-UI you specify the residence time 1 and residence time 2 for the data to be archived per object type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Search and Open Define Residence Times for Archiving | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Open General Settings.Choose Configure in Define Residence Times for Archiving row.Enter a value for day(s) (for example 0) for Residence time 1 and Residence time 2 for Type: REFX_CNEnter a value for day(s) (for example 0) for Residence time 1 and Residence time 2 for Type: REFX_CNCF | The Residence Times have been added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Residence Times for Archiving | Go to the Business Processes Configuration app and search for the following activity: Define Residence Times for Archiving.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Define Residence Times for Archiving | Enter a value for day(s) (for example 0) for Residence time 1 and Residence time 2 for Type: REFX_CNEnter a value for day(s) (for example 0) for Residence time 1 and Residence time 2 for Type: REFX_CNCF | The Residence Times have been added. |  |

#### Define Question Catalogs

Purpose

In this configuration activity, you define the individual questions and assign them to various catalogs. You also specify the order of the questions in the respective catalog.

Questions: All relevant questions are defined here, irrespective of their relevance for a question catalog and the call sequence. Note the following logic:

- Questions that are answered with yes lead to the next question and finally to setting the required valuation rules.
- Questions that are answered with no lead to the questionnaire being exited. This means that no further valuation rule can be selected.

This means that you should choose the questions such that yes answers lead to leasing balancing (use of valuation rules) and no answers lead to handling without leasing balancing (use of object cash flow).

Question Catalog: This is where you define the required question catalogs.

Questions for Question Catalogs: Assign the questions defined under Questions to the individual question catalogs and specify the call sequence.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Contract Valuation |  |  |
| 5 | Configure | In the Define Question Catalogs row, choose Configure. |  |  |
| 6 | Search and Open Define Question Catalogs | Choose New Entries.Make the following entries:ID of Question: <Your question ID>Question: <Your question>Choose Save.Choose Question Catalog.Choose New Entries.ID Catalog: <Your ID catalog>Catalog Name: <Your catalog name>Choose Save.Choose the entry, choose Questions for Question Catalog.Choose New Entries.ID Catalog: <Your ID catalog>ID of Question: <Your question ID>Position: <Your position>Choose Save. | The Catalog of Questions have been added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Question Catalogs | Go to the Business Processes Configuration app and search for the following activity: Define Question Catalogs.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Search and Open Define Question Catalogs | Choose New Entries.Make the following entries:ID of Question: <Your question ID>Question: <Your question>Choose Save.Choose Question Catalog.Choose New Entries.ID Catalog: <Your ID catalog>Catalog Name: <Your catalog name>Choose Save.Choose the entry, choose Questions for Question Catalog.Choose New Entries.ID Catalog: <Your ID catalog>ID of Question: <Your question ID>Position: <Your position>Choose Save. | The Catalog of Questions have been added. |  |

#### Control Parameters Question Catalog

Purpose

In this configuration activity, you define the leasing questionnaires to be used in accordance with various control parameters.

You can filter the assignment of a questionnaire company code, contract type, and valuation object (including criteria for differentiation).

ID Catalog: In the Define Question Catalogs configuration activity, you define the possible question catalogs and their catalog IDs. This catalog ID is assigned in the control parameters.

Valuation Rule: The valuation rule assigned here defines the criteria or settings (for example, condition valuation groups, interest methods, valuation classification) that are used to calculate the informational net present value in questionnaires. This net present value is provisional information only and may change after completion of the questionnaire (for example, as a result of the condition classification being changed).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Contract Valuation |  |  |
| 5 | Configure | In the Control Parameters Question Catalog row, choose Configure. |  |  |
| 6 | Search and Open Control Parameters Question Catalog | Choose New Entries.Make the following entries and choose Save:Company Code: <Your company code>Type: <Assignment object type> for example, J4 or J5DifCrt: <Your Object Type>, for example: YCO01CTyp: <Your Contract Type>Valuation Rule: <Your Valuation Rule>ID Catalog: <Your Contract Type>, for example, 1 | The control parameters for question catalog are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Control Parameters Question Catalog.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Control Parameters Question Catalog | Choose New Entries.Make the following entries and choose Save:Company Code: <Your company code>Type: <Assignment object type> for example, J4 or J5DifCrt: <Your Object Type>, for example: YCO01CTyp: <Your Contract Type>Valuation Rule: <Your Valuation Rule>ID Catalog: <Your Contract Type>, for example, 1 | The control parameters for question catalog are added. |  |

#### Prerequisites – Define Output Parameter Determination – Invoice

Prerequisites

Relevant output parameters have been configured in background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Choose Show Rules for | In the Show Rules for field, click the triangle button and choose RE Contract Invoice from the drop-down list. |  |  |
| 4 | Choose the Determination Step | In the Determination step field, click the triangle button.Choose Output type, maintain and activate the following entries in Table Contents.Output type: RE_CONTRACT_A520Dispatch Time: 1 (Immediately)Choose Receiver in the Determination Step field, and maintain the following entries in Table Contents:Role: VWExclusive Indicator: - (false)Choose Channel in the Determination Step field, and maintain the following entries in Table ContentsChannel: PRINT (Print)Exclusive Indicator: - (false)Choose Print Settings in the Determination Step field, and maintain the following entries in Table Contents:Print Queue: DEFAULTNumber of Copies: 1Choose Email Settings in the Determination Step field, and maintain the following entries in Table Contents:Output type: RE_CONTRACT_A520Email Template: RE_CN_INVOICE_EMAILChoose Form template in the Determination Step field, and maintain the following entries in Table Contents:The first entry:Output type: RE_CONTRACT_A520Channel: PRINT (Print)Sender Ctry/Reg.: <Sender country/region>Company Code: <Your company code>Form Template: RE_CN_INVOICE_DEThe second entry:Output type: RE_CONTRACT_A520Channel: EMAIL(Email)Sender Ctry/Reg.: <Sender country/region>Company Code: <Your company code>Form Template: RE_CN_INVOICE_DEChoose Output Relevance in the Determination Step field, and maintain the following entries in Table Contents:Maintain the following entries in Table Contents.Relevance Indicator: X (true) |  |  |

#### Prerequisites – Define Output Parameter Determination – General Letter

Prerequisites

Relevant output parameters have been configured in background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Choose Show Rules for | In the Show Rules for field, click the triangle button and choose RE Contract from the drop-down list. |  |  |
| 4 | Choose the Determination Step | In the Determination step field, click the triangle button.Choose Output type, maintain and activate the following entries in Table Contents.Output type: RE_CONTRACT_A400Dispatch Time: 1 (Immediately)Choose Receiver in the Determination Step field, and maintain the following entries in Table Contents:Role: TRExclusive Indicator: - (false)Choose Channel in the Determination Step field, and maintain the following entries in Table Contents:Channel: PRINT (Print)Exclusive Indicator: - (false)Choose Print Settings in the Determination Step field, and maintain the following entries in Table Contents:Print Queue: DEFAULTNumber of Copies: 1Choose Form template in the Determination Step field, and maintain the following entries in Table Contents:Form Template: RE_CN_GENERAL_LETTER_DEOutput Relevance in the Determination Step field, and maintain the following entries in Table Contents:Relevance Indicator: X (true) |  |  |

#### Define Output Parameter Determination – Adjustment Letter

Purpose

In this activity, you define the output parameter determination for adjustment letters.

Prerequisites

Relevant output parameters are configured in the background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Choose Show Rules for | In the Show Rules for field, choose RE Adjustment of Conditions from the drop-down list. |  |  |
| 4 | Choose the Determination Step | In the Determination Step field, choose Output Type, maintain and activate the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Dispatch Time: 1 (Immediately)Choose Receiver in the Determination Step field, and maintain the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Role: VWExclusive Indicator: - (false)Choose Channel in the Determination Step field, and maintain the following column entries in the Table Contents.Output Type: ADJUSTMENT (Adjustment Result)Channel: PRINT (Print)Exclusive Indicator: - (false)Output Type: ADJUSTMENT (Adjustment Result)Channel: EMAIL (Email)Exclusive Indicator: - (false)Choose Printer Settings in the Determination Step field, and maintain the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Print Queue: DEFAULTNumber of Copies: 1Choose Email Settings in the Determination Step field, and maintain the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Email Template: RE_AJ_ADJUSTMENT_EMAILChoose Form Template in the Determination Step field, and maintain the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Form Template: RE_CPOM_CN_ADJUSTMENTRESULTChoose Output Relevance in the Determination Step field, and maintain the following column entries in the Table Contents:Output Type: ADJUSTMENT (Adjustment Result)Relevance Indicator: X (true) |  |  |

#### Prerequisites – Define Permitted Superordinate Architecture Object Types

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Define Permitted Superordinate Architecture Object Types | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Architecture Objects.Choose Configure in Define Permitted Superordinate Architecture Object Types row.Enter the new entry according to your needs. For example, select S2BU for Architecture Object Type, S1SI for Architecture Parent Object Type.Choose Save. | The new entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Permitted Superordinate Architecture Object Types | Go to the Business Processes Configuration app and search for the following activity: Define Permitted Superordinate Architecture Object Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Permitted Superordinate Architecture Object Types | Enter the new entry according to your needs. For example, select S2BU for Architecture Object Type, S1SI for Architecture Parent Object Type.Choose Save. | The new entry is saved. |  |

## Overview Table

This scope item consists of several processes provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

2SB

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_21) [page ] 35 | Contract Specialist - Leasing | Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Valuation |  |  |  |
| [Maintain Valuation Rule](#unique_22) [page ] 40 | Contract Valuation Specialist - Leasing | Valuation Management (F6170) | Existing contract valuation rule can be changed. |
| Valuation Posting |  |  |  |
| Periodic Valuation Posting |  |  |  |
| [Periodic Valuation Posting (Simulation)](#unique_23) [page ] 42 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is simulated. |
| [Periodic Valuation Posting (Update Run)](#unique_24) [page ] 44 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is executed. |
| Reverse Valuation Posting |  |  |  |
| [Reverse Valuation Posting (Simulation)](#unique_25) [page ] 46 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is simulated. |
| [Reverse Valuation Posting (Update Run)](#unique_26) [page ] 47 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is executed. |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Valuation Posting (Simulation)](#unique_23) [page ] 42 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_27) [page ] 50 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_28) [page ] 52 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update](#unique_29) [page ] 54 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |

2SA

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_30) [page ] 55 | Contract Specialist - Leasing | Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Valuation |  |  |  |
| [Maintain Valuation Rule](#unique_31) [page ] 60 | Contract Valuation Specialist - Leasing | Valuation Management (F6170) | Existing contract valuation rule can be changed. |
| Valuation Posting |  |  |  |
| Periodic Valuation Posting |  |  |  |
| [Periodic Valuation Posting (Simulation)](#unique_32) [page ] 62 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is simulated. |
| [Periodic Valuation Posting (Update Run)](#unique_33) [page ] 64 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is executed. |
| Reverse Valuation Posting |  |  |  |
| [Reverse Valuation Posting (Simulation)](#unique_34) [page ] 66 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is simulated. |
| [Reverse Valuation Posting (Update Run)](#unique_35) [page ] 67 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is executed. |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Posting - Simulation](#unique_36) [page ] 69 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_37) [page ] 70 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_38) [page ] 72 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update](#unique_39) [page ] 74 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |

34O

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_40) [page ] 75 | Contract Specialist - Leasing | Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Valuation |  |  |  |
| [Maintain Valuation Rule](#unique_41) [page ] 80 | Contract Valuation Specialist - Leasing | Valuation Management (F6170) | Existing contract valuation rule can be changed. |
| Valuation Posting |  |  |  |
| Periodic Valuation Posting |  |  |  |
| [Periodic Valuation Posting (Simulation)](#unique_42) [page ] 82 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is simulated. |
| [Periodic Valuation Posting (Update Run)](#unique_43) [page ] 84 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is executed. |
| Reverse Valuation Posting |  |  |  |
| [Reverse Valuation Posting (Simulation)](#unique_44) [page ] 86 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is simulated. |
| [Reverse Valuation Posting (Update Run)](#unique_45) [page ] 87 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is executed. |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Posting - Simulation](#unique_46) [page ] 89 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_47) [page ] 90 | Accounts Receivable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_48) [page ] 92 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update](#unique_49) [page ] 94 | Accounts Receivable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

Context

In this activity, you can create a new contract as part of your daily business.

Procedure

Three different scenarios are illustrated here by referring to

(1) Test Scenario for 0L (leading ledger):Lease-Out for Sublease Accounting (2SB)

(2) Test Scenario for 2L (non-leading ledger): Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA)

(3) Test Scenario for 3L (non-leading ledger): Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O)

Please refer to the relevant scenario(s) according to the scope item(s) you installed.

|  |
| --- |
| Note For lessee company code 1020, corresponding lease-in transaction need to be carried out. Refer to Lease-In Accounting (1T6) for Lease-Out for Sublease Accounting (2SB), Lease-In Accounting – Group Ledger IFRS (21P) for Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA), Lease-In Accounting – Group Ledger US GAAP (34N) for Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O) by replacing business partner 10300001 with 10401010. For lessee company code 1020, corresponding lease-in transaction need to be carried out. Refer to (1T6) and (21P) by replacing business partner 10300001 with 10401010. |

For countries that do not deliver all these three scope items (Lease-Out for Sublease Accounting (2SB), Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA) and Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O)), please ignore the scope items that are not delivered.

### (2SB) Lease-Out for Sublease Accounting

If local GAAP is used, follow this chapter to execute the scenario.

This test script, which is specifically designed for inter-company scenarios, contains a part of scope item Lease-Out for Sublease Accounting (2SB). For the rest part, please refer to Lease-Out for Sublease Accounting (2SB).

#### Contract Management

##### Create Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create a new contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing． | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object and make the following entries.Contract Type: <Lease out contract type> For example, Lease Out OtherCompany Code: <Your company code>Choose Continue. | Data is validated, next screen General Data screen displays. |  |
| 4 | Insert General Data | In General Data, make the following entries:Contract Name: <Your contract name>Main Contract: <Your company code and lease in contract number created in scope item 1T6>Contract Currency: <Your local currency> (as defaulted)Note The company code currency is defaulted here. It's allowed to be changed to a different currency.Valuation Relevance: Leasing ValuationNote If you also use IFRS, please refer to 2SA Lease-Out for Sublease Accounting – Group Ledger IFRS, chapter Create Contract for further guidance. | Data is validated. |  |
| 5 | Assign New Partner | Choose Partners.Choose Assign New Partner.Choose Customer (Fin.Accounting).Make the following entries:Business Partner: <Your intercompany business partner> for example, 10401020 | The Business Partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries and choose Enter:Contract start date: <Your contract start date>1st Contract end date: <Your contract end date> | The Correct Cash Flow From view displays. |  |
| 7 | Continue | Choose Continue in the Correct Cash Flow From view. | The cash flow from data is filled.The Term has been created. |  |
| 8 | Insert Contract Objects | Choose Objects.Choose Assign to link a contract object to the contract, then choose OK.Option 1:Contract Object: <Contract object designation> For example, COBObject Type: <Contract object type>Note Choose object type in accordance with the Contract Type you selected.For Lease Out Real Estate contract type, use the following objects:Land/PropertyBuildingLocation/SiteFloorRoomFor Lease Out Other contract type, use the following objects:DP/HardwareFixtures FittingsMachineryVehiclesBuilding EquipmentOffice EquipmentAccount assignment: <Select a cost center for an account assignment> for example, CTR A000/10101101 for DE, CTR A000/17101101 for US.Option 2:Select GRO Gen. Rental Obj and choose OK. For details, see 7AD Create Rental Object – MDS-MDS.Note Choose on the following dependent of the underling rentable object:Rentable Object with portfolio structureRentable Object without portfolio structureObject Type of Assigned Object: J7 (for details, see 7AD) | Data is validated.The Condition screen displays. |  |
| 9 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.For each condition, make the following entries:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note The currency in Contract Currency of tab General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Posting.Note If a foreign currency is used in Contract Currency in tab General Data or in Currency of tab Condition, select a currency translation rule in the field below.CrcyTrRule: <Select a rule>Tax Group: <Your default tax group>, for example, Y-FULLNote Default tax group can be set by SSC-UI Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_8) [page ] 9.For US, maintain the jurisdiction code.Tax Jurisdiction code: <Select a Tax Jurisdiction code>Note Additional Posting Term can be created. But tax jurisdiction code must be maintained in all Posting Terms.Choose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Choose Continue.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract.Choose Simulate to simulate the cash flow.Choose Back to Conditions.For US, maintain the statistical condition.Choose Insert Condition(s) to select the Condition Type of your contract.Condition Purpose: <Statistical>Valid From: <Condition valid from date>Unit Price: <Input amount of tax calculated from the origin condition>Note Ensure that the contract type, object type, and condition type are matched. For example, if the contract type is Lease out Real Estate, the condition type should be YCO01 Land/Property or YCO02 Building, and the condition type should be RE land or RE building related. | Data is validated.Cash flow can be simulated. |  |
| 10 | Insert Critical Dates and Reminders for Contract | Choose Resubmission.Choose Create reminder rule to create a reminder rule for your contract. Select the one reminder rule type (for example, Before End of Term).For each reminder rule, make the following entries and choose Continue:Reminder Rule: <Select a reminder rule>Resubmission Reason: <Select a reason>Then choose Save and go to the next screen. | The reminder rule is generated.The contract is saved and the number of the new contract is released. |  |
| 11 | Activate Contract | Choose Activate.Choose Yes. | A message to execute the activation is shown. The contract is activated. |  |

#### Contract Valuation

##### Maintain Valuation Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can change an existing contract valuation rule as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Valuation Management (F6170). | The Valuation Management screen displays. |  |
| 3 | Edit Contract Valuation | Input your contract number in search field and choose Go.Select the contract and choose Edit.Choose Create on the valuation tab.Make the following entries and choose Apply:Valuation Rule: <the relevant valuation principle> (for example, Germany Commercial Code - debit side (HGB_D))Object Identification: <COB contract object (J4) or gen. rental object (J7)>Start of Consideration: <defaulted by contract start date>Object Type of Assigned Object: <defaulted>Accounting Object ID: <defaulted>Note You shall change the default entry if you want to use a different accounting object.For US, maintain the interest rate.Interest Rate: <Your interest rate> | The valuation rule is created. |  |
| 4 | Save Contract | Choose Save.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed. | Data is saved. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract Valuation (RECECN). | The Contract screen displays. |  |
| 3 | Edit Contract Valuation | Make the following entries and choose Change Object:Company Code: <Your company code>Contract: <Your contract> | Data is validated, and next screen Valuation Parameters screen is displayed. |  |
| 4 | Update Valuation Parameters | Choose Create Term and make the following entries.Valuation parameter: <the relevant valuation principle> (for example, Germany Commercial Code - debit side (HGB_D))Acct. Assignment: as objectInterest Rate: <Your interest rate> | Data is validated.The Valuation parameters screen is displayed |  |
| 5 | Complete Valuation Rule and Save Contract | Select your valuation rule and click Rule Complete.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed.Choose Save. | Valuation rule is completed.Data is validated. |  |

##### Valuation Posting

###### Periodic Valuation Posting

###### Periodic Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: SimulationDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting simulation result is correct. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Periodic Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: Update RunDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting result is correct. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting

###### Reverse Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Valuation PostingJob Name: Reverse Valuation PostingChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: SimulationReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed. Contract valuation posting is displayed. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update run reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: <as defaulted>Job Name: <as defaulted>Choose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: Update RunReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed.Reversal document of valuation posting is posted and displayed. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

#### Accounting

##### Periodic Posting

###### Periodic Posting - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic posting of an existing contract as part of your daily business.

Procedure

When a contract is posted, it is useful to first simulate the posting.

To execute this activity go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: SimulationType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are generated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

###### Periodic Posting - Update Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the periodic posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: Update RunType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

##### Reverse Contract Postings

###### Reverse Contract Postings - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: SimulationReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

###### Reverse Contract Postings - Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: Update RunReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

### (2SA) Lease-Out for Sublease Accounting – Group Ledger IFRS

If parallel ledger (IFRS) is used, follow this chapter to execute the scenario.

This test script, which is specifically designed for inter-company scenarios, contains a part of scope item Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA). For the rest part, please refer to Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA).

#### Contract Management

##### Create Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create a new contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing． | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object and make the following entries.Contract Type: <Lease out contract type> For example, Lease Out OtherCompany Code: <Your company code>Choose Continue. | Data is validated, next screen General Data screen displays. |  |
| 4 | Insert General Data | In General Data, make the following entries:Contract Name: <Your contract name>Main Contract: <Your company code and lease in contract number created in scope item 21P>Contract Currency: <Your local currency> (as defaulted)Valuation Relevance: Leasing ValuationNote If you also use IFRS, please refer to 2SA Lease-Out for Sublease Accounting – Group Ledger IFRS, chapter Create Contract for further guidance. | Data is validated. |  |
| 5 | Assign New Partner | Choose Partners.Choose Assign New Partner.Choose Customer (Fin.Accounting).Make the following entries and choose Continue.Business Partner: <Your intercompany business partner> for example, 10401020 | The Business Partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries and choose Enter:Contract start date: <Your contract start date>1st Contract end date: <Your contract end date> | The Correct Cash Flow From view displays. |  |
| 7 | Continue | Choose Continue in the Correct Cash Flow From view. | The cash flow from data is filled.The Term has been created. |  |
| 8 | Insert Contract Objects | Choose Objects.Choose Assign to link a contract object to the contract, then choose OK.Option 1:Contract Object: <Contract object designation> For example, COBObject Type: <Contract object type>Note Choose object type in accordance with the Contract Type you selected.For Lease Out Real Estate contract type, use the following objects:Land/PropertyBuildingLocation/SiteFloorRoomFor Lease Out Other contract type, use the following objects:DP/HardwareFixtures FittingsMachineryVehiclesBuilding EquipmentOffice EquipmentAccount assignment: <Select a cost center for an account assignment> for example, CTR A000/10101101 for DE, CTR A000/17101101 for USOption 2:Select GRO Gen. Rental Obj and choose OK. For details, see 7AD Create Rental Object – MDS-MDS.Note Choose on the following dependent of the underling rentable object:Rentable Object with portfolio structureRentable Object without portfolio structureObject Type of Assigned Object: J7 (for details, see 7AD) | Data is validated.The Condition screen displays. |  |
| 9 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.For each condition make the following entries:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note The currency in Contract Currency of tab General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Posting.Note If a foreign currency is used in Contract Currency in tab General Data or in Currency of tab Condition, select a currency translation rule in below field.CrcyTrRule: <Select a rule>Tax Group: <your default tax group>, for example, Y-FULLNote Default tax group can be set by configuration step Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_8) [page ] 9.For US, maintain the jurisdiction code.Tax Jurisdiction code: <Select a Tax Jurisdiction code>Note Additional Posting Term can be created. But tax jurisdiction code must be maintained in all Posting Terms.Choose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract.Choose Continue.Choose Simulate to simulate the cash flow.Choose Back to Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.Condition Purpose: <Statistical>Valid From: <Condition valid from date>Unit Price: <Input amount of tax calculated from the original condition>Note Ensure that the contract type, object type, and condition type are matched. For example, if the contract type is Lease out Real Estate, the condition type should be YCO01 Land/Property or YCO02 Building, and the condition type should be RE land or RE building related. | Data is validated.Cash flow can be simulated. |  |
| 10 | Insert Critical Dates and Reminders for Contract | Choose Resubmission.Choose Create reminder rule to create a reminder rule for your contract. Select the one reminder rule type (for example, Before End of Term).For each reminder rule, make the following entries:Reminder Rule: <Select a reminder rule>Resubmission Reason: <Select a reason>Then choose Continue and go to the next screen. | The reminder rule is generated.The contract is saved and the number of the new contract is released. |  |
| 11 | Activate Contract | Choose Activate.Choose Yes. | A message to execute the activation is shown. The contract is activated. |  |

#### Contract Valuation

##### Maintain Valuation Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can change an existing contract valuation rule as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Valuation Management (F6170). | The Valuation Management screen displays. |  |
| 3 | Edit Contract Valuation | Input your contract number in search field and choose Go.Select the contract and choose Edit.Choose Create on the valuation tab.Make the following entries and choose Apply:Valuation Rule: <the relevant valuation principle> (for example, IFRS – Sublease (IFRS_FL))Object Identification: <COB contract object (J4) or gen. rental object (J7)>Start of Consideration: <defaulted by contract start date>Object Type of Assigned Object: <defaulted>Accounting Object ID: <defaulted>Note You shall change the default entry if you want to use a different accounting object.For US, maintain the interest rate.Interest Rate: <Your interest rate> | The valuation rule is created. |  |
| 4 | Save Contract | Choose Save.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed. | Data is saved. |  |
| 5 | Complete Valuation Rule | Select your valuation rule and click Complete. | Valuation rule is completed. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract Valuation (RECECN). | The Contract screen displays. |  |
| 3 | Edit Contract Valuation | Make the following entries and choose Enter:Company Code: <Your company code>Contract: <Your contract> | Data is validated, and next screen Valuation Parameters screen is displayed. |  |
| 4 | Update Valuation Parameters | Choose Edit and make the following entries:Valuation parameter: <the relevant valuation principle> (for example, IFRS – Sub-lease (IFRS_FL))Acct. Assignment: as objectInterest Rate: <Your interest rate> | Data is validated.The Valuation parameters screen is displayed |  |
| 5 | Complete Valuation Rule | Select your valuation rule and click on Rule Complete.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed.Choose Save. | Valuation rule is completed.Data is validated. |  |

##### Valuation Posting

###### Periodic Valuation Posting

###### Periodic Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: SimulationDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting simulation result is correct. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Periodic Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: Update RunDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting result is correct. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting

###### Reverse Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Valuation PostingJob Name: Reverse Valuation PostingChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: SimulationReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed. Contract valuation posting is displayed. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update run reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: <as defaulted>Job Name: <as defaulted>Choose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: Update RunReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed.Reversal document of valuation posting is posted and displayed. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

#### Accounting

##### Periodic Posting

###### Periodic Posting - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic posting of an existing contract as part of your daily business.

Procedure

When a contract is posted, it is useful to first simulate the posting.

To execute this activity go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: SimulationType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are generated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

###### Periodic Posting - Update Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the periodic posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date:<First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: Update RunType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

##### Reverse Contract Postings

###### Reverse Contract Postings - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: SimulationReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

###### Reverse Contract Postings - Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: Update RunReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

### (34O) Lease-Out for Sublease Accounting – Group Ledger US GAAP

For countries Austria, Belgium, Brazil, China, Denmark, Finland, Ghana, Hungary, Hong Kong, India, Indonesia, Italy, Ireland, Luxembourg, Malaysia, Mexico, Mozambique, New Zealand, Nigeria, Norway, Philippines, Poland, Romania, Saudi Arabia, Singapore, South Korea, Sweden, Taiwan, United Arab Emirates, please ignore this scope item Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O).

This test script, which is specifically designed for inter-company scenarios, contains a part of scope item Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O). For the rest part, please refer to Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O).

#### Contract Management

##### Create Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create a new contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing． | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object and make the following entries:Contract Type: <Lease out contract type> For example, Lease Out OtherCompany Code: <Your company code>Choose Continue. | Data is validated, next screen General Data screen displays. |  |
| 4 | Insert General Data | In General Data, make the following entries:Contract Name: <Your contract name>Main Contract: <Your company code and lease in contract number created in scope item 21P>Contract Currency: <Your local currency> (as defaulted)Note The company code currency is defaulted here. It’s allowed to be changed to a different currency.Valuation Relevance: Leasing ValuationNote If you also use IFRS, please refer to 2SA Lease-Out for Sublease Accounting – Group Ledger IFRS, chapter Create Contract for further guidance. | Data is validated. |  |
| 5 | Assign New Partner | Choose Partners.Choose Assign New Partner.Choose Customer (Fin.Accounting).Make the following entries and choose Continue.Business Partner: <Your intercompany business partner> for example, 10401020 | The Business Partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries and choose Enter:Contract start date: <Your contract start date>1st Contract end date: <Your contract end date> | The Correct Cash Flow From view displays. |  |
| 7 | Continue | Choose Continue. | The cash flow from data is filled.The Term has been created. |  |
| 8 | Insert Contract Objects | Choose Objects.Choose Assign to link a contract object to the contract, then choose Condition.Option 1:Contract Object: <Contract object designation> For example, COBObject Type: <Contract object type>Note Choose object type in accordance with the Contract Type you selected.For Lease Out Real Estate contract type, use the following objects:Land/PropertyBuildingLocation/SiteFloorRoomFor Lease Out Other contract type, use the following objects:DP/HardwareFixtures FittingsMachineryVehiclesBuilding EquipmentOffice EquipmentAccount assignment: <Select a cost center for an account assignment> for example, CTR A000/10101101 for DE, CTR A000/17101101 for USOption 2:Select GRO Gen. Rental Obj and choose OK. For details, see 7AD Create Rental Object – MDS-MDS.Note Choose on the following dependent of the underling rentable object:Rentable Object with portfolio structureRentable Object without portfolio structureObject Type of Assigned Object: J7 (for details, see 7AD) | Data is validated.The Condition screen displays. |  |
| 9 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.For each condition make the following entries:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note The currency in Contract Currency of tab General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Posting.Note If a foreign currency is used in Contract Currency in tab General Data or in Currency of tab Condition, select a currency translation rule in below field.CrcyTrRule: <Select a rule>Tax Group: <Your default tax group>, for example, Y-FULLNote Default tax group can be set by SSC-UI Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_8) [page ] 9.For US, maintain the jurisdiction code.Tax Jurisdiction code: <Select a Tax Jurisdiction code>Note Additional Posting Term can be created. But tax jurisdiction code must be maintained in all Posting Terms.Choose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Choose Continue.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract.Choose Simulate to simulate the cash flow.Choose Back to Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.Condition Purpose: <Statistical>Valid From: <Condition valid from date>Unit Price: <Input amount of tax calculated from the origin condition>Note Ensure that the contract type, object type, and condition type are matched. For example, if the contract type is Lease out Real Estate, the condition type should be YCO01 Land/Property or YCO02 Building, and the condition type should be RE land or RE building related. | Data is validated.Cash flow can be simulated. |  |
| 10 | Insert Critical Dates and Reminders for Contract | Choose Resubmission.Choose Create reminder rule to create a reminder rule for your contract. Select the one reminder rule type (for example, Before End of Term).For each reminder rule, make the following entries:Reminder Rule: <Select a reminder rule>Resubmission Reason: <Select a reason>Then choose Save and go to the next screen. | The reminder rule is generated.The contract is saved and the number of the new contract is released. |  |
| 11 | Activate Contract | Choose Activate.Choose Yes. | A message to execute the activation is shown. The contract is activated. |  |

#### Contract Valuation

##### Maintain Valuation Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can change an existing contract valuation rule as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Valuation Management (F6170). | The Valuation Management screen displays. |  |
| 3 | Edit Contract Valuation | Input your contract number in search field and choose Go.Select the contract and choose Edit.Choose Create on the valuation tab.Make the following entries and choose Apply:Valuation Rule: <the relevant valuation principle> (for example, Group United States GAAP FL – Sublease (USGP_SL))Object Identification: <COB contract object (J4) or gen. rental object (J7)>Start of Consideration: <defaulted by contract start date>Object Type of Assigned Object: <defaulted>Accounting Object ID: <defaulted>Note You shall change the default entry if you want to use a different accounting object.Interest Rate: <Your interest rate> | The valuation rule is created. |  |
| 4 | Save Contract | Choose Save.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed. | Data is saved. |  |
| 5 | Complete Valuation Rule | Select your valuation rule and click Complete. | Valuation rule is completed. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract Valuation (RECECN). | The Contract screen displays. |  |
| 3 | Edit Contract Valuation | Make the following entries and choose Change Object:Company Code: <Your company code>Contract: <Your contract> | Data is validated, and next screen Valuation Parameters screen is displayed. |  |
| 4 | Update Valuation Parameters | Make the following entries and choose Create Term.Valuation parameter: <the relevant valuation principle> (for example, Group United States GAAP FL – Sublease (USGP_SL))Acct. Assignment: as objectInterest Rate: <Your interest rate> | Data is validated.The Valuation parameters screen is displayed. |  |
| 5 | Complete Valuation Rule and Save Contract | Select your valuation rule and click Rule Complete.Please ignore the warning message below:Caution Valuation is pending and still needs to be completed.Choose Save. | Valuation rule is completed.Data is validated. |  |

##### Valuation Posting

###### Periodic Valuation Posting

###### Periodic Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: SimulationDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting simulation result is correct. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Periodic Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update the periodic valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: Update RunDocument Date: <Your document date> | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting result is correct. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting

###### Reverse Valuation Posting (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Valuation PostingJob Name: Reverse Valuation PostingChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: SimulationReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed. Contract valuation posting is displayed. |  |
| 6 | Check Contract Valuation Simulation Result | Choose Back to go back. |  |  |

###### Reverse Valuation Posting (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update run reversal of valuation posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs screen displays. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Valuation PostingJob Name: Reverse Valuation PostingChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Contract: <Your contract>Mode: Update RunReason for Reversal: <Your reason> for example, Wrong Period | The Job Details screen displays. |  |
| 4 | Check Contract Valuation Update Run Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 5 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed.Reversal document of valuation posting is posted and displayed. |  |
| 6 | Check Contract Valuation Update Run Result | Choose Back to go back. |  |  |

#### Accounting

##### Periodic Posting

###### Periodic Posting - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the periodic posting of an existing contract as part of your daily business.

Procedure

When a contract is posted, it is useful to first simulate the posting.

To execute this activity go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: SimulationType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are generated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

###### Periodic Posting - Update Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the periodic posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting - Background job (F4607). | The Periodic Posting screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: <Your company code>Input entry for either Contract Type or Contract:Contract Type: <Your contract type>Contract: <Your contract number>In the Period selection area:Month for Posting Run: <the month for posting run>Year for Posting Run: <the posting year>Due date: <before or on the last day of the posting month>In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <the posting period>Posting Run Mode: Update RunType of Posting Run: Integrated Posting | Data is validated, next screen New Job: Leasing contract: Periodic posting run screen is displayed. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are generated. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Periodic Posting screen is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

##### Reverse Contract Postings

###### Reverse Contract Postings - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: SimulationReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

###### Reverse Contract Postings - Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: <Your company code>Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: Update RunReason for reversal: <Your reason> for example, Wrong Period | Data is validated, next screen New Job: Reverse Contract Postings Application screen displays. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are gererated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Reverse Contract Postings screen displays. |  |

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
- related-to :: [[17-leasing-and-real-estate/lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-2sb-ae-859]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O9_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 139,899 chars in the whole document
