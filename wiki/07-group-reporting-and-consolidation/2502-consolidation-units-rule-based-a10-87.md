---
id: 07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-a10-87
title: 2502 Consolidation Units Rule Based A10 (2502_Consolidation_Units_Rule_Based_A10)
description: SAP S/4HANA Cloud Public Edition consolidation unit master data upload template (version A10 Actuals) with 9 sample units and a hidden value-help sheet.
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-units-and-fs-item-mapping]
aliases: [2502_Consolidation_Units_Rule_Based_A10]
keywords: [Consolidation Units and FS Item Mapping, consolidation units, consolidation master data, master data upload, currency translation methods, consolidation versions, local currency, universal journal integration, fiscal year variants, upload methods]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_Consolidation_Units_Rule_Based_A10.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-87
topic: 07-group-reporting-and-consolidation/consolidation-units-and-fs-item-mapping
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2502 Consolidation Units Rule Based A10 (2502_Consolidation_Units_Rule_Based_A10)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_Consolidation_Units_Rule_Based_A10.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Units and FS Item Mapping** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2502 Consolidation Units Rule Based A10

### Sheet: Consolidation Unit

| Consolidation Unit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mandatory Filter Values |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FINCS_S_MD_XLSX_HD_UNIT_2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| *Consolidation Version (3) | *Effective Fiscal Year and Period (YYYY/PPP) | *Language (2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CONSOLIDATIONVERSION+CONSOLIDATIONVERSIONTEXT | FISCALYEARPERIOD | LANGUAGE+LANGUAGENAME |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| A10 -- Actuals | 2023/012 | EN -- English |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Master Data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FINCS_S_MD_XLSX_UNIT_2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| *Consolidation Unit (18) | Consolidation Unit Description (15) | Consolidation Unit Medium Description (30) | Consolidation Unit Long Description (60) | *Local Currency (5) | Company (6) | Country/Region (3) | Consolidation Unit is Partner Unit Only (1) | Currency Translation Method (5) | Tax Rate (8) | Deviating Fiscal Year Variant (2) | Universal Journal Integration (1) | Upload Method (5) | Data Collection Selection (30) | Posting Rule Selection (30) | Partner Selection (30) | Validation Selection (30) | Link Title (255) | Link URL (1333) |
| CONSOLIDATIONUNIT | CONSOLIDATIONUNITTEXT | CONSOLIDATIONUNITMDMTEXT | CONSOLIDATIONUNITLONGTEXT | CONSOLIDATIONUNITLOCALCURRENCY+CURRENCYNAME | COMPANY+COMPANYNAME | COUNTRY+COUNTRYNAME | CONSOLIDATIONUNITISPARTNERONLY+PARTNER_ONLY_TEXT | CNSLDTNCRCYTRANSLATIONMETHOD+CNSLDTNCRCYTRNSLTNMETHODTEXT | TAXRATE | FISCALYEARVARIANT+FISCALYEARVARIANTDESCRIPTION | CNSLDTNDATATRANSFERMETHOD+CNSLDTNDATATRANSFERMETHODTEXT | CNSLDTNUPLOADMETHOD+CNSLDTNUPLOADMETHODTEXT | CNSLDTNUNITDATACOLLECTION+CNSLDTNUNITDATACOLLECTIONTEXT | CONSOLIDATIONUNITPOSTINGRULE+CNSLDTNUNITPOSTINGRULETEXT | CONSOLIDATIONUNITPARTNER+CONSOLIDATIONUNITPARTNERTEXT | CONSOLIDATIONUNITVALIDATION+CNSLDTNUNITVALIDATIONTEXT | CONSOLIDATIONUNITLINKLABEL | CONSOLIDATIONUNITLINK |
| MXX00 | Germany | Germany |  | EUR -- European Euro |  | DE -- Germany |  | S0903 -- Standard translation Periodic | 35.0000 |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX02 | France | France |  | EUR -- European Euro |  | FR -- France |  | S0903 -- Standard translation Periodic | 39.0000 |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX03 | USA East | USA East |  | USD -- United States Dollar |  | US -- USA |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX04 | USA West | USA West |  | USD -- United States Dollar |  | US -- USA |  | S0904 -- Translation-FC@Incoming Unit |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX05 | Belgium | Belgium |  | EUR -- European Euro |  | BE -- Belgium |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX06 | Japan | Japan |  | JPY -- Japanese Yen |  | JP -- Japan |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX07 | Austria | Austria |  | EUR -- European Euro |  | AT -- Austria |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| MXX08 | China | China |  | CNY -- Chinese Yuan Renminbi |  | CN -- China |  | S0903 -- Standard translation Periodic |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |
| 999999 | Company 999999 | Company 999999 |  | EUR -- European Euro |  |  |  |  |  |  | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) |  |  |  |  |  |  |

