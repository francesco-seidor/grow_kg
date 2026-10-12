---
id: 13-quality-ehs-and-compliance/classification-for-customs-tariff-number-and-commodity-code-2u3-ae-868
title: Classification for Customs Tariff Number and Commodity Code (2U3_AE) (2U3_S4CLD2608_BPD_EN_AE)
description: "Test script for SAP S/4HANA Cloud 2608 (AE) scope item 2U3_AE: maintaining and classifying commodity codes and customs tariff numbers, incl. AI options."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/trade-classification-and-legal-control]
aliases: [2U3_S4CLD2608_BPD_EN_AE]
keywords: [Trade Classification and Legal Control, commodity codes, customs tariff numbers, product classification, product reclassification, numbering schemes, data provider content, trade classification agent, ai-assisted classification, fuzzy search proposals]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-868
topic: 13-quality-ehs-and-compliance/trade-classification-and-legal-control
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Classification for Customs Tariff Number and Commodity Code (2U3_AE) (2U3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Trade Classification and Legal Control** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Classification for Customs Tariff Number and Commodity Code (2U3_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Classification for Customs Tariff Number and Commodity Code (2U3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850475)

[2 Prerequisites 4](#_Toc232850476)

[2.1 Additional Manual Configuration 4](#_Toc232850477)

[2.2 System Access 4](#_Toc232850478)

[2.3 Roles 4](#_Toc232850479)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232850480)

[2.5 Preliminary Steps 6](#_Toc232850481)

[2.5.1 Prerequisite Configuration Activities Without DEMO Data 6](#_Toc232850482)

[2.5.2 Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers from Data Provider (Optional) 17](#_Toc232850483)

[2.5.3 Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional) 20](#_Toc232850484)

[2.5.4 Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers with International Trade Classification Agent (Optional) 23](#_Toc232850485)

[2.5.4.1 Prerequisite Configuration Activities 23](#_Toc232850486)

[2.5.4.2 Master Data 25](#_Toc232850487)

[3 Overview Table 27](#_Toc232850488)

[4 Test Procedures 30](#_Toc232850489)

[4.1 Manage Commodity Codes 30](#_Toc232850490)

[4.2 Manage Commodity Codes from Data Provider (Optional) 31](#_Toc232850491)

[4.2.1 Schedule Commodity Codes Content Request to Data Provider (Background Job) 31](#_Toc232850492)

[4.2.2 Manage Commodity Codes Content from Data Provider 32](#_Toc232850493)

[4.3 Classify Products Commodity Codes 34](#_Toc232850494)

[4.3.1 Classify Products Commodity Codes 34](#_Toc232850495)

[4.3.2 Classify Products Commodity Codes using the International Trade Classification Agent (Optional) 35](#_Toc232850496)

[4.4 Reclassify Products Commodity Codes (Optional) 37](#_Toc232850497)

[4.5 Classify Products Commodity Codes with AI-Assisted Generation of Trade Classification Proposals (Optional) 38](#_Toc232850498)

[4.5.1 Create Products 39](#_Toc232850499)

[4.5.2 Manage Commodity Codes 39](#_Toc232850500)

[4.5.3 Classify Products Commodity Codes 40](#_Toc232850501)

[4.5.4 Schedule Creation of Trade Classification Attributes Fuzzy Search 41](#_Toc232850502)

[4.5.5 Schedule Creation of Trade Classification Proposals Fuzzy Search 42](#_Toc232850503)

[4.5.6 Activate Classification Proposal Commodity Code 43](#_Toc232850504)

[4.5.7 Schedule Simulation of Trade Classification Proposals Fuzzy Search 44](#_Toc232850505)

[4.6 Manage Customs Tariff Numbers 45](#_Toc232850506)

[4.7 Manage Customs Tariff Numbers from Data Provider (Optional) 46](#_Toc232850507)

[4.7.1 Schedule Customs Tariff Numbers Content Request to Data Provider (Background Job) 47](#_Toc232850508)

[4.7.2 Manage Customs Tariff Numbers Content from Data Provider 48](#_Toc232850509)

[4.8 Classify Products Customs Tariff Numbers 49](#_Toc232850510)

[4.8.1 Classify Products Customs Tariff Numbers 49](#_Toc232850511)

[4.8.2 Classify Products Customs Tariff Numbers using the International Trade Classification Agent (Optional) 50](#_Toc232850512)

[4.9 Reclassify Products Customs Tariff Numbers (Optional) 52](#_Toc232850513)

[4.10 Classify Products Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional) 54](#_Toc232850514)

[4.10.1 Manage Customs Tariff Numbers 54](#_Toc232850515)

[4.10.2 Classify Products Customs Tariff Numbers 55](#_Toc232850516)

[4.10.3 Schedule Creation of Trade Classification Attributes Fuzzy Search 56](#_Toc232850517)

[4.10.4 Schedule Creation of Trade Classification Proposals Fuzzy Search 57](#_Toc232850518)

[4.10.5 Activate Classification Proposal Customs Tariff Numbers 58](#_Toc232850519)

[4.10.6 Schedule Simulation of Trade Classification Proposals Fuzzy Search 59](#_Toc232850520)

[4.11 Display Classification Decisions with Agent Assistance (Optional) 60](#_Toc232850521)

[4.11.1 Display Classified Products 60](#_Toc232850522)

[4.11.2 Display Classification Decisions with Agent Assistance (Optional) 61](#_Toc232850523)

## Purpose

Overview

This scope item provides the business processes to maintain tariff codes and commodity codes. The defined codes can be assigned to products for proper classification.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/eb72674b6e8727467c91d75ac795e295)

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Trade Classification Specialist | SAP_BR_TRD_CLS_SPECIALIST | International Trade Classification | SAP_BR_TRD_CLS_SPECIALIST | Please ask your system administrator to assign to the testers. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Please ask your system administrator to assign to the testers. |
| Administrator - International Trade | SAP_BR_ADMINISTRATOR_SLL | International Trade Administration | SAP_BR_ADMINISTRATOR_SLL | Please ask your system administrator to assign to the testers. |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and suppliers for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 | Company Code for AE |  |
| Material | TG11 | Trading Goods |  |
| Material | TG10 | Trading Goods |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Preliminary Steps

#### Prerequisite Configuration Activities Without DEMO Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter is only needed when the scope item has been activated without Demo Data. In a SAP S/4HANA Cloud Public Edition system without pre-delivered Demo Data, we recommend you configure the settings described here using the Configuration Activities before starting to test.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Navigate | Open Manage Your Solution (F1241) and navigate to Configure Your Solution.Note Search for the apps in the subsequent test steps. Choose the row that appears in the list. In the second screen, the searched app is viewed. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution - Classification | In the Configure Your Solution: Realize Phase view, make the following entries:Application Area: FinanceSub Application Area: International Trade ManagementIn the Item Name column, choose Classification. | The Configure Your Solution - Classification screen is displayed. |  |
| 4 | Define Numbering Scheme for Commodity Codes | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the table, search for the Define Numbering Scheme for Commodity Codes and choose Configure.Choose New Entries and maintain as follows：Scheme: AE01Description: Commodity Codes for AEChoose SAVE. | Numbering scheme is defined. |  |
| 5 | Define Numbering Scheme Content for Commodity Codes | In the Configuration Steps area and in the Step Name column of the table, search for the Define Numbering Scheme Content for Commodity Codes and choose Configure.Choose New Entries and maintain as follows.No. Scheme Content: AE01Description: Commodity Codes for AEContent Source: LocalChoose SAVE. | Numbering scheme content is defined for Commodity Codes |  |
| 6 | Activate Numbering Scheme Content for Commodity Codes | In the Configuration Steps area and in the Step Name column of the table, search for the Activate Numbering Scheme Content for Commodity Codes and choose Configure.In the Determine Work Area: Entry screen, maintain Numbering Scheme: AE01 and choose Continue (Enter).Choose New Entries and maintain as followsValid From: 01.01.1900Valid To: 30.12.9999No. Scheme Content: AE01Choose SAVE. | Numbering scheme content is activated. |  |
| 7 | Define Numbering Scheme for Customs Tariff Numbers | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the table, search for the Define Numbering Scheme for Customs Tariff Numbers and choose Configure.Make the following entries and choose Save:Scheme: AE04Description: Customs Tariff Numbers for AE | Numbering scheme is defined. |  |
| 8 | Define Numbering Scheme Content for Customs Tariff Numbers | In the Configuration Steps area and in the Step Name column of the table, search for the Define Numbering Scheme Content for Customs Tariff Numbers and choose Configure.Choose New Entries.No. Scheme Content: AE04Source: LocalDescription: Customs Tariff Numbers for AEChoose SAVE. | Numbering scheme content is defined for Customs Tariff Numbers. |  |
| 9 | Activate Numbering Scheme Content for Customs Tariff Numbers | In the Configuration Steps area and in the Step Name column of the table, search for the Activate Numbering Scheme Content for Customs Tariff Numbers and choose Configure.In the Determine Work Area: Entry screen, maintain Numbering Scheme : AE04 and choose Continue (Enter).Choose New Entries.Scheme: AE04Valid From: 01.01.1900Valid To: 30.12.9999No. Scheme Content: AE04Choose SAVE. | Numbering scheme content is activated. |  |
| 10 | Assign Numbering Scheme for Commodity Codes to Country | In the Configuration Steps area and in the Step Name column of the table, search for the Assign Numbering Scheme for Commodity Codes to Country and choose Configure.Choose New Entries.Country: AEDescription: United Arab EmiratesNumbering Scheme: AE01Description: Commodity Codes for USChoose SAVE. | Numbering scheme is assigned for commodity codes to country. |  |
| 11 | Assign Numbering Scheme for Customs Tariff Numbers to Country | In the Configuration Steps area and in the Step Name column of the table, search for the Assign Numbering Scheme for Customs Tariff Numbers to Country and choose Configure.Choose New Entries.Country: AEDescription: United Arab EmiratesNumbering Scheme: AE04Description: Customs Tariff Numbers for AEChoose SAVE. | Numbering scheme is assigned for customs tariff numbers to country/region |  |
| 12 | Define Unit of Measure System | In the Configuration Steps area and in the Step Name column of the table, search for the Define Unit of Measure System and choose Configure.Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUSelect the line of UOM_EU and in the Dialog Structure pane, double-click Customs Unit of Measure.Maintain the following entries:Customs Unit of MeasureDescriptionASV%volASVX%vol/hectolitersCCTCarrying capacity in tonnesCENHundred itemsCTMCarats(1 metric carat=2 x 10-4 kg)DAPDecatonDTN100 kilogramsDTNEHectokilogram net drained weightDTNFHectokilogram net soft wheatDTNGHectokilogram net raw weightDTNMHectokilogram net dry matterDTNNHectokilogram dead weightDTNRHectokilogram raw sugar with a yield of 92%DTNSHectokilogram white sugarDTNZHectokilogram per 1% by weight of sucroseGFIGram of fissile isotopesGRMGramGRTGross tonnageHLTHectolitreKACKg net Ace KKCCKilograms of choline chlorideKCLTonne of potassium chlorideKGMkilogramKGMAkilograms total alcoholKGMBkilograms gross weightKGMEkilogram drained net weightKGMNKilogram dead weightKGMPKilogram of lactic matterKGMSkg of raw sugarKGMTKilogram dry lactic matterKLT1000 LitreKMAKilogram of methylaminesKMTKilometerKNIKilogram of nitrogenKNSKilogram of hydrogen peroxideKPHKilogram of Potassium hydroxide(Caustic potash)KPOKilogram of potassium oxideKPPKilogram of diphosphorus pentaoxideKSDKilogram of substance 90% dryKSHKilogram of sodium hydroxide(caustic soda)KURKilogram of uraniumLPALitre pure(100%) alcoholLTRLitreMILThousand itemsMTKSquare metersMTQCubic metersMTQCThousand cubic metersMTRMeterMWHMegawatt hoursNARNumber of itemsNARBper bottleNCLNumber of cellsNPRNumber oof pairsTJOTerajoule (gross calorific value)TNETonne netTNEGTonne net gross weightTNEI1000 kg/biodieselTNEJ1000 kg/ fuel contentTNEKTonne Bioethanol contentTNEM1000 kg/ net dry weightTNEN1000 kg/ net dead weightTNEZ1000 kg/ net / % saccharWATWatt |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Define Numbering Scheme for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Customs Tariff Numbers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Numbering Scheme for Customs Tariff Numbers screen displays. |  |
| 3 | Define Numbering Scheme for Customs Tariff Numbers | Choose New Entries and maintain as follows:Scheme: AE01Description: Commodity Codes for AEChoose SAVE. | Numbering scheme is defined. |  |
| 4 | Define Numbering Scheme Content for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme Content for Commodity Codes.Choose New Entries and maintain as follows.No. Scheme Content: AE01Description: Commodity Codes for AEContent Source: LocalChoose SAVE. | Numbering scheme content is defined for Commodity Codes |  |
| 5 | Activate Numbering Scheme Content for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Activate Numbering Scheme Content for Commodity Codes.In the Determine Work Area: Entry screen, maintain Numbering Scheme: AE01 and choose Continue (Enter).Choose New Entries and maintain as followsValid From: 01.01.1900Valid To: 30.12.9999No. Scheme Content: AE01Choose SAVE. | Numbering scheme content is activated. |  |
| 6 | Define Numbering Scheme for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Customs Tariff Numbers.Make the following entries and choose Save:Scheme: AE04Description: Customs Tariff Numbers for AE | Numbering scheme is defined. |  |
| 7 | Define Numbering Scheme Content for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme Content for Customs Tariff Numbers.Choose New Entries.No. Scheme Content: AE04Source: LocalDescription: Customs Tariff Numbers for AEChoose SAVE. | Numbering scheme content is defined for Customs Tariff Numbers. |  |
| 8 | Activate Numbering Scheme Content for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Activate Numbering Scheme Content for Customs Tariff Numbers.In the Determine Work Area: Entry screen, maintain Numbering Scheme : AE04 and choose Continue (Enter).Choose New Entries.Scheme: AE04Valid From: 01.01.1900Valid To: 30.12.9999No. Scheme Content: AE04Choose SAVE. | Numbering scheme content is activated. |  |
| 9 | Assign Numbering Scheme for Commodity Codes to Country | Go to the Business Processes Configuration app and search for the following activity: Assign Numbering Scheme for Commodity Codes to Country.Choose New Entries.Country: AEDescription: United Arab EmiratesNumbering Scheme: AE01Description: Commodity Codes for USChoose SAVE. | Numbering scheme is assigned for commodity codes to country. |  |
| 10 | Assign Numbering Scheme for Customs Tariff Numbers to Country | Go to the Business Processes Configuration app and search for the following activity: Assign Numbering Scheme for Customs Tariff Numbers to Country.Choose New Entries.Country: AEDescription: United Arab EmiratesNumbering Scheme: AE04Description: Customs Tariff Numbers for AEChoose SAVE. | Numbering scheme is assigned for customs tariff numbers to country/region. |  |
| 11 | Define Measure System | Go to the Business Processes Configuration app and search for the following activity: Define Unit of Measure System.Choose New Entries.Unit of Measure System: UOM_EUDescription: Measure System for EUSelect the line of UOM_EU and in the Dialog Structure pane, double-click Customs Unit of Measure.Maintain the following entries:Customs Unit of MeasureDescriptionASV%volASVX%vol/hectolitersCCTCarrying capacity in tonnesCENHundred itemsCTMCarats(1 metric carat=2 x 10-4 kg)DAPDecatonDTN100 kilogramsDTNEHectokilogram net drained weightDTNFHectokilogram net soft wheatDTNGHectokilogram net raw weightDTNMHectokilogram net dry matterDTNNHectokilogram dead weightDTNRHectokilogram raw sugar with a yield of 92%DTNSHectokilogram white sugarDTNZHectokilogram per 1% by weight of sucroseGFIGram of fissile isotopesGRMGramGRTGross tonnageHLTHectolitreKACKg net Ace KKCCKilograms of choline chlorideKCLTonne of potassium chlorideKGMkilogramKGMAkilograms total alcoholKGMBkilograms gross weightKGMEkilogram drained net weightKGMNKilogram dead weightKGMPKilogram of lactic matterKGMSkg of raw sugarKGMTKilogram dry lactic matterKLT1000 LitreKMAKilogram of methylaminesKMTKilometerKNIKilogram of nitrogenKNSKilogram of hydrogen peroxideKPHKilogram of Potassium hydroxide(Caustic potash)KPOKilogram of potassium oxideKPPKilogram of diphosphorus pentaoxideKSDKilogram of substance 90% dryKSHKilogram of sodium hydroxide(caustic soda)KURKilogram of uraniumLPALitre pure(100%) alcoholLTRLitreMILThousand itemsMTKSquare metersMTQCubic metersMTQCThousand cubic metersMTRMeterMWHMegawatt hoursNARNumber of itemsNARBper bottleNCLNumber of cellsNPRNumber oof pairsTJOTerajoule (gross calorific value)TNETonne netTNEGTonne net gross weightTNEI1000 kg/biodieselTNEJ1000 kg/ fuel contentTNEKTonne Bioethanol contentTNEM1000 kg/ net dry weightTNEN1000 kg/ net dead weightTNEZ1000 kg/ net / % saccharWATWatt |  |  |

#### Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers from Data Provider (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter is only needed if you activated the scope item without Demo Data. As a result, the system does not contain the predelivered Demo Data configuration; you must maintain all the following configurations by SSCUIs before performing testing. We recommend that you configure SSCUIs before starting to test in SAP S/4HANA Cloud Public Edition system.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Navigate | Open Manage Your Solution (F1241) and navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution - Classification | In the Configure Your Solution: Realize Phase screen, select Application Area Finance, Sub Application Area International Trade. Then the Configuration Items will be searched out. In the search result screen, choose the item named Classification.Search for apps mentioned in subsequent Test Step Name respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Configure Your Solution - Classification screen is displayed. |  |
| 4 | Define Numbering Scheme Content for Commodity Codes | Choose New Entries.No. Scheme Content: AE01_DPDescription: Commodity Codes for AEContent Source: Data ProviderData Provider ID: For example, _A ReguvisContent Reference: <Please check with data provider>Number Length: 8Unit of Measure System: Measure System for EUChoose SAVE. | Note It is an optional step. If the commodity codes are retrieved by external data provider and the connection with external data provider is established, please perform the step.The Numbering scheme content is defined for commodity codes. |  |
| 5 | Define Numbering Scheme Content for Customs Tariff Numbers | Choose New Entries.No. Scheme Content: AE04_DPDescription: Commodity Codes for AEContent Source: Data ProviderData Provider ID: For example, _A ReguvisContent Reference: <Please check with data provider>Number Length: 10Unit of Measure System: Measure System for EUChoose SAVE. | It is an optional step. If the Customs Tariff Numbers are retrieved from external data provider and the connection with external data provider is established, please perform the step.The Numbering scheme content is defined for Customs Tariff Numbers. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Define Numbering Scheme Content for Commodity Codes | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme Content for Commodity Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Numbering Scheme Content for Commodity Codes screen displays. |  |
| 3 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 4 | Define Numbering Scheme Content for Commodity Codes | Choose New Entries.No. Scheme Content: AE01_DPDescription: Commodity Codes for AEContent Source: Data ProviderData Provider ID: For example, _A ReguvisContent Reference: <Please check with data provider>Number Length: 8Unit of Measure System: Measure System for EUChoose SAVE. | Note It is an optional step. If the commodity codes are retrieved by external data provider and the connection with external data provider is established, please perform the step.The Numbering scheme content is defined for commodity codes. |  |
| 5 | Open Define Numbering Scheme Content for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme Content for Customs Tariff Numbers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Numbering Scheme Content for Customs Tariff Numbers screen displays. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 7 | Define Numbering Scheme Content for Customs Tariff Numbers | Choose New Entries.No. Scheme Content: AE04_DPDescription: Commodity Codes for AEContent Source: Data ProviderData Provider ID: For example, _A ReguvisContent Reference: <Please check with data provider>Number Length: 10Unit of Measure System: Measure System for EUChoose SAVE. | It is an optional step. If the Customs Tariff Numbers are retrieved from external data provider and the connection with external data provider is established, please perform the step.The Numbering scheme content is defined for Customs Tariff Numbers. |  |

#### Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional)

Purpose

Starting from SAP S/4HANA Cloud Public Edition 2508 and onwards, AI-Assisted Generation of trade classification proposals for commodity codes and custom tariff numbers will be assigned to products through a similarity search conducted on existing product classifications utilizing SAP HANA fuzzy search technology.

Please ensure the following configurations are maintained using Configuration Activities before proceeding with steps: Classify Products Commodity Codes with AI-Assisted Generation of Trade Classification Proposals (Optional) and Classify Products Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Navigate | Open Manage Your Solution (F1241) and navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution - Classification | In the Configure Your Solution: Realize Phase screen, make the following entries:Application Area: FinanceSub Application Area: International Trade ManagementIn the Item Name column, choose Classification. | The Configure Your Solution - Classification screen is displayed. |  |
| 4 | Define Numbering Scheme for Commodity Codes | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the section, search for Define Numbering Scheme for Commodity Codes and choose Configure.Choose Numbering Scheme: AE01 and maintain the attributes as follows:Numbering Scheme: AE01Fuzzy Search Active: <select>Fuzzy AI Attributes Language: EN (The language requires product descriptions in English)Fuzzy Search Min. Text Score: <for example, 75%>Fuzzy Search And Threshold: <for example, 80%>Fuzzy Search Exactness: <for example, 80%>Note You can check [FUZZY Search \| SAP Help Portal](https://help.sap.com/docs/SAP_HANA_PLATFORM/691cb949c1034198800afde3e5be6570/cc602780bb5710148aa2bf6cab3c015b.html?locale=en-US) for Fuzzy Search technology.Choose SAVE. | Numbering scheme with Fuzzy Search is saved. |  |
| 5 | Define Numbering Scheme for Customs Tariff Numbers | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the section, search for Define Numbering Scheme for Customs Tariff Numbers and choose Configure.Choose Numbering Scheme: AE04 and maintain the attributes as follows:Numbering Scheme: AE04Fuzzy Search Active: <select>Fuzzy AI Attributes Language: ENFuzzy Search Min. Text Score: <for example, 75%>Fuzzy Search And Threshold: <for example, 80%>Fuzzy Search Exactness: <for example, 80%>Choose SAVE. | Numbering scheme with Fuzzy Search is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Search for Define Numbering Scheme for Commodity Codes | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Commodity Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Define Numbering Scheme for Commodity Codes | Choose Numbering Scheme: AE01 and maintain the attributes as follows:Numbering Scheme: AE01Fuzzy Search Active: <select>Fuzzy AI Attributes Language: EN (The language requires product descriptions in English)Fuzzy Search Min. Text Score: <for example, 75%>Fuzzy Search And Threshold: <for example, 80%>Fuzzy Search Exactness: <for example, 80%>Note You can check [FUZZY Search \| SAP Help Portal](https://help.sap.com/docs/SAP_HANA_PLATFORM/691cb949c1034198800afde3e5be6570/cc602780bb5710148aa2bf6cab3c015b.html?locale=en-US) for Fuzzy Search technology.Choose SAVE. | Numbering scheme with Fuzzy Search is saved. |  |
| 4 | Search for Define Numbering Scheme for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Customs Tariff Numbers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Define Numbering Scheme for Customs Tariff Numbers | Choose Numbering Scheme: AE04 and maintain the attributes as follows:Numbering Scheme: AE04Fuzzy Search Active: <select>Fuzzy AI Attributes Language: ENFuzzy Search Min. Text Score: <for example, 75%>Fuzzy Search And Threshold: <for example, 80%>Fuzzy Search Exactness: <for example, 80%>Choose SAVE. | Numbering scheme with Fuzzy Search is defined. |  |

#### Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers with International Trade Classification Agent (Optional)

##### Prerequisite Configuration Activities

Purpose

Starting from SAP S/4HANA Cloud Public Edition 2608 and onwards, you can classify products by commodity code and customs tariff number with the assistance of the International Trade Classification Agent.

You need to maintain the following configurations by configuration activities before performing steps [Classify Products Commodity Codes using the International Trade Classification Agent (Optional)](#unique_11) [page ] 35 and [Classify Products Customs Tariff Numbers using the International Trade Classification Agent (Optional)](#unique_12) [page ] 50.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Navigate | Open Manage Your Solution (F1241) and navigate to Configure Your Solution.Search for apps mentioned in subsequent test steps respectively. Choose the row that appears in the list. On the second screen you would see the searched app. Choose Configure. Please proceed ahead with further steps described in the document. | The Manage Your Solution screen is displayed. |  |
| 3 | Configure Your Solution - Classification | In the Configure Your Solution: Realize Phase screen, make the following entries:Application Area: FinanceSub Application Area: International Trade ManagementIn the Item Name column, choose Classification. | The Configure Your Solution - Classification screen is displayed. |  |
| 4 | Define Numbering Scheme for Commodity Codes | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the section, search for Define Numbering Scheme for Commodity Codes and choose Configure.Choose Numbering Scheme: AE01 and maintain the attributes as follows:AI-Assisted Trade ClassificationLanguage: ENChoose SAVE. | Numbering scheme with Fuzzy Search is saved. |  |
| 5 | Define Numbering Scheme for Customs Tariff Numbers | Choose the > (Details) button of the item.In the Configuration Steps area and in the Step Name column of the section, search for Define Numbering Scheme for Customs Tariff Numbers and choose Configure.Choose Numbering Scheme: AE04 and maintain the attributes as follows:AI-Assisted Trade ClassificationLanguage: ENChoose SAVE. | Numbering scheme with Fuzzy Search is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Search for Define Numbering Scheme for Commodity Codes | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Commodity Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage Your Solution screen is displayed. |  |
| 3 | Define Numbering Scheme for Commodity Codes | Choose Numbering Scheme: AE01 and maintain the attributes as follows:AI-Assisted Trade ClassificationLanguage: ENChoose SAVE. | Numbering scheme with Fuzzy Search is saved. |  |
| 4 | Search for Define Numbering Scheme for Customs Tariff Numbers | Go to the Business Processes Configuration app and search for the following activity: Define Numbering Scheme for Customs Tariff Numbers.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 5 | Define Numbering Scheme for Customs Tariff Numbers | Choose Numbering Scheme: AE04 and maintain the attributes as follows:AI-Assisted Trade ClassificationLanguage: ENChoose SAVE. | Numbering scheme with Fuzzy Search is defined. |  |

##### Master Data

Purpose

In this activity, you create a product with specific material descriptions.

Procedure

Please refer to Master Data Scripts (MDS) documentation BNF - Create Product Master of type "Trading Good" - MDS to create following two Material (Product) Master Data - Basic Data with following material numbers and attributes.

Material: ZSK_AI_01_FLASK

Description: Thermo Flask

Base Unit of Measure: PC

Material Group: L001

GenItemCatGroup: NORM

Gross Weight: 670

Net Weight: 550

Unit of Weight: G

Volume: 1.200

Volume Unit: L

Size/dimensions: 12 X 12 X 38 CM

EAN/UPC: 5010576966483

EAN Category: HE

## Overview Table

Process steps of this scope item are provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Commodity Codes](#unique_15) [page ] 30 | Trade Classification Specialist | Manage Commodity Codes (F2516) | Commodity Code is created / changed. |
| [Manage Commodity Codes from Data Provider (Optional)](#unique_16) [page ] 31 |  |  |  |
| [Schedule Commodity Codes Content Request to Data Provider (Background Job)](#unique_17) [page ] 31 | Administrator - International Trade | Schedule Content Request to Data Provider - Commodity Codes (F3051) | Commodity Codes are created base on the data from Data Providers. |
| [Manage Commodity Codes Content from Data Provider](#unique_18) [page ] 32 | Trade Classification Specialist | Manage Content from Data Provider - Commodity Codes (F3429) | Commodity Codes are created base on the data from Data Providers. |
| Classify Products Commodity Codes |  |  |  |
| [Classify Products Commodity Codes](#unique_19) [page ] 34 | Trade Classification Specialist | Classify Products - Commodity Codes (F2151) | Commodity codes are assigned to products. |
| [Classify Products Commodity Codes using the International Trade Classification Agent (Optional)](#unique_11) [page ] 35 | Trade Classification Specialist | Classify Products - Commodity Codes (F2151) | Commodity Codes are classified by using the International Trade Classification Agent. |
| [Reclassify Products Commodity Codes (Optional)](#unique_20) [page ] 37 | Trade Classification Specialist | Reclassify Products - Commodity Codes (F2152) | Commodity codes are changed for products. |
| [Classify Products Commodity Codes with AI-Assisted Generation of Trade Classification Proposals (Optional)](#unique_21) [page ] 38 |  |  |  |
| [Create Products](#unique_22) [page ] 39 | Please refer to [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2502-master-data/start?locale=en-US) documentation BNF - Create Product Master of type "Trading Good" - MDS |  |  |
| [Manage Commodity Codes](#unique_23) [page ] 39 | Trade Classification Specialist | Manage Commodity Codes (F2516) | Commodity Codes are created. |
| [Classify Products Commodity Codes](#unique_24) [page ] 40 | Trade Classification Specialist | Classify Products - Commodity Codes (F2151) | Commodity codes are assigned to products. |
| [Schedule Creation of Trade Classification Attributes Fuzzy Search](#unique_25) [page ] 41 | Administrator - International Trade | Schedule Creation of Trade Classification Attributes - Fuzzy Search (F8511) | Job is scheduled and shown in the list. |
| [Schedule Creation of Trade Classification Proposals Fuzzy Search](#unique_26) [page ] 42 | Administrator - International Trade | Schedule Creation of Trade Classification Proposals - Fuzzy Search (F8512) | Job is scheduled and shown in the list. |
| [Activate Classification Proposal Commodity Code](#unique_27) [page ] 43 | Trade Classification Specialist | Activate Classification Proposals - Commodity Codes (F8427) | The commodity code proposal is activated. |
| [Schedule Simulation of Trade Classification Proposals Fuzzy Search](#unique_28) [page ] 44 | Administrator - International Trade | Schedule Simulation of Trade Classification Proposals - Fuzzy Search (F8670) | Job is scheduled and shown in the list. |
| [Manage Customs Tariff Numbers](#unique_29) [page ] 45 | Trade Classification Specialist | Manage Customs Tariff Numbers (F3122) | Customs Tariff Number is created / changed. |
| [Manage Customs Tariff Numbers from Data Provider (Optional)](#unique_30) [page ] 46 |  |  |  |
| [Schedule Customs Tariff Numbers Content Request to Data Provider (Background Job)](#unique_31) [page ] 47 | Administrator - International Trade | Schedule Content Request to Data Provider - Customs Tariff Numbers (F3569) | Customs Tariff Numbers are created base on the data from Data Providers. |
| [Manage Customs Tariff Numbers Content from Data Provider](#unique_32) [page ] 48 | Trade Classification Specialist | Manage Content from Data Provider - Customs Tariff Numbers (F3581) | Customs Tariff Numbers are created base on the data from Data Providers. |
| Classify Products Customs Tariff Numbers |  |  |  |
| [Classify Products Customs Tariff Numbers](#unique_33) [page ] 49 | Trade Classification Specialist | Classify Products - Customs Tariff Numbers (F3146) | Customs Tariff Numbers are classified to products. |
| [Classify Products Customs Tariff Numbers using the International Trade Classification Agent (Optional)](#unique_12) [page ] 50 | Trade Classification Specialist | Classify Products - Customs Tariff Numbers (F3146) | Customs Tariff Numbers are classified to products by using the International Trade Classification Agent. |
| [Reclassify Products Customs Tariff Numbers (Optional)](#unique_34) [page ] 52 | Trade Classification Specialist | Reclassify Products - Customs Tariff Numbers (F3147) | Customs Tariff Numbers are changed for products. |
| [Classify Products Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional)](#unique_35) [page ] 54 |  |  |  |
| [Manage Customs Tariff Numbers](#unique_36) [page ] 54 | Trade Classification Specialist | Manage Customs Tariff Numbers (F3122) | Customs Tariff Numbers are created. |
| [Classify Products Customs Tariff Numbers](#unique_37) [page ] 55 | Trade Classification Specialist | Classify Products - Customs Tariff Numbers (F3146) | Customs Tariff Numbers are assigned to products. |
| [Schedule Creation of Trade Classification Attributes Fuzzy Search](#unique_38) [page ] 56 | Administrator - International Trade | Schedule Creation of Trade Classification Attributes - Fuzzy Search (F8511) | Job is scheduled and shown in the list. |
| [Schedule Creation of Trade Classification Proposals Fuzzy Search](#unique_39) [page ] 57 | Administrator - International Trade | Schedule Creation of Trade Classification Proposals - Fuzzy Search (F8512) | Job is scheduled and shown in the list. |
| [Activate Classification Proposal Customs Tariff Numbers](#unique_40) [page ] 58 | Trade Classification Specialist | Activate Classification Proposals - Customs Tariff Numbers (F8428) | The Customs Tariff Number proposal is activated. |
| [Schedule Simulation of Trade Classification Proposals Fuzzy Search](#unique_41) [page ] 59 | Administrator - International Trade | Schedule Simulation of Trade Classification Proposals - Fuzzy Search (F8670) | Job is scheduled and shown in the list. |
| Display Classification Decisions with Agent Assistance (Optional) |  |  |  |
| [Display Classified Products](#unique_42) [page ] 60 | Trade Classification Specialist | Display Classified Products - International Trade (F3789) | You displayed all the international trade classification data. |
| [Display Classification Decisions with Agent Assistance (Optional)](#unique_43) [page ] 61 | Trade Classification Specialist | Display Classified Products - International Trade (F3789) | You displayed all the international trade classification data with Agent assistance. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create new commodity code in this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Commodity Codes (F2516). | The Manage Commodity Codes overview screen displays. |  |
| 3 | Enter Numbering Scheme Content | In the overview screen, make the following entries and choose Go :No. Scheme Content: AE01 |  |  |
| 4 | Enter Commodity Codes Details | In the Manage Commodity Codes screen choose Add. Make the following entries:Commodity Code: for example, 72290000Official Description: <free text>Valid from: for example, 2018.01.01Valid to: for example, 9999.12.301st Customs Unit: <customs unit of measure>When the Unit of Measure System is assigned to the Numbering Scheme Content, the 1st Customs unit will be visible for maintenance.Please refer to the step Define Numbering Scheme Content (Optional) in the chapter [Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers from Data Provider (Optional)](#unique_8) [page ] 17.Please maintain the customs unit of measure if there is.Choose Save.Make a note of the Commodity code number. | Commodity code is saved. |  |

### Manage Commodity Codes from Data Provider (Optional)

If the commodity codes are generated by a data provider, perform the following steps.

|  |
| --- |
| Note Additional Manual ConfigurationTo manage commodity codes from a data provider, complete the additional and mandatory configuration steps as described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation, and include mandatory settings that are not delivered by SAP and must be created by you. For more information, refer to the Set-Up Instructions document for this scope item in SAP Signavio Process Navigator. |

|  |
| --- |
| Note Additional InformationTo manage commodity codes from a data provider, you must have a commercial contract with Data Provider. |

#### Schedule Commodity Codes Content Request to Data Provider (Background Job)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job which can schedule commodity codes content request to data provider automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Content Request to Data Provider - Commodity Codes (F3051). | The overview screen is displayed. |  |
| 3 | Schedule Commodity Codes Content Request to Data Provider by Background Job | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Content Request to Data Provider - Commodity CodesChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme Content: AE01_DPChoose Schedule. | Job is scheduled and shown in the list. |  |

#### Manage Commodity Codes Content from Data Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can activate the commodity codes from data provider and you can monitor the application logs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Trade Classification Specialist. |  |  |
| 2 | Access App | Open Manage Content from Data Provider - Commodity Codes (F3429). | The overview screen is displayed. |  |
| 3 | Active the Commodity Codes | In the overview screen, make the following entries and choose Go.No. Scheme Content: AE01_DPData Provider ID: _AChoose the No. Scheme Content and choose Activate.The confirmation message is displayed. Choose OK.Note The Data Provider ID should be unified with the communication arrangement in the Set-up Instruction. | The numbering scheme content of commodity codes is active. |  |
| 4 | View the Details of Commodity Codes from Data Provider (Optional) | Choose the No. Scheme Content and Click it. | The details of commodity codes are displayed. |  |
| 5 | View Application Log(Optional) | In the Manage Content from Data Provider - Commodity Codes.If the content consistency is marked failed, please click the content consistency and view the application log.Click the log and check the information description. For example, if the description is Missing UOM, please go to Configuration Step of Define Unit of Measure System to maintain Measure System.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |

### Classify Products Commodity Codes

#### Classify Products Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the commodity code you crated in [Manage Commodity Codes](#unique_15) [page ] 30.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Commodity Codes (F2151). | The Classify Products Commodity Codes screen is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Valid On: for example, 2018.01.01 (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: AE01Product: for example, TG11Note If the product has already been assigned commodity code, it won't display in this tile. To maintain, tile Reclassify Products Commodity Codes should be used. | Product entry displays. |  |
| 4 | Choose Product | Choose the product entry.In the Product column, double-click the product.Note Use the product dropdown menu if you would like to view more than one product.Choose Go. |  |  |
| 5 | Classify Product | Choose the checkbox of the products you want to classify and choose Classify.Make the following entries and choose Save:Commodity Code: <commodity code previously created>Classification From/To: for example, 2018.01.01 / 2018.12.31Remark: <your remark> | Classification is saved. |  |

#### Classify Products Commodity Codes using the International Trade Classification Agent (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the commodity code using the International Trade Classification Agent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Commodity Codes (F2151). | The Classify Products Commodity Codes screen is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Valid On: for example, 2026.03.01 (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: AE01Product: <the product ZSK_AI_01_FLASK, you've created in Master Data> | Product entry displays. |  |
| 4 | Enter Product | Select the checkbox of the product ZSK_AI_01_FLASK and choose Classify.Press the Generate Proposals button. | The Propose Commodity Code for Trade Classification screen is displayed. |  |
| 5 | Classify Product using the International Trade Classification Agent | On the Propose Commodity Code for Trade Classification screen, Step 1 Product information is displayed.In the Additional Information text field, you can maintain additional product information, for example:MATERIAL & CONSTRUCTION:Outer Material: Stainless Steel 304/18-8Inner Material: Stainless Steel Food GradeLid Type: Leak-proof Screw Cap / PushButton Lid:Seal: BPA-free Silicone GasketDesign: Ergonomic Non-slip GripFEATURES:Lightweight & DurableCorrosion ResistantEasy to CleanDishwasher Safe (Lid Only)Eco-friendlyAvailable Colors: Black, Silver, Blue, RedPDF documents, such as product data sheets, can be uploaded to the Attachments field in this step.Press Step 2 to proceed.The message International Trade Classification Agent is generating the product profile is displayed.Step 2: Product Profile is displayed.You can review the product attributes in this step. The product profile is generated by the agent and presents the AI assistant's understanding of the product in terms of its characteristics and intended use.The product profile also includes a pre-analysis of the product according to the General Rules for the interpretation of the Harmonized System (World Customs Organization).Press Step 3 to proceed.Message International Trade Classification Agent is generating proposals is displayed.Step 3: Generated Proposal is displayedBased on the product profile, the agent generates classification proposals. You can open the summary, detailed reasoning, and note analysis sections for each proposed commodity code.After checking the information provided, you can now select the proposal that best suits your requirements by pressing the Select Proposal button and confirming your decision by pressing the Submit button.The proposed commodity code is entered in this field.Click Save to confirm your entry.Note The commodity code should be maintained by APP Manage Commodity Codes before you classify the product. | The classification proposal is generated and the classification of commodity code is saved. |  |

### Reclassify Products Commodity Codes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reclassify the products which were classified with commodity codes before with new commodity codes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Reclassify Products - Commodity Codes (F2152). | The Reclassify Products - Commodity Codes screen is displayed. |  |
| 3 | Enter Filters | Make the following entries:Valid On: for example, 2018.01.01 (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: AE01Product (Optional): for example, TG11 | Product entry displays. |  |
| 4 | Choose Product | Choose the product entry.In the Product column, double-click the product.Note Use the product dropdown menu if you would like to view more than one product.Choose Go. |  |  |
| 5 | Reclassify Product | Choose the checkbox of the products you want to reclassify and choose Reclassify.Make the following entries and choose Save:Commodity Code: <another commodity code>Classification From/To: for example, 2018.01.01 / 2018.12.31Remark: <your remark> | Reclassification is saved. |  |

### Classify Products Commodity Codes with AI-Assisted Generation of Trade Classification Proposals (Optional)

Purpose

In this activity, you will utilize AI-Assisted Generation of Trade Classification Proposals to classify products with commodity codes.

Trade classification proposals can be generated by the SAP HANA Fuzzy Search algorithm that searches for similar products based on the comparison of the product descriptions.

For an unclassified product, a trade classification number proposal is generated with a certain level of accuracy, based on similar products that have already been classified.

#### Create Products

Purpose

In this activity, you create products with specific material descriptions.

Procedure

Please refer to [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2502-master-data/start?locale=en-US) documentation BNF - Create Product Master of type "Trading Good" - MDS to create following two Material (Product) Master Data - Basic Data with following material numbers and descriptions.

Material1: ZTR001

Description: AC motors, multi-phase, output 800W

Material1: ZTR002

Description: Dry zinc-carbon batteries of a voltage of 5.5 V

Material1: ZTR003

Description: AC motors EA, multi-phase, output 800W

Material1: ZTR004

Description: Dry zinc-carbon batteries of a voltage of 6V

#### Manage Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, you can display all the international trade classification data including commodity code, control class, customs tariff number, and Intrastat services codes for the products you classified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Commodity Codes (F2516). | The Manage Commodity Codes overview screen displays. |  |
| 3 | Enter Numbering Scheme Content | In the overview screen, make the following entries and choose Go:No. Scheme Content: AE01 |  |  |
| 4 | Enter Commodity Codes Details | In the Manage Commodity Codes screen choose Add. Make the following entries:Commodity Code: 85015220Official Description: <AC motors, multi-phase, of an output > 750 W but <= 7,5 kW>Valid from: <for example, 2025.01.01>Valid to: <for example, 9999.12.30>Choose add.Continue to create the following commodity code:Commodity Code: 85068005Official Description: <Dry zinc-carbon batteries of a voltage of 5,5 V or more but not exceeding 6,5 V>Valid from: <for example, 2025.01.01>Valid to: <for example, 9999.12.30>Choose Save.Make a note of the commodity code number. | Commodity codes are saved. |  |

#### Classify Products Commodity Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can classify the product commodity code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Commodity Codes (F2151). | The Classify Products Commodity Codes screen is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Valid On: <for example, 2025.04.01> (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: AE01Product: ZTR001 | Product entry displays. |  |
| 4 | Classify Product | Choose the checkbox of the product ZTR001 and choose Classify.Make the following entries and choose Save:Commodity Code: 85015220Classification From/To: <for example, 2025.05.01 / 9999.12.31>Continue to classify product ZTR002 with Commodity Code 85068005. | Classification is saved. |  |

#### Schedule Creation of Trade Classification Attributes Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule the creation of trade classification attributes via AI-Assisted generation of trade classification proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Creation of Trade Classification Attributes - Fuzzy Search (F8511). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Attributes | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Creation of Trade Classification AttributesChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE01Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Schedule Creation of Trade Classification Proposals Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule the creation of trade classification attributes via AI-Assisted generation of trade classification proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Creation of Trade Classification Proposals - Fuzzy Search (F8512). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Proposals | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Creation of Trade Classification Proposals – Fuzzy SearchChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE01Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Activate Classification Proposal Commodity Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display the product classification proposals for commodity codes including an accuracy score for products that have not been classified. By activating trade classification proposals, the product will be classified.

|  |
| --- |
| Note Only proposals with the highest accuracy score will be displayed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Activate Classification Proposals - Commodity Codes (F8427). | The Application Jobs screen is displayed. |  |
| 3 | Activate Classification Proposals – Commodity Codes | In the Activate Classification Proposal – Commodity Codes screen, make the following entries:Numbering Scheme: AE01Product: Click the search button and search product ZTR003 and ZTR004Select Product ZTR003 and ZTR004.Choose Go.The proposed commodity code for products are displayed.Select the product ZTR003 and ZTR004.Check the Accuracy.Choose Activate Proposal.In the Activate Proposal screen, make the following entry:Valid from: <for example, 2025.04.01>Valid to: <for example, 9999.12.30>Choose Activate Proposal. | The commodity code proposal is activated. |  |

#### Schedule Simulation of Trade Classification Proposals Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule simulation of trade classification proposals.

This simulation app evaluates how the fuzzy classification algorithm would behave by using already classified products as a reference. It simulates the fuzzy logic process to determine whether the algorithm would propose the same or different trade classification numbers based on current product data.

By utilizing the app, you can fine-tune the fuzzy parameters maintained in the configuration activity: Define Numbering Scheme of Commodity Codes, enhancing the accuracy of your classifications proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Simulation of Trade Classification Proposals - Fuzzy Search (F8670). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Proposals | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Fuzzy Proposal SimulationChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE01Accuracy Threshold (%): 40%Choose Schedule. | Job is scheduled and shown in the list. |  |

### Manage Customs Tariff Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create new customs tariff number in this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access App | Open Manage Customs Tariff Numbers (F3122). | The Manage Customs Tariff Numbers screen is displayed. |  |
| 3 | Manage Customs Tariff Numbers | Make the following entries and choose Go:No. Scheme Content: AE04 | Customs Tariff Numbers related to AE04 is displayed. |  |
| 4 | Create Customs Tariff Numbers | Choose Add. Make the following entries and choose Save:Customs Tariff Numbers: for example, 72290000000Official Description: <free text>Valid from: for example, 2018.01.01Valid to: for example, 9999.12.301st Customs Unit: for example, KGMWhen the Unit of Measure System is assigned to the Numbering Scheme Content, the 1st Customs unit will be visible for maintenance.Please refer to the step Define Numbering Scheme Content (Optional) in the chapter [Prerequisite Steps for Manage Commodity Codes and Customs Tariff Numbers from Data Provider (Optional)](#unique_8) [page ] 17.Make a note of the Customs Tariff Number. | Customs Tariff Number is saved. |  |

### Manage Customs Tariff Numbers from Data Provider (Optional)

If the Customs Tariff Numbers are generated by external Data Provider, below steps should be performed.

|  |
| --- |
| Note Additional Manual Configuration:To manage Customs Tariff Numbers from Data Provider, you need to have completed the additional and mandatory configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation. It includes mandatory settings that are not delivered by SAP and must be created by you. For more information, refer to the document in SAP Signavio Process Navigator. |

|  |
| --- |
| Note Additional Manual Configuration:To manage Customs Tariff Numbers from Data Provider, you need to sign a commercial contract with Data Provider. |

#### Schedule Customs Tariff Numbers Content Request to Data Provider (Background Job)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job which can schedule customs tariff numbers content request to data provider automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Administrator - International Trade. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Content Request to Data Provider - Customs Tariff Numbers (F3569). | The overview screen is displayed. |  |
| 3 | Schedule Customs Tariff Numbers Content Request to Data Provider by Background Job | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Content Request to Data Provider - Customs Tariff NumbersChoose Step 2.Start Immediately: XChoose Step 3.No. Scheme Content: AE04_DPChoose Schedule. | Job is scheduled and shown in the list. |  |

#### Manage Customs Tariff Numbers Content from Data Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can activate the customs tariff numbers and you can monitor the application logs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Content from Data Provider - Customs Tariff Numbers (F3581). | The overview screen is displayed. |  |
| 3 | Activate the Customs Tariff Numbers | In the overview screen, make the following entries and choose Go.No. Scheme Content: AE04_DPData Provider: _A BundesanzeigerChoose the No. Scheme Content and click Activate.The confirmation message is popped up. Click OK.Note The Data Provider ID should be unified with the communication arrangement in the Set-Up Instruction. | The numbering scheme content of customs tariff numbers is activated. |  |
| 4 | View the details of Customs Tariff Numbers from Data Provider (Optional) | Choose the No. Scheme Content and Click it. | The details of customs tariff numbers are displayed. |  |
| 5 | View Application log(Optional) | In the Manage Content from Data Provider – Customs Tariff view, if the content consistency is marked failed, please click the content consistency and view the application log.Choose the log and check the information description. For example, if the description is Missing UOM, please go to SSCUI of Define Unit of Measure System to maintain the Measure System.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |

### Classify Products Customs Tariff Numbers

#### Classify Products Customs Tariff Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the customs tariff numbers you created in last step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launch pad as a Trade Classification Specialist. | The SAP Fiori launch pad displays. |  |
| 2 | Access SAP Fiori App | Open Classify Products - Customs Tariff Numbers (F3146). | The Classify Product Customs Tariff Numbers screen displays. |  |
| 3 | Classify Products Customs Tariff Numbers | In the filter bar make the following entries:Valid On: for example, 2018.01.01 (This date should be in the valid period of the customs tariff number you want to use.)Numbering Scheme: AE04Product (Optional): for example, TG10Choose Go. | Product entry displays.If the product has already been assigned customs tariff number, it won't display in this tile. To maintain this one, tile Reclassify Products Customs Tariff Numbers should be used. |  |
| 4 | Classify Product | In the Products area, chosoe the product entry and choose Classify. Make the following entries:Customs Tariff Numbers: <created in last step>Classification Period: for example, 2018.01.01 / 2018.12.31Remark: <your remark>Choose Save. | Classification is saved, and product is removed from the list. |  |

#### Classify Products Customs Tariff Numbers using the International Trade Classification Agent (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you classify the products with the customs tariff numbers you created in last step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Customs Tariff Numbers (F3146). | The Classify Product Customs Tariff Numbers screen is displayed. |  |
| 3 | Classify Products Customs Tariff Numbers | Make the following entries and choose Go:Valid On: for example, 2026.03.01 (This date should be in the valid period of the Commodity code you want to use.)Numbering Scheme: AE04Product (optional): <the product ZSK_AI_01_FLASK, you've created in Master Data> | Product entries are displayed. If a product has already been assigned a customs tariff number, it will not appear in this tile. To maintain such product, please use the Reclassify Products Customs Tariff Numbers tile. |  |
| 4 | Enter Product | Select the checkbox of the product ZSK_AI_01_FLASK and choose Classify.Press the Generate Proposals button. | The Propose Customs Tariff Numbers for Trade Classification screen is displayed. |  |
| 5 | Classify Product using the International Trade Classification Agent | On the Propose Customs Tariff Number for Trade Classification screen, Step 1 Product information is displayed.In the Additional Information text field, you can maintain additional product information, for example:MATERIAL & CONSTRUCTION:Outer Material: Stainless Steel 304/18-8Inner Material: Stainless Steel Food GradeGrade:Lid Type: Leak-proof Screw Cap / PushButton Lid:Seal: BPA-free Silicone GasketDesign: Ergonomic Non-slip GripFEATURES:Lightweight & DurableCorrosion ResistantEasy to CleanDishwasher Safe (Lid Only)Eco-friendlyAvailable Colors: Black, Silver, Blue, RedPDF documents, such as product data sheets, can be uploaded to the Attachments field in this step.Press Step 2 to proceed.The message International Trade Classification Agent is generating the product profile is displayed.Step 2: Product Profile is displayed.You can review the product attributes in this step. The product profile is generated by the agent and presents the AI assistant's understanding of the product in terms of its characteristics and intended use.The product profile also includes a pre-analysis of the product according to the General Rules for the interpretation of the Harmonized System (World Customs Organization).Press Step 3 to proceed.Message International Trade Classification Agent is generating proposals is displayed.Step 3: Generated Proposal is displayedBased on the product profile, the agent generates classification proposals. You can open the summary, detailed reasoning, and note analysis sections for each proposed customs tariff number.After checking the information provided, you can now select the proposal that best suits your requirements by pressing the Select Proposal button and confirming your decision by pressing the Submit button.The proposed customs tariff number is entered in this field.Click Save to confirm your entry.Note The customs tariff number should be maintained by APP Manage Customs Tariff Number before you classify the product. | The classification proposal is generated and the classification of customs tariff number is saved. |  |

### Reclassify Products Customs Tariff Numbers (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can reclassify the products which were classified with customs tariff numbers before with new customs tariff numbers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reclassify Products - Customs Tariff Numbers (F3147). | The Reclassify Products Customs Tariff Numbers screen is displayed. |  |
| 3 | Enter Filters | In the filter bar make the following entries:Valid On: for example, 2018.01.01 (This date should be in the valid period of the customs tariff numbers you want to use.)Numbering Scheme: AE04Product (Optional): for example, TG10Choose Go. | The Classify Products - Customs Tariff Numbers view displays to allow Reclassification. |  |
| 4 | Reclassify Product | Choose the product entry and choose Reclassify.Make the following entries:Customs Tariff Numbers: <other customs tariff numbers>Classification From/To: for example, 2018.01.01 / 2018.12.31Remark: <your remark>Choose Save. | Reclassification is saved. |  |

### Classify Products Customs Tariff Numbers with AI-Assisted Generation of Trade Classification Proposals (Optional)

Purpose

In this activity, you can use AI-assisted generation of Trade Classification Proposals to classify products with customs tariff numbers.

Trade classification proposals can be generated using the SAP HANA Fuzzy Search algorithm, which identifies similar products by comparing product descriptions.

For any unclassified product, a trade classification number proposal is generated with a certain level of accuracy, based on similar products that have already been classified.

#### Manage Customs Tariff Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create customs tariff numbers with similar descriptions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customs Tariff Numbers (F3122) | The Manage Customs Tariff Numbers overview screen displays. |  |
| 3 | Enter Numbering Scheme Content | In the Manage Customs Tariff Numbers overview screen, make the following entries and choose Go:No. Scheme Content: AE04 |  |  |
| 4 | Enter Customs Tariff Numbers Details | In the Manage Customs Tariff Numbers screen choose Add. Make the following entries:Customs Tariff Numbers: 8501522010Official Description: <Electric motors and generators, of an output exceeding 750 W but not exceeding 7,5 kW, for use in civil aircraft>Valid from: <for example, 2025.01.01>Valid to: <for example, 9999.12.30>Choose add.Continue to create the following Customs Tariff Number:Customs Tariff Numbers: 8506800500Official Description: <Dry zinc-carbon batteries of a voltage of 5,5 V or more but not exceeding 6,5 V>Valid from: <for example, 2025.01.01>Valid to: <for example, 9999.12.30>Choose Save.Make a note of the Customs Tariff Numbers. |  |  |

#### Classify Products Customs Tariff Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can classify the product customs tariff numbers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Classify Products - Customs Tariff Numbers (F3146). | The Classify Product Customs Tariff Numbers screen is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Valid On: for example, 2025.04.01 (This date should be in the valid period of the Commodity code you want to use)Numbering Scheme: AE04Product: ZTR001 | Product entry displays. |  |
| 4 | Classify Product | Choose the checkbox of the product ZTR001 and choose Classify.Make the following entries and choose Save:Customs Tariff Numbers: 8501522010Classification From/To: <for example, 2025.05.01 / 9999.12.31>Continue to classify product ZTR002 with Customs Tariff Number 8506800500. | Classification is saved. |  |

#### Schedule Creation of Trade Classification Attributes Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule the creation of trade classification attributes via AI-Assisted generation of trade classification proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Creation of Trade Classification Attributes - Fuzzy Search (F8511). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Attributes | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Creation of Trade Classification AttributesChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE04Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Schedule Creation of Trade Classification Proposals Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule the creation of trade classification proposals via AI-Assisted generation of trade classification proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Creation of Trade Classification Proposals - Fuzzy Search (F8512). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Proposals | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Creation of Trade Classification Proposals – Fuzzy SearchChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE04Choose Schedule. | Job is scheduled and shown in the list. |  |

#### Activate Classification Proposal Customs Tariff Numbers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display product classification proposals for customs tariff numbers, along with an accuracy score for products that have yet to be classified. By activating these trade classification proposals, the product will be assigned a classification.

|  |
| --- |
| Note Only proposals with the highest accuracy score will be displayed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Activate Classification Proposals - Customs Tariff Numbers (F8428). | The Application Jobs screen is displayed. |  |
| 3 | Activate Classification Proposals – Commodity Codes | In the Activate Classification Proposal – Customs Tariff Numbers screen, make the following entries:Numbering Scheme: AE04Product: Click the search button and search for product ZTR003 and ZTR004Select Product ZTR003 and ZTR004.Choose Go.The proposed customs tariff number for products are displayed.Select the product ZTR003 and ZTR004.Check the Accuracy.Choose Activate Proposal.In the Activate Proposal Screen, make the following entry:Valid from: <for example, 2025.04.01>Valid to: <for example, 9999.12.30>Choose Activate Proposal. | The customs tariff number proposal is activated. |  |

#### Schedule Simulation of Trade Classification Proposals Fuzzy Search

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can schedule simulation of trade classification proposals.

This simulation app evaluates how the fuzzy classification algorithm would behave by using already classified products as a reference. It simulates the fuzzy logic process to determine whether the algorithm would propose the same or different trade classification numbers based on current product data.

By utilizing the app, you can fine-tune the fuzzy parameters maintained in the configuration activity: Define Numbering Scheme of Customs Tariff Numbers, enhancing the accuracy of your classifications proposals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Administrator - International Trade. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Simulation of Trade Classification Proposals - Fuzzy Search (F8670). | The Application Jobs screen is displayed. |  |
| 3 | Schedule the Creation of Trade Classification Proposals | In the overview screen, choose Create.In the New Job screen, make the following entries:Job Template: Schedule Fuzzy Proposal SimulationChoose Step 2.Start Immediately: XChoose Step 3.Numbering Scheme: AE04Accuracy Threshold (%): 40%Choose Schedule. | Job is scheduled and shown in the list. |  |

### Display Classification Decisions with Agent Assistance (Optional)

#### Display Classified Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, you can display all the international trade classification data including commodity code, control class, customs tariff number, and Intrastat services codes for the products you classified.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Display Classified Products - International Trade (F3789). | The Display Classified Products view is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Plant: <plant> for example, 3310 | The Display Classified Products screen is displayed. All previously classified products are displayed. |  |
| 4 | Display the List for Classified Products | Choose a product. | The Display Classified Products - International Trade view displays.Different tabs for the classification data are displayed, including Commodity Codes, Customs Tariff Numbers, Legal Control and Intrastat Service Codes. |  |
| 5 | Display Classification Data for Product | Choose the numbering scheme you maintained for the product (for example, AE01). | The Classification for Commodity Code view is displayed. |  |
| 6 | Display the Classification History for Commodity Code | In the Commodity Codes view, you can find the classification history of commodity codes for the product with validation period.In the Change Documents tab, you can see the details of changed data including old and new values, created by, created on, and change types for the fields belonging to classification.You can follow the same steps to display other classification data like Customs Tariff Number for the product. |  |  |

#### Display Classification Decisions with Agent Assistance (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the activity, you can display the classification decisions made with agent assistance for commodity codes and customs tariff numbers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Trade Classification Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Display Classified Products - International Trade (F3789). | The Display Classified Products view is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Product: <for example, ZSK_AI_01_FLASK> | The Display Classified Products screen is displayed. All previously classified products are displayed. |  |
| 4 | Display the List for Classified Products | Choose the details for product. | The Classification Overview view displays.Different tabs for the classification data are displayed, including Commodity Codes, Customs Tariff Numbers, Legal Control and Intrastat Service Codes. |  |
| 5 | Display Classification Data for Product | Choose the numbering scheme you maintained for the product (for example, AE01). | The Classification for Commodity Code view is displayed. |  |
| 6 | Display the Classification Decisions | Choose Display Trade Classification.The detailed information including product information, product profile, generated proposals of the International Trade classification agent and your submitted decision are displayed. | The classification decisions are displayed. |  |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-sap-s-4hana-cloud-public-edition-legal-control-1w8-ae-767]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2U3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 101,578 chars in the whole document
