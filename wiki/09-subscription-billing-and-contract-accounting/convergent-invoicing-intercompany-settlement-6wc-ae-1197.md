---
id: 09-subscription-billing-and-contract-accounting/convergent-invoicing-intercompany-settlement-6wc-ae-1197
title: Convergent Invoicing – Intercompany Settlement (6WC_AE) (6WC_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud Public Edition test script (scope item 6WC_AE): configure and test Convergent Invoicing intercompany settlement, from billable items to payment."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/revenue-sharing-and-partner-settlement]
aliases: [6WC_S4CLD2608_BPD_EN_AE]
keywords: ["Revenue Sharing, Partner and Intercompany Settlement", intercompany settlement, convergent invoicing, intercompany settlement configuration, billable items, billing process, invoicing process, amount calculation key, company code groups, main and subtransactions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WC_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1197
topic: 09-subscription-billing-and-contract-accounting/revenue-sharing-and-partner-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Convergent Invoicing – Intercompany Settlement (6WC_AE) (6WC_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WC_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Revenue Sharing, Partner and Intercompany Settlement** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Convergent Invoicing – Intercompany Settlement (6WC_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Convergent Invoicing – Intercompany Settlement (6WC_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860188)

[2 Prerequisites 4](#_Toc232860189)

[2.1 Additional Manual Configuration 4](#_Toc232860190)

[2.2 System Access 4](#_Toc232860191)

[2.3 Roles 4](#_Toc232860192)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232860193)

[2.5 Business Conditions 6](#_Toc232860194)

[2.6 Preliminary Steps 6](#_Toc232860195)

[2.6.1 Assign Company Code to Company Code Group 6](#_Toc232860196)

[2.6.2 Contract Accounting - Master Data and Basic Functions (2AR) 8](#_Toc232860197)

[2.6.3 Maintain Amount Calculation Key 8](#_Toc232860198)

[2.6.4 Assign Subtype to Intercompany Settlement Type 10](#_Toc232860199)

[2.6.5 Activate Intercompany Settlement 12](#_Toc232860200)

[2.6.6 Master Data Determination for Intercompany Settlement 13](#_Toc232860201)

[2.6.7 Define Main- and Subtransactions for Company Code to Be Invoiced 15](#_Toc232860202)

[2.6.8 Define Main- and Subtransactions for Offsetting Entries 17](#_Toc232860203)

[2.6.9 Define Account Assignment of General Ledger Items 19](#_Toc232860204)

[2.6.10 Define Account Assignment for Business Partner Items 21](#_Toc232860205)

[3 Overview Table 24](#_Toc232860206)

[4 Test Procedures 26](#_Toc232860207)

[4.1 Create Billable Items of Customer 26](#_Toc232860208)

[4.1.1 Option 1: Upload Billable Items 26](#_Toc232860209)

[4.1.2 Option 2: Invoke Create Billable Items SOAP API 28](#_Toc232860210)

[4.2 Perform Billing Process of Customer 28](#_Toc232860211)

[4.2.1 Option 1: Perform Billing Process (Mass Run) 28](#_Toc232860212)

[4.2.2 Option 2: Perform Billing Process (Individual Run) 30](#_Toc232860213)

[4.3 Perform Invoicing Process of Customer 31](#_Toc232860214)

[4.3.1 Option 1: Perform Invoicing Process (Mass Run) 31](#_Toc232860215)

[4.3.2 Option 2: Perform Invoicing Process (Individual Run) 33](#_Toc232860216)

[4.4 Perform Intercompany Settlement 34](#_Toc232860217)

[4.4.1 Display Billable Item for Intercompany Settlement (Optional) 34](#_Toc232860218)

[4.4.2 Perform Billing Process for Intercompany Settlement 35](#_Toc232860219)

[4.4.2.1 Option 1: Perform Billing Process for Intercompany Settlement (Mass Run) 35](#_Toc232860220)

[4.4.2.2 Option 2: Perform Billing Process for Intercompany Settlement (Individual Run) 36](#_Toc232860221)

[4.4.3 Perform Invoicing Process for Intercompany Settlement 37](#_Toc232860222)

[4.4.3.1 Option 1: Perform Invoicing Process for Intercompany Settlement (Mass Run) 37](#_Toc232860223)

[4.4.3.2 Option 2: Perform Invoicing Process for Intercompany Settlement (Individual Run) 39](#_Toc232860224)

[4.4.4 Perform Payment Lot for Intercompany Settlement 40](#_Toc232860225)

[4.4.5 Perform Payment Run for Intercompany Settlement Offsetting 40](#_Toc232860226)

[4.5 Reverse Billable Item of Customer (Optional) 41](#_Toc232860227)

[5 Appendix 43](#_Toc232860228)

[5.1 Process Integration 43](#_Toc232860229)

[5.1.1 Preceding Processes 43](#_Toc232860230)

[5.2 CSV Template Creation 43](#_Toc232860231)

[5.2.1 Sample Data for Intercompany Settlement 43](#_Toc232860232)

## Purpose

Overview

This process enables cross-company-code business between two companies that belong to the same corporate group. It allows the creation of an intercompany invoice for subscription and usage services.

Based on billing data received from an external source, the system determines if an intercompany settlement needs to take place, calculates the respective charges, and triggers the intercompany invoice and the postings in the supplying and receiving company code.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/53b660d37fb15d9cd8775dd348cfc6d2)

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
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company code | 3310 | Requesting Company |  |
| Company code | 3330 | Supplying Company |  |

### Business Conditions

Before this scope item can be tested, the following business condition must be met:

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Business Partner and Contract Account must be created. |
| 2BI - Contract Accounting – Customer Initiated Payments | Must be deployed before running this test script. |

### Preliminary Steps

#### Assign Company Code to Company Code Group

Use

In this step, you assign the supplying company code to the same company code group of requesting company so that the supplying company code and requesting company code are in the same company code group.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Company Codes to Company Code Groups | On the Configure Your Solution: Realize Phase screen, search Assign Company Codes to Company Code Groups, then choose Enter.Select the line of the item of Configure your company codes and go to the next screen.On the Configuration Your Solution “ Organization screen, choose Configure on the line of configuration step with name Assign Company Codes to Company Code Groups. |  |  |
| 5 | Assign supplying Company Code to Company Code Group | On Assign Company Codes to Company Group screen, choose New Entries and make the entries as below:Company Code Group: <the company code group of requesting company code> eg: 3310Company Code: <the supplying company code > eg: 3330Chose Save. | Your requesting company code and supplying company code has been in the same company code group.In this test script, the requesting company code 3310 and supplying company code 3330 are assigned to company code group 3310. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Company Codes to Company Code Groups | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Assign Company Codes to Company Code Groups. |  |  |
| 3 | Assign supplying Company Code to Company Code Group | On Assign Company Codes to Company Group screen, choose New Entries and make the entries as below:Company Code Group: <the company code group of requesting company code> eg: 3310Company Code: <the supplying company code > eg: 3330Chose Save. | Your requesting company code and supplying company code has been in the same company code group.In this test script, the requesting company code 3310 and supplying company code 3330 are assigned to company code group 3310. |  |

#### Contract Accounting - Master Data and Basic Functions (2AR)

Context

This scope item descripts the steps on how to create business partner, contract account, provider contract for Contract Accounts Receivable and Payable (FI-CA). Furthermore, you can create and print correspondence.

Procedure

Complete all the activities descripted in Contract Accounting – Master Data and Basic Functions (2AR) to create master data for Business Partner and Contract Account as below:

Customer of the Requesting Company (eg: company code 3310, company code group 3310):

- Business Partner
- Contract Account

Service Requester of the Requesting Company (eg: company code 3310, company code group 3310):

- Business Partner
- Contract Account

Service Supplier of the Supplying Company (eg: company code 3330, company code group 3310):

- Business Partner
- Contract Account

|  |
| --- |
| Note Please maintain the bank details at Business Partner – Payment Transaction for Service Supplier.Please maintain Outgoing Payment Method eg: T at Contract Account – Payment / Taxes for Service Supplier. |

#### Maintain Amount Calculation Key

Use

In this step, you enhance the amount calculation key of SICO1.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration.. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Calculation Key | On the Configure Your Solution: Realize Phase screen, search Maintain Amount Calculation Key, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution "Intercompany Settlement" screen, choose Configure on the line of configuration step with name Maintain Amount Calculation Key. |  |  |
| 5 | Make Parameters to maintain calculation key | On the Maintain Amount Calculation Key": Change screen, choose the line with the calculation key SICO1, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today's date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message Entries are not added individually to the change request.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit : <Lower Limit for Base Amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 10.Choose Save. | The calculation key SICO1 is enhanced.Note The amount of cost will be determined as: Based on the given example, the amount of cost = Customer Amount * Percentage. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Amount Calculation Key | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Maintain Amount Calculation Key. |  |  |
| 3 | Make Parameters to maintain calculation key | On the Maintain Amount Calculation Key": Change screen, choose the line with the calculation key SICO1, and then choose Validity.Choose New Entries and make the entries as below:Crcy: <your currency>Valid From: <today's date>Choose Save to save the validity.Choose the newly added validity and choose Calculation Rules.Confirm the information dialog with message Entries are not added individually to the change request.Choose New Entries, on the New Entries: Details of Added Entries screen, make the entries as below:Base Amt Limit: <Lower Limit for Base Amount>, for example, 0.Debit/Credit: <Debit or Credit> for example, Debit.Percentage: <your percentage>, for example, 10.Choose Save. | The calculation key SICO1 is enhanced.Note The amount of cost will be determined as: Based on the given example, the amount of cost = Customer Amount * Percentage. |  |

#### Assign Subtype to Intercompany Settlement Type

Use

In this step, you assign the Subtype of SUB1to Intercompany Type of SIC1.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Intercompany Settlement Types | On the Configure Your Solution: Realize Phase screen, search Define Intercompany Settlement Types, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution "Intercompany Settlement" screen, choose Configure on the line of configuration step with name Define Intercompany Settlement Types. |  |  |
| 5 | Assign Subtype to Intercompany Settlement Type | On the Define Intercompany Settlement Type screen, choose Intercompany settlement type of SIC1 and assign the value to Subtype as blow:Subtype: SUB1Choose Save. | The Subtype of SUB1 has been assigned to Intercompany Settlement Type of SIC1. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Intercompany Settlement Types | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Intercompany Settlement Types. |  |  |
| 3 | Assign Subtype to Intercompany Settlement Type | On the Define Intercompany Settlement Type screen, choose Intercompany settlement type of SIC1 and assign the value to Subtype as blow:Subtype: SUB1Choose Save. | The Subtype of SUB1 has been assigned to Intercompany Settlement Type of SIC1. |  |

#### Activate Intercompany Settlement

Use

In this step, you activate the intercompany settlement of SIC1.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Activate Intercompany Settlement | On the Configure Your Solution: Realize Phase screen, search Activate Intercompany Settlement, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution “ Intercompany Settlement screen, choose Configure on the line of configuration step with name Activate Intercompany Settlement. |  |  |
| 5 | Activate Intercompany Settlement | On the Activate Intercompany Settlement: Change screen, choose New Entries and make the entries as below:RepCCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg:3330Valid From: <the Valid from Date> eg: today's dateIntSettlmntType: <the Intercompany Settlement Type> eg: SIC1.Choose Save. | You have activated the Intercompany Settlement of SIC1. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Activate Intercompany Settlement | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Activate Intercompany Settlement. |  |  |
| 3 | Activate Intercompany Settlement | On the Activate Intercompany Settlement: Change screen, choose New Entries and make the entries as below:RepCCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Valid From: <the Valid from Date> eg: today's dateIntSettlmntType: <the Intercompany Settlement Type> eg: SIC1.Choose Save. | You have activated the Intercompany Settlement of SIC1. |  |

#### Master Data Determination for Intercompany Settlement

Use

In this step, you maintain the Master Data for Intercompany Settlement.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Master Data Determination for Intercompany Settlement | On the Configure Your Solution: Realize Phase screen, search Master Data Determination for Intercompany Settlement, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution “ Intercompany Settlement screen, choose Configure on the line of configuration step with name Master Data Determination for Intercompany Settlement. |  |  |
| 5 | Maintain Master Data for Intercompany Settlement | On the Master Data Determination for Intercompany Settlement screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1.Requesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Choose Continue and make the entries as below:Req. Bus. Partner: <the Business Partner of Requesting Company> eg: the Business Partner of the Service RequesterReq. ContractAccount: <the Contract Account of Requesting Company> eg: the Contract Account of the Service Requester.Supp. Bus. Partner: <the Business Partner of Supplying Company> eg: the Business Partner of the Service Supplier.Supp. ContractAccount: <the Contract Account of the Supplying Company> eg: the Contract Account of the Service Supplier.Choose Save. | In the previous step, you have created the business partner and contract account for Service Requester and Service Supplier.Service Requester of the Requesting Company:Business PartnerContract AccountService Supplier of the supplying Company:Business PartnerContract AccountAt this step, you have maintained them accordingly for Master Data Determination of Intercompany Settlement. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Master Data Determination for Intercompany Settlement | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Master Data Determination for Intercompany Settlement. |  |  |
| 3 | Maintain Master Data for Intercompany Settlement | On the Master Data Determination for Intercompany Settlement screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1.Requesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Choose Continue and make the entries as below:Req. Bus. Partner: <the Business Partner of Requesting Company> eg: the Business Partner of the Service RequesterReq. ContractAccount: <the Contract Account of Requesting Company> eg: the Contract Account of the Service Requester.Supp. Bus. Partner: <the Business Partner of Supplying Company> eg: the Business Partner of the Service Supplier.Supp. ContractAccount: <the Contract Account of the Supplying Company> eg: the Contract Account of the Service Supplier.Choose Save. | In the previous step, you have created the business partner and contract account for Service Requester and Service Supplier.Service Requester of the Requesting Company:Business PartnerContract AccountService Supplier of the supplying Company:Business PartnerContract AccountAt this step, you have maintained them accordingly for Master Data Determination of Intercompany Settlement. |  |

#### Define Main- and Subtransactions for Company Code to Be Invoiced

Use

In this step, you maintain the Derivation of the Main Transaction and Subtransaction (Debit and Credit) of the Billable Items of the Intercompany Settlement.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Main- and Subtransactions for Company Code to Be Invoiced | On the Configure Your Solution: Realize Phase screen, search Define Main- and Subtransactions for Company Code to Be Invoiced, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution “ Intercompany Settlement screen, choose Configure on the line of configuration step with name Define Main- and Subtransactions for Company Code to Be Invoiced. |  |  |
| 5 | Define the Derivation of the Main Transaction and Subtransaction (Debit and Credit) of the Billable Items of the Intercompany Settlement. | On Trans. Determination for Clearing Within a Corporate Group screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1.Billable Item Type: <the Billable Item Type> eg: SICRRequesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Choose Continue and make the entries as below:Debit Main Trans.:<the Debit Main Transaction> eg: Y600Debit Subtransaction: <the Debit Subtransaction> eg: 0020Credit Main Trans.: <the Credit Main Transaction> eg: Y600Credit Subtransact.: <the Credit Subtransaction> eg: 0010Tax Determination: <the Tax Determination> eg: Y1Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Main- and Subtransactions for Company Code to Be Invoiced | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Main- and Subtransactions for Company Code to Be Invoiced. |  |  |
| 3 | Define the Derivation of the Main Transaction and Subtransaction (Debit and Credit) of the Billable Items of the Intercompany Settlement. | On Trans. Determination for Clearing Within a Corporate Group screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1.Billable Item Type: <the Billable Item Type> eg: SICRRequesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Choose Continue and make the entries as below:Debit Main Trans.:<the Debit Main Transaction> eg: Y600Debit Subtransaction: <the Debit Subtransaction> eg: 0020Credit Main Trans.: <the Credit Main Transaction> eg: Y600Credit Subtransact.: <the Credit Subtransaction> eg: 0010Tax Determination: <the Tax Determination> eg: Y1Choose Save. |  |  |

#### Define Main- and Subtransactions for Offsetting Entries

Use

In this step, you maintain the derivation of the main transaction and subtransaction (debit and credit) of the offsetting items of the intercompany settlements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Main- and Subtransactions for Offsetting Entries | On the Configure Your Solution: Realize Phase screen, search Define Main- and Subtransactions for Offsetting Entries, then choose Enter.Select the line of the item of Intercompany Settlement and go to the next screen.On the Configuration Your Solution " Intercompany Settlement" screen, choose Configure on the line of configuration step with name Define Main- and Subtransactions for Offsetting Entries. |  |  |
| 5 | Define the Derivation of the Main Transaction and Subtransaction (Debit and Credit) of the Offsetting Items of the Intercompany Settlements. | On the Trans. Determination f. Clearing Within a Grop.Grp.OffstgItm screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1Requesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Main Transaction: <the Main Transaction> eg: Y600Subtransaction: <the Subtransaction> eg: 0020Choose Continue and make the entries as below:MTrans. (Offset.Itm): <the Main Transaction of Offsetting Item> eg: 0800Subtrans.(OffsetItm): <the Subtransaction of Offsetting Item> eg: 0010Tax Determination: <the Tax Determination for Input Tax> eg: S1 for AEChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Main- and Subtransactions for Offsetting Entries | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Main- and Subtransactions for Offsetting Entries. |  |  |
| 3 | Define the Derivation of the Main Transaction and Subtransaction (Debit and Credit) of the Offsetting Items of the Intercompany Settlements. | On the Trans. Determination f. Clearing Within a Grop.Grp.OffstgItm screen, choose Create and make the entries as below:Int. Settlement Type: <the Intercompany Settlement Type> eg: SIC1Requesting CCode: <the Requesting Company Code> eg: 3310Supplying CCode: <the Supplying Company Code> eg: 3330Main Transaction: <the Main Transaction> eg: Y600Subtransaction: <the Subtransaction> eg: 0020Choose Continue and make the entries as below:MTrans. (Offset.Itm): <the Main Transaction of Offsetting Item> eg: 0800Subtrans.(OffsetItm): <the Subtransaction of Offsetting Item> eg: 0010Tax Determination: <the Tax Determination for Input Tax> eg: S1 for AEChoose Save. |  |  |

#### Define Account Assignment of General Ledger Items

Use

In this step, you maintain the Account Assignment of General Ledger Items of Supplying Company.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Account Assignment of General Ledger Items | On the Configure Your Solution: Realize Phase screen, search Define Account Assignment of General Ledger Items, then choose Enter.Select the line of the item of Invoicing and go to the next screen.On the Configuration Your Solution - Invoicing screen, choose Configure on the line of configuration step with name Define Account Assignment of General Ledger Items. |  |  |
| 5 | Maintain Account Assignment of General Ledger Items for Supplying Company | On the Chrt/Accts screen, make the entries as below:Chart of Accts: <the Chart of Account> eg: YCOAChoose Continue.On the Invoicing: Account Assignments for General Ledger Items screen, choose Create and make the entries as below:Company Code: <the Supplying Company Code> eg: 3330Division: <the Division> eg: *Account Determin. ID: <the Account Determination ID> eg: *Main Transaction:<the Main Transaction> eg: *Subtransaction: <the Subtransaction> eg: *Service Type: <the Service Type> eg: *Tax Code: <the Tax Code> eg: *Choose Continue and make the entries as below:G/L Account: <the G/L account> eg: 0041005100Tax Determination: <the Tax Determination> eg: Y1CO Acct Assignment: <the CO Account Assignment> eg: Y02Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Account Assignment of General Ledger Items | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Account Assignment of General Ledger Items. |  |  |
| 3 | Maintain Account Assignment of General Ledger Items for Supplying Company | On the Chrt/Accts screen, make the entries as below:Chart of Accts: <the Chart of Account> eg: YCOAChoose Continue.On the Invoicing: Account Assignments for General Ledger Items screen, choose Create and make the entries as below:Company Code: <the Supplying Company Code>eg: 3330Division: <the Division> eg: *Account Determin. ID: <the Account Determination ID> eg: *Main Transaction:<the Main Transaction> eg: *Subtransaction: <the Subtransaction> eg: *Service Type: <the Service Type> eg: *Tax Code: <the Tax Code> eg: *Choose Continue and make the entries as below:G/L Account: <the G/L account> eg: 0041005100Tax Determination: <the Tax Determination> eg: Y1CO Acct Assignment: <the CO Account Assignment> eg: Y02Choose Save. |  |  |

#### Define Account Assignment for Business Partner Items

Use

In this step, you maintain Account Assignment for Business Partner Items of Supplying Company.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution .Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Account Assignment for Business Partner Items | On the Configure Your Solution: Realize Phase screen, search Define Account Assignment for Business Partner Items, then choose Enter.Select the line of the item of Invoicing and go to the next screen.On the Configuration Your Solution "Invoicing screen, choose Configure on the line of configuration step with name Define Account Assignment for Business Partner Items. |  |  |
| 5 | Maintain Account Assignment for Business Partner Items for Supplying Company | On the Chrt/Accts screen, make the entries as below:Chart of Accts: <the Chart of Account> eg: YCOAChoose Continue.On the Invoicing: Account Assignments for Business Partner screen, choose Create and make the entries as below:Company Code: <the Supplying Company Code>eg: 3330Division: <the Division> eg: *Account Determin. ID: <the Account Determination ID> eg: *Main Transaction:<the Main Transaction> eg: *Subtransaction: <the Subtransaction> eg: *Service Type: <the Service Type> eg: *Tax Code: <the Tax Code> eg: *Choose Continue and make the entries as below:G/L Account: <the G/L account> eg: 0012100200Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Account Assignment for Business Partner Items | Go to the Business Processes Configuration app. You can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).Search for Define Account Assignment for Business Partner Items. |  |  |
| 3 | Maintain Account Assignment for Business Partner Items for Supplying Company | On the Chrt/Accts screen, make the entries as below:Chart of Accts: <the Chart of Account> eg: YCOAChoose Continue.On the Invoicing: Account Assignments for Business Partner screen, choose Create and make the entries as below:Company Code: <the Supplying Company Code>eg: 3330Division: <the Division> eg: *Account Determin. ID: <the Account Determination ID> eg: *Main Transaction:<the Main Transaction> eg: *Subtransaction: <the Subtransaction> eg: *Service Type: <the Service Type> eg: *Tax Code: <the Tax Code> eg: *Choose Continue and make the entries as below:G/L Account: <the G/L account> eg: 0012100200Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Create Billable Items of Customer |  |  |  |
| [Option 1: Upload Billable Items](#unique_19) [page ] 26 | Invoicing Specialist (Convergent Invoicing) | Upload Billable Items (F4664) | Billable Item is created. |
| [Option 2: Invoke Create Billable Items SOAP API](#unique_20) [page ] 28 | N/A | N/A | Billable Item is created by invoking create billable items SOAP API |
| Perform Billing Process of Customer |  |  |  |
| [Option 1: Perform Billing Process (Mass Run)](#unique_21) [page ] 28 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created |
| [Option 2: Perform Billing Process (Individual Run)](#unique_22) [page ] 30 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | Billing Document is created |
| Perform Invoicing Process of Customer |  |  |  |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_23) [page ] 31 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | Invoicing Document is created |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_24) [page ] 33 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created |
| Perform Intercompany Settlement |  |  |  |
| [Display Billable Item for Intercompany Settlement (Optional)](#unique_25) [page ] 34 | Invoicing Specialist (Convergent Invoicing) | Manage Billable Items (F2621) | Billable Item is created. |
| Perform Billing Process for Intercompany Settlement |  |  |  |
| [Option 1: Perform Billing Process for Intercompany Settlement (Mass Run)](#unique_26) [page ] 35 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) |  |
| [Option 2: Perform Billing Process for Intercompany Settlement (Individual Run)](#unique_27) [page ] 36 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) |  |
|  |  |  |  |
| Perform Invoicing Process for Intercompany Settlement |  |  |  |
| [Option 1: Perform Billing Process for Intercompany Settlement (Mass Run)](#unique_26) [page ] 35 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) |  |
| [Option 2: Perform Invoicing Process for Intercompany Settlement (Individual Run)](#unique_28) [page ] 39 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) |  |
| Perform Payment Lot for Intercompany Settlement | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) |  |
| Perform Payment Run for Intercompany Settlement Offsetting | Accounts Payable and Receivable Accountant (FI-CA) | Payment Run / Debit Memo Run (F3529) |  |
| [Reverse Billable Item of Customer (Optional)](#unique_29) [page ] 41 | Invoicing Specialist (Convergent Invoicing) | Manage Billable Items (F2621) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Billable Items of Customer

#### Option 1: Upload Billable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload csv file based on the selected items to generate the billable item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Upload Billable Items (F4664) tile. | The Upload of Billable Item page is displayed. |  |
| 3 | Create Template | In the Upload of Billable Items screen, make the following entries as below and choose Create Template.Upload Schema: CSV File for Billable Items |  |  |
| 4 | Choose Billable Item Class | In the Create Template screen, make the entries as below:Choose Billable Item Class: 0SAP |  |  |
| 5 | Choose Record Type | Choose Main Items. |  |  |
| 6 | Choose Fields for Record Types | Please refer to Data Item Selection in the Appendix to choose fields of record type based on Sample Data for Intercompany Settlement.Choose Download Template. | The items were chosen and saved successfully. |  |
| 7 | Edit the local CSV file | Open and edit the copy at your native file system and add value to it accordingly. | Based on the given sequence of main item, the values were filled into csv file.Add value for Intercompany SettlementNote Please follow the sample data mentioned in Appendix to create the CSV file for Intercompany Settlement. |  |
| 8 | Import CSV File | In the Upload of Billable Items screen, make the entries as below:File Source: Choose Browse and find the file you edited.Choose OK to close the popup dialog of File Upload and upload the file you edited at step7 from native file system to SAP file system. | The file you edited at step7 was uploaded to SAP system. |  |
| 9 | Read CSV File | Choose Read. | Log is provided to identify the csv file read error.If there is no error, the field and filed value of CSV file can be displayed at Preview section. You also can choose Edit to modify the value as your demands. |  |
| 10 | Load CSV File | Choose the entries you want to upload then choose Upload. | Before load data, you can make the modification to the individual field based on your request. |  |
| 11 | Display Billable Items of Customer | Choose Show Billable Items on the Upload Messages screen.The Billable Item of Customer with Billable Item Type Service(Y001) has been generated. | The Billable Item of Customer with Billable Item Type Service(Y001) is displayed.Please record the Source Transaction Id of the Billable Item of the Customer. |  |
| 12 | Display Billable Item of Intercompany Settlement | In the Manage Billable Items screen, choose the billable item of the customer then choose Details .In the Billable Items of a Source Transaction screen, choose Details of the Billable Item In the Manage Billable Items screen, choose Show Secondary Items. | The Billable Item of Intercompany Settlement with Billable Item Type SICR is displayed.Please record the Source Transaction ID of the Billable Item of Intercompany Settlement. |  |

#### Option 2: Invoke Create Billable Items SOAP API

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the billable items by invoking the SOAP API of convergent invoicing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Navigate to SAP API Business HUB | Open web browser and navigate to [https://api.sap.com](https://api.sap.com) | The SAP API Business HUB home page is displayed. |  |
| 2 | Locate SAP S/4HANA Cloud Public Edition API package | Choose SAP S/4HANA Cloud Public Edition and choose APIs tab. | The SAP S/4HANA Cloud Public Edition API package is located. |  |
| 3 | Search out create billable items SOAP API | Choose SOAP and search for Convergent Invoicing Billable Items - Create. | The create billable items SOAP API is displayed. |  |

### Perform Billing Process of Customer

In this step, you start up the billing process to create the billing document. You can process with mass run or individual creation.

#### Option 1: Perform Billing Process (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: Y001Contract Account: <the required contract account of customer>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access the located application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Billing Process (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: Y001Billing Date: <the current date>Contract Account: <the required contract account of customer> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items dialog, choose the Billable Items of Customer whose Source Transaction ID is the same as the one you have recorded in the previous step then choose Save. In the Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed.Please record the Billing Document Number. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Perform Invoicing Process of Customer

In this step, you create invoice document based on the billing document you created at previous step. You can proceed with mass run or individual creation.

#### Option 1: Perform Invoicing Process (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524). | The Execute Invoicing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Invoicing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <the required business partner of customer>Contract Account: <the required contract account of customer>Simulation Run: <don’t choose>Document Date: <the current date>Posting Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. |  |  |
| 9 | Check Log | Choose Image of Log to located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

#### Option 2: Perform Invoicing Process (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner of customer>Contract Account: <the required contract account of customer> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose the one which Source Document No. is the same as your recorded Billing Document No. , then choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document dialog, choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check thedocuments before posting. | A dialog Invoicing Ended is displayed.Invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

### Perform Intercompany Settlement

#### Display Billable Item for Intercompany Settlement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Intercompany Settlement Billable Item is displayed

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Billable Items (F2621) tile. |  |  |
| 3 | Locate the Billable Item for Customer | On the Manage Billable Items screen, make the following entries as below:Invoicing Document: <the Invoicing Document of Customer>Choose Go. | You have searched out the Billable Item for Customer by Customer Invoicing Document number you recorded at previous step. |  |
| 4 | Display Billable Item for Intercompany Settlement | On the Manage Billable Items screen, choose the located Customer Billable Item and choose Details.On the Source Transaction XXXXX screen, choose Main Items tab and choose Details of the Billable Item.On the Package of Billable Items XXXX screen, choose Show Secondary Items. | The Billable Item for Intercompany Settlement is displayed. |  |

#### Perform Billing Process for Intercompany Settlement

##### Option 1: Perform Billing Process for Intercompany Settlement (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run page is displayed |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: SICOContract Account: <the required contract account of Service Requester>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access the located application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

##### Option 2: Perform Billing Process for Intercompany Settlement (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: SICOBilling Date: <the current date>Contract Account: <the required contract account of Service Requester> |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items dialog, the Billable Item of Intercompany Settlement whose Source Transaction ID is the same as the one you have recorded in the previous step, then choose Save. In the Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed.Please record the Billing Document Number. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog. |  |  |

#### Perform Invoicing Process for Intercompany Settlement

##### Option 1: Perform Invoicing Process for Intercompany Settlement (Mass Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Administrator (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524). | The Execute Invoicing - Mass Run page is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Invoicing (Mass Creation)Job Name; <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: SIBusiness Partner: <the required business partner of Service Requester>Contract Account: <the required contract account of Service Requester>Simulation Run: <don’t choose>Document Date: <the current date>Posting Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. |  |  |
| 9 | Check Log | Choose Image of Log to located the application job log. | The log of application job is displayed. From the log, you can see the result of application job. |  |

##### Option 2: Perform Invoicing Process for Intercompany Settlement (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Invoicing - Business Partner (FKKINV_S) tile. | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: SIDocument Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose the one which Source Document No. is the same as your recorded Billing Doucment No. , then choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then choose Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document dialog, choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed.Invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog. |  |  |

#### Perform Payment Lot for Intercompany Settlement

Purpose

In this activity, you process Payment Lot for Intercompany Settlement. To do so, refer to the test script of the scope item Contract Accounting – Customer Initiated Payments(2BI), chapter Payment Lot Processing – Process Payment Lot and chapter Payment Lot Processing – Post Payment Lot to clear the Posting Document of Intercompany Settlement.

| RefDoc Type | Doc. No. | Name of Reference Document Type | Comments |
| --- | --- | --- | --- |
| 0ICO | <the posting document of Intercompany Settlement> | Posting Intercompany Settlement | The posting document of Intercompany Settlement you recorded at previous Step. |

#### Perform Payment Run for Intercompany Settlement Offsetting

Purpose

In this activity, you process Payment Run for Intercompany Settlement Offsetting. To do so, refer to the test script of the scope item Contract Accounting – Company Initiated Payments(2DP), chapter Payment Process – Execute Payment Run and chapter Payment Process – Check Payment Documents to clear the Posting Document of Intercompany Settlement Offsetting.

| RefDoc Type | Doc. No. | Name of Reference Document Type | Comments |
| --- | --- | --- | --- |
| 0ICS | <the posting document of Intercompany Settlement Offsetting> | Posting Intercompany Settlement (Offsetting Doc) | The posting document of Intercompany Settlement Offsetting you recorded at previous Step. |

### Reverse Billable Item of Customer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the customer Billable Item to reverse the customer consumption and intercompany Settlement. The corresponding write-off customer billable item and write-off intercompany settlement billable item have been generated by system. User can choose to do billing and invoicing against the write-off billable items to write off the customer consumption and intercompany settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Billable Items (F2621) tile. |  |  |
| 3 | Maintain Parameters | In the Manage Billable Items screen, make the entries as below and choose Go.Source Transaction ID:<the business transaction ID of customer>Business Partner:<the business partner of customer>Contract Account: <the contract account of customer> | The billable item of customer has been located in the list. |  |
| 4 | Reverse Billable Item | In the Manage Billable Items screen, choose the billable item of customer then choose Reverse.In the Reverse screen, make the entry as below:Reversal Reason: <the reversal reason> eg: Reverse (Y1)Choose Reverse. | The write-off billable item of customer can be located via Manage Billable Items (F2621).The write-off billable item of Intercompany can be located via Manage Billable Items (F2621). |  |

## Appendix

### Process Integration

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

Table 1:

| Process | Business Condition |
| --- | --- |
| Contract Accounting – Master Data and Basic Functions(2AR) | Must be run before the test script. Business Partner and Contract Account must be created. |

### CSV Template Creation

#### Sample Data for Intercompany Settlement

| Item of Main Items | Global Field Name | Intercompany Settlement | Comments |
| --- | --- | --- | --- |
| BIT_AMOUNT | CABllbleItmAmount | Positive Value | Billable Item Amt |
| GPART | BusinessPartner | The business partner | Business Partner |
| SRCTAID | CABllbleItmSourceTransId | Any Number | Source Trans.ID |
| SUBPROCESS | CABillgSubprocess | Y001 | Subprocess of Billing |
| BITTYPE | CABllbleItmType | Y001 | Type of Billable Item |
| VKONT | ContractAccount | The contract account | Contract Account |
| BIT_CURR | CABllbleItmCurrency | The currency | Currency |
| ICO_BUKRS_REQ | CAIntcoCompanyCodeRequesting | The requesting company code | Requesting CCode |
| ICO_BUKRS_SUP | CAIntcoCompanyCodeSupplying | The supplying company code | Supplying CCode |
| ICO_TYPE | CAIntcoType | SIC1 | Int. Settlement Type |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-revenue-sharing-and-partner-settlemen]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6WC_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 76,132 chars in the whole document
