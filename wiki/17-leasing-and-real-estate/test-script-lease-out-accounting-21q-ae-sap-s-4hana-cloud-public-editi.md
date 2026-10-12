---
id: 17-leasing-and-real-estate/test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi
title: "Test Script: Lease-Out Accounting (21Q_AE) - SAP S/4HANA Cloud Public Edition (21Q_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 21Q (UAE) Lease-Out Accounting, release 2608: prerequisites, SSCUI setup, and test steps for contracts, periodic posting, invoicing, adjustment."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/lease-out-sublease-and-sales-based-rent]
aliases: [21Q_S4CLD2608_BPD_EN_AE]
keywords: ["Lease-Out, Sublease and Sales-Based Rent Accounting", lease-out accounting, lease contract management, contract renewal, contract notice, periodic posting, lease invoicing, condition adjustment, account symbols, contract reminders]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21Q_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-798
topic: 17-leasing-and-real-estate/lease-out-sublease-and-sales-based-rent
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lease-Out Accounting (21Q_AE) - SAP S/4HANA Cloud Public Edition (21Q_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21Q_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Lease-Out, Sublease and Sales-Based Rent Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lease-Out Accounting (21Q_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232848521)

[2 Prerequisites 5](#_Toc232848522)

[2.1 System Access 5](#_Toc232848523)

[2.2 Roles 5](#_Toc232848524)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232848525)

[2.4 Preliminary Steps 7](#_Toc232848526)

[2.4.1 Default Value for Tax Rate per Contract Type 7](#_Toc232848527)

[2.4.2 Assign Tax Codes 9](#_Toc232848528)

[2.4.3 Assign Tax Code (for FI Document) 10](#_Toc232848529)

[2.4.4 Enter Index Level 12](#_Toc232848530)

[2.4.5 Maintain Residence Time 14](#_Toc232848531)

[2.4.6 Assign Account Symbol to Flow Type 15](#_Toc232848532)

[2.4.7 Replace Account Symbol 17](#_Toc232848533)

[2.4.8 Define Output Parameter Determination – Invoice 20](#_Toc232848534)

[2.4.9 Define Output Parameter Determination – General Letter 21](#_Toc232848535)

[2.4.10 Define Output Parameter Determination – Adjustment Letter 23](#_Toc232848536)

[2.4.11 Define Permitted Superordinate Architecture Object Types 24](#_Toc232848537)

[3 Overview Table 26](#_Toc232848538)

[4 Test Procedures 31](#_Toc232848539)

[4.1 Contract Management 31](#_Toc232848540)

[4.1.1 Create Contract 31](#_Toc232848541)

[4.1.2 Contract Renewal 35](#_Toc232848542)

[4.1.2.1 Maintain Renewal Rule 35](#_Toc232848543)

[4.1.2.2 Execute Renewal Option (Single Contract) 36](#_Toc232848544)

[4.1.2.3 Reverse Renewal 37](#_Toc232848545)

[4.1.2.4 Execute Renewal Option (Multiple Contract) 38](#_Toc232848546)

[4.1.3 Contract Notice 40](#_Toc232848547)

[4.1.3.1 Maintain Notice Rule 40](#_Toc232848548)

[4.1.3.2 Give Notice (Single Contract) 41](#_Toc232848549)

[4.1.3.3 Reverse Notice 42](#_Toc232848550)

[4.1.3.4 Notice on Contracts 43](#_Toc232848551)

[4.1.4 Reminder for Contracts 45](#_Toc232848552)

[4.1.4.1 Maintain Reminder Rule 45](#_Toc232848553)

[4.1.4.2 Process Reminder 46](#_Toc232848554)

[4.1.5 Print General Correspondence 46](#_Toc232848555)

[4.1.6 Reports Contract Management 47](#_Toc232848556)

[4.1.6.1 Contract and Lease Management Dashboard 47](#_Toc232848557)

[4.1.6.2 Contracts - Information System 48](#_Toc232848558)

[4.1.6.3 Conditions for Contracts - Information System 49](#_Toc232848559)

[4.1.6.4 Business Partners of Contracts - Information System 50](#_Toc232848560)

[4.1.6.5 Objects for Contracts - Information System 51](#_Toc232848561)

[4.1.6.6 Term of Contracts - Information System 51](#_Toc232848562)

[4.1.6.7 Memos of Contract - Information System 52](#_Toc232848563)

[4.1.6.8 Contract Change Documents - Information System 53](#_Toc232848564)

[4.1.6.9 Real Estate Contract Validity Report 54](#_Toc232848565)

[4.1.6.10 Real Estate Contract Object Assignment Report 55](#_Toc232848566)

[4.2 Accounting 56](#_Toc232848567)

[4.2.1 Periodic Posting 56](#_Toc232848568)

[4.2.1.1 Periodic Posting - Simulation 56](#_Toc232848569)

[4.2.1.2 Periodic Posting - Update Run 57](#_Toc232848570)

[4.2.2 Reverse Contract Postings 59](#_Toc232848571)

[4.2.2.1 Reverse Contract Postings - Simulation 59](#_Toc232848572)

[4.2.2.2 Reverse Contract Postings - Update Run 61](#_Toc232848573)

[4.2.3 Invoicing 62](#_Toc232848574)

[4.2.3.1 Schedule Invoice Creation 62](#_Toc232848575)

[4.2.3.1.1 Schedule Invoice Creation - Simulation 62](#_Toc232848576)

[4.2.3.1.2 Schedule Invoice Creation - Update Run 63](#_Toc232848577)

[4.2.3.2 Schedule Invoice Output Requests 65](#_Toc232848578)

[4.2.3.3 Manage Invoice Output 66](#_Toc232848579)

[4.2.3.4 Reverse Invoice 67](#_Toc232848580)

[4.2.4 Reports Accounting 68](#_Toc232848581)

[4.2.4.1 Contract and Lease Cashflow Dashboard 68](#_Toc232848582)

[4.2.4.2 General Real Estate Posting Log 69](#_Toc232848583)

[4.2.4.3 Item Overview - Information System 70](#_Toc232848584)

[4.2.4.4 Contract Cashflow Report 71](#_Toc232848585)

[4.2.4.5 Conditions for Contracts - Information System 72](#_Toc232848586)

[4.2.4.6 Periodic Posting: Previous Period Comparison 73](#_Toc232848587)

[4.3 Adjustment 74](#_Toc232848588)

[4.3.1 Maintain Adjustment Rule 74](#_Toc232848589)

[4.3.2 Create Adjustment 76](#_Toc232848590)

[4.3.3 Modify and Activate Adjustment (Optional) 78](#_Toc232848591)

[4.3.4 Display Adjustment 79](#_Toc232848592)

[4.3.5 Create Adjustment Letter 80](#_Toc232848593)

[4.3.6 Manage Adjustment Letter Output 81](#_Toc232848594)

[4.3.7 Reports Adjustment 82](#_Toc232848595)

[4.3.7.1 Adjustments on Contracts 82](#_Toc232848596)

[4.3.7.2 Cond./Adjustment Rule - Information System 83](#_Toc232848597)

[4.4 Technical Transactions 84](#_Toc232848598)

[4.4.1 Analyze Logs 84](#_Toc232848599)

[4.4.2 Update Objects in Worklist - Background Job 85](#_Toc232848600)

[4.4.3 Check Contracts - Background Job 86](#_Toc232848601)

[4.4.4 Cash Flow Update for Contracts 87](#_Toc232848602)

[4.4.5 Generate Reminder Dates for Contracts 88](#_Toc232848603)

[4.4.6 Schedule Generic Rental Object Checks 89](#_Toc232848604)

[4.5 Archive Contracts 91](#_Toc232848605)

## Purpose

Overview

Lease contracts describe contractual agreements between two partners: the lessor and the lessee. The lessor owns an asset, whereas the lessee has a right to use this asset during the period agreed in the lease contract. The lessee pays lease payments for the use of the asset, as agreed upon in the lease contract.

This scope item helps you standardize and automate your lease-out debit contract management activities for real estate, as well as for machinery, equipment, vehicles, and computer hardware.

You can easily create new contracts and execute periodic postings for existing contracts.

You can change the customer of an existing contract, as well as run a report of existing contracts as part of your daily business.

Leveraging the reporting functions helps you to make better and more informed lease management decisions.

This scope item is applicable for operating lease of Lease Out scenarios.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/21Q_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Accounts Receivable Accountant - Leasing | SAP_BR_RECM_AR_ACCOUNTANT | Accounts Receivable - Leasing | SAP_BR_RECM_AR_ACCOUNTANT |  |
| Administrator - Leasing | SAP_BR_RECM_ADMINISTRATOR | Administration - Leasing | SAP_BR_RECM_ADMINISTRATOR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Administrator - Real Estate Management | SAP_BR_RE_ADMINISTRATOR | Administration - Real Estate | SAP_FIN_SPT_RE_ADMIN_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Customer | 3310000133100002 |  |  |
| Cost Center | any available cost center with company code relation, for example, 33101101 |  |  |
| Profit Center | any available profit center, for example, YB600 |  |  |
| Functional Area | any available functional location, for example, YB40 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNH | Create Profit Center - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| 7AD | Create Rental Object – MDS |

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

#### Assign Account Symbol to Flow Type

Starting with the 2102 release, the account symbol for flow type FA00, FA10, FA20, FK00, FK10, FK20, OA00, OA10, OA20, OK00, OK10, OK20, IA00, IA10 and IA20, IK00, IK10 and IK20 is changed from Y-ASSETCLEARING (with assigned G/L account 16014000 - Technical Clrng Acct Integrated Asset Acquisition) to S-LEASERTMLGADJ (with assigned G/L account 71010300 - Loss from Asset Transactions (ROU)) for new customers. It has impact on RoU asset acquisition/reduction/early termination postings.

Since the 2105 release, the account symbol for flow type I940, I941, I945, I946, F940, F941, F945 and F946 for new customer is changed from S-D_CLEARING (with assigned G/L account 21320000 - Leasing Out Clearing) to S-LEASERTMLGADJ (with assigned G/L account 71010300 - Loss from Asset Transactions (ROU)) for new customers. It has impact on RoU asset retirement/subletting postings.

Since the 2105 release, the account symbols for flow type IL00, IL10, IL20, FL00, FL10 and FL20 are changed for new customer. Please refer to below table for detailed changes. It has impact on service charge postings.

| Old Account Symbols | New Account Symbols |
| --- | --- |
| Y-LEASEEXPBULIN | S-SERTRABUILD |
| Y-LEASEEXPCOLI | S-SERTRACOMP |
| Y-LEASEEXPFFLIN | S-SERTRAFIXF |
| Y-LEASEEXPLALIN | S-SERTRALAND |
| Y-LEASEEXPMALIN | S-SERTRAMACH |
| Y-LEASEEXPOFLIN | S-SERTRAOFFI |
| Y-LEASEEXPVELIN | S-SERTRAVEHI |

Since the 2105 release, the debit account symbol for flow type I800 (assigned in condition type LG90) have been changed as per below table. This change will cause the G/L account change in valuation posting for condition type LG90.

Table 1:

| Account Determination | Old Account Symbols | Old G/L Account | New Account Symbols | New G/L Account |
| --- | --- | --- | --- | --- |
| YROUBU | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECBU | 0064001100 |
| YROUCO | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECCO | 0064007100 |
| YROUFF | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECFF | 0064006100 |
| YROULA | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECLA | 0064000100 |
| YROUMA | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECMA | 0064002100 |
| YROUOF | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECOF | 0064005100 |
| YROUVE | Y-ASSETCLEARING | 0016014100 | S-EXTRADEPRECVE | 0064004100 |

Since the 2608 release, the account determinations for the advance payment (condition type OR50) and flat rate (condition type OR60) conditions have been updated as shown in the tables below. The existing account symbol Y‑SERCHARINCRE has been replaced with the new symbol S‑SERTRINCRE.

Table 2:

| Account Determination | Old Credit Account Symbol | New Credit Account Symbol | Old G/L Account | New G/L Account |
| --- | --- | --- | --- | --- |
| R505 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |
| R506 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |
| R605 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |
| R606 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |

Table 3:

| Account Determination | Old Credit Account Symbol | New Credit Account Symbol | Old G/L Account | New G/L Account |
| --- | --- | --- | --- | --- |
| R507 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |
| R607 | Y-SERCHARINCRE | S-SERTRINCRE | 70800100 | 70800100 |

If you installed the leasing solution before the 2608 release and want to apply the update, make the required change using the relevant SSCUI.

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

#### Define Output Parameter Determination – Invoice

Purpose

In this activity, you define the output parameter determination for the invoice.

Prerequisites

Relevant output parameters have been configured in background system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen displays. |  |
| 3 | Show Rules | In the Show Rules for field, choose RE Contract Invoice on the drop down list. |  |  |
| 4 | Determination Step | Use the Edit button to update Table Contents fields.In the Determination Step field, use the drop-down menu to choose Output Type, maintain and activate the following column entries in the Table Contents.Output type: RE_CONTRACT_A520 (RE Contract Invoice)Dispatch Time: 1 (Immediately)Choose Receiver in the Determination Step field, and maintain the following column entries in theTable Contents:Role: VWExclusive Indicator: - (false)Choose Channel in the Determination Step field, and maintain the following column entries in the Table ContentsChannel: PRINT (Print)Exclusive Indicator: - (false)Choose Print Settings in the Determination Step field, and maintain the following column entries in the Table Contents:Print Queue: DEFAULTNumber of Copies: 1Choose Email Settings in the Determination Step field, and maintain the following column entries in the Table Contents:Output type: RE_CONTRACT_A520 (RE Contract Invoice)Email Template: RE_CN_INVOICE_EMAILChoose Form template in the Determination Step field, and maintain the following column entries in the Table Contents:The first entry:Output type: RE_CONTRACT_A520 (RE Contract Invoice)Channel: PRINT (Print)Sender Ctry/Reg.: AECompany Code: 3310Form Template: RE_CN_INVOICE_DEThe second entry:Output type: RE_CONTRACT_A520Channel: EMAIL(Email)Sender Ctry/Reg.: AECompany Code: 3310Form Template: RE_CN_INVOICE_DEChoose Output Relevance in the Determination Step field, and maintain the following entries in Table Contents:Maintain the following entries in Table Contents.Relevance Indicator: X (true) |  |  |

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

#### Define Permitted Superordinate Architecture Object Types

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Manage Your Solution | Open Manage Your Solution. | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Define Permitted Superordinate Architecture Object Types | Set Application Area to Finance.Set Sub Application Area to Contract and Lease Management.Choose Architecture Objects.Choose Configure in Define Permitted Superordinate Architecture Object Types row.Choose the New Entry button according to your needs. For example, select S2BU for Architecture Object Type, S1SI for Architecture Parent Object Type.Choose Save. | The new entry is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Permitted Superordinate Architecture Object Types | Go to the Business Processes Configuration app and search for the following activity: Define Permitted Superordinate Architecture Object Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Permitted Superordinate Architecture Object Types | Choose the New Entry button according to your needs. For example, select S2BU for Architecture Object Type, S1SI for Architecture Parent Object Type.Choose Save. | The new entry is saved. |  |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Contract Management |  |  |  |
| [Create Contract](#unique_18) [page ] 31 | Contract Specialist - Leasing | ; Manage Contract (RECN) | The contract is created. The system message confirms creation and displays the new contract number. |
| Contract Renewal |  |  |  |
| [Maintain Renewal Rule](#unique_19) [page ] 35 | Contract Specialist - Leasing | Contract Management (F5273); Manage Contract (RECN) | Contract can be renewed. |
| [Execute Renewal Option (Single Contract)](#unique_20) [page ] 36 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Existing contract can be renewed. |
| [Reverse Renewal](#unique_21) [page ] 37 | Contract Specialist - Leasing | Manage Contract Term (F6580); Manage Contract (RECN) | The performed renewal can be reversed. |
| [Execute Renewal Option (Multiple Contract)](#unique_22) [page ] 38 | Contract Specialist - Leasing | Renewal of Contracts - Information System (REISCNRN) | Several contracts can be renewed at the same time. |
| Contract Notice |  |  |  |
| [Maintain Notice Rule](#unique_23) [page ] 40 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Notice rule can be maintained. |
| [Give Notice (Single Contract)](#unique_24) [page ] 41 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | You can give notice to a contract. |
| [Reverse Notice](#unique_25) [page ] 42 | Contract Specialist - Leasing | Manage Contract Term (F6580), Manage Contract (RECN) | Notice can be reversed. |
| [Notice on Contracts](#unique_26) [page ] 43 | Contract Specialist - Leasing | Notice on Contracts - Information System (REISCNNT) | You can give notification to your contract. |
| Reminder for Contracts |  |  |  |
| [Maintain Reminder Rule](#unique_27) [page ] 45 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder rule is maintained. |
| [Process Reminder](#unique_28) [page ] 46 | Contract Specialist - Leasing | Contract Management (F5273), Manage Contract (RECN) | Reminder is processed. |
| [Print General Correspondence](#unique_29) [page ] 46 | Contract Specialist - Leasing | Print: General Correspondence (RECPA400) | General correspondence for existing contracts can be printed. |
| Reports Contract Management |  |  |  |
| [Contract and Lease Management Dashboard](#unique_30) [page ] 47 | Contract Specialist - Leasing | Contract and Lease Management Dashboard (F4555) | You run a report of existing contracts. |
| [Contracts - Information System](#unique_31) [page ] 48 | Contract Specialist - Leasing | Contracts - Information System (REISCN) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_32) [page ] 49 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Business Partners of Contracts - Information System](#unique_33) [page ] 50 | Contract Specialist - Leasing | Business Partners of Contracts - Information System (REISCNBP) | You run a report of existing contracts. |
| [Objects for Contracts - Information System](#unique_34) [page ] 51 | Contract Specialist - Leasing | Objects for Contracts - Information System (REISCNOA) | You run a report of existing contracts. |
| [Term of Contracts - Information System](#unique_35) [page ] 51 | Contract Specialist - Leasing | Term of Contracts - Information System (REISCNPE) | You run a report of existing contracts. |
| [Memos of Contract - Information System](#unique_36) [page ] 52 | Contract Specialist - Leasing | Memos of Contract - Information System (REISCNMEMO) | You run a report of existing contracts. |
| [Contract Change Documents - Information System](#unique_37) [page ] 53 | Contract Specialist - Leasing | Contract Change Documents - Information System (REISCHGDOCCN) | You run a report of existing contracts. |
| [Real Estate Contract Validity Report](#unique_38) [page ] 54 | Contract Specialist - Leasing | Real Estate Contract Validity Report (W0200) | You run a report of existing contracts. |
| [Real Estate Contract Object Assignment Report](#unique_39) [page ] 55 | Contract Specialist - Leasing | Real Estate Contract Object Assignment Report (W0201) | You run a report of existing contracts. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Accounting |  |  |  |
| Periodic Posting |  |  |  |
| [Periodic Posting - Simulation](#unique_40) [page ] 56 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is simulated. |
| [Periodic Posting - Update Run](#unique_41) [page ] 57 | Accounts Payable Accountant - Leasing | Periodic Posting - Background job (F4607) | Period posting is executed. |
| Reverse Contract Postings |  |  |  |
| [Reverse Contract Postings - Simulation](#unique_42) [page ] 59 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is simulated. |
| [Reverse Contract Postings - Update Run](#unique_43) [page ] 61 | Accounts Payable Accountant - Leasing | Reverse Contract Postings - Background Job (F6275) | Reversal of contract posting is executed. |
| Invoicing |  |  |  |
| Create Invoice |  |  |  |
| [Schedule Invoice Creation - Simulation](#unique_44) [page ] 62 | Accounts Receivable Accountant - Leasing | Schedule Invoice Creation - Background Job (F7931) | Invoice creation is simulated. |
| [Schedule Invoice Creation - Update Run](#unique_45) [page ] 63 | Accounts Receivable Accountant - Leasing | Schedule Invoice Creation - Background Job (F7931) | Invoice creation is executed. |
| [Schedule Invoice Output Requests](#unique_46) [page ] 65 | Accounts Receivable Accountant - Leasing | Schedule Invoice Output Requests - Background Job (F7932) | Invoice is printed. |
| [Manage Invoice Output](#unique_47) [page ] 66 | Accounts Receivable Accountant - Leasing | Manage Real Estate Output Requests (F7482) | You can manage the output of your invoice. |
| [Reverse Invoice](#unique_48) [page ] 67 | Accounts Receivable Accountant - Leasing | Reverse Invoices (RERAIVRV) | Created invoice is reversed. |
| Reports Accounting |  |  |  |
| [Contract and Lease Cashflow Dashboard](#unique_49) [page ] 68 | Accounts Payable Accountant - Leasing | Contract and Lease Cashflow Dashboard (F5379) | You run a report of existing contracts. |
| [General Real Estate Posting Log](#unique_50) [page ] 69 | Contract Valuation Specialist - Leasing or Accounts Payable Accountant - Leasing | General Real Estate Posting Log (RERAPL) | You review the general posting for contracts. |
| [Item Overview - Information System](#unique_51) [page ] 70 | Accounts Payable Accountant - Leasing | Item Overview - Information System (REISRADOCITEM) | You run a report of existing contracts. |
| [Contract Cashflow Report](#unique_52) [page ] 71 | Accounts Payable Accountant - Leasing | Contract Cashflow Report (F5363) | You run a report of existing contracts. |
| [Conditions for Contracts - Information System](#unique_53) [page ] 72 | Contract Specialist - Leasing | Conditions for Contracts - Information System (REISCDCN) | You run a report of existing contracts. |
| [Periodic Posting: Previous Period Comparison](#unique_54) [page ] 73 | Accounts Payable Accountant - Leasing | Periodic Posting: Previous Period Comparison (RERAPPCMP) | You run a report of existing contracts. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Adjustment |  |  |  |
| [Maintain Adjustment Rule](#unique_55) [page ] 74 | Contract Specialist - Leasing | Manage Contract (RECN) | Condition of an existing contract can be adjusted. |
| [Create Adjustment](#unique_56) [page ] 76 | Contract Specialist - Leasing | Specify Adjustments (REAJPR) | Condition of an existing contract can be adjusted. |
| [Modify and Activate Adjustment (Optional)](#unique_57) [page ] 78 | Contract Specialist - Leasing | Continue Adjustment (REAJCH) | Adjustment of contracts can be modified. |
| [Display Adjustment](#unique_58) [page ] 79 | Contract Specialist - Leasing | Display Adjustments (REAJSH) | Adjustment of contracts can be displayed. |
| [Create Adjustment Letter](#unique_59) [page ] 80 | Contract Specialist - Leasing | Create Adjustment Letter (F7435) | Adjustment letter can be created. |
| [Manage Adjustment Letter Output](#unique_60) [page ] 81 | Contract Specialist - Leasing | Manage Real Estate Output Requests (F7482) | Condition of an existing contract can be adjusted. |
| Reports Adjustment |  |  |  |
| [Adjustments on Contracts](#unique_61) [page ] 82 | Contract Specialist - Leasing | Adjustments on Contracts (REAJAHCN) | Condition of an existing contract can be adjusted. |
| [Cond./Adjustment Rule - Information System](#unique_62) [page ] 83 | Contract Specialist - Leasing | Cond./Adjustment Rule - Information System (REISCDCNAJ) | You run a report of existing contracts. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Technical Transactions |  |  |  |
| [Analyze Logs](#unique_63) [page ] 84 | Administrator - Leasing | Analyze Logs (RECALA) | Logs are analyzed. |
| [Update Objects in Worklist - Background Job](#unique_64) [page ] 85 | Administrator - Leasing | Update Objects in Worklist - Background job (F5969) | Update objects in worklist is simulated. |
| [Check Contracts - Background Job](#unique_65) [page ] 86 | Administrator - Leasing | Check Contracts - Background job (F5968) | Update objects in worklist is executed. |
| [Cash Flow Update for Contracts](#unique_66) [page ] 87 | Administrator - Leasing | Cash Flow Update for Contract (RECDCGOL) | Cash flow of existing contracts can be updated. |
| [Generate Reminder Dates for Contracts](#unique_67) [page ] 88 | Administrator - Leasing | Generate Dates for Contracts (RECARSGENCN) | General reminder item of the new year is displayed. |
| [Schedule Generic Rental Object Checks](#unique_68) [page ] 89 | Administrator - Real Estate Management or Administrator - Leasing | Schedule Generic Rental Object Check - Background Job (F7963) | Generic rental object can be checked. |

| Process Diagram | Business Roles | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Archive Contracts](#unique_69) [page ] 91 | Contract Specialist - Leasing | Manage Contract (RECN) | Existing contract is archived. |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing． | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Create Contract | Choose Create Object.Make the following entries and choose Continue.Contract Type: <Lease out contract type>Note Choose the contract type dependent of the underlining Asset:Lease Out Real Estate (for Land and building)Lease Out Others (for Cars, Machine, IT, Equipment, etc)Company Code: 3310 | Data is validated, next screen General Data screen displays. |  |
| 4 | Insert General Data | Make the following entries and choose Partners.Contract Name: <Your contract name>Contract Currency: AED (As defaulted)Note The company code currency is defaulted here. It’s allowed to be changed to a different currency.Valuation Relevance: No Leasing Valuation | Data is validated.The Partners screen displays. |  |
| 5 | Assign New Partner | Choose Assign New Partner (the + sign in the Display All Periods section)..Use the dropdown to select Customer (Fin.Accounting).Make the following entries and choose Continue.Business Partner: 33100001 | Data is validated. |  |
| 6 | Insert Term | Choose Term.Make the following entries:Contract start date: <Your contract start date>1st Contract End: <Your contract end date>Press Enter and choose Continue in the Correct Cash Flow From dialog box. | The data is validated and Cash Flow From date is filled.The Term has been created. |  |
| 7 | Insert Contract Objects | Choose Objects.Choose Assign and select COB Contract Object.Choose OK and link a contract object to the contract.Contract Object: <Your description of the contract object> For example, COBObject Type: <Select a contract object type>Note Choose Object Type in accordance with the Contract Type you selected.For Lease Out Real Estate contract type, use the following objects:Land/PropertyBuildingLocation/SiteFloorRoomFor Lease Out Other contract type, use the following objects:DP/HardwareFixtures FittingsMachineryVehiclesBuilding EquipmentOffice EquipmentAccount assignment: <Select a cost center for a account assignment> for example, CTR A000/33101101Choose Save. | Data is validated.The Object screen displays. |  |
| 8 | Insert Contract Conditions | Choose Conditions.Choose Insert Condition(s) in the Condition Type(2) dialog box and choose OK to select the Condition Type of your contract.For each condition, make the following entries:Condition Purpose: StatisticalUnit Price: <Your unit price of the condition>Currency: <your contract currency>Note The currency in Contract Currency of tab General Data is defaulted here. It is allowed to be changed to a different currency.Under Terms, choose Display or Change Term for Posting.Note If a foreign currency is used in Contract Currency in tab General Data or in Currency of tab Condition, select a currency translation rule in below field.CrcyTrRule: <Select a rule>Tax Group: <your default tax group>, for example, Y-FULLNote Default tax group can be set by configuration step Default Value for Tax Rate per Contract Type as described in chapter [Default Value for Tax Rate per Contract Type](#unique_6) [page ] 7.Choose Continue.Under Terms, choose Display or Change Term for Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area> for example, YB40Note The Profit Center and Functional Area entered here should be matched with the values in cost center master data, which is entered in Account Assignment of tab Objects in the contract.Under Enhancements: <Select a business place> for example, DXBChoose Continue.Choose Memo. Input your memo.Note In order to display memo in report Memos of Contract - Information System, memo should be entered here or in tab Term, Objects, Conditions or Valuation Parameters in contract. | Data is validated.Cash flow can be simulatedThe Resubmission screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Perform Renewal | Note Before you make any change, please make sure the contract is already activated.Note Automatic renewal does not require either approval or activation. Only Option renewal requires.Choose Term.In the Overview section of tab Term, make sure the Renewal term category entry is selected.Choose Renew Contract.Choose Approve and Activate. | The contract is renewed. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
| 3 | Real Estate Contract | Make the following entries and choose Change Object:Company Code: 3310Contract: <Your contract> | Data is validated, and next screen General Data screen is displayed. |  |
| 4 | Reverse Renewal | Note Before you make any change, please make sure the contract is already activated and has active renewals.Choose Term.Select the entry with Renewal cateogory by double-clicking it. Then choose Renew Contract on the Renewal tab.Choose Reverse Renewal on the next screen.Approved/Rejected: <blank>Decided On: <blank> | The performed renewal is reversed. |  |
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
| 2 | Access the SAP Fiori App | Open Renewal of Contracts - Information System (REISCNRN). |  |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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
| 2 | Access the SAP Fiori App | Open Notice on Contracts - Information System (REISCNNT). | The Information System: Giving Notice on Contracts screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract (RECN). | The Contract screen displays. |  |
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
| 2 | Access the SAP Fiori App | Open Print: General Correspondence (RECPA400). | The Print general correspondence screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Contract and Lease Management Dashboard (F4555). | The Contract and Lease Management Dashboard screen displays. |  |
| 3 | Report Contract | Check the information displayed on the dashboard. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Contracts - Information System (REISCN). | The Info System: Contracts screen displays. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Use Grid Control: Selected |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Conditions for Contracts - Information System (REISCDCN). | The Info System: Conditions for Contracts view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Use Grid Control: Selected |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Business Partners of Contracts - Information System (REISCNBP) . | The Information System: Business Partners of Contracts view is displayed. |  |
| 3 | Report Contract | Make the following entries and press Run:Company Code: 3310Contract: <Your contract(s)>Use Grid Control: <Select> |  |  |

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
| 2 | Access the SAP Fiori App | Open Objects for Contracts - Information System (REISCNOA). | The Information System: Objects for Contracts screen displays. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Term of Contracts - Information System (REISCNPE). | The Information System: Term of Contracts view is displayed. |  |
| 3 | Report Contract | Make the following entries and press Run:Company Code: 3310Contract: <Your contracts>Use grid control: Selected |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Memos of Contract - Information System (REISCNMEMO) . | The Information System: Contracts Memos view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>Use grid control: Selected |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Contract Change Documents - Information System (REISCHGDOCCN). | The Info System: Change Documents for Contractsview is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Run:Company Code: 3310Contract: <Your contracts>In the Type of Data Change section:Change: SelectedUse Grid Control: Selected | Change log is displayed for the contracts. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Real Estate Contract Validity Report (W0200). | The Valid Contract Report view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Go:Validity Start: <Start date>Validity End: <End date> | The system displays company code and contract numbers with validity during the chosen period. |  |
| 4 | Report Contract | From the left pane, select the available fields and choose Add to Row axis or Add to Columns axis. For example, select the Real Estate Contract field and choose Add field Real Estate Contract to Row axis. | Field contract number is added to the report. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Real Estate Contract Object Assignment Report (W0201). | The RE Contract Subject Assignment view is displayed. |  |
| 3 | Report Contract | Make the following entries and choose Go:Validity Start: <Start date>Validity End: <End date> |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting - Background job (F4607). | The Application Jobs view is displayed. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job. |  |  |
| 4 | Periodic Posting: Contracts Selection | Make the following entries and choose Step 2:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting run |  |  |
| 5 | Periodic Posting: Contracts Selection | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Periodic Posting: Contracts Selection | Make the following entries and choose Schedule:Company Code: 3310Input entry for either Contract Type or Contract:Contract Type: <your contract type>Contract: <Lease Out contract number>In the Period selection area:Month for Posting Run: <The month for posting run>Year for Posting Run: <The posting year>Due date: <before or on the last day of the posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <The posting period>Posting Run Mode: SimulationType of Posting Run: Integrated Posting | Data is validated. The Application Jobs screen displays. |  |
| 7 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result display. |  |
| 8 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |
| 9 | Periodic Posting: Contract | Choose Back. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting - Background job (F4607). | The Application Jobs view is displayed. |  |
| 3 | Periodic Posting: Contracts Selection | Choose Create to add new job. |  |  |
| 4 | Periodic Posting: Contracts Selection | Make the following entries and choose Step 2:Job Template: Leasing contract: Periodic posting runJob Name: Leasing contract: Periodic posting run |  |  |
| 5 | Periodic Posting: Contracts Selection | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Periodic Posting: Contracts Selection | Make the following entries and choose Schedule:Company Code: 3310Input entry for either Contract Type or Contract:Contract Type: <your contract type>Contract: <Lease Out contract number>In the Period selection area:Month for Posting Run: <The month for posting run>Year for Posting Run: <The posting year>Due date: <before or on the last day of the posting month>Note Choose the search help, then select before or on from the Include dropdown list. Then choose OK.In the Posting parameter area:Document Header Text: <Your document header text> for example, Per.Posting: MMM YY. MMM represents month, YY represents yearPosting Date: <First day of the posting month>Document Date: <First day of the posting month>Posting Period: <The posting period>Posting Run Mode: Update RunType of Posting Run: Integrated Posting | Data is validated. The Application Jobs screen displays. |  |
| 7 | Periodic Posting Contract | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log and job result are attached. |  |
| 8 | Periodic Posting Contract: Documents | Check the run details and choose Back to go back. | Postings are correct.The Application Jobs screen displays. |  |
| 9 | Periodic Posting: Contract | Choose Back. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job. |  |  |
| 4 | Reverse Postings | Make the following entries and choose Step 2:Job Template: Reverse Contract PostingsJob Name: Reverse Contract Postings |  |  |
| 5 | Reverse Postings | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Reverse Postings | Make the following entries and choose Schedule:In the Document selection area:Company Code: 3310Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: SimulationReason for reversal: <Your reason> for example, Wrong Period | Data is shown.Default mode is Simulation. You can change it to Update Run for execution. |  |
| 7 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log is generated. |  |
| 8 | Reverse Postings | Check the run details and choose Back. | Postings are correct.The Application Jobs view is displayed. |  |

##### Reverse Contract Postings - Update Run

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reverse Contract Postings - Background Job (F6275). | The Reverse Contract Postings screen displays. |  |
| 3 | Reverse Postings | Choose Create to add new job. |  |  |
| 4 | Reverse Postings | Make the following entries and choose Step 2:Job Template: Reverse Contract PostingsJob Name: Reverse Contract Postings |  |  |
| 5 | Reverse Postings | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Reverse Postings | Make the following entries and choose Schedule:In the Document selection area:Company Code: 3310Contract: <Your contract number>Type of Posting Run: Integrated PostingIn the Posting parameter area:Mode: Update RunReason for reversal: <Your reason> for example, Wrong Period | Data is shown.Default mode is Simulation. You can change it to Update Run for execution. |  |
| 7 | Reverse Postings | Refresh Go until the job is finished.Choose Navigate to the job details and go to the next screen. | The Job log is generated. |  |
| 8 | Reverse Postings | Check the run details and choose Back. | Postings are correct.The Application Jobs view is displayed. |  |

#### Invoicing

##### Schedule Invoice Creation

###### Schedule Invoice Creation - Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity you simulate an invoice for existing and already posted contracts as part of your daily business. Please note that successful periodic posting is a prerequisite for step Create Invoice.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Invoice Creation - Background Job(F7931). | The Application Jobs screen displays. |  |
| 3 | Create Invoice | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing Contract: Create InvoicesJob Name: Leasing Contract: Create InvoicesChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: 3310Input entry for either Contract Type or Contract.Contract Type: <Your contract type>Contract: <Lease Out contract number>In the Selection of Invoice Items area:Start Due Period: <Your preferred start date>End Due Period: <Your preferred end date>In the Invoice Creation area:Execution Mode: <Simulation>Note Please select Cleared Items Also if the periodic posting has been cleared. | Invoice created. |  |
| 4 | Create Invoice | Choose Navigate to the job details to preview or download the invoice overview list. | The Invoice overview screen displays or is downloaded. |  |
| 5 | Create Invoice | Choose Back to go back. |  |  |

###### Schedule Invoice Creation - Update Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity you create an invoice for existing and already posted contracts as part of your daily business. Please note that successful periodic posting is a prerequisite for step Create Invoice.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Invoice Creation - Background Job(F7931). | The Application Jobs screen displays. |  |
| 3 | Create Invoice | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing Contract: Create InvoicesJob Name: Leasing Contract: Create InvoicesChoose Step 2.Start Immediately: SelectChoose Step 3.Company Code: 3310Input entry for either Contract Type or Contract.Contract Type: <Your contract type>Contract: <Lease Out contract number>In the Selection of Invoice Items area:Start Due Period: <Your preferred start date>End Due Period: <Your preferred end date>In the Invoice Creation area:Execution Mode: <Update Run>Note Please select Cleared Items Also if the periodic posting has been cleared. | Invoice created. |  |
| 4 | Create Invoice | Choose Navigate to the job details to preview or download the invoice overview list. | The Invoice overview screen displays or is downloaded. The Invoicing Run ID can be found there. |  |
| 5 | Create Invoice | Choose Back to go back. |  |  |

##### Schedule Invoice Output Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you print an invoice for existing and already posted contracts as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Invoice Output Requests - Background Job (F7932). | The Application Jobs screen displays. |  |
| 3 | Print Invoice | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Leasing Contract: Invoice OutputJob Name: Leasing Contract: Invoice OutputChoose Step 2.Start Immediately: SelectChoose Step 3.Select invoice by Invoice run ID or business partner or company code.Invoicing Run ID: <Select your invoicing run ID>OrBusiness Partner: <Select your business partner>OrCompany Code: 3310 | Invoices are printed. |  |

##### Manage Invoice Output

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you manage the output for an invoice for existing and already posted contracts as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Real Estate Output Requests (F7482). | The Manage Real Estate Output Requests screen displays. |  |
| 3 | Choose the Invoice | Make the following entries and choose Go:Company Code: 3310Contract: <Your contract> orProcess ID: < Your process ID> orAppl. Object Type: <Your Appl. Object Type> for example, RE Contract Invoice | Data is shown. |  |
| 4 | Display the Invoice Output | Choose the line which invoice you’d like to check.Check Contract, Process, Invoice respectively for information.Under Output Item, choose an item to check General Information, Sender, Channel Settings, Form Template and Log respectively for invoice output information.Adjust the column width to get column Display and Form Template displayedClick Open File to display the PDF document.Close the PDF document. | Information about invoice output request is displayed. |  |

##### Reverse Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you reverse an invoice for existing and already posted contracts as part of your daily business.

Procedure

To execute this activity, go step by step go through the table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Invoices (RERAIVRV). | The Reverse Invoice screen displays. |  |
| 3 | Select Invoice | Selection by Invoicing RunInvoicing Run ID: <Select your invoicing run>orSelection using InvoicesCompany Code: <Select your company code>Invoice Number: <Select your invoice>Fiscal Year: <Select fisc. year for your invoice>orSelection by ContractsCompany Code: <Select your company code>Contract: <Select your contract>orSelection by RecipientBusiness Partner: <Select your business partner>Choose Run. | Data is shown. |  |
| 4 | Invoice Overview | Select an entry and choose Reverse Invoices and agree. | Reversed mark is set. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Contract and Lease Cashflow Dashboard (F5379). | Data is shown. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing or Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open General Real Estate Posting Log (RERAPL). | The Posting Log view is displayed. |  |
| 3 | General Real Estate Posting Log | Make the following entries as RE Document for Selection is checked by default:Process: <Your process to display the report>, for example, REPP Periodic Posting: Contracts or REEP Valuations for ContractsOrCheck FI Document for Selection, and make the following entries:Company Code: 3310User Name: <Your user name>Choose Run. | If you get a runtime error No more memory available to add rows to an internal table, add more selection criteria to narrow your search. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Item Overview - Information System (REISRADOCITEM) . | The Item Overview view is displayed. |  |
| 3 | Item Overview | Make the following entries and choose Run:Company Code: 3310Contract: <Your contract(s)>Open Items On: <Periodic Posting Date>Use Grid Control: <Select> |  |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Contract Cashflow Report (F5363). | The Real Estate Contract Cashflow Report view is displayed. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Conditions for Contracts - Information System (REISCDCN). | The Info System: Conditions for Contracts view is displayed. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Receivable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Periodic Posting: Previous Period Comparison (RERAPPCMP). |  |  |
| 3 | Compare Periodic Postings | Make the following entries:Company Code: 3310Contract: <Your contract>In the Comparison Mode section, choose between Comparison Only and Compar. and Posting.Option 1:If Comparison Only is chosen, make the following entries and choose Execute:Calculation Period 1: <the first day of the selected month>To: <the last day of the selected month>Calculation Period 2: <the first day of the selected month>To: <the last day of the selected month>Note Data is only displayed when the periodic posting is executed.Option 2:If Compar. and Posting is chosen, make the following entries and choose Execute:Calculation Period Comparison: <the first day of the selected month>To: <the last day of the selected month>Month for Posting Run: <the comparison month for posting run>Year of Posting Run: <the year for posting run>Posting Run Mode: SimulationType of Posting Run: Integrated postingIn the Output section, choose between Display All Records and Display Difference Only.Note If Display Difference Only is chosen, data is only displayed when a difference exists between the month for comparison and the month to execute periodic posting.Check the data and choose Back.Posting Run Mode: Update RunChoose Run. | Differences are shown, or the posting result is displayed. |  |
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
| 4 | Assign Adjustment Rule | Choose Adjustment. There are two options to assign the adjustment rule.Option 1:Choose Create Term and select the adjustment rule Free - Modifiable for your contract.Choose the Conditions tab next to Free - Modifiable.Choose Assign Free Condition(s) to assign one of the conditions of the contract.Option 2:Choose the Create Term icon and select the adjustment rule Index - Modifiable United Arab Emirates for your contract.Choose the Unlink from Customizing icon and maintain your data.Base Year: <Your base year>Min. Change Pts: <Your point> orMin. Percent: <Your percent>Note Either input values for one of those fields or ignore the warning message Adjustment XX: the minimum change fields are not filled.If point is maintained in Min. Change Pts, please make sure the point maintained here is less than the difference between the points of the index series for the current date and the index level for the date the last time the condition was adjusted (Both points are maintained by SSCUI Enter Index Level in the Preliminary Steps section).If point is maintained in Min. Percent, please make sure the percent maintained here is less than the percentage difference between the points of the index series for the current date and the index level for the date the last time the condition was adjusted (Both points are maintained by SSCUI Enter Index Level in the Preliminary Steps section). The percentage difference is calculated on the basis of this absolute difference, using the following formula: difference * 100 / (index level at last adjustment).Index Start: <The first date of index level>First adjust. from: <Today>Remaining in Adjustment, choose Conditions.Choose Assign Free Condition(s) to assign one of the conditions of the contract.Choose Save. | Adjustment rule is assigned. |  |

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
| 3 | Process Contract | In the Specify Adjustments view, make the following entries and choose Change Object.Company Code: 3310Contract: <Your contracts>Note You can execute adjustment against more than one contract.On the Procedure tab,If free adjustment rule is maintained in the contract, select Custom and make the following entries:Reason: < Standard>Rule: <FREECN>If index adjustment rule is maintained in the contract, select Index and make the following entries:Reason: < Standard>For free adjustment, choose Processing Paramet.Choose the Insert Row icon on the Custom tab, and make the following entries:%Increase: <Your increase percentage for free adjustment>, for example: 10.Choose Activity Parameters, and make the following entries on the Determine Adjustments tab.Next Possible Valid-From: <Select>Status of Contract: <Active Contracts>OccupancyContracts: <Select>Subject to Approval: <Both>Non-Occupancy Contracts: <Select>Subject to Approval: <Both>Choose Run. | Data is validated and the Specify Adjustments view is displayed. |  |
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
| 2 | Access the SAP Fiori App | Open Cond./Adjustment Rule - Information System (REISCDCNAJ) . | The Info System: Conditions for Adjust-ment Rule for Contract screen displays. |  |
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

In this activity, you can analyze logs as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Analyze Logs (RECALA). | The Analyze Logs view is displayed. |  |
| 3 | Analyze Logs Selection | Make the following entries and choose Execute:User: <Own user ID> | Data is validated. The Log Display view is displayed. |  |
| 4 | Analyze Logs | Analyze the data. | Data is shown. |  |
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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Leasing. |  |  |
| 2 | Access the SAP Fiori App | Open Update Objects in Worklist - Background job (F5969) . | The Application Jobs view is displayed. |  |
| 3 | Update Objects in Worklist Seletion | Choose Create to add new job.Make the following entries and choose Schedule:Job Template: Update Objects in WorklistJob Name: Update Objects in WorklistChoose Step 2.Start Immediately: <Select>Choose Step 3.Person responsible: <Own user ID>Update Immediately: <Select> | Data is validated, and next screen Application Jobs view is displayed. |  |
| 4 | Update Objects in Worklist | Choose Navigate to the job details and go to the next screen. | The Job Details view is displayed. |  |
| 5 | Update Objects in Worklist: Job Detail | Check the run details and choose Back. | The Application Jobs view is displayed. |  |
| 6 | Update Objects in Worklist | Choose Back. |  |  |

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
| 2 | Access the SAP Fiori App | Open Check Contracts - Background job (F5968) . | The Application Jobs screen displays. |  |
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
| 4 | Real Estate Contract | Go to: Contract > Activation and Term > DeactivateConfirm the message. | Message diplays: Status was changed. |  |
| 5 | Real Estate Contract | Go to: Edit > Change Status > Archive > Set Deletion Flag .Note The end-of-term date must be earlier than the system date; otherwise, you get the error: Object validity not yet elapsed; deletion flag is not allowed. | Message diplays: Status was changed. |  |
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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table assigns Periodic Posting and Reverse Contract Postings to 'Accounts Payable Accountant - Leasing', but the test procedures log on as 'Accounts Receivable Accountant - Leasing' (the roles table lists only the AR role).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[17-leasing-and-real-estate/intercompany-process-for-sublease-accounting-2o9-test-script-sap-s-4ha]]
- related-to :: [[17-leasing-and-real-estate/lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-2sb-ae-859]]
- related-to :: [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/21Q_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 140,544 chars in the whole document
