---
id: 04-tax-and-statutory-reporting/2608-pre-configured-tax-codes-en-ae-702
title: 2608 Pre configured Tax Codes EN AE (2608_Pre-configured_Tax_Codes_EN_AE)
description: "Pre-delivered United Arab Emirates (AE) VAT tax codes in S/4HANA Cloud content 2608: rates, EU codes, and tax box/tax group mappings, plus glossary of tax terms."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/uae-tax-codes]
aliases: [2608_Pre-configured_Tax_Codes_EN_AE]
keywords: [Preconfigured UAE VAT Tax Codes, tax codes, uae vat, time-dependent tax rates, tax box mapping, tax groups, reverse charge, eu codes, tax condition types, input and output tax]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Setup/2608_Pre-configured_Tax_Codes_EN_AE.xlsx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-702
topic: 04-tax-and-statutory-reporting/uae-tax-codes
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 Pre configured Tax Codes EN AE (2608_Pre-configured_Tax_Codes_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Setup/2608_Pre-configured_Tax_Codes_EN_AE.xlsx`, extracted with `xlsx2md`. Grouped under **Preconfigured UAE VAT Tax Codes** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 Pre configured Tax Codes EN AE

### Sheet: About

| Pre-delivered Tax codes in SAP S/4 HANA Cloud Content |  |
| --- | --- |
| Version | 2608 |
| Usage of this document | This document gives you an overview about the country/region specific tax codes pre-delivered in S/4 HANA Content, incl. main parameters and mapping information to Tax boxes (if relevant for your country/region). |
| Worksheets description | Based on the country-specific SAP standard Tax content for your country, you will see different tabs in this document:<br>- "Technical About": technical parameters of the generation program. Please ignore this tab. <br>- "Tax codes": List of pre-delivered tax codes<br>Following tabs are only available for countries with active Time-Dependent Taxes:<br>- "Time Dependent Tax Rates": Pre-delivered time-dependent tax rates<br>- "T1_Mapping Tax Group-Tax Codes" (for countries with simple Tax Box Mapping: DE, IT, NZ, ZA): Pre-delivered content for tax groups - tax codes Mapping<br>- "T1_Mapping Tax Box - Tax Group" (for countries with simple Tax Box Mapping: DE, IT, NZ, ZA): Pre-delivered content for tax boxes - tax groups Mapping<br>- "T2_Mapping Tax Group-Tax Code" (for countries with enhanced Tax Box Mapping): Pre-delivered content for tax groups - tax codes Mapping<br>- "T2_Mapping Tax Box - Tax Group" (for countries with enhanced Tax Box Mapping): Pre-delivered content for tax boxes - tax groups Mapping |
| Description SAP technical terms |  |
| Tax Type | Indicator for differentiating output tax (A) and input tax (V). |
| EU Code | The European Union code (EU code) is used primarily for classifying tax codes that are considered in the EC sales list. It has come to be used for other purposes as well.<br>Possible entries:<br><empty> - Non-EU-Relevant<br>1 - Delivery of Goods Within the EU<br>2 - Services Within the EU<br>3 - Subcontracting Within the EU<br>4 - Output Tax for Services Within the EU<br>5 - Reverse Charge EU: Service with Tax with Zero Balance<br>6 - HU: Triungular Deal with County Outside the EU<br>7 - As for value "1", but tax balance zero<br>8 - As for value "3", but tax balance zero<br>9 - Acquisition Tax or General Tax with Zero Balance<br>A - Reverse Charge with Tax with Zero Balance<br>M - EU Goods Delivery - After Tax-Exempt Import<br>H - EU Goods Delivery - After Tax-Exempt Import by Fiscal Agent<br>B - Non-EU-Relevant, No Check on Input Tax Acct/Output Tax Acct<br>T - Non-EU-Relevant Exempt Output Tax for Goods<br>U - Non-EU-Relevant Exempt Output Tax for Services<br>R - Romania: Output Tax with Tax 0 for Farmers EU<br>C - Transport to Consignment Store Within the EU<br>D - Delivery from Consignment Store Within the EU |
| Error Indicator | Indicator which determines that an error message should be issued if the tax amount is not correct. If the indicator is not set, a warning message appears in place of the error message.<br>The system checks in the case of tax entered manually, whether the amount is correct within the document. Per tax code, the correct tax is calculated by means of the base amount and the percentage rate. In the case of a deviation of more than one currency unit per line item, an error message is issued. |
| Transaction key | The transaction keys are used to determine accounts or posting keys for line items which are created automatically by the system. You can find a description of all tax related transaction key in the account determintion documentation: https://help.sap.com/viewer/S4CLD_COA_Documentation |
| Condition type - MWVS | The condition type is used for Input Tax.<br>Condition type MWVS is connected to Transaction key VST. |
| Condition type - MWAS | The condition type is used for Output Tax.<br>Condition type MWAS is connected to Transaction key MWS. |
| Condition type - MWVN | The condition type is used for Non-deductable Input Tax. <br>Condition type MWVN is connected to Transaction key NAV. |
| Condition type - MWVZ | The condition type is used for Non-deductable Input Tax. <br>Condition type MWVN is connected to Transaction key NVV. |
| Condition type - NLXA | The condition type is used for Acquisition Tax Cred. <br>Condition type NLXA is connected to Transaction key ESA. |
| Condition type - NLXV | The condition type is used for Acquisition Tax Deb. <br>Condition type NLXV is connected to Transaction key ESE. |
| Mapping Tax box/Tax group - valid for Time-dependent Taxes | This configuration step is used to maintain your tax box mappings, tax groups, and, optionally, your tax box structures.<br>Tax boxes specify in which item of the tax return form the amount is posted. This amount can be the tax base amount, the total tax amount, or the sum of the tax base amount and the tax amount. Which of these three amounts is reported here depends on the specific tax form used for reporting. If you create tax boxes using Maintain Tax Box Mapping for Advanced Tax Return, you determine which amount is reported here by selecting the Tax Box Output Type.<br>Tax Groups consist of the tax group number, which should be same as the tax box number, the tax code, the valid-from and valid-to dates, the kinds of transactions to be reported, and the credit/debit marker.<br>Please note that the validity dates in the tax groups are the validity dates of the tax code. They must match the validity dates you set in the Define Tax Codes for Sales and Purchases.<br>The Tax Box Structure field is an optional text field that you can use to distinguish between different grouping versions.<br>For more information on how to maintain tax box mappings using this configuration step, see the Finance section in the product assistance for SAP S/4HANA Cloud. Search for "Time-Dependent Taxes". |

### Sheet: Tax Codes

| Country | Tax code | Description | Description in local language | Tax Type | EU Code | Error Indicator |
| --- | --- | --- | --- | --- | --- | --- |
| AE | S0 | AE Output VAT exempted | الإمارات: معفى من ضريبة القيمة المضافة على مبيعات | A |  | X |
| AE | S1 | AE Output VAT 0% - goods | الإمارات: ضريبة القيمة المضافة على مبيعات 0%-بضائع | A |  | X |
| AE | S2 | AE Output VAT 5% - goods | الإمارات: ضريبة القيمة المضافة على مبيعات 5%-بضائع | A |  | X |
| AE | S3 | AE Output VAT 0% - services | الإمارات: ضريبة القيمة المضافة على مبيعات 0%-خدمات | A |  | X |
| AE | S4 | AE Output VAT 5% - services | الإمارات: ضريبة القيمة المضافة على مبيعات 5%-خدمات | A |  | X |
| AE | S5 | AE Output VAT 0% for GCC export goods supplies | إمارات:ض.قيمةم.مبيعات0%لتصديرت.بضائع لمجلس تعاون خ | A |  | X |
| AE | S6 | AE Output VAT 0% for GCC export service supplies | إمارات:ضريبةقيمةم.مبيعات0%لتصديرت.خدمةمجلس تعاون خ | A |  | X |
| AE | S7 | AE Output VAT 0% for non-GCC export goods supplies | إمارات:ض.قيمةم.مبيعات0%لتصديرت.ب.لغيرمجلس تعاون خ. | A |  | X |
| AE | S8 | AE Output VAT 0% for non-GCC export srv supplies | إمارات:ض.قيمةم.مبيعات0%لتصديرت.خدمةلغيرمجلس تعاون | A |  | X |
| AE | S9 | AE Output VAT 0% for deemed supplies | إمارات:ضريبة قيمة مضافة لمبيعات 0% لتوريدات مفترضة | A |  | X |
| AE | SA | AE Output VAT 5% for transport goods to GCC state | إمارات:ض.قيمةم.مبيعات5%لنقل بضائع لدولةمجلس تعاون | A |  | X |
| AE | V0 | AE Input VAT exempted | الإمارات: معفى من ضريبة القيمة المضافة على مشتريات | V |  | X |
| AE | V1 | AE Input VAT 0% - goods | الإمارات: ضريبة قيمة مضافة على مشتريات 0% - بضائع | V |  | X |
| AE | V2 | AE Input VAT 5% - goods | الإمارات: ضريبة قيمة مضافة على مشتريات 5% - بضائع | V |  | X |
| AE | V3 | AE Input VAT 0% - services | الإمارات: ضريبة قيمة مضافة على مشتريات 0% - خدمات | V |  | X |
| AE | V4 | AE Input VAT 5% - services | الإمارات: ضريبة قيمة مضافة على مشتريات 5% - خدمات | V |  | X |
| AE | VA | AE import subject to reverse charge VAT 0% | إمارات: استيراد خاضع لمحاسبة عكسية ضريبة مضافة 0% | V | A |  |
| AE | VB | AE local supplies subject to reverse charge VAT5% | إمارات:توريد محلي خاضع لمحاسبةعكسية ضريبة مضافة 5% | V | A |  |
| AE | VX | AE VAT 5% for Reverse Charge imported goods | إمارات:ضريبةقيمةمضافة5% لمحاسبةعكسيةلبضائع مستوردة | V | A |  |
| AE | VY | AE VAT 5% for Reverse Charge imported service | الإمارات:ضريبةقيمةمضافة5%لمحاسبةعكسيةلخدمة مستوردة | V | A |  |

### Sheet: Time Dependent Tax Rates

| Tax Rate Valid From (YYYYMMDD) | Tax Code | Country | MWVS | MWAS | NLXA | NLXV |
| --- | --- | --- | --- | --- | --- | --- |
| 19000101 | S0 | AE |  | 0 |  |  |
| 19000101 | S1 | AE |  | 0 |  |  |
| 19000101 | S2 | AE |  | 0.05 |  |  |
| 19000101 | S3 | AE |  | 0 |  |  |
| 19000101 | S4 | AE |  | 0.05 |  |  |
| 19000101 | S5 | AE |  | 0 |  |  |
| 19000101 | S6 | AE |  | 0 |  |  |
| 19000101 | S7 | AE |  | 0 |  |  |
| 19000101 | S8 | AE |  | 0 |  |  |
| 19000101 | S9 | AE |  | 0 |  |  |
| 19000101 | SA | AE |  | 0.05 |  |  |
| 19000101 | V0 | AE | 0 |  |  |  |
| 19000101 | V1 | AE | 0 |  |  |  |
| 19000101 | V2 | AE | 0.05 |  |  |  |
| 19000101 | V3 | AE | 0 |  |  |  |
| 19000101 | V4 | AE | 0.05 |  |  |  |
| 19000101 | VA | AE |  |  | 0 | 0 |
| 19000101 | VB | AE |  |  | -0.05 | 0.05 |
| 19000101 | VX | AE |  |  | -0.05 | 0.05 |
| 19000101 | VY | AE |  |  | -0.05 | 0.05 |

### Sheet: T2 Mapping Tax Group-Tax Code

| Tax Box Structure Valid-From | Transaction | Country Key | Tax Code | Total/Debit/Credit | Tax Group | Tax Box Structure Type | Valid From | Valid To |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20180101 | MWS | AE | S0 |  | EXEMPT |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S0 |  | EXEMPT |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S0 |  | EXEMPT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VX |  | IMPORT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VX |  | IMPORT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VX |  | IMPORT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VX |  | IMPORT_ADJ |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V2 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V2 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V2 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V4 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V4 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V4 |  | PURCHINV |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V2 |  | PURCHINVBD |  | 19000101 | 99991231 |
| 20180101 | VST | AE | V4 |  | PURCHINVBD |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VA |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VA |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VA |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VB |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VB |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VB |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VX |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VX |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VX |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VY |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VY |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESE | AE | VY |  | RC_IN |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VA |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VA |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VA |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VB |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VB |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VB |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VY |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VY |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | ESA | AE | VY |  | RC_OUT |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S2 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S2 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S2 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S4 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S4 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S4 |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | SA |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | SA |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | SA |  | SALESINV |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S2 |  | SALESINVBD |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S4 |  | SALESINVBD |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | SA |  | SALESINVBD |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S2 |  | TOURIST_RE |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S1 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S1 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S1 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S3 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S3 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S3 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S5 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S5 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S5 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S7 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S7 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S7 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S8 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S8 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S8 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S9 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S9 |  | ZEROTAX |  | 19000101 | 99991231 |
| 20180101 | MWS | AE | S9 |  | ZEROTAX |  | 19000101 | 99991231 |

### Sheet: T2 Mapping Tax Box-Tax Group

| Country Key | Tax Box Structure Type | Tax Box Structure Valid-From | Tax Box | Tax Group |
| --- | --- | --- | --- | --- |
| AE |  | 20180101 | 1.1_base | SALESINV |
| AE |  | 20180101 | 1.1_tax | SALESINV |
| AE |  | 20180101 | 1.2_tax | SALESINVBD |
| AE |  | 20180101 | 10.1_base | RC_IN |
| AE |  | 20180101 | 10.1_tax | RC_IN |
| AE |  | 20180101 | 2.1_base | TOURIST_RE |
| AE |  | 20180101 | 2.1_tax | TOURIST_RE |
| AE |  | 20180101 | 3.1_base | RC_OUT |
| AE |  | 20180101 | 3.1_tax | RC_OUT |
| AE |  | 20180101 | 4.1_base | ZEROTAX |
| AE |  | 20180101 | 5.1_base | EXEMPT |
| AE |  | 20180101 | 6.1_base | IMPORT |
| AE |  | 20180101 | 6.1_tax | IMPORT |
| AE |  | 20180101 | 7.1_base | IMPORT_ADJ |
| AE |  | 20180101 | 7.1_tax | IMPORT_ADJ |
| AE |  | 20180101 | 9.1_base | PURCHINV |
| AE |  | 20180101 | 9.1_tax | PURCHINV |
| AE |  | 20180101 | 9.2_tax | PURCHINVBD |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Glossary lists condition type MWVZ as 'MWVN is connected to Transaction key NVV' - internal inconsistency in naming

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]
- related-to :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-ae-133]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Setup/2608_Pre-configured_Tax_Codes_EN_AE.xlsx` — full document · extracted with `xlsx2md` · 14,767 chars in the whole document
