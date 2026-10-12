---
id: 05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-02
title: Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 2 of 2
description: "Part 2 of 2: Step-by-step test script for scope item 2UN_AE (Money Market Mutual Fund Management, release 2608, AE localisation): prerequisites, test procedures, job scheduling appendix."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/money-market-mutual-funds]
aliases: []
keywords: [Money Market Mutual Fund Management, simulated valuation, rebate reinvestment, securities account transfer, securities transactions, money market mutual fund, general valuation class, period-end closing, posting logs, 2UN]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx#lines-3336-3424"]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-873
topic: 05-treasury-and-cash-management/money-market-mutual-funds
language: EN
part: 2/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 2 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx`, part 2 of 2 (lines 3336–3424 of the extracted text), extracted with `mammoth`. Grouped under **Money Market Mutual Fund Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example,02ASec. Class ID Number: for example, <Security class ID number(s) for which Simulated Valuation has been executed>, for example, MMF_AE1Security Account: for example, <Securities account(s) for which valuation has been executed>, for example, DE_MMFSimulation Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:simulated results deleted for key date (the date on which the reversal takes place). |  |

### Rebate Reinvestment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you get rebate as reinvestment, an entry into the system is required to update the securities position. Rebate reinvestment is only supported with product type 02A Money Market Fund.

If the granted rebate reinvestment is reversed, another entry with transaction type 400 is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE1Transaction Type: 300Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:In the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: choose an appropriate General Valuation Class (GVC), for example, 30 Cash equivalentsNote If it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to the latest floating NAV (security price), so it is evaluated at fair value through P/L or OCI from the accounting perspective.Position Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amounts area,Number of Units: for example, 1000Price (Unit Quoted): for example, 1 | All data is entered. |  |
| 5 | Save the Transaction | Choose Save. |  |  |
| 6 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

### Security Account Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you transfer the money market fund position to the new security account.

Prerequisite

You have purchased a money market fund transaction.

A new security account has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Securities Account Transfer (FWDU). | The Securities Account Transfer: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria for Securities Account Transfer | On the Securities Account Transfer: Initial screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, for example, MMF_AE1Source Sec. Account: for example, for example, AE_MMFPos. Value Date: for example, <the current date> | The Securities Account Transfer: Edit screen is displayed. |  |
| 4 | Enter Detailed Data for Securities Account Transfer | On the Securities Account Transfer: Edit screen, enter the following data and choose Save:Target Sec.Acct: for example, AE_MMF1Nominal Amount: for example, 100000Pos. Value Date: for example, <the current date>Calc. Date: for example, <the current date>Document Date: for example, <the current date> | The screen Information Overview is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the posting information by choosing Logs + Messages. |  |
| 5 | Review Logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the postings. | Logs are reviewed. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-01]]
- related-to :: [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-ifrs-2uo-ae-874]]
- related-to :: [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-us-gaap-34g-ae-911]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx` — lines 3336–3424 of the extracted text · extracted with `mammoth` · 257,646 chars in the whole document
