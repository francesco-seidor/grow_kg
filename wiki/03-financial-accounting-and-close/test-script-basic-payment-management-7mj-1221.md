---
id: 03-financial-accounting-and-close/test-script-basic-payment-management-7mj-1221
title: "Test Script: Basic Payment Management (7MJ) (7MJ_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 7MJ Basic Payment Management: functional approval classifier, payment rules, workflow, requested payments, approval."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/basic-payment-management]
aliases: [7MJ_S4CLD2608_BPD_EN_XX]
keywords: [Basic and Advanced Payment Management, basic payment management, functional approval, payment business rules, approval classifier, requested payments, payment workflows, business roles, test scripts, business conditions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MJ_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1221
topic: 03-financial-accounting-and-close/basic-payment-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Basic Payment Management (7MJ) (7MJ_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MJ_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Basic and Advanced Payment Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Basic Payment Management (7MJ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232828438)

[2 Prerequisites 3](#_Toc232828439)

[2.1 System Access 3](#_Toc232828440)

[2.2 Roles 3](#_Toc232828441)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232828442)

[2.4 Business Conditions 4](#_Toc232828443)

[2.5 Preliminary Steps 4](#_Toc232828444)

[2.5.1 Define Funtional Approval Classifier 4](#_Toc232828445)

[2.5.2 Manage Payment Business Rule 6](#_Toc232828446)

[3 Overview Table 10](#_Toc232828447)

[4 Test Procedures 11](#_Toc232828448)

[4.1 Manage Requested Payments 11](#_Toc232828449)

[4.2 Manage Payment Approval 12](#_Toc232828450)

[4.2.1 Manage Functional Approval (Optional) 12](#_Toc232828451)

## Purpose

Overview

Basic Payment Management is fully embedded in SAP S/4HANA Cloud Public Edition and supports end-to-end monitoring of self-initiated payments for both SAP and non-SAP systems. This comprises internal processing states as well as external bank responses from payment status notification reports and bank statements.

In detail, this scope item allows for central monitoring an approvals of payments from various different initiating sources.

Moreover, Basic Payment Management serves as single source of truth with a concise semantic payment data model (ISO20022).

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
| Payment Specialist | SAP_BR_PAYMENT_SPECIALIST | Payment Management | SAP_BR_PAYM_SPECIALIST | Suggested sample user PAYMENT_SPECIALIST representing the business role Payment Specialist. |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC | Suggested sample user BUSINESS_PROCESS_SPEC representing the business role Business Process Specialist. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Payer Company Code | 10101710 | DE Company CodeUS Company Code |  |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J60 - Accounts Payable | Invoice entry without purchase order is posted and paid via payment run. |
| J77 - Advanced Bank Account Management | The payment approvers are maintained. |
| J78 - Advanced Cash Operations | The Bank Communication Management settings are ready for payment approval. |

### Preliminary Steps

#### Define Funtional Approval Classifier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this section, you create functional approval classifers used in the functional approval process of payments. The classification is available in the flexible workflow as an attribute to derive the respective approval processes/workflow steps.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Manage Your Solution | Open Manage Your Solution (F1241). |  |  |
| 3 | Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Search | Make the following entries:Application Area: FinanceSub Application Area: Payments and Bank Communications | Selected application area items are displayed in the Configuration Items view. |  |
| 5 | Select Configuration Item | Choose the arrow button at the end of the row for Basic Payment Management. | The Configuration Steps for the selected row display. |  |
| 6 | Configure | On the Define Functional Approval Classifiers row, choose Configure. | The "Define Functional Approval Classifiers: Change” screen displays. |  |
| 7 | New Entries | Choose New Entries. |  |  |
| 8 | Define New Functional Approval Classifier | Enter the following data and choose Save.Funct. Approval Clf.: ZSALADescription: for example, Payroll Payments | The new functional approval classifier is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Select Customizing Activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Functional Approval Classifiers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Functional Approval Classifiers: Change” screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Define New Functional Approval Classifier | Enter the following data and choose Save.Funct. Approval Clf.: ZSALADescription: for example, Payroll Payments | The new functional approval classifier is created. |  |

#### Manage Payment Business Rule

Purpose

In this section, you set up payment business rules for your payment approvals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Payment Business Rules (F9155). | The Manage Payment Business Rules screen displays. |  |
| 3 | Create Payment Business Rule | On the entry screen of the app, choose Create and choose Functional Approval Classifier ftrom the dropdown list.Note If there is an existing rule set of component Functional Approval Classifier, you cannot create one more. In that case, choose Navigatge (Enter) to navigate to the list of rules.Choose Create. In the screen of New Object, make the following entries:Description: Payroll PaymentsFunctional Approval Classifier: for example, ZSALAIn the section of Conditions, choose Create. Make the following entries and choose Apply:Entry OneCharacteristic: PF2_CURROption: Equal toValue Low: for example, EUR for country DE, USD for country USEntry TwoCharacteristic: PF2_AMOption: Equal toValue Low: -713.10Note For testing purpose, it is recommended that the paying amount is as specific and rare as possible. Later, the amount maintained in the invoice should equal to this value to meet the condition.Note For credit transfer, use minus sign for the amount.Choose Create. In the pop-up window, choose Create.Note Choose Keep Draft to save the draft, or choose Discard Draft to discard the change. | A payment business rule is created with Release Status In Process. |  |
| 4 | Release Payment Business Rule | Choose Submit. | The payment business rule is Released. |  |
| 5 | Log On | Log onto the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 6 | Access App | Open Manage Teams and Responsibilities (F6742). |  |  |
| 7 | Create New Team | Choose Create.Note You can also copy teams from the existing team list. |  |  |
| 8 | Maintain General Information | On the Team screen, there are four facets:Team InformationResponsibility DefinitionsTeam OwnersTeam MembersIn the Team Information section, enter the following values:Name: FUNC_APPR_SALAGlobal ID: FUNC_APPR_SALADescription: Functional Approval (SALA Payments)Team Status: EnabledType: SPF_PY_SITCategory: FSCM_PFThe Type and Category values can be selected from the value help.Note On selecting the type, category is generated automatically.Now, you have entered new team information. |  |  |
| 9 | Maintain Team Owner | The business process specialist can change or add team owners.Note If the business process specialist (who is creating the team) has a business user, this business process specialist is then defaulted as team owner. |  |  |
| 10 | Maintain Team Member | In the Team Members section, choose Create.Enter the following values:Business Partner: <user ID>, for example, PaymentSpecialistFunctions: S_PFMON_FTo display the connection between the business partner, Payment Specialist, and user ID, see the search help. Generic users are described in the Last Name field.Then choose Create on the lower right. |  |  |
| 11 | Log On | Log onto the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 12 | Access App | Open Manage Workflows for Payment Processing (F9207). | The Manage Workflows screen displays with only workflow scenario Functional Payment Approval by default. |  |
| 13 | Create Workflow | Choose Create, enter the following values:Workflow Name:Valid From: for example, <today>Valid To: 12/31/9999In the Start Conditions section, choose Functional Approval Classifier Is from the dropdown list, enter ZSALA as the value. |  |  |
| 14 | Create Step | In the Steps section, choose Create, enter the following values:Step Type: Release of Payment Approval GroupAssignment By: TeamTeam: FUNC_APPR_SALAStep to be completed by: One recipientChoose Create on the lower right. |  |  |
| 15 | Save Workflow | Choose Save and choose Activate if workflow status is Inactive. |  |  |

## Overview Table

This scope item consists of several procedures provided in the tables below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Requested Payments](#unique_10) [page ] 11 | Payment Specialist | Manage Requested Payments (F8522) |  |
| [Manage Functional Approval (Optional)](#unique_11) [page ] 12 | Payment Specialist | Manage Requested Payments (F8522) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Requested Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is monitoring end-to-end payment status for payables/receivables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Requested Payments (F8522). | The Manage Requested Payments screen displays. |  |
| 3 | Check Payments | On the entry screen of the Manage Requested Payments (F8522) app, make the following entries and choose Go:Payer Company Code: 1010 (DE Company Code) 1710 (US Company Code)Note You can check specific payment by End to End ID. In case of accounts payables, note down the Payment Document No. after payment run as End to End ID. | A list of payments for the selected payer company code is displayed with the correct amounts and payer/payee party information. |  |

### Manage Payment Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for end-to-end payment approval for your payment requests.

Prerequisite

J77 Advanced Bank Account Management and J78 Advanced Cash Operations are in scope.

Procedure

After payment run is conducted, if the functional approval conditions are met, the payment item will go through functional approval process.

#### Manage Functional Approval (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for functional approval by business experts to ensure that the content of the payment (amount, currency, payee, bank account number etc.) is correct.

Prerequisite

Feature toggle PF2_PAYM_FOUND_FUNC_APPROVAL_2 is active via activity Activate Features.

An invoice entry without purchase order and with the specific gross invoice amount is posted, and paid via payment run. For more details, refer to Invoice Entry without Purchase Order and Payment Run in the test script of J60 Accounts Payable.

Make sure the invoice gross invoice amount equals to 713.10. Note down the payment run payment document number, for example, 2000031458.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Payment Specialist. |  |  |
| 2 | Access App | Open Manage Requested Payments (F8522). | The Manage Requested Payments screen displays. |  |
| 3 | Check Payments | On the entry screen of the Manage Requested Payments (F8522) app, make the following entries and choose Go:Payer Company Code: 1010 (DE Company Code) 1710 (US Company Code)Origin Document Type: 02End to End ID: <payment document number> from payment run result as the prerequisite, 2000031458Created At: <This Week>Note Use Picker to filter the time.Note You can check specific payment by End to End ID. In case of accounts payables, note down the Payment Document No. after payment run as End to End ID. | A list of payments for the selected payer company code is displayed with the correct amounts and payer/payee party information.For the payments which meet functional approval payment business rule conditions, the payment status is In Approval. |  |
| 4 | Navigate to Payment | Choose > , navigate to the detail page of payment with status In Approval. |  |  |
| 5 | Check Functional Approval Workflow | In the Processing Status History section, expand Payment Processing process step.Choose >, navigate to the detail page of Functional Approval process step. | In the detail page of the functional approval process step, the workflow step is displayed with the correct amounts, payment status, functional approval classifier, a generated approval group ID, and all the processors (recipients) assigned as the payment approvers.Example PaymentSpecialist is listed in the processors column. |  |
| 6 | Access App | Open My Inbox (F0862). | The My Inbox for Payment Approvals screen displays. |  |
| 7 | Approve Payment | Locate the workflow item by amount -713.10.Compare the functional approval classifier and orgin document ID with the classifier defined in preliminary step and the End to End ID.Choose Approve, in the pop-up window, choose >Submit. | The functional approval is done, the payment status is changed to Sent to Bank. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MJ_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 20,746 chars in the whole document
