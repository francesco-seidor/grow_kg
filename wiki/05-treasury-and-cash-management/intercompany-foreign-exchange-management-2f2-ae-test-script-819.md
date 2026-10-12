---
id: 05-treasury-and-cash-management/intercompany-foreign-exchange-management-2f2-ae-test-script-819
title: Intercompany Foreign Exchange Management (2F2_AE) Test Script (2F2_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2F2_AE: intercompany FX spot/forward, swap, NDF creation and mirror deal checks (AE)."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/intercompany-fx-deals]
aliases: [2F2_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Foreign Exchange Deals, intercompany foreign exchange, fx spot forward, fx swap, non-deliverable forward, mirror deal, intercompany business partner, cash position analysis, business roles, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-819
topic: 05-treasury-and-cash-management/intercompany-fx-deals
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intercompany Foreign Exchange Management (2F2_AE) Test Script (2F2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Foreign Exchange Deals** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Foreign Exchange Management (2F2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849302)

[2 Prerequisites 4](#_Toc232849303)

[2.1 System Access 4](#_Toc232849304)

[2.2 Roles 4](#_Toc232849305)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849306)

[2.4 Business Conditions 5](#_Toc232849307)

[2.5 Preliminary Steps 6](#_Toc232849308)

[2.5.1 Maintain Data for Intercompany Business Partner 6](#_Toc232849309)

[3 Overview Table 7](#_Toc232849310)

[4 Test Procedures 8](#_Toc232849311)

[4.1 Negotiate Process for Intercompany Foreign Exchange Contract 8](#_Toc232849312)

[4.1.1 Analyze Cash Position 8](#_Toc232849313)

[4.1.2 Determine Foreign Exchange Rates 8](#_Toc232849314)

[4.1.3 Agreement on Internal Foreign Exchange Contract by Receiving Company 9](#_Toc232849315)

[4.1.4 Agreement on Internal Foreign Exchange Contract by Issuing Company 9](#_Toc232849316)

[4.2 Create Foreign Exchange Contract - Intercompany Transaction 9](#_Toc232849317)

[4.2.1 Create Foreign Exchange Spot/Forward - Intercompany Transaction 9](#_Toc232849318)

[4.2.2 Create Foreign Exchange Swap - Intercompany Transaction 11](#_Toc232849319)

[4.2.3 Create Non-deliverable Forward - Intercompany Transaction 13](#_Toc232849320)

[4.3 Check Mirror Deal 14](#_Toc232849321)

[5 Appendix 16](#_Toc232849322)

[5.1 Succeeding Processes 16](#_Toc232849323)

## Purpose

Overview

This scope item allows a company to exchange foreign currency with affiliate companies. The contracts and deals are mirrored automatically. These intercompany transactions can be posted into the leading accounting principle.

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

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company, depending on the operational focus of your company.

You need to create company code for the affiliate company as the receiving company code via configuration step Create Your Organizational Structure in Configure Your Solution or configuration activity Set Up Organizational Structure in SAP Central Business Configuration depending on which configuration environment you are in. You can also use the company codes pre-delivered by SAP Best Practice.

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
| 1XN - Market Rates Management – Manually via Upload | Perform 1XN to prepare market data. |
| BFA - Basic Bank Account Management | Perform BFA to maintain house bank for an affiliate company. |
| J60 - Accounts Payable | Execute Prerequisites in J60 to define the Payment Medium Format (PMF) variants. Prerequisites > Preliminary Steps > Define Payment Medium Format Variants |

### Preliminary Steps

#### Maintain Data for Intercompany Business Partner

Purpose

To maintain intercompany business process such as mirror deals in the system, you need to create intercompany business partners first to make the functionality work.

To maintain business partner for TRM, refer to Setting Up Intercompany Foreign Exchange Management (2F2) for details. Make sure you go through the following steps for both Issuing Company and Receiving Company:

- Maintain General Data for Intercompany Business Partner
- Maintain Company Code Data for Intercompany Business Partner
- Maintain Relevant Settings for Intercompany Transaction

## Overview Table

The Intercompany Foreign Exchange Management (2F2) scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Negotiate Process for Intercompany Foreign Exchange Contract](#unique_9) [page ] 8 |  |  | This procedure occurs outside of the system. |
| [Analyze Cash Position](#unique_10) [page ] 8 | Cash Manager | If you are using the basic solution, refer to Basic Cash Operations (BFB). If full package has been purchased, refer to Advanced Cash Operations(J78). | This should appear under Transaction/ APP |
| [Determine Foreign Exchange Rates](#unique_11) [page ] 8 | Treasury Specialist - Front Office | - | This procedure occurs outside of the system. |
| [Agreement on Internal Foreign Exchange Contract by Receiving Company](#unique_12) [page ] 9 | Treasury Specialist - Front Office | - | This procedure occurs outside of the system. |
| [Agreement on Internal Foreign Exchange Contract by Issuing Company](#unique_13) [page ] 9 | Treasury Specialist - Front Office | - | This procedure occurs outside of the system. |
| [Create Foreign Exchange Contract - Intercompany Transaction](#unique_14) [page ] 9 |  |  | Prerequisites in the currency risk management script are met. |
| [Create Foreign Exchange Spot/Forward - Intercompany Transaction](#unique_15) [page ] 9 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Transaction is saved and a transaction number is generated. |
| [Create Foreign Exchange Swap - Intercompany Transaction](#unique_16) [page ] 11 | Treasury Specialist - Front Office | Create FX Swap (TX10) | Two transactions are saved and two transaction numbers are generated. |
| [Create Non-deliverable Forward - Intercompany Transaction](#unique_17) [page ] 13 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Transaction is saved and a transaction number is generated. |
| [Check Mirror Deal](#unique_18) [page ] 14 | Treasury Specialist - Front Office | Process Spots/Forwards - Collective Processing (TX06) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Negotiate Process for Intercompany Foreign Exchange Contract

Purpose

This following step are about the negotiation process for intercompany foreign exchange agreements.

Procedure

The negotiation process takes place outside of the system.

#### Analyze Cash Position

Purpose

The Cash Manager from central group verifies the cash position status and determines that a specific foreign currency is required for a subsidiary company based on analysis of foreign currency cash position. The Cash Manager enables the intercompany foreign currency exchange transactions.

Procedure

If full cash management is implemented in your system, use the Cash Flow Analyzer (F2332) app to analyze the cash position. For more information about procedures, see Advanced Cash Operations (J78).

#### Determine Foreign Exchange Rates

Purpose

In this activity, you determine the foreign exchange (FX) rates in Intercompany Foreign Currency Exchange Deals.

Procedure

The Treasury Specialist - Front Office from the central group determines the foreign exchange (FX) rates based on internal guidelines and external market environment. This activity takes places outside of the system.

#### Agreement on Internal Foreign Exchange Contract by Receiving Company

Purpose

In this activity, an agreement is reached on the internal foreign exchange (FX) contract by the receiving company.

Procedure

The Treasury Specialist - Front Office of the receiving company agrees on the internal FX contract details. This activity occurs outside of the system.

#### Agreement on Internal Foreign Exchange Contract by Issuing Company

Purpose

In this activity, an agreement is reached on the internal foreign exchange (FX) contract by the issuing company.

Procedure

The Treasury Specialist - Front Office of the issuing company agrees on the internal foreign exchange (FX) contract. This activity occurs outside of the system.

### Create Foreign Exchange Contract - Intercompany Transaction

Purpose

In the following procedures, you create the Foreign Exchange contracts as an Intercompany transaction.

Prerequisites

The prerequisites for intercompany transaction creation are in accordance to the foreign exchange (FX) transactions, which are described in the Foreign Currency Risk Management (1X1) test script. Complete the prerequisites of the Foreign Exchange Creation procedure using the affiliate company before proceeding.

#### Create Foreign Exchange Spot/Forward - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Spot or Forward transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

You can create a new transaction through the Copy Existing Transaction function. For detail steps, please refer to the Appendix section in the Foreign Currency Risk Management (1X1).

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the selection criteria:Company Code: For example, 3310 for AEProduct Type: 60ITransaction Type: For example, 101Partner: For example, 17401710and choose Enter.Note Use Transaction Type102 for forward transaction.Please make sure that you also maintained Payment Details for your counterparty. For details, see the Maintain Payment Details for Intercompany Business Partners section in the Create Business Partner for Treasury and Risk Management - MDS master data script. | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 4 | Enter Initial Data | Enter the following data:Rate: For example, EUR/USD 1.3Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: +2Trader: <leave blank>Note For Value Date, you can add more than +2 days for forward transaction.and select the Administr. tab. | The Administr. tab displays. |  |
| 5 | Enter Administr. Data | Enter the following data, and choose Save:Hdg Classific.: For example, Y0Risk Mitigation: For example, Check | The transaction saves and a transaction number generates.Note the transaction number for use in the mirror transaction query step. |  |

#### Create Foreign Exchange Swap - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a foreign exchange swap transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Swap (TX10). | The Create Forex Swap: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteriaCompany Code: For example, 3310 for AEPartner: For example, 17401710Note Please make sure that you also maintained Payment Details for your counterparty. For details, see the Maintain Payment Details for Intercompany Business Partners section in the Create Business Partner for Treasury and Risk Management - MDS master data script.First transactionProduct Type: 60ITransaction Type: For example, 101Second transactionProduct Type: 60ITransaction Type: For example, 102and choose Enter. | The Create Forex Swap: Structureview displays. |  |
| 4 | Enter data | Enter the following data:First TransactionCurrencies: For example, EUR/USDRate: For example, 1.3Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: For example, +22nd TransactionRate: For example, 1.2Value Date: For example, ++6Trader: <leave blank>and choose Save. | Two transactions save and two transaction numbers generate.Note both transaction numbers for use with the mirror transaction query step. |  |

#### Create Non-deliverable Forward - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Non-Deliverable-Forward transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

You can create a new transaction through the Copy Existing Transaction function. For detail steps, please refer to the Appendix section in the Foreign Currency Risk Management (1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteriaCompany Code: For example, 3310 for AEProduct Type: 60JTransaction Type: For example, 110Partner: For example, 17401710and choose Enter.Note Please make sure that you also maintained Payment Details for your counterparty. For details, see the Maintain Payment Details for Intercompany Business Partners section in the Create Business Partner for Treasury and Risk Management - MDS master data script. | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 4 | Enter data | Enter the following data:Rate: For example, AED/BRL 3.3220Buy/Sell: For example, B BuyTraded Amt: For example, BRL 50MValue Date: ++6+2Fixing Date: ++6Settlement Currency: For example, AEDTrader: <leave blank> | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 5 | Enter Data in Administration tab | Under the Administration tab, enter the following data, and chooseSave:Hdg Classific: For example, Y0Risk Mitigation: For example, Check | Transaction saves and a transaction number generates.Note the transaction number for use with the mirror transaction query. |  |

### Check Mirror Deal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An FX mirror deal is created automatically with the same status as the issuing deal. This activity describes how to review the mirror deal details.

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Spots/Forwards - Collective Processing (TX06). | The Forex: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria | Enter the following dataCompany Code: For example, 3310 for AETransaction: <Issuing Transaction Number(s) created in previous steps>Accept default values for other parameters.Choose Execute. | The transaction is displays in the next view. |  |
| 4 | Display Issuing Deal | On the Forex: Collective Processing view, select the checkbox for the transaction line and choose Display | Display Forex Transaction: view displays with the transaction data.Mirror transaction 1000XXXXXXX is available in company code XXXX message displays.Note down the mirror transaction number for use with the query. |  |
| 5 | Query Mirror Transaction | Return to Forex: Collective Processing view, enter the following data:Company Code: your country-specific custom company code, for example, 3310Transaction: <Enter Mirror Transaction Number(s) created in previous steps>Accept default values for the other parameters.Choose Execute. | Mirror Transaction lists on the Forex: Collective Processing view. For additional details, choose Display.Note Note down the transaction number of the mirror deal for later use. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, the following business processes must be completed for intercompany transaction:

| Scope Item | Business Condition |
| --- | --- |
| 1X1 - Foreign Currency Risk Management. | Complete the processes for both the issuing Forex (FX) deal and mirror deal respectively.Note The status of the issuing deal and the mirror deal are independent of each other.Process the following steps:Correspondence processes for transaction settlement.Fair value of transaction determination and key date valuation for period-end closing.Note For Net Present Value (NPV) calculation of intercompany deals, select Y001 Risk-free type as the evaluation type. Credit Value Adjustment/Debt Value Adjustment (CVA/DVA) type is not necessary.For Non-Deliverable Forward deal, perform fixing operation and reflecting correspondence.Generate and process Payment Request for Mature Transaction.Post flows to General Ledger.Post realized profit and loss. |

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
- related-to :: [[05-treasury-and-cash-management/intercompany-foreign-exchange-group-ledger-ifrs-2hu-ae-test-script-826]]
- related-to :: [[05-treasury-and-cash-management/test-script-intercompany-foreign-exchange-group-ledger-us-gaap-34m-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 25,611 chars in the whole document
