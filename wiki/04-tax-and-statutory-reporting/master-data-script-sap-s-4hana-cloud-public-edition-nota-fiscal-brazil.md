---
id: 04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil
title: Master Data Script - SAP S/4HANA Cloud Public Edition - Nota Fiscal Brazil (JD0_BR) (JD0_S4CLD2608_Master_Data_EN_BR)
description: "SAP Best Practices 2608 test script for Brazil master data and tax configuration (business place, BP, material, tax laws, CNAE, CFOP, SUFRAMA, CPRB, ICMS-ST, jurisdictions)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/brazil-nota-fiscal]
aliases: [JD0_S4CLD2608_Master_Data_EN_BR]
keywords: [Brazil Nota Fiscal Master Data and Tax Configuration, brazil master data, business place, customer master data, supplier master data, material master data, tax laws, withholding tax, service types, cfop determination]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/JD0_S4CLD2608_Master_Data_EN_BR.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-701
topic: 04-tax-and-statutory-reporting/brazil-nota-fiscal
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - SAP S/4HANA Cloud Public Edition - Nota Fiscal Brazil (JD0_BR) (JD0_S4CLD2608_Master_Data_EN_BR)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/JD0_S4CLD2608_Master_Data_EN_BR.docx`, extracted with `mammoth`. Grouped under **Brazil Nota Fiscal Master Data and Tax Configuration** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Nota Fiscal Brazil (JD0_BR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233905247)

[2 Prerequisites 4](#_Toc233905248)

[2.1 System Access 4](#_Toc233905249)

[2.2 Roles 4](#_Toc233905250)

[2.3 Required Organizational Units 5](#_Toc233905251)

[2.4 Required Master Data 5](#_Toc233905252)

[2.5 Main Parameters for Data Creation 6](#_Toc233905253)

[2.5.1 Define Country for Cloud 6](#_Toc233905254)

[3 Overview Table 7](#_Toc233905255)

[4 Test Procedures 12](#_Toc233905256)

[4.1 Define BR Specific Fields for Business Place 12](#_Toc233905257)

[4.2 Define BR Specific Fields for Master Data 17](#_Toc233905258)

[4.2.1 Customer Master Data 18](#_Toc233905259)

[4.2.2 Supplier Master Data 23](#_Toc233905260)

[4.2.3 Material Master Data 29](#_Toc233905261)

[4.3 Define Tax Laws 35](#_Toc233905262)

[4.3.1 Define ISS Tax Laws 35](#_Toc233905263)

[4.3.2 Define PIS Tax Laws 38](#_Toc233905264)

[4.3.3 Define COFINS Tax Laws 40](#_Toc233905265)

[4.3.4 Define ICMS Tax Laws 42](#_Toc233905266)

[4.3.5 Define IPI Tax Laws 44](#_Toc233905267)

[4.3.6 Define ISS Tax Situations as per ABRASF Standard 47](#_Toc233905268)

[4.4 Define ISS Tax Situation Defined by the Municipality 48](#_Toc233905269)

[4.5 Maintain Benefit Code for ISS Tax 50](#_Toc233905270)

[4.6 Assign Service Type to Service Number 51](#_Toc233905271)

[4.7 Define Official Brazilian Service Types - Outgoing 53](#_Toc233905272)

[4.8 Define Official Brazilian Service Types - Incoming 56](#_Toc233905273)

[4.9 Define Service Type Code for REINF (tpServiço) 59](#_Toc233905274)

[4.10 Assign Material to Service Type Code for REINF 61](#_Toc233905275)

[4.11 Define LC116 Codes 62](#_Toc233905276)

[4.12 Assign Material to LC 116 Codes 64](#_Toc233905277)

[4.13 Determine CEST 65](#_Toc233905278)

[4.14 Determine CFOP 67](#_Toc233905279)

[4.15 Define Tax Classification for Material or Service 69](#_Toc233905280)

[4.16 Define CPOM for Plants - SD 71](#_Toc233905281)

[4.17 Define CPOM for Service Provider - MM 72](#_Toc233905282)

[4.18 Define Withholding Tax Accumulation for Customers - SD 73](#_Toc233905283)

[4.19 Define Withholding Tax Accumulation for Plants - MM 75](#_Toc233905284)

[4.20 Determine Relevant Purchase Services for CPRB Contribution 76](#_Toc233905285)

[4.21 Determine Not Relevant Purchase Services for CPRB Contribution 77](#_Toc233905286)

[4.22 Determine Relevant Sales Services for CPRB Contribution 78](#_Toc233905287)

[4.23 Determine Not Relevant Sales Services for CPRB Contribution 79](#_Toc233905288)

[4.24 Determine Relevant Sales Materials for CPRB Contribution 80](#_Toc233905289)

[4.25 Determine Not Relevant Sales Materials for CPRB Contribution 82](#_Toc233905290)

[4.26 Maintain Benefit Code for ICMS Tax 84](#_Toc233905291)

[4.27 Configure Rules to Determine CNAE 85](#_Toc233905292)

[4.28 Configure Rules to Determine SUFRAMA and State Tax Number for Sales 97](#_Toc233905293)

[4.29 Configure Rules to Determine SUFRAMA and State Tax Number for Purchasing and Stock Transfer Orders 101](#_Toc233905294)

[4.30 Configure Rules to Determine ICMS-ST Contributors 104](#_Toc233905295)

[4.31 Configure Rules to Determine CFOP Extension for Sales 108](#_Toc233905296)

[4.32 Define Tax Jurisdiction Codes 114](#_Toc233905297)

[4.33 Assign Postal Codes to Tax Jurisdiction Codes 116](#_Toc233905298)

[4.34 Assign Tax Rate for Simples Nacional Supplier 118](#_Toc233905299)

[4.35 Configure Business Transactions for Sales 119](#_Toc233905300)

[4.36 Configure Usage Purposes for Sales 122](#_Toc233905301)

[4.37 Transfer Pricing Condition Value to Notas Fiscais for Material Management (MM)⁠ 124](#_Toc233905302)

[4.38 Configure the Additional Fiscal Data (AFD) Fields for Material Management (MM) 126](#_Toc233905303)

## Purpose

This document describes Master Data creation (Brazil) for your SAP S/4HANA system. The description includes data that are relevant for the SAP S/4HANA Brazil appliance, such as Tax Master Data, Central Data, Sales Area Data, Purchase and Company Code Data. Fields that are not relevant for the scope of the SAP S/4HANA Brazil content as delivered by SAP Best Practices are not described in this document.

This country version is designed for use by businesses with operations in Brazil. As well as the generic SAP system functions, it comprises functions designed for laws and business practices to Brazil.

This documentation explains how the country-specific functions work and what Master Data are needed to implement these country-specific functions. It does not cover the generic functions, which are described in the rest of the SAP Library.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

Conduct the test in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA System | Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

SAP S/4HANA Cloud Public Edition :

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Tax Specialist for Brazil | SAP_BR_TAX_SPECIALIST_BR |  |  |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Required Organizational Units

Some Tax Master Data are dependent on the organizational units of the company and some does not depend on an organizational unit or the company code. The following table gives an overview of these relevant organizational units.

This test script covers only a sample scenario and you are responsible for setting up the master data and taxes to meet your specific business requirements.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the business process steps of the scope item.

This chapter refers to Organization Data required.

| Data | Sample Value | Details | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Company Code | 1410 | -x- | Company Code 1410 | Company Code:____________ |
| Plant | 1410 | -x- | Plant 1410 | Plant Code:____________ |
| Business Place | 1410 | -x- | Business Place is the Fiscal Branch, like 1410 | Business Place:____________ |

### Required Master Data

Tax Master Data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to use in a Master Data and Tax Master Data record.

This set-up covers only a sample scenario and you are responsible for setting up the master data and taxes to meet your specific business requirements.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the business process steps of the scope item.

This chapter refers to Master Data required.

| Master Data | Sample Value | Details | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Vendor Master | 14300030 | -x- | Vendor 14300030 | Vendor Master:____________ |
| Customer Master | 14100001 | -x- | Customer 14100001 | Customer Master:____________ |
| Material Master | TG0011 | -x- | Material TG0011 – Trading Good |  |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a tax, customer, supplier and material master record and are always required to create master data record for Brazil. There is no tax master data which are always required except define country as it is shown at below.

#### Define Country for Cloud

All Master Data are defined under a country definition. Country for this document must be BR (Brazil).

Country BR is an input required at start when you are using J1BTAX transaction. This is not required when you are using the Fiori Apps listed in this document.

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Define BR Specific Fields for Business Place](#unique_10) [page ] 12 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Brazil Specific Fields are defined. |
| [Define BR Specific Fields for Master Data](#unique_11) [page ] 17 |  |  |  |
| [Customer Master Data](#unique_12) [page ] 18 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Brazil Specific Fields are defined. |
| [Supplier Master Data](#unique_13) [page ] 23 | Master Data Specialist - Business Partner Data | Maintain Business Partner (BP) | Brazil Specific Fields are defined. |
| [Material Master Data](#unique_14) [page ] 29 | Master Data Specialist - Product Data | Create Material (MM01) | Brazil Specific Fields are defined. |
| [Define Tax Laws](#unique_15) [page ] 35 |  |  |  |
| [Define ISS Tax Laws](#unique_16) [page ] 35 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ISS Tax Laws are defined. |
| [Define PIS Tax Laws](#unique_17) [page ] 38 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | PIS Tax Laws are defined. |
| [Define COFINS Tax Laws](#unique_18) [page ] 40 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | COFINS Tax Laws are defined. |
| [Define ICMS Tax Laws](#unique_19) [page ] 42 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ICMS Tax Laws are defined. |
| [Define IPI Tax Laws](#unique_20) [page ] 44 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | IPI Tax Laws are defined. |
| [Define ISS Tax Situations as per ABRASF Standard](#unique_21) [page ] 47 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ISS Tax Situations are defined (ABRASF). |
| [Define ISS Tax Situation Defined by the Municipality](#unique_22) [page ] 48 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ISS Tax Situations are defined (Municipal). |
| [Maintain Benefit Code for ISS Tax](#unique_23) [page ] 50 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ISS Benefit Code is created per tax jurisdiction code. |
| [Assign Service Type to Service Number](#unique_24) [page ] 51 | Tax Specialist for Brazil | Assign Official Service Types to Material Numbers - Brazil (J_1BSERVASSIGN2V) | Service Types are assigned to Service Numbers. |
| [Define Official Brazilian Service Types - Outgoing](#unique_25) [page ] 53 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Municipal service types for rendering services are created and assigned to LC 116/03. |
| [Define Official Brazilian Service Types - Incoming](#unique_26) [page ] 56 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Municipal service types for purchasing services are created and assigned to LC 116/03 service type. |
| [Define Service Type Code for REINF (tpServiço)](#unique_27) [page ] 59 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Define tpServiço codes. |
| [Assign Material to Service Type Code for REINF](#unique_28) [page ] 61 | Tax Specialist for Brazil | Assign EFD-REINF Service Codes - Brazil (S_ER9_52001552) | Assign material code to tpServiço. |
| [Define LC116 Codes](#unique_29) [page ] 62 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Define LC116 codes. |
| [Assign Material to LC 116 Codes](#unique_30) [page ] 64 | Tax Specialist for Brazil | Assign LC 116 Service Codes (S_ER9_52001553) | Assign material code to LC116. |
| [Determine CEST](#unique_31) [page ] 65 | Tax Specialist for Brazil | Assign Specifier Code of Substituição Tributária - Brazil (J_1BTCESTDET) | CEST determination are defined. |
| [Determine CFOP](#unique_32) [page ] 67 |  |  |  |
| [Define Tax Classification for Material or Service](#unique_33) [page ] 69 | Tax Specialist for Brazil | Define Tax Classification for Material or Service - Brazil (LOGBR_TAX_CLFN) | Tax Classification used with External Tax Calculation Engine Partners are assigned to material/service. |
| [Define CPOM for Plants - SD](#unique_34) [page ] 71 | Tax Specialist for Brazil | Define CPOM for Plants - Brazil (LOGBR_CPOM_PLNTV) | Informs the system that Plant/Business Place which is the service provider has CPOM registration with the municipal authorities of the city in which services will be rendered. |
| [Define CPOM for Service Provider - MM](#unique_35) [page ] 72 | Tax Specialist for Brazil | Define CPOM for Service Provider - Brazil (LOGBR_CPOM_VNDRV) |  |
| [Define Withholding Tax Accumulation for Customers - SD](#unique_36) [page ] 73 | Tax Specialist for Brazil | Define Withholding Tax Accumulation for Customers - Brazil (LOGBR_WHT_CUSTV) | Determines that withholding taxes on Sales and Distribution (PIS/COFINS/CSLL/IR) shall follow accumulation rules. |
| [Define Withholding Tax Accumulation for Plants - MM](#unique_37) [page ] 75 | Tax Specialist for Brazil | Define Withholding Tax Accumulation for Plants - Brazil (LOGBR_WHT_PLNTV) | Determines that withholding taxes in Purchase (PIS/COFINS/CSLL/IR) shall follow accumulation rules. |
| [Determine Relevant Purchase Services for CPRB Contribution](#unique_38) [page ] 76 | Tax Specialist for Brazil | Determine Relevant Purchase Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001575) | Determine if the combination Vendor + CNAE + Material + LC 116 Code + Validity period is subject to CPRB regimen. |
| [Determine Not Relevant Purchase Services for CPRB Contribution](#unique_39) [page ] 77 | Tax Specialist for Brazil | Determine Not Relevant Purchase Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001576) | Determine exception in the law for when the combination Vendor + CNAE + Material + LC 116 Code + Validity period is not subject to CPRB regimen. |
| [Determine Relevant Sales Services for CPRB Contribution](#unique_40) [page ] 78 | Tax Specialist for Brazil | Determine Relevant Sales Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001570) | Determine if the combination Company Code + CNAE + Material + LC 116 Code + Validity period is subject to CPRB regimen. |
| [Determine Not Relevant Sales Services for CPRB Contribution](#unique_41) [page ] 79 | Tax Specialist for Brazil | Determine Not Relevant Sales Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001571) | Determine exception in the law for when the combination Company Code + CNAE + Material + LC 116 Code + Validity period is not subject to CPRB regimen. |
| [Determine Relevant Sales Materials for CPRB Contribution](#unique_42) [page ] 80 | Tax Specialist for Brazil | Determine Relevant Sales Materials for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001572) | Determine if the combination Company Code + CNAE + Material + NCM + Validity period is subject to CPRB regimen. |
| [Determine Not Relevant Sales Materials for CPRB Contribution](#unique_43) [page ] 82 | Tax Specialist for Brazil | Determine Not Relevant Sales Material for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001574) | Determine exception in the law for when the combination Company Code + CNAE + Material + NCM + Validity period is not subject to CPRB regimen. |
| [Maintain Benefit Code for ICMS Tax](#unique_44) [page ] 84 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | ICMS Benefit Code is created per region. |
| [Configure Rules to Determine CNAE](#unique_45) [page ] 85 | Tax Specialist for Brazil | Configure Rules to Determine CNAE (WDA_TXS_BRF_CNAE) | Configure the rules for automatic determination of the CNAE Code that applies to a particular material or service transaction. |
| [Configure Rules to Determine SUFRAMA and State Tax Number for Sales](#unique_46) [page ] 97 | Tax Specialist for Brazil | Configure Rules to Determine Suframa and State Tax Number (WDA_TXS_BRF_SUFRAMA) | Configure the rules for automatic determination of the SUFRAMA Code and corresponding IE State Tax Number that applies to sales with Free Tax Areas (ZFM or ALC). |
| [Configure Rules to Determine SUFRAMA and State Tax Number for Purchasing and Stock Transfer Orders](#unique_47) [page ] 101 | Tax Specialist for Brazil | Configure Rules to Determine Suframa and State Tax Number (WDA_TXS_BRF_SUFRAMA) | Configure the rules for automatic determination of the SUFRAMA Code and corresponding IE State Tax Number that applies to purchasing transactions and stock transfer orders with Free Tax Areas (ZFM or ALC). |
| [Configure Rules to Determine ICMS-ST Contributors](#unique_48) [page ] 104 | Tax Specialist for Brazil | Configure Rules to Determine ICMS-ST Contributors (WDA_TXS_BRF_ICMSST) | Configure rules to identify if the vendor and the plant are ICMS-ST contributors for the same material so that ICMS-ST is not calculated in purchasing documents and their subsequent documents. |
| [Configure Rules to Determine CFOP Extension for Sales](#unique_49) [page ] 108 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Configure Rules for use in exceptional cases of sales transactions, where the government forsees the use of the same CFOP code for multiple business transactions, but still requires the CFOP’s description used for NFE and Reporting purpose, to reflect the individual sales transaction. |
| [Define Tax Jurisdiction Codes](#unique_50) [page ] 114 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Create Tax Jurisdiction Codes. |
| [Assign Postal Codes to Tax Jurisdiction Codes](#unique_51) [page ] 116 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Assign Tax Jusrisdiction Codes to Ranges of Postal Codes. |
| [Assign Tax Rate for Simples Nacional Supplier](#unique_52) [page ] 118 | Tax Specialist for Brazil | Assign Tax Rate for Simples Nacional Supplier - Brazil (LOGBR_MM_SIMPLES) | The tax rate was included for supplier. |
| [Configure Business Transactions for Sales](#unique_53) [page ] 119 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Customer Business Transaction is created. |
| [Configure Usage Purposes for Sales](#unique_54) [page ] 122 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | Customer usage Purpose is created. |
| [Transfer Pricing Condition Value to Notas Fiscais for Material Management (MM)⁠](#unique_55) [page ] 124 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | The mapping of MM conditions to NF is done. |
| [Configure the Additional Fiscal Data (AFD) Fields for Material Management (MM)](#unique_56) [page ] 126 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | The new Business Transaction with Usage Purpose is created. |

## Test Procedures

This section describes procedures for creating and testing the creation of master data.

### Define BR Specific Fields for Business Place

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Business Place data is the data you require to conduct business in Brazil. It includes address data and fiscal classifications related to the business place. Data, such as the taxes which are relevant when conducting business transactions. For Brazil, the main business place fields are described below.

- Tax Jurisdiction Code: A code used for determining tax rates in Brazil; it controls which tax authorities must be paid for a given transaction.
- Tax Numbers: Are tax identification numbers required in Brazil for levying taxes and subsequently reporting to the tax authorities. You maintain your business place tax numbers in the business place customizing screen.
    - [CNPJ Business Place tax number](https://help.sap.com/erp2005_ehp_03/helpdata/EN/df/48d953292a424de10000000a174cb4/content.htm)

You enter in the CNPJ Business Place tax number, the 4 digits which identify the business place (from the 9th to the 12th digit of the full 14 CNPJ digits).

-
    - State tax number

You enter the state tax number of the business place (no fixed number of digits or special format).

-
    - Municipal tax number

You enter the municipal tax number of the business place (no fixed number of digits or special format).

- Suframa Code: A code used to identify that the business place is located in a free tax zone and has certain fiscal incentives.
- CNAE: A code used for identifying the business place’s main National Classification of Economic Activities.
- Legal Nature: A code used for identifying the business place’s Legal Nature.
- CRT Number: The value identifies the business place’s Tax Regimen.
- ICMS Taxpayer: The value identifies the business place’s ICMS status (ICMS Contributor, ICMS Contributor - IE Exempted, Not ICMS Contributor).
- Industry Main Type: The value identifies the business place’s main industry type (Consumer, Manufacturing or Resale).
- Tax Declaration Type: The value identifies the business place’s main industry type (Presumed Profit, Real Profit or Simples National).
- Company Size: The value identifies the business place’s size according to the number of employees and the annual sales revenue (Large Business, MEI: Individual Microentrepreneur, Micro company, Medium Business, Small Business).
- SPED Activity Indicator: The value identifies the business place’s SPED indicator (Industrial/ Industrial Equivalent, Others).
- PIS/COFINS Declaration Regimen: The value identifies the business place’s PIS/COFINS declaration regimen (Cumulative or Non-Cumulative).
- NIRE ID and NIRE Date: The values identify the business place’s Registration Identification Number and date.
- Tax contributor Flags: The flags identify which taxes are relevant for the Business Place on Sales and Purchase transactions.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The app opens. |  |
| 3 | Set Country | Set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 4 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 5 | Display Existing Business Place | Inform the Company Code ID and choose Continue. | The existing business places for such company code displays. |  |
| 6 | Select the Business Place | Select a Business Place and go to Details. |  |  |
| 7 | Enter Tax Number | In the Nota Fiscal section, enter the follow information:CNPJ Business PlaceState Tax NumberMunicipal Tax NumberSAP recommends that this number corresponds to your business place.Note The CNPJ number is comprised of the following three elements:CNPJ company registration number, which is stored on the company levelCNPJ business place, which is stored on the plant levelCNPJ check digit, which is stored on the plant levelThe following data is mandatory when tax calculation is done via External Tax Calculation Engine:CNPJTax Numbers may be used by External Tax Calculation Engine Partners for handling exceptions. |  |  |
| 8 | Enter Tax Calculation Information | In the Nota Fiscal section, enter the follow information as per your business process requirements:Suframa CodeCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany SizeSPED Activity IndicatorPIS/COFINS Declaration RegimenNIRE IDNIRE DateThe following data is mandatory when tax calculation is done via External Tax Calculation Engine:Suframa CodeCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany Size | Inform the business place’s main CNAE Code, as per expected in SPED reporting. |  |
| 9 | Enter Tax Classification for Business Place | In the Nota Fiscal section set the flags for the taxes for which the business place is a contributor:ICMS ContributorIPI ContributorPIS ContributorCOFINS ContributorISS ContributorICMS ST ContributorThe data is mandatory when tax calculation is done via External Tax Calculation Engine.For Sales and Distribution, taxes will only be calculated when the business place is tax contributor.For Purchase, in case of ICMS, IPI, PIS and COFINS, having the flags marked means that the company may get credit of the taxes, depending on the scenario. |  |  |
| 10 | Enter Address and ZIP Code | Select the Address button at the top of the screen. At the Street Address section enter the full address and ZIP code.The ZIP code is used by External Tax Calculation Engine Partners for determination of Free Tax Zones within Brazil.The District is a required information for Electronic Invoicing (NF-e). |  |  |
| 11 | Enter Tax Jurisdiction Code | In the Street Address section enter the Tax Jurisdiction CodeThe Tax Jurisdiction Code is used by External Tax Calculation Engine Partners for calculation of all taxes. |  |  |
| 12 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Business Place.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Display Existing Business Place | Inform the Company Code id and Continue. | The existing business places for such company code displays. |  |
| 4 | Select the Business Place | Select a Business Place and go to Details. |  |  |
| 5 | Enter Tax Number | In the Nota Fiscal section enter the follow information:CNPJ Business PlaceState Tax NumberMunicipal Tax NumberSAP recommends that this number corresponds to your business place.Note The CNPJ number is comprised of the following three elements:CNPJ company registration number, which is stored on the company levelCNPJ business place, which is stored on the plant levelCNPJ check digit, which is stored on the plant levelThe following data is mandatory when tax calculation is done via External Tax Calculation Engine:CNPJTax Numbers may be used by External Tax Calculation Engine Partners for handling exceptions. |  |  |
| 6 | Enter Tax Calculation Information | In the Nota Fiscal section enter the follow information as per your business process requirements:Suframa CodeCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany SizeSPED Activity IndicatorPIS/COFINS Declaration RegimenNIRE IDNIRE DateThe following data is mandatory when tax calculation is done via External Tax Calculation Engine:Suframa CodeCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany Size | Inform the business place’s main CNAE Code, as per expected in SPED report-ing. |  |
| 7 | Enter Tax Classification for Business Place | In the Nota Fiscal section set the flags for the taxes for which the business place is a contributor:ICMS ContributorIPI ContributorPIS ContributorCOFINS ContributorISS ContributorICMS ST ContributorThe data is mandatory when tax calculation is done via External Tax Calculation Engine.For Sales and Distribution, taxes will only be calculated when the business place is tax contributor.For Purchase, in case of ICMS, IPI, PIS and COFINS, having the flags marked means that the company may get credit of the taxes, depending on the scenario. |  |  |
| 8 | Enter Address and ZIP Code | Select the Address button at the top of the screen. At the Street Address section enter the full address and ZIP code.The ZIP code is used by External Tax Calculation Engine Partners for determination of Free Tax Zones within Brazil.The District is a required information for Electronic Invoicing (NF-e). |  |  |
| 9 | Enter Tax Jurisdiction Code | In the Street Address section enter the Tax Jurisdiction CodeThe Tax Jurisdiction Code is used by External Tax Calculation Engine Partners for calculation of all taxes. |  |  |
| 10 | Save Your Data | Save your entries. |  |  |

### Define BR Specific Fields for Master Data

Purpose

Master data is the core data that is used as a base for any transaction. If you are producing, transferring stock, selling, purchasing, doing physical inventory, whatever your activity may be, it requires certain master data to be maintained. For Brazil, we have some specific fields as you can see below:

- Tax Jurisdiction Code: A code used for determining tax rates in Brazil; it controls which tax authorities must be paid for a given transaction.
- Tax Number: Country Version Brazil covers multiple tax numbers required in Brazil for levying taxes and subsequently reporting to the tax authorities. You maintain your customers' and vendors' tax numbers in their master records.
    - CNPJ number for legal entities
    - CPF number for natural persons

You enter the CPF number in the Tax Number 2 field and set the Natural Person indicator. The CPF number consists of 11 digits, for example, 076.635.658-80. Enter all 11 digits directly - with no spaces, periods, or hyphens.

-
    - State tax number

You enter the state tax number in the Tax Number 3 field (no fixed number of digits or special format).

-
    - Municipal tax number

You enter the municipal tax number in the Tax Number 4 field (no fixed number of digits or special format).

You enter your own state and municipal tax numbers per business place (see Business Place ).

- Control Code (NCM Code): The rate varies depending on its product classification, as defined by its NCM code. For some products, IPI is calculated on a reduced base amount. In most cases, the system uses the IPI rate entered for the material's NCM code. However, if any other value has been entered as an exception (including per material), this value always overwrites that of the NCM code.

#### Customer Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Customer master data is the data you require to conduct business relationships with your customers. It includes address data and terms of payment, for example. It also controls how business transactions are posted to a customer account and how the posted data is processed. Master data, such as whether complete delivery is required and the default delivery plant, is stored in master records. For Brazil, the main fields are described below, and many are prerequisite for tax determination via External Tax Calculation Engine.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | A new window opens, displaying the Maintain Business Partner (BP) screen. |  |
| 3 | Enter Address and ZIP Code | In BP role Business Partner (Gen.), on the General Data, Address tab and in the Standard Address section enter the full Address and ZIP Code.Note The ZIP code is used by External Tax Calculation Engine Partners for determination of Free Tax Zones within Brazil. |  |  |
| 4 | Enter Tax Jurisdiction Code | In BP role Business Partner (Gen.), on the General Data, Address tab and in the Standard Address section enter the Tax Jurisdiction Code.Note The Tax Jurisdiction Code is used by External Tax Calculation Engine Partners for calculation of all taxes. |  |  |
| 5 | Enter Tax Number | In BP role Business Partner (Gen.), on the General Data, Identification tab and in the Tax Number section enter the follow information:BR1 for Brazil: CNPJ NumberBR2 for Brazil: CPF NumberBR3 for Brazil: State Tax NumberBR4 for Brazil: Municipal Tax NumberNatural Person: If the indicator is not set, 'CGC' is relevant in tax number BR1. If the indicator is set, 'CPF' is relevant in tax number BR2.Note When creating a Customer master related to a Plant for Stock Transfer processes, please let all data identical to the ones in the respective Business Place. |  |  |
| 6 | Enter Tax Calculation Information | In BP role Customer, on the General Data, Customer: Tax Data tab and in the Tax Calculation Brazil section enter the follow information per your business process requirements:Suframa CodeRG NumberStateRG Issuing DateRIC NumberForeign National RegistrationRNE Issuing DateCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany SizePIS/COFINS Declaration RegimenThe following data is mandatory when tax calculation is done via External Tax Calculation Engine:Suframa CodeCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeCompany SizeNote When creating a Customer master related to a Plant for Stock Transfer processes, please let all data identical to the ones in the respective Business Place. | Inform the business partner’s main CNAE Code, as per expected in SPED reporting.Inform the business partner’s Suframa Code only when all sales of material to the business partner are related to the same tax incentive code (SUFRAMA Code). When more than ole occurs, keep the field empty and maintain the Suframa Code determination via Determine Business Partner’s SUFRAMA Code and Corresponding IE State Tax Number for Sales Materials. |  |
| 7 | Enter Payment Method | In BP role Customer (Fin. Accounting), on the Company Code data, Customer: Payment Transactions tab, in the Automatic Payment Transactions section and Payment Method enter one of the options below, as appropriate for the Customer:E - BoletoK - Duplicata/Borderô |  |  |
| 8 | Enter Withholding Tax | In BP role Customer (Fin. Accounting), on the Company Code data, Customer: Withholding Tax tab, in the Withholding Tax Type section and fields Withholding Tax Type and Withholding Tax Code enter one of the options below, as appropriate for the Customer:Actual postings considered in sales related transactions at time of invoice:IW/IW - ISS Withholding Tax at InvoiceRF/RF - IRRF WHT at InvoiceNS/NS - INSS WHT at InvoiceActual postings considered in sales related transactions at time of payment:PIS, COFINS, CSLL and IRRF Withholding Tax at Payment (daily accumulation rules):CA/CA - COFINS at PaymentPA/CA - PIS at PaymentRA/RA - IR at PaymentSA/SA - CSLL at PaymentPIS, COFINS, CSLL and IRRF Withholding Tax at Payment (without daily accumulation rules):CP/CP - COFINS at PaymentPP/PP - PIS at PaymentRP/RP - IR at PaymentSP/SP - CSLL at PaymentSales Examples:Sales of ISS relates services to Federal Public Companies, with provision of service by assignment of labor or contract agreement: IW/IW, NS/NS, CP/CP, PP/PP, SP/SP, RP/RPSales of ISS relates services to Federal Public Companies, without provision of service by assignment of labor or contract agreement: IW/IW, CP/CP, PP/PP, SP/SP, RP/RPSales of Goods to Federal Public Companies: CP/CP, PP/PP, SP/SP, RP/RPSales of ISS relates services to Private Companies, with provision of service by assignment of labor or contract agreement: IW/IW, NS/NS, RF/RF, and CP/CP, PP/PP, SP/SP or CA/CA, PA/PA, SA/SASales of ISS relates services to Private Companies, without provision of service by assignment of labor or contract agreement: IW/IW, RF/RF, and CP/CP, PP/PP, SP/SP or CA/CA, PA/PA, SA/SAActual postings considered in Financial related transactions:Withholding Tax at Payment Time (daily accumulation rules):CA - COFINS at PaymentPA - PIS at PaymentRA - IR at PaymentSA - CSLL at PaymentWithholding Tax at Payment Time (without daily accumulation rules):CP - COFINS at PaymentPP - PIS at PaymentRP - IR at PaymentSP - CSLL at PaymentWithholding Tax at Invoice Time:IW/IW - INSS Withholding Tax at InvoiceIR/R5 - IRRF Withholding Tax at Invoice |  |  |
| 9 | Enter Tax Classification for Customer | In BP role Customer (Fin. Accounting), on the Sales and Distribution data, Billing tab and in the Output Tax section enter one of the options below:0 for Tax Exempt1 for Liable for Taxes2 for Zona Franca - ICMS |  |  |
| 10 | Enter Tax Classification for Customer | On the Business Partner General data, Control tab and in the Tax Classification section enter one of the options below:BR01 for Brazil:0 for ICMS Non- Contributor1 for ICMS ContributorBR02 for Brazil:0 for IPI Non- Contributor1 for IPI ContributorBR03 for Brazil:0 for PIS Non- Contributor1 for PIS ContributorBR04 for Brazil:0 for COFINS Non- Contributor1 for COFINS ContributorBR05 for Brazil:0 for ISS Non- Contributor1 for ISS ContributorBR06 for Brazil:0 for ICMS ST Non- Contributor1 for ICMS ST ContributorNote The data is mandatory when tax calculation is done via External Tax Calculation Engine.Note When creating a Customer master related to a Plant for Stock Transfer processes, please let all data identical do the ones in the respective Business Place.The identical content for fields of tax and legal information will lead to correct tax calculation in the delivery for stock transfer. |  |  |
| 11 | Save Your Data | Save your entries. |  |  |

#### Supplier Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The vendor master database contains information about the vendors that supply an enterprise. This information is stored in individual vendor master records. A vendor aster record contains the vendor’s name and address, as well as data such as:

- The currency used for ordering from the vendor
- Terms of payment
- Names of important contact persons (sales staff)
- Payment methods

Since, to the accounts department, vendors are generally creditors (accounts payable), the vendor master record also contains accounting information, such as the relevant control account (reconciliation account) in the general ledger. For Brazil, the main fields are described below.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | A new window opens, displaying the Maintain Business Partner screen. |  |
| 3 | Enter Tax Jurisdiction Code | In BP role Business Partner (Gen.), on the General Data, Address tab and in the Standard Address section enter the Tax Jurisdiction Code. |  |  |
| 4 | Enter Tax Number | In BP role Business Partner (Gen.), on the General Data, Identification tab and in the Tax Number section enter the follow information:BR1 for Brazil: CNPJ NumberBR2 for Brazil: CPF NumberBR3 for Brazil: State Tax NumberBR4 for Brazil: Municipal Tax NumberNatural Person: If the indicator is not set, 'CGC' is relevant in tax number BR1. If the indicator is set, 'CPF' is relevant in tax number BR2.Note When creating a Supplier master related to a Plant for Stock Transfer processes, please let all data identical do the ones in the respective Business Place. |  |  |
| 5 | Enter Bank Details | In BP role Business Partner (Gen.), on the General Data, Payment Transactions tab and in the Bank Details section enter the follow information:IDCtry = BRBank Key (see note 152336)Bank acct (see note 152336)Control Key (see note 152336) |  |  |
| 6 | Enter Tax Calculation Information | In BP role Vendor, on the General Data, Vendor: Tax Data tab and in the Additional Tax Data section enter the follow information per your business process requirements:CRC numberRG NumberIssued byRG Issuing DateRIC NumberForeign National RegistrationRNE Issuing DateCNAELegal NatureCRT NumberICMS TaxpayerIndustry Main TypeTax Declaration TypeTax SplitThis field checked means that a purchase for industrialization from a reseller vendor will allow 50% of IPI credit for the invoice that has no IPI calculated by the vendor.Check this field only if the supplier has the field CNAE filled with a code related to a resale activity, such as retailer, wholesaler or distributor.Note When creating a Supplier master related to a Plant for Stock Transfer processes, please let all data identical do the ones in the respective Business Place.Different tax data between the Business Place and correspondent Supplier Master data can lead to wrong tax calculation and/or legal information.If the CRT number corresponds to a vendor under the Simples Nacional tax regime, then use the app Assign Tax Rate for Simples Nacional Supplier - Brazil (LOGBR_MM_SIMPLES) in order to register the tax rates applicable for in-coming invoices. The app is under the role SAP_BR_TAX_SPECIALIST_BR . See the [Assign Tax Rate for Simples Nacional Supplier](#unique_52) [page ] 118 section for more details. |  |  |
| 7 | Enter Tax Classification for Supplier | On the Business Partner General data, Control tab and in the Tax Classification section enter one of the options below:BR01 for Brazil:0 for ICMS Non- Contributor1 for ICMS ContributorBR02 for Brazil:0 for IPI Non- Contributor1 for IPI ContributorBR03 for Brazil:0 for PIS Non- Contributor1 for PIS ContributorBR04 for Brazil:0 for COFINS Non- Contributor1 for COFINS ContributorBR05 for Brazil:0 for ISS Non- Contributor1 for ISS ContributorBR06 for Brazil:0 for ICMS ST Non- Contributor1 for ICMS ST ContributorBR07 for Brazil:0 for Non Industrial Equivalent1 for Industrial EquivalentNote When creating a Supplier master related to a Plant for Stock Transfer processes, please let all data identical do the ones in the respective Business Place.Different tax classifications between the Business Place and correspondent Supplier Master data can lead to wrong tax calculation and/or legal information. |  |  |
| 8 | Enter Payment Method for Supplier | In BP role Vendor (Fin. Accounting), on the Company Code data, Vendor Payment Transactions tab, in the Automatic Payment Transactions section and field Payment Method enter one of the options below, as appropriate for the Vendor:A - TEDB - Credit on AccountD - DOCP - Payment OrderT - Bank TransferR - Utilities and Tax Payments2 - Pix out.Payments with PIX KEY3 - PIX transfer with Bank Account5 - Pix Inc. Payments with PIX KEYNote Payment Method “R” Utilities an Tax payments require a specific Business Partner, like a BP = Utilities (ENEL, CEMIG, CELPE, CPFL, etc), Telecom (Vivo, TIM, Claro), Gas (Comgas), Wa-ter (SABESP).And for tax payment, specific Business Partner for each tax authority, Receita Federal do Brasil, Sefaz SP, Sefaz RJ, etc. |  |  |
| 9 | Enter Withholding Tax for Supplier | In BP role Vendor (Fin. Accounting), on the Company Code data, Vendor: Withholding Tax tab, in the Withholding Tax Type section and fields Withholding Tax Type and Withholding Tax Code enter one of the options below, as appropriate for the Vendor:Actual postings considered in purchase related transactions at time of invoice:IJ - INSS - PJIM - INSS EMPLOYERIN - INSSIR - IRRF PJIW/IW – ISS Withholding Tax at InvoiceRF/1R- IRRF WHT at InvoiceNS/1N – INSS WHT at invoiceActual postings considered in sales related transactions at time of payment:CA - COFINS at PaymentCP - COFINS at PaymentID - IRRF PFPA - PIS at PaymentPP - PIS at PaymentRA - IR at PaymentRP - IR at PaymentSA - CSLL at PaymentGA - General Acc.GP - Gen WHT (PIS/COF/CSLL) at PaymentNote Covered by External Tax Calculation Engine:CACPIWPAPPRARPSASPRFNSGAGPActual postings considered at Payment Time:Withholding Tax at Payment Time (without daily accumulation rules):CP - COFINS at PaymentPP - PIS at PaymentSP - CSLL at PaymentAlternatively, the company can retain all the withholding taxes in only one account by using:GP – Gen WHT (PIS/COFINS/CSLL) at PaymentNever enter GP along with the specific withholding tax types (CP+PP+SP).Withholding Tax at Payment Time (daily accumulation rules):CA - COFINS at PaymentPA - PIS at PaymentSA - CSLL at PaymentAlternatively, the company can retain all the withholding taxes in only one account by using:GA- General accumulationNever enter GA along with the specific withholding tax types (CA+PA+SA).Accumulated withholding taxes demand the configuration of the view Define Withholding Tax Accumulation for Plants - Brazil.Do not mix withholding tax with and without accumulation. |  |  |
| 10 | Link Plant to the Business Partner | In BP role Vendor, on the General Data, Vendor: General Data tab and in the Additional General Data section enter the follow information:Plant: <input the Plant code to which this Business Partner refers to>Note This step is required only for Supplier master data that corresponds to a Plant for a Stock Transfer process.It is required to input the Plant code so that the Stock Transfer Order works properly. |  |  |
| 11 | Save Your Data | Save your entries. |  |  |

#### Material Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material master database (often referred to simply as the "material master", comprising all the individual material master records stored in the system) contains descriptions of all materials that an enterprise procures, produces, and keeps in stock. It is the central repository of information on materials (such as inventory levels) for the enterprise.

The integration of all material data in a single materials database eliminates the problem of data redundancy and permits the data to be used not only by Purchasing, but by other applications (such as Inventory Management, Materials Planning and Control, Invoice Verification, and so on).

Descriptions of the individual materials used in an enterprise are stored in material master records. For Brazil, the main fields are described below.

Procedure: Option 1 - Create Material

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Create Material (MM01).Note If you want to change material, you can search for the Change Material (MM02) app. | The Create Material (Initial Screen) displays. |  |
| 3 | Enter Material Basic Data | Make the follow entries:Material: Material NumberIndustry sector: Any oneMaterial Type: Finished Product or Trading Goods or Raw materials or Semifinished ProductsNote There are other material types such as Service Product, Non-Stock Material, Packaging, and Returnable packaging that can be created. |  |  |
| 4 | Choose Views | The views of material creation depend on the material type.For Brazil, there are views that have specific fileds for tax calculation:Sales: Sales Org. Data 1International Trade: ExportInternational Trade: Import: for SalesAccounting 2: for PurchaseIn this example, the material type has the views of sales in the configuration. Then in the Select View(s) dialog box, select Sales: Sales Org. Data 1, International Trade: Export, Accounting 2 and choose Continue. | The New Entries: Details of Added Entries screen displays. |  |
| 5 | Enter Organizational Levels Data | On the Organizational Levels screen, in the Organizational Levels section, make the following entries and choose Continue:Plant: for example, 1410Sales Organization: for example, 1410Distibution Channel: for example, 10 |  |  |
| 6 | Enter Basic data 1 Data | On the Basic data 1 tab, in the General Data section, enter the follow information according to your business process requirements:Material GroupExt. Matl Group |  |  |
| 7 | Enter Sales: sales org. 1 Data | On the Sales: sales org. 1 tab, in the Tax data section, enter an appropriate value for the Tax classification.Note For Brazil, select as below:Departure Ctry/Reg.: BRTax Category: IBRXTax classification:1 - for material2 - for services |  |  |
| 8 | Enter Intl. Trade: Export Data | On the Intl. Trade: Export tab, in the Foreign trade data section, enter an appropriate value in the Control code field.Note For Brazil, the Control code means NCM code.The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Control Code/NCM. For example: 3808.94.29In the Material CFOP category section, select an appropriate value in the Mat. CFOP category filed from the following:0: material1: electricity2: communication3: transportation4: animal |  |  |
| 9 | Enter Accounting 2 Data | On the Accounting 2 tab, in the Determination of CFOP code section, enter an appropriate value for the Material Usage, Material Origin and Produced in-house fields.The data is mandatory when tax calculation is done via External Tax Calculation Engine:Material Usage0: Resale1: Industrialization2: Consumption3: Asset4: Consumption for Main ActivityMaterial OriginChoose according to Brazilian fiscal classification:0: National - except indicated for codes 3, 4, 5 or 81: Foreign - imported directly2: Foreign - acquired nationally3: National - with import content over 40% and below/equal 70%4: National - production with tax incentive5: National - with import content less than or equal to 40%6: Foreign - imp direct, no similar nat., Res.CAMEX & nat.gas7: Foreign - acquired nat., no similar nat., Res.CAMEX & nat.gas8: National - with import content over 70%Produced in-houseThis field must be checked if the material is manufactured internally by the company. Generally, it applies to semifinished and finished materials. |  |  |
| 10 | Additional Data | On the Additional Data screen, on the Units of measure tab, in the Units of measure/EANs/dimensions section, enter an appropriate value for the EAN/UPC.The following data, when available, is important when tax calculation is done via External Tax Calculation Engine:EAN/UPC |  |  |
| 11 | Save Your Data | Save your entries. |  |  |
| 12 | Enter Intl. Trade: Import Data | In case of material types that have no sales views, it is necessary to enter Brazilian fileds in the two views: Internaltional Trade: Import and Accounting 2.On the Intl Trade: Import tab, in the Foreign trade data section, enter an appropriate value in the Control code field.Note For Brazil, the Control code means NCM code.The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Control Code/NCM. For example: 3808.94.29In the Material CFOP category section, select an appropriate value in the Mat. CFOP category filed from the following:0: material1: electricity2: communication3: transportation4: animalFor Accounting 2 fields, verify the Step 9 (Enter Accounting 2 Data).In case of material type Service Product, there is no Accounting 2 view. |  |  |

Procedure: Option 2 - Manage Product Master Data

Use the following procedure when your user access presents you with the Manage Product Master Data (F1602) app.

After creation of the material as recommended in MDS documentation, for example: Create Product Master of Type "Trading Good" (BNF), it is necessary to input the Brazilian fields to calculate the taxes.

This step only clarifies the views that have the Brazilian fields.

For Brazil, there are views that have specific fields for tax calculation: Sales: Sales Org. Data 1, International Trade: Export, International Trade: Import and Accounting 2.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Product Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Product Master Data (F1602). | The Manage Product Master Data screen displays. |  |
| 3 | Open the Product to Edit | Search for the previously created product by entering the product number in the Product search filed.Slect the product from the list which will navigate you to the Product view and choose Edit. | Product is displayed in edit mode. |  |
| 4 | Choose Distributions Chains | This step is used for materials that have sales views.In the Product view, select the Distribution Chains tabfor Sales Organization/Distribution created before. | The Distribution Chains tab displays. |  |
| 5 | Enter Sales Tax Data | In the Sales Tax section, make the following entries:Departure Ctry/Reg.: BRTax Category: IBRXTax Classification: Enter 1 for material or 2 for services | Tax Classification is maintained. |  |
| 6 | Returen to Main Screen | Choose Apply to return to the Product view. | The Product view displays. |  |
| 7 | Choose Plants Data | In the Product view, choose Plants and enter the detail page of the plant created before. |  |  |
| 8 | Enter Product CFOP Category Data | In the General Information section, make the following entries:Product CFOP Category:Choose the appropriate value as below:0: material1: electricity2: communication3: transportation4: animal |  |  |
| 9 | Enter Taxes in International Trade Data | In the International Trade section, make the following entries:Taxes in International Trade:Choose the code of taxes in International Trade (NCM). For example, 3808.94.29. |  |  |
| 9 | Returen to Main Screen | Choose Apply to return to the Product view. | Choose Apply to return to the Product view. |  |
| 10 | Choose Valuation Areas | In the Valuation Areas section, choose the valuation area and enter the detail page of the Valuation Area created before. |  |  |
| 11 | Enter Determination of CFOP Code | In the Determination of CFOP Code section, you must enter data for Determination of CFOP Code:Usage of the ProductChoose according to the Brazilian fiscal classification:0: Resale1: Industrialization2: Consumption3: Asset4: Consumption for Main ActivityOrigin of the Product:Choose according to the Brazilian fiscal classification:0: National - except indicated for codes 3, 4, 5 or 81: Foreign - imported directly2: Foreign - acquired nationally3: National - with import content over 40% and below/equal 70%4: National - production with tax incentive5: National - with import content less than or equal to 40%6: Foreign - imp direct, no similar nat., Res.CAMEX & nat.gas7: Foreign - acquired nat., no similar nat., Res.CAMEX & nat.gas8: National - with import content over 70%Produced in-houseThis field must be checked if the material is manufactured internally by the company. Generally, it applies to semifinished and finished materials.In case of material type Service Product, it is not necessary to fill the Usage of the Product, Origin of the Product, and Produced in-house fields. |  |  |
| 12 | Returen to Main Screen | Choose Apply to return to the Product view. | Manage Product Masterview displays. |  |
| 13 | Save Your Data | Save your entries. | A system message indicates that the object is saved. |  |

### Define Tax Laws

Purpose

Tax laws are defined by the relevant tax authorities and describe what rates apply for IPI, ICMS, PIS, COFINS and ISS for different sales and purchases of goods or services. They detail which transactions are subject to the full rate, which are subject to a reduced rate, and which are exempt from the tax.

Associated with each tax law is a text which might have to be printed on the Nota Fiscal (DANFE). For IPI and ICMS, you need to print this text for transactions that are not subject to the full rate. It is not mandatory to print a tax law text for ISS, but we recommend that you print a dummy tax law, such as IS0.

When tax calculation is done via External Tax Calculation Engine, both Purchase and Sales transactions will show all tax laws as TXS. The legal bases that supports a base reduction or exemption will be determined by the External Tax Calculation Engine Partner, and mapped to the Nota Fiscal database when the document is saved.

#### Define ISS Tax Laws

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine returns the ISS tax situation as per national definition from ABRASF (content is delivered by SAP).This activity is required when you create a NF document via NF writer (External Tax Calculation Engine is not requested) and you need a different ISS tax situation code. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by Application Area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define ISS Tax Laws. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:ISS Law: <3 digit key which will identify the ISS Tax Law>Tax Sit. ISS: <ISS tax situation as per ABRASF definition>Benefit Code for ISS Tax: <ISS benefit code>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  | The creation of ISS benefit codes is explained in chapter 4.5 Maintain Benefit Code for ISS Tax. |
| 7 | Save Your Data | Save your entries. | The new ISS tax law is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define ISS Tax Laws.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:ISS Law: <3 digit key which will identify the ISS Tax Law>Tax Sit. ISS: <ISS tax situation as per ABRASF definition>Benefit Code for ISS Tax: <ISS benefit code>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  | The creation of ISS benefit codes is explained in chapter 4.5 Maintain Benefit Code for ISS Tax. |
| 5 | Save Your Data | Save your entries. | The new ISS tax law is created. |  |

#### Define PIS Tax Laws

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine expects TXS as tax law (TXS is delivered by SAP). In this scenario, the fiscal texts are provided by External Tax Calculation Engine.This activity is required when you create a NF document via NF writer because External Tax Calculation Engine is not requested. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define PIS Tax Laws. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:PIS Law: <3 digit key which will identify the PIS Tax Law>Tax Sit. Inc. PIS: <Specifies the tax situation for PIS for an incoming nota fiscal>Tax Sit. Out. PIS: <Specifies the tax situation for PIS for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 7 | Save Your Data | Save your entries. | The new PIS tax law is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define PIS Tax Laws.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:PIS Law: <3 digit key which will identify the PIS Tax Law>Tax Sit. Inc. PIS: <Specifies the tax situation for PIS for an incoming nota fiscal>Tax Sit. Out. PIS: <Specifies the tax situation for PIS for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 5 | Save Your Data | Save your entries. | The new PIS tax law is created. |  |

#### Define COFINS Tax Laws

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine expects TXS as tax law (TXS is delivered by SAP). In this scenario, the fiscal texts are provided by External Tax Calculation Engine.This activity is required when you create a NF document via NF writer because External Tax Calculation Engine is not requested. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define COFINS Tax Laws. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:COFINS Law: <3 digit key which will identify the COFINS Tax Law>Tax Sit. Inc. COFINS: <Specifies the tax situation for COFINS for an incoming nota fiscal>Tax Sit. Out. COFINS: <Specifies the tax situation for COFINS for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 7 | Save Your Data | Save your entries. | The new COFINS tax law is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define COFINS Tax Laws.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:COFINS Law: <3 digit key which will identify the COFINS Tax Law>Tax Sit. Inc. COFINS: <Specifies the tax situation for COFINS for an incoming nota fiscal>Tax Sit. Out. COFINS: <Specifies the tax situation for COFINS for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 5 | Save Your Data | Save your entries. | The new COFINS tax law is created. |  |

#### Define ICMS Tax Laws

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine expects TXS as tax law (TXS is delivered by SAP). In this scenario, the fiscal texts are provided by External Tax Calculation Engine.This activity is required when you create a NF document via NF writer because External Tax Calculation Engine is not requested. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define ICMS Tax Laws. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:ICMS Law: <3 digit key which will identify the ISS Tax Law>Tax Sit. ICMS: <ICMS tax situation>Fiscal Benefit Code: <ICMS benefit code>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> | The creation of ICMS benefit codes is explained in chapter 4.26 Maintain Benefit Code for ICMS Tax. |  |
| 7 | Save Your Data | Save your entries. | The new ICMS tax law is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define ICMS Tax Laws.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:ICMS Law: <3 digit key which will identify the ISS Tax Law>Tax Sit. ICMS: <ICMS tax situation>Fiscal Benefit Code: <ICMS benefit code>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> | The creation of ICMS benefit codes is explained in chapter 4.26 Maintain Benefit Code for ICMS Tax. |  |
| 5 | Save Your Data | Save your entries. | The new ICMS tax law is created. |  |

#### Define IPI Tax Laws

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine expects TXS as tax law (TXS is delivered by SAP). In this scenario, the fiscal texts are provided by External Tax Calculation Engine.This activity is required when you create a NF document via NF writer because External Tax Calculation Engine is not requested. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define IPI Tax Laws. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:IPI Law: <3 digit key which will identify the IPI Tax Law>Tax Sit. Inc. IPI: <Specifies the tax situation for IPI for an incoming nota fiscal>Tax Sit. Out. IPI: <Specifies the tax situation for IPI for an outgoing nota fiscal>Legal Class. In: <Legal Classification Code for IPI for an incoming nota fiscal>Legal Class. Ou: <Legal Classification Code for IPI for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 7 | Save Your Data | Save your entries. | The new IPI tax law is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define IPI Tax Laws.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:IPI Law: <3 digit key which will identify the IPI Tax Law>Tax Sit. Inc. IPI: <Specifies the tax situation for IPI for an incoming nota fiscal>Tax Sit. Out. IPI: <Specifies the tax situation for IPI for an outgoing nota fiscal>Legal Class. In: <Legal Classification Code for IPI for an incoming nota fiscal>Legal Class. Ou: <Legal Classification Code for IPI for an outgoing nota fiscal>Description: <Description of the tax law, the text inserted here will appear when the user call the match code>Law: <First line of legal text>Law: <Second line of legal text>Law: <Third line of legal text>Law: <Fourth line of legal text> |  |  |
| 5 | Save Your Data | Save your entries. | The new IPI tax law is created. |  |

#### Define ISS Tax Situations as per ABRASF Standard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is not required for incoming and outgoing processes performed through MM and SD since External Tax Calculation Engine returns the ISS tax situation as per national definition from ABRASF (content is delivered by SAP).This activity is required when you create an NF document via NF writer (External Tax Calculation Engine is not requested) and you need a different ISS tax situation code. |

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for step Define ISS Tax Situation. |  |  |
| 5 | Create a New Entry | Choose New Entries and inform the ISS Tax Situation Code and its description. Assign the ISS Liability Indicator as per ABRASF definition. |  |  |
| 6 | Save Your Data | Save your entries. | The new ISS tax situation is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define ISS Tax Situation.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | Choose New Entries and inform the ISS Tax Situation Code and its description. Assign the ISS Liability Indicator as per ABRASF definition. |  |  |
| 4 | Save Your Data | Save your entries. | The new ISS tax situation is created. |  |

### Define ISS Tax Situation Defined by the Municipality

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| RememberThis activity is required to display ISS Tax Situation Description in NF documents as per City definition. External Tax Calculation Engine returns the ISS tax situation defined by the City.This activity is required when you create a NF document via NF writer (External Tax Calculation Engine is not requested) and you manually inform the ISS Tax Situation defined by the City. |

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for step Define Municipal CST ISS Description. |  |  |
| 5 | Create a New Entry | Choose New Entries and inform the Jurisdiction Code, the CST for ISS Defined by Municipality and its Description. |  |  |
| 6 | Save Your Data | Save your entries. | The new ISS tax situation is created as per Municipality definition. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Municipal CST ISS Description.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | Choose New Entries and inform the Jurisdiction Code, the CST for ISS Defined by Municipality and its Description. |  |  |
| 4 | Save Your Data | Save your entries. | The new ISS tax situation is created as per Municipality definition. |  |

### Maintain Benefit Code for ISS Tax

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Some municipalities require the ISS benefit code informed in the NFS-e (XML). This activity allows the creation of ISS benefit codes per jurisdiction code.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241) , set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for step Maintain Benefit Code for ISS Tax |  |  |
| 5 | Create a New Entry | Choose New Entries and inform the Jurisdiction Code, the Benefit Code for ISS and its Description. |  |  |
| 6 | Save Your Data | Save your entries. | The new ISS benefit code is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Benefit Code for ISS Tax.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | Choose New Entries and inform the Jurisdiction Code, the Benefit Code for ISS and its Description. |  |  |
| 4 | Save Your Data | Save your entries. | The new ISS benefit code is created. |  |

### Assign Service Type to Service Number

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Official Brazilian Service Type is the service type referred to in municipal laws and may vary from city to city. This information is required for tax calculation whenever External Tax Calculation Engine is responsible for tax calculation. Besides the municipal service type code, there is also the service type code defined on national level by the federal authorities and published in law LC 116/03 (LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003). The “LC 116” service type information is mandatory for tax calculation by External Tax Calculation Engine Partners, and is also required to be reported in XML file of NFS-e National layout (ABRASF).

Since the Official Brazilian Service Type may vary from city to city, it is required to have its value maintained for all the service tax relevant locations/cities (Service Provider, Service Execution, Service Purchaser). This data along with the “LC 116” service type will allow the External Tax Calculation Engine Partner to determine the tax relevant location/city as well as the ISS tax rules applied.

In this activity you assign the Official Brazilian Service Type to the service (material code) for both incoming and outgoing processes within a city.

Procedure

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Official Service Types to Material Numbers - Brazil (J_1BSERVASSIGN2V). |  |  |
| 3 | Determine Work Area | Make the following entry:Country Key: BRChoose Apply. |  |  |
| 4 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 5 | Enter General Data | Make entries according to the company needs:Material : <Material number>Jurisdict. Code: <Jurisdiction code>Inc. Serv. Type: <Incoming service type>Inc. Serv. Type: <Outgoing service type>Note The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Purchasing Service (MM): <Incoming service type>Rendering Services (SD): <Outgoing service type> |  |  |
| 6 | Save Your Data | Save your entries. |  |  |

### Define Official Brazilian Service Types - Outgoing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Official Brazilian Service Type is the service type referred to in municipal laws and may vary from city to city. This information is required for tax calculation whenever External Tax Calculation Engine is responsible for tax calculation. Besides the municipal service type code, there is also the service type code defined on national level by the federal authorities and published in law LC 116/03 (LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003). The “LC 116” service type information is mandatory for tax calculation by External Tax Calculation Engine Partners, and is also required to be reported in XML file of NFS-e National layout (ABRASF).

Since the Official Brazilian Service Type may vary from city to city, it is required to have its value maintained for all the service tax relevant locations/cities (Service Provider, Service Execution, Service Purchaser). This data along with the “LC 116” service type will allow the External Tax Calculation Engine Partner to determine the tax relevant location/city as well as the ISS tax rules applied.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Set Country | Set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 4 | Filter the Proper SSCUI | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 5 | Open Brazil Service Types | Choose Configure for Define Official Brazilian Service Types for Outgoing Notas Fiscais. |  |  |
| 6 | Determine Work Area | Make the following entry:Country Key: BRJurisdiction Code: <Jurisdiction code>Choose Continue (Enter).Select the Country BR and the Jurisdiction Code related to the city for which the service type entries are to be created. |  |  |
| 7 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 8 | Enter General Data | Make entries according to the company needs:Service type (outgoing): <service type code when rendering services as per Municipality Legislation >Text: <Description of the service as per Municipality Legislation >ABRASF Cod: <DO NOT inform here, leave blank>The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Jurisdiction CodeService type (outgoing)ABRASF Service type | Note The field ABRASF Cod will be inactivated in this app. Follow the chapters [Define LC116 Codes](#unique_29) [page ] 62 and [Assign Material to LC 116 Codes](#unique_30) [page ] 64 to define the service type as per LC116 (ABRASF Code) . |  |
| 9 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Official Brazilian Service Types for Outgoing Notas Fiscais.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Determine Work Area | Make the following entry:Country Key: BRJurisdiction Code: <Jurisdiction code>Choose Continue (Enter).Select the Country BR and the Jurisdiction Code related to the city for which the service type entries are to be created. |  |  |
| 4 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 5 | Enter General Data | Make entries according to the company needs:Service type (outgoing): <service type code when rendering services as per Municipality Legislation >Text: <Description of the service as per Municipality Legislation >ABRASF Cod: <DO NOT inform here, leave blank>The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Jurisdiction CodeService type (outgoing)ABRASF Service type | Note The field ABRASF Cod will be inactivated in this app. Follow the chapters [Define LC116 Codes](#unique_29) [page ] 62 and [Assign Material to LC 116 Codes](#unique_30) [page ] 64 to define the service type as per LC116 (ABRASF Code) . |  |
| 6 | Save Your Data | Save your entries. |  |  |

### Define Official Brazilian Service Types - Incoming

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Official Brazilian Service Type is the service type referred to in municipal laws and may vary from city to city. This information is required for tax calculation whenever External Tax Calculation Engine is responsible for tax calculation. Besides the municipal service type code, there is also the service type code defined on national level by the federal authorities and published in law LC 116/03 (LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003). The “LC 116” service type information is mandatory for tax calculation by External Tax Calculation Engine Partners, and is also required to be reported in XML file of NFS-e National layout (ABRASF).

Since the Official Brazilian Service Type may vary from city to city, it is required to have its value maintained for all the service tax relevant locations/cities (Service Provider, Service Execution, Service Purchaser). This data along with the “LC 116” service type will allow the External Tax Calculation Engine Partner to determine the tax relevant location/city as well as the ISS tax rules applied.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Set Country | Set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 4 | Filter the Proper SSCUI | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 5 | Open Brazil Service Types | Choose Configure for Define Official Brazilian Service Types for Outgoing Notas Fiscais. |  |  |
| 6 | Determine Work Area | Make the following entry:Country Key: BRJurisdiction Code: <Jurisdiction code>Choose Continue (Enter).Select the Country BR and the Jurisdiction Code related to the city for which the service type entries are to be created. |  |  |
| 7 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 8 | Enter General Data | Make entries according to the company needs:Service type (incoming): <service type code when rendering services as per Municipality Legislation >Text: <Description of the service as per Municipality Legislation >ABRASF Serv. Cod: <DO NOT inform here, leave blank>The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Jurisdiction CodeService type (incoming)ABRASF Service type | Note The field ABRASF Cod will be inactivated in this app. Follow the chapters [Define LC116 Codes](#unique_29) [page ] 62 and [Assign Material to LC 116 Codes](#unique_30) [page ] 64 to define the service type as per LC116 (ABRASF Code) . |  |
| 9 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Official Brazilian Service Types for Outgoing Notas Fiscais.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Determine Work Area | Make the following entry:Country Key: BRJurisdiction Code: <Jurisdiction code>Choose Continue (Enter).Select the Country BR and the Jurisdiction Code related to the city for which the service type entries are to be created. |  |  |
| 4 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 5 | Enter General Data | Make entries according to the company needs:Service type (incoming): <service type code when rendering services as per Municipality Legislation >Text: <Description of the service as per Municipality Legislation >ABRASF Serv. Cod: <DO NOT inform here, leave blank>The following data is mandatory when tax calculation is done via External Tax Calculation Engine:Jurisdiction CodeService type (incoming)ABRASF Service type | Note The field ABRASF Cod will be inactivated in this app. Follow the chapters [Define LC116 Codes](#unique_29) [page ] 62 and [Assign Material to LC 116 Codes](#unique_30) [page ] 64 to define the service type as per LC116 (ABRASF Code) . |  |
| 6 | Save Your Data | Save your entries. |  |  |

### Define Service Type Code for REINF (tpServiço)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Service Type code for REINF (a.k.a. tpServico) is the service type referred in SPED REINF and is defined by a list published by government. In Purchase of services, this information is required for INSS Withholding tax calculation whenever External Tax Calculation Engine is responsible for tax calculation.

Since all the Notas Fiscais with services related to Labor Contract “Cessão de mão-de-obra” are required to be reported in SPED REINF, for both Sales and Purchase of services, this information is relevant.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. |  |  |
| 3 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 4 | Open Brazil Service Types | Choose Configure for Maintain EFD-REINF Service Types. |  |  |
| 5 | Select New Entries | Choose Edit if required.Choose New Entries. |  |  |
| 6 | Enter General Data | Make entries according to the company needs:EFD-REINF Service Type code: <service type code from the REINF list>Description:<Description of the EFD-REINF service code> |  |  |
| 7 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain EFD-REINF Service Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select New Entries | Choose Edit if required.Choose New Entries. |  |  |
| 4 | Enter General Data | Make entries according to the company needs:EFD-REINF Service Type code: <service type code from the REINF list>Description:<Description of the EFD-REINF service code> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Assign Material to Service Type Code for REINF

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Service Type code for REINF (a.k.a. tpServico) is the service type referred in SPED REINF and is defined by a list published by government. In Purchase of services, this information is required for INSS Withholding tax calculation whenever External Tax Calculation Engine is responsible for tax calculation.

Since all the Notas Fiscais with services related to Labor Contract “Cessão de mão-de-obra” are required to be reported in SPED REINF, for both Sales and Purchase of services, this information is relevant.

By maintaining data here, tpServico code will be determined based on material code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Assign EFD-REINF Service Codes | Open Assign EFD-REINF Service Codes - Brazil (S_ER9_52001552). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Material: <material number>Description :<Description of the material number>EFD-REINF Service Type code: <service type code from the REINF list >Description: <Description of the EFD-REINF service code> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Define LC116 Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is a service type code defined on national level by the federal authorities and published in law LC 116/03 (LEI COMPLEMENTAR Nº 116, DE 31 DE JULHO DE 2003). The “LC 116” service type information is mandatory for tax calculation by External Tax Calculation Engine Partners and is also required to be reported in XML file of NFS-e National layout (ABRASF), as well as in record 0200 of SPED EFD Contributions and SPED ICMS/IPI, block B. Due to NF-e and NFS-e requirements, the LC116 code must contain leading zeroes as per expected in XML layouts (NN.NN).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays |  |
| 3 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance. |  |  |
| 4 | Open Brazil Service Types | Choose Maintain LC 116 Service Types. |  |  |
| 5 | Select New Entries | Choose Edit.Choose New Entries. |  |  |
| 6 | Enter General Data | Make entries according to the company needs:LC116 Service Type: <service type code from the LC116 list>Description: <Description of the LC116 service code>Note LC116 code format must be NN.NN, as per expected in NFE-e and NFS-e XML Layouts. |  |  |
| 7 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain LC 116 Service Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. |  |  |
| 4 | Enter General Data | Make entries according to the company needs:LC116 Service Type: <service type code from the LC116 list>Description: <Description of the LC116 service code>Note LC116 code format must be NN.NN, as per expected in NFE-e and NFS-e XML Layouts. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Assign Material to LC 116 Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By maintaining data here, LC 116 code for purchase or sales of services will be determined based on material code. This configuration is a mandatory for tax calculation via External Tax Calculation Engine, as well as for Service Nota Fiscal and reporting SPED EFD Contributions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system determines the national service type number using the jurisdiction code and municipal service type number. |  |
| 2 | Open Assign LC116 Service Codes | Open Assign LC 116 Service Codes (S_ER9_52001553). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Material: <material number>Description: <Description of the material number>LC116: <service type code from the LC116 list>Description: <Description of the LC116 service code>Note LC116 code format must be NN.NN, as per expected in NFE-e and NFS-e XML Layouts. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine CEST

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Código Especificador da Substituição Tributária (CEST) or in English, Tax Substitution Specifier Code, is part of an ICMS rule defined by ICMS Convênio no. 92 of August 20th, 2015 established the standard and identification on products and goods that are ICMS-ST (Tax Substitution). A List of products and goods that are subjected to this rule can be found in the Annex I to XXIX of this rule and in the CONFAZ Note S/No. from October 20th, 2015. All Tax Contributor Companies issuing a nota fiscal selling or transferring goods and products that may be taxed to ICMS-ST or to ICMS collect anticipation listed in the Annex above, must inform the corresponding CEST (Código Especificador da Substituição Tributária) code in the xml of that respective nota fiscal, regardless the transaction or good that are subjected to ICMS ST or to ICMS collect anticipation.

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction J1BTAX with the path: J1BTAX > Entities > CEST > CEST Determination with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Specifier Code of Substituição Tributária - Brazil (J_1BTCESTDET). | The app opens. |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Ini. Date: <Initial date when the rule should apply>Control Code: <NCM Code>Material: <Material Number>CEST: <CEST Number> | The user should fill the Control code OR the Material number.Note The CEST code, when relevant, is mandatory when tax calculation is done via External Tax Calculation Engine Partner. |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine CFOP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A code defined by the Brazilian authorities that describes the type of business transaction. In Portuguese, it is called código fiscal de operações e prestações. A CFOP code contains information on the good’s or service origin, as well as the type of business transaction, such as sales, returns, stock transfers, or services. The CFOP code must appear all state level Notas Fiscais, as well as on legal reporting of state and federal levels. An exception would be municipal level Service Notas Fiscais, where CFOP is not required.

When using a External Tax Calculation Engine Partner for tax calculation, the 4-digit CFOP will be automatically determined by the External Tax Calculation Engine Partner and mapped to the Nota Fiscal Database when the document is created. As a default solution, the CFOP extension “/AA” will be automatically added to the CFOP code when saving the document to the Nota Fiscal Database. Although External Tax Calculation Engine returns the 4-digit CFOP code for the sales and purchase processes, the full CFOP code (6 digits = CFOP + extension) must be created in S/4 tables, as described in this section.

Exclusively for use in Sales Transactions, it is possible to determine different CFOP extensions, but should only be done in case of CFOP codes where the government fore-sees the use of the same code for multiple business transactions, but still requires the CFOP’s description used for NFE DANFE and XML file, as well as Reporting purpose, to reflect the individual sales transaction. The different descriptions can be achieved via maintaining the same CFOP code with different extensions. The activity for determination of different extensions in sales transactions can be found under section Configure Rules to Determine CFOP Extension for Sales.

Examples of CFOP codes used in sales transactions, where the government expect the actual CFOP’s business transaction description to appear in all legal related documents and reports:

- CFOP 5910/AA – Shipment of Bonus, Donation or Gift (description as published by law)

Description as expected by the government to appear in all legal documents and reporting:

-
    - CFOP 5910/A1 - Bonus Shipment
    - CFOP 5910/A2 - Donation Shipment
    - CFOP 5910/A3 - Gift Shipment
- CFOP 1949/AA - Other goods receipt or service provision not specified (description as published by law)

Description as expected by the government to appear in all legal documents and reporting:

-
    - 1949/A1 – Return of Bonus Shipment
    - 1949/A2 – Return of Donation Shipment
    - 1949/A3 – Return of Gift Shipment

In case of NF Writer, where External Tax Calculation Engine is not called, the CFOP should be manually selected by the user as per the business transaction requirements.

Follow the procedure below in case you need to create a new CFOP Code.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by application area Application Platform and Infrastructure and sub-application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define CFOP Codes and Assign Version. |  |  |
| 5 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:Version: <use current version 4>CFOP: <enter CFOP code as per Government definition, use /AA in the end>Description: <enter CFOP description>ICMS Exempt: <if applicable, enter an ICMS exemption reason to be reported in NF-e >Issue Purpose: <in exception cases, you can inform an specific NF-e issue purpose> |  | Remember to use /AA as CFOP extension for the common CFOP codes, and a different extension when more than one description applies to the same CFOP code.Example:CFOP 5910/AA – Shipment of Bonus, Donation or GiftCFOP 5910/A1 - Bonus ShipmentCFOP 5910/A2 - Donation ShipmentCFOP 5910/A3 - Gift ShipmentCFOP 1949/AA - Other goods receipt or service provision not specified1949/A1 – Return of Bonus Shipment1949/A2 – Return of Donation Shipment1949/A3 – Return of Gift ShipmentThe reason for the rule is that External Tax Calculation Engine partner only returns the 4 numbers of the CFOP code, and “/AA” is automatically added to the end of the code before saving to the Nota Fiscal, unless a different CFOP code is determined. See item Configure Rules to Determine CFOP Extension for Sales for details. |
| 7 | Save Your Data | Save your entries. | The new CFOP code is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define CFOP Codes and Assign Version.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Version: <use current version 4>CFOP: <enter CFOP code as per Government definition, use /AA in the end>Description: <enter CFOP description>ICMS Exempt: <if applicable, enter an ICMS exemption reason to be reported in NF-e >Issue Purpose: <in exception cases, you can inform an specific NF-e issue purpose> |  |  |
| 5 | Save Your Data | Save your entries. | The new CFOP code is created. |  |

### Define Tax Classification for Material or Service

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Tax Classification is an attribute used by Sales and Distribution (SD) and Materials Management (MM) only when tax calculation is done by External Tax Calculation Engine Partner, and there is the need of further information in order to determine the correct tax values. In general, when required, it is for specific federal taxes but it may also be used by the External Tax Calculation Engine Partners for other purpose. The information that is maintained by the user must be done in accordance to the External Tax Calculation Engine Partner. It may be used for goods or services. When the External Tax Calculation Engine calls the Partner for tax calculation, the content of the Tax classification is passed on to the Partner as an attribute of the material or service for which taxes are being calculated.

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction SM30 with the table LOGBR_TAX_CLFN with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system determines the Tax Classification using the material number and validity period. |  |
| 2 | Open Define Tax Classification for Material or Service | Open Define Tax Classification for Material or Service - Brazil (LOGBR_TAX_CLFN). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Material: <Material Number>Ini. Date: <Initial date when the rule should apply>End Date: <Final date when the rule should apply>Tax Classification: <value as per instructed by External Tax Calculation Engine Partner> | The user should fill the Material number.Note When required, the value is defined by the External Tax Calculation Engine Partner used for tax calculation. |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Define CPOM for Plants - SD

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cadastro de Empresas de Fora do Município (CPOM) or in English, Record of Companies from Outside the Municipality is part of an ISS rule defined by certain cities in Brazil in order to ensure that service providers from other cities are in fact located outside of the city where the service is provided. The database record, when exists, avoids double taxation. Otherwise the company purchasing the services is responsible for tax collection to the destination city, which implies in double taxation via ISS withholding tax.

CPOM is only relevant when using a External Tax Calculation Engine Partner for tax calculation, the CPOM attribute will be automatically sent to External Tax Calculation Engine Partner for use in determination of ISS, this avoiding double taxation in the cities that have CPOM requirement.

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction SM30 with the table LOGBR_CPOM_PLNTV with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system determines the if plant which is the service provider (ISS) is registered at with the local authorities of the location in which the service is provided. The determination is done using the plant, material number, service location jurisdiction code, validity period and CPOM flag. |  |
| 2 | Open Define CPOM for Plants | Open Define CPOM for Plants - Brazil (LOGBR_CPOM_PLNTV). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Plant: <Plant which is the service provider in SD>Jurisdiction Code: <Jurisdiction Code of the location where service is executed>Service: <Material Number of the service>Ini. Date: <Initial date when the rule should apply>CPOM: <CPOM Flag> | The user should create an entry with CPOM flagged whenever requiredNote When CPOM is flagged, the information is sent to the External Tax Calculation Engine Partner for use in tax calculation. |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Define CPOM for Service Provider - MM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Cadastro de Empresas de Fora do Município (CPOM) or in English, Record of Companies from Outside the Municipality is part of an ISS rule defined by certain cities in Brazil in order to ensure that service providers from other cities are in fact located outside of the city where the service is provided. The database record, when exists, avoids double taxation. Otherwise the company purchasing the services is responsible for tax collection to the destination city, which implies in double taxation via ISS withholding tax.

CPOM is only relevant when using a External Tax Calculation Engine Partner for tax calculation, the CPOM attribute will be automatically sent to External Tax Calculation Engine Partner for use in determination of ISS, this avoiding double taxation in the cities that have CPOM requirement.

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction SM30 with the table LOGBR_CPOM_VNDRV with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Open Define CPOM for Service Provider | Open Define CPOM for Service Provider - Brazil (LOGBR_CPOM_VNDRV). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. |  |  |
| 4 | Enter General Data | Make entries according to the company needs:Service Provider: <Company that is providing the service>Service Location: <Location where service is being provided>Material (Original): <Material Number of the service>Valid From: <Initial date when the rule should apply>CPOM: <CPOM Flag> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Define Withholding Tax Accumulation for Customers - SD

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration of the Withholding Tax Accumulation for Customers is related to withholding taxes PIS, COFINS, CSLL and IR at payment time. It is used for determination of a particular set of condition types in the sales pricing, as per maintained in the Business Partner, role Customer (Fin. Accounting), on the Company Code data, Customer: Withholding Tax tab.

When accumulation is not required for withholding tax calculation, an entry is not required, and withholding taxes calculated by the External Tax Calculation Engine Partner will be automatically mapped to the SD pricing conditions which are assigned to withholding tax types CP (COFINS at Payment), PP (PIS at Payment), SP (CSLL at Payment) and RP (IR at Payment). When entries exist, then the values are automatically mapped to the conditions which are assigned to cumulative withholding tax types CA (COFINS at Payment), PA (PIS at Payment), SA (CSLL at Payment) and RA (IR at Payment).

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction SM30 with the table LOGBR_WHT_CUSTV with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system determines the service type number using the material number, jurisdiction code and direction of movement. |  |
| 2 | Open Define Withholding Tax Accumulation for Customers | Open Define Withholding Tax Accumulation for Customers - Brazil (LOGBR_WHT_CUSTV). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Customer: <Business Partner Code>Material: <Material Number>Ini. Date: <Initial date when the rule should apply>Cumulative WHT Flag: <WHT Number>Note When Cumulative WHT is flagged, the system will map the withholding taxes calculated by the External Tax Calculation Engine Partner to the corresponding withholding tax condition types in the sales pricing. | The user should set the flag when withholding tax accumulation is required. |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Define Withholding Tax Accumulation for Plants - MM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration of the Withholding Tax Accumulation for Plants is related to withholding taxes PIS, COFINS, CSLL and IR at payment time. It is used for determination of a particular set of condition types in the purchasing pricing, as per maintained in the Business Partner, role Supplier (Fin. Accounting), on the Company Code data, Vendor: Withholding Tax tab.

When accumulation is not required for withholding tax calculation, an entry is not required, and withholding taxes calculated by the External Tax Calculation Engine Partner will be automatically mapped to the MM pricing conditions which are assigned to withholding tax types CP (COFINS at Payment), PP (PIS at Payment), SP (CSLL at Payment) and RP (IR at Payment). When entries exist, then the values are automatically mapped to the conditions which are assigned to cumulative withholding tax types CA (COFINS at Payment), PA (PIS at Payment), SA (CSLL at Payment) and RA (IR at Payment).

|  |
| --- |
| Note In case of on-premise version of SAP S/4HANA, the maintenance of the table needs to be done by Transaction SM30 with the table LOGBR_WHT_PLNTV with data reported as Cloud version. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Open Define Withholding Tax Accumulation for Plants | Open Define Withholding Tax Accumulation for Plants - Brazil (LOGBR_WHT_PLNTV). |  |  |
| 3 | Select New Entries | Choose Edit.Choose New Entries. |  |  |
| 4 | Enter General Data | Make entries according to the company needs:Plant: <Receiving Plant>Material: <Material/Service Number>Valid From: <Initial date when the rule should apply>Cumulative WHT Tax: <WHT Flag> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Relevant Purchase Services for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sobre a Receita Bruta. This information is required for INSS Withholding tax rate determination whenever External Tax Calculation Engine is responsible for tax calculation.

In case CPRB is set as relevant for the combination of Supplier and other parameters, whenever INSS Withholding is due, its tax rate is determined as reduced.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Relevant Purchase Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001575). |  |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Vendor: <Supplier code/number>Material: <material code>LC116 Service Type code: <service type code from the LC116 list>Valid From: <initial date when the rule should apply>Valid To: <Final date when the rule should apply> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Not Relevant Purchase Services for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sobre a Receita Bruta. This information is required for INSS Withholding tax rate determination whenever External Tax Calculation Engine is responsible for tax calculation.

By maintaining data here, you are telling the system that there is an exception, and it is not CPRB relevant. As a result, if INSS Withholding is due, its tax rate is not reduced.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Not Relevant Purchase Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001576). |  |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Vendor: <Supplier code/number>Material: <material code>LC116 Service Type Code: < service type code from the LC116 list>Valid From: <initial date when the rule should apply>Valid To: <Final date when the rule should apply> |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Relevant Sales Services for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sober a Receita Bruta. Whenever External Tax Calculation Engine is responsible for tax calculation, in sales of service, this information is required for tax calculation of INSS CPRB and INSS Withholding.

In case CPRB is set as relevant for the combination of Company Code and other parameters:

- If due, INSS Withholding tax rate is determined as reduced
- INSS CPRB is calculated

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Relevant Sales Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001570). |  |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Company Code: <Supplier code/number>CNAE: <CNAE code>Material: <material code>LC116 Service Type Code: < service type code from the LC116 list>Valid From: <initial date when the rule should apply>Valid To: <Final date when the rule should apply>Note LC116 code format must be NN.NN, as per expected in NFE-e and NFS-e XML Layouts. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Not Relevant Sales Services for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sobre a Receita Bruta. Whenever External Tax Calculation Engine is responsible for tax calculation, in sales of service, this information is required for tax calculation of INSS CPRB and INSS Withholding.

By maintaining data here, you are telling the system that for the combination of Company Code and other parameters, there is an exception, and it is not CPRB relevant. As a result:

- If due, INSS Withholding tax rate is determined without reduction
- INSS CPRB is not calculated

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Not Relevant Sales Services for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001571). |  |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Company Code: <Supplier code/number>CNAE: <CNAE code>Material: <material code>LC116 Service Type Code: <service type code from the LC116 list>Valid From: <initial date when the rule should apply>Valid To: <Final date when the rule should apply>Note LC116 code format must be NN.NN, as per expected in NFE-e and NFS-e XML Layouts. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Relevant Sales Materials for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sobre a Receita Bruta. Whenever External Tax Calculation Engine is responsible for tax calculation, in sales of material, this information is required for tax calculation of INSS CPRB.

INSS CPRB tax is calculated in case CPRB is set as relevant for the combination of Company Code and other parameters.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Relevant Sales Materials for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001572). |  |  |
| 3 | Select New Entries | Choose the Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Company Code: <Supplier company code/number>CNAE: <CNAE code>Material: <material code>NCM Code: <Material Classification code>Valid From: <Initial date when the rule should apply>Valid To: <Final date when the rule should apply>The CNAE Code to be maintained here is one of the following:The Main CNAE maintained in the Business PlaceThe Transaction Business Place CNAE determined via Configure Rules to Determine CNAE.Maintain the NCM code as required. Either the complete code(8 to 10 numbers), or the first 4 digits (chapter+position). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Determine Not Relevant Sales Materials for CPRB Contribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CPRB means Contribuição Previdenciária sobre a Receita Bruta. Whenever Integration with External Tax Calculation Engine is responsible for tax calculation, in sales of material, this information is required for tax calculation of INSS CPRB.

By maintaining data here, you are telling the system that for the combination of Company Code and other parameters, there is an exception, and it is not CPRB relevant. As a result, INSS CPRB tax is not calculated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . |  |  |
| 2 | Access the SAP Fiori App | Open Determine Not Relevant Sales Material for CPRB Contribution for Tax Calc. - Brazil (S_ER9_52001574). |  |  |
| 3 | Select New Entries | Choose the Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Company Code: <Supplier company code/number>CNAE: <CNAE code>Material: <material code>NCM Code: <Material Classification code>Valid From: <Initial date when the rule should apply>Valid To: <Final date when the rule should apply>The CNAE Code to be maintained here is one of the following:The Main CNAE maintained in the Business PlaceThe Transaction Business Place CNAE determined via Configure Rules to Determine CNAEMaintain the NCM code as required. Either the complete code(8 to 10 numbers), or the first 4 digits (chapter+position). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. |  |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Maintain Benefit Code for ICMS Tax

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Some Brazilian States require ICMS benefit code informed in the NF-e (XML). This activity allows the creation of ICMS benefit codes per region.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using your user credentials. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by Application Area Application Platform and Infrastructure and Sub-Application Area Legal Compliance |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for step Maintain Benefit Code for ICMS Tax |  |  |
| 5 | Create a New Entry | Choose New Entries and inform the Region, the State Fiscal Benefit Code and its Description. |  |  |
| 6 | Save Your Data | Save your entries. | The new ICMS benefit code is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Benefit Code for ICMS Tax.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Entry | Choose New Entries and inform the Region, the State Fiscal Benefit Code and its Description. |  |  |
| 4 | Save Your Data | Save your entries. | The new ICMS benefit code is created. |  |

### Configure Rules to Determine CNAE

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

CNAE means Classificação Nacional de Atividades Econômicas. Whenever External Tax Calculation Engine is responsible for tax calculation, the CNAE code related to the business transaction is required by the External Tax Calculation Engine partner in order to insure the correct tax calculation.

This activity is not required whenever the same values applies to both Main CNAE and Business Transaction CNAE. The system will make use of the CNAE Codes maintained in both [Business Place](#unique_10) and Business Partner Master Data ([Customer](#unique_12)/[Supplier](#unique_13)).

Procedure

There may be up to four CNAE Codes related to a business transaction (Business Place’s Main CNAE/Business Place’s Business Transaction CNAE/Business Partner’s Main CNAE/Business Partner’s Business Transaction CNAE). Different CNAEs are required according to the different brazilian legal requirements, and therefore the system is prepared for each different requirements:

- For reporting purpose it is considered only the Business Place’s Main CNAE Code
- For NFE it is considered only the Business Transaction CNAE Code
- For tax calculation are considered the Business Transaction’s CNAE Codes of both Business Place and Business Partner

CNAE detemination functionality makes use of BRF Plus, which provides great flexibility for implementation of the required rules.

There is no Save button, new entries or changes are saved by selecting Activate.

When entering the selection, choose Edit for the Insert new row (+ sign) to appear.

Choose Insert new row for a new row to appear, and follow the steps below for creation of the rules:

- On the new row, enter the attributes required for determination.
- For each attribute select Direct value input for the input field to open.
- Then select the Comparison operators required (see field help for options and more details).
- Then enter the required data in the fields and chose OK.
- Proceed with the same steps until all required fields for CNAE determination are filled.
- Columns may be left empty as required.
- Entered rows may be moved up and down as required access sequence.

CNAE maintenance:

- Enter the CNAE Code for each of the Sales and Purchase options.

BRF Plus Maintenance:

- In case changes to existing entries are required, select the row by setting a flag in the check-box. When multiple row shall have the same content changed for the same value, select all rows required and then select to change a specific column. System will show one field for input and all rows selected for the change.
- The set the rules in their required access sequence, select the individual row by setting the flag in the check-box and use the Move up and Move down arrows to position the rule in the required access sequence.
- To save the new entries and changes to existing ones:
    - Choose Check on the header for checking consistency. Message Object is consistent is raised when no errors exist.
    - Choose Activate on the header for saving and activating the entries. Message Objects saved and activated appears when activation was successful.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system allows the user to maintain rules for automatic determination of the CNAE Code in a Business Transaction. |  |
| 2 | Access the (VH) Enabled Transactions | Open Configure Rules to Determine CNAE (WDA_TXS_BRF_CNAE) |  |  |
| 3 | Select Business Transaction | Choose Sales as Business Transaction. | The scenarios filtered for user selection in the next step are related to rules to be maintained for sales transactions. |  |
| 3.1 | Select Rule | Choose Business Place CNAE for Service Sales as Rules for.Select the subject for which you want to set the rules. |  |  |
| 3.1.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 3.1.2 | Enter General Data | Make entries according to the company needs:Plant: <Plant code/number>Sales Organization: <Sales Org. code>Distribution Channel: <Distribution Channel code>Material Group: <Material Group code>LC 116/ABRASF Service Type: <LC 116/ABRASF Service Type code>Material: <Material code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Place’s CNAE code of the transaction>Note Determine Business Place’s CNAE Code for Service Sales Transaction.The NF-e and NFS-e XML Layouts expect LC116 code in the format NN.NN. As a consequence the codes must be created in the tables in this format, and also maintained here in the same formatMaintain the validity period as required. | The Business Place’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 3.1.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a Save button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 3.2 | Select Rule | Choose Business Place CNAE for Material Sales as Rules for.Select the subject for which you want to set the rules. |  |  |
| 3.2.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 3.2.2 | Enter General Data | Make entries according to the company needs:Plant: <Plant code/number>Sales Organization: <Sales Org. code>Distribution Channel: <Distribution Channel code>Material Group: <Material Group code>NCM Code: <Material Fiscal code>Own Production Flag: <Own Production Flag>Material: <Material code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Place’s CNAE code of the transaction>Tip Determine Business Place’s CNAE Code for Material Sales Transaction.Maintain the validity period as required.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Place’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 3.2.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 3.3 | Select Rule | Choose Customer CNAE for Service Sales as Rules for.Select the subject for which you want to set the rules. |  |  |
| 3.3.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 3.3.2 | Enter General Data | Make entries according to the company needs:Customer: <Business Partner’s code/number>Sales Organization: <Sales Org. code>Distribution Channel: <Distribution Channel code>Material Group: <Material Group code>Industry Main Type: <Business Partner’s Industry Main Type>LC 116/ABRASF Service Type: <LC 116/ABRASF Service Type code>Material: <Material code>Valid Period: <Interval date when the rule should apply>CNAE: < Business Partner’s CNAE code of the transaction>Note Determine Business Partner’s CNAE Code for Service Sales Transaction.The NF-e and NFS-e XML Layouts expect LC116 code in the format NN.NN. As a consequence the codes must be created in the tables in this format, and also maintained here in the same format.For CNAE Codes related to all service types starting with a particular number, it is possible to maintain only the initial part of the code (use option Starts with).Maintain the validity period as required. | The Business Partner’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 3.3.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 3.4 | Select Rule | Choose Customer CNAE for Material Sales as Rules for.Select the subject for which you want to set the rules. |  |  |
| 3.4.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 3.4.2 | Enter General Data | Make entries according to the company needs:Customer: <Business Partner code/number>Sales Organization: <Sales Org. code>Distribution Channel: <Distribution Channel code>Material Group: <Material Group code>NCM Code: <Material Fiscal code>Industry Main Type: <Business Partner’s Industry Main Type>Material: <Material code>Customer Usage of Goods: <Customer Usage as per SD Tax Code(Resale, Industrialization, Consumption, Assets))>Valid Period: <Interval date when the rule should apply>CNAE: <Business Partner’s CNAE code of the transaction>Tip Determine Business Partner’s CNAE Code for Material Sales Transaction.Maintain the validity period as required.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Parner’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 3.4.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 4 | Select Business Transaction | Choose Purchase as Business Transaction. | The scenarios filtered for user selection in the next step are related to rules to be maintained for purchase transactions. |  |
| 4.1 | Select Rule | Choose Business Place for Service Purchase as Rules for.Select the subject for which you want to set the rules. |  |  |
| 4.1.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 4.1.2 | Enter General Data | Make entries according to the company needs:Plant: <Plant code/number>Supplier: <Supplier code/number>Purchasing Organization: <Purchasing Org. code>Material Group:: <Material Group code>LC 116/ABRASF Service Type: <LC 116/ABRASF Service Type code>Material Usage: <Material Usage>Material: <Material code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Place’s CNAE code of the transaction>Note Determine Business Place’s CNAE Code for Service Purchase Transaction.The NF-e and NFS-e XML Layouts expect LC116 code in the format NN.NN. As a consequence the codes must be created in the tables in this format, and also maintained here in the same format.Maintain the validity period as required.Material usage for service is informed only when the service is related to the main business of the buyer. | The Business Place’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 4.1.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 4.2 | Select Rule | Choose Business Place CNAE for Material Purchase as Rules for.Select the subject for which you want to set the rules. |  |  |
| 4.2.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 4.2.2 | Enter General Data | Make entries according to the company needs:Supplier: <Supplier code>Purchasing Organization: <Purchasing Org. code>Plant: <Plant code/number>Material Group: <Material Group code>NCM Code: <Material Fiscal code>Type of Industry: <Type of Industry>Material: <Material code>Material Origin <Material Origin code>Material Usage: <Material Usage code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Place’s CNAE code of the transaction>Tip Determine Business Place’s CNAE Code for Material Purchase Transaction.Maintain the validity period as required.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Place’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 4.2.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 4.3 | Select Rule | Choose Supplier CNAE for Service Purchase as Rules for.Select the subject for which you want to set the rules. |  |  |
| 4.3.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 4.3.2 | Enter General Data | Make entries according to the company needs:Supplier: <Supplier code/number>Purchasing Organization: <Purchasing Org. code>Material Group: <Material Group code>Plant: <Plant code/number>LC 116/ABRASF Service Type: <LC 116/ABRASF Service Type code>Material Usage: <Material Usage>Material: <Material code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Partner’s CNAE code of the transaction>Note Determine Business Partner’s CNAE Code for Service Purchase Transaction.The NF-e and NFS-e XML Layouts expect LC116 code in the format NN.NN. As a consequence the codes must be created in the tables in this format, and also maintained here in the same format.Maintain the validity period as required. | The Business Partner’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 4.3.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |
| 4.4 | Select Rule | Choose Supplier CNAE for Material as Rules for. |  |  |
| 4.4.1 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 4.4.2 | Enter General Data | Make entries according to the company needs:Supplier: <Supplier code>Purchasing Organization: <Purchasing Org. code>Plant: <Plant code/number>Material Group: <Material Group code>NCM Code: <Material Fiscal code>Type of Industry: <Type of Industry>Material: <Material code>Material Origin: <Material Origin code>Material Usage: <Material Usage code>Valid Period: <Interval date when the rule should apply>CNAE: <Business Partner’s CNAE code of the transaction>Tip Determine Business Partner’s CNAE Code for Material Purchase Transaction.Maintain the validity period as required.Material usage for service is informed only when the service is related to the main business of the buyer.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done accord-ing to the format as per the material master. When the mask “.” exists in material master’s NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Partner’s CNAE code of the transaction is determined according to the attributes informed by the user. |  |
| 4.4.3 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |

### Configure Rules to Determine SUFRAMA and State Tax Number for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SUFRAMA means Superintendência da Zona Franca de Manaus. Whenever External Tax Calculation Engine is responsible for tax calculation, this information may be required for the correct tax calculation.

This activity is not required whenever the Business Partner SUFRAMA Code and IE State Tax Number applies to all sales to the customer. The system will make use of the data maintained in Business Partner Master Data ([Customer](#unique_12) ).

Procedure

Suframa detemination functionality makes use of BRF Plus, which provides great flexibility for implementation of the required rules.

There is no Save button, new entries or changes are saved by selecting Activate.

When entering the selection, choose the “edit” button for the Insert new row (+ sign) to appear.

Choose Insert new row for a new row to appear, and follow the steps below for creation of the rules:

- On the new row, enter the attributes required for determination.
- For each attribute select “direct value input” for the input field to open.
- Then select the Comparison operators required (see field help for options and more details).
- Then enter the required data in the fields and chose OK.
- Proceed with the same steps until all required field for SUFRAMA determination are filled.
- Columns may be left empty as required.
- Entered rows may be moved up and down as required access sequence.

SUFRAMA maintenance:

- Enter the customer SUFRAMA Code and the corresponding IE State Tax Number applicable to the material being sold.
- For materials for which the ICMS Tax exemption is not applicable, and a SUFRAMA Code is maintained in the Business Partner Master Data ([Customer](#unique_12)), the SUFRAMA Code shall be cleared and the appropriate IE State Tax Number shall be determined. This is achieved by adding an empty entry for SUFRAMA Code which the system will show as “ “.

IE State Tax Number maintenance:

- The State tax number (IE) cannot be left empty. This is a feature of the law. Different SUFRAMA Codes have their equivalent State Tax Number, and when SUFRAMA Code does not apply, then the main State Tax Number shall be informed in the column State Tax Number. This is a mandatory field when adding rows.

BRF Plus Maintenance:

- In case changes to existing entries are required, select the row by setting a flag in the check-box. When multiple row shall have the same content changed for the same value, select all rows required and then select to change a specific column. System will show one field for input and all rows selected for the change.
- The set the rules in their required access sequence, select the individual row by setting the flag in the check-box and use the “move up” and “move down” arrows to position the rule in the required access sequence.
- To save the new entries and changes to existing ones:
    - Choose Check on the header for checking consistency. Message Object is consistent is raised when no errors exist.
    - Choose Activate on the header for saving and activating the entries. Message Objects saved and activated appears when activation was successful.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system allows the user to maintain rules for automatic determination of the SUFRAMA Code and State Tax Number of the business transaction. |  |
| 2 | Access the (VH) Enabled Transactions | Open Configure Rules to Determine Suframa and State Tax Number (WDA_TXS_BRF_SUFRAMA). |  |  |
| 3 | Select Business Transaction | Select Sales as Business Transaction. | The scenarios filtered for user selection in the next step are related to rules to be maintained for sales transaction. |  |
| 4 | Select Rule | Choose Customer Suframa and State Tax Number for Material Sales as Rules for.Select the subject for which you want to set the rules. | The rules configuration accessed is the one related to destination business partner. |  |
| 5 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 6 | Enter General Data | Make entries according to the company needs:Plant: <Plant code/number>Customer: <Business Partner’s code/number>Material Group <Material Group code>Industry Main Type: <Business Partner’s Industry Main Type>NCM Code: <Material Fiscal code>Material: <Material code>Validity: <Interval date when the rule should apply>Suframa Code: < Business Partner’s SUFRAMA code of the transaction>State Tax No.: < Business Partner’s IE State Tax Number of the transaction>Tip The SUFRAMA Code and State Tax Number determined are the ones to be saved to Nota Fiscal database.When a SUFRAMA code is maintained in the Busnes Partner master data, but the product is not due for tax exemption, the SUFRAMA code can be removed from the process by maintaining an entry with the relevant attributes, and leaving the SUFRAMA field empty (system displays as “ “).It is mandatory to inform the IE State Tax Number whenever an entry is maintained, with or without a SUFRAMA Code. When the SUFRAMA code is not not informed, the use shall inform the customer’s main IE - State Tax Number.Maintain the validity period as required.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (con-trol code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Partner’s SUFRAMA code and IE State Tax Number of the transaction are determined according to the attributes informed by the user. |  |
| 7 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |

### Configure Rules to Determine SUFRAMA and State Tax Number for Purchasing and Stock Transfer Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SUFRAMA means Superintendência da Zona Franca de Manaus. Whenever External Tax Calculation Engine is responsible for tax calculation, this information may be required for the correct tax calculation.

This activity is not required whenever the Business Partner SUFRAMA Code and IE State Tax Number applies to all Purchases and Stock Transfer Orders to Zona Franca de Manaus. The system will make use of the data maintained in Business Place (branch).

Procedure

Suframa determination functionality makes use of BRF Plus, which provides great flexibility for implementation of the required rules.

There is no Save button. New entries or changes are saved by choosing Activate.

When entering the selection, choose edit for the Insert new row (+ sign) to appear.

Choose Insert new row for a new row to appear, and follow the steps below for creation of the rules:

- On the new row, enter the attributes required for determination.
- For each attribute select "direct value input" for the input field to open.
- Then select the Comparison operators required (see field help for options and more details).
- Then enter the required data in the fields and choose OK.
- Proceed with the same steps until all required field for SUFRAMA determination are filled.
- Columns may be left empty as required.
- Entered rows may be moved up and down as required access sequence.

SUFRAMA maintenance:

- Enter the SUFRAMA Code and the corresponding IE State Tax Number applicable to the material being purchased or transferred to a plant in Zona Franca de Manaus.
- For materials for which the ICMS Tax exemption is not applicable, and a SUFRAMA Code is maintained in the Business Place, the SUFRAMA Code shall be cleared and the appropriate IE State Tax Number shall be determined. This is achieved by adding an empty entry for SUFRAMA Code which the system will show as "".

IE State Tax Number maintenance:

- The State tax number (IE) cannot be left empty. This is a feature of the law. Different SUFRAMA Codes have their equivalent State Tax Number, and when SUFRAMA Code does not apply, then the main State Tax Number shall be informed in the column State Tax Number. This is a mandatory field when adding rows.

BRF Plus Maintenance:

- In case changes to existing entries are required, select the row by setting a flag in the check-box. When multiple rows shall have the same content changed for the same value, select all rows required and then select to change a specific column. System will show one field for input and all rows selected for the change.
- The set the rules in their required access sequence, select the individual row by setting the flag in the checkbox and use the "move up" and "move down" arrows to position the rule in the required access sequence.
- To save the new entries and changes to existing ones:
    - Choose Check on the header for checking consistency. Message Object is consistent is raised when no errors exist.
    - Choose Activate on the header for saving and activating the entries. Message Message Objects saved and activated appears when activation was successful.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system allows the user to maintain rules for automatic determination of the SUFRAMA Code and State Tax Number of the business transaction. |  |
| 2 | Access the (VH) Enabled Transactions | Open Configure Rules to Determine Suframa and State Tax Number (WDA_TXS_BRF_SUFRAMA). |  |  |
| 3 | Select Business Transaction | Choose Material Management as Business Transaction. | The scenarios filtered for user selection in the next step are related to rules to be maintained for purchase and stock transfer transactions. |  |
| 4 | Select Rule | Choose Branch Suframa and State Inscription for Material Management.Select the subject for which you want to set the rules. | The rules configuration accessed is the one related to destination plant. |  |
| 5 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing, it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flag in the checkbox of each row.For change that applies to multiple rows, first select the rows and then the columns to be changed. | The Insert New Row (+ sign) appears for adding new rules. |  |
| 6 | Enter General Data | Make entries according to the company needs:Plant: <Plant code/number>It is informed for purchase.Material Group <Material Group code>Industry Main Type: <Business Partner’s Industry Main Type>NCM Code: <Material Fiscal code>Material: <Material code>Validity: <Interval date when the rule should apply>Ship From: <Origin plant for a stock transfer order>Ship To: <Destination plant for a stock transfer order>Suframa Code: <Business Partner’s SUFRAMA code of the transaction>State Tax No.: < Business Partner’s IE State Tax Number of the transaction>Tip The SUFRAMA Code and State Tax Number determined are the ones to be saved to Nota Fiscal database.When a SUFRAMA code is maintained in the Business Place, but the product is not due for tax exemption, the SUFRAMA code can be removed from the process by maintaining an entry with the relevant attributes, and leaving the SUFRAMA field empty (system displays as "").It is mandatory to inform the IE State Tax Number whenever an entry is maintained, with or without a SUFRAMA Code. When the SUFRAMA code is not not informed, the user shall inform the Business Place's main IE - State Tax Number.Maintain the validity period as required.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask "." exists in material master's NCM code (control code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 – OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government's TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master. | The Business Place's SUFRAMA code and IE State Tax Number of the transaction are determined according to the attributes informed by the user. |  |
| 7 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |

### Configure Rules to Determine ICMS-ST Contributors

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A specific purchase document has a combination of parameters that would result in ICMS ST calculation. However, if the plant (buyer) is eligible for ICMS ST for a material that they can also purchase, and the seller (supplier) is also eligible for ICMS ST, then ICMS ST (Substitute Tax) will not be included in the Nota Fiscal.

If we do not indicate this Supplier tax characteristic, on BP Master Data, the External Tax Partner will return ICMS ST calculated for this operation, and it would be wrong.

As the indicators for ICMS-ST contributor in the business plant as well as in the business partner do not indicate for which material there is ST contribution, there is a Configuration Step to configure the relationship among business place, business partner and material (it is possible to indicate NCM or EAN instead of a material number). The result of the configuration will be “true” or “false”, when “true” occurs when both vendor (business partner) and plant (business place) are ICMS-ST contributors for the same material/NCM/EAN.

If true, no ICMS-ST will be calculated in the purchasing documents and Notas Fiscais. Besides, the parameter "supplierBuyerIcmsStContributors" is sent as additional information in the request to the tax partner.

If false, ICMS-ST will be normally calculated - where “false” can be no entries or entries that do not satisfy the variables in the purchasing document.

Procedure

The determination of ICMS-ST contributor for a specific material, configured by NCM or EAN / UPC in MM scenarios makes use of BRF Plus, which provides great flexibility for implementation of the required rules.

There is no Save button, new entries or changes are saved by selecting Activate.

When entering the selection, choose Edit for the Insert new row (+ sign) to appear.

Choose Insert new row for a new row to appear, and follow the steps below for creation of the rules:

- On the new row, enter the attributes required for determination.
- For each attribute select direct value input for the input field to open.
- Then select the Comparison operators required (see field help for options and more details).
- Then enter the required data in the fields and chose OK.
- Proceed with the same steps until all required fields for ICMS-ST contributor determination are filled.
- Columns may be left empty as required.
- Entered rows may be moved up and down as required access sequence.

ICMS-ST maintenance at business place level (buyer):

- Update the flag ICMS-ST Contributor in the business place if the buyer plant is ICMS-ST contributor of any material.

ICMS-ST maintenance at business partner level (supplier):

- Access the role Business general, tab Identification and the area Tax classification. Then select the tax type BR06 and Tax group equal to 1, which means "ICMS-ST contributor" if this vendor is ICMS-ST contributor for any material.

BRF Plus Maintenance:

- In case changes to existing entries are required, select the row by setting a flag in the check-box. When multiple row shall have the same content changed for the same value, select all rows required and then select to change a specific column. System will show one field for input and all rows selected for the change.
- The set the rules in their required access sequence, select the individual row by setting the flag in the check-box and use the move up and move down arrows to position the rule in the required access sequence.
- To save the new entries and changes to existing ones:
    - Choose Check on the header for checking consistency. Message Object is consistent is raised when no errors exist.
    - Choose Activate on the header for saving and activating the entries. Message Objects saved and activated appears when activation was successful.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays.In this activity, the system allows the user to maintain rules for automatic determination of the SUFRAMA Code and State Tax Number of the business transaction. |  |
| 2 | Access the (VH) Enabled Transactions | Open Configure Rules to Determine ICMS-ST Contributors (WDA_TXS_BRF_ICMSST). |  |  |
| 3 | Select Business Transaction | Choose Purchase as Business Transaction. | The scenarios filtered for user selection in the next step are related to rules to be maintained for purchase transactions. |  |
| 4 | Select Rule | Choose Supplier and Buyer ICMS-ST contributor for material purchase. |  |  |
| 5 | Select New Entries | Choose Edit if necessary.Choose Insert New Row.Note While editing it is also possible to change existing rules. For change or existing rules, select the individual rows by setting a flg in the check box of each row.For change that applies to multiple rows, first select the rows and then the colums to be changed. | The Insert New Row (+ sign) appers for adding new rules. |  |
| 6 | Enter General Data | Make entries according to the company needs:Validity Period: <Interval date when the rule should apply>Supplier: <Business Partner’s code/number>Plant: <Plant code/number>ICMS ST Legal Classif. Code: <CEST>NCM Code: <Material Fiscal code>EAN/UPC: <EAN or UPC code>Tip Maintain the validity period as required.The Supplier is the Business Partner number.The Plant is the plant that buys the material from the respective vendor. Although the ICMS-ST contributor indicator is in the Business Place, the Plant is the entity informed in the purchasing documents. Besides, the Plant is linked to the business plant.ICMS ST Legal Classification Code: it is the CEST number.Maintain the NCM code as required. Either the complete code, or part of it (chapter, position, subposition, or item). It is important that the value entered as NCM is done according to the format as per the material master. When the mask “.” exists in material master’s NCM code (con-trol code), the mask shall be maintained here.Example of NCM Structure with mask:Chapter: 01 - Live animalsPosition: 0104 - Live sheep and goatsSubposition: 0104.10 - SheepItem: 0104.10.1 - Purebred breedersNCM: 0104.10.11 - Pregnant or with calf at the footNCM: 0104.10.19 - OtherSubposition: 0104.20 - GoatsNCM: 0104.20.10 - Purebred breeders goatsNCM: 0104.20.90 - Other goatsNote When the product represented by the NCM code contains an extra classification known as EX Code from government’s TIPI table, the EX Code is maintained as the last 2 digits of the NCM code, thus then having 10 digits instead of 8 digits.This feature is dealt with throughout the system, but it is very important that when maintaining the full NCM code in this configuration, that this is done with all 10 digits, as selected when maintaining the material master.EAN / UPC: If the NCM is not enough to configure ICMS-ST contribution, then EAN can be used to define both plant and vendor as ICMS-ST contributors for the same material. | Validity, Supplier and Plant are required fields. However, it is possible to inform one or more parameters among NCM, CEST and EAN/UPC.According to parameters entered by the user, External Tax Calculation Engine will identify if both Vendor and Plant are ICMS-ST contributors for the same material and then avoid the ICMS-ST calculation in the purchasing documents. |  |
| 7 | Save Your Data | Save your entries by activating the new rules maintained. | When using BRF+, a SAVE button is not available. In order to save, the user shall check and then activate the entered rules. The Check and Activate buttons are located on the header of the screen. Once activated the user may leave the screen or add/change new entries. |  |

### Configure Rules to Determine CFOP Extension for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For sales transactions, the government expects the appropriate CFOP description to be used throughout the sales process (DANFE, NFE XML, and SPED Reporting). Althought External Tax Calculation Engine is responsible for determining the CFOP code of the sales transaction, whenever the same CFOP code applies to different tax scenarios, it is required to add configuration for the determination of the appropriate CFOP code within SAP system (CFOP + Extension), which is done by determining a CFOP extension different from “/AA”, which contains the appropriate CFOP description.

Examples of CFOP codes used in sales transactions, where the government expect the actual CFOP’s business transaction description to appear in all legal related documents and reports:

- CFOP 5910/AA – Shipment of Bonus, Donation or Gift (description as published by law)

Description as expected by the government to appear in all legal documents and reporting:

-
    - CFOP 5910/A1 - Bonus Shipment
    - CFOP 5910/A2 - Donation Shipment
    - CFOP 5910/A3 - Gift Shipment
- CFOP 1949/AA - Other goods receipt or service provision not specified (description as published by law)

Description as expected by the government to appear in all legal documents and reporting:

-
    - 1949/A1 – Return of Bonus Shipment
    - 1949/A2 – Return of Donation Shipment
    - 1949/A3 – Return of Gift Shipment

Before starting the configuration of CFOP extension determination, the user shall insure that the required CFOP codes and extensions are created with the appropriate descriptions as described in [Determine CFOP](#unique_32) [page ] 67.

Procedure

Follow the steps below to create a new CFOP rule for automatic determination of CFOP extension for sales transactions.

Besides the creation of rules, the same functionality also allows the maintenance of validity periods, thus controlling the activation/deactivation of the rules.

Each rule is composed of input and output parameters:

- The input parameters are the parameters available for user combination, in order to achieve the automatic determination of the output parameter (full SAP CFOP code). Available parameters are:
    - Business Transaction, which is a parameter available for exceptional cases when the determination of an exact CFOP is required, but it cannot be achieved without it;
    - CFOP code as per law Ajuste SINIEF, which is the 4 digit CFOP code determined by External Tax Calculation Engine Partner. This is a mandatory parameter that will insure that when selecting the output parameter, only CFOP codes starting with the 4 digit code are available for user selection.
    - Labor Contract Activity, which is a parameter used to identify when the service is related to Labor Contract Activity, thus INSS tax is due. This parameter is only required when the service rendered is related to Mixed Nota Fiscal model 55 or 01, which is mandatory for service rendering companies installed in Distrito Federal.
    - Nota Fiscal Item Type, which is a parameter used in certain circumstances like returnable packaging material, future delivery, consignment and others. It may also be used for automatic determination of CFOP, when other parameters available are not sufficient;
    - Usage Purpose, which is a parameter available for many transactions and also allows to easily determine the required SAP CFOP code.
- The output parameter is the actual full SAP CFOP code created in [Determine CFOP](#unique_32) [page ] 67.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aConfiguration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and subapplication area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Configure Rules to Determine CFOP Extension for Sales for Tax Calculation. | The user should create a rule sequence to be considered by the system to determine different CFOP extensions created in Item Determine CFOP |  |
| 5 | Create New Rules | The creation of a new rule includes the steps of the activity. Create the rule, crate input parameters, and finaly create the output parameter. | The full activity will allow automatic determination of the 6 digit CFOP code as per required in SAP system for all legal requirements (NFE, DNAFE and Reporting). |  |
| 6 | Create a New Rule Position Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays.Customer Rules |  |
| 7 | Enter General Data | Make entries according to the company needs:Rule Position: <enter a number which will be considered in sequence by the system to apply the rules created for CFOP extensions determination. For example, 01>Rule Name: <enter CFOP code and operation nature description that defines this rule>Valid From: <Initial date when the rule should apply>Valid To: <Final date when the rule should apply>Note The rule position is used as an access sequence. In case more than one rule exist for the same CFOP, and they are all valid entries, the lowest rule position number will be determined.After rule positions are created, it is possible to change the rule number, thus shifting its position and access sequence as required.Validity period is mandatory, thus insuring that rules are maintained and access as per legal requirements.When rules are no longer required, it is advised to enter an end date instead of deleting the rules. | The rule position created will be accessed during automatic CFOP determination.The input parameters defined under the rule position will be used for the automatic determination. The CFOP determined is the one entered under output parameter. |  |
| 8 | Save Your Data | Save your rule position entry. | The new CFOP Rules is saved and ready for adding input and output parameters. |  |
| 9 | Define the Rule Position Input Parameters Values | Select the rule position created and double click in Input Parameter Values.Note Input parameters shall be created under the rule position created.The input parameters are the parameters available for user combination, in order to achieve the automatic determination of the output parameter (full SAP CFOP code).Among the available parameters is the mandatory parameter “CFOP code as per law Ajuste SINIEF”, which is the 4 digit CFOP code determined by External Tax Calculation Engine Partner. |  |  |
| 10 | Create a New Entry | Choose New Entries.Input Parameter Values.Enter the combination of input parameters as per CFOP determination requirements.Parameter CFOP_CODE is mandatory for every rule position configuration. This represents the CFOP code determined by External Tax Calculation Engine Partner. | The New Entries: Overview of Added Entries screen displays. |  |
| 11 | Enter General Data | Make entries according to the CFOP determination needs. More than one Parameter can be defined to be considered by the system to determine the CFOP Extension defined in the next step Output Parameters Values. CFOP code is a mandatory entry.First select the CFOP code:Parameter: <enter a Parameter available. For example, CFOP CODE>Parameter Value: <Select the Parameter Value available. For example, 5910>Then select other parameters which will help with the determination. For example, Usage Purpose:Parameter: <enter a Parameter available. For example, USAGE PURPOSE>Parameter Value: <Select the Parameter Value available. For example, Usage Purpose for Free Charge>Note Example: CFOP code 5910 in combination with External Tax Calculation Engine’s usage purpose parameter free charge, which is used for Bonus Sales Transaction. | The full combination of input parameters and values are selected |  |
| 12 | Save Your Data | Save your input parameter entries. | The new set of CFOP input parameters is saved. |  |
| 13 | Define the Output Parameter Value | Double click in Output Parameter Values. |  |  |
| 14 | Create a New Entry | Choose New Entries.Enter the parameter and value related to the full SAP CFOP code (CFOP + extension) which contains the description required by law for the sales business transaction. | The New Entries: Overview of Added Entries screen displays.Output Parameter Values. |  |
| 15 | Enter General Data | Make an entry for the full SAP CFOP code to be determined under the rule position:Parameter: <enter parameter “Selected CFOP Code and Extension”>Parameter Value: <Select the Parameter Value available. For example, 5910A1>Note You will notice that the CFOP code entered under input parameters serves as a filter for the selection of the full SAP CFOP code determined under this activity.If the desired full SAP CFOP code ends with “/AA”, this activity is not required, since without any entries maintained under this activity for a CFOP code, External Tax Calculation Engine will automatically add “/AA” to whatever CFOP code is determined by External Tax Calculation Engine. | The user should select in this step the CFOP code with the appropriate extension defined under Item Determine CFOP as parameter value. For example, 5910/A1 for Bonus Shipment. |  |
| 16 | Save Your Data | Save your output parameter entry. | The new CFOP output parameter is saved and now the new CFOP Rules is ready for automatic determination of CFOP code in sales transactions. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Start page displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Configure Rules to Determine CFOP Extension for Sales.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create New Rules | The creation of a new rule includes the steps of the activity. Create the rule, crate input parameters, and finaly create the output parameter. | The full activity will allow automatic determination of the 6 digit CFOP code as per required in SAP system for all legal requirements (NFE, DNAFE and Reporting). |  |
| 4 | Create a New Rule Position Entry | If necessary, choose Edit.Choose New Entries. | The New Entries: Overview of Added Entries screen displays.Customer Rules |  |
| 5 | Enter General Data | Make entries according to the company needs:Rule Position: <enter a number which will be considered in sequence by the system to apply the rules created for CFOP extensions determination. For example, 01>Rule Name: <enter CFOP code and operation nature description that defines this rule>Valid From: <Initial date when the rule should apply>Valid To: <Final date when the rule should apply>Note The rule position is used as an access sequence. In case more than one rule exist for the same CFOP, and they are all valid entries, the lowest rule position number will be determined.After rule positions are created, it is possible to change the rule number, thus shifting its position and access sequence as required.Validity period is mandatory, thus insuring that rules are maintained and access as per legal requirements.When rules are no longer required, it is advised to enter an end date instead of deleting the rules. | The rule position created will be accessed during automatic CFOP determination.The input parameters defined under the rule position will be used for the automatic determination. The CFOP determined is the one entered under output parameter. |  |
| 6 | Save Your Data | Save your rule position entry. | The new CFOP Rules is saved and ready for adding input and output parameters. |  |
| 7 | Define the Rule Position Input Parameters Values | Select the rule position created and double click in Input Parameter Values.Note Input parameters shall be created under the rule position created.The input parameters are the parameters available for user combination, in order to achieve the automatic determination of the output parameter (full SAP CFOP code).Among the available parameters is the mandatory parameter “CFOP code as per law Ajuste SINIEF”, which is the 4 digit CFOP code determined by External Tax Calculation Engine Partner. |  |  |
| 8 | Create a New Entry | Choose New Entries.Input Parameter Values.Enter the combination of input parameters as per CFOP determination requirements.Parameter CFOP_CODE is mandatory for every rule position configuration. This represents the CFOP code determined by External Tax Calculation Engine Partner. | The New Entries: Overview of Added Entries screen displays. |  |
| 9 | Enter General Data | Make entries according to the CFOP determination needs. More than one Parameter can be defined to be considered by the system to determine the CFOP Extension defined in the next step Output Parameters Values. CFOP code is a mandatory entry.First select the CFOP code:Parameter: <enter a Parameter available. For example, CFOP CODE>Parameter Value: <Select the Parameter Value available. For example, 5910>Then select other parameters which will help with the determination. For example, Usage Purpose:Parameter: <enter a Parameter available. For example, USAGE PURPOSE>Parameter Value: <Select the Parameter Value available. For example, Usage Purpose for Free Charge>Note Example: CFOP code 5910 in combination with External Tax Calculation Engine’s usage purpose parameter free charge, which is used for Bonus Sales Transaction. | The full combination of input parameters and values are selected |  |
| 10 | Save Your Data | Save your input parameter entries. | The new set of CFOP input parameters is saved. |  |
| 11 | Define the Output Parameter Value | Double click in Output Parameter Values. |  |  |
| 12 | Create a New Entry | Choose New Entries.Enter the parameter and value related to the full SAP CFOP code (CFOP + extension) which contains the description required by law for the sales business transaction. | The New Entries: Overview of Added Entries screen displays.Output Parameter Values. |  |
| 13 | Enter General Data | Make an entry for the full SAP CFOP code to be determined under the rule position:Parameter: <enter parameter “Selected CFOP Code and Extension”>Parameter Value: <Select the Parameter Value available. For example, 5910A1>Note You will notice that the CFOP code entered under input parameters serves as a filter for the selection of the full SAP CFOP code determined under this activity.If the desired full SAP CFOP code ends with “/AA”, this activity is not required, since without any entries maintained under this activity for a CFOP code, External Tax Calculation Engine will automatically add “/AA” to whatever CFOP code is determined by External Tax Calculation Engine. | The user should select in this step the CFOP code with the appropriate extension defined under Item Determine CFOP as parameter value. For example, 5910/A1 for Bonus Shipment. |  |
| 14 | Save Your Data | Save your output parameter entry. | The new CFOP output parameter is saved and now the new CFOP Rules is ready for automatic determination of CFOP code in sales transactions. |  |

### Define Tax Jurisdiction Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Tax jurisdiction codes are used to tax calulation and to derive data to NF-e:

For calculation of ICMS and SubTrib, the tax region is sufficient for determining where tax is due. In the case of ISS, however, it is additionally necessary to identify the tax jurisdiction code.

The region in NF-e access key and city code are derived from the tax jurisdiction code.

SAP delivers the tax jurisdiction codes, but you may need to create a new one.

Procedure

Enter your required tax jurisdiction codes as follows:

The first three characters must contain the tax region.

The next four to sixteen characters contain the municipal (município) code.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and sub application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Define Tax Jurisdiction Codes.Inform Country/Regio Key ‘BR’. | A popup displays. |  |
| 5 | Create Tax Jurisdiction Codes | If necessary, choose Edit.Select New Entries.Inform the Tax Jurisdiction Code and the Description. Create as many entries as you need. | The New Entries: Overview of Added Entries screen displays. |  |
| 6 | Save Your Data | Choose Save. | Tax jusrisdiction codes are created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Start page displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Tax Jurisdiction Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |

### Assign Postal Codes to Tax Jurisdiction Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you maintain Brazilian address data in master records, once you enter the postal code and geographical region, the system automatically assigns the correct tax jurisdiction code. For that, the assignment between a range of postal codes and the tax jurisdiction code is required.

Procedure

Assign a tax jurisdiction code for a certain range of postal codes of a region.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and sub application area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Assign Postal Codes to Tax Jurisdiction Codes.Inform Country/Regio Key ‘BR’. | A popup displays. |  |
| 5 | Assign Tax Jurisdiction Codes to Ranges of Postal Codes | If necessary, choose Edit.Select New Entries.Inform the region, the first postal code in the range, the last postal code in the range and the tax jurisdiction code. Create as many entries as you need.Note You can use the Mass Upload to upload a CSV file containing a lot of entries. Further guidance in the Configuration Help of the Assign Postal Codes to Tax Jurisdiction Codes.Enter a 9-digit postal code, for example, 69900-000 | The New Entries: Overview of Added Entries screen displays. |  |
| 6 | Save Your Data | Choose Save. | Tax jusrisdiction codes are assigned to ranges of postal codes. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The Start page displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Postal Codes to Tax Jurisdiction Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |

### Assign Tax Rate for Simples Nacional Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to the Complementary Law (LC) 123 of 2006, the tax rates applied for suppliers who opt for the Simples Nacional tax regime are calculated based on the monthly gross revenue of the supplier.

You can configure your system to calculate taxes when purchasing from suppliers under the Simples Nacional tax regime. Before performing a purchase, you must define the ICMS or the ISS tax rate used in the tax calculation in the Assign Tax Rate for Simples Nacional Supplier - Brazil (LOGBR_MM_SIMPLES) app.

Only CRT numbers with options 1 - Simples Nacional or 4 - Simples Nacional - Microempreendedor Individual are considered for this scenario (see Supplier Master Data chapter to fill in this field).

Procedure

Define the ICMS or the ISS tax rate of a supplier under the Simples Nacional tax regime.

The system uses the tax rate you define to calculate taxes in the incoming invoice. It is the rate for the credit, not the rate used by the supplier.

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Tax Specialist for Brazil . | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Tax Rate for Simples Nacional Supplier - Brazil (LOGBR_MM_SIMPLES). |  |  |
| 3 | Create a New Entry | Choose More > New Entries . | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Enter Simples Nacional Definitions | Make the following entries based on your needs:Supplier: <Business Partner’s code/number>Fiscal year: <year>Period: <month>Simples Nacional Classes Table: <company's activity used to determine the tax rate micro and small enterprises>The available classes are the following:1: Class I - Commerce2: Class II - Manufacturing3: Class III - General Services4: Class IV - Labor Intensive Services5: Class V - Intellectual ServicesTax rate: <ICMS or ISS tax rate>Stores the effective ICMS or ISS tax rate for a supplier in a determined period of the fiscal year, according to the Simples Nacional classes.The system uses the tax rate entered for the respective period to perform the tax calculation of the purchase order or the goods receipt for a supplier who opts for the Simples Nacional tax regime.For ICMS, it is the rate for tax credit and not the one used by the vendor. | Tax rates registered to be used in purchasing documents from Simples Nacional suppliers. |  |
| 5 | Save Your Data | Save your entries. | The entries were saved. |  |

### Configure Business Transactions for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you have the Complementary Business Transaction Attributes functionality active in your system, there should be new fields available on the Country tab under Additional Fiscal Data button, at item level, for all relevant sales documents that will replace the usage of SD Tax Code that in a Sales Order should be read-only and automatically determined by the system. SAP already delivers some standard Business Transactions and Usage Purposes to to attend basic scenarios but the customers can customize their own values according to their specific needs. The new fields are:

- Business Transaction - It is the business transaction for this sales process, for example, “Shipment for Demonstration”
- Customer Usage - It is the usage of this material, for example “Resale”
- Usage Purpose - It is an additional information required for this sales process, for example, “First Use”

The new fields shall be manually selected in accordance with the Internal Tax Department guidance for a sales scenario.

It is also possible to create a new business transaction value for the Business Transaction and Usage Purpose codes already delivered by SAP.

|  |
| --- |
| Note The Complementary Business Transaction Attributes functionality is activated by default as of release 2302. |

Procedure

Follow the steps detailed below to create a custom Business Transaction for sales transactions.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and subapplication area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Configure Business Transactions. | The user should create a custom Business Transaction according to a specific business process. |  |
| 5 | Create a New Custom Business Transaction | If necessary, choose Edit.Select Custom Business Transactions in Dialog Structure on the left.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:Business Transaction Code: <enter a custom Business Transaction code that begins with the letter X, Y or Z. For example, Z_DEMONSTRATION_FOR_SHIPMENT>Business Transaction Value: <enter a custom Business Transaction value that begins with a number or with X, Y or Z up to 4 digits>Business Transaction Description: <enter a custom Business Transaction description>Note If required, you can reuse a Business Transaction Code delivered by SAP and add your own Business Transaction Value. | The custom Business Transaction created will be available for selection during Sales Order creation in Country Tab. |  |
| 7 | Save Your Data | Save your rule position entry. | The new custom Business Transaction is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Configure Business Transactions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New Custom Business Transaction | If necessary, choose Edit.Select Custom Business Transactions in Dialog Structure on the left.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Business Transaction Code: <enter a custom Business Transaction code that begins with the letter X, Y or Z. For example, Z_DEMONSTRATION_FOR_SHIPMENT>Business Transaction Value: <enter a custom Business Transaction value that begins with a number or with X, Y or Z up to 4 digits>Business Transaction Description: <enter a custom Business Transaction description>Note If required, you can reuse a Business Transaction Code delivered by SAP and add your own Business Transaction Value. | The custom Business Transaction created will be available for selection during Sales Order creation in Country Tab. |  |
| 5 | Save Your Data | Save your rule position entry. | The new custom Business Transaction is created. |  |

### Configure Usage Purposes for Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you have the Complementary Business Transaction Attributes functionality active in your system, there should be new fields available on the Country tab under Additional Fiscal Data button, at item level, for all relevant sales documents that will replace the usage of SD Tax Code that in a Sales Order should be read-only and automatically determined by the system. SAP already delivers some standard Business Transactions and Usage Purposes to attend basic scenarios but the customers can customize their own values according to their specific needs. The new fields are:

- Business Transaction - It is the business transaction for this sales process, for example, “Shipment for Demonstration”
- Customer Usage - It is the usage of this material, for example, “Resale”
- Usage Purpose - It is an additional information required for this sales process, for example, “First Use”

The new fields shall be manually selected in accordance with the Internal Tax Department guidance for a sales scenario.

It is also possible to create a new business transaction value for the Business Transaction and Usage Purpose codes already delivered by SAP.

|  |
| --- |
| Note The Complementary Business Transaction Attributes functionality is activated by default as of release 2302. |

Procedure

Follow the steps detailed below to create a custom Usage Purpose for sales transactions.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of Configuration Step displays. |  |
| 3 | Filter the Proper Configuration Step | Filter by application area Application Platform and Infrastructure and subapplication area Legal Compliance. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Configure Usage Purpose. |  |  |
| 5 | Create a New custom Usage Purpose | If necessary, choose Edit.Select Customer Usage Purpose in Dialog Structure on the left.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:Usage Purpose Code: <enter a custom Usage Purpose code that begins with the letter X, Y or Z.>Usage Purpose Value: <enter a custom Usage Purpose value that begins with the letter X, Y or Z>Usage Purpose Description: <enter a custom Usage Purpose description>Note If required, you can reuse a Usage Purpose Code delivered by SAP and add your own Usage Purpose Value. | The custom Usage Purpose created will be accessed during Sales Order creation in Country Tab. |  |
| 7 | Save Your Data | Save your input parameter entries. | The new custom Usage Purpose is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Configure Usage Purpose.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a New custom Usage Purpose | If necessary, choose Edit.Select Customer Usage Purpose in Dialog Structure on the left.Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Usage Purpose Code: <enter a custom Usage Purpose code that begins with the letter X, Y or Z.>Usage Purpose Value: <enter a custom Usage Purpose value that begins with the letter X, Y or Z>Usage Purpose Description: <enter a custom Usage Purpose description>Note If required, you can reuse a Usage Purpose Code delivered by SAP and add your own Usage Purpose Value. | The custom Usage Purpose created will be accessed during Sales Order creation in Country Tab. |  |
| 5 | Save Your Data | Save your input parameter entries. | The new custom Usage Purpose is created. |  |

### Transfer Pricing Condition Value to Notas Fiscais for Material Management (MM)⁠

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Define which MM-condition will be mapped to Nota Fiscal.

Procedure

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Start page displays.In this activity, the system determines the service type number using the material number, jurisdiction code and direction of movement. |  |
| 2 | Open Manage Your Solution | Open Manage Your Solution (F1241), set country Brazil and choose Configure Your Solution. | The list of SSCUI displays. |  |
| 3 | Filter the Proper SSCUI | Filter by Application Area Sourcing and Procurement, Sub-Application Area Invoice Processing and Configuration Item Name Incoming Invoice. |  |  |
| 4 | Open Brazil Tax Determination | Choose Configure for Assign Specifier Code of Substituição Tributária. |  |  |
| 5 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 6 | Enter General Data | Make entries according to the company needs:Usage: <A >Application: <M>Procedure: <ABR001>Condition Type: <MM pricing condition>NF Value field: <NF value field>Description: <Description of the condition>ST base mod: < >ST fr. Base: < >Description: < >Description: < > | The user should fill the Pricing Condition that will be mapped to Nota Fiscal. |  |
| 7 | Save Your Data | Save your entries. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Assign Specifier Code of Substituição Tributária.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Select New Entries | Choose Edit if necessary.Choose New Entries. | The New Entries: Details of Added Entries screen displays. |  |
| 4 | Enter General Data | Make entries according to the company needs:Usage: <A >Application: <M>Procedure: <ABR001>Condition Type: <MM pricing condition>NF Value field: <NF value field>Description: <Description of the condition>ST base mod: < >ST fr. Base: < >Description: < >Description: < > | The user should fill the Pricing Condition that will be mapped to Nota Fiscal. |  |
| 5 | Save Your Data | Save your entries. |  |  |

### Configure the Additional Fiscal Data (AFD) Fields for Material Management (MM)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Additional Fiscal Data are configurable values to provide all further information needed by external tax calculation partners, in order to determine accurate taxation.

Procedure

|  |
| --- |
| Note Some standard values will be already delivery by SAP and the customer can also add your own data to the table. The new configured values must be explained and aligned with the tax calculation partner, so they know and understand which purchasing scenario is being performed. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The app opens. |  |
| 3 | Display Configuration Steps | Select Brazil from the Set Local Version dropdown list and choose Configure Your Solution. | The list of configuration steps displays. |  |
| 4 | Filter the Proper Configuration Step | Select Application Platform and Infrastructure from the Application Platform dropdown list, select Legal Compliance from the Sub Application Area dropdown list, and select the row with Brazil Tax Determination as its Item Name. | The Configuration Steps of Brazil Tax Determination displays. |  |
| 5 | Open Brazil Tax Determination | Select Configure Complementary Business Attributes for Materials Management and choose Configure. | The Configure Complementary Business Attributes..:Change screen displays. |  |
| 6 | Select New Entries | On the Configure Complementary Business Attributes..:Change page, choose Edit > New Entries .Note Namespace restriction is applied on the key fields of an application.Customers cannot create records starting with below mentioned SAP best practice content namespace restrictions.SAP reserved character fields - S, Q, R, X, P, Y.SAP reserved numeric fields - 5, 6, 7, 8, 9, 0.Enter in the Bus. Trans. field and Description field to create a new business transaction and choose Save.Select the created business transaction and choose the Usage Purpose folder.Choose New Entries.Enter in the Usage Purpose field and Description field to create a new usage for the Business Transaction. | New records must be entered without error. |  |
| 7 | Save Your Data | Save your entries. | The new Business Transaction with Usage Purpose is created. |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: ICMS Tax Law step labels the key as 'ICMS Law: 3 digit key which will identify the ISS Tax Law' (likely copy error).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Incoming service types procedure instructs choosing 'Define Official Brazilian Service Types for Outgoing Notas Fiscais' (likely copy error from outgoing section).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Several CPRB steps label Company Code field as '<Supplier code/number>' and Purchase CPRB titles differ slightly from app names (Sales Material vs Materials).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Withholding tax code lists for customers/suppliers vary (e.g. IW/IW described as ISS in sales and INSS in financial list; RF/RF vs RF/1R, NS/1N), possibly inconsistent.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/JD0_S4CLD2608_Master_Data_EN_BR.docx` — full document · extracted with `mammoth` · 241,264 chars in the whole document
