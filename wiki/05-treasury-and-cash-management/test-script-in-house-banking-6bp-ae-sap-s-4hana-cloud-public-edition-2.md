---
id: 05-treasury-and-cash-management/test-script-in-house-banking-6bp-ae-sap-s-4hana-cloud-public-edition-2
title: "Test Script: In-House Banking (6BP_AE) - SAP S/4HANA Cloud Public Edition 2608 (6BP_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script (AE, release 2608) for In-House Banking: prerequisites, setup, payments on behalf, intercompany, central incoming, end of day, reclassification."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/in-house-banking]
aliases: [6BP_S4CLD2608_BPD_EN_AE]
keywords: [In-House Banking, in-house bank accounts, payments on behalf, intercompany payments, central incoming payments, end of day processing, in-house bank conditions, in-house bank limits, multi-bank connectivity, advanced payment management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1162
topic: 05-treasury-and-cash-management/in-house-banking
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: In-House Banking (6BP_AE) - SAP S/4HANA Cloud Public Edition 2608 (6BP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **In-House Banking** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | In-House Banking (6BP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232858410)

[2 Prerequisites 5](#_Toc232858411)

[2.1 System Access 5](#_Toc232858412)

[2.2 Roles 5](#_Toc232858413)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232858414)

[2.4 Additional Manual Configuration 10](#_Toc232858415)

[2.5 Business Conditions 10](#_Toc232858416)

[2.6 Preliminary Steps 11](#_Toc232858417)

[2.6.1 Create/Extend Business Partners Representing Subsidiary Company Code 11](#_Toc232858418)

[2.6.1.1 Create Business Partners Representing Subsidiary Company Code 12](#_Toc232858419)

[2.6.1.2 Extend Business Partners as IHB Account Holder and Inhouse Bank Area Owner 14](#_Toc232858420)

[2.6.2 Manage Banks and House Banks 16](#_Toc232858421)

[2.6.3 Set Up Bank Determination for Payment Transactions 18](#_Toc232858422)

[2.6.4 Assign Account Symbol to Payment Methods (Optional) 22](#_Toc232858423)

[2.6.5 Set Alternative Format Type per Company Code 24](#_Toc232858424)

[2.6.6 Relevant Configuration Steps for Post Balance Sheet Reclassification 26](#_Toc232858425)

[2.6.7 Maintain Routing Setting 28](#_Toc232858426)

[2.6.8 Maintain Multi-Bank Connectivity Connector Outbound Settings 34](#_Toc232858427)

[2.6.9 Define Parameter Sets 36](#_Toc232858428)

[2.6.10 Manage Teams and Responsibilities for Approver 38](#_Toc232858429)

[2.6.10.1 Manage Teams and Responsibility for In-House Banking Account Approver 38](#_Toc232858430)

[2.6.10.2 Manage Teams and Responsibility for In-House Banking Condition Approver 39](#_Toc232858431)

[2.6.10.3 Manage Teams and Responsibility for In-House Banking Limit Approver 40](#_Toc232858432)

[2.6.11 Manage In-House Bank Workflow (Option) 41](#_Toc232858433)

[2.6.12 Manage Cost Center 42](#_Toc232858434)

[3 Overview Table 44](#_Toc232858435)

[4 Test Procedures 48](#_Toc232858436)

[4.1 Initialize In-House Banking End of Day Processing Dates 48](#_Toc232858437)

[4.2 Set Up In-House Bank Accounts 49](#_Toc232858438)

[4.2.1 Create In-House Bank Accounts 49](#_Toc232858439)

[4.2.1.1 Create Directly (Option 1) 49](#_Toc232858440)

[4.2.1.1.1 Create In-House Banking 49](#_Toc232858441)

[4.2.1.1.2 Activate In-House Bank Accounts 54](#_Toc232858442)

[4.2.1.1.3 Download In-House Bank Accounts 54](#_Toc232858443)

[4.2.1.1.4 Validate XML file 56](#_Toc232858444)

[4.2.1.1.5 Import Bank Accounts 57](#_Toc232858445)

[4.2.1.1.6 Maintain Bank Accounts 58](#_Toc232858446)

[4.2.1.2 Create via eBAM Integration (Option 2) 59](#_Toc232858447)

[4.2.2 Manage In-House Bank Conditions 60](#_Toc232858448)

[4.2.3 Manage In-House Bank Limits 62](#_Toc232858449)

[4.2.4 Maintain Payment Transaction for Business Partner 64](#_Toc232858450)

[4.3 Payments on Behalf 66](#_Toc232858451)

[4.3.1 Maintain Payment Agreements 66](#_Toc232858452)

[4.3.2 Subsidiary 1: Create Vendor Invoice 68](#_Toc232858453)

[4.3.3 Subsidiary 1: Payment Run 69](#_Toc232858454)

[4.3.4 Monitor MBC Message (with Payment File) 70](#_Toc232858455)

[4.3.5 Process Payment in Advanced Payment Management 71](#_Toc232858456)

[4.3.6 Check Payment Order 72](#_Toc232858457)

[4.3.7 Approve Payment Batch (Optional) 73](#_Toc232858458)

[4.3.8 Manage In-House Bank Account Balances 73](#_Toc232858459)

[4.3.9 Monitor MBC Message (with Payment File) 74](#_Toc232858460)

[4.3.10 Manage Returned Payment (Optional) 75](#_Toc232858461)

[4.4 Intercompany Payments 75](#_Toc232858462)

[4.4.1 Subsidiary 1: Create Customer Invoice 76](#_Toc232858463)

[4.4.2 Subsidiary 2: Create Vendor Invoice 77](#_Toc232858464)

[4.4.3 Subsidiary 2: Payment Run 78](#_Toc232858465)

[4.4.4 Monitor MBC Message (with Payment File) 79](#_Toc232858466)

[4.4.5 Process Payment in Advanced Payment Management 80](#_Toc232858467)

[4.4.6 Check Payment Order 81](#_Toc232858468)

[4.4.7 Manage In-House Bank Account Balances 82](#_Toc232858469)

[4.5 Central Incoming Payments 83](#_Toc232858470)

[4.5.1 Manage Service Level Agreements 83](#_Toc232858471)

[4.5.2 Manage Processing Rules for Bank Statement 85](#_Toc232858472)

[4.5.3 Import External Bank Statement 87](#_Toc232858473)

[4.5.4 Process Payment in Advanced Payment Management 90](#_Toc232858474)

[4.5.5 Manage In-House Bank Account Balances 91](#_Toc232858475)

[4.6 End Of Day Process 92](#_Toc232858476)

[4.6.1 Maintain Exchange Rates 92](#_Toc232858477)

[4.6.2 Create Correction (Optional) 92](#_Toc232858478)

[4.6.3 Close In-House Bank Accounts 93](#_Toc232858479)

[4.6.4 Manage In-House Bank Application Jobs 95](#_Toc232858480)

[4.6.5 Manage In-House Bank End of Day 99](#_Toc232858481)

[4.6.6 Manage In-House Bank Account Balances 100](#_Toc232858482)

[4.6.7 Monitor MBC Message (with Payment File) 102](#_Toc232858483)

[4.7 Post B/S Reclassification 103](#_Toc232858484)

[5 Appendix 104](#_Toc232858485)

[5.1 Process Chains 104](#_Toc232858486)

## Purpose

Overview

In-house banking offers bank accounts for all subsidiaries in different account currencies. Subsidiaries send their payment files using standard payment processes offered within financial accounting. In-house banking sends electronic bank statements back to clear the open items accordingly.

In-house banking supports payments between subsidiaries (intercompany and cross-bank area intercompany payments), payments towards external business partners (payments on behalf), and central incoming payments (for example, resulting from external zero balancing postings).

In-house banking offers the calculation of interest and fees on internal bank accounts. With help of limits that can be assigned to the internal bank accounts, you can easily monitor the cash situation.

The financial accounting of the in-house banking owner is automatically updated via the general ledger transfer. By leveraging Finance Business Integration Interface (FIBTI) and Account Business Transaction Interface (ABTI), the subledger applications Advanced Payment Management and In-house banking are fully decoupled from Financial Accounting.

In-house banking is fully embedded into SAP S/4HANA Cloud Public Edition, advanced payment management and benefits from the scope of features involved.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/6BP_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Suggested sample user BUPA_MASTER_SPECIALIST representing the business role Master Data Spe-cialist - Business Partner Data. |
| Payment Specialist | SAP_BR_PAYMENT_SPECIALIST | Payment Management | SAP_BR_PAYM_SPECIALIST | Suggested sample user PAYMENT_SPECIALIST representing the business role Payment Specialist. |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST | Suggested sample user CASH_SPECIALIST representing the business role Cash Management Specialist. |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER | Suggested sample user CASH_MANAGER representing the business role Cash Manager. |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Suggested sample user AP_ACCOUNTANT representing the business role Account Payable Account-ant. |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER | Suggested sample user AP_MANAGER representing the business role Accounts Payable Manager. |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT | Suggested sample user AR_ACCOUNTANT representing the business role Accounts Receivable Accountant. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Suggested sample user BPC_EXPERT representing the business role Configuration Expert - Business Process Configuration. |
| Business Integration Specialist - Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Bank Integration | SAP_BR_BANK_INT_SPECIALIST | Suggested sample user BANK_INT_SPECIALIST representing the business role Business Integration Specialist - Bank Integration. |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT | Suggested sample user GL_ACCOUNTANT representing the business role General Ledger Accountant. |
| Payment Specialist - In-House Banking | SAP_BR_PAYM_SPECIALIST_IHB | In-House Bank | SAP_FIN_SPT_FSCM_PF_IHB_PC | Suggested sample user PAYM_SPECIALIST_IHB representing the business role Payment Specialist in-house banking. |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. Depending on the operational focus of your company, the master data represents materials, customers, and vendors.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices deliver standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data table. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value (Head Office) | Sample Val.Subsidiary 1 | Sample Val. Subsidiary 2 | Comments |
| --- | --- | --- | --- | --- |
| Bank Key | #600310101 |  |  | Bank key as In-House Bank CenterThe bank key needs to comply with the country specific settings, e.g. the length of the bank numbers in that specific country. For more details, you can check in configuration activity 102592 Set Country-Specific Checks. |
| In-House Bank area | SIAE |  |  |  |
| Country | AE | AE | AE |  |
| Company Code | 3310 | 33 40 | 33 30 |  |
| Business Partner |  | 33403340 | 33403330 | Business Partner presenting subsidiary company code |
| Payment method | [ | [ | Payment method for In-House Banking Payment |  |
| G/L Account | Clearing. account intercompany payments(APM) 11001410Clearing account OBO payments (APM) 11001400Clring account central incoming payments (APM) 11001420Receivables / liabilities (IHB) 12305100Receivables/affiliated companies (IHB) 12305000Liabilities affiliated companies(IHB) 21305000Charges income (IHB) 70800300Withholding tax receivables (IHB) 21603110Loss from Exchange Rate Differences72010000Gain from exchange rate differences 72510000Interest Expense 70100000Interest Income 71100000 | IHB bank clearing acct 11001020IHB bank account 11001000InterestExpense-Subsidiaries 71300000Interest Income–Subsidiaries 70300000Withholding Tax 21603000Loss from Exch Rate Differences 72010000Gain from exch rate differences 72510000 | IHB bank clearing acct 11001020IHB bank account 11001000InterestExpense-Subsidiaries 71300000Interest Income–Subsidiaries 70300000Withholding Tax 21603000Loss from Exch Rate Differences 72010000Gain from exch rate differences 72510000 | G/L account for bank accounts |
| Chart of Accounts | YCOA | YCOA | YCOA | Chart of accounts |
| House Bank | AE BK1/ AEBK2 (AE) | IHB01 | IHB02 | House bank for head office and In-House Banking Account |
| House Bank Account | AE AC1/ AEAC2 (AE) | the In-House Bank account for subsidiary 1, for example, 1The In-House Bank account to be closed for subsidiary 1, hereafter referred to as IHB Bank account to close sub 1, for example, 3 | the In-House Bank account for subsidiary 2, for example, 2The In-House Bank account to be closed for subsidiary 1, hereafter referred to as IHB Bank account to close sub 2, for example, 4 | House bank account for In-House Banking Account |
| Profit Center | YB600 |  |  | Default Profit Center |
| Cost center | 33 101101 | 33 401101 | 33 301101 | Default Cost Center |
| Customer number |  | 3340IHB01 | 3330IHB02 | The customer number is used in procedure [Manage Banks and House Banks](#unique_6) [page ] 16 |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f33301312a7f3f336f509fc2c25a4635)

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J77 - Advanced Bank Account Management | Payment approvers are maintained per bank account to enable payment approvals. |
| 16R - Bank Integration with SAP Multi-Bank Connectivity | 16R - Multi-Bank Connectivity is in scope and a connection is set up.After payment run is conducted, the payment media file is transmitted into Multi-Bank Connectivity and displayed in the 4MT - Advanced Payment Management Payment Monitor list. |
| J78 - Advanced Cash Operations | After payment processing in 4MT - Advanced Payment Management, the outgoing payment is approved in J78 - Advanced Cash Operations. |
| 4MT - Advanced Payment Management | 4MT - Advanced Payment Management is in scope. |

### Preliminary Steps

#### Create/Extend Business Partners Representing Subsidiary Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you need to create/extend business partners representing headquarter company and subsidiaries companies.

|  |
| --- |
| Note Please make sure that only one business partner is created for each headquarter and subsidiary company code. |

For example, if you have created both subsidiaries company code as 3340 & 3330, you can create and extend following business partner for the headquarter and each subsidiary company code:

| Business Partner | Role | Company Code | Trading Partner | PartnerCocode | Bank Area | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| 33403310 | IHB200 Inhouse Bank Area Owner | N/A | 3310 | N/A | SIAE | The Business partner is created representing headquarter company code 3310. |
| 33403340 | IHB100 IHB Account Holder | N/A | 3340 | 3340 | N/A | The Business partner is created representing subsidiary company code 3340. |
|  | FLVN00 Supplier (Fin.Accounting) | 3330 | N/A | N/A | N/A | The business partner is created under company code 3330 as intercompany vendor which is used in Intercompany scenario.Assign Reconciliation Acct 21300000 (Payables affiliated Companies) |
| 33403330 | IHB100 IHB Account Holder | N/A | 3330 | 3330 | N/A | Business partner is created representing subsidiary company code 3330. |
|  | FLCU00 Customer (Fin.Accounting) | 3340 | N/A | N/A | N/A | The business partner is created under company code 3340 as intercompany customer which is used in Intercompany scenario.Assign Reconciliation Acct 12300000 (Payables affiliated Companies) |
| 33300001 | FLVN00 Supplier (Fin.Accounting) | 3340 | N/A | N/A | N/A | The business partner is created under company code 3340 as external vendor which is used in #unique_61 scenario.Assign Reconciliation Acct 21100000 (Payables Domestic) |

##### Create Business Partners Representing Subsidiary Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you create business partners representing subsidiaries companies.

|  |
| --- |
| Note If the business partner has been created for the subsidiary company code, you skip the whole step and go to next step to extend business Partner. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Business Partner Master Data(F3163). | The Manage Business Partner view displays. |  |
| 3 | Find Existing Business Partner | Make the following entries and choose Go:Business Partner: for example, 33403310 | The existing business partner displays. |  |
| 4 | Copy Existing Business Partner (Optional) | Select the business partner and choose Copy.Note If you want to edit an existing business partner, you can skip step 4-5. Choose > for an existing business partner. | The Business Partner view displays. |  |
| 5 | Edit Header (Optional) | Choose Edit Header. On the Edit Header dialog box, make the following entries and choose OK:Business Partner: for example, 33403340Grouping: BP03 |  |  |
| 6 | Create Role FLVN00 Supplier (Fin.Accounting) | In the Roles section, choose Create.Make the following entries and choose >:Business Partner Role: FLVN00 Supplier (Fin.Accounting)Note If the role exists, you do not need to create the role. | The Change Organization:xxxxxxxx, role Supplier(Fin.Accounting) screen displays. |  |
| 7 | Maintain Parameters Under Company Code | In the Company Codes section, choose Create, make the following entries and choose Apply. In the next screen, choose Apply again:Company Code: 3330Reconciliation Acct: 21300000Note The business partner is created under company code 3330 as intercompany vendor which is used in Intercompany scenario. Assign Reconciliation Acct 21300000 (Payables affiliated Companies). |  |  |
| 8 | Create Business Partner for Subsidiary 1 | Choose Create or Save. | The new business partner is created representing subsidiary 1 company code 3340. |  |
| 9 | Create Business Partner for Subsidiary 2 | Repeat step 3-8, create a business partner for subsidiary 2 company code as following:Business Partner: for example, 33403330Grouping: BP03Change in BP role: FLCU00 Customer(Fin.Accounting)Company Code: 3340Reconciliation Acct: 12300000Note The business partner is created under company code 3340 as intercompany customer which is used in Intercompany scenario. Assign Reconciliation Acct 12300000（Payables affiliated Companies） | The new business partner is created representing subsidiary 2 company code 3330. |  |
| 10 | Maintain Business Partner for Subsidiary 1 | Repeat step 3-8, maintain an existing business partner for subsidiary 1 company code as following:Business Partner: for example: 33300001Change in BP role: FLVN00 Supplier (Fin.Accounting)Company Code: 3340Reconciliation Acct: 21100000Note The business partner is created under company code 3340 as external vendor which is used in Payments On Behalf scenario. Assign Reconciliation Acct 21100000 (Payables Domestic). |  |  |

##### Extend Business Partners as IHB Account Holder and Inhouse Bank Area Owner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you extend business partners as IHB account holder.

Prerequisites

The business partner representing subsidiary company code is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Find Business Partner | Make the following entries and choose Enter:Business Partner: for example, 33403340 | The Display Organization:XXXXXXXX displays. |  |
| 4 | Change | Choose Switch Between Display and Change. | The Change Organization:XXXXXXXX displays. |  |
| 5 | Add E-Mail | In the Address tab, under Communication section, add your email address in E-Mail field.Note The email addresses will be used in In-house bank account to receive the relevant notification. |  |  |
| 5 | Extend Role IHB Account Holder (Subsidiary 1 Business Partner) | Make the following entries and choose OK:Change in BP role: IHB100 IHB Account Holder |  |  |
| 6 | Edit Control Tab | Choose Control tab, make the following entries and choose Save.Trading Partner No.: for example, 3340PartnerCocode.: for example, 3340 | The new role is extended. |  |
| 7 | Extend Business Partner for Subsidiary 2 | Repeat step 3-6, extend a business partner for subsidiary 2 company code as following:Business Partner: for example, 33403330Trading Partner No.: for example, 3330PartnerCocode.: for example, 3330 | The new role is extended. |  |
| 8 | Extend Business Partner for Headquarter | Repeat step 3-6, extend a business partner for headquarter company code as following:Business Partner: for example, 33403310BP role: IHB200 Inhouse Bank Area OwnerTrading Partner No.: 3310Inhouse Bank Area.: for example, SIAENote To define a new bank area, you create an In-House bank in next step and define the bank area in configuration activity 105773 Define Bank Areas for Account Management. | The new role is extended. |  |

#### Manage Banks and House Banks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a bank key as in-house bank center and also create the house banks.

Procedure

This procedure is mentioned in the Advanced Bank Account Management - [J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77) test script. You can refer to the Create Bank Master Data and Manage Banks Cash Management Data step and create a bank key.

|  |
| --- |
| Note In step Create Bank Master Data, choose Create Internal Bank from dropdown list. Otherwise, the Bank Category field will be invisible in the pop up window. |

For example, if you have created both subsidiaries company code as 3340 & 3330, you can create bank and house banks as following:

|  |
| --- |
| Note The bank key and bank number need to comply with the country specific settings, e.g. the length of the bank numbers in that specific country. For more details, you can check in configuration activity 102592 Set Country-Specific Checks. |

General Data:

Bank Country: for example, AE

Bank Key: #600310101

|  |
| --- |
| Note The bank key is used as sender ID during the local routing of the internal bank statement.For more details, refer to test procedure [Maintain Routing Setting](#unique_12) [page ] 28. |

Bank Name: for example, In-house Bank AE

Bank Number: #600310101

SWIFT/BIC: PYFPDEIHBXX

|  |
| --- |
| Note If the bank category is In-House bank, maintain BIC for SEPA counties. However, do not maintain BIC for non-SEPA countries. |

Bank Category: 6 In-House Bank

House Banks:

Item 1)

Company Code: Company Code of the Subsidiary 1. For example, 3340

House Bank: House bank of the subsidiary 1. For example, IHB01

Customer Number: Customer number of the subsidiary 1. For example, 3340IHB01

|  |
| --- |
| Note The customer number is used during the local routing of the payment and internal bank statement.For more details, refer to test procedure [Maintain Routing Setting](#unique_12) [page ] 28. |

Item 2)

Company Code: Company Code of the Subsidiary 2. For example, 3330

House Bank: House bank of the subsidiary 2. For example, IHB02

Customer Number: Customer number of the subsidiary 1. For example, 3330IHB02

|  |
| --- |
| Note The customer number is used during the local routing of the payment and internal bank statement.For more details, refer to test procedure [Maintain Routing Setting](#unique_12) [page ] 28. |

#### Set Up Bank Determination for Payment Transactions

Use

In this activity, make settings that the payment program uses to select the banks or bank accounts from which payment is to be made.

Prerequisite

|  |
| --- |
| Note The In-House bank account for subsidiary is created in test step Set Up In-House Bank Accounts. The house bank is created in preliminary step Manage Banks and House Banks. You need to finish all the steps before this preliminary step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Accounts Payable | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Automatic Payments. | The Configuration Steps for the selected row display. |  |
| 6 | Define Account Determination | On the Set Up Bank Determination for Payment Transactions row, choose Configure. | The “Set Up Bank Determination for Payment Trans..”:Display screen displays. |  |
| 7 | Select Paying Company code | Select the Paying company code: for example, 3340 (company code for subsidiary 1) |  |  |
| 8 | Ranking Order | In the left-side dialog structure, Choose Ranking Order node. | The “Set Up Bank Determination for Payment Trans..”:Change screen displays. |  |
| 9 | New Entries | Choose New Entries and make the following entries:PM: [Crcy: <empty>Rank.order: for example, 1House Bk: for example, IHB01 | The ranking order is defined. |  |
| 10 | Bank Accounts | In the left-side dialog structure, Choose Bank Accounts node. |  |  |
| 11 | Delete Entries | Check if there is any entry maintained for house bank IHB01, payment method [. If yes, delete those entries.Note As there are multiple IHB accounts involved within the same house bank, it is expected that no entry is maintained in this node, instead the multiple account determination has to be maintained in node Bank Accounts (Enhanced). Refer to the next step for the configuration. |  |  |
| 12 | Bank Accounts (Enhanced) | In the left-side dialog structure, choose Bank Accounts (Enhanced) node. |  |  |
| 13 | New Entries | Choose New Entries, enter the following data and choose Save:Entry 1House bank: for example, IHB01Payment method: [Currency: AEDRanking Order: 1Account ID: <the inhouse bank account for subsidiary 1>, for example, 1Bank subaccount: <empty>Entry 2House bank: for example, IHB01Payment method: [Currency: AEDRanking Order: 2Account ID: <the IHB Bank account to close sub 1>, for example, 3Bank subaccount: <empty> | The bank account is defined. |  |
| 14 | Set Up Bank Determination for Payment Transactions for Subsidiary 2 | Repeat step 7-13, make the following entries for subsidiary 2:Paying company code: for example, 3330 (company code for subsidiary 2)Ranking OrderPM: [Crcy: <empty>Rank.order: for example, 1House Bk: for example, IHB02Bank Accounts (Enhanced)Entry 1House bank: for example, IHB02Payment method: [Currency: AEDRanking Order: 1Account ID: <the inhouse bank account for subsidiary 2>, for example, 2Bank subaccount: <empty>Entry 2House bank: for example, IHB02Payment method: [Currency: AEDRanking Order: 2Account ID: <the IHB Bank account to close sub 1>, for example, 4Bank subaccount: <empty> | Bank Determination for Payment Transactions for subsidiary 2 is set up. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Bank Determination for Payment Transactions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Bank Determination for Payment Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Set Up Bank Determination for Payment Trans..”:Display screen displays. |  |
| 3 | Select Paying Company Code | Select the Paying company code: for example, 3340 (company code for subsidiary 1) |  |  |
| 4 | Ranking Order | In the left-side dialog structure, Choose Ranking Order node. | The “Set Up Bank Determination for Payment Trans..”:Change screen displays. |  |
| 5 | New Entries | Choose New Entries and make the following entries:PM: [Crcy: <empty>Rank.order: for example, 1House Bk: For example, IHB01 | The ranking order is defined. |  |
| 6 | Bank Accounts | In the left-side dialog structure, Choose Bank Accounts node. |  |  |
| 7 | Delete Entries | Check if there is any entry maintained for house bank IHB01, payment method [. If yes, delete those entries.Note As there are multiple IHB accounts involved within the same house bank, it is expected that no entry is maintained in this node, instead the multiple account determination has to be maintained in node Bank Accounts (Enhanced). Refer to the next step for the configuration. |  |  |
| 8 | Bank Accounts (Enhanced) | In the left-side dialog structure, choose Bank Accounts (Enhanced) node. |  |  |
| 9 | New Entries | Choose New Entries, enter the following data and choose Save:Entry 1House bank: for example, IHB01Payment method: [Currency: AEDRanking Order: 1Account ID: <the inhouse bank account for subsidiary 1>, for example, 1Bank subaccount: <empty>Entry 2House bank: for example, IHB01Payment method: [Currency: AEDRanking Order: 2Account ID: <the IHB Bank account to close sub 1>, for example, 3Bank subaccount: <empty> | The bank account is defined. |  |
| 10 | Set Up Bank Determination for Payment Transactions for Subsidiary 2 | Repeat step 3-9, make the following entries for subsidiary 2:Paying company code: for example, 3330 (company code for subsidiary 2)Ranking OrderPM: [Crcy: <empty>Rank.order: for example, 1House Bk: for example, IHB02Bank Accounts (Enhanced)Entry 1House bank: for example, IHB02Payment method: [Currency: AEDRanking Order: 1Account ID: <the inhouse bank account for subsidiary 2>, for example, 2Bank subaccount: <empty>Entry 2House bank: for example, IHB02Payment method: [Currency: AEDRanking Order: 2Account ID: <the IHB Bank account to close sub 1>, for example, 4Bank subaccount: <empty> | Bank Determination for Payment Transactions for subsidiary 2 is set up. |  |

#### Assign Account Symbol to Payment Methods (Optional)

Use

In this activity, you specify the account symbol to use for a combination of country/region with payment method.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Accounts Payable | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Automatic Payments. | The Configuration Steps for the selected row display. |  |
| 6 | Configure | On the Assign Account Symbol to Payment Methods row, choose Configure. | The "Assign Account Symbol to Payment Methods” : Overview screen displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Assign Account Symbol to Payment Methods | Enter the following data and choose Save.C/R: AEPayment method: [Account Symbol: for example, SIHB_CLEARING | The account symbol is assigned to payment methods. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Select Customizing Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Account Symbol to Payment Methods..Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Assign Account Symbol to Payment Methods” : Overview screen displays. |  |
| 3 | Assign Account Symbol to Payment Methods | Enter the following data and choose Save.C/R: AEPayment method: [Account Symbol: for example, SIHB_CLEARING | The account symbol is assigned to payment methods. |  |

#### Set Alternative Format Type per Company Code

Use

In this activity, you set alternative format type per company code.

Prerequisite

|  |
| --- |
| Note The In-House bank account for subsidiary is created in Create In-House Bank Accounts section. You need to finish all the steps under the Create In-House Bank Accounts section in Test Procedures. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Accounts Payable | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Automatic Payments. | The Configuration Steps for the selected row display. |  |
| 6 | Define Account Determination | On the Set Up Payment Methods for Each Country/Region for Payment Transactions. | The “Set Up Payment Methods for Each Country/Reg..": Change screen displays. |  |
| 7 | Select Payment Method/Country | Select the payment method/Country: for example, AE/[, then double click the payment method. |  |  |
| 8 | Maintain Payment Medium | In Payment medium section, choose Format in Company Code beside the format AE_CGI_XML_CT. | The "Set a Payment Medium Format per Company Code": Change screen displays. |  |
| 9 | New Entries | Choose New Entries and make the following entries and choose Save.Entry 1)CoCd: 3340PM: [Payt Mdm Format: AE_CGI_XML_CTHouse Bk: For example IHB01Alternative Format Type:90 SAP Multi-Bank ConnectivityEntry 2)CoCd: 3330PM: [Payt Mdm Format: AE_CGI_XML_CTHouse Bk: For example, IHB02Alternative Format Type: 90 SAP Multi-Bank Connectivity | The alternative format Type is defined for subsidiary company code 1 & 2. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Payment Methods for Each Country/Region for Payment Transactions | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Set Up Payment Methods for Each Country/Region for Payment Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Set Up Payment Methods for Each Country/Reg..": Change screen displays. |  |
| 3 | Select Payment Method/Country | Select the payment method/Country: for example, AE, then double click the payment method. |  |  |
| 4 | Maintain Payment Medium | In Payment medium section, choose Format in Company Code beside the format AE_CGI_XML_CT. | The "Set a Payment Medium Format per Company Code": Change screen displays. |  |
| 5 | New Entries | Choose New Entries and make the following entries and choose Save.Entry 1)CoCd: 3340PM: [Payt Mdm Format: AE_CGI_XML_CTHouse Bk: For example IHB01Alternative Format Type:90 SAP Multi-Bank ConnectivityEntry 2)CoCd: 3330PM: [Payt Mdm Format: AE_CGI_XML_CTHouse Bk: For example, IHB02Alternative Format Type:90 SAP Multi-Bank Connectivity | The alternative format Type is defined for subsidiary company code 1 & 2. |  |

#### Relevant Configuration Steps for Post Balance Sheet Reclassification

Purpose

In this activity, you assign G/L account for balance sheet reclassification of in-house banking.

Procedure

For more information, see the Define Reclassification Rules step in the Accounting and Financial Close - [J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58) test script.

For example, you can assign G/L accounts for Reclassification under Valuation Rule SBSR with step 0020 as following table.

|  |
| --- |
| Caution If the following customizing are not conducted, it is expected that during the Post B/S Reclassification job run you get an error message. We recommend customers to complete customizing steps for all valuation rule steps before conducting the reclassification. |

| Chart of Accounts | Target Account | Aging | Aging Increment | Source Account | Reclassification Method | Explanation |
| --- | --- | --- | --- | --- | --- | --- |
| YCOA | 12305000 | SGLOBRCL | CURRENT | 12305100 | Debit balance | Reclassification of Debit balance from long-term Receivables/Liabilities(IHB) account to Receivables affiliated companies (IHB) account |
| YCOA | 12305000 | SGLOBRCL | NONCURRENT | 12305100 | Debit balance | Reclassification of Debit balance from short-term Receivables/Liabilities(IHB) account to Receivables affiliated companies (IHB) account |
| YCOA | 21305000 | SGLOBRCL | CURRENT | 12305100 | Credit balance | Reclassification of Credit balance from long-term Receivables/Liabilities(IHB) account to Liabilities affiliated companies (IHB) account |
| YCOA | 21305000 | SGLOBRCL | NONCURRENT | 12305100 | Credit balance | Reclassification of Credit balance from short-term Receivables/Liabilities(IHB) account to Liabilities affiliated companies (IHB) account |

For example, you can assign G/L accounts for Reclassification under Valuation Rule SLBS with step 0020 as following table.

| Chart of Accounts | Target Account | Aging | Aging Increment | Source Account | Reclassification Method | Explanation |
| --- | --- | --- | --- | --- | --- | --- |
| YCOA | 12305000 | SGLOBRCL | CURRENT | 12305100 | Debit balance | Reclassification of Debit balance from long-term Receivables/Liabilities(IHB) account to Receivables affiliated companies (IHB) account |
| YCOA | 12305000 | SGLOBRCL | NONCURRENT | 12305100 | Debit balance | Reclassification of Debit balance from short-term Receivables/Liabilities(IHB) account to Receivables affiliated companies (IHB) account |
| YCOA | 21305000 | S3IRCL | LONGTERM | 12305100 | Credit balance | Reclassification of Credit balance from long-term Receivables/Liabilities(IHB) account to Liabilities affiliated companies (IHB) account |
| YCOA | 21305000 | S3IRCL | MIDTERM | 12305100 | Credit balance | Reclassification of Credit balance from mid-term Receivables/Liabilities(IHB) account to Liabilities affiliated companies (IHB) account |
| YCOA | 21305000 | S3IRCL | SHORTTERM | 12305100 | Credit balance | Reclassification of Credit balance from short-term Receivables/Liabilities(IHB) account to Liabilities affiliated companies (IHB) account |

#### Maintain Routing Setting

Use

In this activity, you maintain Routing Settings.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Multi-Bank Connectivity Connector | The Configuration Steps for the selected row display. |  |
| 6 | Configure | On the Maintain Routing Settings for Outbound Messages row, choose Configure. | The "Maintain Routing Settings for Out-bound Mess..": Change screen displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Maintain Routing Setting | Enter the following data and choose Save.Item 1)Sender Id: For example, 3340IHB01Note The sender ID here is used during the local routing of the subsidiary payment.To identify the source subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: <empty>Message Type: PAIN.001.001.03Origin: <empty>Routing: LOCALRoute Name: <empty>Item 2)Sender Id: For example, 3330IHB02Receiver ID: <empty>Note The sender ID here is used during the local routing of the subsidiary payment.To identify the source subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Message Type: PAIN.001.001.03Origin: <empty>Routing: LOCALRoute Name: <empty>Item 3)Sender Id: For example, AE/600310101Note The sender ID here is used during the local routing of the internal bank statement.To identify the source In-House Banking internal bank, the sender ID must be the bank key in the corresponding bank master data created per bank area. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: 3340IHB01Note The receiver ID here is used during the local routing of the internal bank statement.To identify the target subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Message Type: CAMT.053.001.02Origin: <empty>Routing: LOCALRoute Name: <empty>Item 4)Sender Id: For example, AE/600310101Note The sender ID here is used during the local routing of the internal bank statement.To identify the source In-House Banking internal bank, the sender ID must be the bank key in the corresponding bank master data created per bank area. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: 3330IHB02Note The receiver ID here is used during the local routing of the internal bank statement.To identify the target subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Message Type: CAMT.053.001.02Origin: <empty>Routing: LOCALRoute Name: <empty>Item 5)Sender Id: BAMReceiver ID: APMIHBMessage Type: ACMT.007.001.04Origin: BAMRouting: LOCALItem 6)Sender Id: APMIHBReceiver ID: BAMMessage Type: ACMT.010.001.03Origin: PFRouting: LOCALItem 7)Sender Id: APMIHBReceiver ID: BAMMessage Type: ACMT.014.001.04Origin: PFRouting: LOCAL | The routing setting is maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Select Customizing Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Routing Settings for Outbound Messages.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Maintain Routing Settings for Out-bound Mess..": Change screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Maintain Routing Setting | Enter the following data and choose Save.Item 1)Sender Id: For example, 3340IHB01Note The sender ID here is used during the local routing of the subsidiary payment.To identify the source subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: <empty>Message Type: PAIN.001.001.03Origin: <empty>Routing: LOCALRoute Name: <empty>Item 2)Sender Id: For example, 3330IHB02Note The sender ID here is used during the local routing of the subsidiary payment.To identify the source subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: <empty>Message Type: PAIN.001.001.03Origin: <empty>Routing: LOCALRoute Name: <empty>Item 3)Sender Id: For example, AE/600310101Note The sender ID here is used during the local routing of the internal bank statement.To identify the source In-House Banking internal bank, the sender ID must be the bank key in the corresponding bank master data created per bank area. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: 3340IHB01Note The receiver ID here is used during the local routing of the internal bank statement.To identify the target subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Message Type: CAMT.053.001.02Origin: <empty>Routing: LOCALRoute Name: <empty>Item 4)Sender Id: For example, AE/600310101Note The sender ID here is used during the local routing of the internal bank statement.To identify the source In-House Banking internal bank, the sender ID must be the bank key in the corresponding bank master data created per bank area. For more details, refer to test procedure Manage Banks and House Banks.Receiver ID: 3330IHB02Note The receiver ID here is used during the local routing of the internal bank statement.To identify the target subsidiary, the sender ID must be the customer number maintained in the corresponding house bank master data. For more details, refer to test procedure Manage Banks and House Banks.Message Type: CAMT.053.001.02Origin: <empty>Routing: LOCALRoute Name: <empty>Item 5)Sender Id: BAMReceiver ID: APMIHBMessage Type: ACMT.007.001.04Origin: BAMRouting: LOCALItem 6)Sender Id: APMIHBReceiver ID: BAMMessage Type: ACMT.010.001.03Origin: PFRouting: LOCALItem 7)Sender Id: APMIHBReceiver ID: BAMMessage Type: ACMT.014.001.04Origin: PFRouting: LOCAL | The routing setting is maintained. |  |

#### Maintain Multi-Bank Connectivity Connector Outbound Settings

Use

In this activity, you maintain Multi-Bank Connectivity Connector Outbound Setting.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Advanced Payment Management. | The Configuration Steps for the selected row display. |  |
| 6 | Configure | On the Maintain Multi-Bank Connectivity Connector Outbound Settings row, choose Configure. | The Change View “Maintain Multi-Bank Connectivity Connector..": … screen displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Maintain Multi-Bank Connectivity Connector Outbound Setting | Enter the following data and choose Save.Entry OneFormat: /CMT053_02Medium: /MBCChannel: /CUSTOMDirection: OUTNote The fields relating to converter: Format, Media, Channel and Direction are combined together to identify a converter. Do not manually populate the Direction, instead you can use search help of Format, Media or Channel to identify a converter. After you select an entry from the search help list, the direction field will be automatically populated.Message Identifier: /ISO_CAMT.053.001.02Message Type: CAMT.053.001.02Entry TwoFormat: /MT940Medium: /MBCChannel: /CUSTOMDirection: OUTMessage Identifier: /SWIFT_MT940Message Type: SWIFT_MT940 | The outbound setting is maintained. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Select Customizing Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Multi-Bank Connectivity Connector Outbound Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View “Maintain Multi-Bank Connectivity Connector..": … screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Maintain Multi-Bank Connectivity Connector Outbound Setting | Enter the following data and choose Save.Entry OneFormat: /CMT053_02Medium: /MBCChannel: /CUSTOMDirection: OUTNote The fields relating to converter: Format, Media, Channel and Direction are combined together to identify a converter. Do not manually populate the Direction, instead you can use search help of Format, Media or Channel to identify a converter. After you select an entry from the search help list, the direction field will be automatically populated.Message Identifier: /ISO_CAMT.053.001.02Message Type: CAMT.053.001.02Entry TwoFormat: /MT940Medium: /MBCChannel: /CUSTOMDirection: OUTMessage Identifier: /SWIFT_MT940Message Type: SWIFT_MT940 | The outbound setting is maintained. |  |

#### Define Parameter Sets

Use

In this activity, you define parameter sets.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution. |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Bank Accounting | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Electronic Bank Statement. | The Configuration Steps for the selected row display. |  |
| 6 | Define Parameter Sets | On the Define Parameter Sets row, choose Configure. | The “Define Parameter Sets”:Change screen displays. |  |
| 7 | New Entries | Choose New Entries and make the following entries:Parameter Set ID: ZPF1CAMT053Parameter Set Name: <parameter set name>Posting Method: 2 Import and Post Bank AccountingAss.Val.Dte to Acct: <selected>Summarization: <deselected>ZeroSales Permitted: <deselected> | The parameter sets is defined. |  |
| 8 | Save | Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Maintain Routing Settings | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Parameter Sets.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The “Define Parameter Sets”:Change screen displays. |  |
| 3 | Define Parameter Sets | On the Define Parameter Sets row, choose Configure. | The “Define Parameter Sets”:Change screen displays. |  |
| 4 | New Entries | Choose New Entries and make the following entries:Parameter Set ID: ZPF1CAMT053Parameter Set Name: <parameter set name>Posting Method: 2 Import and Post Bank AccountingAss.Val.Dte to Acct: <selected>Summarization: <deselected>ZeroSales Permitted: <deselected> | The parameter sets is defined. |  |
| 5 | Save | Choose Save. |  |  |

#### Manage Teams and Responsibilities for Approver

##### Manage Teams and Responsibility for In-House Banking Account Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management- [1NJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1NJ) test script with the following information:

Team Information tab:

Team Name: In-House Banking Account Approver

Global ID: FSCM_IHB_A

Description: In-House Banking Account Approver Team

Team Status: Enabled

Type: SFSCM_IHB_A (In-House Banking Account Approver)

Responsibility Definition tab:

IHBBankArea: <empty>

If fields are empty, the team is responsible for all company codes.

Team Members tab:

Business Partner: <user ID>, for example, Payment Specialist - In-House Banking

Functions: SFSCMIHBA (In-House Banking Account Approver)

To display the connection between the business partner, Payment Specialist - In-House Banking, and user ID, see the search help. Generic users are described in the Last Name field.

##### Manage Teams and Responsibility for In-House Banking Condition Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management- [1NJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1NJ) test script with the following information:

Team Information tab:

Team Name: In-House Banking Condition Approver

Global ID: FSCM_IHB_C

Description: In-House Banking Condition Approver Team

Team Status: Enabled

Type: SFSCM_IHB_C (In-House Banking Condition Approver)

Responsibility Definition tab:

IHB Bank Area: <empty>

If fields are empty, the team is responsible for all company codes.

Team Members tab:

Business Partner: <user ID>, for example, Payment Specialist - In-House Banking

Functions: SFSCMIHBC (In-House Banking Condition Approver)

To display the connection between the business partner, Payment Specialist - In-House Banking, and user ID, see the search help. Generic users are described in the Last Name field.

##### Manage Teams and Responsibility for In-House Banking Limit Approver

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a team to specify responsibilities for the review process.

Procedure

Execute the Manage Teams and Responsibilities steps in the Responsibility Management - [1NJ](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1NJ) test script with the following information:

Team Information tab:

Team Name: In-House Banking Limit Approver

Global ID: FSCM_IHB_L

Description: In-House Banking Limit Approver Team

Team Status: Enabled

Type: SFSCM_IHB_L (In-House Banking Limit Approver)

Responsibility Definition tab:

IHB Bank Area: <empty>

If fields are empty, the team is responsible for all company codes.

Team Members tab:

Business Partner: <user ID>, for example, Payment Specialist - In-House Banking

Functions: SFSCMIHBL (In-House Banking Limit Approver)

To display the connection between the business partner, Payment Specialist - In-House Banking, and user ID, see the search help. Generic users are described in the Last Name field.

#### Manage In-House Bank Workflow (Option)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes the approach to begin the In-house bank management workflow process.

Prerequisite

The Teams need to be created in the Manage Teams and Responsibilities (F2412) app in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Workflow (F6131). | The Manage Workflows view displays. |  |
| 3 | Create Workflow Template | On the current page, choose Create.Workflow Name: IHB_TeamIn the Start Conditions tab, make the following entries:Only start the workflow if all of the following preconditions are met: NoneThis field is used to define preconditions to trigger workflow process.Choose the Steps tab and choose Create. |  |  |
| 4 | Enter Criteria | In the New Step dialog box, in the Header section, make the following entries:Step Name: IHB Manage workflow request ProcessStep Type: Dialog Approval StepIn the Recipients section, make the following entry:Role: for example, In-House Banking Account ApproverStep to be completed by: <Choose One of the recipients>Choose Create.Choose Save. | Workflow successfully created notification appears and the Workflow Details view displays. |  |
| 5 | Activate the Workflow Template | Choose Activate on the top right of the view. | Workflow is activated successfully and the Manage Workflow view displays. |  |
| 6 | Adjust the Order | On the Workflow template list page, choose Define Order.On the Define Order dialog box, select the newly created workflow and choose the Moves the selected workflow to the top icon and Save. | Order is saved successfully. |  |

#### Manage Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create cost centers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - Old Version (F1443A). | The Manage Cost Centers screen displays. |  |
| 3 | Select Existing Cost Center | Make the following entries and choose Go.Cost Center: for example, 33101101 |  |  |
| 4 | Copy Cost Center | Select the cost center, and choose Copy. |  |  |
| 5 | Create New Cost Center | Make the following entries and choose Create.Cost Center: for example, 33401101Company Code: for example, 3340 | The new cost center under subsidiary 1 is created. |  |
| 6 | Create New Cost Center Under Subsidiary 2 | Repeat step 2-5, create new cost center under subsidiary 2.Cost Center: for example, 33301101Company Code: for example, 3330 | The new cost center under subsidiary 2 is created. |  |

## Overview Table

This scope item consists of several procedures provided in the tables below.

Master Data

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create/Extend Business Partners Representing Subsidiary Company Code](#unique_9) [page ] 11 |  |  | Business partners representing subsidiaries companies are created/ extended. |
| [Create Business Partners Representing Subsidiary Company Code](#unique_10) [page ] 12 | Master Data Specialist - Business Partner Data | Manage Business Partner Master Data (F3163) | Business partners representing subsidiaries companies are created. |
| [Extend Business Partners as IHB Account Holder and Inhouse Bank Area Owner](#unique_11) [page ] 14 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Business partners are extended as IHB account holder. |
| [Manage Cost Center](#unique_23) [page ] 42 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | You create cost centers. |
| [Manage Banks and House Banks](#unique_6) [page ] 16 |  |  | You create a bank key as in-house bank center and also create the house banks. |
| [Create In-House Banking](#unique_25) [page ] 49 | Payment Specialist - In-House Banking | Manage In-House Bank Accounts (F5942) | In-House bank accounts are created. |
| [Activate In-House Bank Accounts](#unique_26) [page ] 54 | Payment Specialist - In-House Banking | Manage In-House Bank Accounts (F5942) | In-House bank accounts are activated. |
| [Download In-House Bank Accounts](#unique_27) [page ] 54 | Payment Specialist - In-House Banking | Manage In-House Bank Accounts (F5942) | You download In-House bank accounts for Bank Account Management. |
| [Validate XML file](#unique_28) [page ] 56 |  |  | The XML file is validated. |
| [Import Bank Accounts](#unique_29) [page ] 57 |  |  | Bank accounts are imported. |
| [Maintain Bank Accounts](#unique_30) [page ] 58 |  |  | Bank accounts are created. |
| [Manage In-House Bank Conditions](#unique_31) [page ] 60 | Payment Specialist - In-House Banking | Manage In-House Bank Conditions (F5941) | Interest conditions are defined. |
| [Manage In-House Bank Limits](#unique_32) [page ] 62 | Payment Specialist - In-House Banking | Manage In-House Bank Limits (F5940) | You define a limit for your in-house bank accounts. |
| [Maintain Payment Transaction for Business Partner](#unique_33) [page ] 64 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Payment transaction for business partner is maintained. |

Payments on Behalf

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Payment Agreements](#unique_34) [page ] 66 | Payment Specialist | Manage Payment Agreements (F4629) | You maintain payment agreements. |
| [Subsidiary 1: Create Vendor Invoice](#unique_35) [page ] 68 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | You manually create a vendor invoice. |
| [Subsidiary 1: Payment Run](#unique_36) [page ] 69 | Accounts Payable Accountant | Manage Automatic Payments (F0770) Revise Payment Proposals (F0771) Schedule Accounts Payable Jobs (F2257) Display Payment Lists (S_P99_41000099) | Posting payments use the automatic payment program. |
| [Monitor MBC Message (with Payment File)](#unique_37) [page ] 70 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | You investigate that MBC has routed the payment file into advanced payment management. |
| [Process Payment in Advanced Payment Management](#unique_38) [page ] 71 | Payment Specialist | Manage Payments (F3647) | An incoming payment order is be manually processed. |
| [Check Payment Order](#unique_39) [page ] 72 | Payment Specialist | Manage Payments (F3647) | You check outgoing payment order. |
| [Manage In-House Bank Account Balances](#unique_40) [page ] 73 | Payment Specialist - In-House Banking | Manage In-House Bank Account Balances (F6341) | You can check In-House Account Balances. |
| [Approve Payment Batch (Optional)](#unique_41) [page ] 73 |  |  | You approve payment batch. |
| [Monitor MBC Message (with Payment File)](#unique_42) [page ] 74 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | The payment file/bank statement is sent from head office to external business partner’s bank. |

Intercompany Payments

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Subsidiary 1: Create Customer Invoice](#unique_43) [page ] 76 | Accounts Receivable Accountant | Create Outgoing Invoices (FB70) | An invoice for customer representing subsidiary company code 1 is created manually. |
| [Subsidiary 2: Create Vendor Invoice](#unique_44) [page ] 77 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | An invoice for vendor reprensting subsidiary company code 2 is created manually. |
| [Subsidiary 2: Payment Run](#unique_45) [page ] 78 |  |  | Posting payments uses the automatic payment program. |
| [Monitor MBC Message (with Payment File)](#unique_46) [page ] 79 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | You investigate that MBC has routed the payment file into advanced payment management. |
| [Process Payment in Advanced Payment Management](#unique_47) [page ] 80 | Payment Specialist | Manage Payments (F3647) | An inbound payment order is manually processed. |
| [Check Payment Order](#unique_48) [page ] 81 | Payment Specialist | Manage Payments (F3647) | You can check payment order. |
| [Manage In-House Bank Account Balances](#unique_49) [page ] 82 | Payment Specialist - In-House Banking | Manage In-House Bank Account Balances (F6341) | You can check In-House Account Balances. |

Central Incoming Payments

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Service Level Agreements](#unique_50) [page ] 83 | Payment Specialist | Manage Service Level Agreements (F6183A) | You create Service Level Agreements. |
| [Import External Bank Statement](#unique_51) [page ] 87 | Cash Management Specialist | Manage Bank Statements (F1564) | External bank statement is uploaded. |
| [Process Payment in Advanced Payment Management](#unique_52) [page ] 90 | Payment Specialist | Manage Payments (F3647) | An inbound payment order is manually processed. |
| [Manage In-House Bank Account Balances](#unique_53) [page ] 91 | Payment Specialist - In-House Banking | Manage In-House Bank Application Jobs (F6653) | You manage In-House Account Balances. |

End of Day Processing

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Exchange Rates](#unique_54) [page ] 92 | General Ledger Accountant | Import Foreign Exchange Rates (F2092) | You update exchange rates. |
| [Manage In-House Bank Application Jobs](#unique_55) [page ] 95 | Payment Specialist - In-House Banking | Manage In-House Bank Application Jobs (F6653) | You execute all steps for end of day process. |
| [Manage In-House Bank End of Day](#unique_56) [page ] 99 | Payment Specialist - In-House Banking | Manage In-House Bank End of Day (F6338) | You monitor the end of day processes. |
| [Manage In-House Bank Account Balances](#unique_57) [page ] 100 | Payment Specialist - In-House Banking | Manage In-House Bank Account Balances (F6341) | The bank statements are generated for your accounts and the settlement payment items are posted and have the detailed for the included bank statement. |
| [Monitor MBC Message (with Payment File)](#unique_58) [page ] 102 | Business Integration Specialist - Bank Integration | Manage Bank Messages (F4385) | You monitor the CAMT.053 messages transmitted out of S/4HANA via MBC. |

Table 2:

|  |  |  |  |
| --- | --- | --- | --- |
| [Post B/S Reclassification](#unique_59) [page ] 103 | General Ledger Accountant | Schedule General Ledger Accounting Jobs (F1927) | You post the balance sheet reclassification for in-house bank. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Initialize In-House Banking End of Day Processing Dates

Purpose

In this step, you initialize In-House Banking end of day processing dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Application Jobs (F6653). |  |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: In-House Bank - EOD Jobs (Only Date Jobs)Job Name: for example：In-House Bank - EOD Jobs (Only Date Jobs) | The New Job: In-House Bank-EOD Jobs (Only Date Jobs) view displays. |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entries:Start Immediately: <Selected or deselected>If you choose start immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: <Calendar>Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Set Posting Date - Parameter Section (Step 1) | Choose Step 3. In the Parameter section, make the following entries and choose > to next parameter step:Bank Area: for example, SIAE | Parameter for setting posting date is maintained.Note You set the posting date whereby all subsequent payment transaction postings are entered with the subsequent dates (dependent on the business day as defined in the factory calendar). |  |
| 7 | Set Closing Date - Parameter Section (Step 2) | Make the following entries:Bank Area: for example, SIAE | Parameter for setting closing date is maintained. |  |

### Set Up In-House Bank Accounts

#### Create In-House Bank Accounts

##### Create Directly (Option 1)

###### Create In-House Banking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create In-House bank accounts.

Prerequisite

The In-House Account holder role has been created for business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Accounts (F5942). | The Manage In-House Bank Accounts screen displays. |  |
| 3 | Create In-House Bank Account for Subsidiary 1 | Choose Create. On the Create popup screen, make the following entries and choose Continue.Bank Area: for example, SIAECurrency: for example, AEDBusiness Partner: for example, 33403340Opening Date: <current date>Account Template: <empty> | The In-House Bank Account screen displays. |  |
| 4 | Maintain Details | Make the following entries:Make a note of the number for In-House bank account: __________ .General Information section:Account Description: In-house banking account for subsidiary 1Account Alias: <empty>Account Holder: for example, 33403340Account Options section:Account Balance Needed: <Selected>Account Balancing Frequency: for example, MonthlyBalance Notification Needed: <selected>Interest Scale Notification Needed: <selected>Bank Statement Needed: <selected>Account Balancing section:Account Balancing Frequency: for example: MonthlyAccount Balancing Key Day: for example, 01Next Account Balancing Date: <keep default>Withholding Tax: <Deselected>Balance Notification section:In Recipients subsection, choose Add to add new entry.Business Partner: for example, 33403340Output Format Id: SETTMLEmail Address: <email address>Note If balanced notification is selected, the account holder will get a PDF of this notification via email.Interest Scale Notification section:In Recipients subsection, choose Add to add a new entry.Business Partner: for example, 33403340Output Format Id: INTMLEmail Address: <email address>Note If interest scale notification is selected, the account holder will get a PDF of this notification via email.Bank Statement section:Bank Statements Frequency: for example, 1 DailyBank Statement Within Day: <selected>Timezone: for example CETFrom time: for example 7:00To time: for example 22:00In Recipients subsection, choose Add to add new entry:Entry 1) with format PDFBusiness Partner: for example, 33403340Output Format Id: STMTMLEmail Address: <email address>Original: <Deselected>Send With Alias: <Deselected>Note The account holder will get a PDF of bank statement via email.Note If the account holder wants to get a camt.053 message of bank statement via email, output format Id CMT53E can be used.Entry 2) Interface MBC distribution methodBusiness Partner: for example, 33403340Output Format Id: CMT53MOriginal: <selected>Send With Alias: <Deselected> | The In-house bank account is created with status In review.Note SettlementAccount settlement is a period process that takes places during the end-of-day processing. On account level, you define the frequency and the key date for the settlement run. The frequency can be defined on a monthly, quarterly, or yearly basis. The periodic job is executed each day and considers all accounts where the key data has reached. For these accounts, the settlement takes place.Bank statementThis can be prepared in an electronic file or via a PDF format. Maintain the settings during the account maintenance. You can enter several recipients for a bank statement. One document is marked as original and all the other recipients will get a copy of the same statement in the defined format for each recipient. On the account maintenance, you define the frequency (daily, weekly, monthly, quarterly, yearly) and the key date or some frequencies. During the day, the processing of regular bank statements is also possible. If you select bank statements on a daily basis, you can generate bank statements during the day as well. Otherwise the statements within a day will not be generated. If you select the electronic format, the bank statement generates a CAM.053 message. Further formats not yet available. A parameter to generate bank statements with no items is possible as well.NotificationsThree types of PDF notifications are available within in-house banking. The first two are the balance notification and interest scale notification. These notifications show details of the account settlement and can be created after the settlement of an account has taken place.The third notification is the bank statement notification that can be generated as a PDF file instead of an electronic file for the recipients.An example for each type is provided and a customer-specific version can be defined. |  |
| 5 | Save | Choose Save. | The In-house Bank account, for example, 1 is created with status In review. |  |
| 6 | Create In-House Bank Account for Subsidiary 2 | Repeat step 3-5, create In-House Bank account for subsidiary 2 as following:Description: In-house banking account for subsidiary 2Account Alias: <empty>Account Holder: for example, 33403330Business Partner: for example, 33403330Note Other fields are same as subsidiary 1. | The In-House Bank account, for example, 2 is created for subsidiary 2. |  |
| 7 | Create Additional In-House Bank Account for Subsidiary 1 | Repeat step 3-5, create In-House Bank account to close sub 1. | The In-house Bank account, for example, 3 is created. |  |
| 8 | Create Additional In-House Bank Account for Subsidiary 2 | Repeat step 6, create In-House Bank account to close sub 2. | The In-house Bank account, for example, 4 is created. |  |

###### Activate In-House Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you activate In-House bank accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage In-House Bank Accounts (F5942). | The Manage In-House Bank Accounts screen displays. |  |
| 3 | Select In-House Bank account | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: noted in the previous stepAccount Holder: for example, 33403340 and 33403330 | The In-House Bank Accounts list displays. |  |
| 4 | Select | Select the checkbox for one or more In-house bank accounts from list. |  |  |
| 5 | Submit | Choose Active. | If the dual control is not active the status changed directly to Active. |  |

###### Download In-House Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download In-House bank accounts for Bank Account Management. This file is required for a later process step.

Prerequisite

The In-House Account has been created.

The PartnerCompany code has been maintained in the relevant business partner in step [Extend Business Partners as IHB Account Holder and Inhouse Bank Area Owner](#unique_11) [page ] 14.

The house bank accounts has been created for the in-house bank in step [Manage Banks and House Banks](#unique_6) [page ] 16.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage In-House Bank Accounts (F5942). | The Manage In-House Bank Accounts screen displays. |  |
| 3 | Search | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: noted in previous stepAccount Holder: for example, 33403340 and 33403330 | The In-House bank accounts are listed . |  |
| 4 | Download IHB Accounts | Select the checkbox for both In-House Bank accounts, choose Download Accounts.Note down the XML file name, for example IHB_DATA_DOWNLOAD_FOR_BAM.xml. | Both In-house bank accounts are downloaded and the file is saved on your local PC. We will upload this file in the further step Import Bank Account |  |

###### Validate XML file

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you validate the XML file.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Find local XML file | Find the XML file downloaded in previous step on your local PC.For example: file name IHB_DATA_DOWNLOAD_FOR_BAM.xml. |  |  |
| 2 | Check XML file via Excel | Open the XML file with Excel.Look that all expected information of your in-house bank account is in the file. The required company code must be the same as for the subsidiary that owns these accounts.For example:In sheet General_Additional_Data_SetBUKRS: 3340 or 3330In sheet Connectivity PathBUKRS: 3340 or 3330HBKID: IHB01 or IHB02HKTID: <In-House Bank account number> | Both In-House bank accounts are listed in excel. |  |
| 3 | Maintain the In-House Bank Servicer | Maintain the In-House Bank Servicer for all in-house bank accounts in General_Additional_Data_Set.IHB_SERVICER: 33403310Note The In-House Bank Servicer is the BP as the role IHB200 Inhouse Bank Area Owner. The BP must be created in headquarter. Refer to test step [Create/Extend Business Partners Representing Subsidiary Company Code](#unique_9) [page ] 11 for the BP role extension. |  |  |
| 4 | Select Both Items | As you can see, in both sheets, only the first row is selected, and the background frame is blue. Please go to the last attribute and select all relevant rows with the small arrow in the right corner. You need do it for both sheets. |  |  |
| 5 | Export as XML file | In the Excel file, choose the excel’s menu Developer, then choose Export. On the dialog box Export XML, make the following entries and choose Export.File name: for example, IHB_DATA_DOWNLOAD_FOR_BAMSave as type: keep default value as XML Files.Note If the Developer tab does not exist in Excel, please add it manually.You can find the command in menu File > Options > Customize Ribbon > Choose commands from Main Tabs . | The file is saved on your local PC as XML file to upload it later at Bank Account Management.Note Make sure that both in-house bank accounts are included in your XML file. |  |

###### Import Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you import bank accounts.

Procedure

This procedure is mentioned in the Advanced Bank Account Management- [J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77) test script. You can refer to the Import Bank Accounts step and create bank account in Bank Account Management with the XML File validated in the previous step.

For example, if you have created both subsidiaries company code as 3340 & 3330 you can import following house bank for each subsidiary company code:

| Item | Company code | House Bank | Bank Account |
| --- | --- | --- | --- |
| Subsidiary 1 | 3340 | IHB01 | <In-House Bank account> |
| Subsidiary 2 | 3330 | IHB02 | <In-House Bank account> |

|  |
| --- |
| Note After bank accounts import, the bank accounts will be activated directly. Do not change the account number, keep it the same as the automatically generated In-House Bank account number. |

###### Maintain Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain bank accounts.

Prerequisite

The In-House Account has been uploaded successfully in Bank Account Management.

Procedure

This procedure is mentioned in the Advanced Bank Account Management- [J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77) test script. You can refer to the Create Bank Account step and create House Bank Account Connectivity.

|  |
| --- |
| Note After bank accounts import, the bank account connectivity will be created. Do not change the house bank account, keep it the same as the automatically generated In-House Bank account number. |

For example, if you have created both subsidiaries company code as 3340 & 3330, you can create following house bank for each subsidiary company code.

|  |
| --- |
| Note Do not maintain IBAN for both bank accounts. |

| Item | Company code | House Bank | IBAN | Bank Account | Pmnt Tran Type Group | G/L Account | Customer number |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Subsidiary 1 | 3340 | IHB01 | Maintain IBAN for SEPA counties. However, do not maintain IBAN for non-SEPA countries. You can choose Generate IBAN in Manage Bank Accounts to automatically generate the IBAN. | <number of house bank account> | C053IHB (ISO XML Format CAMT.053 In-House Bank) | 11001000 | 3340IHB01 |
| Subsidiary 2 | 3330 | IHB02 | Maintain IBAN for SEPA counties. However, do not maintain IBAN for non-SEPA countries. You can choose Generate IBAN in Manage Bank Accounts to automatically generate the IBAN. | <number of house bank account> | C053IHB (ISO XML Format CAMT.053 In-House Bank) | 11001000 | 3330IHB02 |

##### Create via eBAM Integration (Option 2)

Purpose

In this activity, you define In-House Bank accounts in Bank Relationship Management.

Prerequisite

The local routings for eBAM integration are maintained in preliminary step [Maintain Routing Setting](#unique_12) [page ] 28.

You assign business roles to business user in Fiori App Maintain Business Users (F1303).

For example, the role PAYMENT_SPECIALIST, BANK_INT_SPECIALIST and PAYM_SPEICIALIST_IHB are assigned to example user CASH_SPECIALIST which is used to create bank accounts.

Procedure

Refer to test step Create Bank Account with Bank Correspondence in Advanced Bank Account Management- [J77](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J77) test script for more details. After an Account Opening Request message with message type ACMT.007.001.04 is routed via MBC into In-House Banking, an In-House Banking account will be created automatically, an Account Request Acknowledgement message with message type ACMT.010.001.03, and an Account Report message with message type ACMT.014.001.04 will be routed via MBC into Bank Relationship Management.

#### Manage In-House Bank Conditions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define interest conditions.

For the settlement testcases it is necessary that the interest conditions are defined and linked to your accounts. Via the app Manage In-House Bank Conditions you have the capability to define conditions on three different levels. You can define conditions on bank area level and all accounts within this level get the defined accounts. You can define a group and link accounts to that group or you define the conditions on single account level. If you define all three levels an account can, be only part of one level and the first level that is checked is the single level, then the group level and at least the bank area level. The valid period of the account in a single or group level can’t be overlapping.

|  |
| --- |
| Note If you make a change on conditions with a valid from date in the past and the period has been already settled, the changes are back dated changes. The existing account settlement results will be corrected as below:All postings related to the existing account settlement are reversed (with an offset posting on the relevant in-house bank account) and the new generated settlement amounts are posted.The corrected amounts are posted with the current bank area posting date, but value date is the value date of the original settlement date. |

Prerequisite

If you want to use Reference Interest Rate, you make sure the reference interest rate has been entered in the Market Rates Management – Manually via Upload - [1XN](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/1XN).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage In-House Bank Conditions (F5941). | The Financial Conditions screen displays. |  |
| 3 | Create Condition | Choose Create. On the Create Financial Condition popup screen, make the following entries and choose Continue.Bank Area: for example, SIAELevel: for example, Bank Area |  |  |
| 4 | Create Condition for Credit | In the Condition section, choose Create. Make the following entries and choose Apply:Example 1:Interest Calculation: tabInterest type: CreditCurrency: AEDInterest Calculation Type: for example, Linear Interest CalculationInterest Calculation Method: for example: act/360Interest DetailsFixed Interest Rate %: <define a percentage between 0 – 10>Valid from: <today’s date>Valid to: <today’s date + at least 5 months>Note If you want to use Reference Interest Rate, please see example 2.Example 2: with Reference Interest RateInterest Calculation: tabInterest type: CreditInterest Calculation Type: for example: Average Compound Interest CalculationInterest Calculation Method: for example:act/360Interest DetailsReference Interest Rate: <choose via value help>Mark Up/Mark Down %: < define a percentage between 0 – 10>Calendar: <your calendar>Interest Adjustment Period: for example: 3Maximum %: for example: 9999Minimum %: for example: -9999 |  |  |
| 5 | Create Condition for Debit | Repeat step 4, create condition for Debit.Interest type is set as debit. |  |  |
| 6 | Create Condition for Overdraft | Repeat step 4, create condition for Overdraft.Interest type is set as Overdraft. |  |  |
| 5 | Apply | Choose Apply. |  |  |
| 6 | Create | Choose Create. | The condition is created with status In Review. |  |
| 7 | Activate | Choose Submit. | The condition is activated with status Active. |  |

#### Manage In-House Bank Limits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a limit for your in-house bank accounts.

For the overdraft testcases it is necessary that the account limits are defined and linked to your accounts. Via the app Manage In-House Bank Limits you have the capability to define limits on two different levels. You can define a group and link accounts to that group or you define the limit on single account level. If you define all levels an account can, be only part of one level at any time and the first level that is checked is the single level, then the group level. The valid period of the account in a single or group level can’t be overlapping.

|  |
| --- |
| Note If you make a change on conditions with a valid from date in the past and the period has been already settled, the changes are back dated changes. The existing account settlement results will be corrected as below:All postings related to the existing account settlement are reversed (with an offset posting on the relevant in-house bank account) and the new generated settlement amounts are posted.The corrected amounts are posted with the current bank area posting date, but value date is the value date of the original settlement date. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Payment Specialist - In-House Banking. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Limits (F5940). | The IHB Account Limit screen displays. |  |
| 3 | Create Limit | Choose Create. On the Create Limit popup screen, make the following entries and choose Continue.Bank Area: for example, SIAELevel: for example, SingleNote If you want to create a group condition you have to click at first on Create Group.IHB Account Number: <the IHB account created in previous step> |  |  |
| 4 | Create Limit | In the Account Limits section, choose Create. Make the following entries :Account Limit Details:Account Limit: for example, -500.00Note A positive limit can be entered as well. Then the limit breaches if the account balances go under the defined positive limit.Currency: <same currency as the account>Basic DataValid from: <today’s date>Valid to: <today’s date + at least 5 months> |  |  |
| 5 | Apply | Choose Apply. |  |  |
| 6 | Create | Choose Create. | The limit is created with status In Review. |  |
| 7 | Activate | Choose Submit. | The limit is activated with status Active. |  |
| 8 | Create for other IHB Account | Repeat step 3-7 to create limit for all of your created IHB accounts. |  |  |

#### Maintain Payment Transaction for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you maintain payment transaction for business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Find Business Partner | Make the following entries and choose Enter:Business Partner: for example, 33403340 | The Display Organization:XXXXXXXX displays. |  |
| 4 | Change | Choose Switch Between Display and Change. | The Change Organization:XXXXXXXX displays. |  |
| 5 | Maintain Payment Transaction for subsidiary 1 | Choose Payment Transactions Tab. Make the following entries and choose Save.ID 0001 (External Bank)ID: for example, 0001C/R: AEBank Key: 18121976ID 0002 (IHB Bank Account)ID: for example, 0002C/R: AEBank Key: #600310101Bank Account: <the IHB account created in the previous step>IBAN: <empty>Note For In-House Bank account, do not maintain IBAN. | Bank details is maintained for the business partner. |  |
| 6 | Maintain Payment Transaction for subsidiary 2 | Repeat step 2-5, maintain bank details for business partner 33403330 with following details..ID 0001 (External Bank)ID: for example, 0001C/R: AEBank Key: 18121976ID 0002 (IHB Bank Account)ID: for example, 0002C/R: AEBank Key: #600310101Bank Account: <the IHB account created in the previous step>IBAN: <empty> |  |  |

### Payments on Behalf

#### Maintain Payment Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain payment agreements.

Procedure

For more information, see the Maintain Payment Agreement step in the Advanced Payment Management- [4MT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4MT) test script.

For example, you can use following data to create payment agreement:

| Field | Value |
| --- | --- |
| Create Agreement |  |
| Agreement ID | IHB_POBO_ AE |
| Description | IHB payment on behalf of AE |
| Company Code | 33 10 |
| Calendar ID | 01 |
| Processing Option | I |
| Batching | Undefined-Default Logic |
| Converter ID | BANK outbound MBC (MBDMEO) |
| Format Tree | CGI: DMEE XML Format as per ISO20022 (CGI_XML_CT)Note Make sure the XML format is defined in DMEE outbound setting for MBC connector. You can refer to the procedure Maintain DMEE Outbound Settings for MBC Connector in scope item [4MT](https://rapid.sap.com/bp/#/scopeitems/4MT) Advanced Payment Management. |
| Bank Details section |  |
| Account Number | For example, 0000000693123456 or 0000000693123456Note The account number must exist in the company code of the payment. You can check within app Manage Bank Accounts. |
| Create Payment Rule for Payment Agreement |  |
| Description | Payment Rule for POBO_AE |
| Condition 1 for payment rule |  |
| Characteristic | Item Category (PI_KIND) |
| Inclusive/exclusive | Inclusive(I) |
| Option | Equal to (EQ) |
| Value Low | 02 |
| Value High | <empty> |
| Condition 2 for payment rule |  |
| Characteristic | PI Bnk Ctry/Reg (COUNTRY) |
| Inclusive/exclusive | Inclusive(I) |
| Option | Equal to (EQ) |
| Value Low | AE |
| Value High | <empty> |

#### Subsidiary 1: Create Vendor Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manually create a vendor invoice.

Procedure

This procedure is mentioned in the Accounts Payable- [J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60) test script. You can refer to the Invoice Entry Without Purchase Orders step and create vendor invoice. Note down the invoice document number.

For example, you can use following data to create a vendor invoice for subsidiary 1 company code 3340 :

| Field | Value |
| --- | --- |
| Basic Data Section |  |
| Company code | 3340 |
| Vendor/Invoicing Party | 33300001 |
| Partner BankType | <external bank account maintained in business partner> |
| Gross Invoice Amount | <Gross Invoice Amount> |
| Invoice Date | <Current date> |
| Posting Date | <Current date> |
| Reference | <any value> |
| G/L Account Items Section |  |
| Offsetting expense GL account | For example, 61400000 |
| Tax Code | <Tax code> |
| Cost Center | 33401101 |
| Payment Section |  |
| Payment Method | In-House Banking Payment |

#### Subsidiary 1: Payment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes posting payments using the automatic payment program.

Prerequisite

You assign business roles to business user in Fiori App Maintain Business Users (F1303).

For example, the role PAYMENT_SPECIALIST. BANK_INT_SPECIALISTand PAYM_SPEICIALIST_IHB are assigned to example user AP_ACCOUNTANT which is used to execute payment run.

Procedure

This procedure is mentioned in the Accounts Payable- [J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60) test script. You can refer to the Payment Run step. Note down the document number.

#### Monitor MBC Message (with Payment File)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you investigate that MBC has routed the payment file into advanced payment management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go:Message Type: PAIN.001.001.03Create Date: For example, <today’s date>Sender ID: for example, 3340IHB01 | The MBC messages are displayed in respective tabs.Note There must be an Outbound and Inbound message with a PAIN.001.001.03 file with the Sender ID 3340IHB01. |  |
| 4 | Check incoming Message | Choose Incoming Messages tab, select the inbound message, choose >. | Details screen of message displays. |  |
| 5 | Display Message Content | Choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 6 | Navigation to Application Log | Choose Log in the detail screen of message. | The detail log of the message processing is listed. |  |

#### Process Payment in Advanced Payment Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incoming payment order can be manually processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Find Payment Order | Make the following entries and choose Go.Clearing Area: Payment Factory Default Configuration (PF) | Payment Orders is listed |  |
| 4 | Go to Details | Select your payment order, choose >. | The payment order is listed in details. |  |
| 5 | Process Payment Order | On the Payment Order screen, choose Process.Note If the incoming order is automatically processed successfully, you can skip this step. | The payment order is processed. The outgoing payment order should be generated and processed. |  |

#### Check Payment Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check outgoing payment order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Find Payment Order | Make the following entries and choose Go.Clearing Area: PF | Payment Orders is listed |  |
| 4 | Go to Details | Select your payment order, choose > . | The detailed screen of the Outgoing Payment Order is displayed.Note If the payment does not need approval process, the process status should be Payment Medium Created.Note If the status is Pending Approval, a payment approval process is expected as per your approval settings and approvers maintained. For more details, please refer to test step Outgoing Payment with BCM Approval process in Advanced Cash Operations - [J78](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J78) test script. |  |
| 5 | Check G/L Document | In the Clearing Items tab, choose G/L Document: for example 1010/0100000059/2022 to navigate to Journal entries. | The FI posting is created as following:Debit: 11001400 Clearing account OBO payments (APM)Credit: 11001020 External clearing account. |  |

#### Approve Payment Batch (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you approve payment batch.

Procedure

For more information, see the (Partial) Approval / Reject by Approver step in the Advanced Payment Management- [4MT](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/4MT) test script.

Note: After the payment batch is approved by the final approver, the batch status is Payment Medium Created. The Payment file is created and the reference Number is generated.

#### Manage In-House Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check In-House Account Balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access App | Open Manage In-House Bank Account Balances (F6341). | The Manage In-House Bank Account Balances view displays. |  |
| 3 | Maintain Filter | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: <the IHB account created in previous step> |  |  |
| 4 | Go to Details | Expand the nodes, and select the lowest node for your bank account, choose > . | The bank account balances is listed in details. All payment items has reached the In-House Bank account. |  |

#### Monitor MBC Message (with Payment File)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The payment file/bank statement is sent from head office to external business partner’s bank. In this activity, you monitor the messages transmitted out of S/4HANA via MBC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and press Enter:Message Type: PAIN.001.001.03Creation Date: For example, <today’s date> | The MBC messages are displayed in respective tabs. |  |
| 4 | Display Message Content | Select the outgoing message and choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 5 | Navigation to Application Log | Select a message and choose Log in the detail screen of message. | The detail log of the message processing is listed. |  |

#### Manage Returned Payment (Optional)

Purpose

In-house banking acts like an external house bank for its subsidiaries and holds current accounts for them. In this activity, In-House Banking identifies and handles payment returns during the import and posting of the external bank statement that have their origin in payments on behalf. A return automatically creates a versal posting on the relevant in-house bank account (by a off set posting).

### Intercompany Payments

Purpose

The following process is for the intercompany payments between two subsidiaries that hold the In-House Banking account in the same bank area.

If the intercompany payments are between two In-House Banking accounts open in two different bank areas, the following prerequisites must be met before the cross bank area payment.

- A bank area is set as clearing bank area in configuration activity 105773 Define Bank Areas for Account Management or Activity Define Bank Areas for Account Management, depending on your configuration environment for SAP S/4HANA Cloud Public Edition.
- The subsidiaries set up house banks in bank key of the clearing bank area.
- The bank areas that do not operate as clearing bank area hold an In-House Banking account in the clearing bank area, as the so-called loro accounts for additional clearing posting.

#### Subsidiary 1: Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manually create an invoice for customer representing subsidiary company code 2.

Procedure

This procedure is mentioned in the Accounts Receivable ([J59](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J59)) test script. You can refer to the Enter Invoice Without Sales Order step and create customer invoice. Note down the invoice document number.

For example, you can use following data to create a customer invoice for subsidiary 1 company code 3340:

| Field | Value |
| --- | --- |
| Company code | 3340 |
| Customer | 33403330 |
| Invoice Date/Posting Date | <Today’s date> |
| Reference | <any> |
| Offsetting expense GL account | For example, 41000400 |

#### Subsidiary 2: Create Vendor Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manually create an invoice for vendor representing subsidiary company code 1.

Procedure

This procedure is mentioned in the Accounts Payable ([J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60)) test script. You can refer to the Invoice Entry Without Purchase Orders step and create vendor invoice. Note down the invoice document number.

For example, you can use following data to create a vendor invoice for subsidiary 2 company code 3330:

| Field | Value |
| --- | --- |
| Company code | 33 30 |
| Invoice Date/Posting Date | <Today’s date> |
| Reference | <any> |
| Vendor/Invoicing Party | 33403340 |
| Offsetting expense GL account | For example, 61400000 |
| Tax Code | For example, V0 |
| Cost Center | 33 30 1101 |
| Payment Method | [ |
| Partner BankType | <select the IHB Bank account for that supplier > |
| House Bank | IHB02 |
| Account | <IHB Bank account for subsidiary 2>, for example, 2 |

Repeat to create another invoice for subsidiary 2.

| Field | Value |
| --- | --- |
| Company code | 33 30 |
| Invoice Date/Posting Date | <Today’s date> |
| Reference | <any> |
| Vendor/Invoicing Party | 33403340 |
| Offsetting expense GL account | For example, 61400000 |
| Tax Code | For example, V0 |
| Cost Center | 33 30 1101 |
| Payment Method | [ |
| Partner BankType | <IHB Bank account to close sub 1>, for example, 3 |
| House Bank | IHB02 |
| Account | <IHB Bank account to close sub 2>, for example, 4 |

#### Subsidiary 2: Payment Run

Purpose

This section describes posting payments using the automatic payment program.

Prerequisite

You assign business roles to business user in Fiori App Maintain Business Users (F1303).

For example, the role PAYMENT_SPECIALIST. BANK_INT_SPECIALIST and PAYM_SPEICIALIST_IHB are assigned to example user AP_ACCOUNTANT which is used to execute payment run.

Procedure

This procedure is mentioned in the Accounts Payable- [J60](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J60) test script. You can refer to the Payment Run step. Note down the document number.

Conduct the payment run for the two invoices.

Note down the document number.

#### Monitor MBC Message (with Payment File)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you investigate that MBC has routed the payment file into advanced payment management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go:Message Type: PAIN.001.001.03Create Date: For example, <today’s date>Sender ID: For example, 3330IHB02 | The MBC messages are displayed in respective tabs.Note There must be an Outbound and Inbound message with a PAIN.001.001.03 file with the Sender ID 3330IHB02. |  |
| 4 | Check incoming Message | Choose Incoming Messages tab, select the inbound message, choose >. | Details screen of message displays. |  |
| 5 | Display Message Content | Choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 6 | Navigation to Application Log | Choose Log in the detail screen of message. | The detail log of the message processing is listed. |  |

#### Process Payment in Advanced Payment Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An inbound payment order can be manually processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments(F3647). |  |  |
| 3 | Find Payment Order | Make the following entries and choose Go.Clearing Area: PF | Payment Orders is listed |  |
| 4 | Go to Details | Select your payment order, choose > . | The payment order is listed in details. |  |
| 5 | Process Payment Order | On the Payment Order screen, choose Process. | The payment order is processed. |  |

#### Check Payment Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check payment order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Find Payment Order | Make the following entries and choose Go.Clearing Area: PF | Payment Orders is listed. |  |
| 4 | Go to Details | Select your payment order, choose > . | The payment order is listed in details. Every item has the final status posted |  |

#### Manage In-House Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check In-House Account Balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access App | Open Manage In-House Bank Account Balances (F6341). | The Manage In-House Bank Account Balances view displays. |  |
| 3 | Maintain Filter | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: <the both IHB accounts created in previous step> |  |  |
| 4 | Go to Details | Expand the nodes, and select the lowest node for your bank account, choose > . | The bank account balances is listed in details. All payment items has reached the both In-House Bank accounts. |  |

### Central Incoming Payments

#### Manage Service Level Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create Service Level Agreements.

|  |
| --- |
| Note If one SLA has been created in clearing area PF, you just need to add a rule of Statement Distribution Owner and a rule of Account Substitute for your country. |

|  |
| --- |
| Note When you import a bank statement, Advanced Payment Management (APM) will be called as part of the bank statement process. For APM to decide that the current transaction is relevant for APM certain configurations need to be in place:APM converter configured for imported bank statement formatApp Manage Service level AgreementsClearing area SLA needs to existAdd rule for “Statement Distribution Relevance”Add rule to derive account for business PartnerOnly if the account can successfully be derived, it will be created in APM. The payment order will be created. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Service Level Agreements (F6183A). | The Service Level Agreement view displays. |  |
| 3 | Create | Choose Create. In the pop-up screen, enter the following data and choose Create:Clearing Area: PFSLA Type: Clearing Area Service Level AgreementSLA ID: for example, CP_SLANote If one SLA has been created in clearing area PF, you can skip step 3-5. Choose > to detailed screen, and choose Edit. Choose > to detailed screen of ruleset Statement Distribution Relevance and Account Substitute to maintain rules. Refer to step 6 and 8 for more details. |  |  |
| 4 | Maintain General Parameters | In the Basic Data tab, enter the following data:SLA Description: for example, Clearing Area SLASLA Status: Active |  |  |
| 5 | Create Rule for Statement Distribution Relevance | In the Rulesets tab, choose Create, and choose Relevant to Statement Distribution. | The Statement Distribution Relevance view displays. |  |
| 6 | Maintain Parameters for Statement Distribution Relevance | In the Statement Distribution Relevance view, choose Create. Enter the following data in the automatic created rule with Sequence Number 1:Description: <description>Relevant for Statement Distribution: Yes (x)Choose the search help of Condition.In the Define Conditions pop-up screen, choose Create.Enter the following data for condition one and choose Create:Characteristic: House Bank (EBS_HBID)Options: equal toValue Low: AEBK1Enter the following data for condition two and choose OK:Characteristic: House Bank Account (EBS_HBAC)Options: equal toValue Low: AEAC1In the Statement Distribution Relevance view, choose Apply. |  |  |
| 7 | Create Rule for Account Substitute | In the Rulesets tab, choose Create, and choose Account Substitute. | The Account Substitute view displays. |  |
| 8 | Maintain Parameters for Account Substitute | In the Account Substitute view, choose Create. Enter the following data in the automatic created rule with Sequence Number 1:Description: <description>Account Number: <the IHB account created for subsidiary 1>Choose the search help of Condition.In the Define Conditions pop-up screen, choose Create.Enter the following data for condition one and choose OK:Characteristic: Memo Line (EBS_MEMO)Options: containsValue Low: for example: *CASHPOOLAE*In the Account Substitute view, choose Apply. |  |  |
| 9 | Save and Release | In the Service Level Agreement view, choose Create, and choose Submit. | The service level agreement is created and released. The release status is Approved, SLA Status is Active. |  |

#### Manage Processing Rules for Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a bank reprocessing rule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist.Note This procedure can also be performed by users with the Accounts Receivable Accountant role. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Processing Rules - For Bank Statements (F3555). | The Manage Processing Rules for Bank Statements view is displayed. |  |
| 3 | Create Rule | To add a new rule, choose Create. |  |  |
| 4 | Add Rule Criteria | Enter the following data:Description: <any description of the rule>Rule For: Incoming PaymentAction Type: G/L Posting |  |  |
| 6 | Add Condition Criteria | In the Condition area, enter the following data:Item 1)Attribute: Memo LineOption: containsFrom: CASHPOOLTo: <empty>Choose Create to add item 2:Attribute: Company CodeOption: equal toFrom: 3310To: <empty> |  |  |
| 7 | Action Type: G/L Posting | In the Post to G/L Account, enter the following:Note You only enter either a Profit Center or a Cost Center, not both, depending on the type of posting. If the G/L account is a cost element, then cost center is required. If the G/L account is a balance sheet item, then profit center is required.Account: 11001090 (Technical Account for Bank Statement (Cash/S)Profit Center: For example, YB600Cost Center: <empty> |  |  |
| 8 | Save | Choose Create. | The new rule is saved. |  |
| 9 | Automate Rule | Choose Automate Rule.On the dialog box Automate Rule, make the following entries and choose Automate Rule.Journal EntryType: SAProcedureType: 001 (One-Step Posting)JE Type Bank SubAcc.: <empty>Bank Subaccount: <empty>Choose Close to confirm the message This rule is applied when bank statements are imported. |  |  |

#### Import External Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You upload external bank statement.

Prerequisite

You assign business roles to business user in Fiori App Maintain Business User Groups (F6399). For example, the role PAYMENT_SPECIALIST, BANK_INT_SPECIALISTand PAYM_SPEICIALIST_IHB are assigned to example user CASH_SPECIALIST which is used to upload bank statement.

You need to create a new xml file and name the file: camt.053_AEBK1_CP_01.xml.

Enter the following text into the newly created file and save it locally:

Sample Code

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="UTF-8"?> <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.02" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <BkToCstmrStmt> <GrpHdr> <MsgId>2014082800000001</MsgId> <CreDtTm>2022-05-25T01:02:00</CreDtTm> <MsgPgntn> <PgNb> 1</PgNb> <LastPgInd>true</LastPgInd> </MsgPgntn> </GrpHdr> <Stmt> <Id>CAMSLINK01000249</Id> <ElctrncSeqNb>02036</ElctrncSeqNb> <CreDtTm>2022-05-25T01:02:00</CreDtTm> <Acct> <Id> <Othr> <Id>1133698</Id> </Othr> </Id> <Svcr> <FinInstnId> <BIC>DEUTDEFFXXX</BIC> </FinInstnId> </Svcr> </Acct> <Bal> <Tp> <CdOrPrtry> <Cd>PRCD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="EUR">100.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2022-05-25</Dt> </Dt> </Bal> <Bal> <Tp> <CdOrPrtry> <Cd>CLBD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="EUR">900.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2022-05-25</Dt> </Dt> </Bal> <Ntry> <Amt Ccy="EUR">1000.00</Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2022-05-25</Dt> </BookgDt> <ValDt> <Dt>2022-05-25</Dt> </ValDt> <AcctSvcrRef>FSN TEST AcctSvcrRef Item 1</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>PMNTRCDTDMCT</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <AmtDtls> <InstdAmt> <Amt Ccy="">0.00</Amt> </InstdAmt> </AmtDtls> <RltdPties> <Dbtr> <Nm>Test Account for Cash</Nm> </Dbtr> <DbtrAcct> <Id> <Othr> <Id>787878</Id> <SchmeNm> <Cd>BBAN</Cd> </SchmeNm> </Othr> </Id> </DbtrAcct> </RltdPties> <RltdAgts> <DbtrAgt> <FinInstnId> <ClrSysMmbId> <ClrSysId> <Cd>DEBLZ</Cd> </ClrSysId> <MmbId>10020033</MmbId> </ClrSysMmbId> </FinInstnId> </DbtrAgt> </RltdAgts> <RmtInf> <Ustrd>4711CASHPOOLDE4712</Ustrd> </RmtInf> <AddtlTxInf>NOCH MAL 4713</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>NOCH MAL 4713</AddtlNtryInf> </Ntry> <AddtlStmtInf>Unittest</AddtlStmtInf> </Stmt> </BkToCstmrStmt> </Document> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). |  |  |
| 3 | Get Latest Bank Statement Number | To get the latest imported bank statement number, choose Show Filter Bar if search criteria are hidden, and make the following entries:Company Code: 3310House Bank: AEBK1House Bank Account: AEAC1Latest Statement: Latest onlyAnd choose Go. | The latest bank statement number of the specified bank account displays on the view Manage Bank Statements.The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 00005, the next number is 00006. If no latest bank statement was found, the next number should be 00001. |  |
| 4 | Get Closing Balance of Latest Bank Statement | Make a note of the closing balance of the specified bank account. It can be found on the view Manage Bank Statements. | The closing balance of the latest bank statement should be the opening balance of the next bank statement. If no latest bank statement was found, the opening balance of the next bank statement should be zero. |  |
| 5 | Open XML File | In a text editor, open the camt.053_AEBK1_CP_01.xml file you previously created in the Prerequisites section. |  |  |
| 6 | Edit XML File | Edit the following values in camt.053 file:<MsgId> 2022052500000001</MsgId:> replace 2014082800000001 by current time (format YYYYMMDDHHMMSS).<ElctrncSeqNb> 02036</ElctrncSeqNb>: in this example, 02036 is the bank statement number, replace it by the right bank statement number.<Id> 1133698 </Id>: in this example, 1133698 is the bank account number of house bank/account ID AEBK1/ AEAC1. Edit this element if you are not using AEBK1/ AEAC1 during testing.<BIC> DEUTDEFFXXX </BIC>: in this example, DEUTDEFFXXX is the SWIFT/BIC of AEBK1, edit this element if you are not using AEBK1 during testing.<Dt> 2022-05-25</Dt>: replace 2022-05-25 by the current date, format is YYYY-MM-DD. Dt2022-05-25/Dt appears several times in this xml file, replace them all.<Amt Ccy=" AED "> 100.00 </Amt>: in this example, 100.00 is the opening balance that is also the closing balance of latest imported bank statement, replace 100.00 by the real opening balance.<Amt Ccy=" AED "> 1000.00 </Amt>: in this example, 1000.00 is the closing balance. Closing balance = opening balance - debit amount + credit amount, for example, 1000.00=100.00+900.00-0.00.<Amt Ccy=" AED "> 900.00 </Amt> in the first <Ntry></ Ntry>: in this example, 900.00 is the amount of the incoming payment from customer, it should be equal to the receivables of customer invoice mentioned in Prerequisites.<RmtInf><Ustrd> 4711CASHPOOL AE 4712 </Ustrd></RmtInf> : in this example, 4711CASHPOOLAE4712 is memo line of bank statement. For this test scenario, the value is mandatory and is maintained in SLA, do not change it.<Amt Ccy="AED"> 0 </Amt> in the second <Ntry></ Ntry>: in this example, 0 is the amount of an outgoing payment transaction. In our test scenario, only incoming payment is relevant.Note In the ISO camt.053 bank statement file, always use ‘.’ as decimal point (don't use ‘,’). And the date format should be YYYY-MM-DD. |  |  |
| 7 | Access the SAP Fiori App | Open Manage Incoming Payment Files (F1680). |  |  |
| 8 | Upload Bank Statement | On the Management Incoming Payment Files view, choose the Import button, on the Import File dialog box, make the following entries:Incoming File Type: <Bank Statement format recognized automatically>Upload Files: choose the plus + button and a new dialog box displays. Choose the electronic bank statement file (for example, camt.053_ AEBK1_CP_01.xml) and choose Open. The result is the electronic bank statement file is selected and displays in the Import File dialog box.Recognized Format: such as BAI format, SWIFT MT940, and XMLSelect Format: a list of local variants with recognized format displays, and choose for example, CAMT.053.001.02Choose Process. | A File imported: 1 notification displays. Choose OK, then choose Go on Management Incoming Payment Files view, the latest imported file is displayed on the first row, you can select the imported file and in the next view, you review the log. |  |

#### Process Payment in Advanced Payment Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An inbound payment order can be manually processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payments (F3647). |  |  |
| 3 | Find Payment Order | Make the following entries and choose Go.Clearing Area: PF | Payment Orders are listed. |  |
| 4 | Go to Details | Select your payment order, choose > . | The payment order is listed in details. |  |
| 5 | Process Payment Order | On the Payment Order screen, choose Process. | The payment order is processed. |  |

#### Manage In-House Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can manage In-House Account Balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access App | Open Manage In-House Bank Account Balances (F6341). | The Manage In-House Bank Account Balances view displays. |  |
| 3 | Maintain Filter | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: <the IHB account created in the previous step> |  |  |
| 4 | Go to Details | Expand the nodes, and select the lowest node for your bank account, choose > . | The bank account balances is listed in details. All payment items has reached the In-House Bank account. |  |

### End Of Day Process

#### Maintain Exchange Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update exchange rates.

Procedure

For more information, see the Currency Exchange Rates step or Import Foreign Exchange Rates step in the Accounting and Financial Close- [J58](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/J58) test script.

#### Create Correction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create correction for In-House bank accounts to correct the account balance. After end of day process is done, the update on accounting is made in background.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access App | Open Manage In-House Bank Account Balances (F6341). | The Manage In-House Bank Account Balances view displays. |  |
| 3 | Maintain Filter | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: In-House Bank account 1 |  |  |
| 4 | Check Details | Expand the nodes, and select the lowest node for your bank account, choose > . | The bank account balance is listed in details. All payment items have reached the In-House Bank account. The bank statements are generated for your accounts. |  |
| 5 | Create Correction | Choose Create Correction and in the pop-up screen Create Correction, make the following entries.Payment Correction Type: for example, 0726 (Incoming Payment from Zero Balancing)Debit-Credit Indicator: CreditAmount: for example, 100.00Value Date: <today>Choose Create Correction. | A payment order is created, and the payment item is listed in the Transactions section. |  |
| 6 | Check Payment Item | In the Transactions section, you can check the settlement payment items. | A payment item is created with the right value date, amount. |  |

#### Close In-House Bank Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you close In-House bank accounts which you do not need. After the charges and interest are settled, the balance will be transferred to a reference account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Accounts (F5942). | The Manage In-House Bank Accounts screen displays. |  |
| 3 | Select In-House Bank Account to Close | Enter the following data and choose Go:Bank Area: for example: SIAE(SAP In-House Banking Area AE)Account Number: for example, <IHB Bank account to close sub 1, account 3> | The In-House Bank Account lists. |  |
| 4 | Close Account with Internal Reference Account | Select one bank account, choose >. In the detailed view, choose Close Account and enter the following data:Requested Closing Date: for example, todayReference Account Number: for example, <IHB Bank account for subsidiary 1, account 1>Note Use search help to select the bank account.Choose Close Account. | The status of the IHB bank account to close sub 1 will be changed to Closure Released. |  |
| 5 | Close Account with External Reference Account | Repeat Step 3-4 to close <IHB Bank account to close sub 2, account 4>, populate an external bank account as reference account.Note Refer to Maintain Payment Agreements. If you choose, select as reference account, and vice versa. | An error message pops up with message negative balance transfer to external reference account not allowed. |  |

#### Manage In-House Bank Application Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you execute all steps as following for end of day process.

- Accounting Balancing: Job: /PF1/JT_IHB_EOD_JOB_ACC_BALANCING Program: /PF1/R_IHB_ACCBALANCING
- Account Balancing/Closing Date: Job: /PF1/JT_IHB_EOD_CHAIN Program: /PF1/R_IHB_EOD_CLOS_SET_DATE
- Account Closure: Job:/PF1/JT_IHB_EOD_JOB_ACC_CLOSURE Program:/PF1/R_IHB_ACCCLOSURE
- Bank Statement: Job: /PF1/JT_IHB_EOD_JOB_BANK STMNT Program:/PF1/R_IHB_ACCT_BK_STMNT
- FX Process: Job:/PF1/JT_IHB_EOD_JOB_FX Program:/PF1/R_IHB_ACC_FX_PROCESS
- GL Transfer: Job:/PF1/JT_IHB_EOD_JOB_GL_TRANS Program:/PF1/R_IHB_GL_TRANSFER
- Notification: Job: /PF1/JT_IHB_EOD_JOB_NOTIF
- Payment Transaction Date: Job: /PF1/JT_IHB_EOD_CHAIN Program:/PF1/R_IHB_EOD_NEXT_SET_DATE

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank Application Jobs (F6653). | The Application Jobs view displays. |  |
| 3 | Create a New Application Job | On the current view, choose Create to create an application job. |  |  |
| 4 | Choose Job Template | In the Template Selection section, make the following entries:Job Template: In-House Bank - EOD Jobs (All Jobs)Job Name: for example：In-House Bank - EOD Jobs (All Jobs) | The New Job: In-House Bank-EOD Jobs (All Jobs) view displays.Note The job template includes following jobs. You can also execute these jobs one by one.Accounting Balancing: /PF1/JT_IHB_EOD_JOB_ACC_BALANCINGAccount Balancing/ClosingDate: /PF1/JT_IHB_EOD_CHAINAccount Closure: /PF1/JT_IHB_EOD_JOB_ACC_CLOSUREBank Statement: /PF1/JT_IHB_EOD_JOB_BANK STMNTFX Process: /PF1/JT_IHB_EOD_JOB_FXGL Transfer: /PF1/JT_IHB_EOD_JOB_GL_TRANSNotification: /PF1/JT_IHB_EOD_JOB_NOTIFPayment Transaction Date: /PF1/JT_IHB_EOD_CHAIN |  |
| 5 | Maintain Scheduling Options | Choose Step 2. In the Scheduling Options section, make the following entriesStart Immediately: <Selected or deselected>If you choose star immediately, other parameter do not need to maintain.Start: <current time or any future time as needed>Time Zone: <time zone>For Recurrence Pattern, choose Define Recurrence Pattern.In the Scheduling Information dialog box, the additional scheduling options are available.Recurrence Pattern: for example, WeeklyEvery: for example, 1On: for example, MondayEnd: <Optional>On Non-Working Day: <Optional>Calendar: <Calendar>Choose OK. | If you would like to run this job immediately, the check-box of Start Immediately should be selected.If you schedule this job at some time in the future, the Start and Time Zone should be defined. |  |
| 6 | Set Posting Date - Parameter Section(Step 1) | Choose Step 3. In the Parameter section, make the following entries and choose > to next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAE | Parameter for setting posting date is maintained.Note You set the posting date whereby all subsequent payment transaction postings are entered with the subsequent dates (dependent on the business day as defined in the factory calendar). |  |
| 7 | Account FX Process - Parameter Section(Step 2) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAESimulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for account FX process is maintained.Note When you make or receive payments, if the transaction currency differs from the in-house bank account currency of the affected current accounts, you must convert currencies. Consider the exchange rate for the calculation. |  |
| 8 | Account Closure - Parameter Section(Step 3) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAEAccount Number: <the IHB account created in the previous step>Alias: <empty or alias>Simulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for account closure is maintained.If the requested closing date is reached, after end of day account closure process, the balancing process will be conducted, the balance is adjusted with interest and charges. Then depending on the reference account, a payment order will be created to transfer the remaining balance to the reference bank account.If it is an IHB account, the balance of the closed IHB account will be set to zero and the status is changed to Closed; the remaining balance is transferred to the reference IHB account via an internal transfer order.If it is an external account and the requested closed account balance is negative, the requested closing IHB account status will remain Closure Released with the requested closing date shifted to next day. |  |
| 9 | Account Balancing - Parameter Section (Step 4) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAEAccount Number: <the IHB account created in previous step>Alias: <empty>Simulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for account balancing is maintained. |  |
| 10 | Transfer PI to G/L - Parameter Section (Step 5) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAEAccount Number: <the IHB account created in the previous step>Simulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for transferring PI to G/L is maintained.Note In-house banking acts as a subledger, meaning that the postings on the in-house banking accounts must be transferred to the general ledger of the in-house bank owner on a regular basis. During the general ledger transfer, the items updated on the in-house bank accounts are transferred to the corresponding general ledger accounts (FI GL). |  |
| 11 | Bank Statement - Parameter Section (Step 6) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAEAccount Number: <the IHB account created in the previous step>Simulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for bank statement is maintained. |  |
| 12 | Notifications - Parameter Section (Step 7) | Make the following entries and choose > to the next parameter step:Bank Area: for example: SIAE(SAP In-House Banking AreaAEAccount Number: <the IHB account created in the previous step>Account Alias: <empty>Balance Notification: <Selected>Interest Scale Notification: <Selected>Bank Statement Notification: <Selected>Simulation: <Deselected>Asynchronous Processing: <Deselected> | Parameter for notification is maintained. |  |
| 13 | Set Closing Date - Parameter Section (Step 8) | Make the following entries:Bank Area: for example: SIAE(SAP In-House Banking AreaAE | Parameter for setting closing date is maintained. |  |
| 14 | Check | Choose Check. |  |  |
| 15 | Run this Application Job | Choose Schedule to run this application job. |  |  |
| 16 | Check Application Jobs Log | Choose Go to update the job status. When your job’s status change to Finished, you choose Log to navigate to the Job Log. | Job log displays. |  |

#### Manage In-House Bank End of Day

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you monitor the end of day processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access the SAP Fiori App | Open Manage In-House Bank End of Day (F6338). | The Manage In-House Bank End of Day view displays. |  |
| 3 | Select Bank Area | Make following entries and Choose Go.Bank Area: for example, SIAE (SAP In-House Banking Area AERun Date: for example: <Today’s date> | All process steps list.Note It may including following processes:Accounting Balancing: /PF1/R_IHB_ACCBALANCINGAccounting Balancing Date: /PF1/R_IHB_EOD_CLOS_SET_DATEAccount Closure: /PF1/R_IHB_ACCCLOSUREBank Statement: /PF1/R_IHB_ACCT_BK_STMNTFX Process: /PF1/R_IHB_ACC_FX_PROCESSGL Transfer: /PF1/R_IHB_GL_TRANSFERNotification:Payment Transaction Date: /PF1/R_IHB_EOD_NEXT_SET_DATE |  |
| 4 | Check log details | Select one process, choose >. | The relevant process’s log displays in details. |  |

#### Manage In-House Bank Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You check that the bank statements are generated for your accounts and the settlement payment items are posted and have the detailed for the included bank statement. You can also navigate to the FI posting via the field FI Journal Entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Payment Specialist - In-House Banking. |  |  |
| 2 | Access App | Open Manage In-House Bank Account Balances (F6341). | The Manage In-House Bank Account Balances view displays. |  |
| 3 | Maintain Filter | Make the following entries and choose Go.Bank Area: for example, SIAEAccount Number: <the IHB account created in previous step> |  |  |
| 4 | Check Details | Expand the nodes, and select the lowest node for your bank account, choose > . | The bank account balances is listed in details. All payment items has reached the In-House Bank account. The bank statements are generated for your accounts. |  |
| 5 | Show More per Row | In Transactions section, choose Show More per Row in the top right corner.Note If FI Journal Entry number is available, you can navigate to FI posting by clicking it. | More details of payment items displays. |  |
| 6 | Check Payment Item | In Transactions section, you can check the settlement payment items. Navigate to payment item by clicking payment Item Number.Navigate to corresponding finance notification record by clicking the Finance Notification ID of the respective item.Note The finance notification from In-House Banking can be monitored in the Manage Finance Notifications (F8825) app. For more details, you can refer the Appendix Manage Finance Notifications in test script of J58 Accounting and Financial Close. | Payment order displays. |  |
| 7 | Check Bank Statement | In Bank Statements section, you can check the bank statement is created for your account. | Bank statement displays.Note If distribution method ‘Interface MBC’is used in your account, the CAMT file for internal bank statement is transferred via MBC connector to the subsidiary G/L. |  |

#### Monitor MBC Message (with Payment File)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You monitor the CAMT.053 messages transmitted out of S/4HANA via MBC.

Prerequisite

The distribution method Interface MBC is used in your account in step In-House Bank Accounts, the CAMT file for internal bank statement is transferred via MBC connector and post to the subsidiary G/L.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Integration Specialist - Bank Integration. |  |  |
| 2 | Access App | Open Manage Bank Messages (F4385). |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and press Enter:Message Type: CAMT.053.001.02Creation Date: For example, <today’s date> | The MBC messages are displayed in respective tabs. |  |
| 4 | Display Message Content | Select the outgoing or incoming message and choose View Payload in the detail screen of message. | The message content is displayed. |  |
| 5 | Navigation to Application Log | Select a message and choose Log in the detail screen of message. | The detail log of the message processing is listed. The outgoing message should be routed locally and the inbound message should be processed successfully.Note After the background job pulls the bank statement from MBC, SAP S/4HANA imports the bank statement automatically. You can monitor the imported bank statements in the Fiori App Manage Bank Statements (F1564) for subsidiary company.Note If the bank statement cannot be posted and shows status 7 (Not completed), you need to reprocess the bank statement. Use app Reprocess Bank Statement Items (F1520) to complete the posting. |  |

### Post B/S Reclassification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the balance sheet reclassification for in-house bank.

Prerequisites

Ensure that you have defined Reclassification Rules in preliminary step .

Procedure

This procedure is mentioned in the Accounting and Financial Close- [J58](https://me.sap.com/processnavigator/SolP/J58) test script. You can refer to the Post B/S Reclassification step and post the balance sheet reclassification for in-house bank. You can check the result of reclassification, the relevant posting document should be generated under Valuation Rule SBSR or SLBS with step 0020.

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
- see-also :: [[05-treasury-and-cash-management/test-script-intercompany-process-for-cash-concentration-2u8-ae-869]]
- see-also :: [[05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6BP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 163,760 chars in the whole document