### Sheet: valuehelpdata (hidden)

| valuehelpdata |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| valuehelpdata |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CONSOLIDATIONVERSION | LANGUAGE | COUNTRY | CNSLDTNDATATRANSFERMETHOD | CNSLDTNUPLOADMETHOD | CONSOLIDATIONUNITLOCALCURRENCY | COMPANY | CNSLDTNCRCYTRANSLATIONMETHOD | DOCUMENTENTRYISINGROUPCURRENCY | CNSLDTNUNITLOCALCRCYSOURCE | CNSLDTNUNITGROUPCRCYSOURCE | FISCALYEARVARIANT | CONSOLIDATIONUNITISPARTNERONLY | CNSLDTNUNITDATACOLLECTION | CONSOLIDATIONUNITPARTNER | CONSOLIDATIONUNITPOSTINGRULE | CONSOLIDATIONUNITVALIDATION |
| A10 -- Actuals | 1P -- Portuguese PT |  |  |  | AED -- United Arab Emirates Dirham |  |  |  |  |  |  |  |  |  |  |  |
| CC2 -- Budget (2022) | 1Q -- Technical code 1 | AD -- Andorra | H -- Transfer from Universal Journal | SRD1 -- FU Mthd (tab only for csv/txt) | AFN -- Afghani | 1010 -- Company 1010 | GD0 -- LC change no option | X -- Yes | B -- Freely Defined Currency 3 | B -- Freely Defined Currency 3 | 24 -- Half periods | X -- Yes | SPD1 -- Standard Package Definition | DD_P1_TEST -- DD Partner 1 Test | JV-QUOTED -- Joint venture - quoted | VALIDATE-K2 -- |
| CV1 -- Actuals | 2Q -- Technical code 2 | AE -- United Arab Emirates | U -- No Integration | SRD2 -- FU Mthd (; only for csv/txt) | ALL -- Albanian Lek | 1012 -- Company 1010 | GD1 -- LC change copy GC to LC | -- No | C -- Freely Defined Currency 4 | C -- Freely Defined Currency 4 | BM -- BI Monthly | -- No |  |  | JV-UNQUOTED -- Joint venture - unquoted | VALIDATE-KLS -- Validate Kls SEL |
| CV2 -- Actuals | 4G -- German CH | AF -- Afghanistan |  |  | AMD -- Armenian Dram | 1020 -- Company 1020 | GD2 -- LC change copy LC to GC |  | D -- Freely Defined Currency 5 | D -- Freely Defined Currency 5 | C1 -- 1st period (calendar year) |  |  |  |  |  |
| D10 -- Actuals | 6E -- English IN | AG -- Antigua and Barbuda |  |  | ANG -- Netherlands Antillean Guilder | 1090 -- Company 1090 | GD3 -- LC change keep GC |  | E -- Freely Defined Currency 6 | E -- Freely Defined Currency 6 | C2 -- Jul-Jun, 1 Per, yr shift |  |  |  |  |  |
| D11 -- Actuals | 6N -- English GB | AI -- Anguilla |  |  | AOA -- Angolanische Kwanza | 1110 -- Company 1110 | S0902 -- Translation-FC@First PeriodPer |  | F -- Freely Defined Currency 7 | F -- Freely Defined Currency 7 | C3 -- Jul-Jun, 2 Per, yr shift |  |  |  |  |  |
| GD0 -- LCC Std EUR | AR -- Arabic | AL -- Albania |  |  | ARS -- Argentine Peso | 1210 -- Company 1210 | S0903 -- Standard translation Periodic |  | G -- Freely Defined Currency 8 | G -- Freely Defined Currency 8 | DL -- Daily |  |  |  |  |  |
| GD1 -- RST Std EUR | BG -- Bulgarian | AM -- Armenia |  |  | AUD -- Australian Dollar | 1310 -- Company 1310 | S0904 -- Translation-FC@Incoming Unit |  | H -- Local Currency | H -- Local Currency | G3 -- Fiscal Year Variant for UK CIS |  |  |  |  |  |
| GD2 -- RST Ext(GD1) EUR | CA -- Catalan | AO -- Angola |  |  | AWG -- Aruban Florin | 1410 -- Company 1410 | S0905 -- Standard trans. Act. based COI |  | K -- Group Currency | K -- Group Currency | K0 -- Calendar year, 0 spec. period |  |  |  |  |  |
| GD3 -- RST GC Ext USD | CS -- Czech | AQ -- Antarctica |  |  | AZN -- Azerbaijan Manat | 1510 -- Company 1510 | S0906 -- Standard trans. Act. based-FC |  | O -- Freely Defined Currency 1 | O -- Freely Defined Currency 1 | K1 -- Cal. Year, 1 Special Period |  |  |  |  |  |
| GD4 -- RST Ext (GD3) USD | DA -- Danish | AR -- Argentina |  |  | BAM -- Bosnia and Herzegovina Convertible Mark | 1610 -- Company 1610 | S0907 -- S4 acct GC w/o retranslation |  | V -- Freely Defined Currency 2 | V -- Freely Defined Currency 2 | K2 -- Cal. Year, 2 Special Periods |  |  |  |  |  |
| GD5 -- RST Ext(GD1) EUR | DE -- German | AS -- American Samoa |  |  | BBD -- Barbados Dollar | 1710 -- Company 1710 | S9904 -- Translation-FC@Incoming Unit |  |  |  | K3 -- Cal. Year, 3 Special Periods |  |  |  |  |  |
| K10 -- Actuals | EL -- Greek | AT -- Austria |  |  | BDT -- Bangladesh Taka | 1790 -- Company 1790 | Y0901 -- Standard translation YTD |  |  |  | K4 -- Cal. Year, 4 Special Periods |  |  |  |  |  |
| K12 -- Actuals | EN -- English | AU -- Australia |  |  | BGN -- Bulgarian Lev | 1810 -- Company 1810 | Y0902 -- S4 Accounting GC |  |  |  | M3 -- AA Apr-Mar, 24 Per. |  |  |  |  |  |
| K20 -- Actuals | ES -- Spanish | AW -- Aruba |  |  | BHD -- Bahrain Dinar | 1910 -- Company 1910 | Y0903 -- Translation-S4 and Upload |  |  |  | M4 -- AA Cal. Year, 24 Per. |  |  |  |  |  |
| KL9 -- Actuals | ET -- Estonian | AX -- Aland Islands |  |  | BIF -- Burundi Franc | 2010 -- Company 2010 |  |  |  |  | M6 -- AA Jul-Jun, 24 Per. |  |  |  |  |  |
| Y10 -- Actuals | FI -- Finnish | AZ -- Azerbaijan |  |  | BMD -- Bermudan Dollar | 2110 -- Company 2110 |  |  |  |  | M9 -- AA Oct-Sep, 24 Per. |  |  |  |  |  |
| Y11 -- Actuals @ Budget rates | FR -- French | BA -- Bosnia and Herzegovina |  |  | BND -- Brunei Dollar | 2210 -- Company 2210 |  |  |  |  | N3 -- AA Apr-Mar,24 P.,yr shift+1 |  |  |  |  |  |
| Y12 -- Actuals @ Budget rates | HE -- Hebrew | BB -- Barbados |  |  | BOB -- Boliviano | 2310 -- Company 2310 |  |  |  |  | N6 -- AA Jul-Jun,24 P.,yr shift+1 |  |  |  |  |  |
| Y20 -- Actuals Version Y20 | HI -- Hindi | BD -- Bangladesh |  |  | BRL -- Brazilian Real | 2410 -- Company 2410 |  |  |  |  | Q4 -- Quaterly2 |  |  |  |  |  |
| YB2 -- Budget (2022) | HR -- Croatian | BE -- Belgium |  |  | BSD -- Bahaman Dollar | 2510 -- Company 2510 |  |  |  |  | QT -- Quaterly |  |  |  |  |  |
| YB3 -- Budget (2023) | HU -- Hungarian | BF -- Burkina Faso |  |  | BTN -- Bhutan Ngultrum | 2610 -- Company 2610 |  |  |  |  | S3 -- Apr-Mar,4 Sp. Per,yr shift +1 |  |  |  |  |  |
| YB4 -- Budget (2024) | ID -- Indonesian | BG -- Bulgaria |  |  | BWP -- Botswana Pula | 2710 -- Company 2710 |  |  |  |  | S6 -- Jul-Jun,4 Sp. Per,yr shift +1 |  |  |  |  |  |
| YF1 -- Forecast 1+11 | IS -- Icelandic | BH -- Bahrain |  |  | BYN -- Belarusian Ruble | 2810 -- Company 2810 |  |  |  |  | SA -- Configurable template FI-AA US |  |  |  |  |  |
| YF2 -- Forecast 2+10 | IT -- Italian | BI -- Burundi |  |  | BYR -- Belorussian Ruble | 2910 -- Company 2910 |  |  |  |  | SZ -- Configurable template variant |  |  |  |  |  |
| YP1 -- Predictive Accounting | JA -- Japanese | BJ -- Benin |  |  | BZD -- Belize Dollar | 3010 -- Company 3010 |  |  |  |  | V3 -- Apr.- March, 4 special periods |  |  |  |  |  |
| Z10 -- Actuals | KK -- Kazakh | BL -- Saint Barthelemy |  |  | CAD -- Canadian Dollar | 3110 -- Company 3110 |  |  |  |  | V6 -- July - June, 4 special periods |  |  |  |  |  |
| Z12 -- Actuals | KO -- Korean | BM -- Bermuda |  |  | CDF -- Congolese Franc | 3210 -- Company 3210 |  |  |  |  | V9 -- Oct.- Sept., 4 special periods |  |  |  |  |  |
| Z20 -- Actuals | LT -- Lithuanian | BN -- Brunei Darussalam |  |  | CHF -- Swiss Franc | 3310 -- Company 3310 |  |  |  |  |  |  |  |  |  |  |
| Z22 -- Actuals | LV -- Latvian | BO -- Bolivia |  |  | CLF -- Chile Unidad de Fomento | 3410 -- Company 3410 |  |  |  |  |  |  |  |  |  |  |
| ZA1 -- Actuals @ Budget rates | MS -- Malay | BQ -- Bonaire, Sint Eustatius and Saba |  |  | CLP -- Chilean Peso | 3510 -- Company 3510 |  |  |  |  |  |  |  |  |  |  |
| ZB2 -- Budget (2016) | NL -- Dutch | BR -- Brazil |  |  | CNY -- Chinese Yuan Renminbi | 3610 -- Company 3610 |  |  |  |  |  |  |  |  |  |  |
| ZB3 -- Budget (2023) | NO -- Norwegian | BS -- Bahamas |  |  | COP -- Colombian Peso | 3710 -- Company 3710 (NL) |  |  |  |  |  |  |  |  |  |  |
| ZD1 -- Actuals | PL -- Polish | BT -- Bhutan |  |  | CRC -- Costa Rica Colon | 3810 -- Company 3810 |  |  |  |  |  |  |  |  |  |  |
| ZD2 -- Actuals | PT -- Portuguese | BV -- Bouvet Islands |  |  | CUC -- Peso Convertible | 3910 -- Company 3910 |  |  |  |  |  |  |  |  |  |  |
| ZD3 -- Actuals | RO -- Romanian | BW -- Botswana |  |  | CUP -- Cuban Peso | 4010 -- Company 4010 |  |  |  |  |  |  |  |  |  |  |
| ZD4 -- Actuals | RU -- Russian | BY -- Belarus |  |  | CVE -- Cape Verde Escudo | 4210 -- Company 4210 |  |  |  |  |  |  |  |  |  |  |
| ZD5 -- Actuals | SH -- Serbian (Latin) | BZ -- Belize |  |  | CZK -- Czech Krona | 4310 -- Company 4310 |  |  |  |  |  |  |  |  |  |  |
| ZD6 -- Actuals | SK -- Slovak | CA -- Canada |  |  | DJF -- Djibouti Franc | 4410 -- Company 4410 |  |  |  |  |  |  |  |  |  |  |
| ZF2 -- Forecast 2+10 | SL -- Slovenian | CC -- Cocos (Keeling) Islands |  |  | DKK -- Danish Krone | 4510 -- Company 4510 |  |  |  |  |  |  |  |  |  |  |
| ZI1 -- Actuals | SQ -- Albanian | CD -- Democratic Republic of the Congo |  |  | DOP -- Dominican Peso | 4610 -- Company 4610 |  |  |  |  |  |  |  |  |  |  |
| ZI2 -- Actuals | SR -- Serbian | CF -- Central African Republic |  |  | DZD -- Algerian Dinar | 4810 -- Company 4810 |  |  |  |  |  |  |  |  |  |  |
| ZIC -- Actuals | SV -- Swedish | CG -- Republic of the Congo |  |  | EGP -- Egyptian Pound | 5110 -- Company 5110 |  |  |  |  |  |  |  |  |  |  |
| ZK1 -- Actuals | TH -- Thai | CH -- Switzerland |  |  | ERN -- Eritrean Nafka | 5410 -- Company 5410 |  |  |  |  |  |  |  |  |  |  |
| ZKA -- Actuals | TR -- Turkish | CI -- Cote d'Ivoire |  |  | ETB -- Ethiopian Birr | 5510 -- Company 5510 - Mexico |  |  |  |  |  |  |  |  |  |  |
| ZKB -- Actuals | UK -- Ukrainian | CK -- Cook Islands |  |  | EUR -- European Euro | 5710 -- Company 5710 |  |  |  |  |  |  |  |  |  |  |
| ZKC -- Actuals | VI -- Vietnamese | CL -- Chile |  |  | FJD -- Fiji Dollar | 5810 -- Company 5810 |  |  |  |  |  |  |  |  |  |  |
| ZKD -- Actuals | Z1 -- Customer reserve | CM -- Cameroon |  |  | FKP -- Falkland Pound | 5910 -- Company 5910 |  |  |  |  |  |  |  |  |  |  |
| ZKE -- Actuals | ZF -- Chinese trad. | CN -- China |  |  | GBP -- British Pound | 6110 -- Company 6110 |  |  |  |  |  |  |  |  |  |  |
| ZKF -- Actuals | ZH -- Chinese | CO -- Colombia |  |  | GEL -- Georgian Lari | 6210 -- Company 6210 |  |  |  |  |  |  |  |  |  |  |
| ZMH -- Actuals |  | CR -- Costa Rica |  |  | GHS -- Ghanian Cedi | 6310 -- Company 6310 |  |  |  |  |  |  |  |  |  |  |
| ZMI -- Actuals |  | CU -- Cuba |  |  | GIP -- Gibraltar Pound | 6410 -- Company 6410 |  |  |  |  |  |  |  |  |  |  |
|  |  | CV -- Cabo Verde |  |  | GMD -- Gambian Dalasi | 6510 -- Company 6510 |  |  |  |  |  |  |  |  |  |  |
|  |  | CW -- Curaçao |  |  | GNF -- Guinean Franc | 6610 -- Company 6610 |  |  |  |  |  |  |  |  |  |  |
|  |  | CX -- Christmas Island |  |  | GTQ -- Guatemalan Quetzal | 6810 -- Company 6810 |  |  |  |  |  |  |  |  |  |  |
|  |  | CY -- Cyprus |  |  | GYD -- Guyana Dollar | 6910 -- Company 6910 |  |  |  |  |  |  |  |  |  |  |
|  |  | CZ -- Czech Republic |  |  | HKD -- Hong Kong Dollar | 7210 -- Company 7210 |  |  |  |  |  |  |  |  |  |  |
|  |  | DE -- Germany |  |  | HNL -- Honduran Lempira | 7510 -- Company 7510 |  |  |  |  |  |  |  |  |  |  |
|  |  | DJ -- Djibouti |  |  | HRK -- Croatian Kuna | 8210 -- Company 8210 |  |  |  |  |  |  |  |  |  |  |
|  |  | DK -- Denmark |  |  | HTG -- Haitian Gourde | 8810 -- Company 8810 |  |  |  |  |  |  |  |  |  |  |
|  |  | DM -- Dominica |  |  | HUF -- Hungarian Forint | 9010 -- Company 9010 |  |  |  |  |  |  |  |  |  |  |
|  |  | DO -- Dominican Republic |  |  | IDR -- Indonesian Rupiah | 9110 -- Company 9110 |  |  |  |  |  |  |  |  |  |  |
|  |  | DZ -- Algeria |  |  | ILS -- Israeli Shekel | 9510 -- Company 9510 |  |  |  |  |  |  |  |  |  |  |
|  |  | EC -- Ecuador |  |  | INR -- Indian Rupee | 9710 -- Company 9710 |  |  |  |  |  |  |  |  |  |  |
|  |  | EE -- Estonia |  |  | IQD -- Iraqui Dinar | 6D10 -- Company 6D10 |  |  |  |  |  |  |  |  |  |  |
|  |  | EG -- Egypt |  |  | IRR -- Iranian Rial | 6J10 -- Company 6J10 |  |  |  |  |  |  |  |  |  |  |
|  |  | EH -- West Sahara |  |  | ISK -- Iceland Krona | 6K10 -- Company 6K10 |  |  |  |  |  |  |  |  |  |  |
|  |  | ER -- Eritrea |  |  | JMD -- Jamaican Dollar | 6L10 -- Company 6L10 |  |  |  |  |  |  |  |  |  |  |
|  |  | ES -- Spain |  |  | JOD -- Jordanian Dinar | 6M10 -- Company 6M10 |  |  |  |  |  |  |  |  |  |  |
|  |  | ET -- Ethiopia |  |  | JPY -- Japanese Yen | 6N10 -- Company 6N10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FI -- Finland |  |  | KES -- Kenyan Shilling | 7J10 -- Company 7J10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FJ -- Fiji |  |  | KGS -- Kyrgyzstan Som | 7K10 -- Company 7K10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FK -- Falkland Islands |  |  | KHR -- Cambodian Riel | 7N10 -- Company 7N10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FM -- Federated States of Micronesia |  |  | KMF -- Comoros Franc | 7P10 -- Company 7P10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FO -- Faroe Islands |  |  | KPW -- North Korean Won | 7Q10 -- Company 7Q10 |  |  |  |  |  |  |  |  |  |  |
|  |  | FR -- France |  |  | KRW -- South Korean Won | 7Y10 -- Company 7Y10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GA -- Gabon |  |  | KWD -- Kuwaiti Dinar | 8E10 -- Company 8E10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GB -- United Kingdom |  |  | KYD -- Cayman Dollar | 8G10 -- Company 8G10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GD -- Grenada |  |  | KZT -- Kazakstanian Tenge | 8H10 -- Company 8H10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GE -- Georgia |  |  | LAK -- Laotian Kip | 8I10 -- Company 8I10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GF -- French Guyana |  |  | LBP -- Lebanese Pound | 8V10 -- Company 8V10 |  |  |  |  |  |  |  |  |  |  |
|  |  | GG -- Guernsey |  |  | LKR -- Sri Lankan Rupee | DE00 -- Company 1010 |  |  |  |  |  |  |  |  |  |  |
|  |  | GH -- Ghana |  |  | LRD -- Liberian Dollar | FI00 -- Company 4510 |  |  |  |  |  |  |  |  |  |  |
|  |  | GI -- Gibraltar |  |  | LSL -- Lesotho Loti | FR00 -- Company 1210 |  |  |  |  |  |  |  |  |  |  |
|  |  | GL -- Greenland |  |  | LYD -- Libyan Dinar | FR10 -- Company 1210 |  |  |  |  |  |  |  |  |  |  |
|  |  | GM -- Gambia |  |  | MAD -- Moroccan Dirham | RU00 -- Company 1610 |  |  |  |  |  |  |  |  |  |  |
|  |  | GN -- Guinea |  |  | MDL -- Moldavian Leu | RU10 -- Company 1610 |  |  |  |  |  |  |  |  |  |  |
|  |  | GP -- Guadeloupe |  |  | MGA -- Madagascan Ariary |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GQ -- Equatorial Guinea |  |  | MKD -- Macedonian Denar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GR -- Greece |  |  | MMK -- Myanmar Kyat |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GS -- South Georgia and the Southern Sandwich Islands |  |  | MNT -- Mongolian Tugrik |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GT -- Guatemala |  |  | MOP -- Macao Pataca |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GU -- Guam |  |  | MRO -- Mauritanian Ouguiya |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GW -- Guinea-Bissau |  |  | MRU -- Mauritanian Ouguiya |  |  |  |  |  |  |  |  |  |  |  |
|  |  | GY -- Guyana |  |  | MUR -- Mauritian Rupee |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HK -- Hong Kong |  |  | MVR -- Maldive Rufiyaa |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HM -- Heard and McDonald Islands |  |  | MWK -- Malawi Kwacha |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HN -- Honduras |  |  | MXN -- Mexican Pesos |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HR -- Croatia |  |  | MXV -- Mexic Unidad de Inversión |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HT -- Haiti |  |  | MYR -- Malaysian Ringgit |  |  |  |  |  |  |  |  |  |  |  |
|  |  | HU -- Hungary |  |  | MZN -- Mozambique Metical |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ID -- Indonesia |  |  | NAD -- Namibian Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IE -- Ireland |  |  | NGN -- Nigerian Naira |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IL -- Israel |  |  | NIO -- Nicaraguan Cordoba Oro |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IM -- Isle of Man |  |  | NOK -- Norwegian Krone |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IN -- India |  |  | NPR -- Nepalese Rupee |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IO -- British Indian Ocean Territory |  |  | NZD -- New Zealand Dollars |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IQ -- Iraq |  |  | OMR -- Omani Rial |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IR -- Iran |  |  | PAB -- Panamanian Balboa |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IS -- Iceland |  |  | PEN -- Peruvian New Sol |  |  |  |  |  |  |  |  |  |  |  |
|  |  | IT -- Italy |  |  | PGK -- Papua New Guinea Kina |  |  |  |  |  |  |  |  |  |  |  |
|  |  | JE -- Jersey |  |  | PHP -- Philippine Peso |  |  |  |  |  |  |  |  |  |  |  |
|  |  | JM -- Jamaica |  |  | PKR -- Pakistani Rupee |  |  |  |  |  |  |  |  |  |  |  |
|  |  | JO -- Jordan |  |  | PLN -- Polish Zloty |  |  |  |  |  |  |  |  |  |  |  |
|  |  | JP -- Japan |  |  | PYG -- Paraguayan Guarani |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KE -- Kenya |  |  | QAR -- Qatar Rial |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KG -- Kyrgyzstan |  |  | RON -- Romanian Leu |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KH -- Cambodia |  |  | RSD -- Serbian Dinar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KI -- Kiribati |  |  | RUB -- Russian Ruble |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KM -- Comoros |  |  | RWF -- Rwandan Franc |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KN -- Saint Kitts and Nevis |  |  | SAR -- Saudi Riyal |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KP -- North Korea |  |  | SBD -- Solomon Islands Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KR -- South Korea |  |  | SCR -- Seychelles Rupee |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KW -- Kuwait |  |  | SDG -- Sudanese Pound |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KY -- Cayman Islands |  |  | SEK -- Swedish Krona |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KZ -- Kazakhstan |  |  | SGD -- Singapore Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LA -- Laos |  |  | SHP -- St.Helena Pound |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LB -- Lebanon |  |  | SLE -- Sierra Leone Leone |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LC -- St. Lucia |  |  | SLL -- Sierra Leone Leone |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LI -- Liechtenstein |  |  | SOS -- Somalian Shilling |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LK -- Sri Lanka |  |  | SRD -- Surinam Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LR -- Liberia |  |  | SSP -- South Sudanese Pound |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LS -- Lesotho |  |  | STN -- Sao Tome / Principe Dobra |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LT -- Lithuania |  |  | SVC -- El Salvador Colon |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LU -- Luxembourg |  |  | SYP -- Syrian Pound |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LV -- Latvia |  |  | SZL -- Swaziland Lilangeni |  |  |  |  |  |  |  |  |  |  |  |
|  |  | LY -- Libya |  |  | THB -- Thailand Baht |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MA -- Morocco |  |  | TJS -- Tajikistani Somoni |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MC -- Monaco |  |  | TMT -- Turkmenistani Manat |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MD -- Moldova |  |  | TND -- Tunisian Dinar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ME -- Montenegro |  |  | TOP -- Tongan Pa'anga |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MF -- Saint Martin |  |  | TRY -- Turkish Lira |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MG -- Madagascar |  |  | TTD -- Trinidad and Tobago Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MH -- Marshall Islands |  |  | TWD -- New Taiwan Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MK -- Republic of North Macedonia |  |  | TZS -- Tanzanian Shilling |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ML -- Mali |  |  | UAH -- Ukraine Hryvnia |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MM -- Myanmar |  |  | UGX -- Ugandan Shilling |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MN -- Mongolia |  |  | USD -- United States Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MO -- Macao |  |  | UYU -- Uruguayan Peso |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MP -- North Mariana Islands |  |  | UZS -- Uzbekistan Som |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MQ -- Martinique |  |  | VEF -- Venezuelan Bolivar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MR -- Mauretania |  |  | VES -- Bolivar Soberano |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MS -- Montserrat |  |  | VND -- Vietnamese Dong |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MT -- Malta |  |  | VUV -- Vanuatu Vatu |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MU -- Mauritius |  |  | WST -- Samoan Tala |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MV -- Maldives |  |  | XAF -- Gabon CFA Franc BEAC |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MW -- Malawi |  |  | XCD -- East Carribean Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MX -- Mexico |  |  | XOF -- Benin CFA Franc BCEAO |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MY -- Malaysia |  |  | XPF -- CFP Franc |  |  |  |  |  |  |  |  |  |  |  |
|  |  | MZ -- Mozambique |  |  | YER -- Yemeni Ryal |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NA -- Namibia |  |  | ZAR -- South African Rand |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NC -- New Caledonia |  |  | ZMW -- Zambian Kwacha |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NE -- Niger |  |  | ZWL -- Zimbabwean Dollar |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NF -- Norfolk Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NG -- Nigeria |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NI -- Nicaragua |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NL -- Netherlands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NO -- Norway |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NP -- Nepal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NR -- Nauru |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NU -- Niue |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | NZ -- New Zealand |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | OM -- Oman |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PA -- Panama |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PE -- Peru |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PF -- French Polynesia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PG -- Papua New Guinea |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PH -- Philippines |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PK -- Pakistan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PL -- Poland |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PM -- St. Pierre and Miquelon |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PN -- Pitcairn Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PR -- Puerto Rico |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PS -- State of Palestine |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PT -- Portugal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PW -- Palau |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | PY -- Paraguay |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | QA -- Qatar |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RE -- Reunion |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RO -- Romania |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RS -- Serbia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RU -- Russian Federation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RW -- Rwanda |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SA -- Saudi Arabia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SB -- Solomon Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SC -- Seychelles |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SD -- Sudan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SE -- Sweden |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SG -- Singapore |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SH -- Saint Helena |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SI -- Slovenia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SJ -- Svalbard |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SK -- Slovakia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SL -- Sierra Leone |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SM -- San Marino |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SN -- Senegal |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SO -- Somalia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SR -- Suriname |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SS -- Republic of South Sudan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ST -- Sao Tome and Principe |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SV -- El Salvador |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SX -- Sint Maarten (Dutch part) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SY -- Syria |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | SZ -- The Kingdom of Eswatini |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TC -- Turks and Caicos Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TD -- Chad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TF -- French Southern Territories |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TG -- Togo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TH -- Thailand |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TJ -- Tajikistan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TK -- Tokelau Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TL -- Timor-Leste |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TM -- Turkmenistan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TN -- Tunisia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TO -- Tonga |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TR -- Turkey |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TT -- Trinidad and Tobago |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TV -- Tuvalu |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TW -- Taiwan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | TZ -- Tanzania |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | UA -- Ukraine |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | UG -- Uganda |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | UM -- American Minor Outlying Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | US -- USA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | UY -- Uruguay |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | UZ -- Uzbekistan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VA -- Vatican City |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VC -- St. Vincent and the Grenadines |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VE -- Venezuela |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VG -- British Virgin Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VI -- American Virgin Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VN -- Vietnam |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | VU -- Vanuatu |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | WF -- Wallis and Futuna Islands |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | WS -- Samoa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | YE -- Yemen |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | YT -- Mayotte |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ZA -- South Africa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ZM -- Zambia |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ZW -- Zimbabwe |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-j10-88]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-j1s-89]]
- related-to :: [[07-group-reporting-and-consolidation/2502-consolidation-units-rule-based-mc-90]]
- related-to :: [[07-group-reporting-and-consolidation/2602-template-financial-statement-item-mapping-109]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_Consolidation_Units_Rule_Based_A10.xlsx` — full document · extracted with `xlsx2md` · 31,199 chars in the whole document
