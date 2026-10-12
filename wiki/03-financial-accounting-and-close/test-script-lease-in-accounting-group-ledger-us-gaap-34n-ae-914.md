---
id: 03-financial-accounting-and-close/test-script-lease-in-accounting-group-ledger-us-gaap-34n-ae-914
title: "[DEPRECATED] Test Script: Lease-In Accounting – Group Ledger US GAAP (34N_AE) (34N_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (2608, AE) for scope item 34N: lease-in contracts, valuation, postings, adjustments, prerequisites and technical jobs."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/lease-in-accounting]
aliases: [34N_S4CLD2608_BPD_EN_AE]
keywords: [Lease-In Accounting, contract management, contract renewal, contract notice, contract valuation, valuation posting, periodic posting, rent adjustment, contract reminders, rou asset deactivation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34N_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: deprecated
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-914
topic: 03-financial-accounting-and-close/lease-in-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lease-In Accounting – Group Ledger US GAAP (34N_AE) (34N_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34N_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Lease-In Accounting** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lease-In Accounting – Group Ledger US GAAP (34N_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232851842)

[2 Prerequisites 6](#_Toc232851843)

[2.1 System Access 6](#_Toc232851844)

[2.2 Roles 6](#_Toc232851845)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232851846)

[2.4 Business Conditions 9](#_Toc232851847)

[2.5 Preliminary Steps 9](#_Toc232851848)

[2.5.1 Validate Asset Accounting System Readiness 9](#_Toc232851849)

[2.5.2 Default Value for Tax Rate per Contract Type 10](#_Toc232851850)

[2.5.3 Assign Tax Codes 11](#_Toc232851851)

[2.5.4 Prerequisites – Assign Tax Code (for FI Document) 13](#_Toc232851852)

[2.5.5 Prerequisites – Valuation Rule 14](#_Toc232851853)

[2.5.6 Enter Index Level 16](#_Toc232851854)

[2.5.7 Maintain Residence Time 18](#_Toc232851855)

[2.5.8 Define Question Catalogs 20](#_Toc232851856)

[2.5.9 Control Parameters Question Catalog 22](#_Toc232851857)

[2.5.10 Assign Account Symbol to Flow Type 24](#_Toc232851858)

[2.5.11 Replace Account Symbol 25](#_Toc232851859)

[2.5.12 Define Output Parameter Determination – General Letter 28](#_Toc232851860)

[2.5.13 Define Output Parameter Determination – Adjustment Letter 29](#_Toc232851861)

[2.5.14 Prerequisites – Define Permitted Superordinate Architecture Object Types 31](#_Toc232851862)

[2.5.15 Prerequisites – Edit Cost Element Group (Optional) 32](#_Toc232851863)

[2.5.16 Manage Global Hierarchies (Optional) 33](#_Toc232851864)

[3 Overview Table 34](#_Toc232851865)

[4 Test Procedures 40](#_Toc232851866)

[4.1 Contract Management 40](#_Toc232851867)

[4.1.1 Create Contract 40](#_Toc232851868)

[4.1.2 Contract Renewal 45](#_Toc232851869)

[4.1.2.1 Maintain Renewal Rule 45](#_Toc232851870)

[4.1.2.2 Execute Renewal Option (Single Contract) 47](#_Toc232851871)

[4.1.2.3 Reverse Renewal 49](#_Toc232851872)

[4.1.2.4 Execute Renewal Option (Multiple Contract) 51](#_Toc232851873)

[4.1.3 Contract Notice 52](#_Toc232851874)

[4.1.3.1 Maintain Notice Rule 52](#_Toc232851875)

[4.1.3.2 Give Notice (Single Contract) 55](#_Toc232851876)

[4.1.3.3 Reverse Notice 57](#_Toc232851877)

[4.1.3.4 Notice on Contracts 59](#_Toc232851878)

[4.1.4 Reminder for Contracts 61](#_Toc232851879)

[4.1.4.1 Maintain Reminder Rule 61](#_Toc232851880)

[4.1.4.2 Process Reminder 62](#_Toc232851881)

[4.1.5 Print General Correspondence 64](#_Toc232851882)

[4.1.6 Reports Contract Management 65](#_Toc232851883)

[4.1.6.1 Contract and Lease Management Dashboard 65](#_Toc232851884)

[4.1.6.2 Contracts - Information System 65](#_Toc232851885)

[4.1.6.3 Conditions for Contracts - Information System 66](#_Toc232851886)

[4.1.6.4 Business Partners of Contracts - Information System 67](#_Toc232851887)

[4.1.6.5 Objects for Contracts - Information System 68](#_Toc232851888)

[4.1.6.6 Term of Contracts - Information System 69](#_Toc232851889)

[4.1.6.7 Memos of Contract - Information System 70](#_Toc232851890)

[4.1.6.8 Contract Change Documents - Information System 70](#_Toc232851891)

[4.1.6.9 Real Estate Contract Validity Report 71](#_Toc232851892)

[4.1.6.10 Real Estate Contract Object Assignment Report 72](#_Toc232851893)

[4.2 Contract Valuation 73](#_Toc232851894)

[4.2.1 Maintain Valuation Rule 73](#_Toc232851895)

[4.2.2 Valuation Cashflow 75](#_Toc232851896)

[4.2.2.1 Generate Valuation Cashflow (Single Contract) 75](#_Toc232851897)

[4.2.2.2 Reverse Valuation Step 76](#_Toc232851898)

[4.2.2.3 Perform Contract Valuation – Mass Processing 78](#_Toc232851899)

[4.2.2.3.1 Perform Contract Valuation - Mass Processing (Simulation) 78](#_Toc232851900)

[4.2.2.3.2 Perform Contract Valuation - Mass Processing (Update Run) 79](#_Toc232851901)

[4.2.3 Valuation Posting 80](#_Toc232851902)

[4.2.3.1 Periodic Valuation Posting 80](#_Toc232851903)

[4.2.3.1.1 Periodic Valuation Posting (Simulation) 80](#_Toc232851904)

[4.2.3.1.2 Periodic Valuation Posting (Update Run) 82](#_Toc232851905)

[4.2.3.2 Reverse Valuation Posting 84](#_Toc232851906)

[4.2.3.2.1 Reverse Valuation Posting (Simulation) 84](#_Toc232851907)

[4.2.3.2.2 Reverse Valuation Posting (Update Run) 85](#_Toc232851908)

[4.2.4 Periodic Activities 87](#_Toc232851909)

[4.2.4.1 Asset Clearing Reconciliation 87](#_Toc232851910)

[4.2.4.2 Reclassification 88](#_Toc232851911)

[4.2.4.3 Liabilities Grading 88](#_Toc232851912)

[4.2.4.4 Deactivate Leased Assets 89](#_Toc232851913)

[4.2.4.5 Cancel Deactivation Leased Assets 91](#_Toc232851914)

[4.2.5 Reports Valuation Management 93](#_Toc232851915)

[4.2.5.1 Display Contract Valuation 93](#_Toc232851916)

[4.2.5.2 Valuation Balance - Information System 94](#_Toc232851917)

[4.2.5.3 Valuation Rules - Information System 95](#_Toc232851918)

[4.2.5.4 Condition Specific Valuation Rules for Contracts - Information System 95](#_Toc232851919)

[4.2.5.5 Assets for Contracts - Information System 96](#_Toc232851920)

[4.3 Accounting 97](#_Toc232851921)

[4.3.1 Periodic Posting 97](#_Toc232851922)

[4.3.1.1 Periodic Posting - Simulation 97](#_Toc232851923)

[4.3.1.2 Periodic Posting - Update Run 99](#_Toc232851924)

[4.3.2 Reverse Contract Postings 101](#_Toc232851925)

[4.3.2.1 Reverse Contract Postings - Simulation 101](#_Toc232851926)

[4.3.2.2 Reverse Contract Postings - Update 102](#_Toc232851927)

[4.3.3 Reports Accounting 104](#_Toc232851928)

[4.3.3.1 Contract and Lease Cashflow Dashboard 104](#_Toc232851929)

[4.3.3.2 General Real Estate Posting Log 104](#_Toc232851930)

[4.3.3.3 Documents for Contracts 105](#_Toc232851931)

[4.3.3.4 Item Overview - Information System 106](#_Toc232851932)

[4.3.3.5 Contract Cashflow Report 107](#_Toc232851933)

[4.3.3.6 Conditions for Contracts - Information System 108](#_Toc232851934)

[4.3.3.7 Periodic Posting: Previous Period Comparison 109](#_Toc232851935)

[4.3.3.8 Lease and Real Estate Accounting Review Booklet (Optional) 111](#_Toc232851936)

[4.4 Adjustment 112](#_Toc232851937)

[4.4.1 Maintain Adjustment Rule 112](#_Toc232851938)

[4.4.2 Create Adjustment 113](#_Toc232851939)

[4.4.3 Modify and Activate Adjustment (Optional) 115](#_Toc232851940)

[4.4.4 Display Adjustment 116](#_Toc232851941)

[4.4.5 Create Adjustment Letter 117](#_Toc232851942)

[4.4.6 Manage Adjustment Letter Output 118](#_Toc232851943)

[4.4.7 Reports Adjustment 119](#_Toc232851944)

[4.4.7.1 Adjustments on Contracts 119](#_Toc232851945)

[4.4.7.2 Cond./Adjustment Rule - Information System 120](#_Toc232851946)

[4.5 Technical Transactions 121](#_Toc232851947)

[4.5.1 Analyze Logs 121](#_Toc232851948)

[4.5.2 Update Objects in Worklist - Background Job 122](#_Toc232851949)

[4.5.3 Check Contracts - Background Job 123](#_Toc232851950)

[4.5.4 Cash Flow Update for Contracts 124](#_Toc232851951)

[4.5.5 Generate Reminder Dates for Contracts 126](#_Toc232851952)

[4.5.6 Schedule Generic Rental Object Checks 127](#_Toc232851953)

[4.6 Archive Contracts 128](#_Toc232851954)

## Purpose

Overview

Lease contracts describe contractual agreements between two partners: the lessor and the lessee. The lessor is the owner of an asset, whereas the lessee has a right to use this asset during the period agreed in the lease contract. For the use of the asset, the lessee must pay lease payments that are agreed in the lease contract.

This scope item helps you standardize and automate your lease-in credit contract management activities for real estate, as well as for machinery, equipment, vehicles, and computer hardware.

You can easily create new contracts, execute periodic postings for existing contracts, and execute valuation postings for existing contracts.

You can run reports of your existing contracts as part of your daily business.

You can create reminder rules for every contract, for example, to check the contract conditions, the contract term, or the renewal options, saving you time and effort and freeing up capacity for more strategic tasks.

Leveraging the reporting functions enables you to make better and more informed lease management decisions.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Contract Specialist - Leasing | SAP_BR_RECM_SPECIALIST | Leasing Contract Management / Leasing Contract Management - Sales-Based Rent | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |
| Contract Valuation Specialist - Leasing | SAP_BR_RECM_VALSPECIALIST | Leasing Valuation | SAP_BR_RECM_VALSPECIALIST |  |
| Accounts Payable Accountant - Leasing | SAP_BR_RECM_AP_ACCOUNTANT | Accounts Payable - Leasing | SAP_BR_RECM_AP_ACCOUNTANT |  |
| Accounts Receivable Accountant - Leasing | SAP_BR_RECM_AR_ACCOUNTANT | Accounts Receivable - Leasing | SAP_BR_RECM_AR_ACCOUNTANT |  |
| Administrator - Leasing | SAP_BR_RECM_ADMINISTRATOR | Administration - Leasing | SAP_BR_RECM_ADMINISTRATOR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Administrator - Real Estate Management | SAP_BR_RE_ADMINISTRATOR | Administration - Real Estate | SAP_FIN_SPT_RE_ADMIN_PC |  |
| Cost Accountant - Real Estate | SAP_BR_RE_COST_ACCOUNTANT | Cost Accounting - Real Estate | SAP_FIN_SPT_RE_COST_ACCOUNT_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310; 3320 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Asset Class | 6210 FL Land6220 FL Building6230 FL Computer6240 FL Fixture & Fitt.6250 FL Machinery Fitt.6260 FL Vehicles6310 OL Land6320 OL Building6330 OL Computer6340 OL Fixture & Fitt.6350 OL Machinery6360 OL Vehicles |  |  |
| Asset | Note The asset is created in the system during this process. |  |  |
| Vendor | 33300001 33300002 |  |  |
| Cost Center | Any available cost center with company code relation (for example, 33101101) |  |  |
| Profit Center | Any available profit center (for example, YB600) |  |  |
| Functional Area | Any available functional area, for example, YB40 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNH | Create Profit Center - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNP | Create Cost Element Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| Accounting and Financial Close – Group Ledger US GAAP (2VA) | Technical constraint for CBC scoping purpose. |
| Lease-In Accounting (1T6) | Lease-in contract with external party must exist. |

### Preliminary Steps

#### Validate Asset Accounting System Readiness

Please refer to the Preliminary Steps of J62, specifically chapter Confirm Takeover Date Information and Confirm Run of Balance Carry Forward for Current Fiscal Year.

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
| 6 | Assign Tax Type and Tax Group | In the Default Tax Group column, verify or change your default tax group (for example, Y-FULL).Choose Save.Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Default Value for Tax Rate per Contract Type | Go to the Business Processes Configuration app and search for the following activity: Default Value for Tax Rate per Contract Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Default Values for Tax Type/Group": Overview view is displayed. |  |
| 3 | Assign Tax Type and Tax Group | In the Default Tax Group column, verify or change your default tax group (for example, Y-FULL).Choose Save.Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. |  |  |

#### Assign Tax Codes

Purpose

In this SSC-UI, you assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country-dependent and time-dependent.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Accounting Integration |  |  |
| 5 | Configure | In the Assign Tax Codes row, choose Configure. |  |  |
| 6 | Assign Tax Code | Enter a tax code if it is blank (for example, <Input Tax Code>).Choose Save.Note To change the tax code, choose the Display/Edit button, then select the magnifying glass in the cell you wish to change. | The tax code is assigned to the company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Tax Code Assignment | Go to the Business Processes Configuration app and search for the following activity: Tax Code Assignment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Code | Enter a tax code if it is blank (for example, <Input Tax Code>).Choose Save.Note To change the tax code, choose the Display/Edit button, then select the magnifying glass in the cell you wish to change. | The tax code is assigned to the company code. |  |

#### Prerequisites – Assign Tax Code (for FI Document)

Purpose

In this SSC-UI, you assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country-dependent and time-dependent.

You have to make this assignment in order for FI documents to be read correctly in RE. This assignment is relevant, for example, for service charge settlement and input tax distribution.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launch Pad displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Assign Tax Type and Tax Group | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Accounting Integration.Choose Configure in Assign Tax Code (for FI Document) row.Enter Tax Type and Tax Group if they are blank (for example, Y1 and Y-NONE).Choose Save. | The Tax Code has been assigned to company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Tax Code (for FI Document) | Go to the Business Processes Configuration app and search for the following activity: Assign Tax Code (for FI Document).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a . |  |  |
| 3 | Assign Tax Type and Tax Group | Enter Tax Type and Tax Group if they are blank (for example, Y1 and Y-NONE).Choose Save. | The Tax Code has been assigned to company code. |  |

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

#### Enter Index Level

Purpose

In this configuration activity, you can create:

- Index class as the basis for further defining indexes for rent adjustments
- Index series used in your organization for rent adjustments, including index series with base year
- Index points for the index series

Standard Settings

SAP supplies the index class 6 for real estate objects, and index class 5 for maintenance.

Activities

1. Check if you need to change the standard setting. The Real Estate component requires the following index classes:
    - An index class for rent adjustment with the following settings:
        - Details on indexing frequency (monthly: entry 2)
        - Details on base year
2. Index series
    - Per index class, maintain the required index series and, for index series with base year, the required base years for the respective index series.
3. Index data
    - Create the required index data for the index series. To do so, navigate over the required entry (index series with or without base year).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Recurring settings |  |  |
| 5 | Configure | In the Enter Index Levels row, choose Configure. |  |  |
| 6 | Search and Open Enter Index Levels | Select Index classes (for example, 6).In the Dialog Structure pane, double-click, Index Series and select an Index Series (for example S_AE).Remain in the Dialog Structure pane and double-click Base years for index series and select a base year (if no data is displayed, choose New Entries to add a new base year.).Double-click Index points for index series with base year.Choose New Entries. Enter the Year, Month, Day and Index, then save your entries.Note The index points maintained here are related to the Index Adjustment section. Make sure the index points are maintained for the contract adjustment period and the next period so that adjustment can be calculated. For example, the contract start date is 01.11.2018 and there is no additional adjustment parameters are set, then index point must be maintained for 11. 2018 and 12. 2018. | The Index points have been added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Enter Index Levels | Go to the Business Processes Configuration app and search for the following activity: Enter Index Levels.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Enter Index Levels | Select Index Classes (for example, 6).Double-click Index Series and select an Index Series (for example S_AE).In the Dialog Structure pane, double-click Base years for index series and select a base year (choose New Entries to add a new base year if no data displayed).Double-click Index points for index series with base year.Choose New Entries. Enter the Year, Month, Day and Index, then save your entries.Note The index points maintained here are related to the Index Adjustment section. Make sure the index points are maintained for the contract adjustment period and the next period so that adjustment can be calculated. For example, the contract start date is 01.11.2018 and there is no additional adjustment parameters are set, then index point must be maintained for 11. 2018 and 12. 2018. | The Index points have been added. |  |

#### Maintain Residence Time

Purpose

Data archiving reduces the data volume in your production system by removing data that is no longer needed for current work, but must be available in case of inquiries.

In this configuration activity, you specify the residence times (1 and 2) for the data to be archived per object type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: General Settings | The General Settings view displays. |  |
| 5 | Configure | In the Define Residence Times for Archiving row, choose Configure. |  |  |
| 6 | Search and Open Define Residence Times for Archiving | For the REFX_CN.and REFX_CNCF rows, under Residence time 1 and Residence time 2, enter a value represented in days (for example, 0).Choose Save. | The Residence Times have been added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Residence Times for Archiving | Go to the Business Processes Configuration app and search for the following activity: Define Residence Times for Archiving.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Define Residence Times for Archiving | Enter a value for day(s) (for example, 0) for Residence time 1 and Residence time 2 for Type: REFX_CN.Enter a value for day(s) (for example, 0) for Residence time 1 and Residence time 2 for Type: REFX_CNCF.Choose Save. | The Residence Times have been added. |  |

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

#### Assign Account Symbol to Flow Type

|  |
| --- |
| Note From 2102, the account symbol for flow type FA00, FA10, FA20, FK00, FK10, FK20, OA00, OA10, OA20, OK00, OK10, OK20, IA00, IA10 and IA20, IK00, IK10 and IK20 is changed from Y-ASSETCLEARING (with assigned G/L account 16014000 - Technical Clrng Acct Integrated Asset Acquisition) to S-LEASERTMLGADJ (with assigned G/L account 71010300 - Loss from Asset Transactions (ROU)) for new customers. It has impact on RoU asset acquisition/reduction/early termination postings.From 2105, the account symbol for flow type I940, I941, I945, I946, F940, F941, F945 and F946 for new customer is changed from S-D_CLEARING (with assigned G/L account 21320000 - Leasing Out Clearing) to S-LEASERTMLGADJ (with assigned G/L account 71010300 - Loss from Asset Transactions (ROU)) for new customers. It has impact on RoU asset retirement/subletting postings.From 2105, the account symbols for flow type IL00, IL10, IL20, FL00, FL10 and FL20 are changed for new customer. Please refer to below table for detailed changes. It has impact on service charge postings.Old Account SymbolsNew Account SymbolsY-LEASEEXPBULINS-SERTRABUILDY-LEASEEXPCOLIS-SERTRACOMPY-LEASEEXPFFLINS-SERTRAFIXFY-LEASEEXPLALINS-SERTRALANDY-LEASEEXPMALINS-SERTRAMACHY-LEASEEXPOFLINS-SERTRAOFFIY-LEASEEXPVELINS-SERTRAVEHIFrom 2105, the debit account symbol for flow type I800 (assigned in condition type LG90) have been changed as per below table. This change will cause the G/L account change in valuation posting for condition type LG90.Table 1:Account DeterminationOld Account SymbolsOld G/L AccountNew Account SymbolsNew G/L AccountYROUBUY-ASSETCLEARING0016014100S-EXTRADEPRECBU0064001100YROUCOY-ASSETCLEARING0016014100S-EXTRADEPRECCO0064007100YROUFFY-ASSETCLEARING0016014100S-EXTRADEPRECFF0064006100YROULAY-ASSETCLEARING0016014100S-EXTRADEPRECLA0064000100YROUMAY-ASSETCLEARING0016014100S-EXTRADEPRECMA0064002100YROUOFY-ASSETCLEARING0016014100S-EXTRADEPRECOF0064005100YROUVEY-ASSETCLEARING0016014100S-EXTRADEPRECVE0064004100If an existing customer, who installed the leasing solution before 2015, wants to apply this change as well, make the changes using this SSCUI accordingly. |

#### Replace Account Symbol

Purpose

To complete the configuration which is used for RoU asset unplanned depreciation scenario, please check whether the relevant replace account symbols have been maintained in this SSCUI or manually add them according to the following procedure.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution | The Configure Your Solution screen displays. |  |
| 4 | Search and Open Control Parameters Question Catalog | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Condition and account determination.Choose Configure in Replace Account Symbols row.Choose New Entries and enter below value:Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECBUG/L Account: 0063009100Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECLAG/L Account: 0063009200Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECMAG/L Account: 0063009300Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECVEG/L Account: 0063009400Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECOFG/L Account: 0063009500Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECFFG/L Account: 0063009600Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECCOG/L Account: 0063009700Note You can replace the SAP predelivered G/L account with your own G/L account.Choose Save. | The account symbol is added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Replace Account Symbols | Go to the Business Processes Configuration app and search for the following activity: Replace Account Symbols.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Search and Open Control Parameters Question Catalog | Choose New Entries and enter below value:Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECBUG/L Account: 0063009100Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECLAG/L Account: 0063009200Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECMAG/L Account: 0063009300Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECVEG/L Account: 0063009400Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECOFG/L Account: 0063009500Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECFFG/L Account: 0063009600Chart of Account: YCOAAccount Symbol: S-EXTRADEPRECCOG/L Account: 0063009700Note You can replace the SAP predelivered G/L account with your own G/L account.Choose Save. | The account symbol is added. |  |

#### Define Output Parameter Determination – General Letter

Purpose

In this activity, you define the output parameter determination for the general letter.

Prerequisites

Relevant output parameters have been configured in background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Choose Show Rules for | In the Show Rules for field, choose RE Contract from the drop-down list. |  |  |
| 4 | Choose the Determination Step | In the Determination step field, choose Output type, maintain and activate the following column entries in the Table Contents.Output type: RE_CONTRACT_A400Dispatch Time: 1 (Immediately)Choose Receiver in the Determination Step column field, and maintain the following column entries in the Table Contents:Role: TRExclusive Indicator: - (false)Choose Channel in the Determination Step field, and maintain the following column entries in the Table Contents:Channel: PRINT (Print)Exclusive Indicator: - (false)Choose Print Settings in the Determination Step field, and maintain the following column entries in the Table Contents:Print Queue: DEFAULTNumber of Copies: 1Choose Form template in the Determination Step field, and maintain the following column entries in the Table Contents:Form Template: RE_CN_GENERAL_LETTER_DEChoose Output Relevance in the Determination Step field, and maintain the following column entries in the Table Contents:Relevance Indicator: X (true) |  |  |

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

#### Prerequisites – Edit Cost Element Group (Optional)

Context

This section covers the Cost Element Group creation.

Procedure

Below cost element group 10_RE is pre-delivered. To change it, refer to Create Cost Element Group - MDS (BNP).

Table 2:

|  |  |  |  |
| --- | --- | --- | --- |
| 10_RE | Real Estate Costs |  |  |
|  | 100_RE | RE Operating Costs |  |
|  | 200_RE | RE Consumption Costs |  |
|  | 300_RE | RE Capital Costs |  |
|  | 400_RE | RE Administration Costs |  |
|  | 500_RE | RE Other Costs |  |
|  |  | 5100_RE | Others |

#### Manage Global Hierarchies (Optional)

To display the amounts of the cost element group in the report [Lease and Real Estate Accounting Review Booklet (Optional)](#unique_23) [page ] 111, the cost element group hierarchy needs to be imported and created via SAP Fiori app Manage Global Hierarchies (F2918). Please refer to the Appendix of Accounting and Financial Close (J58) scope item, specifically chapter Bank Account Grouping.

## Overview Table

The Lease-In Accounting – Group Ledger US GAAP scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_25) [page ] 40 | Contract Specialist - Leasing | Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Renewal |  |  |  |
| [Maintain Renewal Rule](#unique_26) [page ] 45 | Contract Specialist - Leasing | Contract Management (F5273); Manage Contract (RECN) | Contract can be renewed. |
| [Execute Renewal Option (Single Contract)](#unique_27) [page ] 47 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Existing contract can be renewed |
| [Reverse Renewal](#unique_28) [page ] 49 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | The performed renewal can be reversed. |
| [Execute Renewal Option (Multiple Contract)](#unique_29) [page ] 51 | Contract Specialist - Leasing | Renewal of Contracts - Information System (REISCNRN) | Several contracts can be renewed at the same time. |
| Contract Notice |  |  |  |
| [Maintain Notice Rule](#unique_30) [page ] 52 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Notice rule can be maintained. |
| [Give Notice (Single Contract)](#unique_31) [page ] 55 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | You can give notice to a contract. |
| [Reverse Notice](#unique_32) [page ] 57 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Notice can be reversed. |
| [Notice on Contracts](#unique_33) [page ] 59 | Contract Specialist - Leasing | Notice on Contracts - Information System (REISCNNT) | You can give notification to your contract. |
| Reminder for Contracts |  |  |  |
| [Maintain Reminder Rule](#unique_34) [page ] 61 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder rule is maintained. |
| [Process Reminder](#unique_35) [page ] 62 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder is processed. |
| [Print General Correspondence](#unique_36) [page ] 64 | Contract Specialist - Leasing | Print: General Correspondence (RECPA400) | General correspondence for existing contracts can be printed. |
| Reports Contract Management |  |  |  |
| [Contract and Lease Management Dashboard](#unique_37) [page ] 65 | Contract Specialist - Leasing | Contract and Lease Management Dashboard (F4555) | You run a report of existing contracts. |
| [Contracts - Information System](#unique_38) [page ] 65 | Contract Specialist - Leasing | Contracts - Information System (REISCN) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_39) [page ] 66 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Business Partners of Contracts - Information System](#unique_40) [page ] 67 | Contract Specialist - Leasing | Business Partners of Contracts - Information System (REISCNBP) | You run a report of existing contracts. |
| [Objects for Contracts - Information System](#unique_41) [page ] 68 | Contract Specialist - Leasing | Objects for Contracts - Information System (REISCNOA) | You run a report of existing contracts. |
| [Term of Contracts - Information System](#unique_42) [page ] 69 | Contract Specialist - Leasing | Term of Contracts - Information System (REISCNPE) | You run a report of existing contracts. |
| [Memos of Contract - Information System](#unique_43) [page ] 70 | Contract Specialist - Leasing | Memos of Contract - Information System (REISCNMEMO) | You run a report of existing contracts. |
| [Contract Change Documents - Information System](#unique_44) [page ] 70 | Contract Specialist - Leasing | Contract Change Documents - Information System (REISCHGDOCCN) | You run a report of existing contracts. |
| [Real Estate Contract Validity Report](#unique_45) [page ] 71 | Contract Specialist - Leasing | Real Estate Contract Validity Report (W0200) | You run a report of existing contracts. |
| [Real Estate Contract Object Assignment Report](#unique_46) [page ] 72 | Contract Specialist - Leasing | Real Estate Contract Object Assignment Report (W0201) | You run a report of existing contracts. |
| Contract Valuation |  |  |  |
| [Maintain Valuation Rule](#unique_47) [page ] 73 | Contract Valuation Specialist - Leasing | Valuation Management (F6170) | Existing contract valuation rule can be changed. |
| Valuation Cashflow |  |  |  |
| [Generate Valuation Cashflow (Single Contract)](#unique_48) [page ] 75 | Contract Valuation Specialist - Leasing | Valuation Management (F6170), Manage Contract Valuation (RECECN) | Contract valuation can be performed. |
| [Reverse Valuation Step](#unique_49) [page ] 76 | Contract Valuation Specialist - Leasing | Reverse Valuation Steps (RECEPRRV) | Performed contract valuation can be canceled. |
| Perform Contract Valuation - Mass Processing |  |  |  |
| [Perform Contract Valuation - Mass Processing (Simulation)](#unique_50) [page ] 78 | Contract Valuation Specialist - Leasing | Perform Contract Valuation - Background Job (F6277) | Valuation generation is simulated. |
| [Perform Contract Valuation - Mass Processing (Update Run)](#unique_51) [page ] 79 | Contract Valuation Specialist - Leasing | Perform Contract Valuation - Background Job (F6277) | Valuation generation is executed. |
| Valuation Posting |  |  |  |
| Periodic Valuation Posting |  |  |  |
| [Periodic Valuation Posting (Simulation)](#unique_52) [page ] 80 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is simulated. |
| [Periodic Valuation Posting (Update Run)](#unique_53) [page ] 82 | Contract Valuation Specialist - Leasing | Periodic Valuation posting - Background job (F4608) | Periodic valuation posting is executed. |
| Reverse Valuation Posting |  |  |  |
| [Reverse Valuation Posting (Simulation)](#unique_54) [page ] 84 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is simulated. |
| [Reverse Valuation Posting (Update Run)](#unique_55) [page ] 85 | Contract Valuation Specialist - Leasing | Reverse Valuation Posting - Background Job (F6276) | Reversal of valuation posting is executed. |
| Periodic Activities |  |  |  |
| [Asset Clearing Reconciliation](#unique_56) [page ] 87 | Contract Valuation Specialist - Leasing | Asset Clearing Reconciliation (RECEASCLEARRECON) |  |
| [Reclassification](#unique_57) [page ] 88 | Contract Valuation Specialist - Leasing | Reclassification - Information System (RECEISRECLASSIFY) |  |
| [Liabilities Grading](#unique_58) [page ] 88 | Contract Valuation Specialist - Leasing | Liabilities Grading - Information System (RECEISLIABGRAD) |  |
| [Deactivate Leased Assets](#unique_59) [page ] 89 | Contract Valuation Specialist - Leasing | Deactivate Leased Assets (RECEASSETDEACT) |  |
| [Cancel Deactivation Leased Assets](#unique_60) [page ] 91 | Contract Valuation Specialist - Leasing | Cancel Deactivation Leased Assets (RECEASSETDEACTRV) |  |
| Reports Valuation Management |  |  |  |
| [Display Contract Valuation](#unique_61) [page ] 93 | Contract Valuation Specialist - Leasing | Display Contract Valuation (RECESH) | You run a report of existing contracts. |
| [Valuation Balance - Information System](#unique_62) [page ] 94 | Contract Valuation Specialist - Leasing | Valuation Balance - Information System (RECEISBALANCE) | You run a report of existing contracts. |
| [Valuation Rules - Information System](#unique_63) [page ] 95 | Contract Valuation Specialist - Leasing | Valuation Rules - Information System (RECEISRULECN) | You run a report of existing contracts. |
| [Condition Specific Valuation Rules for Contracts - Information System](#unique_64) [page ] 95 | Contract Valuation Specialist - Leasing | Condition specific valuation rules for Contracts - Information System (RECEISCONDRULECN) | You run a report of existing contracts. |
| [Assets for Contracts - Information System](#unique_65) [page ] 96 | Contract Valuation Specialist - Leasing | Assets for Contracts - Information System (RECEISASSETCN) | You run a report of existing contracts. |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Posting - Simulation](#unique_66) [page ] 97 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_67) [page ] 99 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_68) [page ] 101 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update](#unique_69) [page ] 102 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |
| Reports Accounting |  |  |  |
| [Contract and Lease Cashflow Dashboard](#unique_70) [page ] 104 | Accounts Payable Accountant - Leasing | Contract and Lease Cashflow Dashboard (F5379) | You run a report of existing contracts. |
| [General Real Estate Posting Log](#unique_71) [page ] 104 | Contract Valuation Specialist - Leasing or Accounts Payable Accountant - Leasing | General Real Estate Posting Log (RERAPL) | You review the general posting for contracts. |
| [Documents for Contracts](#unique_72) [page ] 105 | Contract Valuation Specialist - Leasing | Documents for Contracts - Information System (REISREDOCCN) | You run a report of existing contracts. |
| [Item Overview - Information System](#unique_73) [page ] 106 | Accounts Payable Accountant - Leasing | Item Overview - Information System (REISRADOCITEM) | You run a report of existing contracts. |
| [Contract Cashflow Report](#unique_74) [page ] 107 | Accounts Payable Accountant - Leasing | Contract Cashflow Report (F5363) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_75) [page ] 108 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Periodic Posting: Previous Period Comparison](#unique_76) [page ] 109 | Accounts Payable Accountant - Leasing | Periodic Posting: Previous Period Comparison (RERAPPCMP) | You run a report of existing contracts. |
| [Lease and Real Estate Accounting Review Booklet (Optional)](#unique_23) [page ] 111 | Cost Accountant - Real Estate | Lease and Real Estate Accounting Review Booklet (F8196) | You run a report of existing contracts. |
| Adjustment |  |  |  |
| [Maintain Adjustment Rule](#unique_77) [page ] 112 | Contract Specialist - Leasing | Manage Contract (RECN) | Condition of an existing contract can be adjusted. |
| [Create Adjustment](#unique_78) [page ] 113 | Contract Specialist - Leasing | Specify Adjustments (REAJPR) | Condition of an existing contract can be adjusted. |
| [Modify and Activate Adjustment (Optional)](#unique_79) [page ] 115 | Contract Specialist - Leasing | Continue Adjustment (REAJCH) | Adjustment of contracts can be modified. |
| [Display Adjustment](#unique_80) [page ] 116 | Contract Specialist - Leasing | Display Adjustments (REAJSH) | Adjustment of contracts can be displayed. |
| [Create Adjustment Letter](#unique_81) [page ] 117 | Contract Specialist - Leasing |  | Adjustment letter can be created. |
| [Manage Adjustment Letter Output](#unique_82) [page ] 118 | Contract Specialist - Leasing | Manage Real Estate Output Requests (F7482) | Condition of an existing contract can be adjusted. |
| Reports Adjustment |  |  |  |
| [Adjustments on Contracts](#unique_83) [page ] 119 | Contract Specialist - Leasing | Adjustments on Contracts (REAJAHCN) | Condition of an existing contract can be adjusted. |
| [Cond./Adjustment Rule - Information System](#unique_84) [page ] 120 | Contract Specialist - Leasing | Cond./Adjustment Rule - Information System (REISCDCNAJ) | You run a report of existing contracts. |
| Technical Transactions |  |  |  |
| [Analyze Logs](#unique_85) [page ] 121 | Administrator - Leasing | Analyze Logs (RECALA) | Logs are analyzed. |
| [Update Objects in Worklist - Background Job](#unique_86) [page ] 122 | Administrator - Leasing | Update Objects in Worklist - Background job (F5969) | Update objects in worklist is simulated. |
| [Check Contracts - Background Job](#unique_87) [page ] 123 | Administrator - Leasing | Check Contracts - Background job (F5968) | Update objects in worklist is executed. |
| [Cash Flow Update for Contracts](#unique_88) [page ] 124 | Administrator - Leasing | Cash Flow Update for Contract (RECDCGOL) | Cash flow of existing contracts can be updated. |
| [Generate Reminder Dates for Contracts](#unique_89) [page ] 126 | Administrator - Leasing | Generate Dates for Contracts (RECARSGENCN) | General reminder item of the new year is displayed. |
| [Schedule Generic Rental Object Checks](#unique_90) [page ] 127 | Administrator - Real Estate Management or Administrator - Leasing | Schedule Generic Rental Object Check - Background Job (F7963) | Generic rental object can be checked. |
| [Archive Contracts](#unique_91) [page ] 128 | Administrator - Leasing | Manage Contract (RECN) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Contract Management

#### Create Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To execute this activity, go step by step through the table.

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object.Make the following entries and choose Continue:Contract Type: <Lease in contract type> For example, Lease In OthersNote Choose the contract type dependent of the underlining Asset:Lease In Real Estate (for Land and building)Lease In Others (for Cars, Machine, IT, Equipment, etc)Company Code: 3310 | Data is validated. Next screen General Data screen is displayed. |  |
| 4 | Insert General Data | Make the following entries (if the contract is relevant for valuation) and choose Partners to go to the next screen:Contract Name: <Your contract name>Contract Currency: AED as defaultedNote The company code currency is defaulted here. It’s allowed to be changed to a different currency.Valuation Relevance: Leasing ValuationNote If you also use IFRS, please refer to the section Create Contract in scope item 21P - Lease-In Accounting – Group Ledger IFRS for further guidance. | Datais validated.The Partners screen is displayed. |  |
| 5 | Assign New Partner | Choose Assign New Partner. Choose Supplier (Fin.Accounting).Make the following entries and choose Continue.Select the BP Role.Choose Go.Business Partner: <Business Partner number> (for example, 33300001) | Data is validated.The Business Partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries:Contract start date: <Your contract start date>1st Contract End: <Your contract end date>Press Enter and choose Continue in the Correct Cash Flow From view. | The data is validated and Cash Flow From date is filled.The Term has been created. |  |
| 7 | Insert Contract Objects | Choose Objects.Choose Assign and select one of options below.Option 1:Select COB Contract Object and choose OK.Contract Object: <Your description of the contract object> (for example, COB)Object Type: <Select a contract object type>Note Choose object type in accordance with the Contract Type you selected.For Lease In Real Estate contract type, use the following objects:Land/PropertyBuildingLocation/SiteFloorRoomFor Lease In Others contract type, use the following objects:DP/HardwareFixtures FittingsMachineryVehiclesBuilding EquipmentOffice EquipmentAccount Assignment: <Select a cost center for a account assignment> for example, CTR A000/33101101Option 2:Select GRO Gen. Rental Obj and choose OK. For details, see 7AD Create Rental Object – MDS.Note Choose on the following dependent of the underling usable object:Usable Object with portfolio structureUsable Object without portfolio structureObject Type of Assigned Object: J7 (for details, see 7AD) | Data is validated.The Object screen is displayed. |  |
| 8 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.For each condition make the following entries:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note The currency in Contract Currency of General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Postings.Note If a foreign currency is used in Contract Currency under tab General Data or in Currency under tab Conditions, select a currency translation rule in the field below.CrcyTrRule: <Select a rule>Tax Group: <Your default tax group>, for example, Y-FULLNote Default tax group can be set by configuration step Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_8) [page ] 10.Note If Registration for Indirect Taxation Abroad (RITA) is activated in your system, a new field AltTaxCnty is available for selecting a different country. The tax code of the newly selected country will be applied.If RITA is not activated in your system, the field AltTaxCnty is invisible. In this case, you can disregard the field AltTaxCnty below.For more information on activating RITA, please refer to J58 - Accounting and Financial Close - Preliminary Steps - Activate Registration for Indirect Taxation Abroad (Optional).AltTaxCnty: <Select a country> for example, NLChoose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Under Enhancements: <Select a business place> for example, DXBChoose Continue.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract.Choose Simulate to simulate the cash flow.Choose Back to Conditions.Note Make sure the contract type, object type and condition type are matched. For example, if contract type is Lease in Real Estate, condition type should be YCO01 Land/Property or YCO02 Building, condition type should be RE land or RE building related. | Data is validated.Cash flow is simulated |  |
| 9 | Activate Contract | Choose Activate to activate your contract.Choose Yes to activate your contract. | A message to execute the activation is shown. The contract is activated. |  |

Explanation of condition types:

Choose Lease In Rate <Underling Asset dependent> when the lease payment relates to the rent of the Asset:

- Lease In Rate Machinery
- Lease In Rate Fixtures and Fit
- Lease In Rate Vehicles
- Lease In Rate DP/Hardware
- Lease In Rate Office Equipment

Choose Lease In Service Charge <Underling Asste dependent> when the lease payment relates to a service which you don’t want to book on the Balance Sheet:

- LI Service Charge Machinery
- LI Service Charge Fixt.&Fit.
- LI Service Charge Vehicles
- LI Service Charge DP/Hardware
- LI Serv. Charge Office Equip.
- Asset Retirement

a. Used in Sub-lease, please refer to chapter Maintain Contract - Main Contract in scope item 2SB - Lease-Out for Sublease Accounting for detailed procedures.

b. To reflect the sub-lease-contract during asset capitalization, it is required to enter the total amount of rent income as statistical condition (Condition type LG92) on the main-lease contract (Asset retirement). This condition will reduce the asset capitalization.

#### Contract Renewal

##### Maintain Renewal Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can renew an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1: Contract Management Fiori App (F5273)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Management (F5273). | The Contract Management screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Go:Company Code: 3310Contract: <Your contract>Choose the line of the contract to expand it. | Contract is in edit mode. |  |
| 4 | Insert Renewal | Note Before you make any change, please make sure the contract is already activated.Choose Edit.Choose Term Rule.In the Renewal Rules area, choose Create, then make the following entries:Name of Term: <Input the name>Renewal Type: Individual Renewal RuleAutomatic Renewal Type: for example, One or More RepetitionsSequence: <Your renewal sequence>, for example, 1Option/Automatic: <Choose either Option or Automatic according to your needs>Number of Renewals: <Your renewals number>, for example, 1Rnewed Years: <Your renewal years>, for example, 3Rounding of Renewal: Month-EndChoose Apply. | Data is validated. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated.Next screen General Data screen is displayed. |  |
| 4 | Insert Renewal | Note Before you make any change, please make sure the contract is already activated.Choose Term.Choose Create Term, then choose Renewal.Make the following entries:Renewal Type: Individual Renewal Rule and choose Append Row.Option/Automatic: <Choose either Option or Automatic according to your needs>Seq: <Your renewal sequence>, for example, 1Number: <Your renewals number>, for example, 1RnwYrs: <Your renewal years>, for example, 3NtfY: <Your notification years>, for example, 1Choose Save.Choose Back. | Data is validated. |  |

##### Execute Renewal Option (Single Contract)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can renew an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1: Manage Contract Term (F6580)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Term (F6580). | The Manage Contract Term screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Go:Company Code: 3310Contract: <Your contract>Choose the line of the contract to expand it. | Contract is in display mode. |  |
| 4 | Perform Renewal | Note Please make sure the contract is already activated and in display mode.Choose Renewal.Select the renewal option and Perform Renewal. In the Perform Renewal dialog box, make the following entries:Note Automatic renewal does not require either approval or activation. Only Option renewal requires.Approved/Rejected: ApprovedDecided On: <Enter the date>Renewal Active: <Select>Choose Perform Renewal.Choose Back. | Data is validated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Perform Renewal | Note Before you make any change, please make sure the contract is already activated.Note Automatic renewal does not require either approval or activation. Only option renewal requires.Choose Term.In the Overview section of tab Term, make sure the Renewal term category entry is selected.Choose Renew Contract.Choose Approve and Activate. | The contract is renewed. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Reverse Renewal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can renew an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1: Manage Contract Term (F6580)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Term (F6580). | The Manage Contract Term screen displays. |  |
| 3 | Real Estate Contract | Make the following entries.Company Code: 3310Contract: <Your contract>Choose Go and click the line of the contract to expand it. | The Contract Management view displays. |  |
| 4 | Perform Renewal | Note Please make sure the contract is already performed and in display mode.Choose Renewal.Select the renewals option and Reverse Renewal.Note Automatic renewal does not require either performance or reversal. Only Option renewal requires. | The performed renewal is reversed. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Reverse Renewal | Note Before you make any change, please make sure the contract is already activated and has active renewals.Choose Term.Select the entry with Renewal cateogory by double-clicks. Then choose Renew Contract on the Renewal tab.Choose Reverse Renewal on the next screen.Approved/Rejected: <blank>Decided On: <blank> | The performed renewal is reversed. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Execute Renewal Option (Multiple Contract)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can renew several existing contracts at the same time as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Renewal of Contracts - Information System (REISCNRN). |  |  |
| 3 | Real Estate Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Information System: Renewal of Contracts - Approve and Activate Contracts | Mass select the contracts which you would like to active together, then choose Approve and Activate.Note The Renewal active must be ticked for the contracts you selected.Then save. | Renewal of contracts are approved and activated. |  |
| 5 | Information System: Renewal of Contracts - Reverse contracts | Mass select the contracts which you would like to reverse renewal together, then choose Reverse Renewal.Note The Renewal active must be blank for the contracts you selected. | Renewal of contracts are reversed. |  |

#### Contract Notice

##### Maintain Notice Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can maintain notice rule for your contract objects.

Procedure

Option 1: Contract Management Fiori App (F5273)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Management (F5273). | The Contract Managementscreen displays. |  |
| 3 | Process Contract | Make the following entries and choose Go:Company Code: 3310Contract: <Your contract>Click on the line of the contract to expand it. | Data is validated, and next screen Contract Management screen is displayed. |  |
| 4 | Maintain Notice Rule | Choose Edit.Choose Term Rule.In the Notice Rule area, expand the existing notice rule and make the following entries:Notice Type: Individual Notice ProcedureChoose Create for Period Rule, then make the following entries:Option 1:Notice Rule Name : <Your notice rule name>Notice Type: Individual Period RegulationParty Giving Notice: BothNotice Per: End of the MonthOption 2:Notice Rule Name : <Your notice rule name>Notice Type: Individual Deadline RegulationParty Giving Notice: BothNotice Month: <Your notice month>Notice Date: <Your notice date>Received in Month: <Your notice month>Received on Day: <Your notice date>Grace Period in Calendar/Business Days: <Your Grace Period in Calendar/Business Days>Calendar for Receipt Calculation: <Your Calendar for Receipt Calculation>Choose Apply twice. | Data is validated.The notice rule is added. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Process Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Maintain Notice Rule | Choose Term.Choose the line of notice, and make the following entries:Notice Type: Individual Notice ProcedureChoose Create Notice Rule, then choose Individual Period Regulation.Make the following entries:Option 1:Party Giving Notice: BothNotice Per: End of MonthOption 2:Notice Type: Individual Deadline RegulationNotice Rule Name :: <Your notice rule name>Party Giving Notice: BothChoose Expert Mode.Choose Append Row.NtMo: <Your notice month>NDay: <Your notice date>RMo.: <Your notice month>RDay: <Your notice date>C/B: <Your Grace Period in Calendar/Business Days>Cal: <Your Calendar for Receipt Calculation>Choose Simulate to go to the next screen.Choose Close to close Simulate Notice.Choose Continue. | Data is validated.The notice rule is added. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Give Notice (Single Contract)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can give notice for a contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

Option 1: Manage Contract Term Fiori App (F6580)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Term (F6580). | The Manage Contract Termscreen displays. |  |
| 3 | Process Contract | Note Before you make any change, please make sure the contract is already activated.Make the following entries and choose Go:Company Code: 3310Contract: <Your contract>Click on the line of the contract to expand it. | Data is validated, and next screen Manage Contract Term screen is displayed. |  |
| 4 | Add and Activate Notice | Choose Edit.Choose Notice.In the Notices area, choose Create and make the following entries:Subject of Notice: Give Notice on ContractNotice Given By: ContracteeNotice Per: <End of the month>Reason for Notice: <Select the reason>Choose Apply.Choose Save.In display mode, select the created entry of notice and choose Activate Notice.Note The date of Notice per must be between contract start and contract end.Note Once the notice is given, the system status CANC is activated. | Data is validated.The notice is activated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Process Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Add Notice on Objects | Choose Term.Choose the line of notice, then choose Give Notice.Choose Create Notice, then choose Give Notice on Contract.Reason for Notice: 90Choose Activate Selected Notice to close activate notice.Choose Save.Note The date of Notice per must be between contract start and contract end.Note Once the notice is given, the system status CANC is activated. | Data is validated.The notice is activated. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Reverse Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can reverse a notice given for your contract objects.

When reversing the notice for a contract, the notice must be given.

Option 1: Manage Contract Term Fiori App (F6580)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Term (F6580). | The Manage Contract Term screen displays. |  |
| 3 | Process Contract | Note Before you make any change, please make sure the notice has been given.Make the following entries and choose Go:Company Code: 3310Contract: <Your contract>Click on the line of the contract to expand it. | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Deactivate Notice | Choose Notice and select the entry of notice.Choose Deactivate Notice to close activate notice.Note Once the given notice is reversed, system status CANC is removed from the contract and the contract is activated again. | The notice is deactivated. |  |
| 5 | Delete Notice | Choose Edit.Select the entry of notice and choose Delete.Choose Save. | The notice is deleted. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Process Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract>Choose Yes for the message: System status CANC is active, Perform the activity anyway? on the screen RE: Change object. | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Reverse Notice | Choose the Term tab.Select the row for notice, then choose Give Notice.Choose Yes for the message: System status CANC is active, Perform the activity anyway? on the screen RE: Change object.Choose Reverse Selected Notice to reverse notice.Note Once the given notice is reversed, system status CANC is removed from the contract and the contract is activated again. | Data is validated.The Notice is reversed. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Notice on Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can give a notification to your contracts.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Notice on Contracts - Information System (REISCNNT). | The Information System: Giving Notice on Contracts screen displays. |  |
| 3 | Activate Notice or Reverse Notice | Make the following entries.Company Code: 3310Contract: <Your contracts>Option 1:Contacts with Notice: <Select>Notice Active: <Selected as defaulted>Notice Inactive: <Selected as defaulted>Choose Execute. Your contracts which are notice given can be displayed.Then you can activate the given notice by:Selecting the contracts which notice are not active, choose Activate Notices, and then choose Save.Or you can reverse the given notice by:Selecting the contracts which notice are already activated, choose Reverse Notices, and then choose Save.Option 2:Contacts w/ No Notice Given: <Select>Choose Execute. Then your contracts which are no notice given can be displayed.Select the contracts, choose Activate Notices, and make the following entries:Notice Per: <Your notice date>Reason for Notice: 90Choose Continue.Choose Save. Then the notice of contracts are activated.Select above contracts and choose Reverse Notices, and then choose Save. | Notices are activated or deactivated. |  |

#### Reminder for Contracts

##### Maintain Reminder Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To execute this activity, go step by step through the table.

Option 1: Contract Management Fiori App (F5273)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Management (F5273). | The Contract Management screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Edit:Company Code: 3310Contract: <Your contract> | Contract is in edit mode. |  |
| 4 | Insert Reminder Rule | Choose Reminder.In the Reminder Rule area, choose Create and make the following entries.Reminder Rule: As of date … every … months (C01)Reminder Reason: General Reminder (Y001)Start Date: <Contract start date>Interval in Months: 1Choose Apply. | Data is validated. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Insert Reminder | Choose Resubmission.Choose Create Reminder Rule (for example, Before End of Term).For each reminder rule, make the following entries and choose Continue:Resubmission reason: <Select a reason>Then choose Save and go to the next screen. Choose Back. | Data is validated. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

##### Process Reminder

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Option 1: Contract Management Fiori App (F5273)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Management (F5273). | The Contract Management screen displays. |  |
| 3 | Process Contract | Make the following entries and choose Go:Company Code: 3310Contract: <Your contract> | Your contract is displayed. |  |
| 4 | Process Reminder | Check the header of your contract. If there are critical open reminders, the number will be displayed.Choose Edit then choose Reminder Date.Select an (overdue) open reminder date and press Clear. | Data is validated.The reminder is processed. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

Option 2: Manage Contract Web Gui App (RECN)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Process Reminder | Choose Resubmission.Select an (overdue) open reminder date and choose Designate As Completed. | Data is validated.The reminder is processed. |  |
| 5 | Save Contract | Choose Save. | Data is validated. |  |

#### Print General Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you print general correspondence for existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Print: General Correspondence (RECPA400). | The Print general correspondence screen displays. |  |
| 3 | Create General Correspondence | Make the following entries and choose Run:Under ContractCompany Code: 3310Contract: <Your contract>Under Correspondence data:Data Select. KeyDate: <Actual date>Print Date: <Actual date>Under Text editor:<Your text> | Data is shown. |  |
| 4 | General Correspondence Overview | Select a document and choose Print Preview.Select an output item and choose Display Document.Choose Close to close the PDF version.Choose Back and choose the Print selected documents icon. | General correspondence output via OM. |  |

#### Reports Contract Management

##### Contract and Lease Management Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract and Lease Management Dashboard (F4555). | The Contract and Lease Management Dashboard screen displays. |  |
| 3 | Report Contract | Check the information diaplayed on the dashboard. | Data is shown. |  |

##### Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contracts - Information System (REISCN) . | The Info System: Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> | Data is shown. |  |

##### Conditions for Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Conditions for Contracts - Information System (REISCDCN). | The Info System: Conditions for Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <select> | Data is shown. |  |

##### Business Partners of Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Business Partners of Contracts - Information System (REISCNBP). | The Information System: Business Partners of Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and press Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> | Data is shown. |  |

##### Objects for Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Objects for Contracts - Information System (REISCNOA). | The Information System: Objects for Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> | Data is shown. |  |

##### Term of Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Term of Contracts - Information System (REISCNPE). | The Information System: Term of Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and press Run:Company Code: 3310Contract: <Your contract(s)>Use grid control: <Select> | Data is shown. |  |

##### Memos of Contract - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts to check the added memos.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Memos of Contract - Information System (REISCNMEMO) . | The Information System: Contracts Memos screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use grid control: <Select> |  |  |

##### Contract Change Documents - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of change documents as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Change Documents - Information System (REISCHGDOCCN). | The Info System: Change Documents for Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and press Run:Company Code: 3310Contract: <Your contract(s)>In Type of Data Change section:Change: <Select>Use Grid Control: <Select> | Change log is displayed for the contract(s). |  |

##### Real Estate Contract Validity Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report to check real estate contract validity as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Real Estate Contract Validity Report (W0200). | The Valid Contract Report screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Go:Validity Start: <Enter the desired date>Validity End: <Enter the desired date> | Company code and contract numbers which are valid during this period can be shown. |  |
| 4 | Report Contract | Select the available fields from the left side of the screen and choose Add to Row axis or Add to Columns axis. For example, choose field Real Estate Contract and select Add field Real Estate Contract to Row axis. | Field contract number is added to the report. |  |

##### Real Estate Contract Object Assignment Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report to check real estate contract object assignment as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Real Estate Contract Object Assignment Report (W0201). | The RE Contract Subject Assignment screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Go:Validity Start: <Enter the desired date>Validity End: <Enter the desired date> | Data is shown. |  |

### Contract Valuation

#### Maintain Valuation Rule

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
| 2 | Access the SAP Fiori app | Open Valuation Management (F6170). | The Valuation Management screen displays. |  |
| 3 | Edit Contract Valuation | Input your contract number in search field and choose Go.Select the contract and choose Edit.Choose Create on the valuation tab.Make the following entries and choose Apply:Valuation Rule: <the relevant valuation principle> (for example, Group United States GAAP FL)Object Identification: <COB or GRO you created in chapter Create Contract>Start of Consideration: <defaulted by contract start date>Object type of assigned object: <defaulted in case object identification is a usable object otherwise e.g. cost center>Accounting Object ID: <defaulted in case object identification is a usable object otherwise select a cost center>Note The entry only has to be maintained if you want to use a different accounting object.Interest Rate: <Your interest rate> | The valuation rule is created. |  |
| 4 | Save contract | Choose Save. | Data is saved. |  |
| 5 | Complete Valuation Rule | Select your valuation rule and click Complete. | Valuation rule is completed. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Valuation (RECECN). | The Contract screen displays. |  |
| 3 | Edit Contract Valuation | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen Valuation Parameters screen is displayed. |  |
| 4 | Update Valuation Parameters | Make the following entries and choose Create Term.Valuation parameter: <the relevant valuation principle> (for example, Group United States GAAP FL)Acct. Assignment: as objectInterest Rate: <Your interest rate> | Data is validated.Valuation rule can be completed.The Valuation parameters screen is displayed |  |
| 5 | Complete Valuation Rule | Select your valuation rule and click on Rule Complete.Please ignore the warning message below:Caution IFRS1: Valuation is pending and still needs to be completed. | Valuation rule is completed. |  |
| 6 | Save Contract | Choose Save. | Data is validated. |  |

#### Valuation Cashflow

##### Generate Valuation Cashflow (Single Contract)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can perform contract valuation as part of your daily business.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Valuation Management (F6170). |  |  |
| 3 | Perform Valuation | In the Serach field, enter the contract number that has a completed valuation rule and open valuation status and choose Go.Select the contract and choose Perform. | The valuation status is changed to Complete. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Contract Valuation (RECECN). | The Contract view is displayed. |  |
| 3 | Edit Contract Valuation | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | The Valuation Parameters view is displayed. |  |
| 4 | Perform Valuation | Choose the Valuation tab.Select the valuation rule then choose Perform Valuation. | The Valuation result view is displayed. |  |

##### Reverse Valuation Step

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can cancel already performed valuations of an existing contract as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Steps (RECEPRRV). | The Reverse Contract Valuation screen displays. |  |
| 3 | Cancel Valuation Steps: Contracts Selection | Make the following entries and choose Run:In the Contract Selection area:Company Code: 3310Contract: <Your contract>OrIdentification: <Identification>Execution Mode area:Execution Mode: Simulation | The Reverse Contract Valuation view is displayed. |  |
| 4 | Cancel Valuation Steps: Contracts Selection | Choose Exit.Change Execution Mode to Update Run.Choose Execute. | The Cancel Valuation steps view is displayed. |  |
| 5 | Cancel Valuation Steps | To check the contract valuation reversal, choose Log.Choose Back. |  |  |
| 6 | Cancel Valuation Steps | All contracts are selected. Choose Deselect to deselect a contract and valuation steps. Choose Save. | Valuation steps are deleted. |  |
| 7 | Cancel Valuation Steps | Choose Back. | The valuation is canceled. |  |

##### Perform Contract Valuation – Mass Processing

###### Perform Contract Valuation - Mass Processing (Simulation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the generation of valuation for an existing contract as part of your daily business. Usually, the valuation is generated once the valuation rule is completed for an active contract.

When a contract valuation is generated, it is useful to first simulate the generation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Perform Contract Valuation - Background Job (F6277). | The Application Jobs view is displayed. |  |
| 3 | Perform Contract Valuation Selection | Choose Create to add a job. | The Job Details view is displayed. |  |
| 4 | Perform Contract Valuation Selection | Make the following entries and choose Step 2:Job Template: Perform Contract ValuationJob Name: Perform Contract Valuation |  |  |
| 5 | Perform Contract Valuation Selection | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Contract Valuation Selection | Make the following entries and choose Schedule:Company Code: 3310Contract: <Your contract>Execution Mode: SimulationView: Process |  |  |
| 7 | Check Contract Valuation Simulation Result | Choose Go to refresh the view until the job is finished. | The Job result is attached. |  |
| 8 | Check Contract Valuation Simulation Result | Choose Navigate to the job results. | Contract valuation simulation result is correct.The Contract Valuation Simulate view is displayed. |  |
| 9 | Check Contract Valuation Simulation Result | Choose Back. |  |  |

###### Perform Contract Valuation - Mass Processing (Update Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update the generation of valuation for an existing contract as part of your daily business. Usually, the valuation is generated once the valuation rule is completed for an active contract.

When a contract valuation is generated, it is used to execute the generation in update mode.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Perform Contract Valuation - Background Job (F6277). | The Application Jobs view is displayed. |  |
| 3 | Perform Contract Valuation Selection | Choose Create to add new job. | The Job Details view is displayed. |  |
| 4 | Perform Contract Valuation Selection | Make the following entries and choose Step 2:Job Template: Perform Contract ValuationJob Name: Perform Contract Valuation |  |  |
| 5 | Perform Contract Valuation Selection | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Contract Valuation Selection | Make the following entries and choose Schedule:Company Code: 3310Contract: <Your contract>Execution Mode: Update RunView: Process |  |  |
| 7 | Check Contract Valuation Update Run Result | Choose Go to refresh the view until the job is finished. | The Job result is attached. |  |
| 8 | Check Contract Valuation Update Run Result | Choose Navigate to the job results. | Contract valuation simulation result is correct.The Contract Valuation Simulate view is displayed. |  |
| 9 | Check Contract Valuation Update Run Result | Choose Back. |  |  |

#### Valuation Posting

##### Periodic Valuation Posting

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs view is displayed. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job. | The Job Details view is displayed. |  |
| 4 | Perform Periodic Valuation Posting | Make the following entries and choose Step 2:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation run |  |  |
| 5 | Perform Periodic Valuation Posting | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Periodic Valuation Posting | Make the following entries and choose Schedule:Company Code: 3310Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help. Select before or on from the Include dropdown list. Choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: SimulationDocument Date: <Your document date> |  |  |
| 7 | Check Contract Valuation Simulation Result | Refresh Go until the job is finished. | The Job log and job result are attached. |  |
| 8 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting simulation result is correct. |  |
| 9 | Check Contract Valuation Simulation Result | Choose Back. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Periodic Valuation posting - Background job (F4608). | The Application Jobs view is displayed. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add a job. | The Job Details view is displayed. |  |
| 4 | Perform Periodic Valuation Posting | Make the following entries and choose Step 2:Job Template: Leasing contract: Periodic valuation runJob Name: Leasing contract: Periodic valuation run |  |  |
| 5 | Perform Periodic Valuation Posting | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Periodic Valuation Posting | Make the following entries and choose Schedule:Company Code: 3310Contract Type: <Your contract type> orContract: <Your contract>Month for Posting Run: <the month for posting run>Year for Posting Run: <the year for posting run>Due Date: <before or on last date of posting month>Note Choose the search help. Select before or on from the Include dropdown list. Choose OK.Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <Your posting date>Posting Period: <Your posting period>Posting Run Mode: Update RunDocument Date: <Your document date> |  |  |
| 7 | Check Contract Valuation Update Run Result | Choose Go to refresh the view until the job is finished. | The Job log and job result are attached. |  |
| 8 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Contract valuation posting result is correct. |  |
| 9 | Check Contract Valuation Update Run Result | Choose Back. |  |  |

##### Reverse Valuation Posting

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs view is displayed. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add a job. | The Job Details view is displayed. |  |
| 4 | Perform Periodic Valuation Posting | Make the following entries and choose Step 2:Job Template: <as defaulted>Job Name: <as defaulted> |  |  |
| 5 | Perform Periodic Valuation Posting | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Periodic Valuation Posting | Make the following entries and choose Schedule:Company Code: 3310Contract: <Your contract>Reason for Reversal: <Your reason> for example, Wrong PeriodMode: Simulation |  |  |
| 7 | Check Contract Valuation Simulation Result | Choose Go to refresh the view until the job is finished. | The Job log and job result are attached. |  |
| 8 | Check Contract Valuation Simulation Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed. Contract valuation posting is displayed. |  |
| 9 | Check Contract Valuation Simulation Result | Choose Back. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing |  |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation Posting - Background Job (F6276). | The Application Jobs view is displayed. |  |
| 3 | Perform Periodic Valuation Posting | Choose Create to add new job. | The Job Details view is displayed. |  |
| 4 | Perform Periodic Valuation Posting | Make the following entries and choose Step 2:Job Template: <as defaulted>Job Name: <as defaulted> |  |  |
| 5 | Perform Periodic Valuation Posting | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Perform Periodic Valuation Posting | Make the following entries and choose Schedule:Company Code: 3310Contract: <Your contract>Reason for Reversal: <Your reason> for example, Wrong PeriodMode: Update Run |  |  |
| 7 | Check Contract Valuation Update Run Result | Choose Go to refresh the view until the job is finished. | The Job log and job result are attached. |  |
| 8 | Check Contract Valuation Update Run Result | Choose Navigate to the job logs.Choose Navigate to the job results. | Job logs are displayed.The reversal document of valuation posting is posted and displayed. |  |
| 9 | Check Contract Valuation Update Run Result | Choose Back. |  |  |

#### Periodic Activities

##### Asset Clearing Reconciliation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report to show postings on asset clearing account by selecting various contracts as part of your daily business.

In most of the cases the asset clearing account is balanced. The valuation posting of the asset cashflow generates a debit posting and a credit posting to the account with the same amount. For more information about this report, please refer to SAP Note [3006815](https://me.sap.com/notes/3006815).

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Asset Clearing Reconciliation (RECEASCLEARRECON). | The Asset clearing account reconciliation screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your Contract(s)> |  |  |

##### Reclassification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reclassification - Information System (RECEISRECLASSIFY). | The Info System: Reclassification displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Sort Method: SAP SAP(EU 93 fin.stat.guidelines)Key Date: <Your key date> |  |  |

##### Liabilities Grading

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Liabilities Grading - Information System (RECEISLIABGRAD). | The Info System: Display Liabilities Grading displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Start Date: <Your start date>Sort Method: SAP SAP(EU 93 fin.stat.guidelines)Note When US_GASB_MA (Modified accrual) UGSM account principle is used, there is no liability recognized. | Data is shown. |  |

##### Deactivate Leased Assets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the deactivation of a RoU asset for an existing contract as part of your daily business.

To ensure that a ROU asset can be deactivated, the following conditions must be met:

- The maximum contract end date (including renewal options) must be reached.
- There must not be any open valuation for the asset.
- The useful life of the asset must have expired.
- There must not be any cash flow planned items for the asset.
- If the asset is assigned to the last time slice of the valuation rule, all valuation cash flow records for this valuation rule must have been posted.

Procedure

When a contract valuation is posted, the leased RoU asset is activated.

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Deactivate Leased Assets (RECEASSETDEACT). | The Deactivate Leased Assets view displays. |  |
| 3 | Deactivate Leased Assets Selection | In the Contract Selection area, make the following entries:Company Code: 3310Contract: <Your contract>In the Filter area, make the following entry:Status Selection Active: <Select> (As defaulted)In the Output options area, make the following entries:Report Title: Deactivate Leased AssetsLayout: 0STANDARD (As defaulted)Use Grid Control: <Select> (As defaulted)In the Selection area, make the following entries:Assets for Contracts: <Select> (As defaulted)Assets for Object Groups: <Select> (As defaulted)Assets for Concrete Objects: <Select> (As defaulted)Only Assets That Can Be Deact.: <Select> (As defaulted)Specify Default Deactivation: <Select> (As defaulted)In the Posting area, make the following entries:Month for Posting Run: <The month to deactivate the asset>Year for Posting Run: <The year to deactivate the asset >Document Header Text: <Your Document Header Text>Deactivation Date: <Your deactivation date>Posting Date: <Your posting date>Document Date: <Your document date>Posting Period: <Your posting date>Execution Mode: SimulationChoose Run. | Data is validated. The Deactivate Leased Assets: Simulation view is displayed. |  |
| 4 | Deactivate Leased Assets - Simulation | Choose the entry to be deactivated. Choose Simulate. | The simulation data is shown. |  |
| 5 | Deactivate Leased Assets - Update | Choose Back.Choose Switch Between Simulation/Update.Then choose Save. | The asset is deactivated. |  |
| 6 | Back | Choose Back to go back to homepage. |  |  |

##### Cancel Deactivation Leased Assets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate the cancellation of deactivation of a RoU asset for an existing contract as part of your daily business.

|  |
| --- |
| Note The chapter is applicable only if the leased asset is deactivated. |

Procedure

When a leased RoU asset is deactivated, you can cancel the deactivation of the asset.

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Cancel Deactivation Leased Assets (RECEASSETDEACTRV). | The Deactivate Leased Assets: Reversal view displays. |  |
| 3 | Deactivate Leased Assets Selection | In the Contract Selection area, make the following entries:Company Code: 3310Contract: <Your contract>In the Filter area, make the following entry:Status Selection Active: <Select> (As defaulted)In the Output options area, make the following entries:Report Title: Deactivate Leased Assets: ReversalLayout: 0STANDARD (As defaulted)Use Grid Control: <Select> (As defaulted)In the Selection area, make the following entries:Assets for Contracts: <Select> (As defaulted)Assets for Object Groups: <Select> (As defaulted)Assets for Concrete Objects: <Select> (As defaulted)In the Posting area, make the following entries:Reason for Reversal: <Your reason for reversal, for example, wrong period>Posting Date: <Your posting date>Posting Period: <Your posting date>Execution Mode: SimulationChoose Run. | Data is validated. The Deactivate Leased Assets: Simulation view is displayed. |  |
| 4 | Deactivate Leased Assets - Simulation | Choose the entry to be canceled. Choose Execute. | The simulation data is shown. |  |
| 5 | Deactivate Leased Assets - Update | Choose Back.Choose Switch Between Simulation/Update.Then choose Save. | The deactivation of asset is canceled. |  |
| 6 | Back | Choose Back to go back to homepage. |  |  |

#### Reports Valuation Management

##### Display Contract Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Display Contract Valuation (RECESH). |  |  |
| 3 | Report Contract | Make the following entries and choose Execute:Company Code: 3310Contract: <Your contracts>Output Options area:View: <Process or Cash flow>Currency: Valuation Currency (Defaulted) |  |  |

##### Valuation Balance - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Valuation Balance - Information System (RECEISBALANCE). | The Display Valuation Balances screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Currency: Valuation Currency (Defaulted) | Cash flow data for valuation in the Cash Flow Data for Valuation view is shown. |  |

##### Valuation Rules - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Valuation Rules - Information System (RECEISRULECN). | The Info System: Valuation Rules in Contracts view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Use grid control: <Select>Activity: <Display> (Defaulted) |  |  |

##### Condition Specific Valuation Rules for Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Condition specific valuation rules for Contracts - Information System (RECEISCONDRULECN). | The Info System: Condition-Specific Valuation Rules for Contracts view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Use grid control: <Select>Activity: <Display> (Defaulted) |  |  |

##### Assets for Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assets for Contracts - Information System (RECEISASSETCN). | The Info System: Leased Assets for Contracts displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)> | Data is shown. |  |

### Accounting

#### Periodic Posting

##### Periodic Posting - Simulation

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

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting - Background job (F4607). | The Application Jobs screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: 3310Input entry for either Contract Type or Contract:Contract Type: <your contract type>Contract: <Lease In contract number>In the Period selection area:Month for Posting Run: <The month for posting run>Year for Posting Run: <The posting year>Due date: <before or on the last day of the posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <The posting period>Posting Run Mode: SimulationType of Posting Run: Integrated Posting | Data is validated, and next screen Application Jobs screen displays. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are attached. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

##### Periodic Posting - Update Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update run the periodic posting of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting - Background job (F4607). | The Application Jobs screen displays. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting runChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: 3310Input entry for either Contract Type or Contract:Contract Type: <your contract type>Contract: <Lease In contract number>In the Period selection area:Month for Posting Run: <The month for posting run>Year for Posting Run: <The posting year>Due date: <before or on the last day of the posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <The posting period>Posting Run Mode: Update RunType of Posting Run: Integrated Posting | Data is validated, and next screen Application Jobs screen displays. |  |
| 4 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are displayed. |  |
| 5 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |
| 6 | Periodic Posting: Contract | Choose Back to go back. |  |  |

#### Reverse Contract Postings

##### Reverse Contract Postings - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate reversal documents for periodic posting of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: 3310Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: SimulationReason for reversal: <Your reason> for example, Wrong Period | Data is shown.Default mode is Simulation. You can change it to Update Run for execution. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log is generated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |

##### Reverse Contract Postings - Update

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
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Reverse Contract PostingsJob Name: Reverse Contract PostingsChoose Step 2.Start Immediately: SelectChoose Step 3.In the Document selection area:Company Code: 3310Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: Update RunReason for reversal: <Your reason> for example, Wrong Period | Data is shown.Default mode is Simulation. You can change it to Update Run for execution. |  |
| 4 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log is generated. |  |
| 5 | Reverse Postings | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |

#### Reports Accounting

##### Contract and Lease Cashflow Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract and Lease Cashflow Dashboard (F5379). | Data is shown. |  |

##### General Real Estate Posting Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you review the general posting for contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing or Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open General Real Estate Posting Log (RERAPL). | The Posting Log view displays. |  |
| 3 | General Real Estate Posting Log | Make the following entries as RE Document for Selection is checked by default:Process: <Your process to display the report>, for example, REPP Periodic Posting: Contracts or REEP Valuations for ContractsOrCheck FI Document for Selection, and make the following entries:Company Code: 3310User Name: <Your user name>Choose Run. | Data displays.Pay attention if you get RUNTIME ERROR: No more memory available to add rows to an internal table. Please add more selection criteria to narrow your search. |  |
| 4 | General Real Estate Posting Log | Validate the data and choose Back twice to exit the report. |  |  |

##### Documents for Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you review RE documents for contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Documents for Contracts - Information System (REISREDOCCN). | The Display RE Documents for Contracts view is displayed. |  |
| 3 | Document for Contracts | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s> |  |  |
| 4 | Document for Contracts | Choose Back twice. |  |  |

##### Item Overview - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Item Overview - Information System (REISRADOCITEM). | The Item Overview displays. |  |
| 3 | Item Overview | Make the following entries and press Run:Company Code: 3310Contract: <Your contract(s)>Open Items On: <Periodic Posting Date>Use Grid Control: <Select> |  |  |
| 4 | Item Overview | Choose Back twice to exit the report. |  |  |

##### Contract Cashflow Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Contract Cashflow Report (F5363). | The Real Estate Contract Cashflow Report screen displays. |  |
| 3 | Contract Cashflow | Make the following entries and choose Go:Cash Flow Origin: <as defaulted> for example, PExchange Rate Type: <as defaulted> for example, MDisplay Currency: <as defaulted> for example, AEDValidity Start: <as defaulted>Validity End: <as defaulted> | Data is shown. |  |
| 4 | Contract Cashflow | Choose Back to exit the report. |  |  |

##### Conditions for Contracts - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Conditions for Contracts - Information System (REISCDCN). | The Info System: Conditions for Contracts screen displays. |  |
| 3 | Conditions for Contracts | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> | Data is shown. |  |
| 4 | Conditions for Contracts | Choose Back twice to exit the report. |  |  |

##### Periodic Posting: Previous Period Comparison

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of periodic postings comparison between different months.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting: Previous Period Comparison (RERAPPCMP). | The Periodic Posting Contracts: Previous Period Comparison screen displays. |  |
| 3 | Compare Periodic Postings | Make the following entries:Company Code: 3310Contract: <Your contract>In the Comparison Mode section, choose between Comparison Only and Compar. and Posting.Option 1:If Comparison Only is chosen, make the following entries andchoose Execute:Calculation Period 1: <the first day of the selected month>To: <the last day of the selected month>Calculation Period 2: <the first day of the selected month>To: <the last day of the selected month>Note Data will be displayed only when the periodic posting is executed.Option 2:If Compar. and Posting is chosen, make the following entries and choose Execute:Calculation Period Comparison: <the first day of the selected month>To: <the last day of the selected month>Month for Posting Run: <the comparison month for posting run>Year of Posting Run: <the year for posting run>Posting Run Mode: SimulationType of Posting Run: Integrated postingIn the Output section, choose between Display All Records and Display Difference Only.Note If Display Difference Only is chosen, data will only be displayed when difference exists be-tween the month for comparison and the month to execute periodic posting.Check the data and choose back to go back.Posting Run Mode: Update RunChoose Run. | Differences are shown. Or posting result is displayed. |  |
| 4 | Compare Periodic Postings | Choose Back twice to exit the report. |  |  |

##### Lease and Real Estate Accounting Review Booklet (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With this app, you can review costs for your portfolio objects in Contract and Lease Management. The app provides an aggregated view of financial statements by combining predefined business pages grouped under the main areas of real estate and non-real estate portfolio objects. This collection of pages forms a review booklet that can be used to carry out a financial review. This gives you insights into your cost structures by comparing plan and actual costs using different time periods.

You can adjust the review booklet to your specific requirements and use it as the basis for creating a custom review booklet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Cost Accountant - Real Estate. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Lease and Real Estate Accounting Review Booklet (F8196). | The Lease and Real Estate Accounting Review Booklet screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Go:Ledger: <choose the required ledger, for example, 3L>Reporting Date: <the required reporting date>Company Code: 3310G/L Account Hierarchy: <choose the required hierarchy>Plan Category: PLN | Data displays. | The prerequisites to have data in this report are:To create a generic rental object via 7AD (Create Rental Object) and assign the rental object to your contract.Make periodic posting and valuation posting for your contract. |

### Adjustment

#### Maintain Adjustment Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you adjust the condition of an existing contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Manage Contract screen displays. |  |
| 3 | Process Contract | On the Contract screen, make the following entries and choose Change Object.Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data is displayed. |  |
| 4 | Assign Adjustment Rule | Choose Adjustment. There are two options to assign the adjustment rule.Option 1:Choose Create Term and select the adjustment rule Free - Modifiable for your contract.Choose the Conditions tab next to Free - Modifiable.Choose Assign Free Condition(s) to assign one of the conditions of the contract.Option 2:Choose the Create Term icon and select the adjustment rule Index - Modifiable United Arab Emirates for your contract.Choose the Unlink from Customizing icon and maintain your data.Base Year: <Your base year>Min. Change Pts: <Your point> orMin. Percent: <Your percent>Note Note Either input values for one of those fields or ignore the warning message Adjustment XX: the minimum change fields are not filled.If point is maintained in Min. Change Pts, please make sure the point maintained here is less than the difference between the points of the index series for the current date and the index level for the date the last time the condition was adjusted (Both points are maintained by SSC-UI Enter Index Levels in Preliminary Steps).If point is maintained in Min. Percent, please make sure the percent maintained here is less than the percentage difference between the points of the index series for the current date and the index level for the date the last time the condition was adjusted (Both points are maintained by SSC-UI Enter Index Levels in Preliminary Steps). The percentage difference is calculated on the basis of this absolute difference, using the following formula: difference * 100 / (index level at last adjustment).Index Start: <The first date of index level>First adjust. from: <Today>Remaining in Adjustment, choose Conditions.Choose Assign Free Condition(s) to assign one of the conditions of the contract.Choose Save. | Adjustment rule is assigned. |  |

#### Create Adjustment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you adjust the condition of the contract(s) as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Specify Adjustments (REAJPR). | The Specify Adjustments screen displays. |  |
| 3 | Process Contract | In the Specify Adjustments view, make the following entries and choose Change Object.Company Code: 3310Contract: <Your contracts>Note It’s available for you to execute adjustment against more than one contract.On the Procedure tab,If free adjustment rule is maintained in the contract, select Custom and make the following entries:Reason: <STANDARD Standard>Rule: <FREECN>If index adjustment rule is maintained in the contract, select Index and make the following entries:Reason: <STANDARD Standard>For free adjustment, choose Processing Paramet.Choose the Insert Row icon on the Custom tab, and make the following entries:%Increase: <Your increase percentage for free adjustment>, for example: 10.Choose Activity Parameters, and make the following entries on the Determine Adjustments tab.Next Possible Valid-From: <Select>Status of Contract: <Active Contracts>OccupancyContracts: <Select>Subject to Approval: <Both>Non-Occupancy Contracts: <Select>Subject to Approval: <Both>Choose Run. | Data is validated and the Specify Adjustments view is displayed. |  |
| 4 | Specify Adjustment | Choose Change from Simulation to Update Mode.Select the items, and choose the Activate Adjustment icon.Choose Save.Choose Exit twice to go back. | Log is displayed. |  |

#### Modify and Activate Adjustment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can make changes to the adjustment of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Continue Adjustment (REAJCH). | The Edit Adjustments screen displays. |  |
| 3 | Open Adjustment | Make the following entries:Identification: <Your Identification ID>Tab Activities:Activate Adjustments: <Selected>Choose Execute.Note Only inactive adjustment is displayed. | The details of the existed adjustment of your contract are shown. |  |
| 4 | Change Price of the Adjustment | Select the item displayed and choose Change Price, and make the following entry (Optional):Corrected Unit Price: <Your corrected unit price>Choose Continue. | The Adjusted Price is changed. |  |
| 5 | Activate the Adjustment | Select the item displayed and choose Activate Adjustment. | The selected adjustment is activated. |  |
| 6 | Save the Adjustment | Choose Save.Choose Exit twice to go back. | Adjustment is saved. |  |

#### Display Adjustment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display adjustment of contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Adjustments (REAJSH). | The Display Adjustments screen displays. |  |
| 3 | Display Adjustment | Make the following entry and choose Execute:Identification: <Your Identification ID>Choose Exit twice to go back. | Data is shown. |  |

#### Create Adjustment Letter

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create an adjustment letter based on an executed adjustment run to inform the contract partner (tenant) about the condition adjustment.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment Letters - Background Job (F7435). | The Application Jobs screen displays. |  |
| 3 | Adjustment Letter Creation | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: <Schedule Real Estate Adjustment Output>Job Name: <Schedule Real Estate Adjustment Output>Choose Step 2.Start Immediately: <Select>Choose Step 3.RE Process ID: <Enter the ID> orCompany Code: 3310Contract: <Your contract>Note If error message Sender email address can't be initial. displays, please maintain the company code email address data via SSC UI: Edit Addresses for Company Codes. | The Job Details screen displays. |  |
| 4 | Check the Job Details | Check the run details and choose Back to go back. | The Application Jobs screen displays. |  |

#### Manage Adjustment Letter Output

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you adjust the condition of the contract(s) as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Real Estate Output Requests (F7482). | The Manage Real Estate Output Request screen displays. |  |
| 3 | Choose the Output Request | Make the following entries and choose Go:Contract: <Your contract> orCompany Code: 3310 orProcess ID: <Your process ID> orAppl. Object Type: <Your Appl. Object Type> for example, RE Adjustment of Conditions | The data is displayed. |  |
| 4 | Check the Request Details | Choose the needed entry to check.Check Contract, Process, Adjustment and Output Item respectively for information.Under Output Item, adjust the column width to get column Display and Form Template displayed.Click Open File to display the PDF document.Close the PDF document.Choose the item to check Print Settings, General Information, Sender, Recipient, From Template and Log respectively for condition adjustment information. | Information about output request is displayed. |  |

#### Reports Adjustment

##### Adjustments on Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you adjust the condition of the contract(s) as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Adjustments on Contracts (REAJAHCN). | The Adjustments on Contracts screen displays. |  |
| 3 | Adjustments on Contracts | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract> | Contract(s) with adjustments is shown in the list. |  |
| 4 | Adjustments on Contracts | Choose Exit twice to go back. |  |  |

##### Cond./Adjustment Rule - Information System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run a report of existing contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cond./Adjustment Rule - Information System (REISCDCNAJ). | The Info System: Conditions for Adjust-ment Rule for Contract screen displays. |  |
| 3 | Conditions for Adjustment Rule for Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> | Data displays. |  |
| 4 | Conditions for Adjustment Rule for Contract | Choose Exit twice to go back. |  |  |

### Technical Transactions

#### Analyze Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can analyse logs as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Logs (RECALA). | The Analyze Logs screen displays. |  |
| 3 | Analyze Logs Selection | Make the following entries and choose Execute:User: <Own user ID> | Data is validated, and next screen Log Display is displayed. |  |
| 4 | Analyze Logs | Analyse data. | Data is shown. |  |
| 5 | Analyze Logs | Choose Exit twice to go back. |  |  |

#### Update Objects in Worklist - Background Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the update of the contracts as part of your daily business.

The prerequisite of this testing procedure is to create a contract, save it but not activate it.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Update Objects in Worklist - Background job (F5969). | The Application Jobs screen displays. |  |
| 3 | Update Objects in Worklist Seletion | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Update Objects in WorklistJob Name: Update Objects in WorklistChoose Step 2.Start Immediately: <Select>Choose Step 3.Person responsible: <Own user ID>Update Immediately: <Select> | Data is validated, and next screen Application Jobs screen displays. |  |
| 4 | Update Objects in Worklist | Choose Navigate to the job details and go to the next screen. | The Job Details screen displays. |  |
| 5 | Update Objects in Worklist: Job Detail | Check the run details and choose Back to go back. | The Application Jobs screen displays. |  |
| 6 | Update Objects in Worklist | Choose Back to go back. |  |  |

#### Check Contracts - Background Job

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can execute the job to check your contracts as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Check Contracts - Background job (F5968). | The Application Jobs screen displays. |  |
| 3 | Check Contracts | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Check ContractsJob Name: Check ContractsChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: 3310Person responsible: <Own user ID> | Data is validated, and next screen Application Jobs is displayed. |  |
| 4 | Check Contracts | Choose Navigate to the job details and go to the next screen. | The Job Details screen displays. |  |
| 5 | Check Contracts: Job Detail | Check the details and choose Back to go back. | The Application Jobs screen displays. |  |
| 6 | Check Contracts | Choose Back to go back. |  |  |

#### Cash Flow Update for Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can simulate and execute the update of the cash flow of existing contract as part of your daily business.

There are changes that do not result in a direct update of the cash flow.

- Changes to the measurements of contract objects
- A change to the validity of a contract object
- A change to a condition in a contract that refers to another contract, and so on.

To update the cash flow, you can

- Regular processing of worklists (App Worklist: Update Objects (RECARG))
- Execute Cash Flow Update for Contracts (RECDCGOL)

For more information, please refer to [SAP note 917843 - Consulting note: Cash flow update](https://me.sap.com/notes/917843).

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Update for Contract (RECDCGOL). | The Generation of Cash Flow for Contracts screen displays. |  |
| 3 | Cash Flow Update for Contracts Selection | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Simulation: <activated>Choose Exit to go back. | Data is validated, and next screen Cash Flow Generation for Contracts is displayed. |  |
| 4 | Cash Flow Update for Contracts: Detail | Make the following entries and choose Run:Simulation: <deactivated> | The Generation of Cash Flow for Contracts screen displays. |  |
| 5 | Cash Flow Update for Contracts | Choose Exit to go back. |  |  |

#### Generate Reminder Dates for Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can generate reminder dates of contracts as a periodically recurring task.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Generate Dates for Contracts (RECARSGENCN). | The Generate Reminder Dates for Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>In the Mode section, deselect the Simulation (No Changes) checkbox. | New dates will be generated when:The term of your contract must be over 5 years.Reminder rule of your contract is C01.The report must be run at the beginning of a new year or a new month, that depends on Interval in Months of your contract, after contract creation.Otherwise, no changes are necessary. |  |

#### Schedule Generic Rental Object Checks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can schedule job to check generic rental object as a periodically recurring task.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as either an Administrator - Real Estate Management or Administrator - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Generic Rental Object Check - Background Job (F7963). | The Check Generic Rental Objects screen displays. |  |
| 3 | Create Job | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Check Generic Rental ObjectsJob Name: Check Generic Rental ObjectsChoose Step 2.Start Immediately: SelectOrStart Immediately: UnselectJob Start: <Your job start time>Recurrence Pattern: <Your Recurrence Pattern>, for example, DailyEvery: for example, 1 day(s)On Non-Working Day: for example, No RestrictionChoose OK.Choose Step 3.In the Selection of generic rental objects area:Generic Rental Object: <leave it empty>Company Code: 3310Generic Rental Object Type: <Your generic rental object type, either ‘U’ for Usable Objects or ‘R’ for Rentable Objects>Optional: In the Check settings area:Check in Change Mode: SelectSave Necessary Changes: SelectNote In certain cases, running this check report can allow you to heal inconsistencies in generic rental objects. However, this is only possible in change mode. You can therefore select Check in Change Mode to run the check in change mode. If you want to persist these changes, you also need to select Save Necessary Changes. | Job created. |  |
| 4 | Check Job Log | Choose Navigate to the job details to and check the job log. | The detected inconsistencies are displayed in job log. |  |
| 5 | Back | Choose Back to go back. |  |  |

### Archive Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can archive an existing contract as part of your daily business. A contract can only be deactivated and archived, when the contract is not posted yet.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Manage Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Enter:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data is displayed. |  |
| 4 | Real Estate Contract | Go to: Contract > Activation and Term > DeactivateConfirm the message. | Message: Status was changed. |  |
| 5 | Real Estate Contract | Go to: Edit > Change Status > Archive > Set Deletion Flag | Message: Status was changed. |  |
| 6 | Save | Choose Entry to save your contract. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/lease-in-accounting-group-ledger-ifrs-21p-ae-test-script-797]]
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-lease-in-accounting-1t6-a]]
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-service-contract-21r-ae-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34N_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 195,531 chars in the whole document
