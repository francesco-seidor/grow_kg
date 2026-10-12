---
id: 03-financial-accounting-and-close/test-script-direct-debit-19m-ae-sap-s-4hana-cloud-public-edition-707
title: "Test Script: Direct Debit (19M_AE) - SAP S/4HANA Cloud Public Edition (19M_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 19M (AE): direct debit collection, SEPA mandates, payment run, payment medium, prerequisites and BRF+ setup."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [19M_S4CLD2608_BPD_EN_AE]
keywords: [Direct Debit and SEPA Mandates, direct debit, sepa mandates, payment run, payment proposals, payment medium, payment medium format variants, brf+ output settings, payment advice, payment list]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19M_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-707
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Direct Debit (19M_AE) - SAP S/4HANA Cloud Public Edition (19M_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19M_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Direct Debit (19M_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846464)

[2 Prerequisites 4](#_Toc232846465)

[2.1 System Access 4](#_Toc232846466)

[2.2 Roles 4](#_Toc232846467)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232846468)

[2.4 Business Conditions 7](#_Toc232846469)

[2.5 Preliminary Steps 7](#_Toc232846470)

[2.5.1 Define Payment Medium Format Variants 7](#_Toc232846471)

[2.5.2 BRF+ Settings for Payment Advice 9](#_Toc232846472)

[2.5.3 BRF+ Settings for Payment List 13](#_Toc232846473)

[3 Overview Table 17](#_Toc232846474)

[4 Test Procedures 19](#_Toc232846475)

[4.1 Preparation of Payments 19](#_Toc232846476)

[4.1.1 Maintain Business Partner 19](#_Toc232846477)

[4.2 Customer Invoice Payment Preparation 21](#_Toc232846478)

[4.2.1 View Customer Line Items 21](#_Toc232846479)

[4.2.2 Manage Payment Blocks 22](#_Toc232846480)

[4.2.3 Display Customer Balance 24](#_Toc232846481)

[4.3 Payment Run 25](#_Toc232846482)

[4.3.1 Schedule Payment Proposals 25](#_Toc232846483)

[4.3.2 Revise Payment Proposal 27](#_Toc232846484)

[4.3.3 Release Payment Proposal 28](#_Toc232846485)

[4.3.4 BCM Batch Creation (Optional) 30](#_Toc232846486)

[4.4 Payment Medium 30](#_Toc232846487)

[4.4.1 Create Payment Medium 30](#_Toc232846488)

[4.5 Payment Review 31](#_Toc232846489)

[4.5.1 View Payment List 31](#_Toc232846490)

[4.6 Invoice Management Reporting 32](#_Toc232846491)

[4.6.1 Overdue Receivables 32](#_Toc232846492)

## Purpose

Overview

For SEPA countries/regions: In this scope item, you can use the direct debit payment method in the Single Euro Payments Area (SEPA) to collect payments from your customers in Euro and certain non-SEPA countries/regions to collect payments from your customers in your local currency.

For countries/regions in SEPA, a debtor grants mandates to a creditor as part of a direct debit procedure. Using SAP S/4HANA Cloud Public Edition, you create and maintain the SEPA mandates from the customers, which are the legal basis for the direct debit payment in SEPA.

The system checks that a valid SEPA mandate exists during the payment run. For SEPA countries/regions, the system saves the ID of the SEPA mandate in the payment data and creates a SEPA-specific payment medium.

You can print out SEPA mandates on paper and repeat the printing.

For non-SEPA countries/regions: In this scope item, you can use the direct debit payment method to collect payments from your customers in your local currency.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conduct the test in terms of system, user, master data, organizational data, and other test data and business conditions.

- Customer master data has been created.
- Mandate has been created .
- Invoices have been posted to accounting.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you've installed an SAP Best Practices Package, you can use the following Package scenario data:

Accounting

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Customer | 33100100 |  |  |
| House Bank | AEBK1AEBK2 | AE BK1 is used for Multi-Bank Connectivity (MBC). AEBK2 is used for file download. |  |
| Bank G/L Account | 11001000 and 11002000 |  |  |
| Cost Center | 33101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

Use the following table for creating payment methods (PM) and payment medium format (PMF)

| PM | Name of Payment Method | PMF for House Bank AEBK1 | PMF for File Download (AEBK2 Demo Data*) |
| --- | --- | --- | --- |
| E | Direct Debit | AE _ACH_DD | AE _ACH_DD |

* The AEBK2 value is demo data. Ensure the solution is installed with demo data to test this value.

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Must be run before this test script. Invoices are created and posted to accounting. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Must be run before this test script. Invoices are created and posted to accounting. |
| BKX - Sales Order Processing – SEPA Direct Debit Handling | Must be run before this test script. Invoices are created and posted to accounting. |
| 1LQ - Output Management | Ensure that you set up printers, create a print queue, and/or set up email. These activities are in the Set-up Instructions document. |
| BFB - Basic Cash Operations | Payment is integrated with a bank. |
| 16R - Bank Integration with SAP Multi-Bank Connectivity | SAP Multi-Bank Connectivity (MBC), SAP establishes connections with your banks to automatically send payment instructions. |
| 1EG - Bank Integration with File Interface | Download the payment files for outgoing payments, then upload these payment files to your banking portal or treasury workstation for payment processing. You can also upload the electronic bank statements sent from your bank. |

### Preliminary Steps

#### Define Payment Medium Format Variants

Purpose

In this activity, you create, change, and assign selection variants for payment medium formats. You can use these variants when creating payment media using the Payment Medium Workbench.

The selection variants are required to be able to generate the payment medium.

Prerequisite

- Payment methods are specified and assigned to your country/region and company code.
- Payment medium Formats are assigned to your payment methods.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Payable

1. For the row with Item Name of Payment Medium Formats, choose Details (>).
2. For the Create/Assign Selection Variants (Alternative) row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create/Assign Selection Variants (Alternative).
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Configuration Steps | Select the Payment Medium Format to process, for example:Payt Mdm Format: AE_CGI_XML_DDCaution Ensure you select a Payment Medium Format that is valid for your country/region and was installed in your solution. For more information, see the Payment Methods (PM) and Payment Medium Formats (PMF) table in the Master Data, Organizational Data, and Other Data topic under Prerequisites. | The Change View "Payment Medium Format: Format for Variants": Details view is displayed. |  |
| 2 | Variant Creation | Caution The selected Payment Medium Format determines which fields are available.When defining your payment medium formats, the CoCd, House Bk fields are available, on the row of the company code and house bank you're processing, for example Co. Code3310 and House bank AEBK1.Make the following entries:Selection Variant: <any description (14 characters max.)>Note If the selected variant already exists, create a new variant by entering a new description. Alternately, you can keep the same variant and change the parameters as described in the next step. | The selection variant is created and assigned. |  |
| 3 | Format Parameters | Caution Depending on the selected Payment Medium Format, different fields are available.Note To generate the payment medium, it's enough to have the variant created (previous step) and saved (next step).Choose Format Parameters.Make the following entries and choose Continue: (for your payment medium format, the following are available.)* ACH Batch Hdr. Company Entry Description: <any description> (10 characters max.). | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Save | Choose Save and then Exit. | The variant is created, assigned, and saved. |  |

#### BRF+ Settings for Payment Advice

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view is displayed. |  |
| 3 | Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Output Type | Details are displayed in Maintain Business Rules section. |  |
| 4 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Sep.paymt.adv.: X (Yes)Output type: PAYM_ADVDispatch Time: 1 (Immediately) |  |  |
| 5 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 6 | Receiver | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Receiver | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVSupplier: is not initialCustomer: leave blankRole: HExclusive Indicator: - (false)Choose + to insert a new row.Enter the following:Output type: PAYM_ADVSupplier: leave blankCustomer: Select is not initialRole: SExclusive Indicator: -(false) |  |  |
| 8 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 9 | Channel | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVChannel: PRINT (Printout)Exclusive Indicator: - (false)Choose the + button to insert a new row.Enter the following:Output type: PAYM_ADVChannel: EMAIL (email)Exclusive Indicator: - (false) |  |  |
| 11 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 12 | Printer Settings | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Printer Settings | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVPrint Queue: <choose the print queue defined in your system>Number of Copies: 1 |  |  |
| 14 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 15 | Email Settings | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Email Settings | Details are displayed in the Maintain Business Rules section. |  |
| 16 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVSender Email: sender email addressEmail Template: FFO_PAYM_ADVICE_EMAIL_TEMPLATE |  |  |
| 17 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 18 | Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 19 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVRelevance Indicator: X (True) |  |  |
| 20 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 21 | Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 22 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVForm Template: FIN_FO_PAYM_ADVICEForm Language: For example, E (English). | Rule data is entered. |  |
| 23 | Activate Rules | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 24 | Email Recipient | In the Select Business Rules section, make the following entries:Show Rules for: Payment AdviceDetermination Step: Email Recipient | Details are displayed in the Maintain Business Rules section. |  |
| 25 | Add Rules | Choose Edit.Under Table Contents choose the + button to insert a new row.Enter the following by choosing … or selecting Direct Value Input from the dropdown in each field:Output type: PAYM_ADVRole: SRecipient: 33100100Email Type Code: TOE-mail Address: <email address>. | Rule data is entered. |  |
| 26 | Activate Rules | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 27 | Email Recipient | To specify the email address of the recipient of the payment advice, follow the instructions described in Test Procedures > Preparation of Payments > Maintain Business Partner, in the Correspondence step. |  |  |

#### BRF+ Settings for Payment List

Purpose

In this activity, you define the system determination of output parameters of the payment list for printing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view is displayed. |  |
| 3 | Output Type | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 4 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTDispatch Time: 1 (Immediately) | The Confirm Activation dialog box is displayed. |  |
| 5 | Activate | Choose Yes. | Rules are activated. |  |
| 6 | Receiver | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Receiver | Details are displayed in the Maintain Business Rules section. |  |
| 7 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTIndicator: Only P…: =X (Yes)Role: PPExclusive Indicator: (false)Choose + to insert a row.Enter the following:Output type: PAYM_LISTIndicator: Only P…: =falseRole: PLExclusive Indicator: (false) | The Confirm Activation dialog box is displayed. |  |
| 8 | Activate | Choose Yes. | Rules are activated. |  |
| 9 | Channel | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 10 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTChannel: PRINT (Printout)Exclusive Indicator: - (false) | The Confirm Activation dialog box is displayed. |  |
| 11 | Activate | Choose Activate.On the Confirm Activation dialog box, choose Yes. | Rules are activated. |  |
| 12 | Printer Settings | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Printer Settings | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTPrint Queue: For example, DEFAULT or choose the print queue defined in your systemNumber of Copies: 1 | The Confirm Activation dialog box is displayed. |  |
| 14 | Activate | Choose Yes. | Rules are activated. |  |
| 15 | Form Template | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 16 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries:Output type: PAYM_LISTRole: PLForm Template: FIN_FO_PAYM_LIST_V2Choose + to insert a row.Enter the following:Output type: PAYM_LISTRole: PPForm Template: FIN_FO_PAYM_LIST_V2Choose Activate | The Confirm Activation dialog box is displayed. |  |
| 17 | Activate Rules | Choose Yes. | Rules are activated. |  |
| 18 | Output Relevance | In the Select Business Rules section, make the following entries:Show Rules for: Payment ListDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 19 | Add Rules | Choose Edit.Under Table Contents choose + (Insert New Row).Make the following entries and choose Activate:Output type: PAYM_LISTRelevance Indicator: X (True) | The Confirm Activation dialog box is displayed. |  |
| 20 | Activate | Choose Yes. | Rules are activated. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Preparation of Payments

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner](#unique_11) [page ] 19 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) |  |

Table 3: Customer Invoice Payment Preparation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [View Customer Line Items](#unique_12) [page ] 21 | Accounts Receivable Accountant | Manage Customer Line Items (F0711) | A list of all invoices is displayed. |
| [Manage Payment Blocks](#unique_13) [page ] 22 | Accounts Receivable Accountant | Manage Customer Line Items (F0711) | Blocked invoices are released. |
| [Display Customer Balance](#unique_14) [page ] 24 | Accounts Receivable Accountant | Display Customer Balances (F0703A) | You displayed the customer balance. |

Table 4: Payment Run

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Payment Proposals](#unique_15) [page ] 25 | Accounts Receivable Accountant | Manage Automatic Payments (F0770) | Payment is scheduled. |
| [Revise Payment Proposal](#unique_16) [page ] 27 | Accounts Receivable Accountant | Revise Payment Proposals (F0771) | Payment is revised |
| [Release Payment Proposal](#unique_17) [page ] 28 | Accounts Receivable Accountant | Manage Automatic Payments (F0770) . | Payment is released. |

Table 5: Payment Medium

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Payment Medium](#unique_18) [page ] 30 |  | See topic for details. | The payment medium is created automatically after BCM batch is created. The batch item status changes to Payment Medium Created. |

Table 6: Payment Review

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [View Payment List](#unique_19) [page ] 31 | Accounts Payable Accountant | Display Payment Lists (S_P99_41000099) |  |

Table 7: Invoice Management Reporting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Overdue Receivables](#unique_20) [page ] 32 | Accounts Receivable Manager | Overdue Receivables - Today (F1747) | You view a graphical overview over the overdue receivables. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, you can search for objects such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

- Log on to the SAP Fiori launchpad using the respective user: for example, Internal Sales Representative.
- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search Bar displays, as two filter fields appear left of the search button. Enter your Search Criteria and choose the business object type: for example, Sales Orders from the drop-down menu in the first field. Enter sales order number in the second field and choose Search. The sales order is listed.
- Choose the Sales Order Number link. The system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page. You then can get detailed data by choosing the corresponding links.

There are factsheets available for the following objects, which are visible depending on the assigned role:

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact Sheet.

### Preparation of Payments

#### Maintain Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, specific information for the customer master record, for example payment method, is added.

Prerequisite

The Customer master record is entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The Customer Master view is displayed. |  |
| 3 | Select Roles and Customer | Select the following and choose Go:Role: Customer (Fin.Accounting), CustomerBusiness Partner: 33100100 | The worklist shows your Business Partner. |  |
| 4 | Choose BP | For your Business Partner, choose Details (>). |  |  |
| 5 | Edit Customer | Choose Edit. | The Business Partner Master Data can now be edited. |  |
| 6 | Company Code Data | Choose the Company Codes tab. |  |  |
| 7 | Company Code | On the row for the company code, choose Details (>). | Company code data is displayed. |  |
| 8 | Correspondence | In the Correspondence section, make the following entries:Accounting Clerk: <Choose any available>Clerk Email Address.: <email address> | The accounting clerk is changed. |  |
| 9 | Finance | Choose the Finance tab. |  |  |
| 10 | Payment Methods | In the Automatic Payment Transactions section, select one or more of the following Payment Methods:E | You've chosen payment methods. |  |
| 11 | Apply Changes | Choose Apply. |  |  |
| 12 | Bank Accounts | Choose the Bank Accounts tab. |  |  |
| 13 | Bank Accounts | Select an available bank and make the following entries:Collection Authorization Indicator: Selected |  |  |
| 14 | Apply | Choose Apply. |  |  |
| 15 | Save | Choose Save. | The changes to Business Partner Master Data are saved. |  |

### Customer Invoice Payment Preparation

#### View Customer Line Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, all accounts receivable items are listed. You can modify certain fields of a document to be collected.

Prerequisite

Invoices are posted (for more information, see the [Business Conditions](#unique_6) [page ] 7 section).

Accounts receivable invoices are available in the system using customer 33100100.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Line Items (F0711). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100100Company Code: 3310Status: <status>Note When you select All Items, the system displays all the account items.You can also choose to display only Open items or Cleared Items.Open at key date: <Today’s date>Item type: Normal Items | The customer line items are displayed according to your search criteria. |  |
| 4 | Change Document | Select the checkbox for a line item by choosing the checkbox of the first column and choose Edit Line Items. | The Edit 1 Line Item view is displayed. |  |
| 5 | Make Changes | Make the required changes to line items from the available sections and choose OK:Payment Data: <any>Dunning Data: <any>Additional Data: <any> | The system displays an Items Changed notification. |  |

#### Manage Payment Blocks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review and release blocked invoices.

When an invoice is blocked, Financial Accounting can't collect the invoice. Invoices can be blocked either automatically or manually depending upon the payment block reason and release in the configuration.

Prerequisite

Invoices are posted (for more information, see [Business Conditions](#unique_6) [page ] 7). Documents to be changed must not be included in any Payment Proposal with Pre-Notification.

A customer invoice is blocked for payment either automatically or manually by editing the customer line items using the Manage Customer Line Items (F0711) SAP Fiori app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Line Items (F0711). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100100Company Code: 3310Status: <status>Note When you choose All Items, the system displays all the account items.You can also choose to display only open items or cleared items.Open at key date: <Today’s date>Item type: Normal Items | The customer line items are displayed according to search criteria. |  |
| 4 | Select the Line Item | Select a line item by choosing the checkbox in the first column. |  |  |
| 5 | Unblock | Choose Unblock for Payment from the options in the view. | The system displays an Items Changed notification. |  |
| 6 | Review | Select the row for the document that was unblocked and choose Edit Line Items. | The Edit 1 Line Item view is displayed. |  |
| 7 | Edit | In the Payment Data section, make the following entry and choose OK:Item Payment Block: (Free for payment) |  |  |

#### Display Customer Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity provides an overview of the payments and customer account balances.

Prerequisite

Invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Customer Balances (F0703A). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100100Company Code: 3310Fiscal Year: <Current Year> | A table shows the open balances per month for the year selected.The balances are displayed for the selected fiscal year. |  |
| 4 | Explore Balance Views | Choose the Balances, Special G/L, or Compare tabs to see the different views of the customer balance. | The different views of customer balances are displayed. |  |

### Payment Run

#### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be collected.

Prerequisite

Invoices are posted using customer 33100100 and are open for payment.

Don't include customer and invoices to be paid in any other payment Identification run, so they can be paid.

For more information, see the Business Conditions section in this document.

Invoices are past due. Use the Customer Invoice Payment Preparation procedure to change the payment terms and/or due date of an invoice so it can be paid.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Add | Choose the Create Parameter button. | The New Parameter dialog box displays. |  |
| 4 | Data Entry | Make the following entries:Run Date: <today's date>Identification: any five-character description, for example, DIRD1and choose Create. | An entry input view displays. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <Today's date>Docs Entered Up To: <Today's date>Customers Items Due By: <Today's date + 5 days>Additional Log: ONPayment Controls sectionCompany Code: 3310Next Payment Date: <Today's date + 5 days>Payment Method: For example, ENote For the Payment Method field, verify that the payment method is valid in the customer master record.Open Item Selection section:Customer: 33100100 |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, on the Open Item Selection populate any of the available Free Selection fields:For example, from the dropdown, selectDocument Number (BKPF-BELNR) and enter a <Document Number>. |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays a Parameter has been saved notification. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Select the row of the identification to process and choose Schedule > Proposal . | The Schedule Proposal dialog box displays. |  |
| 9 | Data Entry | Make the following entries:Start Date: <Today's date>Start immediately: Selectedand choose Schedule. | A Proposal has been scheduled notification displays.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposals Processed tab. |  |  |
| 11 | Display | Choose Go. | The proposal is displayed in the list. |  |

#### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be collected.

|  |
| --- |
| Caution Ensure that no other Payment Run Identification Proposals are pending to be executed that use the same supplier as the proposal created in previous procedure. If other proposals like this exist, those must be processed or deleted, otherwise no payment proposal is generated for your proposal |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Revise Payment Proposals (F0771). |  |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select | From the Open column in the proposal, choose the > (Open) button to edit (for example, DIRD1). | The Schedule Payment Proposal view of selected Identification displays. |  |
| 5 | Edit payment | In the Payments tab, select the row to edit and choose the Edit Payment button. | The Edit Payment dialog box displays. |  |
| 6 | Make Entries | Change the options:Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Instruction Key: <key>Note Some countries/regions don't use instruction keys. If this applies to your country/region, ignore the field.Due Date: <date>and choose OK to continue. |  |  |
| 7 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You can unblock or reallocate and pay them by using the option buttons. |  |  |

#### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity releases the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Go | Choose Go. | A list of all payment runs displays. |  |
| 4 | Proposal Processing | Choose the Proposals Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, DIRD1) and choose Schedule Payment. | The Schedule Payment view displays. |  |
| 6 | Schedule Payment | Make the following entries :Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system displays the Payment has been scheduled message. The status changes to Payment Posted. The log displays how many postings were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't display, choose the Settings button. Select the Log field and choose OK. | The log displays how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>). | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on.Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (for example, payment document, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

#### BCM Batch Creation (Optional)

Purpose

The creation of the Cross-Payment run in the BCM Batch is done automatically after the payment is initiated.

Procedure

This step is done automatically.

### Payment Medium

#### Create Payment Medium

Prerequisites

You executed the [Define Payment Medium Format Variants](#unique_7) [page ] 7 procedure in the Preliminary Steps section. To generate the payment medium, you must have activated one or both of the following scope items:

- Bank Integration with File Interface (1EG)
- Bank Integration with SAP Multi-Bank Connectivity (16R)

Procedure

The payment medium is created automatically. To review the relevant payment medium, do the following:

- If payment used Bank 2, follow the procedures described in Bank Integration with File Interface (1EG) test script.
- If payment used Bank 1, follow the procedures described in Bank Integration with SAP Multi-Bank Connectivity (16R) test script.

|  |
| --- |
| Note For payment receipt, execute the Bank Statement procedure described in the Basic Cash Operations (BFB), test script. |

The batch item status should be Payment Medium Created.

### Payment Review

#### View Payment List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment list.

Prerequisite

You executed a payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payment Lists (S_P99_41000099). |  |  |
| 3 | Selection | Enter the following:Program run date: <Date of payment run>Identification feature: <Identification of payment run>Proposal run only: Only select to display data that comes from the payment proposal, not from the paymentNote Additional fields are available for selection. Enter or modify fields according to your requirements. |  |  |
| 4 | Execute | Choose Execute.After reviewing the list, choose Exit to return to Payment List view. | Payment list displays. |  |

### Invoice Management Reporting

#### Overdue Receivables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the status of overdue items. Different predelivered graphs are available.

Prerequisite

Open invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Overdue Receivables - Today (F1747). | The Overdue Receivables view provides a graphical overview of the overdue receivables. |  |
| 3 | Explore Receivables | To explore your options, a dropdown menu (default value of By Due Period) provides different options for viewing the data by table or chart.Other buttons allow different visualization options. | A graph or list is displayed according to your selections. |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/19M_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 49,739 chars in the whole document
