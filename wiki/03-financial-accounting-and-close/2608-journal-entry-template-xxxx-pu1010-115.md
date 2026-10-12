---
id: 03-financial-accounting-and-close/2608-journal-entry-template-xxxx-pu1010-115
title: 2608 Journal Entry Template XXXX PU1010 (2608_Journal_Entry_Template_XXXX_PU1010)
description: "2608 'Upload General Journal Entry' spreadsheet template for company code XXXX: header and line-item field layout plus 10 sample G/L postings dated 2025-11-21."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/general-journal-entry-upload]
aliases: [2608_Journal_Entry_Template_XXXX_PU1010]
keywords: [General Journal Entry Upload Template, journal entry upload, journal entry template, journal entry header, journal entry line items, sample posting data, general ledger accounts, cost center, profit center, house bank]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Journal_Entry_Template_XXXX_PU1010.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-115
topic: 03-financial-accounting-and-close/general-journal-entry-upload
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 Journal Entry Template XXXX PU1010 (2608_Journal_Entry_Template_XXXX_PU1010)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Journal_Entry_Template_XXXX_PU1010.xlsx`, extracted with `xlsx2md`. Grouped under **General Journal Entry Upload Template** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 Journal Entry Template XXXX PU1010

### Sheet: Data

| Upload General Journal Entry |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Batch ID |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Unbilled Revenue | 1000 |  |  |  |  |  | XXXX1101 | YB700 |  |  |  |  |  | 202010 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 1000 |  |  |  |  | XXXX1101 | YB700 |  |  |  | THB01 | SAT11 | 202010 |  | 1000_C |  | 915 |  |  |  |
| 2 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Unbilled Revenue | 900 |  |  |  |  |  | XXXX1101 | YB700 |  |  |  |  |  | 202020 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 900 |  |  |  |  | XXXX1101 | YB700 |  |  |  | THB01 | SAT11 | 202020 |  | 1000_C |  | 915 |  |  |  |
| 3 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Unbilled Revenue | 1400 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202030 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 1400 |  |  |  |  | XXXX1101 |  |  |  |  | THB01 | SAT11 | 202030 |  | 1000_C |  | 915 |  |  |  |
| 4 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Unbilled Revenue | 400 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  |  | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 400 |  |  |  |  | XXXX1101 |  |  |  |  | THB01 | SAT11 |  |  | 1000_C |  | 915 |  |  |  |
| 5 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Unbilled Revenue | 1000 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202050 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 1000 |  |  |  |  | XXXX1101 |  |  |  |  | THB01 | SAT11 | 202050 |  | 1000_C |  | 915 |  |  |  |
| 6 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 31000000 | Common Stock | 1000 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  |  | 1010 | 1000_C |  | 950 |  |  |  |
|  | XXXX | 33000000 | Retained Earnings |  | 1000 |  |  |  |  | XXXX1101 |  |  |  |  |  |  |  |  | 1000_C |  | 920 |  |  |  |
| 7 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12401100 | Allowance for Doubtful Receivables | 1000 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  |  |  | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 1000 |  |  |  |  | XXXX1101 |  |  |  |  | THB01 | SAT11 |  |  | 1000_C |  | 915 |  |  |  |
| 8 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 12550000 | Allowance for Doubtful Receivables | 500 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  |  |  | 1000_A |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 500 |  |  |  |  | XXXX1101 |  |  |  |  | THB01 | SAT11 |  |  | 1000_A |  | 915 |  |  |  |
| 9 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 71100000 | Interest Expense | 800 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202060 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 800 |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202060 |  | 1000_C |  | 915 |  |  |  |
| 10 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal Period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | XXXX | AB | 2025-11-21 | 2025-11-21 | 11 | Integration-GL | USD | 0L |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | FKBER | RMVCT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment Number (18) | Trading Partner (6) | Segment | Function Area | Transaction type | Customer (10) | Product number (40) | Bill-to Party (10) |
|  | XXXX | 71800000 | Other Extra.Expense | 900 |  |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202070 | 1010 | 1000_C |  | 915 |  |  |  |
|  | XXXX | 10010000 | Petty Cash |  | 900 |  |  |  |  | XXXX1101 |  |  |  |  |  |  | 202070 |  | 1000_C |  | 915 |  |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/2402-journal-entry-template-xxxx-pu1010-75]]
- related-to :: [[03-financial-accounting-and-close/2502-journal-entry-template-xxxx-pu1010-91]]
- related-to :: [[03-financial-accounting-and-close/2508-journal-entry-template-xxxx-pu1010-98]]
- related-to :: [[03-financial-accounting-and-close/journal-entry-template-40y-193]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Journal_Entry_Template_XXXX_PU1010.xlsx` — full document · extracted with `xlsx2md` · 18,678 chars in the whole document
