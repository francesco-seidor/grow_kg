---
id: 10-procurement/test-script-automated-invoice-settlement-2lh-ae-831
title: "Test Script: Automated Invoice Settlement (2LH_AE) (2LH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2LH Automated Invoice Settlement (ERS), UAE (AE) baseline: prerequisites, PO-to-ERS test steps."
cluster: 10-procurement
tags: [kb/procurement, topic/evaluated-receipt-settlement]
aliases: [2LH_S4CLD2608_BPD_EN_AE]
keywords: [Automated Invoice Settlement (ERS), evaluated receipt settlement, automated invoice settlement, purchase order creation, purchase order approval, flexible workflow, goods receipt, purchasing info record, ers email output, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LH_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-831
topic: 10-procurement/evaluated-receipt-settlement
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automated Invoice Settlement (2LH_AE) (2LH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Automated Invoice Settlement (ERS)** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automated Invoice Settlement (2LH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849454)

[2 Prerequisites 4](#_Toc232849455)

[2.1 System Access 4](#_Toc232849456)

[2.2 Roles 4](#_Toc232849457)

[2.3 Master Data and Organizational Data 5](#_Toc232849458)

[2.4 Business Conditions 6](#_Toc232849459)

[2.5 Preliminary Steps 7](#_Toc232849460)

[2.5.1 Open New MM Period 7](#_Toc232849461)

[2.5.2 Check Flexible Workflow for Purchase Order Approval 7](#_Toc232849462)

[2.5.3 Configure Flexible Workflow for Purchase Order 9](#_Toc232849463)

[2.5.4 Create Purchasing Info Record (Optional) 10](#_Toc232849464)

[2.5.5 Verify E-mail Output for ERS (Optional) 12](#_Toc232849465)

[2.5.6 Check Or Modify Language And/Or Email Address Of The Invoicing Party (Optional) 16](#_Toc232849466)

[3 Overview Table 17](#_Toc232849467)

[4 Test Procedures 18](#_Toc232849468)

[4.1 Automated Invoice Settlement 18](#_Toc232849469)

[4.1.1 Create Purchase Order 18](#_Toc232849470)

[4.1.2 Change Purchase Order (Optional) 20](#_Toc232849471)

[4.1.3 Approve Purchase Order (Optional) 22](#_Toc232849472)

[4.1.4 Post Goods Receipt 23](#_Toc232849473)

[4.1.5 Execute Evaluated Receipt Settlement 24](#_Toc232849474)

[4.1.6 Check Supplier Invoice List (Optional) 25](#_Toc232849475)

[5 Appendix 27](#_Toc232849476)

[5.1 Specify Automatic Settlement of Planned Delivery Costs (Optional) 27](#_Toc232849477)

[5.2 Monitor Purchasing Info Record Price History 28](#_Toc232849478)

[5.3 ERS Process with Scheduling Agreements 29](#_Toc232849479)

[5.4 ERS Process with Inbound Deliveries 29](#_Toc232849480)

## Purpose

Overview

By using this process, the customer agrees with the supplier that the supplier does not submit an invoice for a purchase order or transaction. The goods receipt is settled directly, by automatically posting the invoice document on the basis of the purchase order and goods receipt. Hence a lean and robust procurement process is ensured. This process is suitable for creating settlement documents at regular intervals.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC | Test User: PURCHASER |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC | Test User: PURCHASING_MANAGER |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK | Test User: WAREHOUSE_CLERK |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC | Test User: AP_ACCOUNTANT |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Test User: BPC_EXPERT |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC | Test User: BUPA_MASTER_SPECIALIST |

### Master Data and Organizational Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, suppliers, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Additional Master Data (Default Values)

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Shop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001/002/003 | Group 001/Group 002/Group 003 | Depending on material |
| Supplier | 33300003 | Domestic UAE Supplier 3 | Supplier with ERS |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc. |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS– MDSNote ERS field is only available in the Maintain Business Partner app which contains all fields related to business partner. If you want to check and update the ERS field or create ERS suppliers individually, you need to use Maintain Business Partner app. Manage Business Partner master data, Manage Supplier master data are Fiori apps and are the lighter versions of Maintain BP app. |
| BHD | Create Purchasing Info Record - MDS – MDS |
| BNF | Create Product Master of type "Trading Good" - MDS – MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNE - Create Supplier Master - MDS | You have completed the steps described in the chapter Creating Supplier Master Data - Purchasing Organization Data.Note On the Purchasing Data tab page in the Control Data section, please make sure:GR-Based Inv. Verif. (Goods-Receipt-Based Invoice Verification): <selected>.On the Purchasing Data tab page in the Additional Purchasing Data section, please make sure:AutoEvalGRSetmt Del.(Evaluated Receipt Settlement): <selected>. |
| BHD - Create Purchasing Info Record - MDS | You have completed the step described in the chapter Create Purchasing Info Record.Note On the Delivery and Quantity tab, please make sure:Goods-Receipt-Based Invoice Verification : <selected>.No Evaluated Receipt Settlement : <deselected>. |
| 2SW - Create Tax Condition - MDS | You have completed the step described in the Create Tax Condition - MDS master data script. Tax condition is set. |
| 5XU - Document and Reporting Compliance | It's an optional step. Perform Activate Document and Reporting Compliance Features in 5XU when you need to enable advanced eDocument features such as eDocument Submit, Cancel and Reject. |

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period:

Closing MM Period and Opening New Posting Period

#### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order

Purpose

In this procedure, you configure your release conditions for purchase order approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872). | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Name: <Test Workflow for Purchase Order>Select Start Conditions, and in the Start Conditions area, make the following entries:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition and make the following entries:Total Net Amount of purchase order is greater than: SelectedAmount: For example, 10.Currency: AEDIn Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the Recipients area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Step to be completed by: One of the recipientsChoose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the Workflow Item just created and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure the default workflow Automatic Release of Purchase Order has been activated. |

#### Create Purchasing Info Record (Optional)

Purpose

Before you perform the test procedures, you need to create one info record for the ERS supplier and the related material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: for example, 33300003Material: for example, TG0011Plant: 3310Purchasing Group: for example, 001Material Group:Auto-complete | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: for example, EXWIncoterm Location 1: <Incoterm Location 1>Note Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an Incoterm automatically populates its associated version, which can be subsequently modified or removed if needed. | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: for example, 1Under Delivery Tolerance in %: for example, 10Over Delivery Tolerance in %: for example, 10,0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 10Only Select the following entry:Goods-Receipt-Based Invoice Verification: Selected | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To:12/31/9999Amount: for example,10Pricing Unit: for example, 1Currency: for example, AEDChoose Create. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |

Result

The info record has been created.

#### Verify E-mail Output for ERS (Optional)

Purpose

If you want to send email automatically during invoice posting, you need to verify email output settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Output Parameter Determination. | The Output Parameter Determination screen is displayed. |  |
| 3 | Select Business Rules | Make the following entries under Select Business Rules.Show rules for: Supplier InvoiceDetermination Step: Output Type | Business rules is selected. |  |
| 4 | Maintain Output Type | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Dispatch Time, and make the following entry:Dispatch Time: 1 (Immediately)Choose OK.Choose Activate. | Output type is added. |  |
| 5 | Select Business Rules | Make the following entries under Select Business Rules :Show rules for: Supplier InvoiceDetermination Step: Receiver | Business rules is selected. |  |
| 6 | Maintain Receiver | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Role, and make the following entry:Role: RSChoose OK.Select Direct Value Input from the dropdown list in column Exclusive Indicator, and make the following entry:Exclusive Indicator: - (false)Choose OK.Choose Activate. | Receiver is added. |  |
| 7 | Select Business Rules | Make the following entries under Select Business Rules :Show rules for: Supplier InvoiceDetermination Step: Channel | Business rules is selected. |  |
| 8 | Maintain Channel | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Role, and make the following entry:Role: RSChoose OK.Select Direct Value Input from the dropdown list in column Channel, and make the following entry:Channel: EmailChoose OK.Choose Activate. | Channel is added. |  |
| 9 | Select Business Rules | Make the following entries under Select Business Rules :Show rules for: Supplier InvoiceDetermination Step: Output Relevance | Business rules is selected. |  |
| 10 | Maintain Output Relevance | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Relevance Indicator, and make the following entry:Relevance Indicator: X (Ture)Choose OK.Choose Activate. | Output relevance is added. |  |
| 11 | Select Business Rules | Make the following entries under Select Business Rules:Show rules for: Supplier InvoiceDetermination Step: Email Recipient | Business rules is selected. |  |
| 12 | Maintain Email Recipient | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Email Type Code, and make the following entry:Email Type Code: TOChoose OK.Select Direct Value Input from the dropdown list in column Email Address, and make the following entry:Email Address: <your email address to receive email>Choose OK.Choose Activate.Note: You can maintain one or more email recipients directly in the determination step Email Recipient , here you can the more information. | Email recipient is added. |  |
| 13 | Select Business Rules | Make the following entries under Select Business Rules :Show rules for: Supplier InvoiceDetermination Step: Email Settings | Business rules is selected. |  |
| 14 | Maintain Email Settings | Choose Edit, then choose Insert New Row. In the new row, select Direct Value Input from the dropdown list in column Output Type, and make the following entry:Output type: EVALUATED_RECEIPT_SETTLEMENTChoose OK.Select Direct Value Input from the dropdown list in column Sender Email, and make the following entry:Sender Email: <Your sender email address>Choose OK.Select Direct Value Input from the dropdown list in column Email Template, and make the following entry:Email Template: MM_IV_DEFAULT_TEMPLATE_ERSChoose OK.Choose Activate.Note If you don’t maintain sender's email address, the system picks the sender email address that is connected to the company code of the supplier invoice.Instead of using the default ERS template MM_IV_DEFAULT_TEMPLATE_ERS provided by SAP, you can (and should) create your own template based on the predelivered one. Using the app ‘Maintain Email Templates’, search for the default template ‘MM_IV_DEFAULT_TEMPLATE_ERS’, select it and press the Copy button. You can customize your copied template (subject and HTML body) by changing the static text and/or the placeholder. An overview of all available placeholder should be visible in the application by clicking on the CDS view.After this, you need to adapt customizing via app Manage your Solution, navigating to ‘Configure Your Solution’. Search the activity ‘Assign Email Templates’ (ID 101945) and create a new entry for the application object type ‘SUPPLIER_INVOICE’, output type ‘EVALUATED_RECEIPT_SETTLEMENT’ and your custom template ID (see the [documentation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/9a181e0e52a54c4091261f92922b99d4.html?locale=en-US) for more details). After saving the customizing, your template can be selected in the output parameter determination, as described in step 3 and step 4. | Email settings is added. |  |

Result

The email output type for ERS has been created.

#### Check Or Modify Language And/Or Email Address Of The Invoicing Party (Optional)

Purpose

The purpose of this activity is to check or modify the language and/or the email address of the invoicing party.

Prerequisite

The invoicing party has been created.

Procedure

| Step | Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. |  |
| 2. | Access the App | Open Maintain Business Partner(BP) | The Maintain Business Partner (Original)screen displays. |
| 3 | Extend supplier purchasing data to cross-country purchasing organization | Choose Open BP.In the field Business Partner, make the following entry and choose Enter:Supplier number: 33300003Choose Switch between Display and Change.Make the following entries:Change in BP role: FLVN01 Supplier (defined)Under Communication section, check the following entries:Language: German, you will receive an email in German.E-Mail: <your email address to receive email>Choose Save. | Supplier purchasing data of business partner 10300003 is created. |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | APP | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_14) [page ] 18 | Purchaser | Manage Purchase Orders (F0842A) | Purchase Order is created. |
| [Change Purchase Order (Optional)](#unique_15) [page ] 20 | Purchaser |  | Purchase Order is changed. |
| [Approve Purchase Order (Optional)](#unique_16) [page ] 22 | Purchasing Manager | My Inbox - All Items (F0862) | Purchase Order is approved. |
| [Post Goods Receipt](#unique_17) [page ] 23 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) | Goods receipt is posted against the purchase order. |
| [Execute Evaluated Receipt Settlement](#unique_18) [page ] 24 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs - Advanced (F1683) | The ERS is executed. |
| [Check Supplier Invoice List (Optional)](#unique_19) [page ] 25 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Credit Memo is displayed and sent. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Automated Invoice Settlement

#### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to formalize a specific requirement for a material from the supplier by creating a purchase order. If the PO’s net order value is more than 500 AED, you must ensure the steps related to workflow have been done in the Preliminary Steps, before creating and approving purchase order. And J45 Procurement of Direct Materials Test Script is regarded as the single source of truth for standard purchasing including purchase order creation, approval and so on. Please refer to J45 Procurement of Direct Materials for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders screen is displayed. |  |
| 3 | Start Purchase Order creation | Without making any selection, choose Create to create a purchase order. | The Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order data | Enter all of the necessary data.On General Information Tab:Basic Data:Supplier: 33300003Currency: AEDOrganization:Purchasing Group:001Purchasing Organization:3310Company Code: 3310In Items section, choose Create.Material: TG0011Plant: 3310Order Quantity: For example, 2Net Order Price: Determined automatically. If the system can not determine the net price automatically, enter the Net Price manually, for example, 10Note If you want your purchase order to be assigned to an approval, choose a quantity and net price higher than 500AED(for Purchase Groups = 003)Navigate to the selected item by clicking on the Chevron (>) or by directly clicking on the item line.On Purchase Order Item screen, choose Process Flow tabThe next data will be displayed after the article is enteredGoods Receipt: yesGoods-Receipt-Based Invoice Verification: xInvoice Receipt: xEvaluated Receipt Settlement: YesMake sure Goods-Receipt-Based Invoice Verification has been selectedIn item section, choose Delivery Details tabStorage Location: 331AIn item section, choose Tax tab.Tax Code: <Input Tax Code>In item section, choose Schedule Lines tab.Delivery date: a date in the future.If you have enabled the automatic settlement of planned delivery costs in section [Specify Automatic Settlement of Planned Delivery Costs (Optional)](#unique_21) [page ] 27, please follow below steps to add a condition type for freight.In Item section, choose tab Pricing.Choose Create .In the Add Price Element section, enter the following condition types for freight and choose Enter:FGW1 (Freight / Gr. Weight 1): freight is calculated based on gross weight.Amount: 4.00 EUR Per KG.Choose Add, then the freight cost condition will be inserted into the Pricing Element panel.Then choose Apply in bottom right to save the draft. | The Purchase Order screen is displayed. |  |
| 5 | Check Purchase Order for completeness and Save Purchase Order | Choose Order in bottom right to save the Purchase Order. | A new Purchase Order is created，if no error is displayed in the dialog box. |  |
| 6 | Correct Issues and Save Purchase Order(Optional) | If the system gives you the message, then choose Message.Check and correct the entries for errors.Choose Order to save the purchase order. | You have corrected any issues.A new Purchase Order is created. |  |

#### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Choose Search | Choose Search on the upper right part of the Fiori launchpad, | The scroll down list and Search box are unhidden. |  |
| 3 | Select from Scroll Down List | Select the specific category: for example, Purchase Orders | The search results will be restricted. |  |
| 4 | Search Purchaser Orders via Search Function | Enter target values in the Search Box on the upper right part of the Fiori launchpad,Search Box: for example, 45*Choose Search to start searching. | One Filters Panel is displayed on the left part and all the related purchase orders are displayed on the right main part |  |
| 5 | Check the Filters Smart Objects | Choose one filter on the left side to check the smart objects, for example, Supplier.Choose Display as right beside Supplier, for example, change from List to Bar Chart | The bar chart is displayed.You can choose any filter on the left side and switch among different Display as approaches. |  |
| 6 | Find the Newly Created Purchase Order | Choose the filter of Created On and select the following:Created On: Today | The Purchase Orders created today are displayed. |  |
| 7 | Select Purchase Order | Select the Purchase Order title you want to change. | The Purchase Order screen is shown. |  |
| 8 | Open the Purchase Order in Manage Purchase Orders App | Choose Manage Purchase Orders from the upper right part of the related Apps listAnd choose Edit in the upper right corner.Choose Display/Change if the screen is transferred to WebGUI. | The Purchase order is opened in change mode. |  |
| 9 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 10 | Check Purchase Order for completeness | Choose Order.Choose Save in WebGUI | The Purchase Order is complete. |  |
| 11 | Messages (Optional) | Choose Messages(if possible). | If a message is displayed, you must correct the Purchase Order. If no message is displayed, the Purchase Order is complete. |  |
| 12 | Save Purchase Order Messages (Optional) | Choose Order to save the Purchase Order. | The Purchase Order has been saved. The system displays a message Purchase order xxx has been saved. |  |

#### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO greater than 500 AED and purchase group is 003, then the PO should do the approval. PO release amount is configured in AED in configure Flexible workflow for Purchase Order.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of existing Purchase Orders is displayed. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Order is displayed. |  |
| 4 | Approve Purchase Order | Select the Purchase Order on the left side of the screen and choose Release at the bottom right. | The Submit Decision screen is displayed. |  |
| 5 | Enter Approval Reason | Enter the approval reason if necessary, and then choose Submit. | The Purchase Order is approved. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Post Goods Receipt for Purchasing Document (F0843). | The Goods Receipt screen is displayed. |  |
| 3 | Select Purchasing Document | Enter the purchase order number. | The system displays the data for the goods receipt on the Goods Receipt screen. |  |
| 4 | Enter Delivery Note | Make the following entries and Choose EnterDelivery Note: xxxNote For ERS, Delivery note is recommended to enter. |  |  |
| 5 | Select Item | Select the items for which a goods receipt is to be posted, namely confirm the delivered quantitySelect an item with a quantity of two or more pieces. | The Post button is activated. |  |
| 6 | Post | Choose Post . | The system displays Material document xxx posted. |  |

#### Execute Evaluated Receipt Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You should only use ERS if agreements with the supplier are clear, and you update the price agreements in the purchase orders in the system. You also need to create goods movements promptly and accurately. Created goods movements can be settled without receipt of an invoice. The system can create and post the appropriate invoices itself. ERS is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute ERS | Make the following entries:For Step 1, in the Template Selection section, from the drop-down box of Job Template, choose Evaluated Receipt Settlement (ERS).Then choose Step 2, in the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Then choose Step 3, in the Parameters section, make the following entries:Company Code: for example, 3310Plant: for example, 3310Goods Receipt Document: Enter the material document number created from the last step.Document Year of Goods Receipt: For example, Current YearSupplier: 33300003Settle Pl Del Cost in addition: Checked if you added condition type for freight in [Create Purchase Order](#unique_14) [page ] 18.Test Run: CheckedNote If you got the message Settlement of planned deliv. costs not possible if GR data was entered., please remove the value of goods receipt document and document year of goods receipt, enter the purchasing document number.Note In Document Selection, you can specify the granularity of a supplier invoice. For example, you can make a single supplier invoice from goods receipts of a supplier if you select per Supplier.Choose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the job without Test Run | Uncheck Test Run, and then choose Schedule. |  |  |
| 6 | Check the result | In the Application Jobs screen, find the job you created. You may need to wait several minutes to see the results after the job status becomes finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding Document number and FI Document number created. |  |

#### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can review the document created in the last step, and get the generated Credit Memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the document | On the Supplier Invoices List screen, enter the following values, then choose Go:Invoicing Party : 33300003Company Code: 3310 | Invoices list is displayed. |  |
| 4 | Go to the invoice detailed page | Choose the invoice you created, whose Entry Type is ERS | The screen will be navigated to the Supplier Invoice detailed page. |  |
| 5 | Display the document | On the Supplier Invoice screen, go to the Output tab. In the Output Details table, find the line with Output Type of EVALUATED_RECEIPT_SETTLEMENT. Choose Display Document in the Display column. | The document (in this case, Credit Memo) is displayed. |  |
| 6 | Download the document | Download the document. | The document is downloaded to your local workspace. |  |
| 7 | Send Documents to Supplier (Optional) | Send the downloaded document to the supplier as printed document, or by fax or by e-mail or via the Internet.The step is executed offline. | The document is sent to your supplier. |  |
| 8 | Send Documents to Supplier Automatically (Optional) | If you complete the configuration in chapter [Verify E-mail Output for ERS (Optional)](#unique_11) [page ] 12 and chapter [Check Or Modify Language And/Or Email Address Of The Invoicing Party (Optional)](#unique_12) [page ] 16, you can see an email output with the status Completed in Output tab. You don’t need to send the document to suppliers manually.The document has been successfully sent to the email address you set in chapter [Verify E-mail Output for ERS (Optional)](#unique_11) [page ] 12 or chapter [Check Or Modify Language And/Or Email Address Of The Invoicing Party (Optional)](#unique_12) [page ] 16. | The document is sent to your supplier automatically. |  |

## Appendix

### Specify Automatic Settlement of Planned Delivery Costs (Optional)

Purpose

This setting is to specify Automatic Settlement of Planned Delivery Costs during ERS invoice posting.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 4 | Search SSCUI Group | In Application Area, choose Sourcing and Procurement and in Sub Application Area, choose Invoice Processing. | The SSCUI group Incoming Invoice is displayed. |  |
| 5 | Open SSCUI | Select item Incoming Invoice, and choose Configure to open the configuration step Specify Automatic Settlement of Planned Delivery Costs. | The Specify Automatic Settlement of Planned Delivery Costs screen is displayed. |  |
| 6 | Specify Automatic Settlement of Planned Delivery Costs | Choose New Entries.Make the following entries:Cocd: For example, 3310POrg: For example, 3310Supplier: For example, 33300003ERS: For example, CheckedChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Activities | Go to the Business Processes Configuration app and search for the following activity: Specify Automatic Settlement of Planned Delivery Costs.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Specify Automatic Settlement of Planned Delivery Costs screen is displayed. |  |
| 3 | Specify Automatic Settlement of Planned Delivery Costs | Choose New Entries.Make the following entries:Cocd: For example, 3310POrg: For example, 3310Supplier: For example, 33300003ERS: For example, CheckedChoose Save. |  |  |

### Monitor Purchasing Info Record Price History

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
| 1 | Log on | Open the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Purchasing Info Record Price History (F2988). | The Monitor Purchasing Info Record Price History screen is displayed |  |
| 3 | Display Item List | Choose Go to display all items. |  |  |
| 4 | Check Price Analysis | Choose Price Analysis of one item to see the chart that shows price change over a period of time. | The Price Analysis screen is displayed. |  |
| 5 | View Purchasing Info Records | Choose one info record number item to display purchasing info record management options. |  |  |

### ERS Process with Scheduling Agreements

In your test system, in which the scope item BMR Scheduling Agreements in Procurement and this scope item 2LH Automated Invoice Settlement are activated, you can test and run the scope item BMR Scheduling Agreements in Procurement process steps with the supplier 33300003 of ERS.

### ERS Process with Inbound Deliveries

In your test system, in which the scope item 2TX Direct Procurement with Inbound Delivery and this scope item 2LH Automated Invoice Settlement are activated, you can test and run the scope item 2TX Direct Procurement with Inbound Delivery process steps with the supplier 33300003 of ERS.

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
- see-also :: [[03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 50,154 chars in the whole document
