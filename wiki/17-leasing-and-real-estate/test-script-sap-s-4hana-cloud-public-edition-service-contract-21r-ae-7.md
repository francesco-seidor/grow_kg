---
id: 17-leasing-and-real-estate/test-script-sap-s-4hana-cloud-public-edition-service-contract-21r-ae-7
title: Test Script SAP S/4HANA Cloud Public Edition - Service Contract (21R_AE) (21R_S4CLD2608_BPD_EN_AE)
description: "Test script (21R, UAE localization, 2608) for Service Contract / lease contract management: config prerequisites, contract lifecycle, postings, adjustments, reports, archiving."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/lease-in-accounting]
aliases: [21R_S4CLD2608_BPD_EN_AE]
keywords: [Lease-In Accounting, lease contract management, contract creation, contract renewal, contract notice, contract reminders, periodic posting, reverse contract postings, rent adjustment, contract reports]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21R_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-799
topic: 17-leasing-and-real-estate/lease-in-accounting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Service Contract (21R_AE) (21R_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21R_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Lease-In Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Contract (21R_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232848801)

[2 Prerequisites 5](#_Toc232848802)

[2.1 System Access 5](#_Toc232848803)

[2.2 Roles 5](#_Toc232848804)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232848805)

[2.4 Preliminary Steps 7](#_Toc232848806)

[2.4.1 Default Value for Tax Rate per Contract Type 7](#_Toc232848807)

[2.4.2 Assign Tax Codes 9](#_Toc232848808)

[2.4.3 Assign Tax Code (for FI Document) 11](#_Toc232848809)

[2.4.4 Enter Index Level 12](#_Toc232848810)

[2.4.5 Maintain Residence Time 14](#_Toc232848811)

[2.4.6 Define Output Parameter Determination – General Letter 15](#_Toc232848812)

[2.4.7 Define Output Parameter Determination – Adjustment Letter 17](#_Toc232848813)

[3 Overview Table 19](#_Toc232848814)

[4 Test Procedures 23](#_Toc232848815)

[4.1 Contract Management 23](#_Toc232848816)

[4.1.1 Create Contract 23](#_Toc232848817)

[4.1.2 Contract Renewal 26](#_Toc232848818)

[4.1.2.1 Maintain Renewal Rule 26](#_Toc232848819)

[4.1.2.2 Execute Renewal Option (Single Contract) 28](#_Toc232848820)

[4.1.2.3 Reverse Renewal 30](#_Toc232848821)

[4.1.2.4 Execute Renewal Option (Multiple Contract) 32](#_Toc232848822)

[4.1.3 Contract Notice 33](#_Toc232848823)

[4.1.3.1 Maintain Notice Rule 33](#_Toc232848824)

[4.1.3.2 Give Notice (Single Contract) 36](#_Toc232848825)

[4.1.3.3 Reverse Notice 38](#_Toc232848826)

[4.1.3.4 Notice on Contracts 40](#_Toc232848827)

[4.1.4 Reminder for Contracts 42](#_Toc232848828)

[4.1.4.1 Maintain Reminder Rule 42](#_Toc232848829)

[4.1.4.2 Process Reminder 43](#_Toc232848830)

[4.1.5 Print General Correspondence 45](#_Toc232848831)

[4.1.6 Reports Contract Management 46](#_Toc232848832)

[4.1.6.1 Contract and Lease Management Dashboard 46](#_Toc232848833)

[4.1.6.2 Contracts - Information System 46](#_Toc232848834)

[4.1.6.3 Conditions for Contracts - Information System 47](#_Toc232848835)

[4.1.6.4 Business Partners of Contracts - Information System 48](#_Toc232848836)

[4.1.6.5 Objects for Contracts - Information System 49](#_Toc232848837)

[4.1.6.6 Term of Contracts - Information System 50](#_Toc232848838)

[4.1.6.7 Memos of Contract - Information System 51](#_Toc232848839)

[4.1.6.8 Contract Change Documents - Information System 51](#_Toc232848840)

[4.1.6.9 Real Estate Contract Validity Report 52](#_Toc232848841)

[4.1.6.10 Real Estate Contract Object Assignment Report 53](#_Toc232848842)

[4.2 Accounting 54](#_Toc232848843)

[4.2.1 Periodic Posting 54](#_Toc232848844)

[4.2.1.1 Periodic Posting - Simulation 54](#_Toc232848845)

[4.2.1.2 Periodic Posting - Update Run 56](#_Toc232848846)

[4.2.2 Reverse Contract Postings 58](#_Toc232848847)

[4.2.2.1 Reverse Contract Postings - Simulation 58](#_Toc232848848)

[4.2.2.2 Reverse Contract Postings - Update 59](#_Toc232848849)

[4.2.3 Reports Accounting 61](#_Toc232848850)

[4.2.3.1 Contract and Lease Cashflow Dashboard 61](#_Toc232848851)

[4.2.3.2 General Real Estate Posting Log 61](#_Toc232848852)

[4.2.3.3 Item Overview - Information System 62](#_Toc232848853)

[4.2.3.4 Contract Cashflow Report 63](#_Toc232848854)

[4.2.3.5 Conditions for Contracts - Information System 64](#_Toc232848855)

[4.2.3.6 Periodic Posting: Previous Period Comparison 65](#_Toc232848856)

[4.3 Adjustment 67](#_Toc232848857)

[4.3.1 Maintain Adjustment Rule 67](#_Toc232848858)

[4.3.2 Create Adjustment 69](#_Toc232848859)

[4.3.3 Modify and Activate Adjustment (Optional) 70](#_Toc232848860)

[4.3.4 Display Adjustment 71](#_Toc232848861)

[4.3.5 Create Adjustment Letter 72](#_Toc232848862)

[4.3.6 Manage Adjustment Letter Output 73](#_Toc232848863)

[4.3.7 Reports Adjustment 75](#_Toc232848864)

[4.3.7.1 Adjustments on Contracts 75](#_Toc232848865)

[4.3.7.2 Cond./Adjustment Rule - Information System 76](#_Toc232848866)

[4.4 Technical Transactions 77](#_Toc232848867)

[4.4.1 Analyze Logs 77](#_Toc232848868)

[4.4.2 Update Objects in Worklist - Background Job 78](#_Toc232848869)

[4.4.3 Check Contracts - Background Job 79](#_Toc232848870)

[4.4.4 Cash Flow Update for Contracts 80](#_Toc232848871)

[4.4.5 Generate Reminder Dates for Contracts 81](#_Toc232848872)

[4.5 Archive Contracts 82](#_Toc232848873)

## Purpose

Overview

Lease contracts describe contractual agreements between two partners: the lessor and the lessee. The lessor owns an asset, whereas the lessee has a right to use this asset during the period agreed in the lease contract. The lessee pays lease payments for the use of the asset, as agreed upon in the lease contract.

This scope item helps you standardize and automate your lease service credit contract management activities for real estate, as well as for machinery, equipment, vehicles, and computer hardware.

You can easily create new contracts and execute periodic postings for existing contracts.

You can change the supplier for existing contracts, as well as run reports of existing contracts as part of your daily business.

You can create reminder rules for every contract, for example, to check the contract conditions, the contract term, or the renewal options, helping you to save time and effort and free up capacity for more strategic tasks.

Leveraging the reporting functions enables you to make better and more informed lease management decisions.

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
| Contract Specialist - Leasing | SAP_BR_RECM_SPECIALIST | Leasing Contract Management / Leasing Contract Management - Sales-Based Rent | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |
| Accounts Payable Accountant - Leasing | SAP_BR_RECM_AP_ACCOUNTANT | Accounts Payable - Leasing | SAP_BR_RECM_AP_ACCOUNTANT |  |
| Administrator - Leasing | SAP_BR_RECM_ADMINISTRATOR | Administration - Leasing | SAP_BR_RECM_ADMINISTRATOR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Vendor | 3330000133300002 |  |  |
| Customer | 3310000133100002 |  |  |
| Cost Center | Any available cost center with company code relation, for example, 33101101 |  |  |
| Profit Center | Any available profit center, for example, YB600 |  |  |
| Functional Area | Any available functional area, for example, YB40 |  |  |
| Asset Class | 6210 FL Land6220 FL Building6230 FL Computer6240 FL Fixture & Fitt.6250 FL Machinery Fitt.6260 FL Vehicles6270 FL Office Equipment6310 OL Land6320 OL Building6330 OL Computer6340 OL Fixture & Fitt.6350 OL Machinery6360 OL Vehicles6370 OL Office Equipment |  |  |

For more information on creating master data objects, refer to the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNH | Create Profit Center - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

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

#### Assign Tax Code (for FI Document)

Purpose

In this configuration activity, you assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales and purchases. The tax code assignment is both country-dependent and time-dependent.

This assignment is required for FI documents to be read correctly in RE. This assignment is relevant, for example, for service charge settlement and input tax distribution.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease ManagementItem Name: Accounting Integration |  |  |
| 5 | Configure | In the Assign Tax Code (for FI Document) row, choose Configure. |  |  |
| 6 | Assign Tax Type and Tax Group | Enter Tax Type and Tax Group if they are blank (for example, Y1 and Y-NONE).Choose Save. | The tax code is assigned to the company code. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Tax Code (for FI Document) | Go to the Business Processes Configuration app and search for the following activity: Assign Tax Code (for FI Document).Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Type and Tax Group | Enter Tax Type and Tax Group if they are blank (for example, Y1 and Y-NONE).Choose Save. | The Tax Code is assigned to the company code. |  |

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

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_14) [page ] 23 | Contract Specialist - Leasing | Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Renewal |  |  |  |
| [Maintain Renewal Rule](#unique_15) [page ] 26 | Contract Specialist - Leasing | Contract Management (F5273); Manage Contract (RECN) | Contract can be renewed. |
| [Execute Renewal Option (Single Contract)](#unique_16) [page ] 28 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Existing contract can be renewed. |
| [Reverse Renewal](#unique_17) [page ] 30 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | The performed renewal can be reversed. |
| [Execute Renewal Option (Multiple Contract)](#unique_18) [page ] 32 | Contract Specialist - Leasing | Renewal of Contracts - Information System (REISCNRN) | Several contracts can be renewed at the same time. |
| Contract Notice |  |  |  |
| [Maintain Notice Rule](#unique_19) [page ] 33 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Notice rule can be maintained. |
| [Give Notice (Single Contract)](#unique_20) [page ] 36 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | You can give notice to a contract. |
| [Reverse Notice](#unique_21) [page ] 38 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Notice can be reversed. |
| [Notice on Contracts](#unique_22) [page ] 40 | Contract Specialist - Leasing | Notice on Contracts - Information System (REISCNNT) | You can give notification to your contract. |
| Reminder for Contracts |  |  |  |
| [Maintain Reminder Rule](#unique_23) [page ] 42 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder rule is maintained. |
| [Process Reminder](#unique_24) [page ] 43 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder is processed. |
| [Print General Correspondence](#unique_25) [page ] 45 | Contract Specialist - Leasing | Print: General Correspondence (RECPA400) | General correspondence for existing contracts can be printed. |
| Reports Contract Management |  |  |  |
| [Contract and Lease Management Dashboard](#unique_26) [page ] 46 | Contract Specialist - Leasing | Contract and Lease Management Dashboard (F4555) | You run a report of existing contracts. |
| [Contracts - Information System](#unique_27) [page ] 46 | Contract Specialist - Leasing | Contracts - Information System (REISCN) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_28) [page ] 47 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Business Partners of Contracts - Information System](#unique_29) [page ] 48 | Contract Specialist - Leasing | Business Partners of Contracts - Information System (REISCNBP) | You run a report of existing contracts. |
| [Objects for Contracts - Information System](#unique_30) [page ] 49 | Contract Specialist - Leasing | Objects for Contracts - Information System (REISCNOA) | You run a report of existing contracts. |
| [Term of Contracts - Information System](#unique_31) [page ] 50 | Contract Specialist - Leasing | Term of Contracts - Information System (REISCNPE) | You run a report of existing contracts. |
| [Memos of Contract - Information System](#unique_32) [page ] 51 | Contract Specialist - Leasing | Memos of Contract - Information System (REISCNMEMO) | You run a report of existing contracts. |
| [Contract Change Documents - Information System](#unique_33) [page ] 51 | Contract Specialist - Leasing | Contract Change Documents - Information System (REISCHGDOCCN) | You run a report of existing contracts. |
| [Real Estate Contract Validity Report](#unique_34) [page ] 52 | Contract Specialist - Leasing | Real Estate Contract Validity Report (W0200) | You run a report of existing contracts. |
| [Real Estate Contract Object Assignment Report](#unique_35) [page ] 53 | Contract Specialist - Leasing | Real Estate Contract Object Assignment Report (W0201) | You run a report of existing contracts. |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Posting - Simulation](#unique_36) [page ] 54 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_37) [page ] 56 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_38) [page ] 58 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update](#unique_39) [page ] 59 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |
| Reports Accounting |  |  |  |
| [Contract and Lease Cashflow Dashboard](#unique_40) [page ] 61 | Accounts Payable Accountant - Leasing | Contract and Lease Cashflow Dashboard (F5379) | You run a report of existing contracts. |
| [General Real Estate Posting Log](#unique_41) [page ] 61 | Contract Valuation Specialist - Leasing or Accounts Payable Accountant - Leasing | General Real Estate Posting Log (RERAPL) | You review the general posting for contracts. |
| [Item Overview - Information System](#unique_42) [page ] 62 | Accounts Payable Accountant - Leasing | Item Overview - Information System (REISRADOCITEM) | You run a report of existing contracts. |
| [Contract Cashflow Report](#unique_43) [page ] 63 | Accounts Payable Accountant - Leasing | Contract Cashflow Report (F5363) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_44) [page ] 64 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Periodic Posting: Previous Period Comparison](#unique_45) [page ] 65 | Accounts Payable Accountant - Leasing | Periodic Posting: Previous Period Comparison (RERAPPCMP) | You run a report of existing contracts. |
| Adjustment |  |  |  |
| [Maintain Adjustment Rule](#unique_46) [page ] 67 | Contract Specialist - Leasing | Manage Contract (RECN) | Condition of an existing contract can be adjusted. |
| [Create Adjustment](#unique_47) [page ] 69 | Contract Specialist - Leasing | Specify Adjustments (REAJPR) | Condition of an existing contract can be adjusted. |
| [Modify and Activate Adjustment (Optional)](#unique_48) [page ] 70 | Contract Specialist - Leasing | Continue Adjustment (REAJCH) | Adjustment of contracts can be modified. |
| [Display Adjustment](#unique_49) [page ] 71 | Contract Specialist - Leasing | Display Adjustments (REAJSH) | Adjustment of contracts can be displayed. |
| [Create Adjustment Letter](#unique_50) [page ] 72 | Contract Specialist - Leasing | Create Adjustment Letters - Background Job (F7435) | Adjustment letter can be created. |
| [Manage Adjustment Letter Output](#unique_51) [page ] 73 | Contract Specialist - Leasing | Manage Real Estate Output Requests (F7482) | Condition of an existing contract can be adjusted. |
| Reports Adjustment |  |  |  |
| [Adjustments on Contracts](#unique_52) [page ] 75 | Contract Specialist - Leasing | Adjustments on Contracts (REAJAHCN) | Condition of an existing contract can be adjusted. |
| [Cond./Adjustment Rule - Information System](#unique_53) [page ] 76 | Contract Specialist - Leasing | Cond./Adjustment Rule - Information System (REISCDCNAJ) | You run a report of existing contracts. |
| Technical Transactions |  |  |  |
| [Analyze Logs](#unique_54) [page ] 77 | Administrator - Leasing | Analyze Logs (RECALA) | Logs are analyzed. |
| [Update Objects in Worklist - Background Job](#unique_55) [page ] 78 | Administrator - Leasing | Update Objects in Worklist - Background job (F5969) | Update objects in worklist is simulated. |
| [Check Contracts - Background Job](#unique_56) [page ] 79 | Administrator - Leasing | Check Contracts - Background job (F5968) | Update objects in worklist is executed. |
| [Cash Flow Update for Contracts](#unique_57) [page ] 80 | Administrator - Leasing | Cash Flow Update for Contract (RECDCGOL) | Cash flow of existing contracts can be updated. |
| [Generate Reminder Dates for Contracts](#unique_58) [page ] 81 | Administrator - Leasing | Generate Dates for Contracts (RECARSGENCN) | General reminder item of the new year is displayed. |
| [Archive Contracts](#unique_59) [page ] 82 | Contract Specialist - Leasing | Manage Contract (RECN) | Existing contract is archived. |

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

Context

In this activity, you can create a new contract as part of your daily business.

Procedure

To execute this activity, go step by step through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object.Make the following entries and choose Continue:Contract Type: ServiceCompany Code: 3310 | Data is validated. Next screen General Data screen is displayed. |  |
| 4 | Insert General Data | Make the following entries (if the contract is relevant for valuation) and choose Partners to go to the next screen:Contract Name: <Your contract name>Contract Currency: AED as defaultedNote The company code currency is defaulted here. It’s allowed to be changed to a different currency. | Datais validated.The Partners screen is displayed. |  |
| 5 | Assign New Partner | Choose Assign New Partner.Choose Supplier (Fin.Accounting).Make the following entries and choose Continue.Business Partner: <Business Partner number> (for example, 33300001) | Data is validated.The Business Partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries:Contract start date: <Your contract start date>1st Contract End: <Your contract end date>Press Enter and choose Continue in the Correct Cash Flow From view. | The data is validated and Cash Flow From date is filled.The Term has been created. |  |
| 7 | Insert Contract Objects | Choose Objects.Choose Assign and select COB Contract Object.Choose OK and link a contract object to the contract.Contract Object: <Your description of the contract object> (for example, COB)Object Type: <Select a contract object type>Account Assignment: <Select a cost center for a account assignment> for example, CTR A000/33101101 | Data is validated.The Object screen is displayed. |  |
| 8 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract.For each condition make the following entries:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note The currency in Contract Currency of General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Postings.Note If a foreign currency is used in Contract Currency under tab General Data or in Currency under tab Conditions, select a currency translation rule in the field below.CrcyTrRule: <Select a rule>Tax Group: <Your default tax group>, for example, Y-FULLNote Default tax group can be set by configuration step Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_6) [page ] 7.Note If Registration for Indirect Taxation Abroad (RITA) is activated in your system, a new field AltTaxCnty is available for selecting a different country. The tax code of the newly selected country will be applied.If RITA is not activated in your system, the field AltTaxCnty is invisible. In this case, you can disregard the field AltTaxCnty below.For more information on activating RITA, please refer to J58 - Accounting and Financial Close - Preliminary Steps - Activate Registration for Indirect Taxation Abroad (Optional).AltTaxCnty: <Select a country> for example, NLChoose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Under Enhancements: <Select a business place> for example, DXBChoose Continue.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract.Choose Simulate to simulate the cash flow.Choose Back to Conditions.Note Make sure the contract type, object type and condition type are matched. For example, if contract type is Lease in Real Estate, condition type should be YCO01 Land/Property or YCO02 Building, condition type should be RE land or RE building related. | Data is validated.Cash flow is simulated |  |
| 9 | Insert Critical Dates and Reminders for Contract | Choose Resubmission.Choose Create Reminder Rule to create a reminder rule for your contract.For each reminder rule, make the following entries:Reminder Rule: <Select a reminder rule>Resubmission Reason: <Select a reason>Date: <Enter a date in the future>Then choose Save and go to the next screen. | The reminder rule is generated.The contract is saved and the number of the new contract is released. |  |
| 10 | Activate Contract | Choose Activate to activate your contract.Choose Yes. | A message to execute the activation is shown. The contract is activated. |  |

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
- related-to :: [[17-leasing-and-real-estate/lease-in-accounting-group-ledger-ifrs-21p-ae-test-script-797]]
- related-to :: [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-in-accounting-group-ledger-us-gaap-34n-ae-914]]
- related-to :: [[17-leasing-and-real-estate/test-script-sap-s-4hana-cloud-public-edition-lease-in-accounting-1t6-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21R_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 126,052 chars in the whole document
