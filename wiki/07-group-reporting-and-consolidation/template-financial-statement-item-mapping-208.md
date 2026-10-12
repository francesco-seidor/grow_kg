---
id: 07-group-reporting-and-consolidation/template-financial-statement-item-mapping-208
title: Template Financial Statement Item Mapping (Template_Financial_Statement_Item_Mapping)
description: "SAP S/4HANA Cloud import template mapping 596 YCOA G/L accounts to financial statement items under consolidation COA Y1 (mapping ID Y1, revision 1)."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-units-and-fs-item-mapping]
aliases: [Template_Financial_Statement_Item_Mapping]
keywords: [Consolidation Units and FS Item Mapping, financial statement item mapping, consolidation chart of accounts, g/l account mapping, import template, financial statement items, fixed assets accounts, tax accounts, payroll accounts, receivables and payables accounts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Template_Financial_Statement_Item_Mapping.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-208
topic: 07-group-reporting-and-consolidation/consolidation-units-and-fs-item-mapping
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Template Financial Statement Item Mapping (Template_Financial_Statement_Item_Mapping)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Template_Financial_Statement_Item_Mapping.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Units and FS Item Mapping** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## Template Financial Statement Item Mapping

### Sheet: Data

| Import Financial Statement Item Mappings |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ConsolidationChartOfAccounts | FSItemMappingID | FSItemMappingName | FSItemMappingRevision | FSItemMappingRevisionText | ChartOfAccounts | GLAccount | GLAccountName | FinancialStatementItem | FinancialStatementItemText |
|  | Header Data |  |  |  |  | Line Items |  |  |  |
| *Consolidation COA (2) | *Mapping ID (10) | Mapping Name (60) | *Mapping Revision (10) | Revision Description (60) | *G/L COA (4) | *G/L Account (10) | G/L Account Name (20) | *FS Item (10) | FS Item Description (15) |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12606010 | Def Inp tax/FXA VST | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605923 | RC Com CESS Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605917 | RC Im IGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605922 | RC UTGST Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605920 | RC SGST Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12609100 | Def Imp inp tax VST | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605909 | OutpTax CGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605908 | OutpTax SGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12609000 | Defer.Input Tax > 0% | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605925 | RC ImCom CESS Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605921 | RC CGST Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605924 | RC Im IGST Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605913 | RC SGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605910 | OutpTax UTGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12550000 | Unbilled Revenue | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12610000 | Input Tax | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12610100 | Dom inp VAT rev char | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12608000 | Tax Transfer Establi | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12614000 | Input Tax (ICx) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605912 | RC IGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605915 | RC UTGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605918 | RC Im Com CESS IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605906 | InpTax ImCom CESS IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605911 | OutpTax Com CESS IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605907 | OutpTax IGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605914 | RC CGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605919 | RC IGST Inv IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12603000 | Input tax (VS3) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12110000 | OthDwnPmtCurrAsset | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12540000 | Other Rcvbls nra | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12618000 | Input CENVAT | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12111000 | Input Tax clrg DownP | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605010 | LuxTax VAT In ID | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12410000 | Guarant.given Clrng | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12540200 | Other Rcvbls Adj | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12501000 | Clrng Interest Rcvbl | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12541000 | Rcvbls Tax Auth nra | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12420000 | Security Deposit Cus | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605903 | InpTax UTGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12543000 | Rcvbls Partners nra | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12112000 | Downpaymts Inventory | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12411000 | Guarantees given Cus | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12631000 | Input Tax (J1*) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605000 | Import Sale Tax paid | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12604000 | Input Tax (VS4) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12619000 | VAT reg&out o sc rec | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605904 | InpTax Com CESS IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605900 | InpTax IGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12119200 | Adj down pmt Vendor | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12532000 | Clrg cont.claims-che | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605901 | InpTax SGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605902 | InpTax CGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605905 | InpTax Im IGST IN | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12542000 | Rcvbls Empl Opay nra | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13711900 | WIP Unbilled Revenue | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12656000 | SED Input ded. (ZVV) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12601000 | Input Tax (VS1) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12600000 | Input Tax (VST) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12602000 | Input Tax (VS2) | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006011 | Input VAT deductible | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12600010 | Input tax/FXA VST | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12590000 | Vendors w/ Debit Bal | 121800 | Oth. Receiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63008000 | Building PerSer | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16005000 | Office Equipment | 161300 | Office Equip |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22003010 | Use Tax Accrued MW3 | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12120000 | Rcvbls Foreign | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52080000 | Loss allwd diff Clrg | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12100100 | Rcvbls Domestic OTA | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61100000 | Payroll Exp Salaries | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17006000 | Acc.Depr'n Furn&Fixt | 161690 | Other PPE,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006022 | veh pur tax pbl(CN) | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006031 | resource tax payable | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41003000 | Accr rev - EBR Adj. | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52541000 | Gain Prc Var PRD | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21310000 | Trade Pbl BoE | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005010 | GST/HST ITC Rece Adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12300000 | Rcvbls Affiliate | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16010500 | InptTxClearTngbDPmt | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21750000 | Clrg Vndr Discnt Net | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001010 | Cash Payment (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44000000 | Over/Underpmt&Ded | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006014 | Tax exempt fr export | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12122000 | Rcvbls Foreign Adj | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61062000 | Worker Comp Assoc | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70500000 | Consump of provision | 514000 | Reversal Prov |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001060 | Checks In (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22004010 | Use Tax Accrued MW4 | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21751000 | Clrg Guaranties Rec | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41001500 | Rev Affiliate- Prod | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52580000 | Gain allwd diff Clrg | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70030000 | Clear ass.disp. | 511000 | G/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 32000000 | Capitl in Exc.of Par | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 55110000 | Sec.Cost Ext.Settlmt | 511000 | G/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001045 | Returns (Cash/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16003000 | Building Improvemnts | 161100 | Lands/Buildings |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75002200 | SoliSurch CorpIncTax | 721000 | Income Tax |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 15300000 | Trip costs advance | 123100 | Prepaid Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44006000 | Sales Deduc Quantity | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 18020000 | Other Long Trm Invst | 172500 | Oth Fin A.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39917000 | Init oth OI GL offs | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090020 | Cr.PPhPasal21 WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71010100 | Gain asset transactn | 511000 | G/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005500 | HST Output Tax Payab | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539105 | Judicial Contingency | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501500 | Hol Pay Prvsn Pre yr | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70010000 | Rev PostCapitalizatn | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21300300 | Paybls Affiliate > 5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44007001 | (-) ICMS on Sales | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21518000 | Doc Split Acct Trip | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65100000 | Office Supplies | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005100 | GST Output Tax Payab | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64050000 | Estimated depreciati | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21110000 | GR/IR Consi/Pipeline | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12609112 | VAT DP Issued Ded RU | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023030 | Payr unempl insuranc | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54051000 | Inv Chg Scrp ext prd | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19320000 | Intangible Assets | 164500 | Oth Intang A. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21522000 | IR to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090000 | Tax Payable | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 14102000 | Loans Other - short | 141400 | Loans &A, C,GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21535001 | COFINS WHT to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72540000 | Gain curr.val. | 604000 | Oth Fin Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71100000 | Interest Expense | 652000 | Int Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24037000 | Deferred Tax Provis | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19310000 | Internal Development | 164500 | Oth Intang A. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44002200 | Sales Disc Affiliate | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21536000 | Tax - IRRF - Contrac | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61022040 | Workers' comp.assoc. | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12121000 | Rcvbls Foreign > 1 | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21780000 | Freight Prov'n SD | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64004000 | Dep.Exp. Motor Veh. | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72010000 | Loss exch.rate diff | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17007000 | Acc.Depr'n Comput HW | 161690 | Other PPE,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12531000 | A/R - Unappl Checks | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21613012 | Tax Col.Source SD IN | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12010000 | Shrt Trm Investments | 111200 | Cash Equiv. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61200000 | Pay Exp Tax&SS Wages | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71010000 | Loss asset transactn | 581000 | L/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21710000 | Amort'n - Prepaymt | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39915000 | Initial FI-AP offset | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75008000 | Trade Tax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70300000 | Intrest income Subs | 601000 | Int Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006013 | trans input VAT(CN) | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71040000 | Discnt lost net proc | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 66010000 | Discountin Exp (ZKB) | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52041000 | Loss Prc Var PRD | 586000 | Op. FV Losses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001000 | Main Bank Acct (C/B) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13100900 | Inv. Reval. Raw Mat. | 131100 | Raw Materials |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21102100 | Cred.adj. FX val. | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539106 | INSS 13 Wage Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21538000 | Tax Other - to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13701400 | WIP Def Rev | 131400 | WIP |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71800000 | Other Extra.Expense | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539002 | INSS on Wage to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75007000 | Property Taxes | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21603000 | Withholding Tax | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17009000 | Acc.Depr'n Auc | 161290 | Tang a UC,Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64030000 | Unsched.dep.Expense | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21516000 | Payroll - ER Benefit | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64006000 | Dep.Exp. Furniture | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21300000 | Paybls Affiliate | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44002000 | Sales Disc Domestic | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61007000 | Trav.Exp Air,Rl,Mile | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65050000 | Unplanned del.costs | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023060 | Payr lab un edu dues | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24010000 | GR/IR Gd/sv not deld | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65000500 | Non Prod Mat Consptn | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61061000 | Payroll Benefits | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21200000 | Paybls Foreign | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12530000 | Rcvbls - Pmt Cards | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24036000 | Other Tax Provision | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539001 | INSS FreeLancer Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530007 | ICMS Complemtry BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21720000 | Other Paybls nra | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61021100 | Payroll Overtime Wag | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16009000 | Assets under Constr. | 161200 | Tang Assets UC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65300000 | Legal&Audit Services | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41000000 | Rev Domestic Prod | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001055 | BoE Out (Cash/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22002010 | Use Tax Accrued MW2 | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52546000 | Consump.Val.(COC) | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21303000 | Paybls affl Comp nra | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16020000 | Low Value Assets | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52570500 | Gain Inv Val Adj Own | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75009000 | Export Duty | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11009055 | BoE Out (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16013000 | Clg cap'd dwn pmt FA | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75002000 | Corp.Income Tax Exp. | 721000 | Income Tax |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63009000 | Leasing Expense | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65002000 | Advert.& Sales Costs | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21900000 | PR Clearing Acct | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501400 | Hol Pay Prvsn Cur yr | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24033000 | Corp Income Tax Prov | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13600000 | Inventory TradingGd | 131200 | Merchandise |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530004 | ICMS Substit Trib | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12101000 | Rcvbls Domestic > 1 | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098500 | Statutory Reserve | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64043000 | Amort.Exp.GoodWill | 572000 | GW Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61102000 | Pay Other Wage exp | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65000000 | Postage and Shipping | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65900000 | Damage Loss | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023020 | Payr endowment insur | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17001000 | Acc.Depr'n Building | 161190 | Lands/Build,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61021000 | Payroll Overtime Sal | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61008000 | Trav.Expense Misc. | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61003000 | Trav.Expense Hotel | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16007000 | Computer HW&Equipmnt | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24031000 | Pension Provision | 261100 | Prov Employe,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11009100 | B of Ex coll (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21533001 | PIS WHT to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39913000 | Initial FI-AM offset | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530000 | Tax - ICMS to Pay (B | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64002000 | Dep.Exp. Mach.& Equ. | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 68002000 | Purchase acct Tradin | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005610 | QST Payab Adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64040000 | Sched.dep. fixed.ass | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 66000600 | Other Operating Gain | 515000 | Oth Op Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21613010 | Tax Col.Off-set.IN | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21200100 | Paybls Foreign OTA | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39916000 | Initial oth GL offs | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16002000 | Machinery & Equipmnt | 161500 | Machinery |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090012 | TDS Provision IN | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75002300 | SoliSurch InteIncTax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65200000 | Other Supplies | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090024 | Cr.PPhPasal26 WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17000000 | Acc.Depr'n Land Impr | 161190 | Lands/Build,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530006 | FCP State Inv BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61052000 | Payroll Exp.Dwn.sal | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12562000 | Deferred Income | 214100 | Def Inc L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71000000 | Bank Charges | 652000 | Int Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41090000 | Other Operating Reve | 515000 | Oth Op Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70015000 | Sttlmt AuC to CO | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 68000000 | Purchase Account Raw | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16014000 | TecClrng Int AAcqu | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 14107000 | Loans to Staff | 141400 | Loans &A, C,GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22140700 | PIx Brazil | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12119000 | Dpaymnt Request Vend | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11008000 | Di Pmnt Acq Bk (C/B) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11009200 | B of Ex Disc (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530005 | FCP Dest State BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005400 | HST ITC Receivable | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64005000 | Dep.Exp. Office Equ. | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61201000 | Pay Exp Tax&SS Salry | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21121000 | GR/IR sett.transf.ML | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24093000 | Indet Paybls Provisi | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005210 | PST Rece Adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006012 | Paid VAT | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44007003 | (-) PIS on Sales | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16001000 | Buildings | 161100 | Lands/Buildings |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22003000 | Sales Tax Accrued | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72520000 | Gain rnd.dif.f.curr | 604000 | Oth Fin Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52560000 | Gain Sml Prc Diff IR | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21200300 | Paybls Foreign > 5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12102000 | Rcvbls Domestic Adj | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61022100 | Payroll Vacatn Pay W | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 15200000 | Prepayments Sal/Wag | 123100 | Prepaid Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21524000 | PIS to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12120100 | Rcvbls Foreign OTA | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65400000 | Freight | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21517000 | Other Personnel Cost | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17002000 | Acc.Depr'n Mch & Equ | 161590 | Machinery, Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44004000 | Sales Deduc Material | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530003 | FCP / FECOEP Recover | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19210000 | Other Rcvbls > 1 | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098400 | Legal Reserve | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13300900 | Invent. Rev.Semi Fin | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21102000 | Paybls Domestic Adj | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12402000 | Depr Rcvbl Affiliate | 121190 | Trade, Allow |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090010 | TDS Provision JV IN | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61104000 | Payroll Expense Indi | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21300200 | Paybls Affiliate 1-5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21532001 | ISS WHT to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539107 | FGTS Vac Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41090010 | VAT Revenue | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61005000 | Travel Exp Grd Trnsp | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21505000 | Payroll - Savings Pl | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44007004 | (-) Cofins on Sales | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65150000 | Computer Supplies | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11008070 | Di Pmnt Aq Clrg(C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21770000 | Accrd Volume Rebate | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13500000 | Inventory Packaging | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52060000 | Loss Sml Prc Diff IR | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21520000 | IPI to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71010200 | Gain from Write Up | 511000 | G/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098000 | Asset Reval Res -ROU | 314000 | Reval Surplus,B |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12303000 | Rcvbls affl Comp nra | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12110100 | Down Payments > 1J | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530002 | ICMS Recover UF Dest | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005700 | QST Output Tax Payab | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16012000 | Cap DP made on asset | 161200 | Tang Assets UC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098600 | Other Reserves | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21100100 | Paybls Domestic OTA | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501200 | 13th mth sal prvsn | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24032000 | Trade Tax Provision | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41000400 | Sales Revenue w/ CE | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 33000000 | Retained Earnings | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001070 | Ck. Clrg Acct (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12609111 | VAT Out Exp Ops RU | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22002000 | Sales Tax Accrued | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21599000 | HR Month End Accrual | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24097000 | Expected Loss Provis | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75009900 | Other Company Taxes | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71050000 | Cash Discount | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52030000 | Loss revaluation | 586000 | Op. FV Losses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006000 | Imp VAT del rev chg | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17030000 | Acc Depr-Excpt Depr | 161690 | Other PPE,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64032000 | Dpr exp(Bk<Tx)-ED | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 18010000 | Common Stck Invt Sub | 172100 | Inv Subs JV AE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 59900000 | COGS (Affiliated) | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22009020 | Defer.Output Tax 0% | 282100 | Def Tax Liab. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24091000 | Guarantees Provision | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006110 | LuxTax VAT Out ID | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005600 | QST ITR Receivable | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75005000 | Input Tax (NAV) | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44003200 | Cust SalesDed Affili | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63003000 | Other PerSer | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001090 | Techn Acct (Cash/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13711400 | WIP AccRev FixPrice | 131400 | WIP |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70800000 | Other Extra.Income | 515000 | Oth Op Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006100 | VAT Tec Exp Cr RU | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41001000 | Rev Foreign - Prod | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63002000 | Water | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72510000 | Gain exch.rate diff | 604000 | Oth Fin Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29120000 | Other Payables > 5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12605916 | RC Com CESS IN | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13400900 | Invent. Rev.FinishGd | 131500 | Finished Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11009900 | BOE Payb - Clr (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006025 | ad loc edu tax pb CN | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64001000 | Dep.Exp. Buildings | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39912000 | Inv Init SF&Fin Bal | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21613011 | Tax Col.at Source IN | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65004000 | Donations | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005800 | RITC | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21523000 | TAX Transfer Plant | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21532000 | Tax - ISS to Pay (BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090021 | Cr.PPhPasal23 WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22512000 | Loans from Banks Adj | 221100 | Borrowing,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12511000 | Rcvbl BoE Bounced | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52590000 | Freight Revenue/Rec. | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21720100 | Guarantees rec Vend | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75004020 | Land Usage Tax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21190000 | Down Paymnt Custome | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21191500 | Tax sett.dwn pmt cus | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530001 | ICMS Recover UF Orig | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090025 | Cr.PPhPasal22 WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65009000 | Other activity costs | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24030000 | Tax Provisions | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12549000 | Deprec other Rcvbls | 121990 | Oth rec,Allow |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 51950000 | Consptn Subcontr | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52070500 | Loss Inv Val Adj Own | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75008050 | Export Taxes | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22100000 | Acquisition tax | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75008020 | Tax Fringe Benefits | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29130000 | Loans from Bank 1-5 | 221100 | Borrowing,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006024 | ad edu tax paya (CN) | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21540000 | Other Clearing Accou | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 26910000 | Investmnt rcvbl recd | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16015000 | OffsetAcct Reval APC | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63004000 | Insurance | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21192000 | Adj acc down pay rec | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21512000 | Payroll - EE Benefit | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22510000 | Loans from Bank nra | 221100 | Borrowing,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70020000 | Rev from Asset Sale | 511000 | G/Disp PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21190100 | Downpaymts rec 1-5 Y | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 51900000 | Consptn Subct.w/o CE | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 41090011 | VAT Goods Sales | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13500900 | Invent.Rev.Packaging | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 51600000 | Consptn Trde Gds | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75004040 | Tax&addit. Duty | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61401000 | HR Recruitement | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21735500 | Delivery Costs MM | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098700 | Spec tax-allow R §6b | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16006000 | Furniture & Fixtures | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65003000 | Vehicle Costs | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44002100 | Sales Disc Foreign | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63005000 | Office/Building Rent | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19420000 | Acc.Depr Intangibles | 164590 | Ot Intang A,Amt |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71300000 | Interest Exp.Subsid | 652000 | Int Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21533000 | Tax - PIS to Pay (B | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023040 | Payr work injury ins | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61060000 | Payroll Exp.Pension | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24099900 | Prov. correction | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006051 | Real estate tax pbl | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005000 | GST ITC Receivable | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 66000000 | Other Expenses | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64021000 | Amort Exp Int Assets | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006071 | Indiv income tax pbl | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21302000 | Paybls Affiliate Adj | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64020000 | Dep.Exp. L.V.A | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21527000 | CSLL to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12606000 | Deferred tax assets | 182100 | Def Tax A.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12401000 | Ind Val Adjmnt Rcvbl | 121190 | Trade, Allow |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17008000 | Acc.Depr'n Comput SW | 164290 | Software,Amt |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54040000 | Inv Chg Reserve | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75001000 | Excise Taxes | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61051000 | Payroll Exp.Dwn.wag | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61002000 | 3rd party material | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44007002 | (-) ISS on Sales | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39911000 | Inv Init RawMat Bal | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72530000 | Gain rebates diff. | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 31100000 | Preferred Stock | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001200 | Bank1 Lockbox | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21790000 | Disposite Reserve SD | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24035000 | For Withhol Tax Prov | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090023 | Cr.PPhPasal15 WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 66019900 | Addition Provi (ZKK) | 584000 | Accruals |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64031000 | Dpr exp(Bk>Tx)-ED | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 31000000 | Common Stock | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65301000 | Marketing Expenses | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70040000 | Discount Received | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501300 | Holiday Pay | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006061 | land usage tax pbl | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21534000 | Tax - IRF General to | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13600900 | Invent.Rev.TradingGd | 131200 | Merchandise |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17005000 | Acc.Depr'n Off Equip | 161390 | Office Equ,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005310 | PST Payab Adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539101 | 13 Wage Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 26900000 | Functional Area Clrg | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21730000 | Freight Clrg MM | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21814000 | Sale fut/free deliv. | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539102 | INSS Vac Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 32100000 | Pd in Cap from stock | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13210000 | WIP | 131400 | WIP |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 39914000 | Initial FI-AR offset | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006041 | land inc.valtaxpb CN | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64008000 | Dep.Exp. Comp.SW | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001050 | Checks Out (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001030 | Other Int Trsf (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19110000 | Loans Other long trm | 181100 | Loans &A, NC,GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16010000 | Down pmnts Tangibles | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52531000 | Gain val'n ext prd | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 51500000 | Consptn Packag Mat | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61022020 | Disability Pay | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21613000 | Prepaid Tax for CWT | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 10020000 | Petty Cash Journal | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75003000 | Deferred Tax | 722000 | Deferred Tax |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006101 | VAT DP Received RU | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 26911000 | Clrg invst rcvbl rcd | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70100000 | Interest Income | 601000 | Int Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001080 | Cash Receipt (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21120000 | GR/IR | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001040 | Direct Debit (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21526000 | COFINS to Recover (B | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65001000 | Purchased Services | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21525000 | ISS to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21191000 | Dpaymnt Request Cust | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54070000 | Inv Chg Rcpt w/o PO | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 90002000 | Deferred Carried For | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22010100 | Dom outp VAT rev chg | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21450000 | Offsett trav exp pd | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005900 | GST/HST Self-Assess | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75004000 | Other Taxes Income | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65008000 | Purchased Svcs-Time | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21760000 | Freight provision MM | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 62020000 | Flatrate Val Adjstmt | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71010700 | Estimated dep FI-AA | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44001000 | Sales Rebates | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64060000 | Accrued interest-CO | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19410000 | Acc. Amort Int. Dev. | 164590 | Ot Intang A,Amt |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24020000 | GR/IR Gs/sv not invd | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005110 | GST/HST Payab Adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21503000 | Payroll - Soc Sec | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21721000 | Res unrealized Costs | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539000 | INSS Contractors to | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44003000 | Cust SalesDed Domest | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21190200 | Downpaymts rec > 5 Y | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21100200 | Paybls Domestic 1-5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 51700000 | Consptn Repair Mat | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023010 | payr medical insuran | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70900000 | Fines&Penalties | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70300100 | Gain Longterm Invest | 512000 | G/Sale Shares |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44003100 | Cust SalesDed Foreig | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005300 | PST Output Tax Payab | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61020000 | Payroll Bonus | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44005000 | Free Gds/Disc in knd | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501000 | Accrued Net Payroll | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22008000 | VAT reg&out o sc pbl | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24031100 | Prv Pension-ledg spc | 261100 | Prov Employe,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63000500 | QM Cspt ExtPrd w/Act | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12301000 | Rcvbls Affiliate > 1 | 181800 | Oth Rec, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61004000 | Trav.Expense Meals | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75004010 | Vehicle Vessels Tax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21122000 | GR/IR Adjustment | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22090022 | Cr.PPhPasal4(2)WT ID | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098200 | Profit Reserves | 316000 | Retained Earn. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64003000 | Dep.Exp. Build.& Imp | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12500000 | Interest Rcvbls | 121900 | Accrued Int. |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539103 | FGTS 13 Wage Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12100000 | Rcvbls Domestic | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29500100 | Zero Balance Clrg | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098100 | Capital Reserves | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63001000 | Electricity&Utilitie | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61500000 | Sales Commissions | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 71015000 | OffsetAcct Reval Dep | 517000 | Op.FV Gain |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22140900 | COx Brazil | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22001010 | Use Tax Accrued MW1 | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22140000 | Output tax (ICZ) | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005710 | QST Outp tax pay adj | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44007000 | (-) IPI on Sales | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24090000 | Other provisions | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12561000 | Prepaid Expenses | 123100 | Prepaid Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 66000500 | Income-redct in prov | 514000 | Reversal Prov |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17004000 | Acc.Depr'n Motor Veh | 161490 | Vehicles, Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61006000 | Trav.Exp Entertainmt | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54011200 | InvCh PurOffs Tradin | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 50200000 | COGS Trade | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12302000 | Rcvbls Affiliate Adj | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24034000 | Cap Gain Tax Provis | 262600 | Misc Prov,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61023050 | Payr housing fund CN | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21735000 | Delivery cst prov MM | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005910 | PST Self-Assess | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19430000 | Accum. Amort. GW | 163190 | Goodwill, Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29131000 | Loans from Bank > 5 | 221100 | Borrowing,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61103000 | Pay Exp Dir Labor co | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 90001000 | Activated Carried Fo | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12609020 | Defer.Input Tax 0% | 182100 | Def Tax A.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21509000 | Payroll Work Comp As | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29110000 | Other Payables 1-5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75004030 | stamp tax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22009999 | Imported Ser Rev ch | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 75002100 | Capital Gains Tax | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001065 | BoE Collection (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61063000 | Dues to Associations | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22001000 | Sales Tax Accrued | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21502000 | Payroll Taxes | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16004000 | Motor Vehicles | 161400 | Vehicles |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21600000 | Reserve Defer'd Tax | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 24098300 | Capital Reserve | 311000 | Issued Capital |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539104 | Labor Contingency | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539100 | Vacation Accrual | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61101000 | Pay Othr salary exp | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21202000 | Paybls Foreign Adj | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52530000 | Gain revaluation | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 19330000 | Goodwill | 163100 | Goodwill |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52041500 | Loss Inv Val Adj Ext | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 29500900 | DocSplit Clrg Act CO | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 68001000 | Purchase acct Packag | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22009000 | Defer.Output tax > % | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21530008 | ICMS clearing BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52031000 | Loss val ext prd | 586000 | Op. FV Losses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21535000 | Tax - COFINS to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72020000 | Loss rnd.dif.f.curr | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16014100 | Clrng Asset Acquisit | 161600 | Other PPE |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21200200 | Paybls Foreign 1-5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22004000 | Sales Tax Accrued | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 62000000 | Bad Debt Expense | 583000 | Bad Debt Allow |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12510000 | Rcvbls - BoE | 121100 | Trade, GV |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21100000 | Paybls Domestic | 211100 | Tra Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 72040000 | Loss curr.val. | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21745000 | Customs prov'n MM | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21508000 | Payroll - Garnishmen | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 52541500 | Gain Inv Val Adj Ext | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65008500 | Subcontract.Services | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61022000 | Payroll Vacatn Pay S | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21537000 | Tax -CSLL to Pay (BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 65008300 | Services - General | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21531000 | Tax - IPI to Pay (BR | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61400000 | Training Education | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61010000 | Payroll Other Exp | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001066 | BoE Disc. (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22006026 | Lic tax vehicl vess | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21180000 | Customers w/ cr bal | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22005200 | PST Receivable | 283100 | Oth Liab, NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 70050000 | Clrg aff assettransf | 515000 | Oth Op Income |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22007000 | Export VAT | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 64007000 | Dep.Exp. Comp.HD | 571000 | Amt/Dep/Imp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63000000 | Mach Equipm PerSer | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 62010000 | Ind Value Adjustment | 653000 | Oth Fin Exp |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21100300 | Paybls Domestic > 5 | 281600 | Oth Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21720200 | Other Paybls Adj | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54441000 | Adj Res Unreal. Cost | 584000 | Accruals |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21539003 | FGTS to Pay | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16008000 | Computer Software | 164200 | Software |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21740000 | Customs Duty Clrg | 214200 | Oth Liab.,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11008030 | Dig Pmnt Tran (C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61310000 | INSS (Direct Product | 730000 | Discontinued |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 13601000 | Inventory Adjustment | 131600 | Oth Inventories |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 16000000 | Land & Ld Improvemts | 161100 | Lands/Buildings |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21105000 | Travel exp payable | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 44420000 | Rev Adj | 411100 | Sale of Goods |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 54011100 | InvCh PurOffs Packag | 412100 | Var Inventory |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63006000 | Telephone and other | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21519000 | Payroll Allocation | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 11001020 | BANK TRANSFER(C/S) | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 68010000 | Purch.acc.(SF&Fin) | 412200 | Cost Serv/Mat |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21521000 | ICMS to Recover (BR) | 151200 | NC Assets HFO |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21350000 | Clrg Invoice Reductn | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 63007000 | Fax and Internet | 585000 | Oth Op.Expenses |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 10010000 | Petty Cash | 111100 | Cash on Hand |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17020000 | Acc.Depr'n L.V.Asse. | 161690 | Other PPE,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 17003000 | Acc.Depr'n Bldg Impr | 161190 | Lands/Build,Dep |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 22000000 | Output tax (MWS) | 213000 | Inc Tax Liab,C |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21460000 | Dividend payable | 211700 | Div Pay L.,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 61022010 | Sick Pay | 560000 | Wages,Oth Benef |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 21501100 | Bonus prvsn Prev yr | 211800 | Oth Payables,NC |
| Y1 | Y1 | Consolidation chart of account | 1 | 1 | YCOA | 12400000 | Doubtfull Rcvbls | 121190 | Trade, Allow |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-a10-87]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-j10-88]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-j1s-89]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-mc-90]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Template_Financial_Statement_Item_Mapping.xlsx` — full document · extracted with `xlsx2md` · 70,172 chars in the whole document
