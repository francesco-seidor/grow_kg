---
id: 01-solution-foundation-and-platform/2608-predelivered-fyv-253
title: 2608 predelivered FYV (2608_predelivered_FYV)
description: "Reference table of fiscal year variants predelivered in SAP S/4HANA Cloud Public Edition 2608: periods, special periods, corporate FYV eligibility, origin and remarks."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/fiscal-year-variants]
aliases: [2608_predelivered_FYV]
keywords: [Predelivered Fiscal Year Variants, fiscal year variants, posting periods, special periods, corporate fiscal year variant, asset accounting, country localization, uk construction industry scheme, 2608]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_predelivered_FYV.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-253
topic: 01-solution-foundation-and-platform/fiscal-year-variants
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 predelivered FYV (2608_predelivered_FYV)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_predelivered_FYV.xlsx`, extracted with `xlsx2md`. Grouped under **Predelivered Fiscal Year Variants** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 predelivered FYV

### Sheet: Fiscal Year Variants

| Fiscal year variants included in SAP S/4HANA Cloud Public Edition |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fiscal Year Variant Name | Fiscal Year Variant Description | Number of posting periods within Fiscal year | Number of special periods within Fiscal year<br>*** | Calendar year dependent i.e. the posting periods match the months of the calendar year | Can be used as corporate FYV and assigned with SSP-UI 102714 "Fiscal Year Variant"? | Origin of Fiscal year variant | Brief Remarks |
| 24 | Half periods | 024 | 00 |  | No | From SAP standard | Each calendar month has 2 posting periods, Fiscal year = Calender year |
| BM | BI Monthly | 006 | 00 |  | No | From SAP standard | Each posting period covers 2 calendar months, Fiscal year = Calender year |
| C1 | 1st period (calendar year) | 001 | 00 |  | No | From SAP standard | Only 1 posting period, Fiscal year = Calender year |
| DL | Daily | 366 | 00 |  | No | From SAP standard | Each calendar day is a posting period, Fiscal year = Calender year |
| K0 | Calendar year, 0 spec. period | 012 | 00 | X | Yes | From SAP standard | Posting period = Calendar Month, Fiscal year = Calender year; no special period |
| K1 | Cal. Year, 1 Special Period | 012 | 01 | X | Yes | From SAP standard | Posting period = Calendar Month, Fiscal year = Calender year |
| K2 | Cal. Year, 2 Special Periods | 012 | 02 | X | Yes | From SAP standard | Posting period = Calendar Month, Fiscal year = Calender year |
| K3 | Cal. Year, 3 Special Periods | 012 | 03 | X | Yes | From SAP standard | Posting period = Calendar Month, Fiscal year = Calender year |
| K4 | Cal. Year, 4 Special Periods | 012 | 04 | X | Yes | From SAP standard | Posting period = Calendar Month, Fiscal year = Calender year |
| M3 (used in FI-AA) | Apr-Mar, 24 Per., 4 sp. Per | 024 | 04 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.04<br>* 2 periods in each calender month<br>* For posting periods in calender month Apr - Dec, Fiscal year = Calender year<br>* For posting periods in calender month Jan - Mar, Fiscal year = Calender year - 1 |
| M4 (used in FI-AA) | Cal. Year, 24 Per., 4 sp. Per | 024 | 04 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.01<br>* 2 periods in each calender month<br>* Fiscal year = Calender year |
| M6 (used in FI-AA) | Jul-Jun, 24 Per., 4 sp. Per | 024 | 04 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.07<br>* 2 periods in each calender month<br>* For posting periods in calender month Jul - Dec, Fiscal year = Calender year<br>* For posting periods in calender month Jan - Jun, Fiscal year = Calender year - 1 |
| M9 (used in FI-AA) | Oct- Sep, 24 Per., 4 sp. Per | 024 | 00 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.10<br>* 2 periods in each calender month<br>* For posting periods in calender month Oct - Dec, Fiscal year = Calender year + 1<br>* For posting periods in calender month Jan - Sep, Fiscal year = Calender year |
| N3 (used in FI-AA) | Apr-Mar,24 P.,4.SP,yr shift+1 | 024 | 04 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.04<br>* 2 periods in each calender month<br>* For posting periods in calender month Apr - Dec, Fiscal year = Calender year + 1<br>* For posting periods in calender month Jan - Mar, Fiscal year = Calender year |
| N6 (used in FI-AA) | Jul-Jun,24 P.,4.SP,yr shift+1 | 024 | 04 |  | No | From SAP standard | * New added in CE1808, used in Asset Accounting only<br>* 1st Posting Period beginns on 01.07<br>* 2 periods in each calender month<br>* For posting periods in calender month Jul - Dec, Fiscal year = Calender year +1<br>* For posting periods in calender month Jan - Jun, Fiscal year = Calender year |
| Q4 ((only for PH) | Quaterly2 | 004 | 00 |  | No | Created by PH Localization | Used in Philippines only<br>*1st Posting Period / Quarter = Jan - Mar<br>* Fiscal year = Calendar year |
| QT | Quaterly | 004 | 00 |  | No | From SAP standard | *1st Posting Period / Quarter = January - March<br>*2st Posting Period / Quarter = April - June<br>*3st Posting Period / Quarter = July - September<br>*4st Posting Period / Quarter = October - December |
| S3 | Apr-Mar,,4 Sp. Per,yr shift+1 | 012 | 04 |  | Yes | From SAP standard | *1st Posting Period = April<br>* For posting periods Apr-Dec, Fiscal year = Calendar year + 1<br>* For posting periods Jan-Mar, Fiscal year = Calendar year |
| S6 | Jul-Jun,4 Sp. Per,yr shift +1 | 012 | 04 |  | Yes | From SAP standard | It is similar to fiscal year variant V6 but with year shift;<br>*1st Posting Period = July<br>* For posting periods July-Dec, Fiscal year = Calendar year + 1<br>* For posting periods Jan-Jun, Fiscal year = Calendar year |
| SA (used in FI-AA) | Configurable template FI-AA US | 012 | 00 |  | No | From SAP standard | * Template variant ONLY for US customers in Asset Accounting. <br>* Freely configurable by customer, e.g. for "4-4-5" FYV. <br>* All settings must be completed by customer via SSC-UI in the Finetuning-Phase. No posting is allowed in the system until this step is done. |
| SZ | Configurable template variant | 012 | 00 | X | Yes | From SAP standard | * Template variant, freely configurable by customer, e.g. for "4-4-5" FYV.<br>* All settings except "Number of posting periods within Fiscal year" (currently only 12 periods are supported for corporate FYV) must be completed by customer via SSC-UI in the Finetuning-Phase. No posting is allowed in the system until this step is done. |
| V3 | Apr.- March, 4 special periods | 012 | 04 |  | Yes | From SAP standard | *1st Posting Period = April<br>* For posting periods Apr-Dec, Fiscal year = Calendar year <br>* For posting periods Jan-Mar, Fiscal year = Calendar year - 1 |
| V6 | July - June, 4 special periods | 012 | 04 |  | Yes | From SAP standard | *1st Posting Period = July<br>* For posting periods July-Dec, Fiscal year = Calendar year <br>* For posting periods Jan-Jun, Fiscal year = Calendar year - 1 |
| V9 | Oct.- Sept., 4 special periods | 012 | 04 |  | Yes | From SAP standard | *1st Posting Period = October<br>* For posting periods Oct-Dec, Fiscal year = Calendar year + 1<br>* For posting periods Jan-Sept, Fiscal year = Calendar year |
| Y4 (only for US) | AA:Cal. Yr, 4 Special Periods | 012 | 04 | X | No | Created by US Localization & FI-AA relevant | Similar to fiscal year variant K4 used in US solution for Asset Accounting only<br>Posting period = Calendar Month, Fiscal year = Calender year |
| G3 | Fiscal Year Variant for UK CIS | 012 | 00 |  | No | UK Withholding Tax | The Construction Industry Scheme for the UK requires the reporting periods to be from the 6th of one month to the 5th of the following month. |
| *** Special periods represent an extension of the last normal posting period. When the posting date falls within the last normal posting period, then during document entry you can specify that the transaction figures be updated separately in one of the special periods. |  |  |  |  |  |  |  |

### Sheet: Sheet2 (hidden)

Apr-Mar,24 P.,4.SP,yr shift+1

## Connections
- part-of :: [[_cluster]]
- see-also :: [[01-solution-foundation-and-platform/2608-org-data-overview-en-xx-121]]
- see-also :: [[03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_predelivered_FYV.xlsx` — full document · extracted with `xlsx2md` · 7,398 chars in the whole document
