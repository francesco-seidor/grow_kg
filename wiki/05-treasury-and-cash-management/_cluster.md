---
title: Treasury and Cash Management
description: "Treasury instruments (debt, FX, derivatives, bonds, securities, guarantees, letters of credit) with IFRS/US GAAP valuation, market rates, bank fees and statements, cash pooling, liquidity."
cluster: 05-treasury-and-cash-management
type: cluster
tags: [kb/treasury-and-cash-management, kb/hub]
keywords: [treasury, TRM, valuation area, FX, derivatives, bonds, securities, letter of credit, market rates, bank statement, bank fees, cash pooling, liquidity planning]
node_count: 82
created: 2026-10-12
updated: 2026-10-12
---

# Treasury and Cash Management

Covers TRM financial transactions, their accounting and bank/cash operations. Excludes customer and supplier payments, SEPA and cash application (see 03), FI-CA cash application (see 09) and HQ treasury replication (see 16 for Central Finance).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Asset-Backed Securities Management

How asset-backed security investment flows and period-end valuation post in IFRS and US GAAP valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-asset-backed-securities-management-6b5-ae-sap-s-4hana-clou\|Test Script: Asset-Backed Securities Management (6B5_AE) - SAP S/4HANA Cloud Public Edition (6B5_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 6B5 (AE localization): ABS/MBS purchase, payment, valuation, repayment, sale, reports, plus appendix jobs, output and risk setup. |
| [[05-treasury-and-cash-management/test-script-asset-backed-securities-management-group-ledger-ifrs-6b6-a\|Test Script: Asset-Backed Securities Management – Group Ledger IFRS (6B6_AE) (6B6_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script 6B6_AE: posting ABS flows and period-end valuation in parallel valuation area 002 for the IFRS group ledger. |
| [[05-treasury-and-cash-management/asset-backed-securities-management-group-ledger-us-gaap-6b7-ae-1160\|Asset-Backed Securities Management – Group Ledger US GAAP (6B7_AE) (6B7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script 6B7: posting ABS investment flows and key date valuation in parallel valuation area 003 for the US GAAP ledger. |

### SWIFT Bank Directory Sample Data

Which SWIFT bank directory records (BIC, IBAN, institution, address, connectivity) the sample file provides for bank master data upload.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/swift-sample-data-206\|SWIFT Sample Data (SWIFT_Sample_Data)]] | Tab-separated sample SWIFT bank directory records (BIC, IBAN, institution name, address, connectivity) with modification flags. |

### Bank Fee Management

How bank billing files are imported and bank fee and interest conditions maintained, monitored and validated.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-bank-fee-management-2o0-ae-sap-s-4hana-cloud-public-editio\|Test Script: Bank Fee Management (2O0_AE), SAP S/4HANA Cloud Public Edition (2O0_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2O0 (AE): importing bank billing files, managing bank fee and interest conditions, monitoring and validating bank fees; dated 19-06-26. |

### Bank Guarantee Management

How bank guarantee flows are posted to IFRS and US GAAP parallel valuation areas with Process Business Transactions (TPM10).

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-bank-guarantee-management-2nz-ae-839\|Test Script: Bank Guarantee Management (2NZ_AE) (2NZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2NZ (UAE, company code 3310): issuing/receiving bank guarantees, rollover, termination, fees, collateral, reports. |
| [[05-treasury-and-cash-management/bank-guarantee-management-group-ledger-ifrs-2o2-ae-test-script-841\|Bank Guarantee Management - Group Ledger IFRS (2O2_AE) - Test Script (2O2_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2O2_AE: posting bank guarantee flows to the IFRS ledger in parallel valuation area 002 via TPM10, Treasury Accountant role. |
| [[05-treasury-and-cash-management/bank-guarantee-management-group-ledger-us-gaap-34f-ae-test-script-910\|Bank Guarantee Management - Group Ledger US GAAP (34F_AE) - Test Script (34F_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 34F_AE: posting bank guarantee flows to the US GAAP ledger in parallel valuation area 003 via TPM10, Treasury Accountant role. |

### Advanced Bank Statement Automation

How the cash specialist role is authorized and jobs scheduled to create and process bank statements automatically.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-advanced-bank-statement-automation-4x8-1056\|Test Script: Advanced Bank Statement Automation (4X8) (4X8_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4X8: authorizing the cash specialist role and scheduling jobs that create bank statement reprocessing rule templates. |

### Bond Management

How bonds are issued and invested, payments and correspondence handled, and IFRS valuation and class transfers posted.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01\|Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | SAP test script for Bond Management (3WY_AE, UAE/AED, company code 3310): bond issuance and investment, payments, correspondence, postings, period-end, in Fiori apps. |
| [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02\|Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP Best Practices 2608 (AE) TRM test script, second part: bond payment, period-end, repayment, reports, and appendix job scheduling, output management, market risk and credit risk steps. |
| [[05-treasury-and-cash-management/bond-management-group-ledger-ifrs-3wz-ae-test-script-982\|Bond Management – Group Ledger IFRS (3WZ_AE) Test Script (3WZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3WZ: parallel valuation area 002 (IFRS) postings, key date valuation and class transfer for bond issuance/investment. |
| [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983\|Test Script: Bond Management – Group Ledger US GAAP (3X0_AE) (3X0_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script (3X0_AE): bond posting, accruals, key date valuation and class transfer in parallel valuation area 003 for US GAAP. |

### Cash Pooling and Cash Concentration

How cash pools are defined and intercompany cash concentration runs in Advanced Cash Operations.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-intercompany-process-for-cash-concentration-2u8-ae-869\|Test Script: Intercompany Process for Cash Concentration (2U8_AE) (2U8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (AE) for cash pools and cash concentration under Advanced Cash Operations: prerequisites, config steps, test procedures. |

### Debt and Investment Management

How loans, deposits and money-market transactions are valued, accrued and reclassified in IFRS and US GAAP valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-01\|Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for SAP S/4HANA Cloud Public Edition 2608 (AE) scope item 1WV Debt and Investment Management: prerequisites, test steps, reports, jobs. |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-02\|Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Test script 1WV (S/4HANA Cloud 2608, AE), part 2: TRM payment posting, reports, background jobs, output management, reversals, valuation, notifications. |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77\|Test Script: Debt and Investment Management – Group Ledger IFRS (1X7_AE) (1X7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1X7: parallel valuation area 002 (IFRS) postings, accruals, valuation, reclassification and realized P&L. |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-us-gaap-34c-ae\|Test Script - Debt and Investment Management – Group Ledger US GAAP (34C_AE) (34C_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 34C_AE: parallel valuation area 003 for US GAAP in treasury debt and investment management. |

### Foreign Currency Risk Management (FX Deals)

How FX spot, forward and swap flows are posted, key-date valued and realized P&L computed in IFRS and US GAAP valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-01\|Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | SAP Best Practices test script for scope item 1X1 (UAE): FX risk management with exposure, hedging, FX forwards/swaps/NDFs/options, settlement, payment and posting. |
| [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-02\|Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Test script 1X1 Foreign Currency Risk Management, S/4HANA Cloud 2608 (AE), part 2: option maturity, payments, valuation, reporting, jobs, netting, termination. |
| [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-ifrs-1x9-ae-777\|Foreign Currency Risk Management – Group Ledger IFRS (1X9_AE) (1X9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for parallel valuation (IFRS 9, valuation area 002) of foreign currency risk: flow posting, key date valuation, realized P&L. |
| [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-us-gaap-34d-ae-908\|Foreign Currency Risk Management – Group Ledger US GAAP (34D_AE) (34D_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for parallel valuation (US GAAP, valuation area 003) of foreign currency risk: flow posting, key date valuation, realized P&L. |

### Intercompany Foreign Exchange Deals

How intercompany FX spot, forward, swap and NDF deals are created and mirror deals checked between group companies.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/intercompany-foreign-exchange-management-2f2-ae-test-script-819\|Intercompany Foreign Exchange Management (2F2_AE) Test Script (2F2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2F2_AE: intercompany FX spot/forward, swap, NDF creation and mirror deal checks (AE). |
| [[05-treasury-and-cash-management/intercompany-foreign-exchange-group-ledger-ifrs-2hu-ae-test-script-826\|Intercompany Foreign Exchange – Group Ledger IFRS (2HU_AE) – Test Script (2HU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2HU_AE: intercompany FX deals, mirror deals and IFRS parallel valuation postings (AE sample data). |
| [[05-treasury-and-cash-management/test-script-intercompany-foreign-exchange-group-ledger-us-gaap-34m-ae\|Test Script: Intercompany Foreign Exchange – Group Ledger US GAAP (34M_AE) (34M_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 34M: intercompany FX deals, mirror deals and US GAAP parallel valuation postings (area 003). |

### Interest Rate Derivatives Management

How interest rate swaps and other derivatives post flows, accruals, key-date valuation and realized P&L in IFRS and US GAAP areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-01\|Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for scope item 1X3_AE (S/4HANA Cloud Public Edition 2608, AE): interest rate swaps, cross-currency swaps, swaptions; prerequisites and step tables. |
| [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-02\|Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Treasury test script (S/4HANA Cloud 2608, AE), part 2: swaption lifecycle, reports, and appendices on jobs, output, accounting, market/credit risk, simulation. |
| [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-ifrs-1xb-ae-test-scr\|Interest Rate Derivatives Management – Group Ledger IFRS (1XB_AE) Test Script (1XB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1XB_AE: parallel IFRS valuation area 002 for interest rate derivatives (flows, accrual, valuation, realized P&L). |
| [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-us-gaap-34e-ae-test\|Interest Rate Derivatives Management – Group Ledger US GAAP (34E_AE) Test Script (34E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 34E_AE: posting flows, accrual, key date valuation and realized P&L in valuation area 003 for US GAAP. |

### Letter of Credit Management

How letter of credit flows are posted and key-date valued in IFRS and US GAAP valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-01\|Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | SAP test script for scope item 49D (UAE): issuing, receiving, rolling over, presenting, paying and terminating normal and standby letters of credit. |
| [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-02\|Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP S/4HANA Cloud 2608 (AE) test script, Letter of Credit Management (49D): payments, standby L/C receive/rollover/terminate, treasury reports, alerts. |
| [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-ifrs-49e-ae-1003\|Letter of Credit Management – Group Ledger IFRS (49E_AE) (49E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script 49E_AE for letter of credit management with IFRS parallel valuation: posting flows and key date valuation in valuation area 002. |
| [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004\|Letter of Credit Management – Group Ledger US GAAP (49F_AE) (49F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 49F_AE: parallel valuation area postings and key date valuation for letter of credit management under US GAAP group ledger. |

### Liquidity Planning

How financial plan data jobs import cash flow plans from SAP Analytics Cloud for liquidity planning.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-liquidity-planning-3l5-ae-953\|Test Script: Liquidity Planning (3L5_AE) (3L5_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script 3L5_AE: configure and schedule financial plan data jobs importing cash flows from SAP Analytics Cloud for liquidity planning. |

### Market Rates Management (Automatic Import and Manual Upload)

How FX and interest market rates are imported automatically from Refinitiv or a bring-your-own-rates provider (1S4), or entered and uploaded manually (1XN).

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/automatic-market-rates-management-1s4-ae-test-script-762\|Automatic Market Rates Management (1S4_AE) - Test Script (1S4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (1S4_AE, UAE) for automatic market rates import via Refinitiv or BYOR: translation tables, retrieval, jobs, notifications. |
| [[05-treasury-and-cash-management/test-script-market-rates-management-manually-via-upload-1xn-ae-782\|Test Script: Market Rates Management – Manually via Upload (1XN_AE) (1XN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (1XN_AE) for manually entering or uploading Treasury market data and checking the Market Data Overview. |

### Money Market Mutual Fund Management

How money market mutual fund positions are posted, accrued and key-date valued in IFRS and US GAAP areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-01\|Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Part 1 of 2: Step-by-step test script for scope item 2UN_AE (Money Market Mutual Fund Management, release 2608, AE localisation): prerequisites, test procedures, job scheduling appendix. |
| [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-02\|Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Part 2 of 2: Step-by-step test script for scope item 2UN_AE (Money Market Mutual Fund Management, release 2608, AE localisation): prerequisites, test procedures, job scheduling appendix. |
| [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-ifrs-2uo-ae-874\|Money Market Mutual Fund Management – Group Ledger IFRS (2UO_AE) (2UO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 2UO_AE: parallel valuation (IFRS 9, area 002) posting, accrual and key date valuation for money market funds. |
| [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-us-gaap-34g-ae-911\|Money Market Mutual Fund Management – Group Ledger US GAAP (34G_AE) (34G_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 34G (AE): parallel valuation area 003 for US GAAP in money market mutual fund management: posting, accrual, key date valuation. |

### Securities Option Management

How securities option flows, key-date valuation and realized P&L post in IFRS and US GAAP valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-securities-option-management-6nd-ae-sap-s-4hana-cloud-publ\|Test Script: Securities Option Management (6ND_AE) - SAP S/4HANA Cloud Public Edition (6ND_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 6ND (AE localization): securities option lifecycle in Treasury, from setup to payment, valuation, exercise/expiry, accounting and reports. |
| [[05-treasury-and-cash-management/test-script-securities-option-management-group-ledger-ifrs-6ne-ae-1182\|Test Script - Securities Option Management - Group Ledger IFRS (6NE_AE) (6NE_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (6NE_AE) for posting flows, key date valuation and realized P&L in parallel IFRS valuation area 002. |
| [[05-treasury-and-cash-management/securities-option-management-group-ledger-us-gaap-6nf-ae-test-script-1\|Securities Option Management – Group Ledger US GAAP (6NF_AE) Test Script (6NF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 6NF (AE) for posting flows, key date valuation and realized P&L in parallel valuation area 003 for US GAAP. |

### Shareholding Management

How shareholdings are purchased, dividends and equity pickup posted, and IFRS/US GAAP valuation performed.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed\|Test Script: Shareholding Management (5WF_AE) - SAP S/4HANA Cloud Public Edition (5WF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 5WF Shareholding Management: BP setup, security classes, purchase, dividends, valuation, sale, reports. |
| [[05-treasury-and-cash-management/shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127\|Shareholding Management - Group Ledger IFRS (5WG_AE) Test Script (5WG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5WG_AE: IFRS 9 parallel valuation postings for shareholdings, dividends, key date valuation, equity pickup (AE). |
| [[05-treasury-and-cash-management/test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128\|Test Script: Shareholding Management – Group Ledger US GAAP (5WH_AE) (5WH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5WH: parallel US GAAP valuation area postings for shareholdings (dividends, equity pickup, reclassification). |

### Stock (Equity Securities) Management

How securities accounts and classes are set up, stock purchases, sales and dividends posted, and IFRS/US GAAP valuation run.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-stock-management-5od-ae-1\|Test Script SAP S/4HANA Cloud Public Edition - Stock Management (5OD_AE) (5OD_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (UAE, 2608) for scope item 5OD Stock Management in Treasury: securities account/class, stock purchase/sale, payments, dividends, corporate actions, valuation. |
| [[05-treasury-and-cash-management/stock-management-group-ledger-ifrs-5oe-ae-test-script-1112\|Stock Management – Group Ledger IFRS (5OE_AE) Test Script (5OE_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5OE_AE: parallel valuation area 002 for IFRS in stock (securities) management, dated 19-06-26. |
| [[05-treasury-and-cash-management/stock-management-group-ledger-us-gaap-5of-ae-test-script-1113\|Stock Management – Group Ledger US GAAP (5OF_AE) Test Script (5OF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5OF_AE: posting stock flows and key date valuation in valuation area 003 for US GAAP, plus subscription rights appendix. |

### Treasury Workstation Accounting Integration

How treasury accounting postings replicate from S/4HANA Cloud to a central ECC or Private Edition accounting system.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-treasury-workstation-accounting-integration-33e-ae-897\|Test Script: Treasury Workstation Accounting Integration (33E_AE) (33E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for 33E: replicating Treasury (TRM) accounting postings to a central accounting system (ECC or Private Edition) and verifying them. |
| [[05-treasury-and-cash-management/test-script-treasury-workstation-cash-integration-34p-ae-sap-s-4hana-c\|Test Script: Treasury Workstation Cash Integration (34P_AE) - SAP S/4HANA Cloud Public Edition (34P_S4CLD2608_BPD_EN_AE)]] | SAP test script (34P_AE) for replicating house banks, bank accounts and cash flows from subsidiary systems to a central treasury workstation. |
| [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-treasury-workstation-paym\|Test Script SAP S/4HANA Cloud Public Edition - Treasury Workstation Payment Integration (3NA) (3NA_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script for scope item 3NA: Treasury payment requests sent by IDoc to a receiving FI system, with reversal, roles and test steps. |

### Business Partners for Treasury and Risk Management

How to create treasury business partners with roles (counterparty, issuer, bank), payment, standing instructions and correspondence data.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/geschaftspartner-fur-treasury-and-risk-management-anlegen-mds-22g-256\|Geschäftspartner für Treasury and Risk Management anlegen - MDS (22G) (22G_S4CLD2608_Master_Data_DE_XX)]] | German master data script (22G) for SAP S/4HANA Cloud Public Edition 2608: manual test steps to create business partners for Treasury and Risk Management. |
| [[05-treasury-and-cash-management/create-business-partner-for-treasury-and-risk-management-mds-22g-257\|Create Business Partner for Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (22G): manual test steps to create treasury business partners, roles, payment, correspondence data. |
| [[05-treasury-and-cash-management/script-de-datos-maestros-crear-socio-comercial-para-treasury-and-risk\|Script de datos maestros: Crear socio comercial para Treasury and Risk Management - MDS (22G) (22G_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data test script (22G) for SAP S/4HANA Cloud Public Edition 2608: creating and maintaining business partners for Treasury and Risk Management. |
| [[05-treasury-and-cash-management/mds-22g-259\|マスタデータスクリプト 財務/リスク管理向けビジネスパートナ登録 - MDS (22G) (22G_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (22G) for creating and maintaining Treasury and Risk Management business partners in SAP S/4HANA Cloud Public Edition 2608, with test steps. |
| [[05-treasury-and-cash-management/script-de-dados-mestre-criar-parceiro-de-negocios-para-o-treasury-and\|Script de dados mestre - Criar parceiro de negócios para o Treasury and Risk Management – MDS (22G) (22G_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT) with manual test steps to create and maintain business partners for Treasury and Risk Management (22G). |
| [[05-treasury-and-cash-management/mds-22g-261\|创建资金和风险管理的业务伙伴 - MDS (22G) (22G_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 22G: manual test steps to create and maintain business partners for Treasury and Risk Management in S/4HANA Cloud Public Edition 2608. |

### Treasury Parallel Valuation Areas for IFRS and US GAAP

How treasury valuation areas (002 IFRS, 003 US GAAP) post flows, accruals and key-date valuation to parallel group ledgers.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77\|Test Script: Debt and Investment Management – Group Ledger IFRS (1X7_AE) (1X7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1X7: parallel valuation area 002 (IFRS) postings, accruals, valuation, reclassification and realized P&L. |
| [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-us-gaap-34c-ae\|Test Script - Debt and Investment Management – Group Ledger US GAAP (34C_AE) (34C_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 34C_AE: parallel valuation area 003 for US GAAP in treasury debt and investment management. |
| [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-ifrs-49e-ae-1003\|Letter of Credit Management – Group Ledger IFRS (49E_AE) (49E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script 49E_AE for letter of credit management with IFRS parallel valuation: posting flows and key date valuation in valuation area 002. |
| [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004\|Letter of Credit Management – Group Ledger US GAAP (49F_AE) (49F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 49F_AE: parallel valuation area postings and key date valuation for letter of credit management under US GAAP group ledger. |

### Bank Integration via Multi-Bank Connectivity and File Interface

How payment files are sent and bank statements (MT940, CAMT.053, MT942, CAMT.052, pain.002) received via SAP Multi-Bank Connectivity or manual file upload.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/bank-integration-with-sap-multi-bank-connectivity-16r-ae-703\|Bank Integration with SAP Multi-Bank Connectivity (16R_AE) (16R_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 test script (16R_AE): simulating MBC outgoing payments, CAMT.053/MT940 bank statements, fee files, situations and message monitoring. |
| [[05-treasury-and-cash-management/test-script-bank-integration-with-file-interface-1eg-ae-sap-s-4hana-cl\|Test Script: Bank Integration with File Interface (1EG_AE) - SAP S/4HANA Cloud Public Edition (1EG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for 1EG_AE: download payment files, upload MT942/camt.052/MT940/camt.053/pain.002 bank files, with AE sample data. |

### Bank Account Management

How bank accounts are created, changed, approved and closed in basic or advanced bank account management, with bank chains, payment approvers and powers of attorney.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-basic-bank-account-management-bfa-ae-sap-s-4hana-cloud-pub\|Test Script: Basic Bank Account Management (BFA_AE) - SAP S/4HANA Cloud Public Edition (BFA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for Basic Bank Account Management: prerequisites, config, bank account lifecycle, bank chains. |
| [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-01\|Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | SAP test script for J77_AE Advanced Bank Account Management: prerequisites, configuration and test steps for bank accounts, approvals and powers of attorney. |
| [[05-treasury-and-cash-management/test-script-advanced-bank-account-management-j77-ae-sap-s-4hana-cloud-part-02\|Test Script: Advanced Bank Account Management (J77_AE), SAP S/4HANA Cloud Public Edition (J77_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | J77 Advanced Bank Account Management test script, part 2: two-person and workflow bank account lifecycles, payment approvers, powers of attorney, reviews. |

### Cash Operations and Cash Positioning

How manual bank statements, memo records, liquidity items, cash flow analyzer, BCM payment approval and bank transfers support daily basic and advanced cash operations.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit\|Basic Cash Operations (BFB_AE) Test Script, SAP S/4HANA Cloud Public Edition (BFB_S4CLD2608_BPD_EN_AE)]] | Test script for scope item BFB (UAE/AE, company code 3310, AED): cash operations setup, bank statements, memo records, cash reports, One Exposure and Flow Builder jobs. |
| [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-01\|Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for SAP scope item J78 Advanced Cash Operations (AE, co. code 3310): cash config, BCM payment approval, bank transfers, cash trade requests. |
| [[05-treasury-and-cash-management/advanced-cash-operations-j78-ae-test-script-sap-s-4hana-cloud-public-e-part-02\|Advanced Cash Operations (J78_AE) Test Script - SAP S/4HANA Cloud Public Edition (J78_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP S/4HANA Cloud 2608 (AE) test script J78, part 2: step-by-step Fiori tests for bank balances, reconciliation, snapshots, monitors and cash reports. |

### In-House Banking

How in-house bank accounts process payments on behalf, intercompany payments and central incoming payments, with end-of-day processing and reclassification.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-in-house-banking-6bp-ae-sap-s-4hana-cloud-public-edition-2\|Test Script: In-House Banking (6BP_AE) - SAP S/4HANA Cloud Public Edition 2608 (6BP_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (AE, release 2608) for In-House Banking: prerequisites, setup, payments on behalf, intercompany, central incoming, end of day, reclassification. |

### Hedge Accounting for FX Exposures

How FX forwards, NDFs, swaps and options are designated as IFRS, US GAAP or local GAAP cash flow hedges, from hedging area and exposure through period-end and reclassification.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-hedge-accounting-for-fx-forward-group-ledger-ifrs-1xd-ae-7\|Test Script: Hedge Accounting for FX Forward – Group Ledger IFRS (1XD_AE) (1XD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (scope item 1XD, AE) for IFRS 9 cash flow hedge accounting with FX forwards/NDF, from hedging area to reporting. |
| [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-ifrs-2rw-ae-test-script-85\|Hedge Accounting for FX Option – Group Ledger IFRS (2RW_AE) – Test Script (2RW_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 2RW_AE, 2608): IFRS 9 cash flow hedge accounting with European FX options, from hedging area to reclassification. |
| [[05-treasury-and-cash-management/hedge-accounting-for-fx-swap-group-ledger-ifrs-2uf-ae-870\|Hedge Accounting for FX Swap – Group Ledger IFRS (2UF_AE) (2UF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 2UF (AE): IFRS 9 cash flow hedge accounting with FX swap overhedge processing, from hedging area to period-end, maturity and termination. |
| [[05-treasury-and-cash-management/test-script-hedge-accounting-for-fx-forward-local-gaap-3x1-ae-984\|Test Script: Hedge Accounting for FX Forward – Local GAAP (3X1_AE) (3X1_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (3X1, AE) for cash flow hedge accounting with FX forwards/NDF under local GAAP: hedging area to reporting, plus appendices. |
| [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-local-gaap-3x2-ae-985\|Hedge Accounting for FX Option – Local GAAP (3X2_AE) (3X2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 3X2_AE: cash flow hedge accounting with European FX options (vanilla and collar) under local GAAP, valuation area AE0. |
| [[05-treasury-and-cash-management/hedge-accounting-for-fx-forward-group-ledger-us-gaap-3x3-ae-986\|Hedge Accounting for FX Forward – Group Ledger US GAAP (3X3_AE) (3X3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3X3_AE: US GAAP cash flow hedge accounting with FX forwards/NDFs, from hedging area to reclassification. |
| [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script\|Hedge Accounting for FX Option – Group Ledger US GAAP (3X4_AE) – Test Script (3X4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3X4: US GAAP cash flow hedge accounting with European FX options (vanilla and collar), incl. dedesignation, termination. |

### Intercompany Debt and Investment (Mirror Loans)

How intercompany loans and current-account instruments create automatic mirror deals and post in the local, IFRS (002) and US GAAP (003) valuation areas.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-intercompany-process-for-debt-and-investment-mgmt-1yi-ae-7\|Test Script: Intercompany Process for Debt and Investment Mgmt (1YI_AE) (1YI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1YI (AE): intercompany loans with automatic mirror deals, covering roles, prerequisites and Fiori test steps. |
| [[05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-ifrs-2o\|Test Script: Intercompany Debt and Investment Mgmt – Group Ledger IFRS (2OI_AE) (2OI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2OI_AE: intercompany loans with mirror deals, posted in parallel IFRS valuation area 002. |
| [[05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-us-gaap\|Test Script: Intercompany Debt and Investment Mgmt – Group Ledger US GAAP (34L_AE) (34L_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 34L_AE: intercompany loans posted to US GAAP parallel valuation area 003, from deal creation to period-end. |

### Treasury Trading Platforms and SWIFT Correspondence

How FX, money market and fund trades arrive from trading platforms (incl. back-to-back and intercompany) and how treasury confirmations (MT300/MT320) exchange via SWIFT.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-01\|Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 1 of 2]] | Test script for SAP S/4HANA Cloud scope item 2F5 (2608): FX, money market and MMF trading via trading platforms, external and intercompany scenarios. |
| [[05-treasury-and-cash-management/test-script-treasury-trading-via-trading-platforms-2f5-sap-s-4hana-clo-part-02\|Test Script: Treasury Trading via Trading Platforms (2F5) - SAP S/4HANA Cloud Public Edition (2F5_S4CLD2608_BPD_EN_XX) — part 2 of 2]] | S/4HANA Cloud 2608 test script (2F5): treasury trading via external platforms - MM/MMF steps, optional trade tasks, mapping and business-rule examples. |
| [[05-treasury-and-cash-management/treasury-correspondence-integration-with-swift-network-3qm-test-script\|Treasury Correspondence Integration with SWIFT Network (3QM) - Test Script, SAP S/4HANA Cloud Public Edition (3QM_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 3QM: set up and test treasury SWIFT correspondence (MT300/MT320) via SAP Multi-Bank Connectivity, from BP settings to settlement. |

### Treasury Analytics and Executive Dashboard

Which FX, liquidity and cash KPIs the Foreign Exchange Overview (F2331) and Treasury Executive Dashboard (F4316) analytical apps show.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-sap-fiori-analytical-apps-for-treasury-and-risk-management\|Test Script: SAP Fiori Analytical Apps for Treasury and Risk Management (1MN) (1MN_S4CLD2608_BPD_EN_XX)]] | Test script for SAP S/4HANA Cloud scope item 1MN: Foreign Exchange Overview (F2331) and Treasury Executive Dashboard (F4316), eight tabstrips. |

### IFRS 18 Presentation in Treasury and Risk Management

How IFRS 18 account assignment reference substitution rules and functional areas are configured in TRM and checked via position indicator and posting journal.

| Node | Description |
| --- | --- |
| [[05-treasury-and-cash-management/test-script-ifrs-18-compliance-in-treasury-and-risk-management-83d-124\|Test Script: IFRS 18 Compliance in Treasury and Risk Management (83D) (83D_S4CLD2608_BPD_EN_XX)]] | Test script for SAP scope item 83D: configure IFRS 18 AAR substitution rules and functional areas in TRM, then check position indicator and posting journal. |

## Related categories
- related-to :: [[03-financial-accounting-and-close/_cluster]]
