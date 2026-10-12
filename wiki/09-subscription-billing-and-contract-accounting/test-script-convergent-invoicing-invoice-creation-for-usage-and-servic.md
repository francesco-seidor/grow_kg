---
id: 09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-invoice-creation-for-usage-and-servic
title: "Test Script: Convergent Invoicing – Invoice Creation for Usage and Service (2BG_AE) (2BG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (scope item 2BG, AE) for Convergent Invoicing: billable items, billing, invoicing, clarification, reversal, with preliminary config steps."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/recurring-and-one-off-billing]
aliases: [2BG_S4CLD2608_BPD_EN_AE]
keywords: ["Convergent Invoicing: Recurring, One-Off and Usage…", convergent invoicing, billable items, billing process, invoicing process, clarification cases, discounting, accrual deferral postings, invoice reversal, invoice printing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BG_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-810
topic: 09-subscription-billing-and-contract-accounting/recurring-and-one-off-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Convergent Invoicing – Invoice Creation for Usage and Service (2BG_AE) (2BG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Convergent Invoicing: Recurring, One-Off and Usage Billing, Invoice Correction** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Convergent Invoicing – Invoice Creation for Usage and Service (2BG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232848900)

[2 Prerequisites 5](#_Toc232848901)

[2.1 Additional Manual Configuration 5](#_Toc232848902)

[2.2 System Access 5](#_Toc232848903)

[2.3 Roles 5](#_Toc232848904)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232848905)

[2.5 Business Conditions 7](#_Toc232848906)

[2.6 Preliminary Steps 7](#_Toc232848907)

[2.6.1 Preliminary Steps Relevant to Discounting (Optional) 7](#_Toc232848908)

[2.6.1.1 Define Filters for Billable Items (Optional) 7](#_Toc232848909)

[2.6.1.2 Define Discount / Charge Key (Optional) 8](#_Toc232848910)

[2.6.1.3 Assign Keys for Across-the-Board Discounts (Optional) 11](#_Toc232848911)

[2.6.2 Preliminary Steps Relevant to Clarification (Optional) 13](#_Toc232848912)

[2.6.2.1 Define Invoicing Category (Optional) 13](#_Toc232848913)

[2.6.2.2 Define Specifications for Determination of Bill Form (Optional) 15](#_Toc232848914)

[2.6.2.3 Maintain Clarification Reasons (Optional) 17](#_Toc232848915)

[2.6.2.4 Define Checks for Source Document (Optional) 19](#_Toc232848916)

[2.6.2.5 Assign Checks for Source Document (Optional) 21](#_Toc232848917)

[2.6.2.6 Define Checks for Invoicing Document (Optional) 23](#_Toc232848918)

[2.6.2.7 Assign Checks for Invoicing Document (Optional) 26](#_Toc232848919)

[2.6.3 Preliminary Steps Relevant to Accrual/Deferral Posting Individual Procedure (Optional） 28](#_Toc232848920)

[2.6.3.1 Define Types of Accrual/Deferral Item 28](#_Toc232848921)

[2.6.4 Preliminary Steps Relevant to Lock Reasons for Invoicing Requests (Optional) 29](#_Toc232848922)

[2.6.4.1 Assign Lock Reasons for Invoicing Requests to Reasons for Reversal of Invoicing Documents 29](#_Toc232848923)

[2.6.5 Preliminary Steps Relevant to Invoicing Payment by Link (Optional) 31](#_Toc232848924)

[2.6.5.1 Define Specifications for Payment Method/Payment Form Control 31](#_Toc232848925)

[3 Overview Table 34](#_Toc232848926)

[4 Test Procedures 36](#_Toc232848927)

[4.1 Create Billable Items 36](#_Toc232848928)

[4.1.1 Option 1: Upload Billable Items 36](#_Toc232848929)

[4.1.2 Option 2: Invoke Create Billable Items SOAP API 37](#_Toc232848930)

[4.2 Reverse Billable Item (Optional) 38](#_Toc232848931)

[4.3 Perform Billing Process 39](#_Toc232848932)

[4.3.1 Option 1: Perform Billing Process (Mass Run) 40](#_Toc232848933)

[4.3.2 Option 2: Perform Billing Process (Individual Run) 41](#_Toc232848934)

[4.4 Perform Billing Process for Discounting (Optional) 42](#_Toc232848935)

[4.4.1 Option 1: Perform Billing Process for Discounting (Mass Run) 43](#_Toc232848936)

[4.4.2 Option 2: Perform Billing Process for Discounting (Individual Run) 44](#_Toc232848937)

[4.5 Display Billing Document (Optional) 46](#_Toc232848938)

[4.6 Clarify Clarification Case Relevant to Billing Document (Optional) 46](#_Toc232848939)

[4.7 Perform Invoicing Process for Accruals / Deferrals and Customer Invoicing (Optional) 47](#_Toc232848940)

[4.7.1 Perform Invoicing Process for Accrual / Deferral Postings (Individual Run) 48](#_Toc232848941)

[4.7.2 Perform Invoicing Process for Customer Invoicing (Individual Run) 49](#_Toc232848942)

[4.8 Perform Invoicing Process 51](#_Toc232848943)

[4.8.1 Option 1: Perform Invoicing Process (Mass Run) 51](#_Toc232848944)

[4.8.2 Option 2: Perform Invoicing Process (Individual Run) 53](#_Toc232848945)

[4.9 Clarify Clarification Case Relevant to Invoicing Document (Optional) 54](#_Toc232848946)

[4.10 Display Invoicing Document (Optional) 55](#_Toc232848947)

[4.11 Print Invoicing Document (Optional) 56](#_Toc232848948)

[4.12 Reverse Invoicing Document (Optional) 58](#_Toc232848949)

[4.13 SII Outgoing Invoice Registration (Optional) 59](#_Toc232848950)

[5 Appendix 61](#_Toc232848951)

[5.1 Process Integration 61](#_Toc232848952)

[5.1.1 Preceding Processes 61](#_Toc232848953)

[5.1.2 Succeeding Processes 61](#_Toc232848954)

[5.2 CSV Template Creation 62](#_Toc232848955)

[5.2.1 Data Item Selection for Paid and Unpaid Service 62](#_Toc232848956)

[5.2.2 Sample Data for Accrual / Deferral Postings 63](#_Toc232848957)

[5.3 Data Archiving 64](#_Toc232848958)

[5.3.1 Maintain Audit Area 64](#_Toc232848959)

[5.3.2 Assign ILM Object to Audit Area 64](#_Toc232848960)

[5.3.3 Maintain ILM Policies and Rules 66](#_Toc232848961)

[5.4 Periodic Invoicing 67](#_Toc232848962)

## Purpose

Overview

This process lets you create a consolidated customer invoice from multiple input channels in a high-volume scenario. Billable data received from external channels is stored in the format of billable items.

The process enables the creation of billing and invoicing documents using billable items:

- Received from external systems
- Created from rating
- Created from billing plan
- Created from invoice corrections
- Imported from spreadsheets

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2BG_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9f772b5fdf4e7d85135bc5105de1fd72)

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
| Invoicing Specialist (Convergent Invoicing) | SAP_BR_INVOICING_SPEC_CINV | Convergent Invoicing / Subscription Billing | SAP_BR_INVOICING_SPECIALIST_CINV / SAP_CEC_SPT_SUBSCR_BILLG_SPCLST_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Administrator (Convergent Invoicing) | SAP_BR_INVOICING_ADMIN_CINV | Administration - Convergent Invoicing | SAP_BR_INVOICING_ADMIN_CINV |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner and Contract Account must be created. |
| 2AR - Setting Up Contract Accounting – Master Data and Basic Functions | If you want to use Credit Card and Payment Service Provider functions, please refer to step Configuration Items for Digital Payments. |
| 2BI - Contract Accounting – Customer Initiated Payments | If you want to offer customers payment via a link within the invoice, please finish the Prerequisite in step Process Payments Paid via Link. |
| 2BK - Contract Accounting – Daily and Monthly Closing | If you want to enable the write-off feature in invoicing, please make sure 2BK is within scope to install the necessary configuration settings in contract accounting.For more information, please refer to the document: [Write Off](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1a561330b0fe4990b9566655770746dd/be0591f0ae5b4f608660b8b7799df9c8.html?version=LATEST&locale=en-US). |

### Preliminary Steps

#### Preliminary Steps Relevant to Discounting (Optional)

##### Define Filters for Billable Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the filters for billable item. This is only relevant to Discounting. If Discounting is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open Filters for Billable Items. |  |  |
| 3 | Create Filter | On the Filter for Billable Items Change (Customizing Maintenance) screen, choose Create FilterOn the Create Filter screen, make the entries as below then choose Continue1. Filter: <your filter>2. Name: <name>On the Change: Filter <your filter> screen, choose Billable Item Type from Work Structure for Selection (Across Statues) and make the entries as below then choose Save.1. Billable Item Type: Y001On the Filter for Billable Items Change (Customizing Maintenance) screen, choose Save. | The filter is created. Record the filter name. |  |

##### Define Discount / Charge Key (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the discount key. This is only relevant to Discounting. If Discounting is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Discount/Charge Key | On the Configure Your Solution: Realize Phase screen, search Define Key for Discounts/Charges on Billable Items, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Discounts and Charges on Billable Items screen, choose Configure on the line of configuration step with name Define Key for Discounts/Charges on Billable Items. |  |  |
| 5 | Create Discount Key | On the Discounts/Charges on Billable Items Display screen, choose Create, and make the entries as below:Key: The discount keyUse: DiscountDescription: <Description>Processing Level: 0000Time of Calculation: <leave it empty or 1>Currency: <the currency>In the Calculation tab, make the following entries:Basis Determ: Prepared Filter for Billable ItemsFilter: The filter you created in [Define Discount / Charge Key (Optional)](#unique_9) [page ] 8RuleType: StandardCalc.Type: Percentage%: 10Choose Save. | The discount key is defined.Note If you set Time of Calculation to 1, you can skip of [Perform Billing Process for Discounting (Optional)](#unique_10) [page ] 42 The Discount and Service Usage will be created within one Billing Document. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Discount/Charge Key | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Key for Discounts/Charges on Billable Items.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create Discount Key | On the Discounts/Charges on Billable Items Display screen, choose Create, and make the entries as below:Key: The discount keyUse: DiscountDescription: <Description>Processing Level: 0000Time of Calculation: 0 or 1In the Calculation tab, make the following entries:Basis Determ: Prepared Filter for Billable ItemsFilter: The filter you created in [Define Discount / Charge Key (Optional)](#unique_9) [page ] 8RuleType: StandardCalc.Type: Percentage%: 10Choose Save. | The discount key is defined.Note If you set Time of Calculation to 1, you can skip of [Perform Billing Process for Discounting (Optional)](#unique_10) [page ] 42 The Discount and Service Usage will be created within one Billing Document. |  |

##### Assign Keys for Across-the-Board Discounts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the discount key. This is only relevant to Discounting. If Discounting is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241) | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version | The Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Keys for Across-the-Board Discounts | On the Configure Your Solution: Realize Phase screen, search Assign Keys for Across-the-Board Discounts on Billable Items, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Discounts and Charges on Billable Items screen, choose Configure on the line of configuration step with name Assign Keys for Across-the-Board Discounts on Billable Items. |  |  |
| 5 | Assign discount key | Choose Create.In the Create dialog, make the entries as below.Billing Type: Billing TypeSubprocess: SubprocessDiscount/Charge Key: The discount key you created in [Define Discount / Charge Key (Optional)](#unique_9) [page ] 8Choose Continue.Calculation Level: 02Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Keys for Across-the-Board Discounts | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Keys for Across-the-Board Discounts on Billable Items.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign discount key | Choose Create.In the Create dialog, make the entries as below.Billing Type: <Billing Type>Subprocess: <Subprocess>Discount/Charge Key: The discount key you created in [Define Discount / Charge Key (Optional)](#unique_9) [page ] 8Choose Continue:Calculation Level: 02Choose Save. |  |  |

#### Preliminary Steps Relevant to Clarification (Optional)

##### Define Invoicing Category (Optional)

Purpose

In this step, you define the invoicing category which can be used at following steps that are relevant to Clarification. If Clarification is out of your scope, you can skip this step.

|  |
| --- |
| Note Please also assign your defined invoicing category to the contract account you are using to verify clarification. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Invoicing Categories | On the Configure Your Solution: Realize Phase screen, search Define Invoicing Categories, choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Invoicing screen, choose Configure on the line of configuration step with name Define Invoicing Categories. |  |  |
| 5 | Maintain Invoicing Categories | On the Define Invoicing Categories: Change screen, choose New Entries, and make the entries as below:Inv.Cat.: <Invoicing Category>Text of Inv.Cat: <description for Invoicing Category>Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Define Invoicing Categories | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Invoicing Categories and create the following settings. |  |  |
| 3 | Maintain Invoicing Categories | On the Define Invoicing Categories: Change screen, choose New Entries, and make the entries as below:Inv.Cat.: <Invoicing Category>Text of Inv.Cat: <description for Invoicing Category>Choose Save. |  |  |

##### Define Specifications for Determination of Bill Form (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the Specifications for Determination of Bill Form for Invoicing Category you defined in the last step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Clarification Reasons | On the Configure Your Solution: Realize Phase screen, search Define Specifications for Determination of Bill Form, and then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution – Invoicing – Print screen, choose Configure on the line of configuration step with name Define Specifications for Determination of Bill Form. |  |  |
| 5 | Maintain Parameters to Define Specifications for Determination of Bill From | On the Maintain Invoicing: Determination of Billing Form: Overview screen, choose Create.Make the entries as below:Invoicing Process: <the Invoicing Process>, for example, Y1Invoicing Type: <the Invoicing Type>, for example, Y1Invoicing Category: <the Invoicing Category>, for example, the invoicing category you created at the last stepStandard CoCode: <the Company Code>, for example, 3310Alt. Form Determin.: <the Determination Characteristic for Alternative Invoice Form>, for example, leave it empty.Form ID: <the Form ID for Invoice Printing>Form ID for Dialog: <the ID of Form for Invoice Printing in Dialog Mode>Form ID: <the Form ID for Attached Payment Medium>Choose Save. | The Specifications for Determination of Bill Form has been created.Note The Bill Form is country-dependent. Please choose the Bill Form accordingly. If there is no country specific form provided, you can choose to use Y001. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Define Invoicing Categories | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Specifications for Determination of Bill Form and create the following settings. |  |  |
| 3 | Maintain Parameters to Define Specifications for Determination of Bill From | On the Maintain Invoicing: Determination of Billing Form: Overview screen, choose Create.Make the entries as below:Invoicing Process: <the Invoicing Process>, for example, Y1Invoicing Type: <the Invoicing Type>, for example, Y1Invoicing Category: <the Invoicing Category>, for example, the invoicing category you created at the last stepStandard CoCode: <the Company Code>, for example, 3310Alt. Form Determin.: <the Determination Characteristic for Alternative Invoice Form>, for example, leave it empty.Form ID: <the Form ID for Invoice Printing>Form ID for Dialog: <the ID of Form for Invoice Printing in Dialog Mode>Form ID: <the Form ID for Attached Payment Medium>Choose Save. | The Specifications for Determination of Bill Form has been created.Note The Bill Form is country-dependent. Please choose the Bill Form accordingly. For example, for DE and US, you can choose to use Y001. |  |

##### Maintain Clarification Reasons (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the clarification reason. This is only relevant to Clarification. If Clarification is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is screen is displayed |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Maintain Clarification Reasons | On the Configure Your Solution: Realize Phase screen, search Maintain Clarification Reasons, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Clarification Processing screen, choose Configure on the line of configuration step with name Maintain Clarification Reasons. |  |  |
| 5 | Maintain Clarification Reasons | On the Maintain Clarification Reasons: Change screen, choose New Entries and make the entries as below then choose Save.CC.Cat.: <01> or <03>Clarific.Reason : <Clarification Reason>Clarification Rsn Txt: <Clarification Reason Descrition> | The two clarification reasons were created.The clarification reason for source document.Eg: CC.Cat: 01Clarific.Reason: Z1Clarification Rsn Txt: Incorrect AmountThe clarification reason for Invoicing documentEg: CC.Cat: 03Clarific.Reason: Z2Clarification Rsn Txt: Incorrect Amount |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Maintain Clarification Reasons | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Maintain Clarification Reasons and create the following settings. |  |  |
| 3 | Maintain Clarification Reasons | On the Maintain Clarification Reasons: Change screen, choose New Entries and make the entries as below then choose Save.CC.Cat.: <01 or 03>Clarific.Reason : <Clarification Reason>Clarification Rsn Txt: <Clarification Reason Descrition> | The two clarification reasons were created.The clarification reason for source document.Eg: CC.Cat: 01Clarific.Reason: Z1Clarification Rsn Txt: Incorrect AmountThe clarification reason for Invoicing documentEg: CC.Cat: 03Clarific.Reason: Z2Clarification Rsn Txt: Incorrect Amount |  |

##### Define Checks for Source Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the checks for source document. This is only relevant to Clarification. If Clarification is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Checks for Source Document | On the Configure Your Solution: Realize Phase screen, search Define Checks for Source Document, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Clarification Processingscreen, choose Configure on the line of configuration step with name Define Checks for Source Document. |  |  |
| 5 | Define check for source document | On the Define Checks for Source Document: Change screen, choose New Entries and make the entries as below:Source Doc.Cat.: Billing DocumentCheck: <the key of check>, for example, CKSRCSrcDocCheckText: <Explanatory Text for Source Document Check>, for example, Amount Exceeds LimitClarific.Reason: <the clarification reason>, for example, Z1, the clarification reason for source document you created at previous step.Choose Amount Limit Values, choose New Entries and then make the entries as below:Currency: <currency>Valid From: <valid from date>Text: <description to amount check>, for example, Check of Amount RangeAmount From: <amount floor>, for example, 0Amount To: <amount celling>, for example, 50Choose Save. | CKSRC, the Check for Source Document is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Checks for Source Document | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Checks for Source Document and create the following settings. |  |  |
| 3 | Define check for source document | On the Define Checks for Source Document: Change screen, choose New Entries and make the entries as below:Source Doc.Cat.: Billing DocumentCheck: <the key of check>, for example, CKSRCSrcDocCheckText: <Explanatory Text for Source Document Check>, for example, Amount Exceeds LimitClarific.Reason: <the clarification reason>, for example, Z1, the clarification reason for source document you created at previous step.Choose Amount Limit Values, choose New Entries and then make the entries as below:Currency: <currency>Valid From: <valid from date>Text: <description to amount check>, for example, Check of Amount RangeAmount From: <amount floor>, for example, 0Amount To: <amount celling>, for example, 50Choose Save. | CKSRC, the Check for Source Document is defined. |  |

##### Assign Checks for Source Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the checks for source document. This is only relevant to Clarification. If Clarification is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version | The Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Checks for Source Document | On the Configure Your Solution: Realize Phase screen, search Assign Checks for Source Document, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Clarification Processing screen, choose Configure on the line of configuration step with name Assign Checks for Source Document. |  |  |
| 5 | Assign Check for Source Document | On the Maintain Invoicing: Assign Check to Source Document: Overview screen, choose Create, and then make the entries as below:Source Document: INVBISource Document Type: 001Check Source Doc.: <the check for source document> For example, CKSRCInvoicing Category: <Invoicing Category>Choose Continue.Seq.Number: <sequence number>Choose Save. | The check for source document you created at previous step has been assigned. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Checks for Source Document | Go to the Business Processes Configuration app and search for the following activity: Assign Checks for Source Document.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Check for Source Document | On the Maintain Invoicing: Assign Check to Source Document: Overview screen, choose Create, and then make the entries as below:Source Document: INVBISource Document Type: 001Check Source Doc.: <the check for source document> For example, CKSRCInvoicing Category: <Invoicing Category>Choose Continue.Seq.Number: <sequence number>Choose Save. | The check for source document you created at previous step has been assigned. |  |

##### Define Checks for Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the checks for invoicing document. This is only relevant to Clarification. If Clarification is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solutiondisplayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version.The Configure Your Solution screen is displayed. |  |  |
| 4 | Open Define Checks for Invoicing Document | On the Configure Your Solution: Realize Phase screen, search Define Checks for Invoicing Document, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Clarification Processing screen, choose Configure on the line of configuration step with name Define Checks for Invoicing Document. |  |  |
| 5 | Define check for invoicing document | On the Define Checks for Invoicing Document: Change screen, choose New Entries and then make the entries as below:Invoicing Check: <the key of check> For example, CKINVInv.Doc.Check Text: <Explanatory Text for Invoicing Document Check> For example, Amount Exceeds LimitClarific.Reason: <the clarification reason> For example, Z2, the clarification reason for invoicing document you created at previous step.With Control Doc.: Simulated Control DocumentChoose Amount Limit Values, choose New Entries, and then make the entries as below:Currency: <currency>Valid From: <valid from date>Text: <description to amount check> For example, Check of Amount RangeAmount From: <amount floor> For example, 50Amount To: <amount celling> For example, 100Choose Save. | CKINV, the Check for Invoicing Document is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Checks for Invoicing Document | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Checks for Invoicing Document and create the following settings. |  |  |
| 3 | Define check for invoicing document | On the Define Checks for Invoicing Document: Change screen, choose New Entries, and then make the entries as below:Invoicing Check: <the key of check> For example, CKINVInv.Doc.Check Text: <Explanatory Text for Invoicing Document Check> For example, Amount Exceeds LimitClarific.Reason: <the clarification reason> For example, Z2, the clarification reason for invoicing document you created at previous step.With Control Doc.: Simulated Control DocumentChoose Amount Limit Values, choose New Entries, and then make the entries as below:Currency: <currency>Valid From: <valid from date>Text: <description to amount check> For example, Check of Amount RangeAmount From: <amount floor> For example, 50Amount To: <amount celling> For example, 100Choose Save. | CKINV, the Check for Invoicing Document is defined |  |

##### Assign Checks for Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the checks for invoicing document. This is only relevant to Clarification. If Clarification is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution (F1241)screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Assign Checks for Invoicing Document | On the Configure Your Solution: Realize Phase screen, search Assign Checks for Invoicing Document, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution - Clarification Processingscreen, choose Configure on the line of configuration step with name Assign Checks for Invoicing Document |  |  |
| 5 | Open Assign Checks for Source Document | On the Maintain Invoicing: Assign Check to Invoicing Document: Overview screen, choose Create and then make the entries as below:Invoicing Process: <the invoicing process> For example, Y1Invoicing Type: <the invoicing type> For example, Y1Invoicing Category: <Invoicing Category>Invoicing Check: <the check for invoicing document> For example, CKINVChoose Continue.Seq.Number: <sequence number>Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Checks for Invoicing Document | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Assign Checks for Invoicing Document and create the following settings. |  |  |
| 3 | Open Assign Checks for Source Document | On the Maintain Invoicing: Assign Check to Invoicing Document: Overview screen, choose Create and then make the entries as below:Invoicing Process: <the invoicing process> For example, Y1Invoicing Type: <the invoicing type> For example, Y1Invoicing Category: <Invoicing Category>Invoicing Check: <the check for invoicing document> For example, CKINVChoose Continue.Seq.Number: <sequence number>Choose Save. |  |  |

#### Preliminary Steps Relevant to Accrual/Deferral Posting Individual Procedure (Optional）

##### Define Types of Accrual/Deferral Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the type of accrual/deferral item. This is only relevant to Accrual /Deferral Postings. If Accrual /Deferral Postings is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241) . | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.If country version needs to be added, choose Set Country Version | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Types of Accrual/Deferral Items | On the Configure Your Solution: Realize Phase screen, search Define Types of Accrual/Deferral Items , then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution – Define Types of Accrual/Deferral Items screen, choose Configure on the line of configuration step with name Define Types of Accrual/Deferral Items. |  |  |
| 5 | Create Type of Accrual /Deferral Items | On the Define Types of Accrual/Deferral Items: Change screen, choose New Entries and make entries as below:A/D Posting Type: <the type of Accrual / Deferral Postings>Txt f.Acc./Def.Typ: <description>Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open Define Types of Accrual/Deferral Items | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Search for Define Types of Accrual/Deferral Items and create the following settings. |  |  |
| 3 | Create Type of Accrual /Deferral Items | On the Define Types of Accrual/Deferral Items: Change screen, choose New Entries and make entries as below:A/D Posting Type: <the type of Accrual / Deferral Postings>Txt f.Acc./Def.Typ: <description>Choose Save. |  |  |

#### Preliminary Steps Relevant to Lock Reasons for Invoicing Requests (Optional)

##### Assign Lock Reasons for Invoicing Requests to Reasons for Reversal of Invoicing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign the Lock Reason for Invoicing Request to Reason for Reversal of Invoicing Document. Once user uses it to reverse invoicing document and redo invoicing, the lock reasons for Invoicing Requests take effect to break the invoicing process. If this is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Reason for Reversal of Invoicing Documents | On the Configure Your Solution: Realize Phase screen, search Define Reasons for Reversal of Invoicing Documents, then choose Search.Select the line of the item and go to the next screen.On the Configuration Your Solution – Invoicing – Reversal screen, choose Configure on the line of configuration step with name Define Reasons for Reversal of Invoicing Documents. |  |  |
| 5 | Assign Lock Reason to Reversal Reason | On the Define Reasons for Reversal of Invoicing Do..: Change screen, make the maintenance as below:RR: <the reversal reason>, for example, S1Lock Reason: <the lock reason>, for example, S1Choose Save. | The Lock Reason for Invoicing Request S1 has been assigned to the Reason for Reversal of Invoicing Document S1. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Reason for Reversal of Invoicing Documents | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert.Search for Define Reasons for Reversal of Invoicing Documents and create the following settings. |  |  |
| 3 | Assign Lock Reason to Reversal Reason | On the Define Reasons for Reversal of Invoicing Do..: Change screen, make the maintenance as below:RR: <the reversal reason>, for example, S1Lock Reason: <the lock reason>, for example, S1Choose Save. | The Lock Reason for Invoicing Request S1 has been assigned to the Reason for Reversal of Invoicing Document S1. |  |

#### Preliminary Steps Relevant to Invoicing Payment by Link (Optional)

##### Define Specifications for Payment Method/Payment Form Control

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the specifications for Payment Methods/Payment Form Control. This is only relevant to Invoicing Payment by Link. If Invoicing Payment by Link is out of your scope, you can skip this step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Configuration Expert. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Define Specifications for Payment Method/Payment Form Control | On the Configure Your Solution: Realize Phase screen, search Define Specifications for Payment Method/Payment Form Control, then choose Enter.Select the line of the item and go to the next screen.On the Configuration Your Solution – Invoicing – Additional functions screen, choose Configure on the line of configuration step with name Define Specifications for Payment Method/Payment Form Control. |  |  |
| 5 | Create Specifications for Payment Method/Payment Form Control | On the Maintain Invoicing: Repayment Method/Payment Form Control: Overview screen, choose Create.In the Create dialog, make the entries as below:Invoicing Process: <Invoicing Process>, for example, Y1Invoicing Type: <Invoicing Type>, or *Invoicing Category: <Invoicing Category>Paying Company Code: <Paying Company Code>, or *Dir. Debit/Cash Payer: <Cash Payment or Direct Debit>or *Debit/Credit Ind.: <Invoice Final Amount is receivable or credit>, or *Choose Continue and on the Maintain Invoicing: Repayment Method/Payment Form Control: Detail scr. screen, make the entries as below:Payment Methods List: <Payment Method List>, or leave it emptyCreate Payment Form: <Yes or No>, for example, XCreate Payment Ref.: <Yes or No>, or leave it emptyChoose Save. | The Specifications for Payment Method/Payment Form Control is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Checks for Invoicing Document | Go to the Business Processes Configuration app, you can search for a configuration activity and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert.Search for Define Specifications for Payment Method/Payment Form Control and create the following settings. |  |  |
| 3 | Create Specifications for Payment Method/Payment Form Control | On the Maintain Invoicing: Repayment Method/Payment Form Control: Overview screen, choose Create.In the Create dialog, make the entries as below:Invoicing Process: <Invoicing Process>, for example, Y1Invoicing Type: <Invoicing Type>, or *Invoicing Category: <Invoicing Category>, or *Paying Company Code: <Paying Company Code>, or *Dir. Debit/Cash Payer: <Cash Payment or Direct Debit>, or *Debit/Credit Ind.: <Invoice Final Amount is receivable or credit>, or *Choose Continue and on the Maintain Invoicing: Repayment Method/Payment Form Control: Detail scr. screen, make the entries as below:Payment Methods List: <Payment Method List>, or leave it emptyCreate Payment Form: <Yes or No>, for example, XCreate Payment Ref.: <Yes or No>, or leave it emptyChoose Save. | The Specifications for Payment Method/Payment Form Control is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Option 1: Upload Billable Items](#unique_23) [page ] 36 | Invoicing Specialist (Convergent Invoicing) | Upload Billable Items (F4664) | Billable Item is created. |
| [Option 2: Invoke Create Billable Items SOAP API](#unique_24) [page ] 37 | N/A | N/A | Billable Item is created by invoking create billable items SOAP API. |
| [Reverse Billable Item (Optional)](#unique_25) [page ] 38 | Invoicing Specialist (Convergent Invoicing) | Manage Billable Items (F2621) | Billable Item is reserved. |
| [Option 1: Perform Billing Process (Mass Run)](#unique_26) [page ] 40 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created. |
| [Option 2: Perform Billing Process (Individual Run)](#unique_27) [page ] 41 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | Billing Document is created. |
| [Option 1: Perform Billing Process for Discounting (Mass Run)](#unique_28) [page ] 43 | Administrator (Convergent Invoicing) | Execute Billing - Mass Run (F3525) | Billing Document is created. |
| [Option 2: Perform Billing Process for Discounting (Individual Run)](#unique_29) [page ] 44 | Invoicing Specialist (Convergent Invoicing) | Execute Billing - Business Partner (FKKBIX_S) | Billing Document is created. |
| [Display Billing Document (Optional)](#unique_30) [page ] 46 | Invoicing Specialist (Convergent Invoicing) | Manage Billing Documents (F2250) | Billing Document is displayed. |
| [Clarify Clarification Case Relevant to Billing Document (Optional)](#unique_31) [page ] 46 | Invoicing Specialist (Convergent Invoicing) | Manage Clarification Cases (F2349) | The Clarification Case is clarified. |
| [Perform Invoicing Process for Accrual / Deferral Postings (Individual Run)](#unique_32) [page ] 48 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created. |
| [Perform Invoicing Process for Customer Invoicing (Individual Run)](#unique_33) [page ] 49 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created. |
| [Option 1: Perform Invoicing Process (Mass Run)](#unique_34) [page ] 51 | Administrator (Convergent Invoicing) | Execute Invoicing - Mass Run (F3524) | Invoicing Document is created. |
| [Option 2: Perform Invoicing Process (Individual Run)](#unique_35) [page ] 53 | Invoicing Specialist (Convergent Invoicing) | Execute Invoicing - Business Partner (FKKINV_S) | Invoicing Document is created. |
| [Clarify Clarification Case Relevant to Invoicing Document (Optional)](#unique_36) [page ] 54 | Invoicing Specialist (Convergent Invoicing) | Manage Clarification Cases (F2349) | The Clarification Case is clarified. |
| [Display Invoicing Document (Optional)](#unique_37) [page ] 55 | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | Invoicing Document is displayed. |
| [Print Invoicing Document (Optional)](#unique_38) [page ] 56 | Administrator (Convergent Invoicing) | Print Correspondence (F3537) | The invoicing document is printed out. |
| [Reverse Invoicing Document (Optional)](#unique_39) [page ] 58 | Invoicing Specialist (Convergent Invoicing) | Manage Invoicing Documents (F2048) | The invoicing document is reversed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Billable Items

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
| 2 | Access the App | Choose Upload Billable Items (F4664) tile. | The Upload Billable Items page is displayed. |  |
| 3 | Create Template | In the Upload Billable Items screen, make the following entries as below and choose Create Template.Upload Schema: CSV File for Billable Items |  |  |
| 4 | Choose Billable Item Class | In the Create Template screen, make the entries as below:Choose Billable Item Class: 0SAP |  |  |
| 5 | Choose Record Type | Based on the different service you want to create, please choose corresponding Record TypeTo unpaid service, you only need to choose Main ItemsTo paid service, you should choose Main Items and Payment Data Items |  |  |
| 6 | Choose Fields for Record Types | Based on the different service you want to create, please choose corresponding fields for Record Type.Please refer to Data Item Selection in the Appendix to choose fields of record type based on the service you want to create.Choose Download Template. | The items were chosen and saved successfully.Note The CSV file template can be created based on paid service and unpaid service.To paid service, the payment data item should be chosen besides main items.Based on the different payment data item selected, the payment card information can be retrieved through CSV file or business partner master data. |  |
| 8 | Import CSV File | In the Upload Billable Items screen, make the entries as below:File Source: Choose Browse and find the file you edited.Choose Open to close the popup dialog of File Upload and upload the file you edited at step7 from native file system to SAP file system. | The file you edited at step7 was uploaded to SAP system. |  |
| 9 | Read CSV File | Choose Read. | Log is provided to identify the csv file read error.If there is no error, the field and filed value of CSV file can be displayed at Preview section. You also can choose Edit to modify the value as your demands. |  |
| 10 | Load CSV File | Choose the entries you want to upload then choose Upload. | Before load data, you can make the modification to the individual field based on your request. |  |
| 11 | Display Log | Choose Show Application Log to display log. | From the log, you will see the billable item is created or not. |  |

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

### Reverse Billable Item (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the billable item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Billable Items (F2621) tile. | The Manage Billable Items page is displayed. |  |
| 3 | Display Billable Item | In the Manage Billable Items screen, make the following entries as below and choose Go buttonStatus: BillableBusiness Partner: <the required business partner>Contract Account: <the required contract account> | The billable item is displayed. |  |
| 4 | Choose Billable Item | In the Manage Billable Items screen, choose the billable item you want to reverse. | The billable item you want to reverse is chosen and you can check details of billable item at Billable Items of a Source Transaction screen. |  |
| 5 | Reverse Billable Item | Choose Reverse.If a Reversal Reason is asked, choose Reverse from the list, then choose Reverse. |  |  |

### Perform Billing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

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
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run screen is displayed |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: Y001 or Y002Contract Account: <the required contract account>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> | Note Billing Process of Y002 is used for immediately invoicing. If you choose Y002 as Billing Process to perform billing process. Chapter 4.5 Perform Invoicing Process can be skipped. |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access the located application job log. | The log of application job is displayed. From the log, you can see the result of application job.Note If you define and assign the check for Source Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, the corresponding Clarification Case will be created. |  |

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
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:Billing Process: Y001 or Y002Billing Date: <the current date>Contract Account: <the required contract account> | Note Billing Process of Y002 is used for immediately invoicing. If you choose Y002 as Billing Process to perform billing process. Perform Invoicing Process can be skipped. |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog.OrChoose Accept Document or Accept with Reservations at Check of Source Documents screen. | Note If you define and assign the check for Source Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, in Check of Source Documents, the Accept Document and Accept with Reservations will open for customer to choose.Accept Document - The Billing Document is created. The corresponding clarification case is created with status completeAccept with Reservations – The Billing Document is created. The corresponding clarification case is created with status to be clarified |  |

### Perform Billing Process for Discounting (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The discount base item is created during the billing process run against billable item Y001 in the previous step. In this step, you start up the billing process to create the billing document based on the discount base item. You can process with mass run or individual creation. Please note that this is only relevant to Discounting. If Discounting is out of your scope, you can skip this step.

#### Option 1: Perform Billing Process for Discounting (Mass Run)

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
| 2 | Access the App | Choose Execute Billing - Mass Run (F3525) tile. | The Execute Billing - Mass Run screen is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Billing (Mass Creation) page is displayed |  |
| 4 | Select Template | Make the following entries as below:Job Template; Billing (Mass Creation)Job Name; <job name>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Billing Process: SDISContract Account: <the required contract account>Simulation Run: <don’t choose>Billing Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Billing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. | The application job you want to find was located in the application jobs list. |  |
| 9 | Check Log | Choose Image of Log to access the located application job log. | The log of application job is displayed. From the log, you can see the result of application job.Note If you define and assign the check for Source Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, the corresponding Clarification Case will be created. |  |

#### Option 2: Perform Billing Process for Discounting (Individual Run)

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
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Execute Billing - Business Partner (FKKBIX_S) tile. | The Billing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Billing (Individual Creation), make the following entries as below:1. Billing Process: SDIS2. Billing Date: the current date3. Contract Account: the required contract account |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Choose Billable Item and Create Billing Units | In the Choose Billable Items and Creation of Billing Units dialog, choose Save, until you see the dialog Billing Ended. | A dialog Billing Ended is displayed. |  |
| 6 | Check Billing Document | Choose Continue (Enter) to leave the dialog.OrChoose Accept Document or Accept with Reservations at Check of Source Documents screen. | The billing document based on the discount base item is created.Note If you define and assign the check for Source Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, in Check of Source Documents, the Accept Document and Accept with Reservations will open for customer to choose.Accept Document – The Billing Document is created. The corresponding clarification case is created with status completeAccept with Reservations – The Billing Document is created. The corresponding clarification case is created with status to be clarified |  |

### Display Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display the billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Billing Documents (F2250) tile. | The Manage Billing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Billing Documents screen, make the following entries as below:Billing Document: <the billing document you want to display> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Billing Document | Choose the item searched out. | The billing document is displayed. |  |

### Clarify Clarification Case Relevant to Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you clarify the clarification case which is created when perform Billing Process. If clarification is out of the scope, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Clarification Cases. |  |  |
| 3 | Locate Clarification Case | In the Manage Clarification Cases screen, make the entries as below and choose Go:Business Partner: <business partner>Contract Account: <contract account>Status: <status> |  |  |
| 4 | Handle Clarification Case | In the Manage Clarification Cases screen, choose the clarification case you want to deal with.Choose Assign to Me and choose Navigation.In the Clarification Case screen, choose Complete to set the status to Completed. |  |  |

### Perform Invoicing Process for Accruals / Deferrals and Customer Invoicing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you create Sample Data based on Accrual /Deferral Postings while uploading Billable Item. This step is relevant, or you can skip it. In this step, you create invoice document based on the Accruals / Deferrals and Customer Invoicing. They have the same Source Document No. BILAC as Category of Source Document is relevant to Accruals / Deferrals. INVBI as Category is relevant to Customer Invoicing. Please proceed invoicing for them respectively with invoicing individual creation.

#### Perform Invoicing Process for Accrual / Deferral Postings (Individual Run)

Purpose

In this step, you create invoice document based on the billing document with BILAC as Category of Source Document. If you create Sample Data based on Accrual /Deferral Postings while uploading Billable Item. This step is relevant, or you can skip it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing) | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Execute Invoicing - Business Partner (FKKINV_S). | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <today>Posting Date: <today>Business Partner:<the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute.A dialog Selection of Source Documents is displayed. |  |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose the entry which source document category is BILAC.Choose Save. | A dialog Creation of Invoicing Units is displayed.Note Please record the Source Document No for the entry which source document category is BILAC. |  |
| 6 | Post Invoicing Document | In the Save invoicing document? dialog chooseYes, until you see the dialog Invoicing Ended. Ifyou choose Document, you can check thedocuments before posting. | A dialog Invoicing Ended is displayed.The invoicing document is posted. |  |
| 7 | Check Invoicing Document of Accrual /Deferral Postings | Choose Continue (Enter) to leave the dialog.OrChoose Continue Invoicing or Create Clarification Cases at Invoicing Document Check screen.Note If you define and assign the check for Invoicing Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, in Invoicing Document Check, the Continue Invoicing and Create Clarification Case will open for customer to choose. Continue Invoicing -- The Invoicing Document is created. Create Clarification Case – The Invoicing Document is not created. The corresponding clarification case is created with status to be clarified. Please proceed [Clarify Clarification Case Relevant to Invoicing Document (Optional)](#unique_36) [page ] 54 to create the invoicing document. |  |  |

#### Perform Invoicing Process for Customer Invoicing (Individual Run)

Purpose

In this step, you create invoice document based on the Customer Invoicing with INVBI as Category of Source Document and the same Source Document No. with Accruals/Deferrals Posting If you create Sample Data based on Accrual /Deferral Postings while uploading Billable Item. This step is relevant, or you can skip it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing) | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Execute Invoicing - Business Partner (FKKINV_S). | The Invoicing (Individual Creation) page is displayed. |  |
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | In the Selection of Source Documents dialog, choose the entry which Source Document Category is INVBI and Source Document No. is the one as you recorded in the previous steps when create invoicing document for accrual /deferral posting.Choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then click Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document? dialog choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed. The invoicing document is posted. |  |
| 7 | Check Invoicing Document of Accrual /Deferral Postings | Choose Continue (Enter) to leave the dialog.OrChoose Continue Invoicing or Create Clarification Cases at Invoicing Document Check screen.Note If you define and assign the check for Invoicing Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, in Invoicing Document Check, the Continue Invoicing and Create Clarification Case will open for customer to choose. Continue Invoicing -- The Invoicing Document is created. Create Clarification Case – The Invoicing Document is not created. The corresponding clarification case is created with status to be clarified. Please proceed [Clarify Clarification Case Relevant to Invoicing Document (Optional)](#unique_36) [page ] 54 to create the invoicing document. |  |  |

### Perform Invoicing Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

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
| 2 | Access the App | Choose Execute Invoicing - Mass Run (F3524). | The Execute Invoicing - Mass Run screen is displayed. |  |
| 3 | Create Application Job | Choose Create button to create a new application job. | The New Job: Invoicing (Mass Creation) page is displayed. |  |
| 4 | Select Template | Make the following entries as below:Job Template; Invoicing (Mass Creation)Job Name; <job name>Choose Step2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: chooseRecurrence Pattern: Single RunChoose Step3. |  |  |
| 6 | Maintain Parameters | Make the following entries as below:Prefix of Run ID: <Prefix of Run ID>Invoicing Process: Y1Business Partner: <the required business partner>Contract Account: <the required contract account>Simulation Run: <don’t choose>Document Date: <the current date>Posting Date: <the current date>Problem Class: <problem class> |  |  |
| 7 | Execute | Choose Schedule. | The job is running immediately. |  |
| 8 | Locate the job from application job list | In the Execute Invoicing - Mass Run screen, make the following entries as below:Date From-To: Today -1/+1 dayChoose Go button. |  |  |
| 9 | Check Log | Choose Image of Log to located the application job log. | The log of application job is displayed. From the log, you can see the result of application job.Note If you define and assign the check for Invoicing Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, the corresponding Clarification Case will be created. |  |

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
| 3 | Maintain Parameters | In the Invoicing (Individual Creation), make the following entries as below:Invoicing Process: Y1Document Date: <the current date>Posting Date: <the current date>Business Partner: <the required business partner>Contract Account: <the required contract account> |  |  |
| 4 | Execute | Choose Execute. | A dialog Selection of Source Documents is displayed. |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog, choose Save. | A dialog Creation of Invoicing Units is displayed if there are more than one source documents to be invoiced. You can choose All Together or All Individually, then click Save to continue. |  |
| 6 | Post Invoicing Document | In the Save invoicing document dialog, choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check thedocuments before posting. | A dialog Invoicing Ended is displayed.Invoicing document is posted. |  |
| 7 | Check Invoicing Document | Choose Continue (Enter) to leave the dialog.OrChoose Continue Invoicing or Create Clarification Cases at Invoicing Document Check screen. | Note If you define and assign the check for Invoicing Document at preliminary steps relevant to Clarification, the check might be triggered based on the settings you made. If the check does not pass, in Invoicing Document Check, the Continue Invoicing and Create Clarification Case will open for customer to choose.Continue Invoicing - The Invoicing Document is created.Create Clarification Case – The Invoicing Document is not created. The corresponding clarification case is created with status to be clarified. |  |

### Clarify Clarification Case Relevant to Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you clarify the clarification case which is created when perform Invoicing Process. If clarification is out of the scope, you can skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Clarification Cases tile. |  |  |
| 3 | Locate Clarification Case | In the Manage Clarification Cases screen, make the entries as below and choose Go:Business Partner: <business partner>Contract Account: <contract account>Status: <status>Choose the located Clarification Case and open it. | The located Clarification Case is displayed. |  |
| 4 | Perform Invoicing | In the Clarification Case screen, choose Invoice. |  |  |
| 5 | Select Source Documents | On the Selection of Source Documents dialog choose the billing document you want to perform invoicing and choose Save. |  |  |
| 6 | Post Invoicing Document | In the Invoicing Document Check screen, choose Continue InvoicingIn the Save invoicing document? dialog choose Yes, until you see the dialog Invoicing Ended. If you choose Document, you can check the documents before posting. | A dialog Invoicing Ended is displayed.The invoicing document is posted. |  |

### Display Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the created invoicing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the App | Choose Manage Invoicing Documents (F2048) tile. | The Manage Invoicing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Invoicing Documents screen, make the following entries as below:Invoicing Document: the invoicing document you want to display |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Display Invoicing Document | Choose the search out item. | The invoicing document is displayed.Note If you have implemented the Preliminary Steps Relevant to Invoicing Payment by Link and set up SAP Payment Service Provider accordingly, there is a QR code visible on invoicing document after pressing Print Preview. |  |

### Print Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you print the invoicing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad with your user credentials as Administrator (Convergent Invoicing) role assigned. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Choose Print Correspondence (F3537). | The Print Correspondence screen displays. |  |
| 3 | Create Job | On the Print Correspondence screen, choose Create. | The New Job: FI-CA: Print Correspondence screen displays. |  |
| 4 | Select Template | Make the following entries as below:Job Template: <FI-CA: Print Correspondence>Job Name: <FI-CA: Print Correspondence>Choose Step 2. |  |  |
| 5 | Maintain Schedule Options | Make the following entries as below:Start Immediately: selectRecurrence Pattern: Single RunChoose Step 3. |  |  |
| 6 | Maintain Parameters | In the New Job: FI-CA: Print Correspondence screen, make the entries as below:Prefix of Run ID: <Prefix of Run ID>Business Partner: <Select Business Partner number>Contract Account: <Select Contract Account number>Company Code: <company code>Correspondence Type: 0042Print Queue Name: <Select Print Queue ID>Actual Print: Selected |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Print Correspondence screen displays.One new application job is created with a status. |  |

### Reverse Invoicing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the invoicing document.

|  |
| --- |
| Note An invoicing document can only be reversed if all posting documents created for this document can be reversed. In particular, these posting documents must not contain clearing by clearing documents of a different transaction. For example, they must not have already been paid. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Invoicing Specialist (Convergent Invoicing). | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Invoicing Documents (F2048) tile. | The Manage Invoicing Documents page is displayed. |  |
| 3 | Maintain Parameters | In the Manage Invoicing Documents screen, make the following entries as below:Invoicing Document: <the invoicing document you want to reverse> |  |  |
| 4 | Execute | Choose Go. |  |  |
| 5 | Reverse Invoicing Document | In the Manage Invoicing Documents screen, choose the Invoicing Document in the search result list and choose Reverse.In the Reverse screen, make the entries as below:Reversal Reason: <select one from drop-down list>Choose Reverse. | The invoicing document is reversed.In the Manage Invoicing Documents screen, you can choose Reversed Documents from drop-down list to locate the reserved invoicing documentIn the Manage Invoicing Documents screen, you can choose Reversal Documents from drop-down list to locate the created invoicing document used to reverse your invoicing document.Note If you implement the preliminary steps relevant to the Invoicing Lock and use the reversal reason assigned with the Lock Reason for the Invoicing Document Reversal, the continue invoicing warning message pops up when you try to perform the invoicing process to the billing document relevant to the reversal invoicing document again. Choose Continue Invoicing to resume the invoicing process. Choose Cancel to stop the invoicing process. |  |

### SII Outgoing Invoice Registration (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check that a registration of an outgoing invoice can be sent to the tax agency and the response can be processed in the SAP S/4HANA Cloud Public Edition Environment using the connection to the interface to SAP BTP.

Prerequisite

Create customer invoices using the AE company code, document type and tax code(s) that have been configured for SII. Preliminary steps described in section Preliminary Steps Relevant to SII must have been carried out.

Run the following test cases of test script J58 for the created invoices:

SII Create eDocuments

SII Create eDocument Lists

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Billing Clerk. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open eDocument Cockpit (EDOC_COCKPIT) . | The app opens. |  |
| 3 | Data Entry | Choose Configure Your Solution.Note If the list is not submitted, choose the Submit button. | The list is submitted to and received by the tax authority. Upon submission, the status should be Accepted, Partially Accepted, or Rejected. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 2AR- Contract Accounting – Master Data and Basic Functions | Must be run before the test script. Business Partner and Contract Account must be created. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 2BE: Convergent Invoicing – Invoice Correction Processing | The invoicing document created as part of process 2BG: Convergent Invoicing – Invoice Creation for Usage and Service can be used for further processing in 2BE: Convergent Invoicing – Invoice Correction Processing |

### CSV Template Creation

#### Data Item Selection for Paid and Unpaid Service

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Item of Main Item | Global Field Name | Unpaid Service | Paid Service (Payment Card Data from CSV) | Paid Service(Payment Card Data from Standard Payment Card of business partner) | Paid Service (Payment Card Data from Payment Card of business partner) | Comments |
| BIT_AMOUNT | CABllbleItmAmount | X | X | X | X | Billable Item Amt |
| BIT_CURR | CABllbleItmCurrency | X | X | X | X | Currency |
| GPART | BusinessPartner | X | X | X | X | Business Partner |
| SRCTAID | CABllbleItmSourceTransId | X | X | X | X | Source Trans.ID |
| VKONT | ContractAccount | X | X | X | X | Contract Account |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Item of Payment Data Item | Global Field Name | Unpaid Service | Paid Service (Payment Card Data from CSV) | Paid Service(Payment Card Data from Standard Payment Card of business partner) | Paid Service (Payment Card Data from Payment Card of business partner) | Comments |
| CCINS | PaymentCardType |  | X |  |  | Payment Card Type |
| CCNUM | PaytCardByPaytServiceProvider |  | X |  |  | Card Number |
| DATAB | CardValidFrom |  | X |  |  | Card valid from |
| DATBI | CardValidTo |  | X |  |  | Card Valid To |
| SRCTAID | CABllbleItmSourceTransId |  | X | X | X | Source Trans.ID |
| PYMET | CAPaymentMethod |  |  | X |  | Payment Method |
| CCARD_ID | CCARD_ID |  |  |  | X | Payment Card ID |

#### Sample Data for Accrual / Deferral Postings

| Item of Main Items | Global Field Name | Accrual /Deferral Postings | Comments |
| --- | --- | --- | --- |
| BIT_AMOUNT | CABllbleItmAmount | Any Value | Billable Item Amt |
| GPART | BusinessPartner | The business partner | Business Partner |
| SRCTAID | CABllbleItmSourceTransId | Any Number | Source Trans.ID |
| SUBPROCESS | CABillgSubprocess | Y001 | Subprocess of Billing |
| BITTYPE | CABllbleItmType | The billable item type | Type of Billable Item |
| VKONT | ContractAccount | The contract account | Contract Account |
| BIT_CURR | CABllbleItmCurrency | The currency | Currency |
| BILLAC_TYPE | CAInvcgAccrualPostingType | Defined at Preliminary Step of Preliminary Steps Relevant to Accrual / Deferral Postings Individual Procedure (Optional) | Acc./Def.Post. Type |

### Data Archiving

#### Maintain Audit Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Manage Your Solution screen is displayed. |  |
| 4 | Open Maintain Audit Area | On the Configure Your Solution: Realize Phase screen, search Maintain Audit Area then choose Search.Select the line of the item and go to the next screen.On the Configuration Your Solution - Settings screen, choose Configure on the line of configuration step with name Maintain Audit Area. | The Change View Maintain Audit Area: screen displays. |  |
| 5 | Create Audit Area | On the Maintain Audit Area: Change screen, choose New Entries and make the following entries:Audit Area: <the audit area>, for example: Z001Description: <the description>Policy Category: <the policy category>, for example: RSTChoose Save. | The Audit Area of Z001 has been generated. |  |

#### Assign ILM Object to Audit Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Manage Your Solution screen is displayed. |  |
| 4 | Open Assign ILM Object To Audit Area | On the Configure Your Solution: Realize Phase screen, search Assign ILM Object To Audit Area then choose Search.Select the line of the item and go to the next screen.On the Configuration Your Solution - Settings screen, choose Configure on the line of configuration step with name Assign ILM Object To Audit Area. | The Assign ILM Objects to Audit Area: screen displays. |  |
| 5 | Choose Policy Category and Audit Area | Make the following entries:Policy Category: <the policy category>, for example: RSTAudit Area: <the audit area you created in the last step>, for example: Z001Choose Run. |  |  |
| 6 | Active ILM Object | Choose New Entries and make the entries as below:ILM Object: <the ILM Object>, for example: FKKBIXBIT4Status: ActiveChoose Save. | The ILM Object of FKKBIXBIT4 has been activated in the Audit Area.Note Here are the ILM Objects in SAP Convergent Invoicing, you may follow the steps to activate them based on your demands.ILM Object for Billing Document: FKKINVBILLILM Object for Invoicing Document: FKKINVDOCILM Object for Billable Item: FKKBIXBIT4ILM Object for Consumption Item: FKKBIXCIT4ILM Object for Billing Request: FKKBIXREQILM Object for Billing Plan: FKKBIXBIP |  |

#### Maintain ILM Policies and Rules

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad as Configuration Expert - Business Process Configuration. | The page containing the Fiori apps associated with your role is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note If country version needs to be added, choose Set Country Version. | The Manage Your Solution screen is displayed. |  |
| 4 | Open Maintain ILM Policies and Rules | On the Configure Your Solution: Realize Phase screen, search Maintain ILM Policies and Rules then choose Search.Select the line of the item and go to the next screen.On the Configuration Your Solution - Settings screen, choose Configure on the line of configuration step with name Maintain ILM Policies and Rules . | The Maintain ILM Policies and Rules screen displays. |  |
| 5 | Choose Policy Category and Audit Area and ILM Object | Make the following entries:Policy Category: <the Policy Category>, for example: RST Residence RulesAudit Area: <the Audit Area generated in the previous steps>, for example: Z001ILM Object: <the ILM Object>, for example: FKKBIXBIT4Choose Run. |  |  |
| 6 | Add Policy | In the Policies section, add policies by choosing New Entries in the upper left corner:Policy: Z_CI_001Status: Not LiveChoose Save. |  |  |
| 7 | Add Condition Fields | Choose Condition Field in the Dialog Structure on the left panel.Choose New Entries and make the following entries:Position: 0001Condition Field: BITCATPosition: 0002Condition Field: BITTYPEChoose Save. |  |  |
| 8 | Add Residence Rules | Choose Residence Rules in the Dialog Structure on the left panel.Choose New Entries and make the following entries:Residence Period: 1Time Unit: DAYTime Reference: STORE_DATETime Offset: END_OF_MONTHChoose Save. |  |  |
| 9 | Add Condition Field Values | Choose Condition Field Values in the Dialog Structure on the left panel.Choose New Entries and make the following entries:Condition Field: BITCATFrom: 0SAPCondition Field: BITTYPEFrom: Y001Choose Save. |  |  |

### Periodic Invoicing

You can perform periodic invoicing for contract accounts where only the periodic invoicing request and no other source document is to be invoiced. If you want to enable the periodic invoicing feature in invoicing, please view [Periodic Invoicing | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1a561330b0fe4990b9566655770746dd/f4d53622a4864690a42aef6a4d9b510d.html?version=LATEST) for details.

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
- related-to :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script]]
- related-to :: [[09-subscription-billing-and-contract-accounting/convergent-invoicing-recurring-and-one-off-items-2t3-ae-test-script-86]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 114,115 chars in the whole document
