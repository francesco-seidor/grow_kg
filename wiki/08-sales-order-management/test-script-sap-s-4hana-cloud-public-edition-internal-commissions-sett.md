---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-internal-commissions-sett
title: Test Script SAP S/4HANA Cloud Public Edition - Internal Commissions Settlement for Sales (3TD_AE) (3TD_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 3TD (AE): internal sales commissions settlement via workforce condition contracts or SuccessFactors Incentive Management, with prerequisites and payroll follow-up."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/condition-contract-settlement]
aliases: [3TD_S4CLD2608_BPD_EN_AE]
keywords: ["Rebates, Commissions and Royalties Settlement", internal commissions settlement, workforce condition contracts, condition contract process variants, delta accruals settlement, final settlement, commissions on paid invoices, approval workflow, graduated scales, service rendered date]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TD_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-969
topic: 08-sales-order-management/condition-contract-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Internal Commissions Settlement for Sales (3TD_AE) (3TD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rebates, Commissions and Royalties Settlement** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Internal Commissions Settlement for Sales (3TD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232853588)

[2 Prerequisites 5](#_Toc232853589)

[2.1 System Access 5](#_Toc232853590)

[2.2 Roles 5](#_Toc232853591)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232853592)

[2.4 Additional Manual Configuration 7](#_Toc232853593)

[2.5 Preliminary Steps 8](#_Toc232853594)

[2.5.1 Prepare Transactional Data (Optional) 8](#_Toc232853595)

[2.5.2 Activate Condition Contract Type (Optional) 8](#_Toc232853596)

[2.5.3 Specify Partner Function for Commission Recipient (Optional) 10](#_Toc232853597)

[2.5.4 Define Condition Contract Process Variants (Optional) 11](#_Toc232853598)

[2.5.4.1 Define Process Variant for Using the Workflow 12](#_Toc232853599)

[2.5.4.2 Define Process Variant for Split Criteria Usage in Settlement 14](#_Toc232853600)

[2.5.4.3 Define Process Variant for Business Volume Selection Criteria Usage 17](#_Toc232853601)

[2.5.4.4 Define Process Variant for Commissions on Paid Invoices 19](#_Toc232853602)

[2.5.4.5 Define Process Variant to Activate Business Volume Selection by Service Rendered Date 22](#_Toc232853603)

[2.5.4.6 Maintain Automatic Account Determination 25](#_Toc232853604)

[2.5.5 Configure Approval Workflow for Workforce Condition Contracts (Optional) 28](#_Toc232853605)

[2.5.5.1 Manage Teams and Responsibilities 28](#_Toc232853606)

[2.5.5.2 Manage Workflow for Condition Contracts - Release Contract 30](#_Toc232853607)

[2.5.5.3 Manage Workflow for Condition Contracts - Release Settlement 31](#_Toc232853608)

[2.5.5.4 Manage Workflow for Settlement Documents 32](#_Toc232853609)

[2.5.6 Configure Approval Workflow for Personnel Settlement Documents (Optional) 34](#_Toc232853610)

[2.5.6.1 Activate Workflow and Define Profiles for Personnel Settlement Document Inbound 34](#_Toc232853611)

[2.5.6.2 Assign Profiles to External Compensation Codes 35](#_Toc232853612)

[2.5.6.3 Define Function and Function Profile 37](#_Toc232853613)

[2.5.6.4 Manage Teams and Responsibilities (Optional) 40](#_Toc232853614)

[2.5.6.5 Create Workflow for Settlement Documents 41](#_Toc232853615)

[3 Overview Table 43](#_Toc232853616)

[4 Test Procedures 46](#_Toc232853617)

[4.1 Commissions Processing Based on Workforce Condition Contracts 46](#_Toc232853618)

[4.1.1 Commissions Processing – Billing Document 46](#_Toc232853619)

[4.1.1.1 Create Condition Contract 46](#_Toc232853620)

[4.1.1.2 Check Business Volume (Optional) 50](#_Toc232853621)

[4.1.1.3 Delta Accruals Settlement (Optional) 51](#_Toc232853622)

[4.1.1.4 Check Personnel Settlement Document for Delta Accruals Settlement (Optional) 52](#_Toc232853623)

[4.1.1.5 Final Settlement 53](#_Toc232853624)

[4.1.1.6 Check Personnel Settlement Document for Final Settlement 54](#_Toc232853625)

[4.1.2 Commissions Processing – Billing Document Paid 56](#_Toc232853626)

[4.1.2.1 Post Incoming Payments (Optional) 57](#_Toc232853627)

[4.1.2.2 Create Condition Contract 59](#_Toc232853628)

[4.1.2.3 Check Business Volume (Optional) 62](#_Toc232853629)

[4.1.2.4 Delta Accruals Settlement (Optional) 62](#_Toc232853630)

[4.1.2.5 Final Settlement 63](#_Toc232853631)

[4.1.3 Commissions Processing – Subscription Billing 63](#_Toc232853632)

[4.1.3.1 Create Condition Contract 63](#_Toc232853633)

[4.1.3.2 Check Settlement Documents 64](#_Toc232853634)

[4.1.4 Commissions Processing with Approval Workflow 64](#_Toc232853635)

[4.1.4.1 Create Condition Contract 64](#_Toc232853636)

[4.1.4.2 Request Approval to Release Condition Contract 67](#_Toc232853637)

[4.1.4.3 Trigger Rework of Condition Contract (Optional) 68](#_Toc232853638)

[4.1.4.4 Rework Condition Contract (Optional) 69](#_Toc232853639)

[4.1.4.5 Release Condition Contract 70](#_Toc232853640)

[4.1.4.6 Check Business Volume (Optional) 71](#_Toc232853641)

[4.1.4.7 Delta Accruals Settlement (Optional) 71](#_Toc232853642)

[4.1.4.8 Request Release of Condition Contract for Settlement 71](#_Toc232853643)

[4.1.4.9 Release Condition Contract for Settlement 72](#_Toc232853644)

[4.1.4.10 Final Settlement 73](#_Toc232853645)

[4.1.4.11 Approve Release of Final Settlement Document to Accounting 73](#_Toc232853646)

[4.1.5 Commissions Processing with Graduated Scales 74](#_Toc232853647)

[4.1.6 Commissions Processing Using Service Rendered Date for Business Volume Selection 76](#_Toc232853648)

[4.1.7 Final Settlement with Adjustments (Optional) 77](#_Toc232853649)

[4.1.8 Commission Unlikelihood (Optional) 78](#_Toc232853650)

[4.2 Commissions Processing with Integration to SAP SuccessFactors Incentive Management 79](#_Toc232853651)

[4.2.1 Schedule Import of Commission Data from SAP SuccessFactors Incentive Management 79](#_Toc232853652)

[4.2.2 Check Personnel Settlement Documents 80](#_Toc232853653)

[4.2.3 Approve Release of Personnel Settlement Documents to Accounting via Workflow (Optional) 81](#_Toc232853654)

[4.2.4 Release Personnel Settlement Documents to Accounting 82](#_Toc232853655)

[4.2.5 Check Postings to FI Accounts (Optional) 83](#_Toc232853656)

[5 Follow-Up Processes 84](#_Toc232853657)

[5.1 Check Processing of Commissions in SuccessFactors (Optional) 84](#_Toc232853658)

[5.1.1 Check Data Import to SuccessFactors Employee Central 84](#_Toc232853659)

[5.1.2 Check Data Replication to SuccessFactors Employee Central Payroll 85](#_Toc232853660)

[5.1.3 Check Results of the Payroll Run 86](#_Toc232853661)

[5.1.4 Check Financial Postings for Payroll Run 87](#_Toc232853662)

[5.2 General Ledger Reporting and Cost Center Reporting (Optional) 88](#_Toc232853663)

## Purpose

Overview

The internal commissions settlement capabilities support you in offering sales commissions as incentives to employees and paying commissions on schedule. The internal commission settlement can be based on workforce condition contracts, or you can import commission data from SAP SuccessFactors Incentive Management. The payout of commissions happens with SAP SuccessFactors Employee Central and SAP SuccessFactors Employee Central Payroll.

In the first business scenario for internal commissions settlement, you use condition contracts from Condition Contract Management to enter the sales commission agreements for internal sales representatives. In a condition contract, you specify the personnel number of the commission recipient, organizational and process control parameter, the business volume selection criteria, the sales commission conditions, and the settlement calendar with settlement dates for delta accrual and final settlement. The delta accruals settlement reflects a procedure in which accruals for commissions aren't posted together with the transactional documents but subsequently in a specific settlement run. In final settlements of condition contracts, usually aligned with the salary process for employees, you perform the sales commission calculation based on business volume and commission conditions and you create the personnel settlement documents.

In the second business scenario, the process starts in SAP SuccessFactors Incentive Management with the calculation of the commissions amount for the employees and continues with the import of this data to create the personnel settlement documents in the SAP S/4HANA Cloud Public Edition.

Usually, personnel settlement documents created in both processing variants are automatically released to accounting leading to postings to the corresponding accounts for commissions in Finance. Optionally, the workflow functionality can be used in SAP S/4HANA Cloud Public Edition for the release of the personnel settlement documents to accounting.

The commission data contained in personnel settlement documents is transferred to SAP SuccessFactors Employee Central and then to SAP SuccessFactors Employee Central Payroll. The payroll run is executed in the payroll system. The payout to the employee is run and finally the posting on the liability account in the SAP S/4HANA Cloud Public Edition system is done.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Run all the steps described in the instruction setup guide for Internal Commissions Settlement for Sales (3TD) scope item.

This includes the setup of the integration between SAP SuccessFactors Incentive Management and S/4HANA, the setup of an SAP SuccessFactors Employee Central system and EC Payroll system for Germany and all related integrations.

In the SAP SuccessFactors Incentive Management system execute the following steps:

1. Upload all sales transaction data into SAP Commissions.
2. Upload Employee and Org data from SAP SuccessFactors Employee Central into SAP Commissions.
3. Set up Commissions rules in SAP Commissions.
4. Run the SAP Commissions pipeline.
5. Set up integration mappings in SAP Commissions.

For more information about steps 3-5, see [Integration with SAP SuccessFactors Employee Central](https://help.sap.com/docs/SAP_Commissions/85ce2a3717a644afa2bbd21f70387549/724c5a907c231014a804993ce4041860.html).

This includes the creation of EC master data and calculation of the commission amounts for the employees.

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
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |
| Contract Manager - Commissions | SAP_BR_CONTR_MGR_COMMSN | Commissions and Incentives | SAP_SD_SPT_COMMSN_MNTN_PC |  |
| Settlement Clerk - Commissions | SAP_BR_SETL_CLERK_COMMSN | Commissions and Incentives | SAP_SD_SPT_COMMSN_PROC_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code for S/4HANA and EC-Payroll System |  |
| Employee | 50004751 |  |  |
| Compensation Reason | 4930 | Commissions Payment |  |
| Compensation Reason | 4931 | Deduction from Commissions Payment |  |
| Compensation Reason | 4932 | Product Bonus |  |
| Compensation Reason | 4933 | Deduction from Product Bonus |  |
| GL Accounts | 61500100 (Expense account) | Internal Commissions |  |
| GL Accounts | Accruals Account: 21772100 (Liability account) | Provision for Internal Commissions |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2bd36100c113885d4ffb4aba534ab87f)

### Preliminary Steps

#### Prepare Transactional Data (Optional)

Purpose

For Internal Commissions: Billing Document process, the business volume for sales commissions settlement is determined from billing documents. To prepare transactional test data, you can follow the Sell from Stock (BD9) scope item which describes the sales process from a standard sales order to a billing document.

For Internal Commissions: Billing Document Paid process, the business volume for commission settlement is determined from paid billing documents, which means the related accounting documents need to be cleared. To prepare transactional test data, you can follow the steps described in the scope items Sell from Stock (BD9) and Accounts Receivable (J59).

Preparing transactional data is a required step. You can perform this step before or after creating the condition contract, or after each settlement run.

Procedure

Perform necessary preliminary steps, as for instance an initial stock set up for materials, and test activities for sales order, delivery and billing document creation as described in the Sell from Stock (BD9) scope item's test script using the master data from this document.

#### Activate Condition Contract Type (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate the condition contract types for post-test procedures.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Configure Condition Contract Types for Workforce Condition Contracts. | The Configure Condition Contract Types for Wor..: Change screen displays. |  |
| 6 | Remove Block | In column Block, choose Not Blocked – Can be Used for the condition contract type you need for post-test procedure:0CSE Internal Commission: Subscription BillChoose Save. | The condition contract type is no longer blocked. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Condition Contract Types for Workforce Condition Contracts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 3 | Remove Block | In column Block, choose Not Blocked – Can be Used for the condition contract type you need for post-test procedure:0CSE Internal Commission: Subscription BillChoose Save. | The condition contract type is no longer blocked. |  |

#### Specify Partner Function for Commission Recipient (Optional)

Purpose

In the commission processing based on workforce condition contracts, you can identify business volume generating billing documents based on defined partner functions maintained in these documents. You can enter a partner function in the sales order on header level to be valid for all items or on item level.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options to specify the relevant partner functions for business volume selection. The partner function chosen must represent a person (partner type PE Personnel Number).

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Internal Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 5 | Go to Partner Functions Overview | Choose Configure on the right to Specify Partner Functions to Identify Internal Commission Recipients configuration step. | The Specify Partner Functions to I..: Change screen displays. |  |
| 6 | Specify Partner Function | Choose New Entries and enter a partner function with partner type PE.Choose Save. | The partner function is created to be mapped with partner type PE. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Partner Functions to Identify Internal Commission Recipients.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 3 | Specify Partner Function | Choose New Entries and enter a partner function with partner type PE.Choose Save. | The partner function is created to be mapped with partner type PE. |  |

#### Define Condition Contract Process Variants (Optional)

This chapter defines condition contract process variants to also test variations of the core process. A process variant is used to define limited variations for condition contract maintenance and settlement that are configured for a condition contract type without changing the overall character of the process defined by a condition contract type.

In this chapter we describe process variants for different purposes. Note that you can also combine settings from these process variants. If you assign a condition contract process variant to a new condition contract you have to enhance the account determination settings. The process variant is a key field in the relevant condition table. We describe how you maintain account determination settings for the first process variant for approval workflow. Proceed in the same way for all other process variants that you want to test.

##### Define Process Variant for Using the Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to activate the workflow for sales commission processing based on workforce condition contracts.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Process Variants Overview | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZE01 Internal Commission with WorkflowSettlement Management Status Group: Personnel CommissionsDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 7 | Assign Condition Contract Types to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new internal commissions condition contract. | The relevant condition contract type is assigned to newly-created process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZE01 Internal Commission with WorkflowSettlement Management Status Group: Personnel CommissionsDefault Application Status for Settlement Documents: Workflow Release RequiredApproval Process: 1 Approval Process Is ActiveChoose Save. | The process variant is created. |  |
| 4 | Assign Condition Contract Type to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save.Note If you want to make use of the workflow feature, enter this condition contract process variant when you create a new internal commissions condition contract. | The relevant condition contract type is assigned to newly-created process variant. |  |

##### Define Process Variant for Split Criteria Usage in Settlement

Purpose

In this activity, you create a condition contract process variant to activate further split criteria defined in the profiles for business volume determination.

Split criteria for condition contract settlement – defined in Customizing in the profiles for business volume determination - are used to point up the contribution of different business objects to the overall sales commission amount. In the profile for business volume determination relevant for sales commission settlement, some split criteria, such as material or profit center, are defined as always active. The usage of these split criteria cannot be influenced with a condition contract process variant. But there are other split criteria which are defined as inactive until activated by a process variant. Note that for the test of an additionally activated split criterion you also have to prepare the business volume data accordingly with different values for the split criterion.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE02 Sales Commission Split Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: <settlement document type>, for example, 0CSA Internal Commission: Billing DocumentField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0CSE.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Contract Process Variant | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE02 Sales Commission Split Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Condition Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate/Deactivate Split Criteria for Settlement | Double-click Split Criteria for Settlement on the left of the screen.Choose New Entries and make the following entries:Profile: <settlement document type>, for example, 0CSA Internal Commission: Billing DocumentField Name: select from field help list, for example AUFNRUsage as Split Criterion: select from the dropdown list as used or not usedNote In case of Subscriptions, if you want the Provider Contract information to appear in the Journal Entries resulting from the settlement process, then please maintain the following entries:PROVIDERCONTRACTPROVIDERCONTRACTITEMSETTLMTADDLREFDOCCATThis is valid for Condition Contract Types that are relevant for Subscription Billing - 0CSE.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant for Business Volume Selection Criteria Usage

Purpose

In this activity, you create a condition contract process variant to change the usage of business volume selection criteria defined in the relevant set of field combinations.

To allow high flexibility in the business volume selection, the set of field combinations for sales commission settlement provides many business volume selection criteria. However, this larger number can complicate the maintenance of business volume selection criteria in the condition contract, as users need to find the desired field combination in a long list when they want to enter a new line. With a suitable condition contract process variant, you can reduce the scope of business volume selection criteria to the relevant ones.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Commission Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration step. | The "Define Condition Contract Process Variant": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE03 Commission Selection Criteria Adaptation | The process variant is created. |  |
| 7 | Assign Condition Contract Types to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save. | The relevant condition contract type is assigned to newly- created process variant. |  |
| 8 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Internal Commission SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Condition Contract Process Variants | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Commission Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE03 Commission Selection Criteria Adaptation | The process variant is created. |  |
| 4 | Assign Condition Contract Type to the Process Variant | Double-click the Condition Contract Types on the left.Choose New Entries and make the following entry:Contract Type: 0CSAChoose Save. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Change the Usage of Selection Criteria for Business Volume Determination | Double-click Business Volume Selection Criteria on the left of the screen.Choose New Entries and make the following entries:Set of Field Combinations: Internal Commission SettlementField Combination: select from field help list, for example, 0035Note You can choose 0069 for Customer Hierarchy.Usage of Field Combination: select from the dropdown list as used or not usedChoose Save. | The usage of field combination is changed with the process variant. |  |

##### Define Process Variant for Commissions on Paid Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a condition contract process variant to enable the use of business volume table groups for business volume determination. This ensures that the commission amount calculation considers only paid invoices.

This approach is applicable when the condition contract type 0CSC does not meet business requirements. For a comparison between condition contract type 0CSC and condition contract type 0CSA used with process variant ZE04, refer to the Commissions Processing – Billing Document Paid section in the Test Procedures.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE04 Commission on Paid InvoicesChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSANote Add further condition contract types if you want to test the process variant for other sales commission scenarios, for example, 0CSE. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0CSABVTab Grp.: 0C02Usage: select from the dropdown list, Use in Condition Contract SettlementNote Add more Profile and BVTab Grp entries if you want to test the process variant for other internal commission scenarios, for example, 0CSE.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZE04 Commission on Paid InvoicesChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSANote Add further condition contract types if you want to test the process variant for other internal commission scenarios, for example, 0CSE. | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Activate Usage of Business Volume Table Group | Double-click on Business Volume Table Group on the left of the screen.Choose New Entries and make the following entries:Profile: 0CSABVTab Grp.: 0C02Usage: select from the dropdown list, Use in Condition Contract SettlementNote Add more Profile and BVTab Grp entries if you want to test the process variant for other internal commission scenarios, for example, 0CSE.Click Enter and choose Save. | The split criteria usage is changed with the process variant. |  |

##### Define Process Variant to Activate Business Volume Selection by Service Rendered Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a condition contract process variant that enables you to use service rendered date instead of billing date for the selection of billing documents to determine the business volume.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Sales Rebate Settlement | Enter the following filters:Application Area: SalesSub Application Area: Incentive and Commission ManagementIn the items table, select the item with item name: Internal Commission Settlement. | The Configure Your Solution - Internal Commission Settlement screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Define Condition Contract Process Variants configuration steps. | The "Define Condition Contract Process Variants": Change screen displays. |  |
| 6 | Create Process Variant | Choose New Entries and make the following entry:Condition Contract Process Variant: ZE05 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 7 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSABusiness Volume Selection Date Type: 0001 Service Rendered Date | The relevant condition contract type is assigned to newly-created process variant. |  |
| 8 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RCS3 to inactive:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS3Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RCS4:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS4Usage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Condition Contract Process Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Sales Rebate Settlement screen displays. |  |
| 3 | Create Process Variant | Choose New Entries and make the following entries:Condition Contract Process Variant: ZE05 BusVol Selection by Service Rendered DateChoose Save. | The process variant is created. |  |
| 4 | Assign Contract Types to the Process Variant | Double-click Condition Contract Types on the left of the screen.Choose New Entries and make the following entry:Contract Type: 0CSABusiness Volume Selection Date Type: 0001 Service Rendered Date | The relevant condition contract type is assigned to newly-created process variant. |  |
| 5 | Enter Condition Types / Tables | This step is to ensure that only that accrual condition type which works with Service Rendered Date is selectable when creating your condition contract with this process variant.Double-click Condition Types / Tables on the left of the screen.Choose New Entries and make the following entries to set the condition type RCS3 to inactive:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS3Usage of Condition Level: 1 InactiveRepeat the current step. Make the following entries to activate condition type RCS4:Application: V Sales/DistributionCond.Type Group: 0C01Condition Type: RCS4Usage of Condition Level: 2 ActiveClick Enter and choose Save. |  |  |

##### Maintain Automatic Account Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you specify G/L account for sales commission processing.

If you assign a condition contract process variant to a new condition contract you have to enhance the account determination settings. The process variant is a key field in the relevant condition table.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

In the following steps, we show how to create the necessary entry for the first defined process variant ZE01 Sales Commission with Workflow.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241).Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Open Configuration Item for Chart of Accounts | Enter the following filters:Application Area: FinanceSub Application Area: General LedgerIn the items table, select the item with item name: Chart of Accounts. | The Configure Your Solution – Chart of Accounts screen displays. |  |
| 5 | Go to Configuration Details | Choose Configure on the right to Automatic Account Determination configuration step. | The Automatic Account Determination 1. Area screen displays. |  |
| 6 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 7 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 8 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORC Commission SettlementCompany Code: 3310Contract Process Variant: ZE01Account Key: 0C3 Internal CommissionG/L Account: 61500100Accruals Acc.: 21772100Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 9 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Automatic Account Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Automatic Account Determination 1. Area screen displays. |  |
| 3 | Fill in Basic Information | Make the following entries:Area: SalesSubarea: Sales BillingProcess: Assign G/L AccountsChoose Step 2. | The Automatic Account Determination 2. Parameters screen displays. |  |
| 4 | Fill in Relevant Information | Make the following entries:Chart of Accounts: YCOAApplication: VCondition Table: 016Choose Step 3. | The Automatic Account Determination 3. Account Assignments screen displays. |  |
| 5 | Maintain G/L Account Assignment | Choose Add and scroll down to the bottom.Make the following entries:Condition Type: KORC Commission SettlementCompany Code: 3310Contract Process Variant: ZE01Account Key: 0C3 Internal CommissionG/L Account: 61500100Accruals Acc.: 21772100Choose Review. | The Automatic Account Determination screen displays with relevant information. |  |
| 6 | Review in the Information and Save | Choose Save. | The G/L account assignment is saved. |  |

#### Configure Approval Workflow for Workforce Condition Contracts (Optional)

##### Manage Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the teams and responsibilities for sales commission workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. | The Team screen displays. |  |
| 4 | Enter General Information | Make the following entries and choose Enter:Name: for example, <CCM_TEST_TEAM_SD_(Country Code)>Description: for example, <Condition Contract Management Team Sales (Country Name)>Status: EnabledType: SCMTV Sales Condition Contract Team TypeCondition Contract Category: 0E | The team is created. |  |
| 5 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: for example, <Sales_Manager> | The Team screen displays. |  |
| 6 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.SCCM_F1: Condition Contract Release ApprovalSCCM_F2: Condition Contract Settlement Release ApprovalChoose Create to create the team. | The team is saved. |  |
| 7 | Create a New Team | Go back and choose Create. | The Team screen displays. |  |
| 8 | Enter General Information | Make the following entries and choose Enter:Name: for example, <STLMT_TEST_TEAM_SD_(Country Code)>Description: for example, <Settlement Management Team Sales (Country Name)>Status: EnabledType: SMT Settlement ManagementSettlmtDocType: for example, 0CA1 | The team is created. |  |
| 9 | Add Team Members | In Team Members, choose Create.From Items section, select a business partner checkbox and choose OK.Business Partner: for example, <Sales_Manager> | The Team screen displays. |  |
| 10 | Add Function to Team Members | In the Functions field, choose Select. In the Select: Functions window, choose the following functions, and choose OK.STLMTAPR: Settlement Document ApproverChoose Create. | The team is saved. |  |
| 11 | Check Team Status | Navigate to the Manage Teams and Responsibilities worklist, and verify the status of the team by selecting Go.The status should be Enabled. | The team status is enabled. |  |

##### Manage Workflow for Condition Contracts - Release Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Release Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Release of Condition Contract - Single Step Level ApprovalUnder Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Condition ContractRole: Condition Contract Release ApprovalIn the Exception Handling section, make the following settings for Rework Condition Contract:Required Action: Rework of Condition ContractAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Condition Contracts - Release Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Condition Contracts (F3680). | The Manage Workflows screen displays. |  |
| 3 | Select Relevant Workflow | Select Settlement Release of Condition Contract in the top left dropdown list.Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for Settlement Release of Cond. Contract - Single StepChoose Create under Steps. | The New Step screen displays. |  |
| 5 | Input Workflow Details | Make the following entries:Step Type: Release of Condition Contract for SettlementRole: Condition Contract Settlement Release ApprovalRework Condition Contract:Required Action: Rework of Condition Contract for Settlement ReleaseAction Result: Restart WorkflowChoose Create. | The New Workflow screen displays. |  |
| 6 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 7 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

##### Manage Workflow for Settlement Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain workflow settings for condition contracts settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Settlement Documents (F3681). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. | The New Workflow screen displays. |  |
| 4 | Enter General Information | Make the following entry:Workflow Name: Workflow for the Approval of Settlement Document (To Accounting)Under Steps, choose Create. | The New Step screen displays. |  |
| 5 | Input Details | Make the following entries:Step Type: Release of Settlement DocumentRole: Settlement Document ApproverChoose Create. | The New Workflow screen displays. |  |
| 6 | Create New Step | Under Steps, choose Create. | The New Step screen displays. |  |
| 7 | Input Details | Make the following entry:Step Type: Automatic Change of Settlement Document StatusChoose Create. | The New Workflow screen displays. |  |
| 8 | Save Workflow | Choose Save. | The Workflow Details screen displays. |  |
| 9 | Activate Workflow | Choose Activate. | The workflow is activated. |  |

#### Configure Approval Workflow for Personnel Settlement Documents (Optional)

##### Activate Workflow and Define Profiles for Personnel Settlement Document Inbound

Purpose

This process step shows you how to activate workflow and define profiles for Personnel Settlement Document Inbound.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Define Profiles for Personnel Settlement Document Inbound | Choose Define Profiles for Personnel Settlement Document Inbound in the following area: Sales > Incentive and Commissions Management > Sales Commission Integration > Set up the personnel settlement integration for sales commissions . |  |  |
| 5 | Create New Profile for Personnel Settlement Document Inbound | Choose New Entries and make the following entries:Profile for Personnel Settlement Document Inbound: <Z000 / Profile for Personnel Settlement Document Inbound>Settlement Process Type: <0CG0 – Commission Personnel External Settlement>Settlement Document Type for Credit to Employee: <0CG1 – Commission Personnel ExtSettl Credit>Compensation Reason for Credit to Employee: <4930 – Commission Payment>Settlement Document Type Debit to Employee: <0CG2 – Commission Personnel ExtSettl Debit>Compensation Reason for Debit to Employee: < 4931 – Deduction from Commissions Payment >Settlement Management Status Group: <0CP1 – Personnel Commissions>Default Application Status for Settlement Documents: <0CP3 – Workflow Release Required>Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Profiles for Personnel Settlement Document Inbound | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Profiles for Personnel Settlement Document Inbound.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Profile for Personnel Settlement Document Inbound | Choose New Entries and make the following entries:Profile for Personnel Settlement Document Inbound: <Z000 / Profile for Personnel Settlement Document Inbound>Settlement Process Type: <0CG0 – Commission Personnel External Settlement>Settlement Document Type for Credit to Employee: <0CG1 – Commission Personnel ExtSettl Credit>Compensation Reason for Credit to Employee: <4930 – Commission Payment>Settlement Document Type Debit to Employee: <0CG2 – Commission Personnel ExtSettl Debit>Compensation Reason for Debit to Employee: < 4931 – Deduction from Commissions Payment >Settlement Management Status Group: <0CP1 – Personnel Commissions>Default Application Status for Settlement Documents: <0CP3 – Workflow Release Required>Choose Save. |  |  |

##### Assign Profiles to External Compensation Codes

Purpose

This process step shows you how to assign profiles to external compensation codes.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Assign Profiles to External Compensation Codes | Choose Assign Profiles to External Compensation Codes in the following area: Sales > Incentive and Commissions Management > Sales Commission Integration > Set up the personnel settlement integration for sales commissions . |  |  |
| 5 | Create New Profile for Personnel Settlement Document Inbound | Choose New Entries and make the following entries:External Compensation Code: <Z000000000 / Test External Compensation Code>Profile for Personnel Settlement Document Inbound: <Z000 – Profile for Personnel Settlement Document Inbound >Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Profiles to External Compensation Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Profile for Personnel Settlement Document Inbound | Choose New Entries and make the following entries:External Compensation Code: <Z000000000 / Test External Compensation Code>Profile for Personnel Settlement Document Inbound: <Z000 – Profile for Personnel Settlement Document Inbound >Choose Save. |  |  |

##### Define Function and Function Profile

Purpose

This process step shows you how to define function and function profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Define Functions | Choose Define Functions in the following area: Application Platform and Infrastructure > Responsibility Management > Functions > Configure functions and function profiles for responsibility management. |  |  |
| 5 | Create New Function | Choose New Entries and make the following entries:Function: <ZPSDOCAPR>Function Description: <Personnel Settlement Document Approver>Choose Save. |  |  |
| 6 | Go Back | Choose Back. |  |  |
| 7 | Define Functions Profile | Choose Define Functions Profile. |  |  |
| 8 | Assign Function to Function Profile | Select STLMT and choose Function Profile to Function Mapping.Choose New Entries and make the following entries:Function: <ZPSDOCAPR>Choose Save. |  |  |
| 9 | Go Back | Choose Back. |  |  |
| 10 | Define Team Types | Choose Define Team Types in the following areas: Application Platform and Infrastructure > Responsibility Management > Teams > Configure team types for responsibility management . |  |  |
| 11 | Create New Team Type | Choose New Entries and make the following entries:Team Type: <ZPSDOC>Category: <STLMT>Team Type Description: <Personnel Settlement Team> |  |  |
| 12 | Define Exclude Standard Responsibility Definition | Select the new team and choose Exclude Standard Responsibility Definition.Choose New Entries and make the following entries:Responsibility Definition Name: DISTRIBUTION_CHANNEL,DIVISION,PURCHASINGGROUP,PURCHASINGORGANIZATION,SALES_GROUP,SALES_OFFICE,SALES_ORGANISATION.Choose Save.Choose Back twice. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Functions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Function | Choose New Entries and make the following entries:Function: <ZPSDOCAPR>Function Description: <Personnel Settlement Document Approver>Choose Save. |  |  |
| 4 | Go Back | Choose Back. |  |  |
| 5 | Define Functions Profile | Choose Define Functions Profile. |  |  |
| 6 | Assign Function to Function Profile | Select STLMT and choose Function Profile to Function Mapping.Choose New Entries and make the following entries:Function: <ZPSDOCAPR>Choose Save. |  |  |
| 7 | Go Back | Choose Back. |  |  |
| 8 | Define Team Types | Choose Define Team Types in the following areas: Application Platform and Infrastructure > Responsibility Management > Teams > Configure team types for responsibility management . |  |  |
| 9 | Create New Team Type | Choose New Entries and make the following entries:Team Type: <ZPSDOC>Category: <STLMT>Team Type Description: <Personnel Settlement Team> |  |  |
| 10 | Define Exclude Standard Responsibility Definition | Select the new team and choose Exclude Standard Responsibility Definition.Choose New Entries and make the following entries:Responsibility Definition Name: DISTRIBUTION_CHANNEL,DIVISION,PURCHASINGGROUP,PURCHASINGORGANIZATION,SALES_GROUP,SALES_OFFICE,SALES_ORGANISATION.Choose Save.Choose back twice. |  |  |

##### Manage Teams and Responsibilities (Optional)

Purpose

This process step shows you how to manage teams and responsibilities (optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create a New Team | Choose Create. |  |  |
| 4 | Enter General Information | Make the following entries and press Enter:Name: <PSTL_COMM_TEAM>Description: <Personnel Settlement Approvers>Status: <Enabled>Type: <Personnel Settlement Team (ZPSDOC)> |  |  |
| 5 | Add Team Members | In the Team Members section, choose Create.From Items section, select a Business Partner check box and choose OK:Business Partner: <Sales_Manager> |  |  |
| 6 | Add Functions to Team Members | In the Functions field, choose Select. On the Select: Functions screen, choose the following functions, and choose OK:ZPSDCOAPR: <Personnel Settlement Document Approver>Choose Save to save the team. |  |  |

##### Create Workflow for Settlement Documents

Purpose

This process step shows you how to create workflow for settlement documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Personnel Settlement Documents (F4021). | The Manage Workflows screen displays. |  |
| 3 | Create New Workflow | Choose Create. |  |  |
| 4 | Enter General Information | Make the following entries:Name: <Approve Personnel Settlement Document>Under Steps, choose Create. |  |  |
| 5 | Enter Details | Make the following entries:Type: <Approve Personnel Settlement Document>Role: <Settlement Document Approver>Choose Create.Choose Steps > Create again to add another step.Type: <Automatic Change of Personnel Settlement Document Status>Choose Create. |  |  |
| 6 | Save Workflow Settings | Choose Save. |  |  |
| 7 | Activate Workflow | Choose Activate. |  |  |

## Overview Table

This scope item consists of several steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Commissions Processing Based on Workforce Condition Contracts |  |  |  |
| Commissions Processing – Billing Document |  |  |  |
| [Create Condition Contract](#unique_27) [page ] 46 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Check Business Volume (Optional)](#unique_28) [page ] 50 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_29) [page ] 51 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Check Personnel Settlement Document for Delta Accruals Settlement (Optional)](#unique_30) [page ] 52 | Settlement Clerk - Commissions | Manage Personnel Settlement Documents (F3808A) |  |
| [Final Settlement](#unique_31) [page ] 53 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Check Personnel Settlement Document for Final Settlement](#unique_32) [page ] 54 | Settlement Clerk - Commissions | Manage Personnel Settlement Documents (F3808A) |  |
| [Commissions Processing – Billing Document Paid](#unique_33) [page ] 56 |  |  |  |
| [Post Incoming Payments (Optional)](#unique_34) [page ] 57 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| [Create Condition Contract](#unique_35) [page ] 59 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Check Business Volume (Optional)](#unique_36) [page ] 62 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_37) [page ] 62 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Final Settlement](#unique_38) [page ] 63 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Commissions Processing – Subscription Billing](#unique_39) [page ] 63 |  |  |  |
| [Create Condition Contract](#unique_40) [page ] 63 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Check Settlement Documents](#unique_41) [page ] 64 | Settlement Clerk - Commissions | Manage Personnel Settlement Documents (F3808A) |  |
| Commissions Processing with Approval Workflow |  |  |  |
| [Create Condition Contract](#unique_42) [page ] 64 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Request Approval to Release Condition Contract](#unique_43) [page ] 67 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Trigger Rework of Condition Contract (Optional)](#unique_44) [page ] 68 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Rework Condition Contract (Optional)](#unique_45) [page ] 69 | Contract Manager - Commissions | My Inbox - All Items (F0862) |  |
| [Release Condition Contract](#unique_46) [page ] 70 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Check Business Volume (Optional)](#unique_47) [page ] 71 | Settlement Clerk - Commissions | Display Business Volume - Condition Contracts (WB2R_BUSVOL) |  |
| [Delta Accruals Settlement (Optional)](#unique_48) [page ] 71 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Request Release of Condition Contract for Settlement](#unique_49) [page ] 71 | Settlement Clerk - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Release Condition Contract for Settlement](#unique_50) [page ] 72 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Final Settlement](#unique_51) [page ] 73 | Settlement Clerk - Commissions | Settle Sales Commissions (WB2R_SP_ICOM) |  |
| [Approve Release of Final Settlement Document to Accounting](#unique_52) [page ] 73 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Commissions Processing with Graduated Scales](#unique_53) [page ] 74 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Commissions Processing Using Service Rendered Date for Business Volume Selection](#unique_54) [page ] 76 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Final Settlement with Adjustments (Optional)](#unique_55) [page ] 77 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| [Commission Unlikelihood (Optional)](#unique_56) [page ] 78 | Contract Manager - Commissions | Manage Condition Contracts - Internal Commissions (F7263) |  |
| Commissions Processing with Integration to SAP SuccessFactors Incentive Management |  |  |  |
| [Schedule Import of Commission Data from SAP SuccessFactors Incentive Management](#unique_57) [page ] 79 | Configuration Expert - Business Network Integration | Schedule Commission Data Import - Personnel Settlement (F3998) |  |
| [Check Personnel Settlement Documents](#unique_58) [page ] 80 | Settlement Clerk - Commissions | Manage Personnel Settlement Documents (F3808A) |  |
| [Approve Release of Personnel Settlement Documents to Accounting via Workflow (Optional)](#unique_59) [page ] 81 | Sales Manager | My Inbox - All Items (F0862) |  |
| [Release Personnel Settlement Documents to Accounting](#unique_60) [page ] 82 | Settlement Clerk - Commissions | Release Documents - Personnel Settlement (WPSDOC_RELEASE) |  |
| [Check Postings to FI Accounts (Optional)](#unique_61) [page ] 83 | General Ledger Accountant | Manage Journal Entries (F0717A) |  |
| [Follow-Up Processes](#unique_62) [page ] 84 |  |  |  |
| [Check Processing of Commissions in SuccessFactors (Optional)](#unique_63) [page ] 84 |  |  |  |
| [Check Data Import to SuccessFactors Employee Central](#unique_64) [page ] 84 | Authorization for HR administration | SuccessFactors Employee Central |  |
| [Check Data Replication to SuccessFactors Employee Central Payroll](#unique_65) [page ] 85 | Authorization for HR administration | SuccessFactors Employee Central Payroll |  |
| [Check Results of the Payroll Run](#unique_66) [page ] 86 | Authorization for HR administration | SuccessFactors Employee Central Payroll |  |
| [Check Financial Postings for Payroll Run](#unique_67) [page ] 87 | Authorization for HR administration | SuccessFactors Employee Central Payroll |  |
| [General Ledger Reporting and Cost Center Reporting (Optional)](#unique_68) [page ] 88 |  |  |  |

## Test Procedures

This chapter comprises the test procedures for the two main internal sales commissions processing variants covered by this scope item.

In the first section Sales Commissions Processing Based on Workforce Condition Contracts, we describe the first processing variant for internal commissions settlement. Here, you use condition contracts from Condition Contract Management to enter the sales commission agreements for internal sales representatives. This processing variant extends the business process for sales as for instance described in scope item BD9 Sell from Stock. The business volume for sales commissions settlement is determined from billing documents. Ideally, the workforce condition contract is created first before you start to enter sales documents in the system. However, you can also create condition contracts subsequently with a validity period starting in the past. Also, sales commissions processing and sales run in parallel in that sense that you process the settlements for billing documents entered continuously during the condition contract’s validity period. For information to set up necessary transactional data, see chapter Prepare Transactional Data.

As a first variation of the corresponding settlement process, you can choose to only consider paid billing documents. In the third subsection, you determine the business volume from billing documents that result from subscription billing transactions.

For each of these process variants, you can configure a workflow process. And during the condition contract creation, you can also use a customer hierarchy node in combination with condition contract types for customers. Only hierarchies of type Customer Hierarchy – Sales can be used.

In the second section Sales Commissions Processing with Integration to SAP SuccessFactors Incentive Management, we describe the integration scenario, for which the process starts in SAP SuccessFactors Incentive Management with the calculation of the commissions amount for the employees and continues with the import of this data in order to create the personnel settlement documents in SAP S/4HANA Cloud Public Edition. Before you can test this processing variant, you must have completed several additional configuration steps. For more information, see Prerequisites.

### Commissions Processing Based on Workforce Condition Contracts

#### Commissions Processing – Billing Document

##### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a workforce condition contract for an employee as condition contract partner.

In the following steps, we show you how to create a 0CSA Internal Commission: Billing Document condition contract.

When using the commission recipient as business volume selection criterion, you have to enter the commission recipient in sales order items for partner function that you have defined in the configuration mentioned in chapter Specify Partner Function for Commission Recipient. If you have already created such sales orders when processing scope item Sell from Stock (BD9), you enter here the commission recipient you have used.

Usually, you pay out sales commissions monthly with the regular salary. Accordingly, you specify a final settlement at the end of each month. Partial settlement usually does not play a role, and we do not consider it in our test procedure. Doing a monthly final settlement, delta accruals settlement is not required. Only when sales commissions payout happens in larger periods as for instance quarterly, it makes sense to post accruals in order to assign costs correctly to fiscal periods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Internal Commissions screen, choose Create.Select the following Condition Contract Type:0CSA Internal Commission: Billing Document |  |  |
| 4 | Enter Condition Contract Details | On the Create Internal Commission: Billing Document screen, make the following entries and choose Enter:Personnel Number: <prepared PERNR>From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant (Optional) | On the Basic Data tab, enter one of the condition contract process variants which varies the basic scenarios. Then choose Enter:Option A:Process Variant: ZE02 Sales Commission Split Criteria AdaptationOption B:Process Variant: ZE03 Commission Selection Criteria Adaptation |  |  |
| 6 | Enter Sales Data | On the Sales tab, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 7 | Check Data of Responsibility Area | On the Responsibility Area tab, check personnel data the system has derived from the entered personnel number:Company Code: 3310Worker Cost Center: <from personnel data>Controlling Area: A000 |  |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and choose Enter.Field Combination: 0060 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: <entered personnel number>Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer. |  |  |
| 9 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Worker: RegularIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This can happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Continue.Settlement Date: for example, <end of current month>Settlement Date Type: Final SettlementRepeat the entry of a final settlement for each month end in the condition contract’s validity period and for the validity end.If delta accruals settlements are required, select New Line and make entries as follows. Repeat the step for further required delta accruals settlement dates.Settlement Date: for example, <end of current month>Settlement Date Type: Delta Accruals |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS3 Internal CommissionCondition Rate: for example, <1%>Accruals: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Release Condition Contract | Choose Release. |  |  |
| 14 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

##### Check Business Volume (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the business volume for the condition contract.

Prerequisites

Use this step if you have prepared transactional data to create billing documents related to a condition contract for an internal sales representative.

Note

You can repeat this process step at every point in time in the test procedure. It’s recommendable to check the business volume before you start a settlement run to enable a control of the business volume determined for a settlement document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Business Volume - Condition Contracts (WB2R_BUSVOL). | The Business Volume for Condition Contracts screen displays. |  |
| 3 | Select Condition Contract | On the Business Volume for Condition Contracts screen, make the following entries:Condition Contract: <number of condition contract created in the previous step>Business Volume Base: From ContractOutput Level Business Volume: Settlement Date and Split Criteria |  |  |
| 4 | Check Business Volume for Condition Contracts | Choose Execute. | Business volume is determined based on the existing billing documents. |  |

##### Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a delta accruals settlement for the condition contract. With this delta accruals settlement, you post accruals for the billing documents related to the condition contract.

Prerequisites

Use this step if you have executed the Sell from Stock scenario for the condition contract for an internal sales representative.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Sales Commissions (WB2R_SP_ICOM). | The Settle Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Select Condition Contract | On the Settle Condition Contracts - Internal Commissions screen, make the following entries and choose Execute:Settlement Date: for example, <today's date>Settlement Date Type: 3 Delta AccrualsCondition Contract: <number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No Filter | The settlement document for posting delta accruals is created. |  |

##### Check Personnel Settlement Document for Delta Accruals Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the personnel settlement document and accounting document for the delta accruals settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Personnel Settlement Documents (F3808A). | The Manage Personnel Settlement Documents screen displays. |  |
| 3 | Select Documents | Enter suitable selection criteria for personnel settlement documents as for instance the workforce condition contract number for field Condition Contract and choose Go. | Selected documents are displayed in the Personnel Settlement Documents table. |  |
| 4 | Display Document Data | In the Personnel Settlement Documents table, find the settlement document for the delta accruals settlement and click the corresponding line. | The Personnel Settlement Document screen displays. |  |
| 5 | Check FI Posting Status | In the header area, check the posting status for the data transfer to Accounting. | The posting status is Accounting document has been created (C). |  |
| 6 | Check Reference Information | Under General Information > Basic Settlement Data, check the reference information. | Under Reference Information, field Reference contains the number of the settlement document, and field Assignment contains the number of the condition contract. |  |
| 7 | Check Document Items | Under Items, check the items of the personnel settlement document in the Personnel Settlement Document Items table. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Personnel Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RCBV Commision BusVol.The system has calculated the accruals amount according to accruals settings maintained in the condition contract. |  |
| 9 | Check Journal Entry | Go back to the Settlement Document screen.Under Document Flow, choose the main customer journal entries. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 61500100 (Internal Commissions) | <Accruals amount> | 0 |
| 21772100 (Provis. int. Commis.) | 0 | <Accruals amount> |

##### Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a final settlement for the condition contract. In this step, you also reverse the accruals posted before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Settle Sales Commissions (WB2R_SP_ICOM). | The Settle Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Settle Condition Contracts - Internal Commissions screen, make the following entries and choose Execute.Settlement Date: for example, <end of current year date>Settlement Date Type: Final SettlementCondition Contract: <Number of condition contract created in this test>Posting Date: for example, <today's date>Document Date: for example, <today's date>Run Type: Live RunList Range: Message LogSave Application Log: Only in Productive RunMessage Log Filter: No FilterTake a note of the number of the personnel settlement document created. | The Log for Workforce Condition Contract Settlement - Live Run screen displays. A personnel settlement document is created. Accruals are reversed. |  |

##### Check Personnel Settlement Document for Final Settlement

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Personnel Settlement Documents (F3808A). | The Manage Personnel Settlement Documents screen displays. |  |
| 3 | Select Documents | Enter suitable selection criteria for personnel settlement documents as for instance the workforce condition contract number for field Condition Contract and choose Go. | Selected documents are displayed in the Personnel Settlement Documents table. |  |
| 4 | Display Document Data | In the Personnel Settlement Documents table, find the settlement document for the final settlement and click the corresponding line. | The Personnel Settlement Document screen displays. |  |
| 5 | Check FI Posting Status | In the header area, check the posting status for the data transferred to Accounting. | The posting status is Accounting document has been created (C). |  |
| 6 | Check Compensation Reason and Reference Information | Under General Information > Basic Settlement Data , check the compensation reason and reference information. | Under Process Details, field Compensation Reason contains compensation reason Commissions Payment (4930).Under Reference Information, field Reference contains the number of the personnel settlement document, and field Assignment contains the number of the condition contract. |  |
| 7 | Check Document Items | Under Items, check the items of the settlement documents. | The system has created the items according to the split criteria. |  |
| 8 | Check Pricing of Items | Click an item in the table. On the following Personnel Settlement Document Item screen, under Pricing Elements, check the pricing elements of the settlement document item.Repeat this step for all the items. | The system has determined the relevant business volume and displays it for condition type RCBV Commission BusVol. The system has calculated the internal commission amount with condition type RCS3 maintained in the condition contract. The system shows the amount of reversed accruals for condition type RCA2. |  |
| 9 | Check Journal Entries | Under Document Flow, choose Main Journal Entry. Click the icon right to the box and select Display Journal Entries from the pop-up window. | You see the financial posting as below. |  |

Financial Posting

| G/L Account | Debit | Credit |
| --- | --- | --- |
| 21772100 (Provis. int. Commis.) | <Accruals reversal amount> | 0 |
| 21772100 (Provis. int. Commis.) | 0 | <Internal commissions amount> |
| 61500100 (Internal Commissions) | 0 | <Sum of internal commissions amount and accruals reversal amount with consideration of signs> |

|  |
| --- |
| Note The journal entry item for account 61500100 disappears when internal commissions amount and accruals reversal amount have the same value. |

#### Commissions Processing – Billing Document Paid

Purpose

This section outlines two available methods for configuring condition contracts to settle commissions based on paid billing documents:

1. Using Condition Contract Type 0CSC

In this method, both accruals and settlement values are calculated based only on paid (cleared) billing documents.

1. Using Condition Contract Type 0CSA with Process Variant ZE04 (or 0CSE for Subscription Billing)

In this method, you can use condition contract type 0CSA together with process variant ZE04 Commission on Paid Invoices, as described in the section Define Process Variant for Commissions on Paid Invoices.

Accruals are calculated based on all billing documents regardless of whether they are paid (cleared) or open. But the settlement is performed using business volume only from the paid (cleared) billing documents.

Alternatively, condition contract type 0CSE can be used when billing data comes from SAP Subscription Billing.

|  |
| --- |
| Note The application does not differentiate between partially and fully paid billing documents, and always takes the full amount in either case. |

Prerequisite

You have activated condition contract type 0CSE Commission External Subscription Bill as described in chapter Activate Condition Contract Types (Optional).

##### Post Incoming Payments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you post the incoming payments from the customer.

|  |
| --- |
| NoteThis is an optional step and applies to condition contract type 0CSC – Internal Commission: Billing Doc Paid. It also applies when using condition contract type 0CSA with process variant ZE04 – Commission on Paid Invoices, or 0CSE for Subscription Billing.If you are testing Commissions Processing: Billing Document Paid scenario, and accounting document is not cleared, you have to follow the steps below. For other options of making incoming posting to clear account receivables, refer to Accounts Receivable (J59) scope item. |

Prerequisites

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments screen displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code: 3310Posting Date: <date>Journal Entry Date: <date>Value Date: for example, <today's date>Journal Entry Type: DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank Data area.G/L Account: 11001060House Bank/Account ID: AEBK1/AEAC1 or AEBK2/AEAC2Amount: <customer invoice amount>Note If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account: 33100001Choose Propose Items. | The open items display in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment will be applied.In the Items to Be Cleared column,Allocated Amount: enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be appliedChoose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1 to 4. |  |  |
| 10 | Enter Data | Choose Post on account and make the following entries:Account Type: CustomerCustomer: 33100001Credit Amount: same amount as in step 4 |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

##### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a condition contract for an external sales agent as Condition Contract Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Internal Commissions screen, choose Create.Select the following Condition Contract Type:Option A:0CSC Internal Commission: Billing Doc PaidOption B:0CSA Internal Commission: Billing Document or0CSE Internal Commission: Subscription BillNote To use condition contract type 0CSA or 0CSE, select the process variant ZE04 on the Basic Data tab. |  |  |
| 4 | Enter Condition Contract Details | On the Create Internal Commission: Billing Document screen, make the following entries and choose Enter:Personnel Number: <prepared PERNR>From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Sales Data | On the Sales tab, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 6 | Enter Header Text | On the Header Texts tab page, make and check the following entries:Text Type: Text for Settlement DocumentLanguage: EnglishChoose Create Header Text and enter the header text. | The header text will be shown in the corresponding settlement documents.Note Choose German if communication language of business partner is German. If the language English is mentioned then the text will not appear in the output form as in the German business partners the communication language German is maintained. |  |
| 7 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and choose Enter.Field Combination: 0060 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: <entered personnel number>Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer. |  |  |
| 8 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Worker: RegularIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This can happen when you do a settlement before you have created transactional documents.If you have selected the process variant for internal commission on paid invoices in step 3, make the following entry and choose Enter:Business Volume Table Group: 0C02 Internal Commission Only Paid Invoices |  |  |
| 9 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Continue.Settlement Date: for example, <end of current month>Settlement Date Type: Final SettlementRepeat the entry of a final settlement for each month end in the condition contract’s validity period and for the validity end.If delta accruals settlements are required, select New Line and make entries as follows. Repeat the step for further required delta accruals settlement dates.Settlement Date: for example, <end of current month>Settlement Date Type: Delta Accruals |  |  |
| 10 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS3 Internal CommissionCondition Rate: for example, <1%>Accruals: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 11 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 12 | Release Condition Contract (Optional) | Choose Release. |  |  |
| 13 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

##### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps of [Check Business Volume (Optional)](#unique_28) [page ] 50.

##### Delta Accruals Settlement (Optional)

Please follow process steps of chapter [Delta Accruals Settlement (Optional)](#unique_29) [page ] 51.

On the selection screen, enter the different condition contracts belonging to this test. After you have processed the delta accruals settlement, you can optionally check the created settlement documents as described in chapter [Check Personnel Settlement Document for Delta Accruals Settlement (Optional)](#unique_30) [page ] 52.

##### Final Settlement

Please follow steps in [Final Settlement](#unique_31) [page ] 53.

On the selection screen, enter the different condition contracts belonging to this test. After you have processed the final settlement, you can optionally check the created settlement documents as described in chapter [Check Personnel Settlement Document for Final Settlement](#unique_32) [page ] 54.

#### Commissions Processing – Subscription Billing

Purpose

This section deals with a variant for the commission processing that uses billing documents from subscription billing as data source.

For this variant, there is the following special feature. In subscription billing, the commercial or sold products are the relevant business objects for profitability analysis and not the component materials (one-time, recurring, usage). Accordingly, the sold product is mapped to the material in settlement documents so that the material split criterion becomes effective for the sold product. In the business volume selection criteria, you can specify both the sold products as well as the component materials for instance to restrict the commissions to the recurring component only.

This process variant is represented by condition contract type 0CSE Internal Commission: Subscription Bill. The test procedure is very similar to the basic process variant so that we only describe the differences to the basic variant.

Prerequisite

You have activated condition contract type 0CSE Internal Commission: Subscription Bill as described in chapter Activate Condition Contract Type (Optional).

##### Create Condition Contract

Please refer to chapter [Create Condition Contract](#unique_27) [page ] 46 to create a condition contract except for the following differences:

1. Condition Contract Type. Please select condition contract type 0CSE Internal Commission: Subscription Bill.
2. Business Volume Selection Criteria. Choose field combination 0068 Product Sold to specify relevant commercial products used in subscription billing.

|  |
| --- |
| Note Materials attributes such as material group or material price group are not available as business volume selection criteria in this process variant. In billing document items resulting from subscription billing, these attributes refer to the component materials and are therefore not appropriate to specify the relevant commercial products. |

##### Check Settlement Documents

Please refer to chapters [Check Personnel Settlement Document for Delta Accruals Settlement (Optional)](#unique_30) [page ] 52 and [Check Personnel Settlement Document for Final Settlement](#unique_32) [page ] 54 to check settlement documents with the following addition aspect:

In step Check Document Items control that the commercial products from subscription billing appear as products.

#### Commissions Processing with Approval Workflow

##### Create Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a workforce condition contract for an employee as condition contract partner.

In the following steps, we show how to create a 0CSA Internal Commission: Billing Document condition contract with approval process active.

Prerequisite

As prerequisite for this process step, you have completed steps mentioned in preliminary steps for creating a process variant with approval process activated and performed steps for configuring approval workflow in Configure Approval Workflow for Workforce Condition Contracts (Optional).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Select Condition Contract Type | On the Manage Condition Contracts - Internal Commissions screen, choose Create.Select the following Condition Contract Type:0CSA Internal Commission: Billing Document |  |  |
| 4 | Enter Condition Contract Details | On the Create Internal Commission: Billing Document screen, make the following entries and choose Enter:Personnel Number: <prepared PERNR>From: for example, <today's date>To: for example, <end of current year> |  |  |
| 5 | Enter Process Variant | On the Basic Data tab, make the following entry and choose Enter:Process Variant: ZE01 Internal Commission with Workflow |  |  |
| 6 | Enter Sales Data | On the Sales tab, make and check the following entries:Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 7 | Check Data of Responsibility Area | On the Responsibility Area tab, check personnel data the system has derived from the entered personnel number:Company Code: 3310Worker Cost Center: <from personnel data>Controlling Area: A000 |  |  |
| 8 | Enter Business Volume Selection Criteria | On the Business Volume Selection Criteria tab, choose New Line.Make the following entries and choose Enter.Field Combination: (optional) 0009 MaterialInclusion Indicator (Incl/Excl): InclusiveMaterial: TG11Choose New Line.Make the following entries and choose Enter.Field Combination: 0060 Commission RecipientInclusion Indicator (Incl/Excl): InclusiveCommission Recipient: <entered personnel number>Optionally, you can also limit the business volume to certain customers using field combination 0001 Customer. |  |  |
| 9 | Check Settlement Data | On the Settlement Data tab, check the following entry:Settlement Type Worker: RegularIf required, enter a settlement material:Settlement Material: for example, TG11Note The entry of a settlement material is required for the case that no material can be determined from the business volume. This can happen when you do a settlement before you have created transactional documents. |  |  |
| 10 | Enter Settlement Calendar | On the Settlement Calendar tab, select New Line.Make the following entries and choose Continue.Settlement Date: for example, <end of current month>Settlement Date Type: Final SettlementRepeat the entry of a final settlement for each month end in the condition contract’s validity period and for the validity end.If delta accruals settlements are required, select New Line and make entries as follows. Repeat the step for further required delta accruals settlement dates.Settlement Date: for example, <end of current month>Settlement Date Type: Delta Accruals |  |  |
| 11 | Enter Condition Data | In the Conditions area, select New Condition:Make the following entries and choose Enter.Condition Type: RCS3 Internal CommissionCondition Rate: for example, <1%>Accruals: for example, <2%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Scale Base Type: Value scaleNote In case the Valid From date and the Valid To date are already there, you can check and change it. |  |  |
| 12 | Enter Scale Data | Select the condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <1000>Unit: AEDCondition Rate: for example, <1%>Select the first created condition line.Choose New Scale Level.Make the following entries and choose Enter.Scales: for example, <2000>Unit: AEDCondition Rate: for example, <2%> |  |  |
| 13 | Save Condition Contract | Choose Save.Make a note of the condition contract number:Document xxxxxxxxxx was saved. |  |  |

##### Request Approval to Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request an approval for releasing a commission condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Request Release of Condition Contract | In the Condition Contracts table, choose the line with the condition contract for which you want to request an approval for release.Choose Change Condition Contract after clicking on condition contract number.Choose Menu > Edit > Request Approval .Choose Save. | The status for the condition contract now should be:NewApproval RequestedThe condition contract with the request for release approval goes to Sales Manager's Inbox. |  |

##### Trigger Rework of Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the status of a commission condition contract and trigger a rework of the condition contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Display the Relevant Condition Contract | Find the condition contract for which Contract Manager – Commissions has just requested the approval for release: Release Condition Contract XXXXXXXXXXX. | The details of the condition contract display on the right of the screen. |  |
| 4 | Check Condition Contract Data and Send Back for Rework | Check the Settlement Lock Status and Status of the condition contract.Now the settlement lock status is Not Locked and the status is New.As the Contract Manager – Commissions has not set the status to be Locked for Settlement, choose Rework.On the Submit Decision pop-up window, enter a decision note, for example, please set the condition contract to Locked for Settlement.Choose Submit. | The condition contract is sent back to Contract Manager – Commissions. |  |

##### Rework Condition Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you rework a commission condition contract in order to set the Lock for Settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Check the Notification and Go to Change Mode | Open the notification: Rework Condition Contract XXXXXXXXXXX.Choose Show Details at the bottom and check the comments on the right side of the screen. Under the Comments tab, there is a message from the Sales Manager: please set the condition contract to Locked for Settlement.Choose Hide Details at the bottom and choose More Details on the upper right of the screen.On the Display Internal Commission: Billing Document screen, choose Menu > Condition Contract > Change . | You check the comment from the Sales Manager and go to the change mode for condition contract. |  |
| 4 | Set Condition Contract to Locked for Settlement Status | On the Change Internal Commission: Billing Document screen, choose Menu > Edit > Lock Settlement .Choose Save.Choose Continue in the dialog box. | The settlement lock status is changed to Locked and the status for condition contract is New. |  |
| 5 | Complete Rework for the Condition Contract | Choose Rework Completed at the bottom.On the Submit Decision pop-up window, enter a decision note: for example, the condition contract is set to Locked for Settlement.Choose Submit. | The condition contract is sent to Sales Manager for release approval again. |  |

##### Release Condition Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a commission in an approval workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract | Find the condition contract for which Contract Manager – Commissions has just requested an approval for release: Release Condition Contract XXXXXXXXXXX.Choose Release at the bottom.Choose Submit in the dialog box. | The condition contract is released now. |  |

##### Check Business Volume (Optional)

As described for the basic processing variant, also check the business volume in this test procedure before you start a settlement run to enable a control of the business volume determined for a settlement document.

Please follow process steps of [Check Business Volume (Optional)](#unique_28) [page ] 50.

##### Delta Accruals Settlement (Optional)

Please follow steps in [Delta Accruals Settlement (Optional)](#unique_29) [page ] 51.

##### Request Release of Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a commission condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Send Condition Contract for Release of Settlement | Find the condition contract for which you want to request the approval to release it for settlement. Choose Change Condition Contract via More Links when choosing condition contract number.Choose Menu > Edit > Request Settlement Approval .Choose Save.Choose Continue in the dialog box.Note Please choose Menu > Edit > Lock Settlement before clicking Request Settlement Approval if you haven't executed steps in chapter [Rework Condition Contract (Optional)](#unique_45) [page ] 69. | The status for the condition contract now should be:ReleasedLocked for SettlementSettlement Approval RequestedNow the request to release condition contract goes to Sales Manager's Inbox. |  |

##### Release Condition Contract for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you release a rebate condition contract for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Release Condition Contract for Settlement | Find the condition contract for which Settlement Clerk – Commissions has just requested an approval for release.Position the notification: Release Condition Contract for settlement XXXXXXXXXXX in the inbox.Choose Release.Choose Submit in the dialog box. | The condition contract is released now for settlement. |  |

##### Final Settlement

Please follow process steps of chapter [Final Settlement](#unique_31) [page ] 53.

On the selection screen, enter the different condition contracts belonging to this test.

|  |
| --- |
| Note Since the workflow is activated, in this step, you will see the following messages including: |

Contract XXXXXXXXXXX locked after final settlement

Document XXXXXXXXXXX with document status Workflow Release Required is blocked for follow-on documents

Document XXXXXXXXXXX saved (no accounting document generated)

Document XXXXXXXXXXX is processed with reference XXXXXXXXXXX

##### Approve Release of Final Settlement Document to Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you approve the release of the final settlement document to Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Approve Release to Accounting | Find the settlement document for which the release to accounting has to be approved. The approval was triggered automatically after the settlement has been processed by the Settlement Clerk – Commissions.Position the notification: Approve Settlement XXXXXXXXXXX in the inbox.Choose Approve.Choose Submit in the dialog box. | The settlement document is released to accounting. |  |

#### Commissions Processing with Graduated Scales

The default calculation of the scales that are set up in the condition table in condition contracts works like volume pricing. This means that on the execution of settlements, the application would apply the rate of the tier that it finds when looking for the business volume, on the entire amount and not only the delta amount:

If you set up the conditions as for example:

| Business Volume | Commission Percentage |
| --- | --- |
| (From) 1,000 EUR | 10% |
| (From) 6,000 EUR | 20% |
| (From) 10,000 EUR | 30% |

Then the settlement run would calculate the commissions as follows:

| Business Volume found at the time of settlement | Total Effective Commission at the time of settlement |
| --- | --- |
| 999 EUR | 0 EUR |
| 6,000 EUR | 1,200 EUR |
| 11,000 EUR | 3,300 EUR |

However, if you would like to set up graduated scales that work like tiered pricing instead of volume pricing, then you need to set up the condition contract slightly differently.

Follow the steps as in the chapter [Create Condition Contract](#unique_27) [page ] 46. In step 9, choose the value of the field Settlement Calculation Method as Graduated-To-Scale. Then in step 12, maintain the scales with scale type as To-scale.

Thereafter, if you set up the conditions as for example:

| Business Volume | Commission Percentage |
| --- | --- |
| (To-scale) 1,000 EUR | 0% |
| (To-scale) 5,000 EUR | 10% |
| (To-scale) 11,000 EUR | 20% |
| (To-scale) 999,999 EUR | 30% |

Then the settlement run would calculate the commissions as follows:

| Business Volume found at the time of settlement | Total Effective Commission at the time of settlement |
| --- | --- |
| 1,000 EUR | 0 EUR |
| 5,000 EUR | 400 EUR |
| 11,000 EUR | 1,600 EUR (= 400 EUR +1,200 EUR) |

In the example above, the calculation works in the following manner.

When business volume is found to be 1,000 EUR, then the first tier with 0% commission is applicable. Hence, the commission is 0 EUR.

When business volume is found to be 5,000 EUR, then the second condition rate with 10% commission is applicable on the difference of business volumes between the first and second scales. Hence, the commission is calculated as 400 EUR.

When business volume is found to be 11,000 EUR, then three condition rates would be applicable. This means that the commission would be calculated at the rate of 0% for 1,000 EUR, 10% for 4,000 EUR and 20% for the remaining 6,000 EUR, resulting in 0, 400 and 1,200 EUR, respectively. Hence, the total commission value comes to 1,600 EUR.

#### Commissions Processing Using Service Rendered Date for Business Volume Selection

In the standard scenario, the system uses the billing date to determine the business volume and the corresponding rates for settlement. However, there are some business scenarios where the business volume impacted by subsequent debit or credit memos (for example, price corrections or customer returns) needs to be considered for the same period as the original sales. One example of such a scenario is when rates vary across multiple periods within a condition contract’s validity duration. To handle these scenarios, you can use the service rendered date for business volume selection instead of the standard billing date, provided that the service rendered date of the subsequent billing document is the same as the service rendered date of the original billing document. This ensures that subsequent billing documents are processed using the rate from the original transaction period.

Example

Consider an agreement with different monthly rates. If you use the billing date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 15% | -$ 7.5 |

The business volume for the return is considered at 15%, which is higher than the 10% rate granted in January prior to the return.

If you use the service rendered date:

| Transaction | Period | Amount | Rate | Calculation | Settlement Amount |
| --- | --- | --- | --- | --- | --- |
| Sale | January | $ 100 | 10% | $ 100 * 10% | $ 10 |
| Return | March | -$ 50 | 15% | -$ 50 * 10% (January) | -$ 5 |

The business volume for the return is considered at the January rate of 10%, reflecting the rate originally granted.

This functionality is supported only for billing document–based calculations and applies to the following condition contract type:

- 0CSA – Internal Commission: Billing Document

To enable this feature, follow the steps described in the chapter [Create Condition Contract](#unique_27) [page ] 46 with the following differences:

- In step 5, choose Process Variant ZE05 as explained in chapter [Define Process Variant to Activate Business Volume Selection by Service Rendered Date](#unique_15) [page ] 22.
- In step 11, select condition type RCS4.

|  |
| --- |
| Caution In case of returns, the service rendered date can differ based on the type of return. For further details about how the service rendered date is filled, consult your Sales and Distribution experts. |

|  |
| --- |
| Note If you have different rates for different periods, then you need to create the settlement calendar with Final Settlement dates for each period for those rates to be correctly applied. Using the service rendered date for business volume selection can cause subsequent billing documents posted after a contract's final settlement to be excluded from settlement. For example, if the original billing document is created in December, final settlement runs in January, and a subsequent billing document is posted in February with a service rendered date in December, the subsequent billing document may not be considered in the final settlement because the contract has already been settled. To capture such late billing documents, you can use delta settlements in subsequent settlement runs. |

#### Final Settlement with Adjustments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter conditions in the condition contract to adjust the final commission amount before you process the final settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contract Manager - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Condition Contracts - Internal Commissions (F7263). | The Manage Condition Contracts - Internal Commissions screen displays. |  |
| 3 | Change Condition Contract | On the Manage Condition Contracts - Internal Commissions screen, select the relevant condition contract and choose More Links.Choose Change Condition Contract from More Links. |  |  |
| 4 | Enter Condition Data for Internal Commissions Condition | In the Conditions area, select the following entry:Condition Table: Condition ContractSelect New Condition.Make one of the following entries and choose Enter.Adjustment of business volume:Cond. Type: RCBE Commission BV DeltaValid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Condition Rate: for example, <100> AEDAdjustment of commission amount:Cond. Type: RCJ3 Commission AdjustmentValid From: for example, <today's date>Valid To: for example, <end of current year>Condition Rate: for example, <20> AEDEntry of a fixed settlement amount:Cond. Type: RCV3 Commission VerifiedValid From: for example, <today's date>Valid To: for example, <validity end of condition contract>Condition Rate: for example, <1000> AEDNote The conditions entered here are used to adjust the commission amount. You can also choose Condition Contract / Material as condition level. You then also specify the material for a condition record. In case the Valid From and Valid To date are copied from the condition contract validity according to user settings, you can check and change these dates if necessary. |  |  |
| 5 | Save Condition Contract | Choose Save. |  |  |

After you have maintained the conditions to adjust the commission amount, you perform the final settlement steps as described in chapter Final Settlement. Then check the created settlement document as described in chapter Check Personnel Settlement Document for Final Settlement. In the pricing elements, particularly check that the system has determined the commission amount using the conditions for adjustment.

#### Commission Unlikelihood (Optional)

Purpose

During the creation of the condition contract (see chapter Create Condition Contract) when entering the conditions, you have the option to use the condition: commission unlikelihood. You use condition type commission unlikelihood in case the minimum sales turnover will not be reached and therefore no accruals should be created or existing accruals should be reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Condition Data (Optional) | In the Conditions area, select New Condition.Make the following entries and choose Enter.Condition Type: RCU3 Commission UnlikelihoodCondition Rate: <100%>Valid From: for example, <today's date>Valid To: for example, <validity end of condition contract> |  |  |

### Commissions Processing with Integration to SAP SuccessFactors Incentive Management

#### Schedule Import of Commission Data from SAP SuccessFactors Incentive Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Extract commissions related data from SAP SuccessFactors Incentive Management system to S/4HANA system. Personnel Settlement Documents are created in the background. The documents are not released to FI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Commission Data Import - Personnel Settlement (F3998). | The Application Job screen displays. |  |
| 3 | Create a New Job | Choose Create. | The Create Personnel Settlement Documents from External Service screen displays. |  |
| 4 | Enter Job Data | Enter the following entries and choose Schedule.Personnel Number: <50023040>Check Run Only: <deselect>Reference Settlement Date: <mm/dd/yyyy>Document Date: <mm/dd/yyyy> | The Application Jobs screen displays where you can check the status of the job you have scheduled. |  |

#### Check Personnel Settlement Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales manager can check the posting status and other details before releasing the document to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Personnel Settlement Documents (F3808A). | The Manage Personnel Settlement Documents screen displays. |  |
| 3 | Enter Data | Enter the following filter value, and choose Go:Personnel Number: <50023040> | The personnel settlement documents are listed. |  |
| 4 | Check Personnel Settlement Document | Select the corresponding line. Write down document date, employee and commission amount and FI document number (journal entry). |  |  |

#### Approve Release of Personnel Settlement Documents to Accounting via Workflow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In case you have activated the workflow functionality for the approval of the release of personnel settlement documents to accounting, the Sales Manager will receive a notification and needs to check the Inbox and approve or reject the request for the release of the personnel settlement document to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | The My Inbox screen displays. |  |
| 3 | Approve Personnel Settlement Document | Verify the inbox contains an item for Personnel Settlement Document Release approval for the document.Choose the item.Choose Approve. |  |  |
| 4 | Check Personnel Settlement Document Status | Go back to Check Personnel Settlement Documents chapter.Check the status on the Personnel Settlement Document. |  |  |

#### Release Personnel Settlement Documents to Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales manager releases the personnel settlement documents to Accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Settlement Clerk - Commissions. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Release Documents - Personnel Settlement (WPSDOC_RELEASE). |  |  |
| 3 | Release Personnel Documents | Enter the following entries:Personnel Number: <Personnel Number>Document Date: <Document Date>Check Run Only: <deselect>Choose Execute. | Check status of personnel settlement documents. |  |

#### Check Postings to FI Accounts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check postings to FI accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Check FI Accounts | Search for the Accounting Document number you created before.Choose the Accounting Document number you created before.Choose Display Journal Entries. | The postings should be as follows:61500100 (Internal Commissions)21772100 (Provis. int. Commis) |  |

## Follow-Up Processes

You have finished all the activities that are part of the business process described in this document.

To accomplish the subsequent activities of this business process, use the master data from this document and carry out the process steps described in one or more of the following scope items.

### Check Processing of Commissions in SuccessFactors (Optional)

Optionally, you can check the processing of commissions data in SuccessFactors, including data transfers, execution of the payroll run, and FI postings. Configured well, the processing of commissions in SuccessFactors does not require additional manual intervention. In the following, we outline the processing steps and show you how to manage these steps within the different modules of SuccessFactors. For more information about data processing in SuccessFactors Employee Central, see [Employee Central Best Practices](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/98e1ecaba5ad46948e133cf095e1c77a/0127f054e5a64677b517b14264adf0b0.html), and for more information about data processing in SuccessFactors Employee Central Payroll, see [The Payroll Process](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3f7761ea74cf4ee9864b8ab713636fe5/6b6ec2531bb9b44ce10000000a174cb4.html).

The processing of commissions data comprises the following major steps:

- Import of commissions data into SuccessFactors Employee Central

You schedule a background job that periodically imports commissions data from new personnel settlement documents created since the last import run.

- Replication of commissions data from SuccessFactors Employee Central to SuccessFactors Employee Central Payroll

The replication of commissions data is part of the usual replication background job.

- Execution of the payroll run

Usually, after several checks, you run a report periodically (commonly monthly) to create the payroll statement for your employees. You can also schedule a background job.

- Transfer of payroll data to accounting

You execute a report to create postings for payroll runs in accounting.

|  |
| --- |
| Note To check the processing of commissions data in SuccessFactors Employee Central and SuccessFactors as described below, you must log on with a user having the necessary authorization for HR administration.When you observe issues for data processing in SuccessFactors Employee Central, create a ticket for an appropriate component with prefix LOD-SF-EC. For issues related to SuccessFactors Employee Central, choose an appropriate component with prefix PY for payroll process. |

#### Check Data Import to SuccessFactors Employee Central

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the import of commissions data to SuccessFactors Employee Central for relevant employees.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central. | The Home screen displays. |  |
| 2 | Open Employee File | Enter the employee number in the Search field and choose Enter. | The employee file displays. |  |
| 3 | Display Commissions Data | Under Employee Information, choose Pay Component Non Recurring. | The system displays the imported one time payments. |  |
| 4 | Check Data | Check the completeness of one time payments and their amounts. | The system displays all imported commissions data. |  |

#### Check Data Replication to SuccessFactors Employee Central Payroll

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you check the replication of commissions data from SuccessFactors Employee Central to SuccessFactors Employee Central Payroll for relevant employees.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central Payroll. | The SAP Easy Access screen displays. |  |
| 2 | Access the Application | Choose Human Resources > Personnel Management > Administration > HR Master Data > Display or call transaction PA20 Display HR Master Data. | The Display HR Master Data screen displays. |  |
| 3 | Display Employee Data | Enter the personnel number in the Personnel No field and 0015 Additional Payments in the Infotype field. Choose Overview from the toolbar. | The Overview Additional Payments screen displays with additional payments in the table. |  |
| 4 | Check Data | Check the completeness of additional payments and their amounts. | The system displays all additional payments. |  |

#### Check Results of the Payroll Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you control the payroll statement for relevant employees created in previous payroll runs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central Payroll. | The SAP Easy Access screen displays. |  |
| 2 | Access the Application | Choose Human Resources > Payroll > Europe > Germany > Tools > Display Results or call transaction PC_PAYRESULT Display Payroll Results. | The Display payroll results screen displays. |  |
| 3 | Display Payroll Results for Employees | Enter the personnel number of a relevant employee in the Personnel number field.Optionally, use the Multiple selection function to enter further personnel numbers.Choose Enter. | Selected personnel numbers appear in the Personnel numbers selected list.Payroll results of a selected personnel number appear in the Payroll Results <Employee> list. |  |
| 4 | Display Details | Double-click an entry in the payroll results list.On the following list, double-click the line with name RT_ Results Table (Collapsed Display). | The Tables / field strings of payroll result screen displays. |  |
| 5 | Check Commissions Data | In the payroll results, search for entries with your wage types for commissions and check the corresponding amounts. | The payroll list contains commissions data as imported before. |  |

#### Check Financial Postings for Payroll Run

Purpose

In this process step, you control the FI postings for relevant payroll runs created before.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SuccessFactors Employee Central Payroll. | The SAP Easy Access screen displays. |  |
| 2 | Access the Application | Choose Human Resources > Payroll > Europe > Germany > Subsequent Activities > Per payroll period > Reporting > Posting to Accounting > Edit Posting Run or call transaction PCP0 Edit posting runs. | The Display posting runs screen displays. |  |
| 3 | Select Payroll Posting | In the PP Payroll posting section, double-click the relevant payroll posting. | The Posting to Accounting: Document overview screen displays. |  |
| 4 | Display Accounting Document | Double-click the line with the payroll posting again. | The Display Payroll Posting Document screen appears. |  |
| 5 | Check Posting | Check the posting of internal commissions. | The clearing account posted in the settlement run is balanced. |  |

### General Ledger Reporting and Cost Center Reporting (Optional)

Purpose

After completing the activities in this test script, it is possible to run General Ledger Reporting and Cost Center Reporting connected with the accounts which were used in this sales commission process. Log on as General Ledger Accountant or Sales Accountant and run the reports which apply to your needs and check the postings on your accounts. Please refer to Accounting and Financial Close (J58) to Manage G/L Account Master Data and Manage Financial Statement Versions.

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
> Flagged while digesting this document, not verified: Prepare Transactional Data is headed (Optional) but its text says 'Preparing transactional data is a required step'.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script]]
- related-to :: [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu]]
- related-to :: [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed]]
- related-to :: [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 158,561 chars in the whole document
