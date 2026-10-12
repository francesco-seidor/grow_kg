---
id: 03-financial-accounting-and-close/coa-overview-banking-180
title: COA Overview Banking (COA_Overview_Banking)
description: "SAP S/4HANA Cloud Public Edition 2608 banking chart of accounts (scope item 5NU, BCOA): G/L accounts with long text and DE (1010) / US (1710) availability flags."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/banking-and-insurance-charts-of-accounts]
aliases: [COA_Overview_Banking]
keywords: [Banking and Insurance Charts of Accounts, banking chart of accounts, g/l accounts, company code coverage, loans and advances, allowance for loan losses, deposits, interest income and expense, fee and commission income, derivatives and off-balance items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/COA_Overview_Banking.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-180
topic: 03-financial-accounting-and-close/banking-and-insurance-charts-of-accounts
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# COA Overview Banking (COA_Overview_Banking)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/COA_Overview_Banking.xlsx`, extracted with `xlsx2md`. Grouped under **Banking and Insurance Charts of Accounts** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## COA Overview Banking

### Sheet: 5NU - BCOA

| G/L Account Number (I_SAKNR) | G/L Acct Long Text (SKAT) | DE (1010) | US (1710) |
| --- | --- | --- | --- |
| 10110100 | Cash-Currency & Coin | X | X |
| 10110200 | Cash-Onsite ATM | X | X |
| 10110400 | Cash In Transit-Currency & Coin | X | X |
| 10110500 | Cash- Clearing Account | X | X |
| 10210100 | CIPC-Sec Collections & Settle | X | X |
| 10210200 | CIPC-Automated Clearghse Items | X | X |
| 10210300 | CIPC-Transit Checks | X | X |
| 10210400 | CIPC-Other | X | X |
| 10310100 | DF Central Bank Reserve | X | X |
| 10310200 | DF Credit at Central Bank | X | X |
| 10410100 | DF Coml Banks -Demand | X | X |
| 10410200 | DF Other Deps Institutes-Demand | X | X |
| 10410700 | Payment Clearing Banks-Demand | X | X |
| 10500100 | Due From CML Banks-Time | X | X |
| 10500200 | DF Other Deps Institutes-Time | X | X |
| 10500300 | Due From Central Banks-Time | X | X |
| 10610100 | O/N CB Fds Sold-Coml Bks | X | X |
| 10610300 | O/N CB Fds Sold-Other | X | X |
| 10610500 | Term CB Fds- Coml Bks | X | X |
| 10610700 | Term CB Fds-Oth local Deps Inst | X | X |
| 10610900 | Term CB Fds-Other | X | X |
| 10720100 | O/N Resell - Coml Bks | X | X |
| 10720400 | O/N Resell-Other | X | X |
| 10720500 | Term Resell- Coml Bks | X | X |
| 10720800 | Term Resell-Other | X | X |
| 10720900 | Term Resell Bonds-Dmstc Coml Bks | X | X |
| 10810100 | AC/HTM-Gvt Debt Sec | X | X |
| 10810200 | AC/HTM-Mortgage Backed Securities | X | X |
| 10810300 | AC/HTM- Sec Bks | X | X |
| 10810400 | AC/HTM-Other | X | X |
| 10810550 | AC/HTM Inv-Quoted Others | X | X |
| 10810570 | AC/HTM Inv-Unquoted Others | X | X |
| 10810600 | AC corporate bonds | X | X |
| 10810700 | FVOCI Private Placements | X |  |
| 10810800 | FVOCI/AFS-Gvt Debt Sec | X | X |
| 10810900 | FVOCI/AFS-MBS | X | X |
| 10810910 | AC Debt Priv Placements | X | X |
| 10810920 | FVOCI/AFS-Debt Securities | X | X |
| 10810930 | FVOCI/AFS-Inv-Quoted Others | X | X |
| 10810940 | FVOCI AFS-Inv-Unquoted Others | X | X |
| 10910100 | FVTPL Eq Sec-Invests - Gvts | X | X |
| 10910200 | FVTPL Eq Sec-Inv In Corps | X | X |
| 10910300 | FVTPL Eq Sec-Other | X | X |
| 10910500 | FVOCI/AFS Eq Invest SecWritedown | X | X |
| 10910600 | FVOCI Equity Secs.-Inv. Gov. | X |  |
| 10910700 | FVOCI Equity Secs.-Inv. | X |  |
| 10910800 | FVOCI Equity Secs. Other | X |  |
| 11010100 | Trdg-Gvt Sec | X | X |
| 11010200 | Trdg-MBS | X | X |
| 11010400 | Trdg-Debt-Bks | X | X |
| 11010600 | Trdg CD'S- Bks | X | X |
| 11010800 | Trdg Bks Accpts | X | X |
| 11010900 | Trdg Commercial Paper | X | X |
| 11010910 | Trdg Assets Other | X | X |
| 11010950 | Inv-Trading-Quoted Others | X | X |
| 11010960 | Inv-Trading-Unquoted Others | X | X |
| 13010100 | AC Lns-Coml-Scd By RE-Cnstr&Land | X | X |
| 13010150 | FVOCI Lns-Coml-Scd By RE-Cnstr&Land | X |  |
| 13010200 | AC Lns-Coml-Scd By RE-Farmland | X | X |
| 13010250 | FVOCI Lns-Coml-Scd By RE-Farmland | X |  |
| 13011200 | AC Lns-Deps Inst- Bks | X | X |
| 13011250 | FVOCI Lns-Deps Inst- Bks | X |  |
| 13011400 | AC Acceptances Purchased- Bks | X | X |
| 13011450 | FVOCI Acceptances Purchased-Bks | X |  |
| 13012100 | AC Coml & Indl Lns- Corp | X | X |
| 13012150 | FVOCI Coml & Indl Lns- Corp | X |  |
| 13012600 | AC Overdrafts-Commercial | X | X |
| 13012650 | FVOCI Overdrafts-Commercial | X |  |
| 13013900 | AC Lns- Govts | X | X |
| 13013950 | FVOCI Lns- Govts | X |  |
| 13014100 | AC Other Coml Loans | X | X |
| 13014150 | FVOCI Other Coml Loans | X |  |
| 13014600 | AC Cash Basis Loan | X | X |
| 13014650 | FVOCI Cash Basis Loan | X |  |
| 13110100 | AC Credit Card | X | X |
| 13110150 | FVOCI Credit Card | X |  |
| 13110200 | AC Credit Card-Def Fee | X | X |
| 13110250 | FVOCI Credit Card-Def Fee | X |  |
| 13110300 | AC Credit Card-Def Costs | X | X |
| 13110350 | FVOCI Credit Card-Def Costs | X |  |
| 13110400 | AC Credit Card Securitized Loans | X | X |
| 13110450 | FVOCI Credit Card Securitized Loans | X |  |
| 13210100 | AC Lns - Installment Credit | X | X |
| 13210150 | FVOCI Lns - Installment Credit | X |  |
| 13210400 | AC Lns-Individual-Overdraft | X | X |
| 13210450 | FVOCI Lns-Individual-Overdraft | X |  |
| 13210500 | AC Lns - Automobile | X | X |
| 13210550 | FVOCI Lns - Automobile | X |  |
| 13210600 | AC Inst Loan Payment Clearing | X | X |
| 13210650 | FVOCI Inst Loan Payment Clearing | X |  |
| 13310100 | AC HML-Secd | X | X |
| 13310150 | FVOCI HML-Secd | X |  |
| 13310300 | AC Home Equity Lns | X | X |
| 13310350 | FVOCI Home Equity Lns | X |  |
| 13310400 | AC Home Mortgage Loans-Deferred Costs | X | X |
| 13310450 | FVOCI Home Mortgage Loans-Deferred Costs | X |  |
| 14001000 | Allowance for LL - Commercial, RE, Constr and Land | X | X |
| 14001100 | Allowance for LL - Commercial, RE and Farmland | X | X |
| 14001200 | Allowance for LL - Commercial Banks | X | X |
| 14001400 | Allowance for LL - Commercial and Industrial | X | X |
| 14001600 | Allowance for LL - Commercial and Governments | X | X |
| 14001700 | Allowance for LL - Other Commercial | X | X |
| 14001800 | Allowance for LL - Credit Card Loans | X | X |
| 14001900 | Allowance for LL - Securitized Loans | X | X |
| 14002100 | Allowance for LL - Consumer Installment Loans | X | X |
| 14002200 | Allowance for LL - Consumer Other | X | X |
| 14002300 | Allowance for LL - Car Loans | X | X |
| 14002600 | Allowance for LL - Loan Loss Valuation | X | X |
| 14002700 | Allowance for LL - Leases | X | X |
| 14002900 | Allowance for LL – Other | X | X |
| 14003000 | Allowance for Mortgage Loans | X | X |
| 14003100 | Allowance-Securitized-Provision |  | X |
| 14003200 | Allowance for LL - Participation Loans | X | X |
| 14003300 | Allowance for LL - Acquisition Loans | X | X |
| 14003400 | Allowance for Loans - Securitizations |  | X |
| 14003500 | Allowance for FVOCI Equity Investment Securities | X |  |
| 14003600 | Allowance for AC Debt Securities | X | X |
| 14003700 | Allowance for FVOCI Debt Securities | X |  |
| 14003800 | Allowance for AC Receivables to banks | X | X |
| 14200100 | Dir Fin Lse-Invst-Auto |  | X |
| 14200200 | Dir Fin Lse-Auto-Accum Depr |  | X |
| 14200300 | Dir Fin Lse-Investment |  | X |
| 14200400 | Dir Fin Lse-Accum Depr |  | X |
| 14200500 | Dir Fin Lse-Residual Value |  | X |
| 14200600 | Dir Fin Lse-Amort Tax |  | X |
| 14200700 | Dir Fin Lse-Sales Tax |  | X |
| 14200800 | Lev Lease Investment |  | X |
| 14200900 | Operating Lease-Investment | X | X |
| 14202100 | Operating Lease-Accum Depr Def | X | X |
| 14202200 | Operating Lease-Equip Reval | X | X |
| 14203000 | Finance Lease Receivable | X |  |
| 15001100 | Prem & Equip-Cost-Land | X | X |
| 15001200 | Prem & Equip-Cost-Building | X | X |
| 15001300 | Prem & Eq-Cst-DP Equipment | X | X |
| 15001400 | Prem & Eq-Cst-Oth-Furn & Fixt | X | X |
| 15001500 | Prem & Equip-Cost-Capitlzd Lse | X | X |
| 15001600 | Prem & Eq-Cst-Cnstr In Process | X | X |
| 15001700 | Prem & Eq-Cst-Purch In Process | X | X |
| 15001800 | Prem & Eq-Cost-Disp In Process | X | X |
| 15001900 | Prem & Eq-Cost-Trnsfrs In Proc | X | X |
| 15101200 | Accumulated Depr-Cost-Land | X | X |
| 15102300 | Accumulated Depr-Building | X | X |
| 15103400 | Accm Depr-Dp Equipment | X | X |
| 15104500 | Accm Depr-Oth Furn & Fixtures | X | X |
| 15109100 | Accum Depr-Captlzd Lease | X | X |
| 16010100 | Due From/Due To - Intercompany | X | X |
| 16010200 | Inv-Trading-Subsidiary | X | X |
| 16020100 | Intercompany Loans Receivable | X | X |
| 16030100 | Inv In Consol Subs-Cost | X | X |
| 16030200 | Inv Consol Subs-Equity | X | X |
| 16030300 | Inv Consol Subs-Dividends | X | X |
| 16040000 | AC/HTM Inv-Subsidiary | X | X |
| 16040100 | FVOCI/AFS Inv- Subsidiary | X | X |
| 16050100 | Inv Branches | X | X |
| 16050500 | Intercompany Accrued Interest Income -Loans | X | X |
| 16090100 | Intercompany Receivables -Other | X | X |
| 16210100 | OREO-Orig Cost-Cnstr,Lnd & Dev | X | X |
| 16220200 | OREO-Original Cost | X | X |
| 16230300 | OREO-Charge-Offs-Cnstr/Lnd Dev | X | X |
| 16240400 | OREO-Charge-Offs-other | X | X |
| 16260600 | OREO-Other | X | X |
| 16410100 | Intang Ast-Brand Name Prem | X | X |
| 16420200 | Intang Ast-Goodwill | X | X |
| 16430300 | Intang Ast-Other | X | X |
| 16510100 | Acc Inc Rec-Bank Balances | X | X |
| 16520200 | Acc Inc Rec-O/N CB Funds Sold | X | X |
| 16521300 | Acc Inc Rec-Term CB Funds Sold | X | X |
| 16530400 | Acc Inc Rec-O/N Resell | X | X |
| 16531500 | Acc Inc Rec-O/N Borrow Bonds | X | X |
| 16535600 | Acc Inc Rec-Term Resell | X | X |
| 16536700 | Acc Inc Rec-Term Borrow Bonds | X | X |
| 16540800 | AC/HTM Acc Inc Rec-Inv Sec | X | X |
| 16545900 | FVOCI/AFS Acc Inc Rec-Inv Sec | X | X |
| 16550910 | Acc Inc Rec-Trading Assets | X | X |
| 16560920 | Acc Inc Rec-Comml Loans | X | X |
| 16565930 | Acc Inc Rec-Credit Card | X | X |
| 16570940 | Acc Inc Rec-Other Consumer Lns | X | X |
| 16575950 | Acc Inc Rec-Home Mtge Loans | X | X |
| 16580960 | Acc Inc Rec-Leases | X | X |
| 16585970 | Acc Inc Rec-Other | X | X |
| 16610100 | Prepd Exp-Insurance | X | X |
| 16615200 | Prepd Exp-Rent | X | X |
| 16620300 | Prepd Exp-Legal | X | X |
| 16625400 | Prepd Exp-Salaries | X | X |
| 16630500 | Prepd Exp-Premiums/Promos | X | X |
| 16640600 | Prepd Exp-FDIC-Oth Regulatory | X | X |
| 16645700 | Prepd Exp-Pension | X | X |
| 16650100 | Prepd Exp-supplier | X | X |
| 16650101 | Prepd Exp-FA | X | X |
| 16650102 | Prepd Exp-Purchasing | X | X |
| 16650800 | Prepd Exp-Other | X | X |
| 17010100 | Accts Rec-Serv.Sales | X | X |
| 17020200 | Accts-Rec-Other | X | X |
| 17510100 | Msc A-Inventory | X | X |
| 17520200 | Msc A-Software | X | X |
| 17530300 | Misc Assets-Other | X | X |
| 17540000 | Deferred Tax Asset | X | X |
| 19020100 | Suspense Account | X | X |
| 19030300 | Interface Clearing | X | X |
| 20110100 | Personal - DDAs | X | X |
| 20120200 | Demand Deposits Corporations | X | X |
| 20130300 | Gov.-DDAs | X | X |
| 20140400 | Bks -DDAs | X | X |
| 20150500 | Other -DDAs | X | X |
| 20210100 | Regular Savings - Personal | X | X |
| 20220200 | Demand Deposits Customers | X | X |
| 20220300 | Regular Savings - Govt | X | X |
| 20230400 | Bks -Savings | X | X |
| 20280900 | Other Savings | X | X |
| 20310100 | Certificate of Deposits - Personal | X | X |
| 20320300 | Certificate of Deposits - Govt | X | X |
| 20330400 | Certificate of Deposits - Bks | X | X |
| 20360900 | Certificate of Deposits - Other | X | X |
| 20610100 | O/N CB Fds Pur Banks | X | X |
| 20620200 | O/N CB Fds Pur Oth | X | X |
| 20640400 | Term CB Fds Pur Banks | X | X |
| 20650500 | Term CB Fds Pur Other | X | X |
| 20710100 | O/N Bks-Repos | X | X |
| 20730300 | O/N Oth-Repos | X | X |
| 20740400 | Term Bks-Repos | X | X |
| 20760600 | Term Other-Repos | X | X |
| 20810100 | ST Borrow-Banks | X | X |
| 20820200 | ST Borrow-CB Reserve | X | X |
| 20860600 | ST Borrow-Com'L Paper | X | X |
| 20870700 | ST Borrow-Other | X | X |
| 20910100 | LT Debt-Convert Debentures | X | X |
| 20920200 | LT Debt- Notes | X | X |
| 20940400 | LT Debt - Other | X | X |
| 20950500 | Trust Preferred Capital Sec | X | X |
| 22010101 | Acc Int Pay-Savs Deps | X | X |
| 22011200 | Acc Int Pay-Time Deps | X | X |
| 22020400 | Acc Int Pay-O/N Fed Funds Purch | X | X |
| 22021500 | Acc Int Pay Term Fed Funds Purch | X | X |
| 22030100 | Acc Int Pay-O/N Repos | X | X |
| 22031200 | Acc Int Pay-Term Repos | X | X |
| 22040100 | Acc Int Pay-Funds Borrowed | X | X |
| 22050200 | Acc Int Pay- LT Debt | X | X |
| 22060300 | Acc Int Pay-Loan Sale | X | X |
| 22070500 | Acc Int Pay-Miscellaneous | X | X |
| 22510400 | Acc Exp Pay-Salaries | X | X |
| 22520300 | Acc Exp Pay-Pensions | X | X |
| 22522100 | Acc Exp Pay-Incnt Comp. | X | X |
| 22523010 | Acc Exp Pay- Social Security | X | X |
| 22523011 | Acc Exp Pay- Payroll Taxes | X | X |
| 22523012 | Payroll Net Accrual | X | X |
| 22523013 | Payroll-Savings Plans | X | X |
| 22523014 | Payroll-ER Benefit | X | X |
| 22524200 | Acc Exp Pay-Medical Insurance | X | X |
| 22524201 | Acc Exp Pay- Workers' Comp. | X | X |
| 22524202 | Other HR - Payables | X | X |
| 22524203 | Payroll Garnishments | X | X |
| 22530400 | Acc Exp Pay-Audit/Legal Fees | X | X |
| 22560700 | Acc Exp Pay-Other | X | X |
| 22560701 | Acc Exp Pay-Other Personnel Costs | X | X |
| 22560702 | Acc Exp Pay - T&E | X | X |
| 25010200 | Accts Pay-Vendors Accounts Payable | X | X |
| 25010201 | Accts Pay Dom.-Vendor Reconciliation | X | X |
| 25010202 | Accts Pay Fgn.-Vendor Reconciliation | X | X |
| 25030100 | Accts Pay-Intercompany | X | X |
| 25030101 | Accts Pay-Recon. Intercompany | X | X |
| 25030800 | Branch Income Tax | X | X |
| 25030900 | Branch Witholding Tax | X | X |
| 25030999 | Intercompany Clearing | X | X |
| 25050800 | Other Accts Payable | X | X |
| 25050900 | Other Misc. Payables | X | X |
| 25200000 | Trading Liabilities | X | X |
| 25500100 | Misc Liab-Bond Purchase | X | X |
| 25500200 | Misc Liab-Interest Rate Swaps | X | X |
| 25510300 | Misc Liab-Under Def Pymt LOC | X | X |
| 25530500 | Misc Liab-RE Premises Taxes | X | X |
| 25531300 | Misc Liab-Personal Prop Taxes | X | X |
| 25532400 | Misc Liab-Retailer Occup Taxes | X | X |
| 25533500 | Misc Liab-Franchise Taxes | X | X |
| 25534600 | Misc Liab-Sales & Use Taxes | X | X |
| 25535100 | Deferred Tax Liabilitiy | X | X |
| 25535700 | Misc Liab-Other Taxes | X | X |
| 25536800 | Misc Liab-Oth Tx-A/P Withhold | X | X |
| 25540100 | Misc Liab-Dividends Payable | X | X |
| 25550300 | Misc Liab-Insur-Clms Payable | X | X |
| 25560400 | Misc Liab-Other | X | X |
| 26010100 | Fed. Income Tax Liab. | X | X |
| 26020200 | State. Income Tax Liab. | X | X |
| 26030300 | Taxes-Deferred | X | X |
| 26040400 | FIT Liab-Deferred | X | X |
| 26050500 | SIT Liab - Deferred | X | X |
| 26060600 | City/County-Deferred | X | X |
| 26130900 | Withholding Tax (for banking) | X | X |
| 26140100 | Accrued Sales Taxes-State |  | X |
| 26140110 | Accrued Sales Taxes-County |  | X |
| 26140120 | Accrued Sales Taxes-City |  | X |
| 26140130 | Accrued Sales Taxes-Other | X | X |
| 26140200 | Accrued Use Taxes-State |  | X |
| 26140210 | Accrued Use Taxes-County |  | X |
| 26140220 | Accrued Use Taxes-City |  | X |
| 26140230 | Accrued Use Taxes-Other | X | X |
| 26140600 | Other Tax | X | X |
| 26200100 | DDA-Pay Intercompany | X | X |
| 26200200 | DDA In Process - Intercompany | X | X |
| 26200300 | Certificate of Deposits -Intercompany | X | X |
| 26200400 | Accrued Exp Pay-Intercompany | X | X |
| 26200500 | Intercompany Loans Payable | X | X |
| 26200600 | Acc Interco Int Pay-Loans | X | X |
| 26200900 | Intercompany -Other Liab. | X | X |
| 31010100 | Perpetual Pref Stock | X | X |
| 31020200 | Convertible Pref Stock | X | X |
| 32010300 | Common Stock-Beg Year | X | X |
| 32011400 | Common Stock-Issuances | X | X |
| 32012500 | Common Stock-Retirements | X | X |
| 33010100 | RE-Prior Year | X | X |
| 33010101 | Retained Earnings (for banking) | X | X |
| 33011300 | RE-Common Stk Dividends | X | X |
| 33012100 | RE-Perpetual Pref Stk Div | X | X |
| 33020200 | RE-Current Year | X | X |
| 34010100 | Treasury Stock-Beg Of Year | X | X |
| 34020200 | Treasury Stock - Acquisitions | X | X |
| 34030300 | Treasury Stock - Issuances | X | X |
| 34050400 | Treasury Stock - Other | X | X |
| 35000100 | Shareholder Equity (parent) | X | X |
| 36000100 | Other Comprehensive Income (Equity) | X | X |
| 40510100 | AC / HTM Interest on Bank Balances | X | X |
| 40610200 | Interest-O/N CB Funds Sold | X | X |
| 40620300 | Interest-Term CB Funds Sold | X | X |
| 40710600 | Interest-O/N Resells | X | X |
| 40720300 | AC / HTM Interest-Term Resells | X | X |
| 40810400 | AC/HTM Dbt-Gv't Treasury -Interest | X | X |
| 40820300 | AC/HTM Dbt-Mtg Backed-Interest | X | X |
| 40840600 | FVOCI/AFS Dbt-Gv't Treasury-Interest | X | X |
| 40850700 | FVOCI/AFS Dbt-Mtg Backed-Int | X | X |
| 40860100 | Debt-AC Int. other | X | X |
| 40860200 | Debt-FVOCI Int. Other | X |  |
| 40910100 | Equity Sec-Div Stk-Taxable |  | X |
| 40920200 | Equity Sec-Div Stk-Tax Ex |  | X |
| 40930300 | Equity Sec-Divd-Oth |  | X |
| 41010100 | Trading Asts-Int-Gvt Treasury | X | X |
| 41020200 | Trdg Asts-Int-Mort Backed Sec | X | X |
| 41030300 | Trading Asts-Int-Oth Debt Sec | X | X |
| 41040400 | Trading Asts-Int-CDs | X | X |
| 41050500 | Trading Asts-Int-Bks Accpts | X | X |
| 41060600 | Trading Asts-Int-Coml Paper | X | X |
| 41070700 | Trading Asts-Int-Other | X | X |
| 41310900 | Int Inc-Lns-Coml-Secd Coml RE | X | X |
| 41311100 | Int Inc-Lns-Coml-Secd by Farmland | X | X |
| 41320200 | Int Inc-Loans-Coml-Bks | X | X |
| 41330300 | Int Inc-Loans-Coml-Accep Purch | X | X |
| 41340400 | Int Inc-Loans-Coml & Indl Loans | X | X |
| 41360600 | Int Inc-Loans-Other Coml | X | X |
| 41370700 | Misc Fee Inc - Coml & Indl Lns | X | X |
| 41381800 | Misc Fee Inc-Cml Lns-Bks | X | X |
| 41382900 | Msc Fee Inc-Other Coml | X | X |
| 41410100 | Credit Card Loan Int | X | X |
| 41420200 | Interest Income-Securitized | X | X |
| 41430300 | Interest Income-Participations | X | X |
| 41440400 | Misc Fee Income-Credit Card | X | X |
| 41450500 | Cash Advance Fees | X | X |
| 41451100 | Card Overlimit Fees | X | X |
| 41452200 | Late Payment Fees | X | X |
| 41510300 | Int Inc-Indl-Consumer Lns | X | X |
| 41520400 | Int Inc-Indl-Student Loans | X | X |
| 41530500 | Int Inc-Indiv-All Oth | X | X |
| 41540600 | Misc Fee Inc-Consumer Lns | X | X |
| 41541700 | Misc Fee Inc-Student | X | X |
| 41542800 | Misc Fee Inc-Indiv Other | X | X |
| 41550900 | Auto Loan Interest | X | X |
| 41560100 | Misc Fee Inc-Auto | X | X |
| 41610200 | Int Inc-HML | X | X |
| 41620300 | Misc Fee Inc-HML | X | X |
| 42010400 | Drct Fin Lease |  | X |
| 42020500 | Lev Lse Inc-Int |  | X |
| 42030600 | Ownrshp Fgn Lse-Int Inc | X | X |
| 42040700 | Conditional Sales Lease Inc |  | X |
| 42050800 | Misc Fee Inc-Leases | X | X |
| 43010100 | Intercompany Int. Inc - Lending | X | X |
| 43010200 | AC Intercompany Int.Inc. - Investments | X | X |
| 43010300 | Intercompany Interest income FVOCI Investments | X |  |
| 43010900 | Intercompany Int. Income - Other | X | X |
| 44010100 | Loan Loss Provision | X | X |
| 44020100 | Loan Loss Provision-Securitized | X | X |
| 44030100 | Loan Loss Provision-Participated | X | X |
| 44040100 | Lease Loss Provision | X | X |
| 44040200 | Amort Exp-Cap Lease |  | X |
| 44060100 | Interco Loan & Lease provisions | X | X |
| 45010200 | Miscellenious Interest Income non-EIR | X |  |
| 45050990 | Miscellaneous Interest Inc EIR | X | X |
| 50510100 | Savs Dep Int-Savings | X | X |
| 50520200 | Savs Dep Int-Other | X | X |
| 50610300 | Time Dep Int-C/D's | X | X |
| 50620400 | Time Dep Int-IRA's | X | X |
| 50630500 | Time Dep Int-Other | X | X |
| 50710400 | Int On O/N CB Funds Purch. | X | X |
| 50720100 | Int Term CB Funds Purch. | X | X |
| 50730200 | Int-Other CB Funds Purch. | X | X |
| 50810400 | Int On O/N Repos | X | X |
| 50820500 | Int On O/N Repos-Other | X | X |
| 50830100 | Int On Term Repos | X | X |
| 50840400 | Int On Term Repos-Other | X | X |
| 51010600 | Int On ST Borr- Banks | X | X |
| 51030700 | Int On ST Borr-CB Reserve | X | X |
| 51040900 | Int On ST Borr-Capital Lease |  | X |
| 51045100 | Int On ST Borr-Lns Sold | X | X |
| 51050200 | Int On ST Borr-Pvt Placements | X | X |
| 51060300 | Int On ST Borr-Comml Paper | X | X |
| 51070400 | Int On ST Borrow-Other | X | X |
| 52010300 | Int On LT Debt-Conv Deben | X | X |
| 52011200 | Int On LT Debt-Subordinate Oth | X | X |
| 52020300 | Int On LT Debt-Notes | X | X |
| 52040600 | Int On LT Debt-Capital Leases |  | X |
| 52050700 | Int On LT Debt-Pvt Placement | X | X |
| 52060800 | Int On LT Debt- Banks | X | X |
| 52090300 | Int On LT Debt-Other | X | X |
| 53010100 | Intercompany Int. Exp | X | X |
| 53010200 | Intercompany Int. Expense Investments | X | X |
| 53010300 | Intercompany Int. Expense Other | X | X |
| 54020100 | Misc Int Exp-Cr for Avail Bal | X | X |
| 54090200 | Misc Int Exp-Other | X | X |
| 60110100 | Fgn Exch Inst-Fx Gain/Loss | X | X |
| 60120100 | Derivative-IRC- Gain/Loss | X | X |
| 60130200 | Derivative-Equity Gain/Loss | X | X |
| 60140700 | Derivative-Credit Swaps | X | X |
| 60150100 | Trading Income from Debt -Securities | X | X |
| 61010100 | Coml Ln Serv Fee | X | X |
| 61020200 | Credit Crd-Merch Fees | X | X |
| 61030300 | Credit Crd-Cardholder Fees | X | X |
| 61031400 | Cardholder Fees-Securitized | X | X |
| 61032500 | Gain/Loss Cr Card Secrtztns | X | X |
| 61033700 | Credit Crd-Other | X | X |
| 61040100 | HML & Eq Cred Fees | X | X |
| 61050200 | Installment Credit Ln Serv Fee | X | X |
| 61055300 | Automobile Ln Serv Fees | X | X |
| 61060400 | Leasing Fee Income | X | X |
| 61073400 | LC Doc Fee Inc | X | X |
| 61510100 | Fiduc Mgmt Fees | X | X |
| 61520200 | Trust Mgmt Fees | X | X |
| 61810100 | Serv Chrgs-Deps-Deficit Balance | X | X |
| 61820200 | Serv Chrgs-Pymnt. Svrcs | X | X |
| 61830300 | Serv Chrgs-Deps-Nsf Chrgs | X | X |
| 61840400 | Serv Chrgs-Deps-Maint. Srvcs. | X | X |
| 61910100 | Oth Serv-Branch Serv Chrgs | X | X |
| 61911200 | Oth Serv-Safe Deposit Fees | X | X |
| 61920300 | Oth Serv-Disc Brokerage Fee | X | X |
| 61921500 | Oth Serv-Mutual Fund Comm. | X | X |
| 61930600 | Insur Prem & Commissions Fees | X | X |
| 61931700 | Insur Prem-Accident&Health | X | X |
| 61990800 | Oth Serv Chrgs-Other | X | X |
| 62010100 | Eq Inc Cons Subs-Eq Inc/Loss | X | X |
| 62020200 | Eq Inc Cons Subs-Transl G/L | X | X |
| 62020900 | Interco Misc Income | X | X |
| 62510100 | Debt Secs G/L-Gvt Treas | X | X |
| 62520200 | Debt Secs G/L-MBS | X | X |
| 62530300 | Oth Eqty Sec G/L-Writedowns | X | X |
| 63010800 | Misc Inc- On Sale Of Loans | X | X |
| 63020800 | Misc Inc Sale-Leased Asset | X | X |
| 63030800 | Misc Inc- On Sale Of Oreo | X | X |
| 63040800 | Misc Inc Sale Oth Assets | X | X |
| 63050600 | Reval FX Gain/Loss | X | X |
| 63060100 | Operating Leases Income | X | X |
| 63070100 | Rev. from Equity Sec-Div Stk-Taxable | X | X |
| 63070200 | Rev. from Equity Sec-Div Stk-Tax Ex | X | X |
| 63070300 | Rev. from Equity Sec-Divd-Oth | X | X |
| 63090700 | Misc Income-Other | X | X |
| 63099999 | P&L Offset | X | X |
| 70110100 | Base Salary Expenses | X | X |
| 70110101 | Other Payroll Expenses | X | X |
| 70120200 | Base Salary-Incent Comp Pymt | X | X |
| 70130300 | Base Salary-Parttime | X | X |
| 70140400 | Base Salary exp-Temporary | X | X |
| 70150500 | Overtime Salary Exp | X | X |
| 70180100 | Other Personnel Expenses | X | X |
| 70190600 | Other Salary Exp | X | X |
| 70210300 | Incent Comp-Cash Plans | X | X |
| 70220400 | Incent Comp-Stock Plans | X | X |
| 70230300 | Incent Comp-Other | X | X |
| 70230400 | Empl Pensions Contributions | X | X |
| 70240400 | Empl Pension Exp | X | X |
| 70250500 | Empl Savs Incent (401K) Exp |  | X |
| 70310100 | Empl Insur Exp-Medical | X | X |
| 70320200 | Empl Insur Exp-Dental | X | X |
| 70330300 | Empl Insur Exp-Life | X | X |
| 70340400 | Empl Insur Exp-Lt Disab | X | X |
| 70390500 | Empl Insur Exp-Other | X | X |
| 70410600 | Fringe Benefits | X | X |
| 70420700 | Empl Post Retirement Exp | X | X |
| 70480800 | Oth Empl Bene Exp-Tuition | X | X |
| 70490900 | Oth Empl Bene Exp | X | X |
| 70510100 | Payroll Taxes (for banking) | X | X |
| 70520200 | Payroll Tax-Unemploy Comp | X | X |
| 70520300 | Payroll -Tax & Social Security | X | X |
| 70590300 | Payroll Tax-Other | X | X |
| 71510100 | Furn&Equip Rentals Exp-Dp | X | X |
| 71520200 | Furn&Equip Rentals Exp-Non Dp | X | X |
| 71530300 | Furn & Equip Depr Exp-Dp | X | X |
| 71540400 | Furn & Equip Depr Exp-Non Dp | X | X |
| 71550500 | Furn & Equip Maint/Repairs-Dp | X | X |
| 71560600 | Furn&Equip-Maint/Rprs-Nondp | X | X |
| 71570700 | Other Furn & Equip-Dp | X | X |
| 71575800 | Other Furn & Equip-Non Dp | X | X |
| 71580900 | Low Value Assets | X | X |
| 71610100 | Occupancy Exp-Rent | X | X |
| 71620200 | Occup Exp Taxes & Ins | X | X |
| 71630300 | Occupancy Exp-Building Depr | X | X |
| 71640400 | Occpy Exp-Leasehold Amort | X | X |
| 71650500 | Occpy Exp-Build Maint&Repair | X | X |
| 71660600 | Occupancy Exp-Utilities | X | X |
| 71670700 | Occpy Exp-Taxes & Insurance | X | X |
| 71670900 | Clearing Account - Asset Disposals | X | X |
| 71680800 | Occupancy Exp-Other | X | X |
| 71910100 | Advertising Exp | X | X |
| 71911200 | Memberships & Prof Dues | X | X |
| 71912300 | Subscrip & Pub. | X | X |
| 71920400 | Contributions | X | X |
| 71925500 | Travel & Entertainment Exp | X | X |
| 71925501 | Travel Expenses- Hotel & Accom. | X | X |
| 71925502 | Travel Expnses - Meals | X | X |
| 71925503 | Travel Expenses - Air , Rail & Mileage | X | X |
| 71925504 | Travel Expenses - Entertainment (for banking) | X | X |
| 71925505 | Travel Expenses- Miscellaneous | X | X |
| 71930600 | Stationery & Supplies Exp | X | X |
| 71935700 | Telecommunications Exp | X | X |
| 71940800 | Pstge & Freight-Postage | X | X |
| 71945100 | Recruiting Costs | X | X |
| 71950300 | Training & Dev Exp | X | X |
| 71960500 | Insurance Exp | X | X |
| 72010101 | Prof Purch Serv-Audit | X | X |
| 72020200 | Prof Purch Serv-Legal Services | X | X |
| 72030300 | Prof Purch Serv-Consulting | X | X |
| 72040400 | Prof Purch Serv-Data Processing | X | X |
| 72090500 | Oth Purch Serv-Other | X | X |
| 73000100 | Intang Amort-Brand Prem | X | X |
| 73000200 | Intang Amort-Goodwill | X | X |
| 73000300 | Intang Amort-Other | X | X |
| 74000100 | Oreo-Provision, Valuation Adjs | X | X |
| 74000200 | Oreo-Management Exp | X | X |
| 74000300 | Oreo-Real Estate Taxes | X | X |
| 74000400 | Oreo-Depreciation Exp | X | X |
| 74000500 | Oreo-Other Expenses | X | X |
| 75010100 | Collection Costs | X | X |
| 75010200 | Conf & Business Meetings | X | X |
| 75010300 | Dep Insur Assmnts | X | X |
| 75010400 | Misc Exp-Equip/Lease Writeoffs | X | X |
| 75010500 | Misc Exp-Commit/Guar. Fees | X | X |
| 75010600 | Misc Exp-Taxes | X | X |
| 75010700 | Misc Exp-Software | X | X |
| 75010800 | Cash Discount Expense -AP | X | X |
| 75010810 | Cash Discount Received -AP | X | X |
| 75010850 | Misc Exp-Other | X | X |
| 76010100 | Income Tax Exp | X | X |
| 76010200 | Inc Tax Exp-SIT |  | X |
| 76010300 | Inc Tax Exp-City/County |  | X |
| 77700100 | Intercompany Expenses | X | X |
| 77700200 | Inc Tax Exp-Subs Tax Prov | X | X |
| 77799999 | Small Clearing Differences | X | X |
| 78010100 | Charge-Off |  | X |
| 79900100 | P&L Suspense | X | X |
| 80110100 | Commit- Loans | X | X |
| 80120200 | Commitments-Credit Cards | X | X |
| 80130300 | Securities Underwriting | X | X |
| 80140400 | Commitments- Oth | X | X |
| 80190500 | Commitments- Contra | X | X |
| 80210100 | Standby Letters of Credit-Corporate | X | X |
| 80220200 | Standby Letters of Credit- Municipalities | X | X |
| 80230300 | Standby Letters of Credit-Correspndnt Bnk | X | X |
| 80240400 | Standby Letters of Credit - Other | X | X |
| 80290500 | Standby Letters of Credit - Contra | X | X |
| 80310100 | Securities Borrowed | X | X |
| 80320200 | Securities Lent | X | X |
| 80390300 | Securities Borrow/Lent-Cntra | X | X |
| 80410100 | Part. Accpt Acq - Corrs Bnk | X | X |
| 80420200 | Part Accpt Conveyed-Corrs Bnk | X | X |
| 80490300 | Accpt Participated-Contra | X | X |
| 80510100 | Forward Deposits Placed | X | X |
| 80511200 | Forward Deposits Taken | X | X |
| 80512300 | Forward Fed Funds Sold | X | X |
| 80519400 | For Dpts/For Fed Funds- Contra | X | X |
| 80520500 | Credit Deriv. Act As Guarantor | X | X |
| 80521600 | Credit Deriv Act Beneficiary | X | X |
| 80529700 | Credit Derivatives - Contra | X | X |
| 80530800 | Oth Misc Contingencies | X | X |
| 80539900 | Oth Misc. Contingencies-Contra | X | X |
| 81010100 | Interest Rate Futures | X | X |
| 81011200 | Interest Rate Forwards | X | X |
| 81012300 | Interest Rate Swaps | X | X |
| 81013400 | IR Fu/Fo/Sw -Contra | X | X |
| 81110200 | IR Opt Bgt Exch | X | X |
| 81111300 | IR Op-Bgt-OTC | X | X |
| 81112400 | IR Opt-Sold Exch | X | X |
| 81119500 | IR Options - Contra | X | X |
| 81210100 | FX Futures | X | X |
| 81211200 | FX Forwards | X | X |
| 81212300 | FX Swaps | X | X |
| 81219400 | FX Fu/Fo/Sw - Contra | X | X |
| 81310100 | FX Opt Bgt Exch Trd | X | X |
| 81311200 | FX Opt-Bgt OTC | X | X |
| 81312300 | FX Opt-Sold | X | X |
| 81319400 | FX Options-Cntra | X | X |
| 81410100 | Eq Derivative Futures | X | X |
| 81411200 | Eq Derivative Forwards | X | X |
| 81412300 | Eq Derivative-Swaps | X | X |
| 81419400 | Eq Derivatives - Contra | X | X |
| 81510100 | Eq Derivatives Opt Bgt Exch Trd | X | X |
| 81511300 | Eq Derivative Opt- Bgt OTC | X | X |
| 81512400 | Eq Derivative Opt-Sold | X | X |
| 81519500 | Eq Derivative Opt-Contra | X | X |
| 81520200 | Eq Der Opt Bgt Exch Trd-Trd 1-5 | X | X |
| 90110100 | Tech. Staff | X | X |
| 90110200 | Software | X | X |
| 90110300 | Hardware | X | X |
| 90110400 | Network Services | X | X |
| 90110500 | Tech. Admin | X | X |
| 90210100 | Support Staff | X | X |
| 90210200 | Occupancy | X | X |
| 90210300 | Telecomm. | X | X |
| 90210400 | Corporate Security | X | X |
| 90810100 | Exec. Management | X | X |
| 90810200 | Admin. Staff & Change Mgmt. | X | X |
| 90810300 | Supplier Management | X | X |
| 90810400 | Other Admin. | X | X |
| 91010010 | Corporate Staff | X | X |
| 91010020 | Treasury Services | X | X |
| 91010030 | Risk Management Services | X | X |
| 91200100 | Audit / Control Services | X | X |
| 91200200 | Regulatory Respose / Policy & Procedures | X | X |
| 91200300 | Litigations | X | X |
| 91501010 | Research & Product Dev. Support Services | X | X |
| 91502040 | Product Branding Services | X | X |
| 92011040 | Investor services & reporting | X | X |
| 92023060 | Customer Support & Services | X | X |
| 92031080 | Loss Mitigation & Foreclosure Services | X | X |
| 92049010 | Real Estate Owned Services | X | X |
| 92051030 | Collection Services | X | X |
| 92066010 | Payroll Services | X | X |
| 93015070 | Tax Services | X | X |
| 93025020 | Billing Services | X | X |
| 93031040 | Operations Support Services | X | X |
| 95011010 | Lending Operations services | X | X |
| 95027010 | Invest ment Operations Servives | X | X |
| 95041030 | Deposit Operations | X | X |
| 95067020 | Treasury Services | X | X |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/coa-overview-insurance-181]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/COA_Overview_Banking.xlsx` — full document · extracted with `xlsx2md` · 30,373 chars in the whole document
