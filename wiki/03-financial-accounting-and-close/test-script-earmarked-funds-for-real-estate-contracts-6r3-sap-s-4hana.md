---
id: 03-financial-accounting-and-close/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana
title: "[DEPRECATED] Test Script: Earmarked Funds for Real Estate Contracts (6R3) - SAP S/4HANA Cloud Public Edition (6R3_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 6R3: configure and test earmarked funds auto-generated from lease-in contracts (create, approve, post, report) in S/4HANA Cloud."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/earmarked-funds]
aliases: [6R3_S4CLD2608_BPD_EN_XX]
keywords: [Earmarked Funds, lease-in contracts, contract and lease management, earmarked funds workflow, earmarked funds approval, document types, contract types, periodic posting, cash flow update, contract valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6R3_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: deprecated
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1187
topic: 03-financial-accounting-and-close/earmarked-funds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Earmarked Funds for Real Estate Contracts (6R3) - SAP S/4HANA Cloud Public Edition (6R3_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6R3_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Earmarked Funds** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Earmarked Funds for Real Estate Contracts (6R3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232826693)

[2 Prerequisites 4](#_Toc232826694)

[2.1 System Access 4](#_Toc232826695)

[2.2 Roles 4](#_Toc232826696)

[2.3 Maintain Business Roles 5](#_Toc232826697)

[2.4 Maintain Business Users 6](#_Toc232826698)

[2.5 Master Data, Organizational Data, and Other Data 7](#_Toc232826699)

[2.6 Business Conditions 8](#_Toc232826700)

[2.7 Preliminary Steps 8](#_Toc232826701)

[2.7.1 Define Document Types for Earmarked Funds 8](#_Toc232826702)

[2.7.2 Define Contract Types 10](#_Toc232826703)

[2.7.3 Permitted Contract Object Types for Each Contract Type 11](#_Toc232826704)

[2.7.4 Make Settings for Roles per Object Type 13](#_Toc232826705)

[2.7.5 Activate Earmarked Funds for Company Code 15](#_Toc232826706)

[2.7.6 Activate Earmarked Funds for CLM Contract Types 16](#_Toc232826707)

[2.7.7 Define Flow Types for Earmarked Funds Generation 18](#_Toc232826708)

[3 Overview Table 20](#_Toc232826709)

[4 Test Procedures 21](#_Toc232826710)

[4.1 Manage Workflows for Earmarked Funds 21](#_Toc232826711)

[4.2 Create Contract 22](#_Toc232826712)

[4.3 Approve Earmarked Funds 26](#_Toc232826713)

[4.4 Activate Contract 27](#_Toc232826714)

[4.5 Perform Periodic Posting 28](#_Toc232826715)

[4.6 Manage Earmarked Funds 29](#_Toc232826716)

[4.7 Cash Flow Update for Contract (Optional) 30](#_Toc232826717)

## Purpose

Overview

Lease contracts describe contractual agreements between two partners: the lessor and the lessee. The lessor is the owner of an asset, whereas the lessee has a right to use this asset during the period agreed in the lease contract. For the use of the asset, the lessee must pay lease payments, which are agreed in the lease contract.

When a public sector organization enters into a lease-in contract, they may need to commit budget for such an obligation. Earmarked funds are used to create such a commitment for a lease-in contract. This scope item automates your lease-in obligation process for contract management by automatically creating earmarked funds for a lease-in contract at the time of contract creation and reducing the obligation with an actual posting when you generate invoices during periodic posting for both valuated and non-valuated leases.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Budget Specialist - Funds Management | SAP_BR_BUDGET_SPECIALIST | Budgeting | SAP_BR_BUDGET_SPECIALIST |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Budget Responsible - Funds Management | SAP_BR_BUDGET_RESPONSIBLE | Budgeting | SAP_BR_BUDGET_RESPONSIBLE |  |
| Administrator - Leasing | SAP_BR_RECM_ADMINISTRATOR | Administration - Leasing | SAP_BR_RECM_ADMINISTRATOR |  |

### Maintain Business Roles

Use

Use the Fiori app Maintain Business Roles (F1492) to add earmarked funds generation authorizations

Procedure

Create a new role by copying the role SAP_BR_RECM_SPECIALIST and add additional business catalogs

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the Fiori Launchpad | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori Launch Pad appears. |  |
| 2 | Open Maintain Business Roles (F1492). | Open Maintain Business Roles (F1492). |  |  |
| 3 | Enter the Role | Enter the role SAP_BR_RECM_SPECIALIST in the Business Role ID.Select and copy SAP_BR_RECM_SPECIALISTto create a new role | Role SAP_BR_RECM_SPECIALIST is available for selection |  |
| 4 | Create the Role | Select and copy SAP_BR_RECM_SPECIALISTto create a new roleProvide a new role name, such as Y_SAP_BR_RECM_SPECIALIST and description Contract Specialist – Leasing and Earmarked Funds. | A new role is created. |  |
| 5 | Add business catalogs to the new role created | Select Assigned Business Catalog tab and add business catalogs SAP_FIN_BC_FACT_GLACC_PC (General Ledger - Account Display) and SAP_PSM_BC_EMRKFNDS_API_PC (Earmarked Funds Document – API).Choose Save. | Additional catalogs are added to the new role Y_SAP_BR_RECM_SPECIALIST. |  |

### Maintain Business Users

Use

Use the Fiori app Maintain Business Users (F1303) to add the new role to the existing business user

Procedure

Assign the business role Y_SAP_BR_RECM_SPECIALIST to the business user RECM_SPECIALIST and RECM_ADMINISTRATOR.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the Fiori Launchpad | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori Launch Pad appears. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). |  |  |
| 3 | Select user | Enter RECM_SPECIALIST_ADMINISTRATOR and RECM_ADMINISTRATOR in the User Name and choose Go. |  |  |
| 4 | Edit business user | Select the business user RECM_SPECIALIST and choose Edit. | The business user RECM_SPECIALIST is available to be edited. |  |
| 5 | Add additional role | Go to the Assigned Business Roles tab, add the role Y_SAP_BR_RECM_SPECIALIST and save. | An additional role is added to the business user RECM_SPECIALIST. |  |
| 6 | Edit business user | Select the business user RECM_ADMINISTRATOR and choose Edit. | The business user RECM_SPECIALIST is available to be edited. |  |
| 7 | Add additional role | Go to the Assigned Business Roles tab, add the role Y_SAP_BR_RECM_SPECIALIST, and save. | An additional role is added to the business user RECM_ADMINISTRATOR. |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data for your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code, for example, 1710 for US> | Company code for example, 1710 |  |
| Vendor | <vendor, for example, 17300001 for US> |  |  |
| Cost Center | <cost center, for example, 17101101 for US> |  |  |
| Profit Center | YB600 |  |  |
| Functional Area | <functional area, for example, 1000 for US> |  |  |
| Fund | <fund, for example, G1100 for US> |  |  |
| Grant | NRG |  |  |

You can find general information about creating master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| 47C | Create Fund - MDS |
| 47D | Create Budget Period - MDS |
| 47E | Create Functional Area - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| OT6 or 1T6 – Lease-In Accounting | OT6 (Lease in Accounting for US State and Local) or1T6 (Lease in Accounting) |
| 78S - Earmarked Funds | Earmarked Funds Scope item |

### Preliminary Steps

#### Define Document Types for Earmarked Funds

Use

Use the configuration activity to define document type to be used for earmarked funds in lease-in contracts.

Procedure

Choose one of the following options according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as the Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open the Manage Your Solution (F1241) app | Frontend Fiori App:Open Manage Your Solution(F1241). | The Manage Your Solution(F1241)screen appears. |  |
| 3 | Open the Configure Your Solution app | Frontend Fiori App:Open the Configure Your Solution (F2962) app. | The Configure Your Solution screen appears. |  |
| 4 | Configure the document type | Search using the following criteria:Application Area: Public SectorSub Application Area: Earmarked FundsClick on the configuration item: Earmarked Funds and locate the Define Document Types for Earmarked Funds.Click Configure in the configuration step: Define Document Types for Earmarked Funds | The configuration: Define Document Types for Earmarked Funds appears. |  |
| 5 | Configure a new document type | Click on New Entries and enter the following values:Doc Category: 050Document Type: CLDocument Type Description: Commitment for lease-in contractsNumber Range: 32Field Status Group: SG30Tolerance Key: ST01Click Start WorkflowTemplate Type: ST01Click save and exit the transaction. | The configuration dialog Define Document Types for Earmarked Funds is open. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in the SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open the document types for earmarked funds | Go to the Business Processes Configuration app and search for the activity Define Document Types for Earmarked Funds.Choose the line item in the search result to see more details about this configuration activity.Choose Go to Activity to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Define Document Types for Earmarked Funds”: Overview screen appears. |  |
| 3 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Document Types for Earmarked FundsChoose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Document Types for Earmarked Funds screen appears. |  |
| 4 | Configure a new document type | Click on New Entries and enter the following values:Doc Category: 050Document Type: REDocument Type Description: Commitment for lease-in contractsNumber Range: 32Field Status Group: SG30Tolerance Key: ST01Click Start WorkflowTemplate Type: ST01Click save and exit the transaction. | The configuration dialog Define Document Types for Earmarked Funds is open. |  |

#### Define Contract Types

Use

Use the configuration activity to define contract type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Contract and Lease Management

1. For the row with Item Name of Contract Settings, choose Details (>).
2. For the Define Contract Types row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Contract Types.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Copy Contract Type | Select the contract type Y150 and click on Copy As | The Change View "Define Contract Types" view is displayed. |  |
| 2 | Enter Details | Make the following entries:Contract Type: <contract type>, for example, CE01Contract Type Text: Earmarked Funds - LeasesContract Type Short Text: Earmarked Funds - Leases |  |  |
| 3 | Save | Save your entries. | A new contract type is created. |  |

#### Permitted Contract Object Types for Each Contract Type

Use

Use the configuration activity to make setting for permitted contract object types for each contract type

Procedure

Choose one of the following options according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad appears. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution(F1241). | The Manage Your Solution(F1241) screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen appears. |  |
| 4 | Activate Earmarked Funds for Company Code | Set the Application Area to Finance.Set the Sub Application Area to Contract and Lease Management.Choose Contract Settings.Click Configure in the Permitted Contract Object Types for Each Contract Type row.Click New EntriesContract type: <CE01>Object Type: YCO06 VehiclesChoose Save. | The Change View " Permitted Contract Object Types for Each Contract Type" view appears. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Permitted Contract Object Types for Each Contract Type.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Permitted Contract Object Types for Each Contract Type screen appears. |  |
| 3 | Activate Earmarked Funds for Company Code | Click Configure in the Permitted Contract Object Types for Each Contract Type row.Click New EntriesContract type: <CE01>Object Type: YCO06 VehiclesChoose Save. | The Change View " Permitted Contract Object Types for Each Contract Type" view appears. |  |

Result

You have set up permitted object types for your contract type.

#### Make Settings for Roles per Object Type

Use

Use the configuration activity to make setting for business partner roles per contract type

Procedure

Choose one of the following options according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad appears. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution(F1241). | The Manage Your Solution(F1241) screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen appears. |  |
| 4 | Activate Earmarked Funds for Company Code | Set the Application Area to Finance.Set the Sub Application Area to Contract and Lease Management.Choose Business Partner.Click Configure in the Make Settings for Roles per Object Type row.Click New EntriesObject type: ISDiff. Criterion: Contract type created from the Create Contract Type for e.g., < CE01 >BP Role: FLVN00 Supplier (Financial Accounting)Object Address: Defaulted to NoBP Assignment: '+' - Selection dependent on role, maintenance not allowedChoose Save. | The Change View "Make Settings for Roles per Object Type" view appears. |  |

#

SAP Central Business Configuration

#

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Make Settings for Roles per Object Type.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Make Settings for Roles per Object Type screen appears. |  |
| 3 | Activate Earmarked Funds for Company Code | Click Configure in the Make Settings for Roles per Object Type row.Click New EntriesObject type: ISDiff. Criterion: Contract type created from the Create Contract Type for e.g., < CE01 >BP Role: FLVN00Object Address: Defaulted to NoBP Assignment: '+' - Selection dependent on role, maintenance not allowedChoose Save. | The Change View " Make Settings for Roles per Object Type " view appears. |  |

Result

Business partner role is assigned to the new contract type.

#### Activate Earmarked Funds for Company Code

Use

Use the configuration activity Activate Earmarked Funds for Company Code to active automatic generation of earmarked funds from contract and lease management for your company code

Procedure

Choose one of the following options according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launcpad appears. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). | The Manage Your Solution (F1241) screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen appears. |  |
| 4 | Activate Earmarked Funds for Company Code | Set the Application Area to Public Sector.Set the Sub Application Area to Earmarked Funds.Choose Earmarked Funds.Click Configure in the Activate Earmarked Funds for Company Code row.Select the checkbox Approval Active for your company code and enter a date (such as today’s date) in Approval Active from on which earmarked funds integration is activeChoose Save.Note Your company code should be available for activation without making a new entry if contract and lease management is enabled. | The Change View "Activate Earmarked Funds for Company Code " view appears. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Earmarked Funds for Company Code.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Activate Earmarked Funds for Company Code screen appears. |  |
| 3 | Activate Earmarked Funds for Company Code | Click Configure in the Activate Earmarked Funds for Company Code row.Select the checkbox Approval Active for your company code and enter a date (such as, today’s date) in Approval Active from on which earmarked funds integration is activeChoose Save.Note Your company code should be available for activation without making a new entry if contract and lease management is enabled. | The Change View "Activate Earmarked Funds for Company Code" view appears. |  |

Result

Your company code is enabled for earmarked funds integration from contract and lease management

#### Activate Earmarked Funds for CLM Contract Types

Use

Use the configuration activity Activate Earmarked Funds for CLM Contract Types to active automatic generation of earmarked funds from contract and lease management for a contract type

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Public Sector

Sub Application Area: Earmarked Funds

1. For the row with Item Name of Earmarked Funds, choose Details (>).
2. For the Activate Earmarked Funds for CLM Contract Types row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate Earmarked Funds for CLM Contract Types.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. | The Change View “Activate Earmarked Funds for CLM Contract Types " view is displayed. |  |
| 2 | Enter Details | Make the following entries and press Enter to have the values defaulted:Contract Type: <contract>, for example, CE01 |  |  |
| 3 | Enter Details | Make the following entries:Approval Active: SelectedApproval Active from: <date> (such as today's date, from which the earmarked funds integration for your contract type is active)The Document Category field defaults to 50 Funds Commitment (Vendor Contracts).Document Type: CLApproval: Only Initial Change Requires ApprovalThe Procedure defaults to Workflow of Earmarked Funds Document. |  |  |
| 4 | Save | Save your entries. | Your contract type is enabled for creation of earmarked funds and approval process. |  |

#### Define Flow Types for Earmarked Funds Generation

Use

Use the configuration activity Define Flow Types for Earmarked Funds Generation to enable integration of cash flow-relevant flow types for earmarked funds.

Procedure

Choose one of the following options according to your configuration environment for SAP S/4HANA Cloud Public Edition:

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto the Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad appears. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241). | The Manage Your Solution (F1241) screen appears. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen appears. |  |
| 4 | Define Flow Types for Earmarked Funds Generation | Set the Application Area to Public Sector.Set the Sub Application Area to Earmarked Funds.Choose Earmarked Funds.Click Configure in Define Flow Types for Earmarked Funds Generation row.Select the checkbox Relevant for Approval for flow types for which you require earmarked funds generation, such as, flow type V100.Choose Save. | The Change View “ Define Flow Types for Earmarked Funds Generation " view appears. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad appears. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Flow Types for Earmarked Funds Generation.Choose Open Documentation for the line item found to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Flow Types for Earmarked Funds Generation screen appears. |  |
| 3 | Define Flow Types for Earmarked Funds Generation | Select the Relevant for Approval indicator for the Flow Type V 1 00 for example.Choose Save. |  |  |

Result

The flow type is enabled for earmarked funds integration

## Overview Table

This scope item consists of several process steps and a report that are provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| ID (Role Template) | Name (Role Template) | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Workflows for Earmarked Funds](#unique_17) [page ] 21 | Configuration Expert - Business Process Configuration | Manage Workflows for Earmarked Funds (F6951) | Workflow is set up for earmarked funds generated from contract and lease management |
| [Create Contract](#unique_18) [page ] 22 | Contract Specialist - Leasing | Manage Contract (RECN) | The valuated contract is created. The system message confirms creation of the contract and the earmarked funds, and displays the new contract number. |
| [Approve Earmarked Funds](#unique_19) [page ] 26 | Budget Responsible - Funds Management | Frontend Fiori App:Open My Inbox (F0862) | Approval of Earmarked Funds |
| [Perform Periodic Posting](#unique_20) [page ] 28 | Accounts Payable Accountant - Leasing | Periodic Posting: Contracts (RERAPP) | The period posting is executed and the document number is displayed. |
| [Manage Earmarked Funds](#unique_21) [page ] 29 | Budget Specialist - Funds Management | Manage Earmarked Funds (F4657) | Earmarked funds for the contract and its consumption |
| [Cash Flow Update for Contract (Optional)](#unique_22) [page ] 30 | Administration - Leasing | Cash Flow Update for Contract (RECDCGOL) | Generated Earmarked Funds for next fiscal year |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Workflows for Earmarked Funds

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can set up workflows for earmarked funds for leases from contract and lease management.

Procedure

To execute this activity, work through the table step by step.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the user Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Earmarked Funds (F6951). | The Manage Workflows for Earmarked Funds(F6951) view appears showing the existing list of workflows. |  |
| 3 | Workflows | Choose Create | The dialog for the New Workflow appears |  |
| 4 | New Workflow | Enter the following data:Workflow Name: “New Workflow for CLM earmarked funds”Start Condition: Select “Document Type of Earmarked Funds” from the dropdown in the first field and enter CL in the second fieldChoose Create in the Steps section | The new step dialog appears |  |
| 5 | New Step | Enter the following data:Header Section:Step Type: Manual Approval of Earmarked FundsRecipient Section:Assignment By: RoleRole: Users with Business Catalog: Earmarked Funds - Document ApprovalChoose Create and then Save in the New Workflow dialog | A success message appears. The workflow is saved. |  |
|  | Activate Workflow | Choose Activate | The new workflow appears in the list of workflows with the status Active. |  |
| 7 | Change Workflow Order | Choose Define Order.The Define Order dialog appears.Select your Workflow and choose Move to move the selected workflow to the top.Choose Save . | Your workflow appears as the first workflow in the list with Order 1. |  |

### Create Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a valuated lease-in contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen appears. |  |
| 3 | Create Contract | Choose Create Object.Make the following entries and choose Continue:Contract Type: CE01, Earmarked Funds-LeasesChoose the contract type that has been enabled for earmarked funds integrationCompany Code: <company code, for example, 1710 for US> | Data is validated, the next screen General Data screen appears. |  |
| 4 | Insert General Data | Make the following entries (if the contract is relevant for valuation) and choose Partners to go to the next screen:Contract Name: <Your contract name>Contract Currency: (As defaulted)Note The company code currency is defaulted here. This can be changed to a different currency.Valuation relevance: No-Leasing Valuation | Data is validated.The Partners screen appears. |  |
| 5 | Assign New Partner | Choose Assign New Partner. Choose Supplier (Fin.Accounting).Make the following entries and choose Continue.Select the BP Role.Choose Copy.Business Partner: 17300001 | Data is validated.The business partner has been assigned. |  |
| 6 | Insert Term | Choose Term.Make the following entries:Contract start date: <Your contract start date>1st Contract End: <Your contract end date>Choose Enter and then Continue in the Correct Cash Flow From view. | The data is validated and the cash flow from date is entered.The Term has been created. |  |
| 7 | Insert Contract Objects | Choose Objects.Choose Assign to link a contract object to the contract, then choose Object:Contract Object: <Your description of the contract object> (for example, COB)Object Type: YCO06 VehiclesChoose an object type that has been enabled for budget account derivation based on the preliminary steps setup:Account Assignment: <Select a cost center for an account assignment> for example, CTR A000/17101101 | Data is validated.The Object screen appears. |  |
| 8 | Insert contract conditions | Choose Conditions.Choose Insert Condition(s) to select the Condition Type of your contract, such as IV10 Lease in Rate VehiclesMake the following entries for each condition:Unit Price: <Your unit price of the condition>Currency: <Your contract currency>Note Use the currency on the Contract Currency tab to create a reminder rule for your contract. Select the reminder rule type. General Data is defined as a default here, but can be changed to a different currency.Under Terms, choose Display or Change Term for Postings.Note If a foreign currency is used as the contract currency on the General Data tab or the Conditions tab, select a currency translation rule in the field below.Tax Type: <Y1>Tax Group: <your default tax group>, for example, Y-NONENote A default tax group can be defined in the configuration step Default Value for Tax Rate per Contract Type as described in the chapter Prerequisites - Default Value for Tax Rate per Contract Type.Tax Jurisdiction code: <Select a Tax Jurisdiction code> (for example, 7700000000)Note An additional posting term can be created. However, a tax jurisdiction code must be maintained in all posting terms.Choose Continue.Under Terms, choose Display or Change Term for the Organization Assignment and enter the following data:Profit Center: <Select a profit center> for example, YB600Functional Area: <Select a functional area, for example, 1000>Fund: <Select a Fund, for example, G1100>Grant: NRGNote The profit center, fund, grant and functional area entered here should match the values in the cost center master data, which is entered in the Account Assignment on the Objects tab in the contract.Similarly, the fund and grant should also be matched if fixed assignments exist in the cost center master data.Choose Continue.Choose Simulate to simulate the cash flow.Choose Back to Conditions.Note If the tax group Y-FULL and jurisdiction code is selected, you must create a statistical condition with the tax amount with the same condition type:Simulate the cash flow, to see the tax amount. | Data is validated.The cash flow can be simulated |  |
| 9 | Insert Critical Dates and Reminders for Contract | Choose Resubmission.Choose Create Reminder Rule (for example Before End of Term).For each reminder rule, make the following entries and choose Continue:Resubmission reason: <Select a reason>Then choose Save and go to the next screen. | The reminder rule is generated.The contract is saved, and the number of the new contract is released. |  |
| 10 | Save, Create Earmarked Funds and Activate Contract | Choose Save to save your contract.Go to the Approval tab and note down the earmarked funds document number | If a message appears informing you that registrations exist in your worklist for the contract, go to the registry, choose “Create Earmarked funds commitment document” and execute. |  |

To insert the valuation parameters:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Contract Valuation Specialist - Leasing. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori App | Open Manage Contract Valuation (RECECN). | The Contract screen appears. |  |
| 3 | Process Contract | Make the following entries and choose Change ObjectCompany Code: <company code, for example, 1710 for US)Contract: <Your contract> | Data is validated. |  |
| 5 | Fast Entry Valuation Parameters | Choose one valuation rule according to your contract, such as, US_UGSF_FL (GASB full accrual)Choose Continue.Interest Rate: <enter the correct interest rate>Choose Rule complete to complete the valuation rule.Please ignore the warning message Valuation is pending and still needs to be completed. | The screen appears. |  |
| 6 | Save Contract | Choose Save. | Data is validated. |  |

### Approve Earmarked Funds

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can approve earmarked funds.

Procedure

To execute this activity, work through the table step by step.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as the budget responsible. | The SAP Fiori launchpad appears. |  |
| 2 | Open My Inbox. | Frontend Fiori App:Open My Inbox (F0862) | The My Inbox(F0862) screen appears. |  |
| 3 | Select Workflow Item | The Earmarked Funds appears on the left-hand side of the screen under All Tasks.Click on the task | The details of the reservation appear on the right-hand side of the screen |  |
| 4 | Approve the Earmarked Funds | Choose Approve .Enter a Decision Note and choose Submit . | The Earmarked Funds is approved, and the workflow task disappears from the inbox. |  |

### Activate Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Activate lease-in contract

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Specialist - Leasing. | The SAP Fiori launchpad appears. |  |
| 2 | Access the SAP Fiori app | Open Manage Contract (RECN). | The Contract screen appears. |  |
| 3 | Activate Contract | Company Code: 1710Contract Number: <Your Contract Number>.Display ObjectActivate | Your contract is activated |  |

### Perform Periodic Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you perform the periodic posting of an existing contract as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Accounts Payable Accountant - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Periodic Posting: Contracts (RERAPP). |  |  |
| 3 | Periodic Posting: Contracts Selection | Make the following entries and choose Run:Company Code: <company code, for example, 1710 for US)Contract: <Your contract>Contract Type: <CE01>Month for Posting Run: <First month of the start date of your contract>Year of Posting Run: <Year of the start date of your contract>Posting Run Mode: Update RunType of Posting Run: Integrated posting | Data is validated, and the next screen Periodic Posting: Contract view is displayed. |  |
| 4 | Periodic Posting Contract | Check the posting and choose Documents and then go to the next screen. | Postings are green.The Documents view is displayed. |  |
| 5 | Periodic Posting Contract: Documents | Check the documents (accounts and cost elements) and choose Back. | Postings are correct.The Periodic Posting: Contracts view is displayed. |  |
| 6 | Periodic Posting: Contract | Choose Back. |  |  |

### Manage Earmarked Funds

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can report on earmarked fund generation and consumption..

Prerequisite

You performed periodic posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Budget Specialist - Funds Management |  |  |
| 2 | Access the SAP Fiori app | Open Manage Earmarked Funds (F4657) . |  |  |
| 3 | Run the earmarked funds report | Make the following entries and choose Go:Company Code: <company code>, for example, 1710 (for US)Document category: Funds CommitmentDocument type: SCReference: <Your contract number> | Data is validated. The Contract Valuation Run view is displayed. |  |
| 4 | Select your earmarked funds | View the document items and consumption. | The report displays earmarked funds and consumption for your contract (in this report, the contract number is found in the reference field). |  |

### Cash Flow Update for Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can run generation of earmarked funds for next fiscal year (provided your contract is valid and budget is available for the next fiscal year).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as an Administrator - Leasing. |  |  |
| 2 | Access the SAP Fiori app | Open Cash Flow Update for Contract (RECDCGOL). |  |  |
| 3 | Generate Cash Flows for Contracts to Create Earmarked Funds for Subsequent Fiscal Year | Make the following entries and choose Run:Company Code: <company code>, for example, 1710 (for U.S.)Contract Type: <CE01>Contract Number: <your contract number>Control Parameters section:Simulation: DeselectedForce Regeneration: SelectedGenerate Next Year’s Approval: Selected | Next year's earmarked funds are generated. |  |

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
> Flagged while digesting this document, not verified: Earmarked funds document type is inconsistent: Define Document Types sets Document Type CL under Configure Your Solution but RE under SAP Central Business Configuration (same description, number range and settings), while later steps (CLM contract type activation, workflow start condition) use CL and the Manage Earmarked Funds report filters on document type SC.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Contract says Valuation relevance 'No-Leasing Valuation', yet the Overview Table says the valuated contract is created and a separate procedure adds valuation parameters (valuation rule such as US_UGSF_FL).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6R3_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 48,761 chars in the whole document
