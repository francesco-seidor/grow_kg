---
id: 03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-ae-133
title: BP CLD ENTPR 2608 Account Master Data for YCOA AE (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 best-practice G/L account master data for chart YCOA, UAE company code 3310, plus SD account determination, CO defaults and UAE VAT tax codes."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/chart-of-accounts-and-gl-accounts, topic/uae-tax-codes]
aliases: [BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE]
keywords: [Chart of Accounts YCOA and G/L Account Creation, chart of accounts, gl account master data, sd account determination, uae vat tax codes, tax account determination, sales commission accounts, cost element defaults, fixed asset accounts, lease accounting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-133
topic: 03-financial-accounting-and-close/chart-of-accounts-and-gl-accounts
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# BP CLD ENTPR 2608 Account Master Data for YCOA AE (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE.xlsx`, extracted with `xlsx2md`. Grouped under **Chart of Accounts YCOA and G/L Account Creation** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## BP CLD ENTPR 2608 Account Master Data for YCOA AE

### Sheet: YCOA_local

| YCOA Chart of Accounts AE (CoCd 3310) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chart of Accounts | Company Code | G/L Account Number | Long Text EN | G/L Account Type | Balance Sheet Account | Group account Number | P&L Statement Acct Type | Account Group | Trading Partner | Functional Area | Planning group | Planning Level | Financial budget | Field Status Group | House Bank | Account ID | Exchange rate difference key | Reconciliationaccount for acct type | Tax category | Interest indicator | Account currency | Acct Managed in Ext. System | Cash receipt account / cash disbursement | Post automatically only | Open Item Management | Interest calc. frequency | Sort key | Alternative Account No. | Recon. acct ready for input | Recovery Indicator | Commitment Item | Posting without tax allowed | Only balances in local crcy | Valuation group | Inflation key | Tolerance group | Ledger Group-Specific Clearing |
| I_KTOPL | I_BUKRS | I_SAKNR | I_TXT50_EN | I_GLACCOUNT_TYPE | I_XBILK | I_BILKT | I_GVTYP | I_KTOKS | I_VBUND | I_FUNC_AREA | I_FDGRV | I_FDLEV | I_FIPLS | I_FSTAG | I_HBKID | I_HKTID | I_KDFSL | I_MITKZ | I_MWSKZ | I_VZSKZ | I_WAERS | I_WMETH | I_XGKON | I_XINTB | I_XOPVW | I_ZINRT | I_ZUAWA | I_ALTKT | I_XMITK | I_RECID | I_FIPOS | I_XMWNO | I_XSALH | I_BEWGP | I_INFKY | I_TOGRU | I_XLGCLR |
| YCOA | 3310 | 0010010000 | Petty Cash | X | X |  |  | FIN. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  | X |  |  | 00 | 003 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0010020000 | Petty Cash Journal - postings automatic only | X | X |  |  | FIN. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  | X | X |  | 00 | 003 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0010090000 | Restricted Cash – Collateral (TRM) | X | X |  |  | FIN. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  | X |  |  | 00 | 003 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0011001000 | Main Bank Account (Cash/B) | C | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  |  |  | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001010 | Cash Payment (Cash/S) | C | X |  |  | FIN. |  |  |  | B3 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001020 | Bank Transfer (Domestic/SEPA/Foreign) (Cash/S) | C | X |  |  | FIN. |  |  |  | B2 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001030 | Other Interim Transfers (Cash/S) | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001040 | Direct Debit (C/S) | C | X |  |  | FIN. |  |  |  | B4 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001045 | Returns (Cash/S) | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001050 | Checks Out (C/S) | C | X |  |  | FIN. |  |  |  | B1 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001055 | BoE Out (Cash/S) | C | X |  |  | FIN. |  |  |  | B7 | 000 | YB05 |  |  |  |  |  |  | AED |  | X | X | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001056 | Bank 1 - Supplier Financing Out | C | X |  |  | FIN. |  |  |  | B0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001057 | Bank VCard Out | C | X |  |  | FIN. |  |  |  | B0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001058 | ARF Fund in Transit | C | X |  |  | FIN. |  |  |  | B0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001060 | Checks In (C/S) | C | X |  |  | FIN. |  |  |  | B8 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001065 | BoE Collection (Cash/S) | C | X |  |  | FIN. |  |  |  | B9 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001070 | Check Clearing Account (Cash/S) | C | X |  |  | FIN. |  |  |  | B8 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001080 | Cash Receipt (C/S) | C | X |  |  | FIN. |  |  |  | B9 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001090 | Technical Account for Bank Statement (Cash/S) | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001091 | Bank 1 - Refunds / Repayments (FI-CA) | C | X |  |  | FIN. |  |  |  | B3 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001092 | Bank 1 - Clarification (FI-CA) | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001093 | Other Interim Transfers (X)(FI-CA) | X | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001400 | Clearing Account OBO Payments (APM) | X | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001410 | Clearing Account Intercompany payments (APM) | X | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011001420 | Clearing Account Central Incoming payments (APM) | X | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011008000 | Digital Payments Acquirer Bank (Cash/B) | C | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  |  |  | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011008030 | Digital Payments Transfer Account (Cash/S) | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  | 009 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011008050 | DP Acquirer Clrng (Stlmnt) (Cash/S) pending | C | X |  |  | FIN. |  |  |  | B8 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 009 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011008070 | Digital Payments Acquirer Clrng (Stlmnt) (Cash/S) | C | X |  |  | FIN. |  |  |  | B8 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  | 009 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011009355 | BoE-PDC Out (Balance Sheet) | X | X |  |  | FIN. |  |  |  | B7 | 000 | YB05 |  |  |  |  |  |  | AED |  | X | X | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011009366 | BoE-PDC Discount (Balance Sheet) | X | X |  |  | FIN. |  |  |  | B9 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011009367 | BoE-PDC Forfeit (Balance Sheet) | X | X |  |  | FIN. |  |  |  | B9 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011999000 | Bank 4 - External Payments Account | C | X |  |  | FIN. |  |  |  | F0 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  |  |  | 027 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011999030 | Bank 4 - External Payments Clearing Account | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  | 009 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0011999070 | Bank 4 - External Payments Settlement Account | C | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X |  | 009 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012021000 | Short Term Investments, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021100 | Short Term Investments, Affili., No Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021200 | Short Term Investments, Affiliated, Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021300 | Investment in Bonds, Short term, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021400 | Investment in Bonds, ST, Affi., No Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021500 | Investment in Bonds, Short term, Affi., Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012021600 | Investment in ABS/MBS, Short term (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012041000 | Derivatives Valuation Balances, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012041100 | Derivatives Valuation Bal, Affil., No Consol.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012041200 | Derivatives Valuation Bal, Affili., Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012042000 | Derivatives Assets, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012042100 | Derivatives Assets, Affiliated, No Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012042200 | Derivatives Assets, Affiliated, Consolidation(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012043000 | Investment in Equity Securities(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012044000 | Investment in Non-Affiliated Company (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012044100 | Investment in Associate or Joint Venture (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012044200 | Investment in Subsidiary (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012100000 | Receivables Domestic | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012100100 | Receivables Domestic - One Time Accounts | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012100200 | Receivable - Contract Accounts | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | V | * |  | AED |  |  |  |  | 00 |  |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0012101000 | Receivables Domestic due > 1 Year | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012101500 | Receivables due > 1 year (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012102000 | Receivables Domestic Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012102100 | Receivables Adjustment (RAR) | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012102500 | Receivable Adjustments due > 1 year (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012103000 | Rcvl. Adj. for Cust. with a Cred. Balance (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012110000 | Other Down Payments Made Current Assets | X | X |  |  | ABST |  |  |  |  | 000 | YB26 |  |  |  | K | -B |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012110100 | Down Payments Made due > 1 Year | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012111000 | Input Tax Clrg-other Down Pyts Made for Curr. Asts | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012112000 | Down Payments made for Inventory | X | X |  |  | ABST |  |  |  |  | 000 | YB26 |  |  |  | K | -B |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012119000 | Down Payment Requests Vendors | X | X |  |  | ABST |  |  |  |  | 000 | YB01 |  |  |  | K | -B |  | AED |  |  |  |  | 00 | 026 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012119100 | Outgoing Payment (Request) (FI-CA) | X | X |  |  | ABST |  |  |  |  | 000 | YB01 |  |  |  | V | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012119200 | Adjustment Account Vendor Down Payments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012120000 | Receivables Foreign | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012120100 | Receivables Foreign - One Time Accounts | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012121000 | Receivables Foreign due > 1 Year | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012122000 | Receivables Foreign Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012200000 | Lease Receivables - Land & Land Improvements (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200100 | Lease Receivables - Buildings (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200200 | Lease Receivables - Machinery & Equipment (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200300 | Lease Receivables - Motor Vehicles (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200400 | Lease Receivables - Office Equipment (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200500 | Lease Receivables - Furniture and Fixtures (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012200600 | Lease Receivables-Compt Hardwr and Eqpmt(ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0012300000 | Receivables affiliated Companies | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012301000 | Receivables affiliated Companies > 1 Year | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012302000 | Receivables affiliated Companies Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012303000 | Receivables vs affil. Companies (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012305000 | Receivables Affiliated Companies (IHB) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012305100 | Receivables / liabilities (IHB) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012400000 | Allowance for Doubtful Receivables | X | X |  |  | ABST |  |  |  |  | 000 | YB12 |  |  |  | D |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012401000 | Individual Value Adjustments for Receivables | X | X |  |  | ABST |  |  |  |  | 000 | YB12 |  |  |  | D |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012401100 | Allowance for Doubtful Receivables(Valuation) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012401200 | Doubtful Receivables (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012401300 | Offset Account for Doubtful Receivables (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012401400 | Allowance for Bad Debt-Ind Val Value Adjust(FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012401500 | Allowance for Bad Debt-Flat Rate Val Adj. (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012402000 | Depreciation Receivables from Aff.Companies | X | X |  |  | ABST |  |  |  |  | 000 | YB12 |  |  |  | D |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012410000 | Clearing of Guarantee Given (Customers) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012411000 | Guarantees given to Customers | X | X |  |  | ABST |  |  |  |  | 000 | YB01 |  |  |  | D |  |  | AED |  |  |  |  | 00 | 026 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012420000 | Security Deposit Customers | X | X |  |  | ABST |  |  |  |  | 000 | YB12 |  |  |  | D |  |  | AED |  |  |  |  | 00 | 026 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012500000 | Interest Receivables | X | X |  |  | ABST |  |  |  |  | 000 | YB01 |  |  |  | D |  |  | AED |  |  |  |  | 00 | 031 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012501000 | Clearing Interest Receivables | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012510000 | Accounts Receivable - BoE Receivable | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012511000 | Accounts Receivable - BOE Bounced Check | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | D |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012512100 | Letter of Credit Receivable(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012530000 | Accounts Receivable - Payment Cards | X | X |  |  | SAKO |  |  |  |  | 000 | YB12 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012530100 | Accounts Receivable - External Payments Clearing | X | X |  |  | SAKO |  |  |  |  | 000 | YB12 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012530110 | Accounts Receivable - External Payments | X | X |  |  | SAKO |  |  |  |  | 000 | YB12 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012530200 | Accounts Receivable - Payment Cards (FI-CA) | X | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012530300 | Accounts Receivable - Paypal (FI-CA) | X | X |  |  | FIN. |  |  |  | B5 | 000 | YB05 |  |  |  |  |  |  | AED |  | X |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012531000 | Accounts Receivable - Unapplied Checks | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012532000 | Clrg Cont.Claims-Check/Bill of Exch. Payments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012540000 | Other Receivables (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012540200 | Other Receivables Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012541000 | Receivables from Tax Authorities (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012542000 | Receivables from Employees Overpay (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012543000 | Receivables from Partners (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012544000 | Sold Receivables (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012544100 | Clearing of Sold Receivables (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012544200 | Adjustment of Sold Receivables (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012545000 | Sold Receivables (ARF Funder) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012545100 | Clearing of Sold Receivables (ARF Funder) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012545200 | Adjustment of Sold Receivables (ARF Funder) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0012549000 | Depreciation from other Receivables | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012550000 | Unbilled Revenue | X | X |  |  | SAKO |  |  |  |  | 000 | YB13 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0012561000 | Prepaid Expenses | X | X |  |  | SAKO |  |  |  |  | 000 | YB13 |  |  |  |  | - |  | AED |  |  |  | X | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0012562000 | Deferred Income | X | X |  |  | SAKO |  |  |  |  | 000 | YB13 |  |  |  |  | + |  | AED |  |  |  | X | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0012590000 | Vendors with a Debit Balance | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012600000 | Input Tax (VST) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | < |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012605000 | Import Sales Tax paid (VST) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | < |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012610000 | Input Tax | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | < |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012660000 | Reclaimable Tax for Interest Income(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012701000 | Accr. Interest Inc./Defer. Int. Exp., Unaffi.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012701100 | Accr. Int. Inc./Defer. Int. Exp., Aff., NoCo.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012701200 | Accr. Int. Inc./Defer. Int. Exp., Affi., Con.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012702000 | Accrued Bonds Interest Income, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012702100 | Accrued Bonds Int. Income, Affil., No Con.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012702200 | Accrued Bonds Interest Income, Affil., Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012702300 | Accrued ABS/MBS Interest (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012703000 | Pre-issuance Loss/Gain(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012801000 | Bonds Interest Receivable, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012801100 | Bonds Interest Receivable, Affili., No Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012801200 | Bonds Interest Receivable, Affili., Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012802000 | Bonds Repayment Receivable, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012802100 | Bonds Repayment Receivable, Affili., No Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012802200 | Bonds Repayment Receivable, Affilia., Consol.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012803000 | ABS/MBS Interest Receivable (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0012803100 | ABS/MBS Repayment Receivable (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0013100000 | Inventory - Raw Material | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0013200000 | Inventory - Work In Progress | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0013210000 | WIP | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0013300000 | Inventory - Semi Finished Goods | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0013400000 | Inventory - Finished Goods | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0013500000 | Inventory - Packaging Materials | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0013600000 | Inventory - Trading Goods | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0013601000 | Inventory Adjustment Account | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0013701400 | WIP Deferred Revenue | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013711100 | WIP Accrued Revenue | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013711400 | WIP Accrued Revenue - Fixed Price | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013711900 | WIP Unbilled Revenue | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013715600 | WIP Accrued Revenue On Account Adjustment | X | X |  |  | SAKO |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013811100 | Deferrals Revenue | X | X |  |  | SAKO |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0013815600 | Deferrals Revenue - On Account Adjustment | X | X |  |  | SAKO |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0014107000 | Loans to Staff | X | X |  |  | ABST |  |  |  |  | 000 | YB40 |  |  |  | D |  |  | AED |  |  |  |  | 00 | 031 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0015200000 | Salary and Wages Advances | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0015300000 | Trip Costs in Advance | X | X |  |  | SAKO |  |  |  |  | 000 | YB70 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0016000000 | Land & Land Improvements | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016001000 | Buildings | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016002000 | Machinery & Equipment | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016003000 | Building Improvements | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016004000 | Motor Vehicles | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016005000 | Office Equipment | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016006000 | Furniture and Fixtures | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016007000 | Computer Hardware and Equipment | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016008000 | Computer Software | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016009000 | Assets under Construction | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016009100 | Asset Retirement Obligation | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016010000 | Down Payments made on Tangible Assets w/o FI-AA | X | X |  |  | ABST |  |  |  |  | 000 | YB39 |  |  |  | K | -B |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016010500 | Input Tax Clearing Tangibles Down Payments made | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0016012000 | Capitalized Down Payments made on Fixed Assets | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016013000 | Clearing capitalized Down Payments on Fixed Assets | X | X |  |  | SAKO |  |  |  |  | 000 | YB08 |  |  |  |  |  |  | AED |  |  | X |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016014000 | Technical Clrng Acct Integrated Asset Acquisition | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016014100 | Clearing Account for Asset Acquisition | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016014200 | ARO Clearing Amt for Asset Acquisit | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016015000 | Offsetting Account Revaluation APC | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016020000 | Low Value Assets | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0016050000 | Land & Land Improvements (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016051000 | Buildings (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016052000 | Machinery & Equipment (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016054000 | Motor Vehicles (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016055000 | Office Equipment (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016056000 | Furniture and Fixtures (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016057000 | Computer Hardware and Equipment (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0016059000 | Leasing Clearing Account | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017000000 | Accumulated Depreciation - Land Improvements | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017001000 | Accumulated Depreciation - Buildings | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017002000 | Accumulated Depreciation - Machinery & Equipment | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017003000 | Accumulated Depreciation - Building Improvements | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017004000 | Accumulated Depreciation - Motor Vehicles | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017005000 | Accumulated Depreciation - Office Equipment | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017006000 | Accumulated Depreciation - Furniture and Fixtures | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017007000 | Accumulated Depreciation - Computer Hardware | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017008000 | Accumulated Depreciation - Computer Software | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017009100 | ARO Accumulated Depreciation | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017020000 | Accumulated Depreciation - Low Value Assets | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0017050000 | Accumulated Depreciation - Land Improvements (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017051000 | Accumulated Depreciation - Buildings (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017052000 | Accumulated Depr'n - Machinery & Equipment (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017054000 | Accumulated Depreciation - Motor Vehicles (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017055000 | Accumulated Depreciation - Office Equipment (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017056000 | Accumulated Depr'n Fixtures Fittings (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0017057000 | Accumulated Depreciation - Computer Hardware (ROU) | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0018010000 | Investment Subsidiaries | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018020000 | Other Long Term Investments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018030000 | Long Term Investments, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018030100 | Long Term Investments, Affili., No Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018030200 | Long Term Investments, Affiliated, Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018031000 | Investment in Bonds, Long term, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018031100 | Investment in Bonds, Long term, Affil, No Con(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018031200 | Investment in Bonds, Long term, Affil., Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0018032000 | Investment in ABS/MBS, Long Term (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0019210000 | Other Receivables > 1 year | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0019310000 | Internal Development | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019320000 | Intangible Assets | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019330000 | Goodwill | X | X |  |  | ANL. |  |  |  |  | 000 | YB07 |  |  |  | A | - |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019410000 | Accumulated amortization - Internal Development | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019420000 | Accumulated Amortization - Intangible Assets | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019430000 | Accumulated Amortization – Goodwill | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  | A |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0019999000 | Money Market Fund (TRM) | X | X |  |  | FIN. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  | X |  |  | 00 | 003 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021100000 | Payables Domestic | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021100100 | Payables Domestic - One Time Accounts | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021100200 | Payables Domestic due within 1-5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021100300 | Payables Domestic due > 5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021102000 | Payables Domestic Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021105000 | Travel Expenses Payable | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021110000 | Goods Received/Invoice Received Consignt/Pipeline | X | X |  |  | MAT. |  |  |  |  | 000 | YB59 |  |  |  |  | - |  | AED |  |  |  | X | 00 | 029 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021120000 | Goods Received/Invoice Received | X | X |  |  | MAT. |  |  |  |  | 000 | YB45 |  |  |  |  | - |  | AED |  |  | X | X | 00 | 014 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021121000 | GR/IR Sett.transferred (material ledger) | X | X |  |  | MAT. |  |  |  |  | 000 | YB45 |  |  |  |  | - |  | AED |  |  | X | X | 00 | 014 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021122000 | Goods Received / Invoice Received Adjustment | X | X |  |  | MAT. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021180000 | Customers with a Credit Balance | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021185000 | Customers with a Credit Balance (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021185100 | Security deposit (Request)(FI-CA) | X | X |  |  | ABST |  |  |  |  | 000 | YB31 |  |  |  | V | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021186000 | Down payment-Customers (FI-CA) | X | X |  |  | ABST |  |  |  |  | 000 | YB31 |  |  |  | V | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021190000 | Down Payments-Customers (sp ind A) | X | X |  |  | ABST |  |  |  |  | 000 | YB31 |  |  |  | D | +B |  | AED |  |  |  |  | 00 | 031 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021190100 | Down Payments received due within 1-5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021190200 | Down Payments received due > 5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021191000 | Down Payment Requests-Customers (Sp Ind F) | X | X |  |  | ABST |  |  |  |  | 000 | YB31 |  |  |  | D | +B |  | AED |  |  |  |  | 00 | 031 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021191100 | Contract Liability for Down Payments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021191200 | Contract Liability for Down Payment Requests | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021191500 | Tax on sls/purch-settlement of Customer Down Pyts | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021192000 | Adjustment account down payments received | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021200000 | Payables Foreign | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021200100 | Payables Foreign - One Time Accounts | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021200200 | Payables Foreign due within 1-5 years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021200300 | Payables Foreign due > 5 years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021202000 | Payables Foreign Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021300000 | Payables affiliated Companies | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K | * |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021300200 | Payables affiliated Companies due 1-5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021300300 | Payables affiliated Companies due > 5 years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021302000 | Payables affiliated Companies Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021303000 | Payables vs affiliated Companies (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021305000 | Liabilities Affiliated Companies (IHB) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021311000 | Supplier Financing Payable | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021311010 | Accounts Payable - Supplier Financing VCard | X | X |  |  | ABST |  |  |  |  | 000 | YB67 |  |  |  | K |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021312000 | Letter of Credit Payable(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021320000 | Lease Out Clearing Account (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021350000 | Clearing Invoice Reduction | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  | X |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021500000 | Payroll Liabilities, Employees | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021501000 | Accrued Net Payroll | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021502000 | Payroll Taxes | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021502100 | Payroll Liabilities: Taxes, Insurances, Pensions | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021503000 | Payroll - Social Security | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021505000 | Payroll - Savings Plan | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021508000 | Payroll - Garnishment | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021509000 | Payroll - Workers' Compensation Association | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021518000 | Document split acct (trip costs co.code clrg HR) | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021519000 | Payroll Allocation | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 016 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021600000 | Reserve for Deferred Taxes | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021603110 | Withholding tax receivables (IHB) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021720000 | Other Payables (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021720100 | Guarantees received from Vendors | X | X |  |  | ABST |  |  |  |  | 000 | YB01 |  |  |  | K | * |  | AED |  |  |  |  | 00 | 026 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021720200 | Other Payables Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021720230 | Other Payable for Subsribed Services (FI-CA) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021721000 | Reserves for Unrealized Costs | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021722000 | Manual Reserves for Imminent Loss | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021723000 | Manual Reserves for Anticipated Sales Deductions | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021724000 | Manual Reserves for Unrealized Costs | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021725000 | Accrued Expenses–Goods & Services | X | X |  |  | SAKO |  |  |  |  |  | YB01 |  |  |  |  |  |  | AED |  |  |  | X |  | 011 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021730000 | Freight Clearing Account (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  | X | X | 00 | 014 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021730010 | Freight Clearing Accnt MM (RUA) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  |  | X | 00 | 014 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021730020 | Freight Clearing Account - TM1 (TM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 010 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021735000 | Delivery Costs Provision (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 014 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021735500 | Delivery Costs Clearing (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 014 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021740000 | Customs Duty Clearing Account (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  | X | X | 00 | 014 |  |  |  |  | X | X |  |  |  |  |
| YCOA | 3310 | 0021745000 | Customs Provision (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  | X |  | 00 | 014 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021750000 | Clearing Vendor Discounts - Net Method | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  | X | X | 00 | 101 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021751000 | Clearing - Guarantees Received Vendors | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021760000 | Freight Provision (MM) | X | X |  |  | MAT. |  |  |  |  | 000 | YB17 |  |  |  |  | - |  | AED |  |  | X |  | 00 | 014 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021770000 | Accrued Volume Rebate | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021771000 | Accrued Supplier Rebate | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021772000 | Provision for Sales Commissions | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021772100 | Provision for Internal Commissions | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0021775000 | Accrual Statistical condition | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 012 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021780000 | Freight Provision SD | X | X |  |  | MAT. |  |  |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 031 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0021900000 | Payment Request Clearing Account(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0021901000 | Virtual Card Clearing for Accnt. Payable Financing | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022000000 | Output Tax (MWS) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | > |  | AED |  |  | X |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022090000 | Alterative Tax Payable - UMS | X | X |  |  | SAKO |  |  |  |  | 000 | YB41 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022100000 | Acquisition Tax | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | > |  | AED |  |  | X |  | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022510000 | Loans from Banks (no recon acct) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0022512000 | Loans from Banks Adjustments | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0022540000 | Short Term Debts, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022540100 | Short Term Debts, Affiliated,No Consolidation(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022540200 | Short Term Debts, Affiliated, Consolidation(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022541000 | Derivatives Liabilities, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022541100 | Derivatives Liabilities, Affil., No Consolid.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022541200 | Derivatives Liabilities, Affili., Consolidat.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022541500 | Bond Payable, Short term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542000 | Accr. Interest Exp./Defer. Int. Inc., Unaffi.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542100 | Accr. Int. Exp./Defer. Int. Inc., Aff., NoCo.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542200 | Accr. Int. Exp./Defer. Int. Inc., Affi., Con.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542300 | Accrued Bond Interest Expense(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542400 | Discount/Bond Issuance Costs, Short term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022542500 | Premium/Bond Issuance Costs, Short term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022543000 | Price Valuation Reserve (OCI) Gains, Unaffil.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022543100 | Price Valua. Reserve (OCI) Gains, Affi., NoCo(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022543200 | Price Valua. Reserve (OCI) Gains, Affi., Con.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022543300 | Other Compr. Inc. (OCI) from Equ. Meth. Inv. (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022544000 | Price Valuation Reserve (OCI) Losses, Unaffi.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022544100 | Price Valu. Reser. (OCI) Losses, Affi., NoCo.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022544200 | Price Valu. Reser. (OCI) Losses, Affi., Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022545000 | FX Valuation Reserve (OCI) Gains, Unaffiliat.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022545100 | FX Valua. Reserve (OCI) Gains, Affil., NoCon.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022545200 | FX Valua. Reserve (OCI) Gains, Affi., Consol.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022546000 | FX Valuation Reserve (OCI) Losses, Unaffili.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022546100 | FX Valua. Reserve (OCI) Losses, Affi., NoCon.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022546200 | FX Valua. Reserve (OCI) Losses, Affil., Cons.(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022547000 | Hedging Reserve (OCI I)(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022548000 | Cost of Hedging Reserve (OCI II)(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022549000 | Treasury Techinal Clearing Account(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0022549300 | Other Considerations Clearing Account (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0023000000 | Lease Liability - Land & Land Improvements (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000100 | Lease Liability - Buildings (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000200 | Lease Liability - Machinery & Equipment (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000300 | Lease Liability - Motor Vehicles (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000400 | Lease Liability - Office Equipment (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000500 | Lease Liability - Furniture and Fixtures (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023000600 | Lease Liability-Computer Hardware&Equipment (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0023007000 | Provision of Asset Retirement Obligation (ROU) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024010000 | GR/IR: Goods and Services not yet delivered | X | X |  |  | MAT. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024020000 | GR/IR: Goods and Services not yet invoiced | X | X |  |  | MAT. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024030000 | Tax Provisions | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024031000 | Pension Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024031100 | Pension Provision - ledgerspecific | X | X |  |  | SASL |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  | X |
| YCOA | 3310 | 0024032000 | Trade Tax Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024033000 | Corporate Income Tax Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024034000 | Capital Gains Tax Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024035000 | Foreign Withholding Tax Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024036000 | Provision for Other Income and Revenue Tax | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024037000 | Provision for Deferred Tax Liabilities | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024090000 | Other Provisions | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024090100 | ARO Provision | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024091000 | Provisions for Guarantees | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024093000 | Provisions for Indeterminate Payables | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024097000 | Prov for expected Losses fr executory Contracts | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024098000 | Asset Revaluation Reserve - ROU | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024098300 | Capital Reserve | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024098400 | Legal Reserve | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024098500 | Statutory Reserve | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024098600 | Other Reserves | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0024098700 | Special tax-allowable Reserve §6b | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0024099900 | Correction of Provisions | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  | X | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0026900000 | Functional Area Clearing | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029110000 | Other Payables due within 1-5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0029120000 | Other Payables due > 5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0029130000 | Loans from Banks remaining Life 1-5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029131000 | Loans from Banks remaining Life > 5 Years | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029140000 | Long Term Debts, Unaffiliated(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029140100 | Long Term Debts, Affiliated, No Consolidation(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029140200 | Long Term Debts, Affiliated, Consolidation(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029141000 | Bond Payable, Long term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029141100 | Discount/Bond Issuance Costs, Long term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029141200 | Premium/Bond Issuance Costs, Long term(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029500100 | Document Split Clearing Account | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0029500900 | Document Split Clearing Account CO | X | X |  |  | SAKO |  |  |  |  | 000 | YB11 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0031000000 | Common Stock | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0031100000 | Preferred Stock | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0032000000 | Capital in Excess of Par Value | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0032100000 | Paid in Capital from treasury stock | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0032100010 | Paid in Capital from Equity Method Inv. (TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0033000000 | Retained Earnings | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039911000 | Inventory - Initial Entry of Raw Material Balances | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039912000 | Inventory - Initial Entry SF & Finish Gds Balances | X | X |  |  | MAT. |  |  |  |  | 000 | YB06 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039913000 | Initial FI-AM offset | X | X |  |  | ANL. |  |  |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039914000 | Initial FI-AR offset | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039915000 | Initial FI-AP offset | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039916000 | Initial other GL offset | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039917000 | Initial other Open Item GL offset | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039918000 | Initial TR Positions Offset(TRM) | X | X |  |  | SAKO |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039920010 | Carbon Transition Account (Green Ledger) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039920020 | GHG Liabilities Collection Account (Green Ledger) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039920030 | GHG Liabilities transfrd to customers(GreenLedger) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0039921000 | Retained GHG Liabilities (Green Ledger) | X | X |  |  | SAKO |  |  |  |  | 000 | YB19 |  |  |  |  |  |  | AED |  |  |  | X | 00 |  |  |  |  |  |  | X |  |  |  |  |
| YCOA | 3310 | 0041000000 | Revenue Domestic - Product | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041000400 | Sales Revenue w/ Cost Element | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041001000 | Revenue Foreign - Product | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041001500 | Revenue Affiliate - Product | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041003000 | Accrued Revenue – EBR Adjustment | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041005100 | Billed Revenue (FI-CA) | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041007100 | On-Account Issued (Service Provider) | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041007200 | On-Account Utilized (Service Provider) | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041090000 | Other Operating Revenue | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041910000 | Billed Revenue Domestic | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041940000 | Billed Revenue Foreign | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0041970000 | Billed Revenue Affiliated | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044000000 | Over/Underpayments and Unallowed Deductions | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044001000 | Sales Rebates | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044002000 | Sales Discounts - Domestic | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044002100 | Sales Discounts - Foreign | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044002200 | Sales Discounts - Affiliated | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044003000 | Customer Sales Deduction - Domestic | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044003100 | Customer Sales Deduction - Foreign | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044003200 | Customer Sales Deduction - Affiliated | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044004000 | Sales Deduction - Material | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044005000 | Free Goods and Discount in kind | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044006000 | Sales Deduction - Quantity | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0044008000 | Sales Deduction (FI-CA) | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044008100 | Rev. from Return Payment (FI-CA) | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044401100 | Revenue Adjustment | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044405600 | Revenue - On Account Adjustment | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044420000 | Revenue Adjustment | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044421000 | Rev Adjust for allocation (RAR) | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044910000 | Sales Deduction Domestic | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044940000 | Sales Deduction Foreign | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0044970000 | Sales Deduction Affiliated | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0049999900 | Clearing Target Revenue Reallocation | P |  |  | X | ERG. |  | YB10 |  |  | 000 | YB29 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050100000 | Cost of Goods Sold (Raw Material w/o Cost Element) | N |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050150000 | Cost of Goods Sold (PackagingMat w/o Cost Element) | N |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050200000 | Cost of Goods Sold (Trade w/o Cost Element) | N |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050300000 | Cost of Goods Sold (SF & Finish Goods w/o Cost El) | N |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050301000 | COGS Direct Material | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050302000 | COGS Third Party | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050303000 | COGS Material Overhead | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050304000 | COGS Personnel Time | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050305000 | COGS Machine Time | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050306000 | COGS Setup Time | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050307000 | COGS Production Overhead | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050308000 | COGS Credits (Co/By-Pr) | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050309000 | COGS - Hardware | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050309500 | COGS - Licenses | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0050309600 | Cost of Sales for Subscribed Services (FI-CA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0051100000 | Consumption - Raw Material | P |  |  | X | ERG. |  |  |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0051500000 | Consumption - Packaging Material | P |  |  | X | ERG. |  |  |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0051600000 | Consumption - Trading Goods | P |  |  | X | ERG. |  |  |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0051700000 | Consumption - Repair Material | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0051900000 | Consumption - Subcontracting, w/o CE | N |  |  | X | ERG. |  | YB18 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0051950000 | Consumption - Subcontracting | P |  |  | X | ERG. |  |  |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052001000 | Loss Inventory Variance (Raw & Trade) | P |  |  | X | ERG. |  |  |  |  | 000 | YB25 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052003000 | Loss Inventory Variance (SF & Finish Goods) | P |  |  | X | ERG. |  |  |  |  | 000 | YB25 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052011000 | Loss Inventory Transfer (Raw & Trade) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052013000 | Loss Inventory Transfer (SF & Finish Goods) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052021000 | Loss Consumption for Quality Control (Raw & Trade) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052023000 | Loss Consumption for Quality Control (SF&Fin Gds) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052030000 | Loss from Revaluation | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052031000 | Loss from Valuation of External Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052033000 | Loss from Valuation of own Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052041000 | Loss Price Variance (PRD) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052041500 | Loss Inventory Value Adjustment Ext. Prod. (BSK) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052042000 | Loss Price Differences (PRL) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052043000 | Loss Price Differences (PRY) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052044000 | Loss Price Differences - Material Ledger (LKW) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052045000 | Loss Price Differences own Products (PRK) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052046000 | Differences (AVR Price) (PRC) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052051000 | Loss Consumption of Consign. Mat (Raw & Trade) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052053000 | Loss Consumption of Consign. Mat (SF & F.Goods) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052060000 | Loss Small Price Differences Invoice Receipt (MM) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052070000 | Loss from Production Variances | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052070500 | Loss Inventory Value Adjustment Own Prod. (BSK) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052080000 | Loss from allowed Differences GL Account Clearing | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052501000 | Gain Inventory Variance (Raw & Trade) | P |  |  | X | ERG. |  |  |  |  | 000 | YB25 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052503000 | Gain Inventory Variance (SF & Finish Goods) | P |  |  | X | ERG. |  |  |  |  | 000 | YB25 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052511000 | Gain Inventory Transfer (Raw & Trade) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052513000 | Gain Inventory Transfer (SF & Finish Goods) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052521000 | Gain Consumption for Quality Control (Raw & Trade) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052523000 | Gain Consumption for QM (SF & Finish Goods) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052530000 | Gain from Revaluation | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052531000 | Gain from Valuation of External Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052532000 | Gain from Valuation own Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052541000 | Gain Price Variance (PRD) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052541100 | Activity Price Diff. writeoff from WIP (PRA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052541200 | Activity Price Diff. writeoff from WIP (PRM) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052541500 | Gain Inventory Value Adjustment Ext. Prod. (BSK) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052542000 | Gain Price Differences (PRL) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052543000 | Gain Price Differences (PRY) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052544000 | Gain Price Differences - Material Ledger (LKW) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052545000 | Posterior Real Rate Activity Allocation (AUI) | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052546000 | Consumption Valuation (COC) | N |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052551000 | Gain Consumption of Consign. Mat (Raw & Trade) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052552000 | Gain Consumption of Consign. Mat (SF & F.Goods) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052560000 | Gain Small Price Difference Invoices Receipt (MM) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052570000 | Gain from Production Variances | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052570500 | Gain Inventory Value Adjustment Own Prod. (BSK) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0052580000 | Gain from allowed Differences GL Account Clearing | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0052590000 | Freight Revenue - Recovery | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB14 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0054011000 | Inventory Change - Purch.Offset.Acct (Raw) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054011100 | Inventory Change - Purch.offset.acct (Packaging) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054011200 | Inventory Change - Purch.offset.acct (Trading) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054013000 | Inventory Change - Purch.Offset.Acct (SF & F.Good) | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054040000 | Inventory Change - Reserve | N |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054051000 | Inventory Change - Scrap External Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB18 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054053000 | Inventory Change - Scrap own Products | P |  |  | X | ERG. |  |  |  |  | 000 | YB18 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054070000 | Inventory Change - Receipt without PO | N |  |  | X | ERG. |  | YB20 |  |  | 000 | YB03 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0054083000 | Inventory Change - Cost of own Goods sold w/C.Elem | P |  |  | X | ERG. |  | YB18 |  |  | 000 | YB30 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054084000 | Inventory Change Cost own Goods sold SO cons. w/CE | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054093000 | Inventory Change - QM cons.own prod. w/ cst elem. | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054200000 | Inventory Change - Work in Progress | N |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054200100 | Inventory Change - Work in Progress Event Based | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054300000 | Inventory Change - Semi Finished goods | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054400000 | Inventory Change - Finished Goods | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054441000 | Adjustment to Reserves for Unrealized Costs | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054442000 | Man Adj of Reserves for Imminent Loss | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0054444000 | Man Adj of Reserves for Unrealized Costs | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB30 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0055100000 | Adjustment Plant Activity Production Order | P |  |  | X | ERG. |  |  |  |  | 000 | YB36 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0055110000 | Secondary Cost external Settlement | P |  |  | X | ERG. |  |  |  |  | 000 | YB36 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0059801000 | Adjustment Reserves for Anticipated Losses | P |  |  | X | ERG. |  | YB15 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0059900000 | Cost of Goods Sold (Affiliated) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YBIC |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061002000 | 3rd party material | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061003000 | Travel Expenses - Hotel and Accommodation | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061004000 | Travel Expenses - Meals | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061005000 | Travel Expenses - Ground Transportation | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061006000 | Travel Expenses - Entertainment | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061007000 | Travel Expenses - Airfare, Rail, Mileage | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061008000 | Travel Expenses - Miscellaneous | P |  |  | X | ERG. |  |  |  |  | 000 | YB69 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061010000 | Payroll - Other Personnel Expenses | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061020000 | Payroll - Bonus | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061021000 | Payroll - Overtime Salaries | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061021100 | Payroll - Overtime Wages | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061022000 | Payroll - Vacation Pay Salaries | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061022100 | Payroll - Vacation Pay Wages | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061051000 | Payroll Expense - Downtime Wages | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061052000 | Payroll Expense - Downtime Salaries | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061060000 | Payroll Expense - Pension Contributions | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061061000 | Payroll - Benefits | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061062000 | Workers' Compensation Association Contributions | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061063000 | Dues to Associations | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061100000 | Payroll Expense - Salaries | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061101000 | Payroll Expense - Other salary-related expenses | P |  |  | X | ERG. |  |  |  |  | 000 | YB49 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061102000 | Payroll Expense - Other wage-related expenses | P |  |  | X | ERG. |  |  |  |  | 000 | YB49 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061103000 | Payroll Expense - Direct Labor Cost | P |  |  | X | ERG. |  |  |  |  | 000 | YB49 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061104000 | Payroll Expense - Indirect Labor Cost | P |  |  | X | ERG. |  |  |  |  | 000 | YB49 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061200000 | Payroll Expense - Tax and Soc Security - Wages | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061201000 | Payroll Expense - Tax and Soc Security - Salaries | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061301000 | Wages and Salaries Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061302000 | Employer Payroll Exp. : Tax, Insurance, Pension | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061400000 | Training and Education | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061401000 | HR Recruitement | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0061500000 | Sales Commissions | P |  |  | X | ERG. |  | YB30 |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0061500100 | Internal Commissions | P |  |  | X | ERG. |  | YB30 |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0061500200 | Royalties for Sales | P |  |  | X | ERG. |  | YB30 |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0062000000 | Bad Debt Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0062001000 | Bad Debt Expense-Individual Value Adjustment(FICA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0062001100 | Bad Debt Expense Reset – Individual Val Adj.(FICA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0062002000 | Bad Debt Expense-Flat Rate Value Adjustment(FICA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0062002100 | Bad Debt Expense Reset – Flat Rate Val Adj.(FICA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0062003000 | Bad Debt Expense (Write-off for FI-CA) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0062010000 | Individual Value Adjustments | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0062020000 | Flat-rate Value Adjustments | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063000000 | Machine and Equipment Periodic Service | P |  |  | X | ERG. |  |  |  |  | 000 | YB23 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063000500 | Qualtiy Control Consumption Ext. Prod. w/ Act Type | P |  |  | X | ERG. |  |  |  |  | 000 | YB18 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063001000 | Electricity and other Utilities | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063002000 | Water | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063003000 | Other Periodic Service | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063004000 | Insurance | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063005000 | Office/Building Rent | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063006000 | Telephone and other Communication | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063007000 | Fax and Internet | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063008000 | Building Periodic Service | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009000 | Leasing Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009100 | Lease Expense Building (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009200 | Lease Expense Land (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009300 | Lease expense Machinery (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009400 | Lease expense Motor Vehicle (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009500 | Lease expense Office Equipment (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009600 | Lease Expense Furniture (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063009700 | Lease Expense Computer Hardware (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010100 | Service Expense Land (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010200 | Service Expense Building (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010300 | Service expense Machinery (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010400 | Operating expense Motor Vehicle (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010500 | Service expense Office Equipment (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010600 | Service Expense Furniture (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063010700 | Service Expense Computer Hardware (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063020100 | Exp./Rev. from Valuation Diff. Building (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020200 | Exp./Rev. from Valuation Diff. Land (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020300 | Exp./Rev. from Valuation Diff. Machinery (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020400 | Exp./Rev. from Valuation Diff. Motor Vehicle (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020500 | Exp./Rev. Valuation Diff. Office Equipment (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020600 | Exp./Rev. from Valuation Diff. Furniture (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063020700 | Exp./Rev. Valuation Diff. Computer Hardware (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0063031000 | Apportionable Real Estate Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063031100 | Apportionable Real Estate Expense w/o Allocation | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063031200 | Apportionable Real Estate Expense (RE Object) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0063031300 | Apportionable Real Estate Expense w/Contract | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064000100 | Depreciation Expense - Land (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064001000 | Depreciation Expense - Buildings | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064001100 | Depreciation Expense - Buildings (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064002000 | Depreciation Expense - Machinery & Equipment | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064002100 | Depreciation Expense - Machinery & Equipment (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064003000 | Depreciation Expense - Building Improvement | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064004000 | Depreciation Expense - Motor Vehicles | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064004100 | Depreciation Expense - Motor Vehicles (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064005000 | Depreciation Expense - Office Equipment | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064005100 | Depreciation Expense - Office Equipment (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064006000 | Depreciation Expense - Furniture | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064006100 | Depreciation Expense - Furniture (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064007000 | Depreciation Expense - Computer Hardware | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064007100 | Depreciation Expense - Computer Hardware (ROU) | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0064008000 | Depreciation Expense - Computer Software | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064009100 | ARO Depreciation Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064010000 | Service Contract Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064020000 | Depreciation Expense - Low Value Assets | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064021000 | Amortization Expense - Intangible Assets | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064030000 | Unplanned Depreciation Expense | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064040000 | Scheduled Deprec Fixed Assets below Asset Value | P |  |  | X | ERG. |  |  |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064043000 | Amortization Expense - Goodwill | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  | X |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064050000 | Estimated Depreciation (CO) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0064060000 | Accrued interest (CO) | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065000000 | Postage and Shipping | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065000500 | Non Production - Material Consumption | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065001000 | Purchased Services | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065002000 | Advertising and Sales Costs | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065003000 | Vehicle Costs | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065004000 | Donations | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065008000 | Purchased Services-Time | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065008300 | Services - General | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065008400 | Purchased Services - Accommodation | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065008410 | Purchased Services - Airfair | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065008420 | Purchased Services - Ground Transportation | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065008430 | Purchased Services - Travel Miscellaneous | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065008500 | Subcontracting Services | N |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065008600 | Warranty Claims Processing | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065009000 | Other Activity Costs | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065050000 | Unplanned Delivery costs | P |  |  | X | ERG. |  |  |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065100000 | Office Supplies | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065150000 | Computer Supplies | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065200000 | Other Supplies | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065300000 | Legal and Audit Services | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065301000 | Marketing Expenses | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0065400000 | Freight | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0065900000 | Loss in the Event of Damage | P |  |  | X | ERG. |  |  |  |  | 000 | YB33 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0066000000 | Other Operating Expenses | P |  |  | X | ERG. |  |  |  |  | 000 | YB64 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0066000500 | Income - reduction in provisions | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB29 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0066000600 | Other Gains | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB64 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0066010000 | Expense of Discounting (ZKB) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB64 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0066019900 | Addition to Provisions (ZKK) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB64 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0066888800 | ICO Expense Travel | N |  |  | X | ERG. |  |  |  |  | 000 | YBXX |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0066999900 | ICO Expense Consultance | N |  |  | X | ERG. |  |  |  |  | 000 | YBXX |  |  |  |  | - |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0068888800 | ICO Clearing Account - Travel | N |  |  | X | ERG. |  |  |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070010000 | Revenue from Post Capitalization | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070015000 | Settlement of Asset u. Construction to CO Object | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070020000 | Revenue from Fixed Asset Sale | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB52 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070020100 | ARO Other Revenue | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB52 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070020200 | ARO Dissolution of provision | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB52 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070030000 | Clearing Account Asset Disposals | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB08 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070040000 | Discount Received | P |  |  | X | ERG. |  | YB81 |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070050000 | Clearing affiliated asset transfer | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB08 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070060000 | Other Income (FI-CA) | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YBXX |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070100000 | Interest Income | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070200000 | Interest Income, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070200100 | Interest Income, Affiliated, No Consolidation(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070200200 | Interest Income, Affiliated, Consolidation(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070200300 | ABS/MBS Interest Revenue (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201000 | Bonds Interest Income, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201100 | Bonds Interest Income, Affili., No Consolid.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201200 | Bonds Interest Income, Affili., Consolidat.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201300 | Dividend Income on Equity Securities(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201400 | Div. Income, Non-Affl. Company Inv. (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201500 | Dividend Income, Ass. or Joint Venture (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070201600 | Dividend Income, Subsidiary (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070210000 | Realized Price Gains, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070210100 | Realized Price Gains, Affiliated, No Consoli.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070210200 | Realized Price Gains, Affiliated, Consolidat.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070220000 | Gain from Price Valuation, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070220100 | Gain from Price Valuation, Affilia., No Cons.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070220200 | Gain from Price Valuation, Affilia., Consol.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070220300 | Gain from Equity Method Investment (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070230000 | Other Income (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070240000 | Non-operating Income from Equity Method Inv. (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070300000 | Interest Income - Subsidiaries | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070300100 | Gain from Long Term Investment | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070500000 | Consumption of Provisions | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070500100 | ARO Consumption of Provision | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700000 | Lease Income for - Non-Residential Real Estate | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700100 | Leasing Income - Residential Real Estate | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700200 | Leasing Income - Other | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700300 | Leasing Income - Interest (ROU) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700400 | Leasing Income - Sublease (ROU) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700500 | Revenue from Real Estate Expense Settlement | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070700600 | Gain from Real Estate Expense Settlement | P |  |  | X | ERG. |  |  |  |  | 000 | YB04 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070800000 | Other Extraordinary Income | P |  |  | X | ERG. |  | YB87 |  |  | 000 | YB04 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0070800100 | Service Income - Real Estate | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB04 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070800200 | Service Income - other | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070800300 | Charge Income (IHB) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0070900000 | Fines and Penalties | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071000000 | Bank Charges | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB04 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071000100 | Commission/Charge (TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071000200 | Other Expenses (TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071010000 | Loss from Asset Transactions | N |  |  | X | ERG. |  | YB75 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071010100 | Gain from Asset Transactions | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071010200 | Gain from Write Up of Fixed Assets | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071010300 | Loss from Asset Transactions (ROU) | N |  |  | X | ERG. |  | YB75 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071010700 | Estimated depreciation (FI-AA) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071011000 | ARO Other Expense | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071015000 | Offsetting Account Revaluation ord. Depreciation | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB07 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071040000 | Discount lost using Net Procedure | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071050000 | Cash Discounts Expense | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071055000 | Statistical Condition cash discount | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100000 | Interest Expense | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071100010 | Financing Expense (ARF Funder) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071100100 | Interest expense Building (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 008 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100200 | Interest expense Land (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100300 | Interest expense Machinery (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100400 | Interest expense Motor Vehicle (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100500 | Interest expense Office Equipment (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100600 | Interest Expense Furniture (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071100700 | Interest Computer Hardware (ROU) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB04 |  |  |  |  | * |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0071101000 | ARO Interest Expense | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071300000 | Interest Expense - Subsidiaries | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071400000 | Interest Expense, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071400100 | Interest Expense, Affiliated, No Consolidat.(TRM) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071400200 | Interest Expense, Affiliated, Consolidation(TRM) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071400300 | Bond Interest Expense(TRM) | P |  |  | X | ERG. |  | YB85 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071500000 | Gain/loss from Hedge Ineffectiveness(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071600000 | Realized Price Losses, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071600100 | Realized Price Losses, Affili., No Consolid.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071600200 | Realized Price Losses, Affiliated, Consolid.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071602000 | Impairment Loss from Equity Investment (TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071700000 | Loss from Price Valuation, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071700100 | Loss from Price Valuation, Affilia., No Cons.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071700200 | Loss from Price Valuation, Affilia., Consoli.(TRM) | P |  |  | X | ERG. |  | YB77 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0071800000 | Other Extraordinary Expenses | P |  |  | X | ERG. |  | YB89 |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072010000 | Loss from Exchange Rate Differences | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072020000 | Loss from Rounding Dif. Foreign Currency | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  | - |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072040000 | Loss from Currency Valuation | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072050000 | Realized FX Rate Losses, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072050100 | Realized FX Rate Losses, Affili., No Consol.(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072050200 | Realized FX Rate Losses, Affiliat., Consolid.(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072060000 | Loss from FX Valuation, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072060100 | Loss from FX Valuation, Affiliat., No Consol.(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072060200 | Loss from FX Valuation, Affiliat., Consolid.(TRM) | P |  |  | X | ERG. |  | YB75 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072510000 | Gain from exchange rate differences | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072520000 | Gain from rounding dif. foreign currency | P |  |  | X | ERG. |  | YB20 |  |  | 000 | YB01 |  |  |  |  | + |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072530000 | Gain from rebates differences | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072531000 | Gain from Supplier Rebate (MM) | P |  |  | X | MAT. |  | YB70 |  |  | 000 | YB14 |  |  |  |  | - |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072532000 | Gain from Supplier Rebate (SD) | P |  |  | X | MAT. |  | YB70 |  |  | 000 | YB14 |  |  |  |  | + |  | AED |  |  |  |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0072540000 | Gain from currency valuation | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072550000 | Realized FX Rate Gains, Unaffiliated(TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072550100 | Realized FX Rate Gains, Affiliat., No Consol.(TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072550200 | Realized FX Rate Gains, Affiliat., Consolid.(TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072560000 | Gain from FX Valuation, Unaffiliated (TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072560100 | Gain from FX Valuation, Affiliat., No Consol.(TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0072560200 | Gain from FX Valuation, Affiliated, Consolid.(TRM) | P |  |  | X | ERG. |  | YB70 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 037 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075001000 | Excise Taxes | P |  |  | X | ERG. |  | YB98 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075002000 | Corporate Income Tax Expense | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075002100 | Capital Gains Tax | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075002200 | Solidary Surcharge on Corporate Income Tax | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075002300 | Solidary surcharge for Interest Income Tax | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075003000 | Deferred Tax | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075004000 | Other Taxes on Income | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075005000 | Input Tax non deductable (NAV) | P |  |  | X | ERG. |  | YB98 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075007000 | Property Taxes | P |  |  | X | ERG. |  | YB98 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075008000 | Trade Tax | P |  |  | X | ERG. |  | YB98 |  |  | 000 | YB01 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 001 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075009000 | Export Duty | P |  |  | X | ERG. |  | YB98 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0075009900 | Other Company Taxes | P |  |  | X | ERG. |  | YB90 |  |  | 000 | YB04 |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0090001000 | Activated Carried Forward Losses | N |  |  | X | ERG. |  | YB90 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0090002000 | Deferred Carried Forward Losses | N |  |  | X | ERG. |  | YB90 |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092101500 | Settl. Rework | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092101800 | Settlement R | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092105100 | Personnel costs | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092105200 | Spare/Service/Ext Material con | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092105300 | Other costs | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0092105400 | Secondary costs | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094111000 | Overhead Material | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094112000 | Overhead production | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094113000 | Overhead administration | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094114000 | Overhead sales | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094201000 | Buildings & Periodic Service | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094202000 | Assessment Quality costs | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094222000 | COPA-Marketing | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094224000 | COPA -Admin. Overhead | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094225000 | COPA -Sales. Overhead | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094226000 | COPA-Non-Operating Expense | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094227000 | COPA-Non-Operating Income | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094228000 | COPA -Taxes | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094229000 | COPA -cash Discount | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094301000 | Machine hours 1 | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094302000 | Machine hours 2 | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094303000 | Setup Production | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094304000 | Water | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094305000 | Industry Effluent | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094306000 | Environmental | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094307000 | Internal Transport | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094308000 | Consulting | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094308100 | Service Time | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094308500 | Activity Unit based Billing | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094309000 | Development | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094310000 | QM Control | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0094311000 | Personnel hours | S |  |  | X | SECC |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0097777500 | Internal Occupancy Cost Clearing Acc. Real Estate | P |  |  | X | ERG. |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  | X |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0097777600 | ICO - Group Valuation Clearing Account | N |  |  | X | ERG. |  | YB70 |  |  | 000 | YB08 |  |  |  |  | + |  | AED |  |  | X |  | 00 | 001 |  |  |  |  | X |  |  |  |  |  |
| YCOA | 3310 | 0097777700 | ICO Margin | P |  |  | X | ERG. |  |  |  |  | 000 | SECC |  |  |  |  |  |  | AED |  |  |  |  | 00 |  |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0098888800 | ICO Clearing Account - Margin | N |  |  | X | ERG. |  |  |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |
| YCOA | 3310 | 0099999900 | ICO Clearing Account - Consultancy | N |  |  | X | ERG. |  |  |  |  | 000 | YBXX |  |  |  |  |  |  | AED |  |  |  |  | 00 | 008 |  |  |  |  |  |  |  |  |  |  |

### Sheet: C001

| SD account determination (Cust.Grp/MaterialGrp/AcctKey) |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Application | Condition type | Chart of Accts (TDC) | Sales Org. (TDC) | AcctAssgGr | Acct asgnmt grp | Account key | G/L Account (TDC) | Provision acc. |
| I_KAPPL | I_KSCHL | I_KTOPL | I_VKORG | I_KTGRD | I_KTGRM | I_KVSL1 | I_SAKN1 | I_SAKN2 |
| V | KOFI | YCOA | 3310 | 01 | 01 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 01 | 01 | ERS | 0044002000 |  |
| V | KOFI | YCOA | 3310 | 01 | 02 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 01 | 02 | ERS | 0044002000 |  |
| V | KOFI | YCOA | 3310 | 01 | 03 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 01 | 03 | ERS | 0044002000 |  |
| V | KOFI | YCOA | 3310 | 01 | X1 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X1 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X2 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X2 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X3 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X3 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X4 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X4 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X5 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X5 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X6 | ERL | 0041007100 |  |
| V | KOFI | YCOA | 3310 | 01 | X7 | ERL | 0041007200 |  |
| V | KOFI | YCOA | 3310 | 01 | X8 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X8 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X9 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | X9 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XA | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XA | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XB | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XB | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XC | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | XC | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 01 | Y1 | ERL | 0041910000 |  |
| V | KOFI | YCOA | 3310 | 01 | Y1 | ERS | 0044910000 |  |
| V | KOFI | YCOA | 3310 | 02 | 01 | ERL | 0041001000 |  |
| V | KOFI | YCOA | 3310 | 02 | 01 | ERS | 0044002100 |  |
| V | KOFI | YCOA | 3310 | 02 | 02 | ERL | 0041001000 |  |
| V | KOFI | YCOA | 3310 | 02 | 02 | ERS | 0044002100 |  |
| V | KOFI | YCOA | 3310 | 02 | 03 | ERL | 0041001000 |  |
| V | KOFI | YCOA | 3310 | 02 | 03 | ERS | 0044002100 |  |
| V | KOFI | YCOA | 3310 | 02 | X1 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X1 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X2 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X2 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X3 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X3 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X4 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X4 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X5 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X5 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X6 | ERL | 0041007100 |  |
| V | KOFI | YCOA | 3310 | 02 | X7 | ERL | 0041007200 |  |
| V | KOFI | YCOA | 3310 | 02 | X8 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X8 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X9 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | X9 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XA | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XA | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XB | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XB | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XC | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | XC | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 02 | Y1 | ERL | 0041940000 |  |
| V | KOFI | YCOA | 3310 | 02 | Y1 | ERS | 0044940000 |  |
| V | KOFI | YCOA | 3310 | 03 | 01 | ERL | 0041001500 |  |
| V | KOFI | YCOA | 3310 | 03 | 02 | ERL | 0041001500 |  |
| V | KOFI | YCOA | 3310 | 03 | 03 | ERL | 0041001500 |  |
| V | KOFI | YCOA | 3310 | 03 | X1 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X1 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X2 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X2 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X3 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X3 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X4 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X4 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X5 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X5 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X6 | ERL | 0041007100 |  |
| V | KOFI | YCOA | 3310 | 03 | X7 | ERL | 0041007200 |  |
| V | KOFI | YCOA | 3310 | 03 | X8 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X8 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X9 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | X9 | ERS | 0044970000 |  |
| V | KOFI | YCOA | 3310 | 03 | Y1 | ERL | 0041970000 |  |
| V | KOFI | YCOA | 3310 | 03 | Y1 | ERS | 0044970000 |  |

### Sheet: C002

| SD account determination (Cust.Grp/Account Key) |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Application | Condition type | Chart of Accts (TDC) | Sales Org. (TDC) | AcctAssgGr | Account key | G/L Account (TDC) | Provision acc. |
| I_KAPPL | I_KSCHL | I_KTOPL | I_VKORG | I_KTGRD | I_KVSL1 | I_SAKN1 | I_SAKN2 |
| V | KOFI | YCOA | 3310 | 01 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 01 | ERS | 0044002000 | 0012550000 |
| V | KOFI | YCOA | 3310 | 01 | YB2 | 0044003000 |  |
| V | KOFI | YCOA | 3310 | 02 | ERL | 0041001000 |  |
| V | KOFI | YCOA | 3310 | 02 | ERS | 0044002100 | 0012550000 |
| V | KOFI | YCOA | 3310 | 02 | YB2 | 0044003100 |  |
| V | KOFI | YCOA | 3310 | 03 | ERL | 0041001500 |  |
| V | KOFI | YCOA | 3310 | 03 | ERS | 0044002200 | 0012550000 |
| V | KOFI | YCOA | 3310 | 03 | YB2 | 0044003200 |  |

### Sheet: C003

| SD account determination (Material Grp/Acct Key) |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Application | Condition type | Chart of Accts | Sales Org. | Acct asgnmt grp | Account key | G/L Account | Provision acc. |
| I_KAPPL | I_KSCHL | I_KTOPL | I_VKORG | I_KTGRM | I_KVSL1 | I_SAKN1 | I_SAKN2 |
| V | KOFI | YCOA | 3310 | 01 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 02 | ERL | 0041000000 |  |
| V | KOFI | YCOA | 3310 | 03 | ERL | 0041000000 |  |

### Sheet: C004

| SD account determination (General) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Application | Condition type | Chart of Accts | Sales Org. | G/L Account | Provision acc. |
| I_KAPPL | I_KSCHL | I_KTOPL | I_VKORG | I_SAKN1 | I_SAKN2 |
| V | KOFI | YCOA | 3310 | 0041000000 |  |
| VD | A001 | YCOA | 3310 | 0012530000 |  |

### Sheet: C005

| SD account determination (Account Key) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Application | Condition type | Chart of Accts | Sales Org. | Account key | G/L Account | Provision acc. |
| I_KAPPL | I_KSCHL | I_KTOPL | I_VKORG | I_KVSL1 | I_SAKN1 | I_SAKN2 |
| V | KOFI | YCOA | 3310 | 0S1 | 0044001000 | 0021770000 |
| V | KOFI | YCOA | 3310 | ERF | 0052590000 |  |
| V | KOFI | YCOA | 3310 | VST | 0012600000 |  |
| V | KOFI | YCOA | 3310 | YB1 | 0044004000 |  |
| V | KOFI | YCOA | 3310 | YB2 | 0044003000 |  |
| V | KOFI | YCOA | 3310 | YB3 | 0044006000 |  |
| V | KOFI | YCOA | 3310 | YB4 | 0044005000 |  |
| V | KOFI | YCOA | 3310 | YSC | 0071055000 | 0021775000 |

### Sheet: C016

| SD account determination (Company Code / Contract Process Variant / Account Key) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Company code | Application | Condition type | Chart of Accts | Account key | G/L Account | Accruals Account |
| I_BUKRS | I_KAPPL | I_KSCHL | I_KTOPL | I_KVSL1 | I_SAKN1 | I_SAKN2 |
| 3310 | V | KORC | YCOA | 0C1 | 0061500000 | 0021772000 |
| 3310 | V | KORC | YCOA | 0C3 | 0061500100 | 0021772100 |
| 3310 | V | KORC | YCOA | 0C4 | 0061500000 | 0021772000 |
| 3310 | V | KORE | YCOA | 0C2 | 0061500100 | 0021772100 |
| 3310 | V | KORP | YCOA | 0P1 | 0072532000 | 0021771000 |
| 3310 | V | KORP | YCOA | 0P2 | 0072531000 | 0021771000 |
| 3310 | V | KORR | YCOA | 0R1 | 0061500200 | 0021772000 |
| 3310 | V | KORR | YCOA | 0R2 | 0041001530 |  |
| 3310 | V | KORR | YCOA | 0R3 | 0066999930 |  |

### Sheet: TKA3A

| Automatic account assignment - default assignments |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Company Code | Cost Element | CO Area | Cost Center | Order | Account Assignment Detail | Profit Center | Indicator: Account assignment business area has priority | Prof. segment |
| I_BUKRS | I_KSTAR | I_KOKRS | I_KOSTL | I_AUFNR | I_REGEL | I_PRCTR | I_XGSBER | I_BSSUBST |
| 3310 | 0041090000 | A000 | 0033101602 |  |  |  |  |  |
| 3310 | 0044000000 | A000 |  |  |  |  |  |  |
| 3310 | 0044001000 | A000 |  |  |  |  |  |  |
| 3310 | 0044008100 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0052001000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052003000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052011000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052013000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052021000 | A000 |  |  |  |  |  |  |
| 3310 | 0052023000 | A000 |  |  |  |  |  |  |
| 3310 | 0052030000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052031000 | A000 |  |  |  |  |  |  |
| 3310 | 0052033000 | A000 |  |  |  |  |  |  |
| 3310 | 0052041000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052042000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052043000 | A000 |  |  |  |  |  | X |
| 3310 | 0052044000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052045000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052046000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052051000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052053000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052060000 | A000 |  |  |  |  |  |  |
| 3310 | 0052080000 | A000 |  |  |  |  |  |  |
| 3310 | 0052501000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052503000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052511000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052513000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052530000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052531000 | A000 |  |  |  |  |  |  |
| 3310 | 0052532000 | A000 |  |  |  |  |  |  |
| 3310 | 0052541000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052542000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052543000 | A000 |  |  |  |  |  | X |
| 3310 | 0052544000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052551000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052552000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0052560000 | A000 |  |  |  |  |  |  |
| 3310 | 0052580000 | A000 |  |  |  |  |  |  |
| 3310 | 0054051000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0054053000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0062000000 | A000 |  |  |  |  |  |  |
| 3310 | 0062001000 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0062001100 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0062002000 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0062002100 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0062003000 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0065009000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0065400000 | A000 |  |  | 1 |  |  |  |
| 3310 | 0066000000 | A000 |  |  |  |  |  |  |
| 3310 | 0070040000 | A000 |  |  |  |  |  |  |
| 3310 | 0070100000 | A000 |  |  |  |  |  |  |
| 3310 | 0070200000 | A000 |  |  |  |  |  |  |
| 3310 | 0070200100 | A000 |  |  |  |  |  |  |
| 3310 | 0070200200 | A000 |  |  |  |  |  |  |
| 3310 | 0070200300 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0070201000 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0070201100 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0070201200 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0070201300 | A000 |  |  |  |  |  |  |
| 3310 | 0070201400 | A000 |  |  |  |  |  |  |
| 3310 | 0070201500 | A000 |  |  |  |  |  |  |
| 3310 | 0070201600 | A000 |  |  |  |  |  |  |
| 3310 | 0070210000 | A000 |  |  |  |  |  |  |
| 3310 | 0070210100 | A000 |  |  |  |  |  |  |
| 3310 | 0070210200 | A000 |  |  |  |  |  |  |
| 3310 | 0070220000 | A000 |  |  |  |  |  |  |
| 3310 | 0070220100 | A000 |  |  |  |  |  |  |
| 3310 | 0070220200 | A000 |  |  |  |  |  |  |
| 3310 | 0070220300 | A000 |  |  |  |  |  |  |
| 3310 | 0070230000 | A000 |  |  |  |  |  |  |
| 3310 | 0070240000 | A000 |  |  |  |  |  |  |
| 3310 | 0071000000 | A000 |  |  |  |  |  |  |
| 3310 | 0071000100 | A000 |  |  |  |  |  |  |
| 3310 | 0071000200 | A000 |  |  |  |  |  |  |
| 3310 | 0071050000 | A000 |  |  |  |  |  |  |
| 3310 | 0071100000 | A000 |  |  |  |  |  |  |
| 3310 | 0071100010 | A000 | 0010101101 |  |  |  |  |  |
| 3310 | 0071400000 | A000 |  |  |  |  |  |  |
| 3310 | 0071400100 | A000 |  |  |  |  |  |  |
| 3310 | 0071400200 | A000 |  |  |  |  |  |  |
| 3310 | 0071400300 | A000 | 0033101101 |  |  |  |  |  |
| 3310 | 0071500000 | A000 |  |  |  |  |  |  |
| 3310 | 0071600000 | A000 |  |  |  |  |  |  |
| 3310 | 0071600100 | A000 |  |  |  |  |  |  |
| 3310 | 0071600200 | A000 |  |  |  |  |  |  |
| 3310 | 0071602000 | A000 |  |  |  |  |  |  |
| 3310 | 0071700000 | A000 |  |  |  |  |  |  |
| 3310 | 0071700100 | A000 |  |  |  |  |  |  |
| 3310 | 0071700200 | A000 |  |  |  |  |  |  |
| 3310 | 0072010000 | A000 |  |  |  |  |  |  |
| 3310 | 0072020000 | A000 |  |  |  |  |  |  |
| 3310 | 0072040000 | A000 |  |  |  |  |  |  |
| 3310 | 0072050000 | A000 |  |  |  |  |  |  |
| 3310 | 0072050100 | A000 |  |  |  |  |  |  |
| 3310 | 0072050200 | A000 |  |  |  |  |  |  |
| 3310 | 0072060000 | A000 |  |  |  |  |  |  |
| 3310 | 0072060100 | A000 |  |  |  |  |  |  |
| 3310 | 0072060200 | A000 |  |  |  |  |  |  |
| 3310 | 0072510000 | A000 |  |  |  |  |  |  |
| 3310 | 0072520000 | A000 |  |  |  |  |  |  |
| 3310 | 0072540000 | A000 |  |  |  |  |  |  |
| 3310 | 0072550000 | A000 |  |  |  |  |  |  |
| 3310 | 0072550100 | A000 |  |  |  |  |  |  |
| 3310 | 0072550200 | A000 |  |  |  |  |  |  |
| 3310 | 0072560000 | A000 |  |  |  |  |  |  |
| 3310 | 0072560100 | A000 |  |  |  |  |  |  |
| 3310 | 0072560200 | A000 |  |  |  |  |  |  |

### Sheet: T030K

| Tax codes and account determination |  |  |  |
| --- | --- | --- | --- |
| Tax Codes | Description | Transaction Key | G/L Account D/C |
| I_MWSKZ | I_TEXT1_EN | I_KTOSL | I_KONTH |
| S0 | AE Output VAT exempted | MWS | 0022000000 |
| S1 | AE Output VAT 0% - goods | MWS | 0022000000 |
| S2 | AE Output VAT 5% - goods | MWS | 0022000000 |
| S3 | AE Output VAT 0% - services | MWS | 0022000000 |
| S4 | AE Output VAT 5% - services | MWS | 0022000000 |
| S5 | AE Output VAT 0% for GCC export goods supplies | MWS | 0022000000 |
| S6 | AE Output VAT 0% for GCC export service supplies | MWS | 0022000000 |
| S7 | AE Output VAT 0% for non-GCC export goods supplies | MWS | 0022000000 |
| S8 | AE Output VAT 0% for non-GCC export srv supplies | MWS | 0022000000 |
| S9 | AE Output VAT 0% for deemed supplies | MWS | 0022000000 |
| SA | AE Output VAT 5% for transport goods to GCC state | MWS | 0012600000 |
| V0 | AE Input VAT exempted | VST | 0012600000 |
| V1 | AE Input VAT 0% - goods | VST | 0012600000 |
| V2 | AE Input VAT 5% - goods | VST | 0012600000 |
| V3 | AE Input VAT 0% - services | VST | 0012600000 |
| V4 | AE Input VAT 5% - services | VST | 0012600000 |
| VA | AE import subject to reverse charge VAT 0% | ESE | 0012610000 |
| VA | AE import subject to reverse charge VAT 0% | ESA | 0022100000 |
| VB | AE local supplies subject to reverse charge VAT5% | ESE | 0012610000 |
| VB | AE local supplies subject to reverse charge VAT5% | ESA | 0022100000 |
| VX | AE VAT 5% for Reverse Charge imported goods | ESE | 0012610000 |
| VX | AE VAT 5% for Reverse Charge imported goods | ESA | 0022100000 |
| VY | AE VAT 5% for Reverse Charge imported service | ESE | 0012610000 |
| VY | AE VAT 5% for Reverse Charge imported service | ESA | 0022100000 |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]
- related-to :: [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602]]
- related-to :: [[03-financial-accounting-and-close/g-l-mds-bng-601]]
- related-to :: [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599]]
- see-also :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE.xlsx` — full document · extracted with `xlsx2md` · 171,414 chars in the whole document
