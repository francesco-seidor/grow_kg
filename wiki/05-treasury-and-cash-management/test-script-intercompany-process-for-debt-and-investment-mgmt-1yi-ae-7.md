---
id: 05-treasury-and-cash-management/test-script-intercompany-process-for-debt-and-investment-mgmt-1yi-ae-7
title: "Test Script: Intercompany Process for Debt and Investment Mgmt (1YI_AE) (1YI_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1YI (AE): intercompany loans with automatic mirror deals, covering roles, prerequisites and Fiori test steps."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/intercompany-debt-and-investment]
aliases: [1YI_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Debt and Investment (Mirror Loans), intercompany debt and investment, mirror transactions, interest rate instruments, current account-style instruments, test scripts, intercompany business partners, treasury business roles, business conditions, intercompany contract negotiation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YI_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-788
topic: 05-treasury-and-cash-management/intercompany-debt-and-investment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Process for Debt and Investment Mgmt (1YI_AE) (1YI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Debt and Investment (Mirror Loans)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Process for Debt and Investment Mgmt (1YI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848371)

[2 Prerequisites 4](#_Toc232848372)

[2.1 System Access 4](#_Toc232848373)

[2.2 Roles 4](#_Toc232848374)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848375)

[2.4 Business Conditions 5](#_Toc232848376)

[2.5 Preliminary Steps 6](#_Toc232848377)

[2.5.1 Maintain Data for Intercompany Business Partner 6](#_Toc232848378)

[3 Overview Table 7](#_Toc232848379)

[4 Test Procedures 8](#_Toc232848380)

[4.1 Negotiation Process for Intercompany Debt and Investment Contract 8](#_Toc232848381)

[4.1.1 Analyze Cash Position 8](#_Toc232848382)

[4.1.2 Determine Interest Rates 8](#_Toc232848383)

[4.1.3 Agree on Internal Contract by Receiving Company 9](#_Toc232848384)

[4.1.4 Agree on Internal Contract by Issuing Company 9](#_Toc232848385)

[4.2 Create Debt and Investment Contract - Intercompany Transaction 9](#_Toc232848386)

[4.2.1 Create Interest Rate Instrument - Intercompany Transaction 9](#_Toc232848387)

[4.2.2 Create Current Acct-Style Instrument - Intercompany Transaction 11](#_Toc232848388)

[4.3 Check Mirror Deal 13](#_Toc232848389)

[5 Appendix 15](#_Toc232848390)

[5.1 Succeeding Processes 15](#_Toc232848391)

## Purpose

Overview

This scope item allows a company to handle loans with an affiliate company.

If the loans contract is created in the issuing company, a mirror transaction is automatically generated in the receiving company.

The mirroring change feature is available for interest rate instrument (product category 550). This means if a mirror-relevant change (such as roll over, give notice / terminate and reverse) is made to one transaction, its mirror transaction is updated automatically.​

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
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| COMPANY CODE | 33101710 | 3310 represents issuing company code;1710 represents receiving company code generated by activation. |  |
| CURRENCY | AED |  |  |
| PARTNER | 3340331017401710 | Business Partner 33403310 represents issuing company code 3310;Business Partner 17401710 represents receiving company code 1710. | For issuing transaction and mirror transaction creation, maintain the Business Partners representing issuing and receiving company codes. |
| VALUATION AREA | AE0 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Perform 1XN to prepare market data. Manually enter the relevant market data or import market data from spreadsheet. |
| BFA - Basic Bank Account Management | Perform BFA to maintain house bank for affiliate company. |
| J60 - Accounts Payable | Execute Prerequisites in J60 to define the Payment Medium Format (PMF) variants. Prerequisites > Preliminary Steps > Define Payment Medium Format Variants |

### Preliminary Steps

#### Maintain Data for Intercompany Business Partner

Purpose

To maintain intercompany business process such as mirror deals in the system, you need to create intercompany business partners first to make the functionality work.

To maintain business partner for TRM, refer to Setting UpIntercompany Process for Debt and Investment Mgmt (1YI) for details. Make sure you go through the following steps for both Issuing Company and Receiving Company:

- Maintain General Data for Intercompany Business Partner
- Maintain Company Code Data for Intercompany Business Partner
- Maintain Relevant Settings for Intercompany Transaction

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Analyze Cash Position](#unique_9) [page ] 8 | Cash Manager | / Cash Flow Analyzer (F2332) | Follow the two cash operations test scripts |
| [Determine Interest Rates](#unique_10) [page ] 8 | Treasury Specialist - Front Office | - | - |
| [Agree on Internal Contract by Receiving Company](#unique_11) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Agree on Internal Contract by Issuing Company](#unique_12) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Create Interest Rate Instrument - Intercompany Transaction](#unique_13) [page ] 9 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) | Transaction is saved and a transaction numbers are generated. |
| [Create Current Acct-Style Instrument - Intercompany Transaction](#unique_14) [page ] 11 | Treasury Specialist - Front Office | Create CA Style Instrument (FTRCAI01) | Transaction is saved and a transaction number is generated. |
| [Check Mirror Deal](#unique_15) [page ] 13 | Treasury Specialist - Front Office | Process MM Transactions - Collective Processing (TM00) | Mirror Transaction Displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Negotiation Process for Intercompany Debt and Investment Contract

Context

In this activity, the negotiation process for intercompany contact agreement takes place. The negotiation process occurs and completes outside of the system.

#### Analyze Cash Position

Purpose

The Cash Manager from the central group reviews the cash position status. If a need of liquidity for a subsidiary company based on analysis of cash position is identified, then it initiates the intercompany debt and investment deal.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) SAP Fiori app to analyze the cash position. For more information, please refer to the Basic Cash Operations(BFB) test script.

#### Determine Interest Rates

Purpose

In this activity, you determine the interest rates in intercompany debt or investment deals.

Procedure

For this procedure, a Treasury Specialist - Front Office, from the central group, determines interest based on internal guidelines and external market environment. This activity occurs outside of the system.

#### Agree on Internal Contract by Receiving Company

Purpose

In this activity, agreement is reached on internal intercompany debt or an investment contract by the receiving company.

Procedure

A Treasury Specialist - Front Office of the receiving company agrees on internal intercompany debt or an investment contract detail. This activity occurs outside of the system.

#### Agree on Internal Contract by Issuing Company

Purpose

In this activity, an agreement is reached on internal intercompany debt or an investment contract by the issuing company.

Procedure

In this procedure, the Treasury Specialist - Front Office of the issuing company agrees to the internal intercompany debt or an investment contract. This activity occurs outside of the system.

### Create Debt and Investment Contract - Intercompany Transaction

Context

In this activity, you create the debt or investment contracts as an intercompany transaction.

Prerequisites

The prerequisites of intercompany deals creation that are in accordance to debt or investment deals with external business partner are described in Debt and Investment Management (1WV). For this procedure, you follow those prerequisites of the debt or investment creation using the affiliate company information.

#### Create Interest Rate Instrument - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an interest rate instrument transaction with an affiliate company. The mirror transaction generates automatically in the affiliate company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument view displays. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument view, enter the following data:Company Code: for example, 3310Product Type: 55ITransaction Type: for example, 200Partner: for example, 17401710and choose Enter. | The Create Interest Rate Instrument: Structure view displays. |  |
| 4 | Maintain Structure of New Deal | Enter the following data:Amount: For example, 10MNominal Amount: For example, 10MStart: For example, <Current Date>End: For example, <Current Date + 3 years>Interest Cat.: For example, VariableRef,Int.Rate: For example, AEDM03EIB+/- 11st Int. Rate: For example, 3.0000000Int. Calc. Method: For example, Act/360Frequency: For example, MonthlyContract Date: For example, <Current Date/Current Time>. | If message Currency entered does not correspond to the reference interest rate displays, that means the currency reference interest rate is not the currency of the transaction, for intercompany transaction, the message can be skipped. |  |
| 5 | Maintain Administration | Choose the Administr. view and enter following data:Portfilio: For example, Y000Gen. Valn Class: For example, Short term debt (current liability). |  |  |
| 6 | Maintain Payment Details | Choose the Payment Details tab and find the incoming line with the direction of flow "+" and outgoing row with the direction of flow "-". Double-click the outgoing row and confirm the assignments or enter the following data:Payment Request, With: <select this checkbox>House Bank: For example, AEBK1Account ID: For example, AEAC1Payer/Payee: For example,Partner Bank: For example, AED1Payment methods: For example, T. |  |  |
| 7 | Save | Choose Check to verify the input data. If no error notification appears, choose Save. | Transaction saves and a transaction number generates. Note the transaction number for the mirror transaction query. |  |

#### Create Current Acct-Style Instrument - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a current acct-style instrument. The mirror transaction generates automatically for an affiliate company.

|  |
| --- |
| Note After a contact settles, the issuing company can increase or decrease the nominal amount of the current acct-style instrument transaction according to business requirement. For internal cash flow balance, the receiving company consequently updates the mirror transaction. The update to the mirror transaction is a manual process. For more information, see the Nominal Amount Adjustment procedure in the Debt and Investment Management (1WV) test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Create CA Style Instrument (FTRCAI01). | The Create Current Acct-Style Instrument view displays. |  |
| 3 | Enter Selection Criteria | Enter the following selection criteria:Company Code: For example, 3310Product Type: 58ITransaction Type: For example, 300Partner: For example, 17401710and choose Enter. | The Create Current Acct-Style Instrument: Structure view displays. |  |
| 4 | Enter data | Enter the following data:Flow Type: For example, 1101 or 1111Amount: For example, 10MStart: For example, <Current Date - 7 days>End: For example, <Current Date + 3 years>Interest Category: For example, FixedPercentage Rate: For example, 3.0000000Int. Calc. Method: For example, Act/360Frequency: For example, MonthlyContract Date: For example, <Current Date - 7 days>and choose Save. | The Administr. tab displays. |  |
| 5 | Maintain Administration of New Deal | Choose Administr. view and enter the following data:Gen. Valn Class: For example, Short term investment (current asset): Amortized cost |  |  |
| 6 | Maintain Payment Details of New Deal | Choose the Payment Details tab. In the Payment Details tab, you see the incoming line with Direction of flow "+" and outgoing row with Direction of flow "-". Double-click the outgoing row. Confirm the assignments or enter following data:Payment Request, With: <select this checkbox>House Bank: For example, AEBK1Account ID: For example, AEAC1Payer/Payee: For example,Partner Bank: For example, AED1Payment methods: For example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error notification displays, choose Save. | The transaction saves and a transaction number generates. Note the transaction number for use with the mirror transaction query. |  |

### Check Mirror Deal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A debt and investment mirror deal is created automatically with the same status as the issuing deal. In this activity, you review the mirror deal details.

|  |
| --- |
| Note Through the configuration activity ICT - Specify Mirroring Mode for Processing of Financial Transactions, you can specify the mirroring mode for already created intercompany transactions. It means that when an intercompany transaction is changed, the related mirror transaction is also updated automatically. Refer to the Maintain Relevant Settings for Intercompany Transaction step in the set up guide Setting Up Intercompany Process for Debt and Investment Mgmt (1YI) for details. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria | On the Money Market: Collective Processing view, enter the following data:Company Code: For example, 3310Transaction: <Issuing Transaction Numbers created in previous step>Accept default values for other parameters.and choose Execute. | The transaction displays in the next view. |  |
| 4 | Change the Transaction | On the Money Market: Collective Processing view, select the checkbox for the transaction line and choose Display. | Display CAI Transaction: Structure view displays with the transaction data.The Mirror transaction 1000XXXXXXX is available in company code XXXX notification displays.Note the Mirror transaction number for use with the following step. |  |
| 5 | Query Mirror Transaction | Return to the Money Market: Collective Processing view and enter the following data:Company Code: your country-specific custom company code, for example, 3310Transaction: <the Mirror Transaction Numbers created in previous step>Accept default values for other parameters and choose Execute. | A Mirror Transaction appears on the Money Market: Collective Processing view, choose Display for details.Note Note down the transaction number of the mirror deal for later use |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 1WV - Debt and Investment Management | After debt and investment transaction creation, the following procedures from Debt and Investment Management (IWV) must be completed for both the issuing and mirror transactions respectively.Note The status of issuing transaction and the mirror deal are independent of each other.Correspondence processes for transaction settlementGenerate and process payment request for Principal Payment, then post flows to general ledger. For incoming cash flow, direct post to general ledger.For current acct-style instrument, perform nominal amount adjustment on issuing and mirror transaction, then generate and process for nominal amount payment.Generate and process Interest Payment, then post flows to general ledger. For incoming cash flow, direct post to general ledger.Generate and process Payment Request for Mature Transaction.Post flows to General Ledger.Post realized profit and loss |

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
- related-to :: [[05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-ifrs-2o]]
- related-to :: [[05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-us-gaap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 23,666 chars in the whole document
