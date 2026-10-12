---
id: 03-financial-accounting-and-close/journal-entry-template-78i-194
title: Journal Entry Template 78I (JournalEntry_Template_78I)
description: Excel upload template for general journal entries (sheet Data) with header and line-item field layout and eight sample intercompany loan entries for company codes 1710 and 17US.
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/general-journal-entry-upload]
aliases: [JournalEntry_Template_78I]
keywords: [General Journal Entry Upload Template, journal entry upload, journal entries, upload templates, intercompany loans, profitability segment fields, company codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/JournalEntry_Template_78I.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-194
topic: 03-financial-accounting-and-close/general-journal-entry-upload
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Journal Entry Template 78I (JournalEntry_Template_78I)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/JournalEntry_Template_78I.xlsx`, extracted with `xlsx2md`. Grouped under **General Journal Entry Upload Template** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## Journal Entry Template 78I

### Sheet: Data

| Upload General Journal Entry |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| // To add field columns to the template, please add technical names. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| // For a complete list of field columns and their technical names, choose ? in the right upper corner of the app screen and then view the Browse entry of web assistance. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| // If you want to add more Profitability Segment (CO-PA) fields, make sure that you add the 'PROF_' prefix in the technical names of the CO-PA fields. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Batch ID |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1710 | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Rec 1710 XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 1710 | 16020100 | ICMR_BD_XXXX | 100000 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
|  | 1710 | 16010100 | ICMR_BD_XXXX |  | 100000 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
| 2 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1710 | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Pay 1710 XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 1710 | 26200500 | ICMR_BD_XXXX |  | 200000 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
|  | 1710 | 16010100 | ICMR_BD_XXXX | 200000 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
| 3 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 17US | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Rec 17US XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 17US | 26200500 | ICMR_BD_XXXX |  | 100000 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
|  | 17US | 16010100 | ICMR_BD_XXXX | 100000 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
| 4 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 17US | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Pay 17US XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 17US | 16020100 | ICMR_BD_XXXX | 200003 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
|  | 17US | 16010100 | ICMR_BD_XXXX |  | 200003 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | DE | 01 | FINANCE01 | CRE-409722 | NY1925 |
| 5 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1710 | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Rec 1710 XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 1710 | 16020100 | ICMR_BD_XXXX | 300000 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
|  | 1710 | 16010100 | ICMR_BD_XXXX |  | 300000 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
| 6 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1710 | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Pay 1710 XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 1710 | 26200500 | ICMR_BD_XXXX |  | 400000 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
|  | 1710 | 16010100 | ICMR_BD_XXXX | 400000 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 17US |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
| 7 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 17US | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Rec 17US XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 17US | 26200500 | ICMR_BD_XXXX |  | 300040 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
|  | 17US | 16010100 | ICMR_BD_XXXX | 300040 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
| 8 | Header |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | BLART | BLDAT | BUDAT | MONAT | BKTXT | WAERS | LDGRP | KURSF_EXT | WWERT | XBLNR | PARGB_HDR | FULFILLDATE | XMWST |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | *Company Code (4) | *Journal Entry Type (2) | *Journal Entry Date | *Posting Date | Fiscal period (2) | Document Header Text (25) | *Transaction Currency (5) | Ledger Group (4) | Exchange Rate (12) | Currency Translation Date | Reference Document Number (16) | Partner Business Area (4) | Tax Fulfillment Date | Calculate Tax Automatically (1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 17US | AB | DD/MM/YYYY | DD/MM/YYYY |  | ICMR Loan Pay 17US XXXX | USD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Transaction Currency |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | BUKRS | HKONT | SGTXT | WRSOL | WRHAB | DMBTR | DMBE2 | MWSKZ | TXJCD | KOSTL | PRCTR | AUFNR | PS_POSID | VALUT | HBKID | HKTID | ZUONR | VBUND | SEGMENT | PROF_KNDNR | PROF_ARTNR | PROF_KUNRE | BRSCH | LAND1 | KDGRP | DATASOURCE_ID | FS_PRODUCT_GROUP | BRANCH_ID |
|  | Company Code (4) | G/L Account (10) | Item Text (50) | Debit | Credit | Amount in Company Code Currency | Amount in second local currency (LC2) | Tax Code (2) | Tax Jurisdiction (15) | Cost Center (10) | Profit Center (10) | Order Number (12) | WBS Element (24) | Value Date | House Bank (5) | House Bank Account (5) | Assignment number (18) | Trading Partner (6) | Segment for Segmental Reporting (10) | Customer (10) | Product number (40) | Bill-to Party (10) | Industry key (4) | Country/Region Key (3) | Customer Group (2) | Data Source (10) | Product Group (Financial Services) (10) | Branch (Financial Services) (10) |
|  | 17US | 16020100 | ICMR_BD_XXXX | 400100 |  |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |
|  | 17US | 16010100 | ICMR_BD_XXXX |  | 400100 |  |  |  |  |  | Y9000 |  |  |  |  |  |  | 1710 |  |  |  |  | 63 | US | 02 | FINANCE01 | CRE-409722 | NY1925 |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/2402-journal-entry-template-xxxx-pu1010-75]]
- related-to :: [[03-financial-accounting-and-close/2502-journal-entry-template-xxxx-pu1010-91]]
- related-to :: [[03-financial-accounting-and-close/2508-journal-entry-template-xxxx-pu1010-98]]
- related-to :: [[03-financial-accounting-and-close/2608-journal-entry-template-xxxx-pu1010-115]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/JournalEntry_Template_78I.xlsx` — full document · extracted with `xlsx2md` · 18,938 chars in the whole document
