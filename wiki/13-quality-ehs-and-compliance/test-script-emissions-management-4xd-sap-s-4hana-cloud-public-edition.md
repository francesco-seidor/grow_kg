---
id: 13-quality-ehs-and-compliance/test-script-emissions-management-4xd-sap-s-4hana-cloud-public-edition
title: "Test Script: Emissions Management (4XD) - SAP S/4HANA Cloud Public Edition (4XD_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for Emissions Management (4XD): GHG compliance requirement, scenarios, data entry, deviation, annual report."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/environmental-compliance-and-emissions]
aliases: [4XD_S4CLD2608_BPD_EN_XX]
keywords: [Environmental Compliance and Emissions Management, emissions management, test scripts, compliance requirements, environmental limits, ghg equations, compliance scenarios, scenario activities, environmental data recording, environmental data monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4XD_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1058
topic: 13-quality-ehs-and-compliance/environmental-compliance-and-emissions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Emissions Management (4XD) - SAP S/4HANA Cloud Public Edition (4XD_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4XD_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Environmental Compliance and Emissions Management** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Emissions Management (4XD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232831357)

[2 Prerequisites 3](#_Toc232831358)

[2.1 System Access 3](#_Toc232831359)

[2.2 Roles 3](#_Toc232831360)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232831361)

[2.4 Business Conditions 4](#_Toc232831362)

[3 Overview Table 6](#_Toc232831363)

[4 Test Procedures 8](#_Toc232831364)

[4.1 Create Compliance Requirement 8](#_Toc232831365)

[4.2 Create Compliance Scenario for Power Unit B1 16](#_Toc232831366)

[4.3 Set Up Compliance Scenario Activities for Power Unit B1 18](#_Toc232831367)

[4.4 Copy Compliance Scenario to Power Unit B2 27](#_Toc232831368)

[4.5 Create Compliance Scenario for Power Plant Boston 30](#_Toc232831369)

[4.6 Set Up Compliance Scenario Activities for Power Plant Boston 31](#_Toc232831370)

[4.7 Activate Compliance Scenarios for Power Plant Boston and Its Sublocations 34](#_Toc232831371)

[4.8 Record Environmental Data for Power Unit B1 35](#_Toc232831372)

[4.9 Record Environmental Data for Power Unit B2 37](#_Toc232831373)

[4.10 Monitor Environmental Data for Power Plant Boston 39](#_Toc232831374)

[4.11 Create a Deviation for Power Plant Boston 40](#_Toc232831375)

[4.12 Create Annual GHG Report for Power Plant Boston 42](#_Toc232831376)

## Purpose

Overview

This scope item helps you to manage compliance with emissions-related environmental regulations. The processes enable you to create and incorporate a strategy to manage environmental data from data collections, samplings, calculations, and aggregations of emissions into the daily operations of your company.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Business Role or Template) | ID | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Environmental Manager | SAP_BR_EHS_ENV_MGMT | Environment Management | SAP_BR_EHS_ENV_MGMT |  |
| Production Operator - EHS Info (displayed as Environmental Technician in some of the apps) | SAP_BR_PRODN_OPTR_EHS_INFO | Environment Management | SAP_BR_EHS_ENV_MGMT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Master Data Script Reference

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Future Energy | Location of a Company type. Parent location for all other sample locations. | You can find more information on how to create this location in the [Business Conditions](#unique_6) [page ] 4 section. |
| Location | Power Plant Boston | Location of a Plant type. Sublocation of Future Energy. |  |
| Location | Power Unit B1 | Location of a Production Unit type. Sublocation of Power Plant Boston. |  |
| Location | Power Unit B2 | Location of a Production Unit type. Sublocation of Power Plant Boston. |  |
| Location | Administrative Building A1 | Location of a Production Unit type. Sublocation of Power Plant Boston. | This location can be used for the calculation of indirect emissions. |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3SR | Create EHS Location - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3SR - Create EHS Location - MDS | Using the instructions in this scope item, create the following EHS locations. Set yourself as a person responsible for them assigning to your user the roles of Environmental Manager and Production Operator - EHS Info (displayed as Environmental Technician in some of the apps). Set the first day of calendar year as a start date for each location revision.Future EnergyPower Plant BostonPower Unit B1Power Unit B2Make sure that all locations are set to Active to enable their use in the test procedures. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Compliance Requirement](#unique_8) [page ] 8 | Environmental Manager | Manage Compliance Requirements - Regulations, Permits, Policies (F5038) | A compliance requirement of a Policy type has been created with an environmental limit, regulatory lists, and equations in it.The compliance requirement has been released and can be used to set company goals for compliance of greenhouse gas emissions with applicable environmental limits. |
| [Create Compliance Scenario for Power Unit B1](#unique_9) [page ] 16 | Environmental Manager | Create Compliance Scenario | A compliance scenario has been created for one of the company's production units and can be used to set that unit as applicable for compliance requirements about greenhouse emissions reporting. |
| [Set Up Compliance Scenario Activities for Power Unit B1](#unique_10) [page ] 18 | Environmental Manager | Edit Compliance Scenario | Compliance activities have been added to the scenario to help ensure the compliance of the company's production unit with the applicable requirements about greenhouse emissions. |
| [Copy Compliance Scenario to Power Unit B2](#unique_11) [page ] 27 | Environmental Manager | Manage Compliance Scenario (WDA0468) | Compliance scenario for Power Unit B1 has been copied to scale up with the setup for compliance management for the additional production unit of the company - Power Unit B2 - where the same compliance requirement applies. |
| [Create Compliance Scenario for Power Plant Boston](#unique_12) [page ] 30 | Environmental Manager | Create Compliance Scenario | A compliance scenario has been created for Power Plant Boston to set up the applicability of the whole company to the compliance requirement about greenhouse emissions. |
| [Set Up Compliance Scenario Activities for Power Plant Boston](#unique_13) [page ] 31 | Environmental Manager | Edit Compliance Scenario | Compliance scenario activities, such as calculations and aggregations, have been set up for Power Plant Boston. These activities can be used to check emissions data from all power plants in the company and verify that the set company targets can be met. |
| [Activate Compliance Scenarios for Power Plant Boston and Its Sublocations](#unique_14) [page ] 34 | Environmental Manager | Manage Compliance Scenario (WDA0468) | The compliance scenarios for Power Plant Boston and its sublocations have been activated in one go. The planned compliance activities in them can start and be monitored on a plant level. |
| [Record Environmental Data for Power Unit B1](#unique_15) [page ] 35 | Environmental Manager | Finalize SamplingMy Data Collections (F3991) | Emissions data for Power Unit B1 has been entered in the system to reflect monthly data collections and samplings, part of the company's operations. |
| [Record Environmental Data for Power Unit B2](#unique_16) [page ] 37 | Environmental ManagerProduction Operator - EHS Info | Finalize SamplingMonitor Data - Environment Management (WDA0149) | Emissions data for Power Unit B2 has been entered in the system to reflect monthly data collections and samplings, part of the company's operations. |
| [Monitor Environmental Data for Power Plant Boston](#unique_17) [page ] 39 | Environmental Manager | Monitor Data - Environment Management (WDA0149) | Emissions data for Power Plant Boston has been monitored and checked against company goals about compliance with applicable environmental limits. |
| [Create a Deviation for Power Plant Boston](#unique_18) [page ] 40 | Environmental Manager | Monitor Data - Environment Management (WDA0149) (Create Deviation Incident option) | Based on the monitoring and analysis of incoming monthly emissions data for Power Plant Boston, a deviation incident has been created for the data where company goals are not met. |
| [Create Annual GHG Report for Power Plant Boston](#unique_19) [page ] 42 | Environmental Manager | Manage Environmental Reports​ (F5638) | An internal annual report for GHG emissions in Power Plant Boston has been created to get a summary of the available greenhouse gas data in the system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Compliance Requirement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new compliance requirement of a Policy type. The Environmental Manager adds regulatory lists, environmental limits, and equations to the requirement paragraph. The Environmental Manager releases the compliance requirement for use in further processes for managing emissions-related data. The requirement is needed to help set company goals for compliance of greenhouse gas emissions with environmental limits.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Requirements - Regulations, Permits, Policies (F5038). | The Manage Compliance Requirements screen is displayed. |  |
| 3 | Navigate to Create Policy | On the entry screen of the Manage Compliance Requirements - Regulations, Permits, Policies (F5038) app, choose Create Policy. | The Create New Policy screen is displayed. |  |
| 4 | Enter Policy Details | Under the Basic Information tab, enter the following information:Compliance Requirement Name: Yearly Greenhouse Gas GoalsIssuing Organization: Future Energy CompanyValid From: <First day of calendar year>Valid To: <Last day of calendar year two years after current year>Domain: AirDescription: This policy includes the yearly CO2e target for emissions management at the Power Plant Boston company. The policy holds the regulatory lists and environmental limits, applicable to the direct and indirect emissions produced by the company, together with some equations to help calculate these emissions. | The policy details are populated under the Basic Information tab. |  |
| 5 | Add Validity Area | Under the Validity Area tab, choose Add to enter a country/region that this policy is valid for or select it from the predefined list (for example, USA).Note Choose Go to check the predefined list.If needed, repeat the same steps to add more countries/regions of validity. | The selected countries/regions are populated under the Validity Area tab. |  |
| 6 | Save Policy | Choose Save at the bottom right side of the screen to save the policy and its details. | The policy is saved.You are navigated to the Policy: Yearly Greenhouse Gas Goals screen. |  |
| 7 | Edit Paragraph | Navigate to the Contents tab. Select the link to the compliance requirement paragraph Yearly Greenhouse Gas Goals for further editing. | You are navigated to the Paragraph: Yearly Greenhouse Gas Goals screen. |  |
| 8 | Add Yearly CO2e Target Environmental Limit to the Paragraph | Go to the Environmental Limits tab.Choose Add (+ icon) to add an environmental limit to the paragraph. | A new row is added. New fields for limit details are displayed on the right side of the screen. |  |
| 9 | Enter Environmental Limit Details | On the right side of the screen, in the new fields for limit details, enter the following information:Limit Name: Yearly CO2e TargetType: Upper LimitSubject: Carbon Dioxide EquivalentUnit: tUpper Limit Value: 55000000Upper Warning Value: 50000000Description: This is the company's yearly target for direct GHG emissions per power plant.Follow-up in case of exceedance: Notify the power plant management.Choose Save at the bottom right side of the screen. | The environmental limit details are saved. The limit is added to the paragraph. |  |
| 10 | Add Monthly CO2 Target Environmental Limit to the Paragraph | Repeat step 8 to add a new environmental limit to the paragraph.In the fields for the limit details, enter the following information:Limit Name: Monthly CO2 TargetType: Upper LimitSubject: Carbon Dioxide EquivalentUnit: tUpper Limit Value: 5500000Upper Warning Value: 5000000Description: This is the company's monthly target for direct GHG emissions per power unit.Follow-up in case of exceedance: Notify the power unit management.Choose Save at the bottom right side of the screen. | The environmental limit details are saved. The limit is added to the paragraph. |  |
| 11 | Add Global Warming Potential as a Regulatory List to the Paragraph | Go to the Regulatory Lists tab.Choose Add (+ icon) to add a regulatory list to the paragraph.Select Global Warming Potential from the dropdown list. | A new row is added. New fields for regulatory list details are displayed on the right side of the screen. |  |
| 12 | Enter Global Warming Potential Regulatory List Details | On the right side of the screen, in the new fields for regulatory list details, enter the following information:Name: Company Global Warming Potential |  |  |
| 13 | Add Pollutants | Add the following pollutant to the regulatory list:nitrous oxideOpen the Pollutant field value help, then enter the pollutant name in the Name field of the Select Listed Substance dialog box that opens, then choose Go. In the results list, make sure to select the listed substance entry where the Conditions for Listed Substance are set to Not Specified.Note Alternatively, instead of searching by name within the value help, enter the following Listed Substance ID information to find the pollutant: L00000035081.Once you make your selection, choose OK to close the value help.Then, enter the following information about the pollutant:Value: 265Additional Information: company-reduced coefficientRepeat the same steps to add the following two pollutants to the regulatory list:MethaneLlisted substance ID: L00000002649Carbon dioxideListed substance ID: L00000007115Then, enter the following values for each entry in the Value field:methane: 25Carbon dioxide: 1Choose Save at the bottom right side of the screen. | The pollutants are saved to the regulatory list. The regulatory list is added to the paragraph. |  |
| 14 | Add Emission Factor as a Regulatory List to the Paragraph | Choose Add (+ icon) to add another regulatory list to the paragraph.Select Emission Factor from the dropdown list. | A new row is added. New fields for regulatory list details are displayed on the right side of the screen. |  |
| 15 | Enter Emission Factor Regulatory List Details | On the right side of the screen, in the new fields for regulatory list details, enter the following information:Name: Company-Specific Emission Factors Based on Federal Regulations |  |  |
| 16 | Add Listed Substances | Choose Add to add two entries for the following listed substance to the regulatory list:Coal (entered as the source subject)Make sure you do this twice to make two listed substance entries for Coal. | The listed substances are added to the regulatory list. |  |
| 17 | Edit Listed Substance Details | Add the following pollutant to the first Coal listed substance entry:nitrous oxideTo do this, open the Pollutant field value help and in the new Select Listed Substance dialog box, in the Name field, enter the pollutant name (nitrous oxide) and choose Go. In the results list, select a listed substance entry whose Conditions for Listed Substances are set to Not Specified.Note Alternatively, instead of searching by pollutant name within the value help, enter the following value into the Listed Substance ID field to find the pollutant: L00000035081.Once you make your selection, choose OK to close the value help.Now, repeat the same steps to add the following pollutant to the second Coal listed substance entry from step 16:methane (listed substance ID: L00000002649) | The pollutants are added to the listed substance. |  |
| 18 | Enter Listed Substance Values | Enter the following values for the Coal listed substance with pollutant nitrous oxide:Value: 0.0016Unit: kg/MMBtuEnter the following values for the Coal listed substance with pollutant methane:Value: 0.011Unit: kg/MMBtuChoose Save at the bottom right side of the screen.Note The solution comes with delivered content for greenhouse gas reporting according to US regulation in the following compliance requirement - Title 40: Protection of Environment; PART 98—MANDATORY GREENHOUSE GAS REPORTING. You can navigate to paragraph Subpart C - General Stationary Fuel Combustion Sources and use regulatory lists Table C-2 to Subpart C of Part 98—Default CH4 Emission Factors and Table C-2 to Subpart C of Part 98—Default N2O Emission Factors, part of it, to get the default values of the listed substances according to that regulation. | The values of the listed substances are saved. The regulatory list is added to the paragraph. |  |
| 19 | Add High Heating Value as a Regulatory List to the Paragraph | Choose Add (+ icon) to add another regulatory list to the paragraph.Select High Heating Value from the dropdown list. | A new row is added. New fields for regulatory list details are displayed on the right side of the screen. |  |
| 20 | Enter High Heating Value Regulatory List Details | On the right side of the screen, in the new fields for regulatory list details, enter the following information:Name: Company-Specific High Heating Values Based on Federal Regulations |  |  |
| 21 | Add Listed Substance | Add the following listed substance to the regulatory list:CoalUse the already provided listed substance ID information from the previous steps to find and select the right entry. Once you make the selection, choose OK. | The listed substance is added to the regulatory list. |  |
| 22 | Enter Listed Substance Value | Enter the following value for the Coal listed substance:Value: 24.8Unit: MMBtu/tonChoose Save at the bottom right side of the screen.Note This value is a default value and can be found in compliance requirement Title 40: Protection of Environment; PART 98—MANDATORY GREENHOUSE GAS REPORTING, paragraph Subpart C - General Stationary Fuel Combustion Sources, regulatory list Table C-1 to Subpart C of Part 98—Default High Heat Values. | The value of the listed substance is saved. The regulatory list is added to the paragraph. |  |
| 23 | Add CO2 Equation to the Paragraph | Go to the Equations tab.Choose Add (+ icon) on the left side of the screen to add an equation to the paragraph. | A new row is added. New fields for equation details are displayed on the right side of the screen. |  |
| 24 | Enter Equation Details | On the right side of the screen, enter the following information:Equation Name: CO2 By Carbon Content of the FuelDescription: Equation C3 from 40 CFR part 98 is adapted by applying company-specific reduction factor 0.99. By applying this factor, the emissions are reduced by 1%. | The data in the top section is populated. |  |
| 25 | Enter Equation Result | Go down to the Result section. Choose Add (+icon) to add a result to the equation.Enter or select the following information in the Add Result dialog box that opens:Result: FinalOutput Variable Name: CO2Subject: Carbon dioxideUnit: tChoose OK.Enter the following in the Expression field: (44/12*FUEL*CC*0.91)*0.99.Note The solution comes with predefined equations for greenhouse gas reporting according to US regulation in the following compliance requirement - Predefined Equations for Greenhouse Gas Calculations based on Title 40 Part 98. You can navigate to paragraph Subpart C, Tier 3 Calculation Methodology and use the default expression for CO2 output variable in equation CO2e based on C3, C8, part of this requirement. You can also adapt this expression to the specifics of your company. | The data in the Result section is populated. |  |
| 26 | Add Input Variables | Go down to the Input Variables section. Choose Scan Variables from Expressions to have the input variables populated.Add a description to each variable. To do this, select the row with the variable and scroll down to the Variable Details section. Enter the respective information in the Description field:CC: CC = Annual average carbon content of the solid fuel (percent by weight, expressed as a decimal fraction, e.g., 95% = 0.95). The annual average carbon content shall be determined using the same procedures as specified for HHVFUEL: Fuel = Annual mass of the solid fuel combusted, from company records (short tons).Choose Save at the bottom right side of the screen. | The input variables are saved to the equation. The equation is added to the paragraph. |  |
| 27 | Add CH4 Equation to the Paragraph | While on the Equations tab, choose Add (+ icon) on the left side of the screen to add another equation to the paragraph. | A new row is added. New fields for equation details are displayed on the right side of the screen. |  |
| 28 | Enter Equation Details | On the right side of the screen, enter the following information:Equation Name: CH4 By Annual Fuel ConsumptionDescription: Equation C8 from 40 CFR part 98 is adapted by applying company-specific reduction factor 0.99. By applying this factor, the emissions are reduced by 1%. | The data in the top section is populated. |  |
| 29 | Enter Equation Result | Go down to the Result section. Choose Add (+icon) to add a result to the equation.Enter or select the following information in the Add Result dialog box that opens:Result: FinalOutput Variable Name: CH4Subject: methaneNote Make sure that you select the same methane entry as in the previous steps.Choose OK.Enter the following in the Expression field: (0.001*FUEL*HHV*EF_CH4)*0.99.Note The solution comes with predefined equations for greenhouse gas reporting according to US regulation in the following compliance requirement - Predefined Equations for Greenhouse Gas Calculations based on Title 40 Part 98. You can navigate to paragraph Subpart C, Tier 3 Calculation Methodology and use the default expression for the CH4 output variable in equation CO2e based on C3, C8, part of this requirement. You can also adapt this expression to the specifics of your company. | The data in the Result section is populated. |  |
| 30 | Add Input Variables | Go down to the Input Variables section. Choose Scan Variables from Expressions to have the input variables populated.Choose Save at the bottom right side of the screen. | The input variables are saved to the equation. The equation is added to the paragraph. |  |
| 31 | Add N2O Equation to the Paragraph | While on the Equations tab, choose Add (+ icon) on the left side of the screen to add another equation to the paragraph. | A new row is added. New fields for equation details are displayed on the right side of the screen. |  |
| 32 | Enter Equation Details | On the right side of the screen, enter the following information:Equation Name: N2O By Annual Fuel ConsumptionDescription: Equation C8 from 40 CFR part 98 is adapted by applying company-specific reduction factor 0.99. By applying this factor, the emissions are reduced by 1%. | The data in the top section is populated. |  |
| 33 | Enter Equation Result | Go down to the Result section. Choose Add (+icon) to add a result to the equation.Enter or select the following information in the Add Result dialog box that opens:Result: FinalOutput Variable Name: N2OSubject: nitrous oxideNote Make sure that you select the same nitrous oxide entry as in the previous steps.Choose OK.Enter the following in the Expression field: (0.001*FUEL*HHV*EF_N2O)*0.99.Note The solution comes with predefined equations for greenhouse gas reporting according to US regulation in the following compliance requirement - Predefined Equations for Greenhouse Gas Calculations based on Title 40 Part 98. You can navigate to paragraph Subpart C, Tier 3 Calculation Methodology and use the default expression for the N2O output variable in equation CO2e based on C3, C8, part of this requirement. You can also adapt this expression to the specifics of your company. | The data in the Result section is populated. |  |
| 34 | Add Input Variables | Go down to the Input Variables section. Choose Scan Variables from Expressions to have the input variables populated.Choose Save at the bottom right side of the screen. | The input variables are saved to the equation. The equation is added to the paragraph. |  |
| 35 | Add CO2e Equation to the Paragraph | While on the Equations tab, choose Add (+ icon) on the left side of the screen to add another equation to the paragraph. | A new row is added. New fields for equation details are displayed on the right side of the screen. |  |
| 36 | Enter Equation Details | On the right side of the screen, enter the following information:Equation Name: CO2e By Applying GWP | The data in the top section is populated. |  |
| 37 | Enter Equation Result | Go down to the Result section. Choose Add (+icon) to add a result to the equation.Enter or select the following information in the Add Result dialog box that opens:Result: FinalOutput Variable Name: CO2eChoose OK.Enter the following in the Expression field: GHG*GWP. | The data in the Result section is populated. |  |
| 38 | Add Input Variables | Go down to the Input Variables section. Choose Scan Variables from Expressions to have the input variables populated.Choose Save at the bottom right side of the screen. | The input variables are saved to the equation. The equation is added to the paragraph. |  |
| 39 | Go Back to Policy | Choose Back to Compliance Requirement at the bottom right side of the screen to navigate back to the policy. | The Policy: Yearly Greenhouse Gas Goals screen is displayed. |  |
| 40 | Release Policy | On the Policy: Yearly Greenhouse Gas Goals screen, go to Set Status on the top left side of the screen. Choose Released from the dropdown list and confirm your selection to release the compliance requirement of Policy type. | The Yearly Greenhouse Gas Goals policy is released and can be used in follow-on business processes. |  |

### Create Compliance Scenario for Power Unit B1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new compliance scenario for the Power Unit B1 location. The compliance scenario is needed to set the company's production unit as applicable for compliance requirements about greenhouse emissions reporting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to the Create Compliance Scenario | On the entry screen of the Manage Compliance Scenario (WDA0468) app, choose Create Compliance Scenario. | You are navigated to the Create Compliance Scenario app entry screen. |  |
| 4 | Enter Scenario Details | Under the Basic Information section, enter or select the following information:Valid From: <First day of calendar year>Location: Power Unit B1Note Use the value help to open the Location Structure. If you have not set Power Unit B1 as My Location, choose Show All Locations in the dialog box to display all locations. Find and select the Power Unit B1 entry from the list. Choose OK.Scenario Name: Greenhouse Gas Monitoring B1Description: This scenario includes activities related to the recording, monitoring, and reporting of monthly emission amounts for Power Unit B1. | The information that you've entered is populated under Basic Information. |  |
| 5 | Add Requirement to Scenario | Under the Requirement Paragraph section, use the value help to open the Requirement Paragraph dialog box. Find and select the Yearly Greenhouse Gas Goals compliance requirement from the list. Choose OK. | The Yearly Greenhouse Gas Goals compliance requirement is added to the compliance scenario of Power Unit B1. |  |
| 6 | Save Scenario | While on the Create Compliance Scenario screen, choose Save at the bottom right side of the screen to save the compliance scenario and its details. | The compliance scenario is saved.You are navigated to the Compliance Scenario: Greenhouse Gas Monitoring B1 at Power Unit B1 screen. |  |

### Set Up Compliance Scenario Activities for Power Unit B1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager sets up compliance activities within the created scenario, such as data collections, samplings, and some calculations. The planned activities help the Environmental Manager to ensure the compliance of the company's production unit with the applicable requirements about greenhouse emissions.

The following diagram provides a visual illustration of these activities:

<!-- image omitted: unnamed -->

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenario | Under the Recent tab, find and open the Greenhouse Gas Monitoring B1 compliance scenario that you've created in the previous test procedure. | You are navigated to the Compliance Scenario: Greenhouse Gas Monitoring B1 at Power Unit B1 screen. |  |
| 4 | Add Data Collection | Under the Activities section on the left side of the screen, choose Add (+icon) and select Data Collection from the dropdown list. | The Add Data Collection dialog box is displayed. |  |
| 5 | Enter Data Collection Details | In the Add Data Collection dialog box, enter or select the following information:Name: Monthly Coal UsageData Period: MonthlySubject: CoalNote Use the value help to select the Coal entry with condition Not Specified, Listed Substance ID L00000114516 and CAS Number 125612-26-2, already set in the compliance requirement as part of the previous test procedure. Choose OK.Unit: tChoose OK. | The data collection is added to the compliance scenario. |  |
| 6 | Add Sampling | Under the Activities section on the left side of the screen, choose Add (+icon) and select Sampling from the dropdown list. | The Add Sampling dialog box is displayed. |  |
| 7 | Enter Sampling Details | In the Add Sampling dialog box, enter or select the following information:Sampling Name: Carbon Content of CoalSampling Subject: CoalNote The Coal entry with condition Not Specified and CAS Number 125612-26-2 should already be visible under the Recent tab of the Subject dialog box. Select it and choose OK.Sampling Method: Choose Create to create a sampling method. | You are navigated to the Sampling Method app. |  |
| 8 | Edit and Save Sampling Method | In the Sampling Method Details section of the Sampling Method app, enter or select the following information:Name: Power Unit B1 Sampling MethodType of Sampling Method: Composition (Predefined Analytes)Sampled Subject: CoalNote To select a sampled subject, choose Change next to the Sampled Subject field. From the Set Sampled Subject dialog box that appears, select Listed Substance from the dropdown list of the Sampled Subject Type field. Then, use the value help to select the Coal entry with CAS Number 125612-26-2 and Listed Substance ID L00000114516 from the list. Choose OK to confirm the sampled subject selection.Navigate down to the Analytes section and choose Add (+icon). Use the value help to find and select one after the other the following entries from the list: the Coal entry with CAS Number 125612-26-2, the Sulfur entry with CAS Number 7704-34-9, and the water entry with CAS Number 7732-18-5. Once the entries have been added, select % as a Unit for each one.Choose Save to confirm your entries. | The sampling method is created and analytes are added to it. |  |
| 9 | Release Sampling Method | While on the same screen, go to Set Status on the top left side of the screen and select Released from the dropdown list. Confirm the change. | The sampling method is released and can be used in the compliance scenario. |  |
| 10 | Add Sampling Method to Compliance Scenario | Navigate back to the Add Sampling dialog box of the compliance scenario. Select the sampling method that you've created.In the Analytes section, the analytes that you've added to the sampling method are automatically populated.Verify the entries and choose OK to confirm them. | The sampling is added to the compliance scenario. |  |
| 11 | Navigate to Sampling Overview | Locate the Sampling Definition section on the right side of the screen. Choose Sampling Overview. | You are navigated to a new screen where you can plan samplings. |  |
| 12 | Plan Sampling | Choose Plan Sampling on the top left side of the screen. | The Plan Sampling dialog box is displayed. |  |
| 13 | Schedule Sampling Dates | In the Plan Sampling dialog box, choose Add (+icon) to enable the selection of a sampling date. In the empty row that opens, use the calendar to select <Fifteenth of January of this calendar year> as a first sampling date. Repeat this step to schedule а sampling for <Fifteenth of June of this calendar year>.Choose OK to confirm the planned dates. | The planned dates for sampling are saved. A success message is displayed at the bottom left side of the screen. |  |
| 14 | Add Monthly CO2 Calculation | Go back to the compliance scenario.Under the Activities section on the left side of the screen, choose Add (+icon) and select Calculation from the dropdown list. | The Add Calculation dialog box is displayed. |  |
| 15 | Choose Source for Monthly CO2 Calculation | In the Add Calculation dialog box, choose Equation from Compliance Requirement.Choose OK. | The compliance requirement is set as a source for the calculation. |  |
| 16 | Enter Calculation Details | In the Add Calculation dialog box, enter or select the following information:Calculation Name: Monthly CO2 EmissionsEquation Name: CO2 By Carbon Content of the FuelNote Use the value help to select the CO2 By Carbon Content of the Fuel entry, already set in the compliance requirement as part of the previous test procedure. Choose OK.Choose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 17 | Set Monthly CO2 Calculation | Locate the Calculation Setup section on the right side of the screen. Choose Calculation Setup Details. | You are navigated to a new screen where you can set your calculation. |  |
| 18 | Set Calculation Title | Under the Calculation Setup section, change the Calculation Mode to Automatic. Then go down to the Results section and choose Set Title. | The Set Title dialog box is displayed. |  |
| 19 | Enter CO2 Calculation Subject and Period | In the Set Title dialog box, enter or select the following information:Data Period: MonthlySubject: Carbon dioxideUnit: tChoose OK to confirm your entries. | Entries are saved. |  |
| 20 | Set Data Source Type for Input Variables | Under Input Variables, go to the Data Source Type field. Make the following selections from the dropdown list:For the CC input variable, select Sampled Data.For the FUEL input variable, select Collected Data. | The data source types are selected. |  |
| 21 | Set Data Source for Input Variables | Under Input Variables, go to the Data Source field. Make the following selections from the dropdown list:For the CC input variable, use the value help to select Coal of Coal.For the FUEL input variable, select Monthly Coal.Note The value help is preset to filter for the data source type, scenario, and location that you've already maintained. Once you choose Go, the relevant entries to select as data sources are displayed.Choose OK. | The data sources are selected. |  |
| 22 | Confirm Calculation Setup | Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly CO2 calculation is set and maintained as part of the compliance scenario. |  |
| 23 | Add Monthly CH4 Calculation | Under the Activities section on the left side of the screen, choose Add (+icon) and select Calculation from the dropdown list. | The Add Calculation dialog box is displayed. |  |
| 24 | Choose Source for Monthly CH4 Calculation | In the Add Calculation dialog box, choose Equation from Compliance Requirement.Choose OK. | The compliance requirement is set as source for the calculation. |  |
| 25 | Enter Calculation Details | In the Add Calculation dialog box, enter or select the following information:Calculation Name: Monthly CH4 EmissionsEquation Name: CH4 By Annual Fuel ConsumptionChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 26 | Set Monthly CH4 Calculation | Repeat steps 17 to 22 to set the CH4 calculation with the following changes:When you perform step 19, select methane as Subject.When you perform step 20, select the following data source types for the input variables:For the EF_CH4 input variable, select Regulatory List.For the FUEL input variable, select Collected Data.For the HHV input variable, select Regulatory List.When you perform step 21, select the following data sources for the input variables:For the EF_CH4 input variable, use the value help to display the Search Data Source dialog box. Select Emission Factor from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the Coal entry with pollutant methane. Choose OK to maintain the data source selections.For the FUEL input variable, use the value help to select the Monthly Coal entry.Note The value help is preset to filter for the data source type, scenario, and location that you've already maintained. Once you choose Go, the relevant entry to select as data source is displayed.For the HHV input variable, use the value help to display the Search Data Source dialog box. Select High Heating Value from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the Coal entry. Choose OK to maintain the data source selections.Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly CH4 calculation is set and maintained as part of the compliance scenario. |  |
| 27 | Add Monthly N2O Calculation | Under the Activities section on the left side of the screen, choose Add (+icon) and select Calculation from the dropdown list. | The Add Calculation dialog box is displayed. |  |
| 28 | Choose Source for Calculation | In the Add Calculation dialog box, choose Equation from Compliance Requirement.Choose OK. | The compliance requirement is set as source for the calculation. |  |
| 29 | Enter Calculation Details | In the Add Calculation dialog box, enter or select the following information:Calculation Name: Monthly N2O EmissionsEquation Name: N2O By Annual Fuel ConsumptionChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 30 | Set Monthly N2O Calculation | Repeat steps 17 to 22 to set the N2O calculation with the following changes:When you perform step 19, select nitrous oxide as Subject.When you perform step 20, select the following data source types for the input variables:For the EF_ N2O input variable, select Regulatory List.For the FUEL input variable, select Collected Data.For the HHV input variable, select Regulatory List .When you perform step 21, select the following data sources for the input variables:For the EF_ N2O input variable, use the value help to display the Search Data Source dialog box. Select Emission Factor from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the Coal entry with pollutant nitrous oxide. Choose OK to maintain the data source selections.For the FUEL input variable, use the value help to select the Monthly Coal entry.Note The value help is preset to filter for the data source type, scenario, and location that you've already maintained. Once you choose Go, the relevant entry to select as data source is displayed.For the HHV input variable, use the value help to display the Search Data Source dialog box. Select High Heating Value from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the Coal entry. Choose OK to maintain the data source selections.Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly N2O calculation is set and maintained as part of the compliance scenario. |  |
| 31 | Add Monthly CO2-to-CO2e Calculation | Repeat steps 14 to 16 to add a new calculation with the following details:Calculation Name: Conversion of CO2 to CO2eEquation Name: CO2e By Applying GWPChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 32 | Set Monthly CO2-to-CO2e Calculation | Repeat steps 17 to 22 to set the CO2-to-CO2e calculation with the following changes:When you perform step 19, select Carbon Dioxide Equivalent as Subject. Make sure that you select the same Carbon Dioxide Equivalent entry from the list that you've already used in the previous test procedures.When you perform step 20, select the following data source types for the input variables:For the GHG input variable, select Calculated Data.For the GWP input variable, select Regulatory List.When you perform step 21, select the following data sources for the input variables:For the GHG input variable, use the value help to select the Monthly Carbon dioxide entry. Choose OK to maintain the data source selection.For the GWP input variable, use the value help to display the Search Data Source dialog box. Select Global Warming Potential from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the Carbon dioxide entry. Choose OK to maintain the data source selections.Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly CO2-to-CO2e calculation is set and maintained as part of the compliance scenario. |  |
| 33 | Add Monthly CH4-to-CO2e Calculation | Repeat steps 14 to 16 to add a new calculation with the following details:Calculation Name: Conversion of CH4 to CO2eEquation Name: CO2e By Applying GWPChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 34 | Set Monthly CH4-to-CO2e Calculation | Repeat steps 17 to 21 to set the CH4-to-CO2e calculation with the following changes:When you perform step 19, select Carbon Dioxide Equivalent as Subject. Make sure that you select the same Carbon Dioxide Equivalent entry from the list that you've already used in the previous test procedures.When you perform step 20, select the following data source types for the input variables:For the GHG input variable, select Calculated Data.For the GWP input variable, select Regulatory List.When you perform step 21, select the following data sources for the input variables:For the GHG input variable, use the value help to select the Monthly methane entry. Choose OK to maintain the data source selection.For the GWP input variable, use the value help to display the Search Data Source dialog box. Select Global Warming Potential from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box that appears, choose Go and select the methane entry. Choose OK to maintain the data source selections.Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly CH4-to-CO2e calculation is set and maintained as part of the compliance scenario. |  |
| 35 | Add Monthly N2O-to-CO2e Calculation | Repeat steps 14 to 16 to add a new calculation with the following details:Calculation Name: Conversion of N2O to CO2eEquation Name: CO2e By Applying GWPChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 36 | Set Monthly N2O-to-CO2e Calculation | Repeat steps 17 to 21 to set the N2O-to-CO2e calculation with the following changes:When you perform step 19, select Carbon Dioxide Equivalent as Subject. Make sure that you select the same Carbon Dioxide Equivalent entry from the list that you've already used in the previous test procedures.When you perform step 20, select the following data source types for the input variables:For the GHG input variable, select Calculated Data.For the GWP input variable, select Regulatory List.When you perform step 21, select the following data sources for the input variables:For the GHG input variable, use the value help to select the Monthly nitrous oxide entry. Choose OK to maintain the data source selection.For the GWP input variable, use the value help to display the Search Data Source dialog box. Select Global Warming Potential from the Regulatory List dropdown list. Choose OK to save your selection. In the new dialog box box that appears, choose Go and select the nitrous oxide entry. Choose OK to maintain the data source selections.Choose Save to confirm your selections and maintain the calculation details in the scenario.Choose Back to Compliance Scenario to return to the scenario. | The monthly N2O-to-CO2e calculation is set and maintained as part of the compliance scenario. The compliance scenario screen is displayed. |  |
| 37 | Add Monthly CO2e Location Aggregation | Under the Activities section on the left side of the screen, choose Add (+icon) and select Location Aggregation from the dropdown list. | The Add Location Aggregation dialog box is displayed. |  |
| 38 | Enter Location Aggregation Details | In the Add Location Aggregation dialog box, enter or select the following information:Name: Monthly GHG Emissions in CO2eData Period: MonthlySubject: Carbon Dioxide EquivalentUnit: tFunction: Arithmetic Sum (SUM)Choose OK. | The location aggregation is added to the compliance scenario. |  |
| 39 | Navigate to Aggregation Setup | On the right side of the screen, go to Edit Aggregation Setup. | You are navigated to a new screen where you can edit the aggregation details. |  |
| 40 | Set Aggregation Mode | In the Location Aggregation Details section, go to Aggregation Mode and select Automatic from the dropdown list.Choose Save on the bottom right side of the screen to save the aggregation details. | The aggregation mode is saved to Automatic. |  |
| 41 | Add Classifier | In the same section, go to Aggregate by Classifier and choose Create. | The Create Data Classifier dialog box is displayed. |  |
| 42 | Create Data Classifier | In the Create Data Classifier dialog box, enter the following in the Classifier field: Power Unit B1.Choose OK to save the classifier.Choose Save at the bottom right side of the screen. | The classifier is saved and selected. |  |
| 43 | Set Classifier | Locate and expand the Matching Data section.Select all entries in the list. Choose Set Classifier.Choose Save at the bottom right side of the screen. | The Power Unit B1 classifier is set to all result data sets of the location aggregation. |  |
| 44 | Go Back to Compliance Scenario | Choose Back to Compliance Scenario. |  |  |

### Copy Compliance Scenario to Power Unit B2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager copies the already created compliance scenario for Power Unit B1 to Power Unit B2. This helps the Environmental Manager to easily scale up with the setup for compliance management for the additional production unit of the company where the same compliance requirement applies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenarios in the Location Structure | On the entry screen of the Manage Compliance Scenario (WDA0468) app, navigate to the Display by Location tab.Under the Location Structure section, select the Power Unit B1 entry from the list.Note If you have not set Future Energy as My Location, choose Show All Locations to display all locations and navigate to the Power Unit B1 entry. | The compliance scenario assigned to the Power Unit B1 location is displayed on the right side of the screen under the Manage Compliance Scenario tab. |  |
| 4 | Copy Compliance Scenario | Under the Manage Compliance Scenario tab, select the Greenhouse Gas Monitoring B1 compliance scenario entry.Choose Copy Compliance Scenario located above the selected entry. | The Copy Compliance Scenario dialog box is displayed. |  |
| 5 | Enter Details for the New Compliance Scenario | In the Copy Compliance Scenario dialog box, make the following entries:New Compliance Scenario Start Date: <First day of calendar year>New Compliance Scenario Name: Greenhouse Gas Monitoring B2 | Your entries are populated in the fields. |  |
| 6 | Select Power Unit B2 as Location of the New Compliance Scenario | Under the Selected Locations section, choose Add and select Add from Location Structure from the dropdown list.In the Add from Location Structure dialog box that opens, find and select the Power Unit B2 location entry. Choose OK to confirm the selection. | The Power Unit B2 location is selected as a location for the new compliance scenario. |  |
| 7 | Complete Copy of Compliance Scenario | In the Copy Compliance Scenario dialog box, choose Confirm Copy on the bottom right side of the dialog box.Note Make sure that you do not have the scenario you are copying from open in another window of your browser. This blocks the copying of the scenario. | A success message is displayed on the bottom left side of the screen. The compliance scenario, together with the activities in it, is copied to Power Unit B2. The new scenario is visible under the Location Structure for Power Unit B2. |  |
| 8 | Navigate to the Copied Compliance Scenario | In the location structure, select the Power Unit B2 entry. The compliance scenario assigned to Power Unit B2 location is displayed on the right side of the screen under the Manage Compliance Scenario tab.Go inside the Greenhouse Gas Monitoring B2 compliance scenario entry. | You are navigated to the Greenhouse Gas Monitoring B2 at Power Unit B2 compliance scenario. |  |
| 9 | Adapt Scenario Description | Go to Basic Information. Locate the Compliance Scenario Details section on the right side of the screen and adapt the description of the scenario. Replace Power Unit B1 with Power Unit B2.Choose Save. | The changes to the description are saved. |  |
| 10 | Adapt Location Aggregation | Under the Activities section, select each of the monthly location aggregations.On the right side of the screen, choose Edit Aggregation Setup. | You are navigated to a new screen where you can edit the aggregation details. |  |
| 11 | Change Classifier | Find the Location Aggregation Details section. In the Aggregate by Classifier field, remove the Power Unit B1 classifier.Choose Create. | The Create Data Classifier dialog box is displayed. |  |
| 12 | Create Data Classifier | In the Create Data Classifier dialog box, enter the following in the Classifier field: Power Unit B2.Choose OK to save the classifier.Choose Save at the bottom right side of the screen. | The classifier is saved and selected. |  |
| 13 | Set Classifier | Locate and expand the Matching Data section.Select all entries in the list. Choose Set Classifier.Choose Save at the bottom right side of the screen. | The Power Unit B2 classifier is set to all result data sets of the location aggregation. |  |
| 14 | Go Back to Compliance Scenario | Go back to the compliance scenario screen. |  |  |
| 15 | Adapt Sampling | Under the Activities section, select the sampling activity.Locate the Sampling Definition section on the right side of the screen. Choose Sampling Overview. | You are navigated to a new screen where you can plan samplings. |  |
| 16 | Plan Sampling | Choose Plan Sampling on the top left side of the screen. | The Plan Sampling dialog box is displayed. |  |
| 17 | Schedule Sampling Dates | In the Plan Sampling dialog box, choose Add (+icon) to enable the selection of a sampling date. In the empty row that opens, use the calendar to select <Fifteenth of January of this calendar year> as a first sampling date. Repeat this step to schedule а sampling for <Fifteenth of June of this calendar year>.Choose OK to confirm the planned dates. | The planned dates for sampling are saved. A success message is displayed at the bottom left side of the screen. |  |

### Create Compliance Scenario for Power Plant Boston

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new compliance scenario for the Power Plant Boston location. The compliance scenario is needed to set up the applicability of the whole company to the compliance requirement about greenhouse emissions

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Location | On the entry screen of the Manage Compliance Scenario (WDA0468) app, navigate to the Display by Location tab.Under the Location Structure section, select the Power Plant Boston entry from the list. With the entry selected, choose Create Compliance Scenario from the top left side of the screen.Note If you have not set Power Plant Boston as My Location, choose Show All Locations to display all locations. | You are navigated to the Create Compliance Scenario app entry screen.The Location field of the new scenario is automatically populated to Power Plant Boston based on your selection. |  |
| 4 | Enter Scenario Details | Under the Basic Information section, enter or select the following information:Valid From: <First day of calendar year>Scenario Name: GHG Monitoring and ReportingDescription: This scenario includes activities for the aggregation of GHG data from all production units of the plant for monitoring and reporting purposes. | The information that you've entered is populated under the Basic Information section. |  |
| 5 | Add Requirement to Scenario | Under the Requirement Paragraph section, use the value help to open the Requirement Paragraph dialog box. Find and select the Yearly Greenhouse Gas Goals compliance requirement from the list. Choose OK. | The Yearly Greenhouse Gas Goals compliance requirement is added to the compliance scenario of Power Plant Boston. |  |
| 6 | Save Scenario | While on the Create Compliance Scenario screen, choose Save at the bottom right side of the screen to save the compliance scenario and its details. | The compliance scenario is saved. You are navigated to the Compliance Scenario: GHG Monitoring and Reporting at Power Plant Boston screen. |  |

### Set Up Compliance Scenario Activities for Power Plant Boston

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager sets up compliance scenario activities, such as calculations and aggregations, for Power Plant Boston. These activities help the Environmental Manager to check emissions data from all power plants in the company and verify that the set company targets can be met.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenario | Under the Recent tab, find and open the GHG Monitoring and Reporting compliance scenario that you've created in the previous test procedure. | You are navigated to the Compliance Scenario: GHG Monitoring and Reporting screen. |  |
| 4 | Add Location Aggregation | Under the Activities section on the left side of the screen, choose Add (+icon) and select Location Aggregation from the dropdown list. | The Add Location Aggregation dialog box is displayed. |  |
| 5 | Enter Location Aggregation Details | In the Add Location Aggregation dialog box, enter or select the following information:Name: Monthly CO2 TargetData Period: MonthlySubject: Carbon Dioxide EquivalentUnit: tFunction: Arithmetic Sum (SUM)Choose OK. | The location aggregation is added to the compliance scenario. |  |
| 6 | Assign Environmental Limit | Under the Assigned Environmental Limits section on the right side of the screen, choose Assign Environmental Limits.In the dialog box that opens, select the prepopulated monthly upper limit from the compliance requirement. Choose OK.Choose Save to confirm your selection. | The environmental limit is assigned. |  |
| 7 | Navigate to Aggregation Setup | While on the same screen, find the Location Aggregation section. Choose Edit Aggregation Setup. | You are navigated to a new screen where you can edit the aggregation details. |  |
| 8 | Set Aggregation Mode | In the Location Aggregation Details section, go to Aggregation Mode and select Automatic from the dropdown list.Choose Save on the bottom right side of the screen to save the aggregation details. | The aggregation mode is saved to Automatic. |  |
| 9 | Add Classifier | In the same section, go to Aggregate by Classifier and choose Create. | The Create Data Classifier dialog box is displayed. |  |
| 10 | Create Data Classifier | In the Create Data Classifier dialog box, enter the following in the Classifier field: Power Plant Boston.Choose OK to save the classifier.Choose Save at the bottom right side of the screen. | The classifier is saved and selected. |  |
| 11 | Set Classifier | Find and expand the Matching Data section.Select all entries in the list. Choose Set Classifier.Choose Save at the bottom right side of the screen. | The Power Plant Boston classifier is set to all result data sets of the location aggregation.Location aggregation setup is completed. |  |
| 12 | Add Calculation for CO2e Monthly-to-Yearly Aggregated Data | Under the Activities section on the left side of the screen, choose Add (+icon) and select Calculation from the dropdown list. | The Add Calculation dialog box is displayed. |  |
| 13 | Choose Source for Calculation | In the Add Calculation dialog box, choose New Local Expression.Choose OK. | The Add Calculation dialog box is displayed. |  |
| 14 | Enter Calculation Details | In the Add Calculation dialog box, enter or select the following information:Calculation Name: Monthly-to-Yearly CO2eData Period: YearlySubject: Carbon Dioxide EquivalentUse the value help to select the Carbon Dioxide Equivalent. It should be visible under the Recent tab.Unit: tChoose OK to confirm all entries in the Add Calculation dialog box. | The calculation is added to the compliance scenario. |  |
| 15 | Assign Environmental Limit | Under the Calculation Results section on the right side of the screen, choose Assign Environmental Limits.In the dialog box that opens, select the prepopulated yearly upper limit from the compliance requirement. Choose OK.Choose Save to confirm your selection. | The environmental limit is assigned. |  |
| 16 | Set Calculation | Locate the Calculation Setup section on the right side of the screen. Choose Calculation Setup Details. | You are navigated to a new screen where you can set your calculation. |  |
| 17 | Set Calculation Mode and Expression | Under the Calculation Setup section, go to Calculation Mode. Select Automatic from the dropdown list.Next, go to the Expression section. Enter the following: SUM(Monthly_GHG). |  |  |
| 18 | Set Input Variables | Under the Input Variables section, choose Scan Variables from Expression. | The input variables are added to the calculation. |  |
| 19 | Set Data Source Type for Input Variables | Under Input Variables, go to the Data Source Type field. Select Location Aggregation Data from the dropdown list. | The data source type is selected. |  |
| 20 | Set Data Source for Input Variables | Under Input Variables, go to the Data Source field. Use the value help to select the SUM Monthly Carbon Dioxide Equivalent t /ID: 12 from the list.Choose OK. | The data source is selected. |  |
| 21 | Confirm Calculation Setup | Choose Save to confirm your selections and maintain the calculation details in the scenario. | The calculation is set and maintained as part of the compliance scenario. |  |
| 22 | Set Data Classifier | Go back to compliance scenario. Select the Monthly-to-Yearly CO2e calculation from the scenario activities on the left side of the screen.Locate the Calculation Results section on the right side of the screen. Choose Manage Data Classifiers. In the dialog box that opens, choose Create Data Classifier. Enter the following in the Data Classifier field: Annual_GHG_Report. | The data classifier is selected for assignment. |  |
| 23 | Assign Data Classifier | Choose Assign Data Classifier to assign the classifier to the calculation result data sets.Close the dialog box. | The data classifier is assigned to the result data sets of the calculation.The relevant data from the system can later be easily grouped by data classifier for reporting purposes. |  |

### Activate Compliance Scenarios for Power Plant Boston and Its Sublocations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager activates the compliance scenarios for Power Plant Boston and its sublocations in one go. Once the scenarios are active, the compliance activities planned in them can start and the Environmental Manager can begin to monitor compliance on a company level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Find Power Plant Boston Location in the Location Structure | On the Manage Compliance Scenario screen, navigate to the Display by Location tab.Under the Location Structure section, find the Power Plant Boston location.In case you have already set Power Plant Boston as My Location during the preliminary setup procedure, it will appear as a top location in your location structure.In case you haven´t, choose Show All Locations. Go down the location structure and select the Power Plant Boston entry. | The compliance scenario assigned to Power Plant Boston location is displayed on the right side of the screen under the Manage Compliance Scenario tab. |  |
| 4 | Display All Scenarios for Power Plant Boston and Its Sublocations | Above the Manage Compliance Scenario tab, select the Display Results for Selected Location and its Sublocations checkbox. | The scenario list on the right side of the screen under the Manage Compliance Scenario tab is refreshed. All scenarios for Power Plant Boston and its sublocation are displayed. |  |
| 5 | Activate Scenarios | In the list under the Manage Compliance Scenario tab for Power Plant Boston, select all scenario entries.Choose Activate. The Activate Multiple Compliance Scenarios dialog box opens. Choose Activate to confirm the activation. | All scenarios are activated in one go. |  |

### Record Environmental Data for Power Unit B1

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager enters emissions data for Power Unit B1 to reflect the monthly samplings, part of the company's operations. The Production Operator - EHS Info does the same for the company's data collection activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open the Manage Compliance Scenario (WDA0468) app. | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenario | Under the Recent tab, find and open the Greenhouse Gas Monitoring B1 compliance scenario that you created in one of the previous test procedures. | You are navigated to the Compliance Scenario: Greenhouse Gas Monitoring B1 at Power Unit B1 screen. |  |
| 4 | Navigate to Sampling Overview | Under the Activities section on the left side of the screen, select the Carbon Content of Coal sampling activity.On the right side of the screen, locate the Sampling Definition section. Choose Sampling Overview. | You are navigated to the Finalize Sampling app where you can get an overview of all samplings that you have scheduled as part of the Set Up Compliance Scenario Activities for Power Unit B1 test procedure. |  |
| 5 | Enter Sampling Results | Under Finalize Samples, choose Enter Results to record an amount that you've received from samples. | You are navigated to a new screen where you can record the sampling amount. |  |
| 6 | Record Sampling Results | Locate the Physical Sample Results section. Under the Finalized Results tab, go to Value. Enter the following sampling results for the samplings scheduled for <Fifteenth of January of this calendar year>:99% for Coal0.5% for Water0.5% for SulfurChoose Submit Results at the top left side of the screen. | The sampling amounts are recorded. |  |
| 7 | Go Back to Compliance Scenario | From the Finalize Sampling app, choose the arrow next to the SAP logo to return to the compliance scenario. | You are navigated back to the Compliance Scenario: Greenhouse Gas Monitoring B1 at Power Unit B1 screen. |  |
| 8 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. |  |  |
| 9 | Access the My Data Collections App | Open My Data Collections (F3991).Note The app might not be visible as a tile on the SAP Fiori launchpad. If this is the case, use the search field or choose App Finder from your profile menu to find it. | You are navigated to the My Data Collections screen. |  |
| 10 | Navigate to Data Collection | Under the All tab, find and select the Monthly Coal Usage data collection entry for Power Unit B1. | You are navigated to the Monthly Coal Usage data collection. |  |
| 10 | Edit Data Collection | Make sure that you have selected the Pending tab under Amounts to view all pending data records. Then, choose Edit on the top right side of the screen. | The data record amounts are open for editing. |  |
| 12 | Enter Data Collection Values | In the Value field, enter amounts for all pending data records. For example, for the data records for winter months, enter around <500000> t. For data records for summer months, enter around <380000> t.Once you've entered values for all pending data records, choose Save at the bottom right side of the screen. | The data collection values are saved. |  |

### Record Environmental Data for Power Unit B2

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager enters emission data for Power Unit B2 to reflect the monthly samplings and data collections, part of the company's operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenario | Under the Recent tab, find and open the Greenhouse Gas Monitoring B2 compliance scenario. | You are navigated to the Compliance Scenario: Greenhouse Gas Monitoring B2 at Power Unit B2 screen. |  |
| 4 | Navigate to Sampling Overview | Under the Activities section on the left side of the screen, select the Carbon Content of Coal sampling activity.On the right side of the screen, locate the Sampling Definition section. Choose Sampling Overview. | You are navigated to a new screen where you can get an overview of all sampling that you have scheduled in the compliance scenario for Power Unit B1 and have copied to the compliance scenario for Power Unit B2. |  |
| 5 | Enter Sampling Results | Under Finalize Sampling, choose Enter Results to record the amounts that you've received from samples. | You are navigated to a new screen where you can record the sampling amounts. |  |
| 6 | Record Sampling Results | Locate the Physical Sample Results section. Under the Finalized Results tab, go to Value. Enter the following sampling results for the samplings scheduled for <Fifteenth of January of this calendar year>:99% for Coal0.5% for Water0.5% for SulfurChoose Submit Results at the top left side of the screen. | The sampling amounts are recorded. |  |
| 7 | Go Back to Compliance Scenario | From the Finalize Sampling app, choose the arrow next to the SAP logo to return to the compliance scenario. | You are navigated back to the Compliance Scenario: Greenhouse Gas Monitoring B2 at Power Unit B2 screen. |  |
| 8 | Navigate to Data Collection | Under the Activities section on the left side of the screen, select the Monthly Coal Usage data collection activity.On the right side of the screen, locate the Data Collection Definition section. Choose Monitor Collected Data. | You are navigated to the Monitor Data - Environment Management (WDA0149) app. |  |
| 9 | Switch to Table View | In the Monitor Data - Environment Management (WDA0149) app, verify that the filters are set to the correct dates to reflect the full compliance scenario data.Then, right under the header section, hover right and switch to the table view. | A list of collected data records with missing amounts is loaded in a table. |  |
| 10 | Replace Amounts | Select the top entry from the list. On the top right side of the table, choose Replace. | The Replace Data Record dialog box is displayed. The data record amount is opened for editing. |  |
| 11 | Enter Data Collection Values | In the Replace Data Record dialog box, enter the amounts that you've received for the pending data record and choose Replace.Repeat the same step to enter amounts for all pending data records. For example, for the data records for winter months, enter around <440000> t. For data records for summer months, enter around <390000> t.Note You can select multiple data records and add amounts for all of them in one go. | The data collection amounts are recorded. |  |

### Monitor Environmental Data for Power Plant Boston

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager checks the incoming monthly emissions data for Power Plant Boston. The Environmental Manager analyzes the data against applicable environmental limits. This helps the Environmental Manager to trace the compliance of the company's production unit over time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Compliance Scenario | Under the Recent tab, find and open the GHG Monitoring and Reporting compliance scenario. | You are navigated to the Compliance Scenario: GHG Monitoring and Reporting at Power Plant Boston screen. |  |
| 4 | Monitor Monthly-to-Yearly CO2e Data on a Company Level | Under the Activities section on the left side of the screen, select the Monthly-to-Yearly CO2e calculation activity.On the right side of the screen, locate the Calculation Results section. Choose Monitor Calculated Data. | You are navigated to the Monitor Data - Environment Management (WDA0149) app. |  |
| 5 | Adjust Filters | Adjust the filters to the data period of your scenario. Choose Go. | The calculated CO2e data is displayed in the graphical view. |  |
| 6 | Check Data Against Environmental Limit | Under the filter bar, on the left side of the screen, choose Show Limit and select the Yearly CO2e Target environmental limit. This way, you can easily measure the data of your production unit against that limit. |  |  |
| 7 | Go back to Compliance Scenario | Go back to the compliance scenario screen. |  |  |
| 8 | Monitor Monthly CO2 Target Data on a Company Level | Under the Activities section on the left side of the screen, select the Monthly CO2 Target location aggregation.On the right side of the screen, find the Location Aggregation section. Choose Monitor Aggregated Data. | You are navigated to the Monitor Data - Environment Management (WDA0149) app. |  |
| 9 | Check Data Against Environmental Limit | Repeat steps 5 to 6 check the monthly CO2 data entered for your production units over time. When you perform step 6, choose Show Limit and select the Monthly CO2 Target environmental limit. |  |  |

### Create a Deviation for Power Plant Boston

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Based on the monitoring and analysis of incoming monthly emissions data for Power Plant Boston, the Environmental Manager creates a deviation incident for the data where company goals are not met.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Compliance Scenario (WDA0468). | The Manage Compliance Scenario screen is displayed. |  |
| 3 | Navigate to Scenario | Under the Recent tab, find and open the GHG Monitoring and Reporting compliance scenario. | You are navigated to the Compliance Scenario: GHG Monitoring and Reporting at Power Plant Boston screen. |  |
| 4 | Monitor Aggregated Data | Under the Activities section on the left side of the screen, select the Monthly CO2 Target location aggregation.On the right side of the screen, find the Location Aggregation section. Choose Monitor Aggregated Data. | You are navigated to the Monitor Data - Environment Management (WDA0149) app. |  |
| 5 | Adjust Filters | Adjust the filters to the data period of your scenario. Choose Go.Next, from the Show Limit dropdown list, select Monthly CO2 target. | The aggregated data for the location is displayed for the selected time period. The monthly environmental limit, part of the assigned compliance requirement, is displayed. |  |
| 6 | Create Deviation | You've identified that one of the amounts goes above the upper environmental limit. Select that amount in the graphical view.To create a deviation for that amount and initiate closer checks on it, choose Create Deviation Incident from the top right side of the graphical view. | The Create Deviation Incident dialog box is displayed. |  |
| 7 | Enter Deviation Information | In the Create Deviation Incident dialog box, enter or select the following information:Title: Company GHG Target not achievedEnd Date: <A date two months after the date when the amount exceeding the limit was first recorded>Note The date when the amount exceeding the limit was first recorded is automatically selected as a Start Date.Choose Create. | The deviation incident is created with the selected deviating value assigned to it.To view the created deviation incident, open Manage Deviation Incident on the SAP Fiori launchpad. Find the newly created record under the Recent tab. Select it to navigate into the deviation and go to the Deviation tab to learn more about it. |  |

### Create Annual GHG Report for Power Plant Boston

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates an internal annual report for GHG emissions in Power Plant Boston to get a summary of the available greenhouse gas data in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. |  |  |
| 2 | Access App | Open Manage Environmental Reports​ (F5638). | The Manage Environmental Reports screen is displayed. |  |
| 3 | Create Report | On the Manage Environmental Reports screen, choose Create. In the dialog box that opens, select the SAP EM Standard Greenhouse Gas Report template. | You are navigated to the report creation page. |  |
| 4 | Specify Report Information | Under Report Information, enter or select the following information:Report Name: Annual GHG Report Plant BostonReporting Period: <enter current calendar year>Main Location: Power Plant BostonChoose Create at the bottom right side of the screen. | The report details are specified and the report is created. You are navigated to the report page. |  |
| 5 | Generate Report | In the actions bar on the top right of the report page, choose Generate. | The final report is generated. |  |
| 6 | View Report | Navigate back to the initial page of the app, and choose Go to display the most recently created reports. The Annual GHG Report Plant Boston report should appear at the top of the list.When the report generation is complete (this may take a few minutes), you will be able to see and open the XLSX report file under the File Name column.Note The report displays the converted CО2e of all emissions at the company location. This is why there's no data for other elements in the report; all emissions have been converted to their CO2 equivalent. | The XLSX report file is ready to view. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-compliance-management-for-environment-health-and-safety-4c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4XD_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 88,008 chars in the whole document
