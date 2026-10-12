---
id: 01-solution-foundation-and-platform/2608-org-data-overview-en-xx-121
title: 2608 Org Data Overview EN XX (2608_Org_Data_Overview_EN_XX)
description: "Workbook of SAP S/4HANA Cloud 2608 enterprise structure naming conventions (global and retail) for org units, with building-block origins and a hidden sample data sheet."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/enterprise-structure-and-org-units]
aliases: [2608_Org_Data_Overview_EN_XX]
keywords: [Enterprise Structure and Organizational Units, enterprise structure, organizational units, retail enterprise structure, naming conventions, storage locations, shipping points, sales areas, building blocks, country codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Org_Data_Overview_EN_XX.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-121
topic: 01-solution-foundation-and-platform/enterprise-structure-and-org-units
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 Org Data Overview EN XX (2608_Org_Data_Overview_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Org_Data_Overview_EN_XX.xlsx`, extracted with `xlsx2md`. Grouped under **Enterprise Structure and Organizational Units** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 Org Data Overview EN XX

### Sheet: Global_Enterprise_Structure

| ## represents the two-digit Country Code, e.g.<br>DE = 10 (Germany)<br>CN = 13 (China)<br>US = 17 (United States) |  |  | ## represents the two-digit Country Code<br>.. = .. (..) |  |  |  |  |  |  |  | Configuration |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  | (XX) --> Global (country-independent) BB<br>(##) --> Local (country-dependent) BB |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Additional Information |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | (initially…) Created in Building Block | 1. Enhanced in<br>Building Block | 2. Enhanced in<br>Building Block |
| Operating Concern |  |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
| A000 |  |  |  |  |  |  |  |  |  | no rule for naming available |  |  |  |
|  | Controlling Area |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  | A000 |  |  |  |  |  |  |  |  | no rule for naming available | J56 (XX) |  |  |
|  | Credit Control Area |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  | A000 |  |  |  |  |  |  |  |  | no rule for naming available | J56 (XX) |  |  |
|  |  | Company |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ##10 |  |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  | Company Code |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ##10 |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  | Purchasing Organization |  |  |  |  |  | A purchasing organization must be assigned to a company code, and only one company code |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | Purchasing Group |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  |  |  |  |  | 001 |  |  |  |  | generic key, starting with 001 | J56 (XX) |  |  |
|  |  |  |  | Plant |  |  |  |  |  |  |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | Storage Location (Plant/Storage Location) |  |  |  |  | STL key must be unique within the ENTIRE organizational structure |  |  |  |
|  |  |  |  |  | ##10 / ##1A |  |  |  | Std. storage 1 | n0m0 with n,m=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | ##10 / ##1B |  |  |  | Std. storage 2 | n0m0 with n,m=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | ##10 / ##1C |  |  |  | Raw mat. stoloc. | n0m0 with n,m=1,2,3… | J47 (##) |  |  |
|  |  |  |  |  | ##10 / ##1E |  |  |  | Kanban | n0m0 with n,m=1,2,3… | BGX (##) |  |  |
|  |  |  |  |  | ##10 / ##1R |  |  |  | Returns | n0m0 with n,m=1,2,3… | J47 (##) |  |  |
|  |  |  |  |  | ##10 / ##1I |  |  |  | 3rd Party WMS | n0m0 with n,m=1,2,3… | 26B(##) |  |  |
|  |  |  |  |  |  | Internal Warehouse Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  | ##2 |  |  | 3rd Party WM Integration | country-specific, ##0 with n=1,2,3… | 26B(##) |  |  |
|  |  |  |  |  | Shipping Point (Plant/Shipping Point) |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##10 |  |  |  | Std.Shipping Point | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | ##1R |  |  |  | Returns | country-specific, ##n0 with n=1,2,3… | J47 (##) |  |  |
|  |  |  |  | Transportation Planning Point |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Sales Organization |  |  |  |  |  |  |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | Distribution Channel |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10 |  |  |  |  | generic key, <br>starting with 10, then 20, 30,…; | J57 (##) |  |  |
|  |  |  |  |  | Division |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 00 |  |  |  |  | generic key,<br>starting with 00, then 01, 02 | J57 (##) |  |  |
|  |  |  |  |  |  |  | Sales Office (Sales Org./Distr. Channel/Division/Sales Office) |  |  | Combined Type |  |  |  |
|  |  |  |  |  |  |  | ##10/10/00/##0 |  |  | country-specific |  |  |  |
|  |  |  |  |  |  |  |  | Sales Group (Sales Office/Sales Group) |  | Combined Type |  |  |  |
|  |  |  |  |  |  |  |  | ##0/##0 |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  | For Basic Enterprise Structure Diagrams, see next worksheet |  |  |  |  |  |  |  |  |  |  |  |  |

### Sheet: Retail_Enterprise_Structure

| ## represents the two-digit Country Code, e.g.<br>DE = 10 (Germany)<br>NO = 44 (Norway)<br>US = 17 (USA)<br>CZ = 20 (Czech Republic)<br>PL = 26 (Poland)<br>SK = 27 (Slovakia)<br>FR = 12 (France) |  |  | ## represents the two-digit Country Code<br>.. = .. (..) |  |  |  |  |  |  |  |  |  | Configuration |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  | (XX) --> Global (country-independent) BB<br>(##) --> Local (country-dependent) BB |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | Additional Information |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | (initially…) Created in Building Block | 1. Enhanced in<br>Building Block | 2. Enhanced in<br>Building Block |
| Operating Concern |  |  |  |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
| A000 |  |  |  |  |  |  |  |  |  |  |  | no rule for naming available |  |  |  |
|  | Controlling Area |  |  |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  | A000 |  |  |  |  |  |  |  |  |  |  | no rule for naming available | J56 (XX) |  |  |
|  | Credit Control Area |  |  |  |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  | A000 |  |  |  |  |  |  |  |  |  |  | no rule for naming available | J56 (XX) |  |  |
|  |  | Company |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ##10 |  |  |  |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  | Company Code |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ##10 |  |  |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  | Purchasing Organization |  |  |  |  |  |  |  | A purchasing organization must be assigned to a company code, and only one company code |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | Purchasing Group |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  |  |  |  |  | 001 |  |  |  |  |  |  | generic key, starting with 001 | J56 (XX) |  |  |
|  |  |  |  | Plant/ Retail Site (Store/ Distribution Center) |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | ##10 | Plant |  |  |  |  |  | Standard Plant | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  | ##40 | Store |  |  |  |  |  | Retail Stores <br>##40, ##41, ##42, ##43, ##44, ##92 | country-specific, ##4n with n=0,1,2,3,4… | 68B (##) |  |  |
|  |  |  |  | ##50 | Distribution center |  |  |  |  |  | Retail Distribution Center ##50, ##91 | country-specific, ##5n with n=0,1,2,3… | 685 (##) |  |  |
|  |  |  |  |  | Storage Location (Plant/Storage Location) |  |  |  |  |  |  | STL key must be unique within the ENTIRE organizational structure |  |  |  |
|  |  |  |  |  | ##10 / ##1A |  |  |  |  |  | Std. storage 1 | n0m0 with n,m=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | ##10 / ##1R |  |  |  |  |  | Returns | n0m0 with n,m=1,2,3… | J47 (##) |  |  |
|  |  |  |  |  | Storage Location (Store/ Storage Location) |  |  |  |  |  |  | STL key should be unique within the ENTIRE organizational structure |  |  |  |
|  |  |  |  |  | ##40 / 994A |  |  |  |  |  | Storage location Store - Allow negativ stock |  | 68B (##) |  |  |
|  |  |  |  |  | Storage Location (Distribution Center/ Storage Location) |  |  |  |  |  |  | STL key should be unique within the ENTIRE organizational structure |  |  |  |
|  |  |  |  |  | ##50 / 995A |  |  |  |  |  | Storage location Distribution center - For finished products |  | 685 (##) |  |  |
|  |  |  |  |  | ##50 / 995R |  |  |  |  |  | Storage location Distribution Center - Return |  | 685 (##) |  |  |
|  |  |  |  |  | ##50 / 995B |  |  |  |  |  | Storage location Distribution Center - WH FT Retail |  | 7BA (##) |  |  |
|  |  |  |  |  | ##50 / 995C |  |  |  |  |  | Storage location Distribution Center - WH CD Retail |  | 7BA (##) |  |  |
|  |  |  |  |  | Storage Location 3rd Party WMS (Distribution Center/ Storage Location) |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##50 / 991I |  |  |  |  |  | Storage location Distribution Center - 3rd Party WMS |  | 6JB (##) |  |  |
|  |  |  |  |  | ##50 / 991K |  |  |  |  |  | Storage location Distribution Center - 3rd Party WMS Return |  | 6JB (##) |  |  |
|  |  |  |  |  |  | Internal Warehouse Number |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | ##2 |  |  |  |  | 3rd Party WM Integration | country-specific, ##0 with n=1,2,3… | 6JB (##) |  |  |
|  |  |  |  |  | Storage Location Cloud Warehouse (Distribution Center/ Storage Location) |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##50 / 995W |  |  |  |  |  | Storage location Distribution Center - Cloud Warehouse |  | 6JG (##) |  |  |
|  |  |  |  |  |  | Internal Warehouse Number |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | ##5 |  |  |  |  | Cloud Warehouse |  | 6JG (##) |  |  |
|  |  |  |  |  |  | Warehouse Number Cloud Warehouse |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ##50 |  |  |  | Cloud Warehouse number |  | 6JG (##) |  |  |
|  |  |  |  |  | Shipping Point (Plant/Shipping Point) |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##10 / ##10 |  |  |  |  |  | Std.Shipping Point | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | ##10 / ##1R |  |  |  |  |  | Returns | country-specific, ##n0 with n=1,2,3… | J47 (##) |  |  |
|  |  |  |  |  | Shipping Point w/o Lead Time (Store/ Shipping Point) |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##40 / 99CC |  |  |  |  |  | Shipping Point w/o Lead time - Click&Collect (cross country) |  | 68B (##) |  |  |
|  |  |  |  |  | ##40 / ##RS |  |  |  |  |  | Shipping Point w/o Lead time - Standard Store (per country) |  | 68B (##) |  |  |
|  |  |  |  |  | Shipping Point w/o Lead Time (Distribution Center (DC)/ Shipping Point) |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##50 / ##50 |  |  |  |  |  | Shipping Point w/o Lead time - StandardDC |  | 685 (##) |  |  |
|  |  |  |  |  | ##50 / ##5C |  |  |  |  |  | Shipping Point w/o Lead time - Consigment DC |  | 685 (##) |  |  |
|  |  |  |  |  | ##50 / ##5R |  |  |  |  |  | Shipping Point w/o Lead time - Return DC |  | 685 (##) |  |  |
|  |  |  |  | Transportation Planning Point |  |  |  |  |  |  |  | CANNOT be maintained within the Organization Structure App |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Sales Organization |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | ##10 |  |  |  |  |  |  |  | country-specific, ##n0 with n=1,2,3… | J57 (##) |  |  |
|  |  |  |  |  | Distribution Channel |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10 |  |  |  |  |  | Wholesale | generic key, <br>starting with 10, then 20, 30,…; | J57 (##) |  |  |
|  |  |  |  |  | 40 |  |  |  |  |  | Store Sales |  | 66W (XX) |  |  |
|  |  |  |  |  | 50 |  |  |  |  |  | Distribution |  | 66W (XX) |  |  |
|  |  |  |  |  | 60 |  |  |  |  |  | E-Commerce |  | 6J5 (XX) |  |  |
|  |  |  |  |  | Division |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 00 |  |  |  |  |  | Product Division | generic key,<br>starting with 00, then 01, 02 | J57 (##) |  |  |
|  |  |  |  |  |  |  |  | Sales Office (Sales Org./Distr. Channel/Division/Sales Office) |  |  |  | Combined Type |  |  |  |
|  |  |  |  |  |  |  |  | ##10/10/00/##0 |  |  |  | country-specific |  |  |  |
|  |  |  |  |  |  |  |  |  | Sales Group (Sales Office/Sales Group) |  |  | Combined Type |  |  |  |
|  |  |  |  |  |  |  |  |  | ##0/##0 |  |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  |  |  |  | Sales Area - Subtype |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | Sales Org | Dist Channel | Division | Plant/ Retail Site |  | Combined Type |  |  |  |
|  |  |  |  |  | Subtype - Wholesale |  | ##10 | 10 | 00 | ##10 |  | country-specific |  |  |  |
|  |  |  |  |  | Subtype - Store Sales |  | ##10 | 40 | 00 | ##4n, ##92 |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  |  |  |  |  | Subtype - Distribution Center |  | ##10 | 50 | 00 | ##50, ##91 |  | country-specific |  |  |  |
|  |  |  |  |  | Subtype -E-Commerce |  | ##10 | 60 | 00 | n/a |  | country-specific |  |  |  |
|  |  |  |  | Sales Organization/ Distribution Channel/ Plant/ Distribution Center/ Store |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Sales Org/ Dist Channel |  | Plant/ Store/ DC |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ##10/ 10 |  | ##10 |  |  |  |  | country-specific |  |  |  |
|  |  |  |  |  | ##10/ 10 |  | ##50, ##91 |  |  |  |  | country-specific |  |  |  |
|  |  |  |  |  | ##10/ 50 |  | ##50, ##91 |  |  |  |  | country-specific |  |  |  |
|  |  |  |  |  | ##10/ 50 |  | ##4n, ##92 |  |  |  |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  |  |  |  |  | ##10/ 40 |  | ##50, ##91 |  |  |  |  | country-specific |  |  |  |
|  |  |  |  |  | ##10/ 40 |  | ##4n, ##92 |  |  |  |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  |  |  |  |  | ##10/ 40 |  | ##50, ##91 |  |  |  |  | country-specific |  |  |  |
|  |  |  |  |  | ##10/ 40 |  | ##4n, ##92 |  |  |  |  | country-specific, ##n with n=0,1,2,3… |  |  |  |
|  | For Basic Enterprise Structure Diagrams, see next worksheet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Sheet: Enterprise_Structure_Data (hidden)

| CO/FI |  |  |  |  | MM |  | LO |  |  |  | SD |  |  |  |  | HR |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Operation Concern | Controlling Area | Credit Control Area | Company Code | Chart of Accounts | Purchasing Organization | Purchasing Group | Plant | Storage Location | Shipping Point | Transportation Planning Point | Sales Org | Distribution Channel | Division | Sales Office | Sales Group | Personnel Area | Personnel Subarea |
| 1000 | 1000 | 1000 | 1000 | YIKR | 1000 | 100 | 1000 | 1000/1010 | 1000 | 1000 | 1000 | 10 | 10 | 100 | 100 | 1000 | 1010 |
|  |  | 2000 | 2000 | 0010 | 2000 | 101 | 1100 | 1000/1020 | 100R | 2000 | 1100 | 20 | 20 | 110 | 110 | 1100 | 1020 |
|  |  |  |  |  |  | 102 | 2000 | 1000/1030 | 1100 |  | 2000 | 30 |  | 200 | 200 | 2000 | 1110 |
|  |  |  |  |  |  | 103 | 2100 | 1000/1040 | 110R |  | 2100 |  |  | 210 | 210 | 2100 | 1120 |
|  |  |  |  |  |  | 110 |  | 1000/1050 | 2000 |  |  |  |  |  |  |  | 2010 |
|  |  |  |  |  |  | 111 |  | 1000/1060 | 200R |  |  |  |  |  |  |  | 2020 |
|  |  |  |  |  |  | 112 |  | 1100/1110 | 2100 |  |  |  |  |  |  |  | 2110 |
|  |  |  |  |  |  | 113 |  | 1100/1120 | 210R |  |  |  |  |  |  |  | 2120 |
|  |  |  |  |  |  | 200 |  | 1100/1130 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 201 |  | 1100/1140 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 202 |  | 1100/1150 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 203 |  | 1100/1160 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 210 |  | 1000/1070 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 211 |  | 1000/1080 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 212 |  | 1100/1170 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | 213 |  | 1000/10Q1 Standard warehouse |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10Q2 Raw materials |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10Q3 Storage tank |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10Q4 Production warehouse |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10Q5 Finished goods |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1100/11Q4 Production warehouse |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1100/11Q5 Finished goods |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10G1 empties blocked |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10G2 Scrapping |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10G3 Warehouse |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10G4 HU / production |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1000/10G5 truck sloc |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1100/11QX |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 1100/11GX |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2010 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2020 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2030 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2040 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2050 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2060 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2110 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2120 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2130 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2140 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2150 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2160 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2070 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/2080 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/2170 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2000/20GX |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/21QX |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 2100/21GX |  |  |  |  |  |  |  |  |  |

*Empty sheets: Basic_Enterprise_Structure, Basic_Enterprise_Struct_Retail*

## Connections
- part-of :: [[_cluster]]
- see-also :: [[01-solution-foundation-and-platform/2608-predelivered-fyv-253]]
- see-also :: [[01-solution-foundation-and-platform/readme-2608]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_Org_Data_Overview_EN_XX.xlsx` — full document · extracted with `xlsx2md` · 17,938 chars in the whole document
