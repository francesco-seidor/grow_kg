---
id: 04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-south-africa-5z5-test-scrip
title: Compliance Formats – Support Preparation for South Africa (5Z5) – Test Script (5Z5_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5Z5: South Africa VAT201, BBBEE AP analytics and cash flow statutory reports, with setup steps."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/south-africa-vat]
aliases: [5Z5_S4CLD2608_BPD_EN_XX]
keywords: [South Africa VAT Calculation and Reporting, vat201 declaration, vat201 supporting data file, south africa cash flow report, south africa ap analytics, bbbee vendor classification, statutory reports, advanced compliance reporting, cash flow report hierarchies, statutory report parameters]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z5_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1136
topic: 04-tax-and-statutory-reporting/south-africa-vat
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Compliance Formats – Support Preparation for South Africa (5Z5) – Test Script (5Z5_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z5_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **South Africa VAT Calculation and Reporting** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Compliance Formats – Support Preparation for South Africa (5Z5)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Compliance Formats – Support Preparation for South Africa (5Z5) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841302)

[2 Prerequisites 4](#_Toc232841303)

[2.1 System Access 4](#_Toc232841304)

[2.2 Roles 4](#_Toc232841305)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232841306)

[2.4 Business Conditions 6](#_Toc232841307)

[2.5 Preliminary Steps 6](#_Toc232841308)

[2.5.1 Import Cash Flow Report Hierarchies for South Africa 6](#_Toc232841309)

[2.5.2 Setting Up Your Statutory Cash Flow Report for South Africa 9](#_Toc232841310)

[2.5.3 Class Handling for South Africa AP Analytics 11](#_Toc232841311)

[2.5.3.1 Check Classes for BBBEE Vendor Report 11](#_Toc232841312)

[2.5.3.2 Assignment of BBBEE Classes to Vendor 12](#_Toc232841313)

[2.5.3.3 Maintain Business Partner Master Data BBBEE Class Values For Vendor 13](#_Toc232841314)

[2.5.4 Assign Company Code 14](#_Toc232841315)

[2.5.5 Activate Registration for Indirect Taxation Abroad 16](#_Toc232841316)

[2.5.5.1 Activate Registration for Indirect Taxation Abroad (Optional) 16](#_Toc232841317)

[3 Overview Table 17](#_Toc232841318)

[4 Test Procedures 18](#_Toc232841319)

[4.1 Run Statutory Reports - South Africa AP Analytics 18](#_Toc232841320)

[4.2 Run Statutory Reports - VAT201 - Declaration 19](#_Toc232841321)

[4.3 Run Statutory Reports - VAT 201 - Supporting Data File 21](#_Toc232841322)

[4.4 Run Statutory Reports - South Africa Cash Flow Indirect Method Reporting 24](#_Toc232841323)

## Purpose

Overview

SAP S/4HANA for advanced compliance reporting is a global legal reporting platform that caters to companies’ indirect tax reporting requirements. This solution enables the end-to-end process of legal reporting including multiple activities that may be necessary to complete the legal reporting. The solution offers a unified and harmonized user experience across countries and reports, enabling a simplified view of the reporting status to the business users and the company's head of tax and compliance. It also provides a design environment to easily create and extend additional report requirements.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

Additional Information on the SAP Help Portal

For additional information, including descriptions of features for Advanced Compliance Reporting, visit the SAP Help Portal ([https://help.sap.com](https://help.sap.com)). On the initial page, enter: Advance Compliance Reporting in the Search field. The results provide additional documentation details about Advanced Compliance Reporting.

With the introduction of scope item Document and Reporting Compliance (5XU), this scope item has been restructured. It now only contains content that does not require an additional license. To use advanced features as specified in the feature and scope description of SAP S/4HANA Cloud Public Edition, an additional license of either SAP S/4HANA Cloud for Advanced Compliance Reporting (discontinued) or its successor SAP Document and Reporting Compliance for SAP S/4HANA Cloud Public Edition is required. To enable the advanced features, please activate scope item 5XU and follow the corresponding instructions.

|  |
| --- |
| Note If your instance was already live before CE2111, we ensure continuity. The advanced features are still visible. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| General Ledger Accountant for South Africa | SAP_BR_GL_ACCOUNTANT_ZA |  |  |  |
| Accounts Payable Manager for South Africa | SAP_BR_AP_MANAGER_ZA |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Product Configuration Modeler | SAP_BR_PRODUCT_CONFIG_MODELER | Variant Configuration | SAP_BR_PRODUCT_CONFIG_MODELER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedures. If you have installed an SAP Best Practices package, you can use the following package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 6410 |  |  |
| Controlling Area | A000 |  |  |
| House Bank | ZABK1/ZAAC1 ZABK2/ZAAC2 | BK1 is used for the Multi-Bank Connectivity (MBC) and BK2 is used for file download. |  |
| Bank G/L Account | 11001000,11002000 |  |  |
| Cost Center | 64101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for customers and payments for the invoices are created. |
| J60 - Accounts Payable | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |
| J62 - Asset Accounting | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |

### Preliminary Steps

#### Import Cash Flow Report Hierarchies for South Africa

Purpose

In this activity, you import the report hierarchies for Cash flow indirect method.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Set Local Version | Choose Set Local Version.On the Set Local Version dialog box, select South Africa from the dropdown and choose Set Local Version. | The local version is set to South Africa. |  |
| 4 | Configure Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 5 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: General LedgerOn the Configuration Items list, select the row of the Item Name: Chart of Accounts. | The Configure Your Solution - Chart of Accounts item details view display. |  |
| 6 | Configure | On the Configuration Steps list, for the Define Financial Statement Versions in Global Hierarchies row, choose Configure. | The Change View "Manage Global Hierarchies": Overview view is displayed. |  |
| 7 | Import Hierarchy | Choose Import Hierarchy. | An Import Hierarchy dialog box displays. |  |
| 8 | Enter Version Criteria | Make the following entries and choose OK:Source: Maintain Financial Statement VersionsFinancial Statement Version ID: ZACFSelect the row of the entry and the information is entered on the Import Hierarchy dialog box. | The Create a Hierarchy Based On <ZACF> dialog box displays. |  |
| 9 | Create a Hierarchy | Make the following entries and choose Create:Type: Financial Statement Version (selected)Hierarchy ID: CFZAHierarchy Description: For example, Indirect Cash Flow Statement ZAChart of Account: YCOA (selected)Valid From: <Current date>Valid To: For example, 12/31/9999 | The Hierarchy ID CFZA was successfully created notification appears. The Manage Global Hierarchies view displays. |  |
| 10 | Open Details | Double-click the new hierarchy on the Hierarchy List. | A CFZA - Financial Statement Version details view displays. |  |
| 11 | Activate | Choose Activate. | The CFZA hierarchy activates. |  |

SAP Central Business Configuration:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Chart of Accounts | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Chart of Accounts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Chart of Accounts item details view display. |  |
| 3 | Configure | On the Configuration Steps list, for the Define Financial Statement Versions in Global Hierarchies row, choose Configure. | The Change View "Manage Global Hierarchies": Overview view is displayed. |  |
| 4 | Import Hierarchy | Choose Import Hierarchy. | An Import Hierarchy dialog box displays. |  |
| 5 | Enter Version Criteria | Make the following entries and choose OK:Source: Maintain Financial Statement VersionsFinancial Statement Version ID: ZACFSelect the row of the entry and the information is entered on the Import Hierarchy dialog box. | The Create a Hierarchy Based On <ZACF> dialog box displays. |  |
| 6 | Create a Hierarchy | Make the following entries and choose Create:Type: Financial Statement Version (selected)Hierarchy ID: CFZAHierarchy Description: For example, Indirect Cash Flow Statement ZAChart of Account: YCOA (selected)Valid From: <Current date>Valid To: For example, 12/31/9999 | The Hierarchy ID CFZA was successfully created notification appears. The Manage Global Hierarchies view displays. |  |
| 7 | Open Details | Double-click the new hierarchy on the Hierarchy List. | A CFZA - Financial Statement Version details view displays. |  |
| 8 | Activate | Choose Activate. | The CFZA hierarchy is activated. |  |

#### Setting Up Your Statutory Cash Flow Report for South Africa

Purpose

In this activity, you set up the parameters for the statutory reports.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Set Local Version | Choose Set Local Version.On the Set Local Version dialog box, select South Africa from the dropdown and choose Set Local Version. | The local version is set to South Africa. |  |
| 4 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 5 | Search Criteria | Make the following entries:Application Area: FinanceSub Application Area: Statutory ReportingOn the Configuration Items list, select the row of the Item Name: Basic setting. | The Configure Your Solution - Cross Country item details view is displayed. |  |
| 6 | Configure | On the Configuration Steps list, Setting Up Your Statutory Reporting, choose Configure. | The Change View "Define Compliance Reporting Entities": Overview view is displayed. |  |
| 7 | Assign | On the Rep Entity column, select RZA_RP_ENT.In the Dialog Structure column, choose Assign Report Categories to Reporting Entity.In the results that display, select the following:Report Category ID: RZA_CASHFLOW | The Report Category ID can be selected. |  |
| 8 | Select Parameters | From the left column, choose Enter Parameters Specific to Report Category. | The parameters list displays to the right of the view. |  |
| 9 | Enter and Save | In the Parameter Name list, locate G_FIN_STMNT_HIER_ID and enter CFZA as the Parameter Value. Locate G_LEDGER and make the following entry:Parameter Value: 0LChoose Save. | The Parameter Values are saved. The parameter value CFZA is assigned to parameter name: G_FIN_STMNT_HIER_ID. |  |

SAP Central Business Configuration:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic setting | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Basic setting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Cross Country item details view is displayed. |  |
| 3 | Configure | On the Configuration Steps list, Setting Up Your Statutory Reporting, choose Configure. | The Change View "Define Compliance Reporting Entities": Overview view is displayed. |  |
| 4 | Assign | On the Rep Entity column, select RZA_RP_EN.In the Dialog Structure column, choose Assign Report Categories to Reporting Entity.In the results that display, select the following:Report Category ID: RZA_CASHFLOW | The Report Category ID can be selected. |  |
| 5 | Select Parameters | From the left column, choose Enter Parameters Specific to Report Category. | The parameters list displays to the right of the view. |  |
| 6 | Enter and Save | In the Parameter Name list, locate G_FIN_STMNT_HIER_ID and enter CFZA as the Parameter Value. Locate G_LEDGER and make the following entry:Parameter Value: 0LChoose Save. | The parameter values are saved. The parameter value CFZA is assigned to parameter name: G_FIN_STMNT_HIER_ID. |  |

#### Class Handling for South Africa AP Analytics

##### Check Classes for BBBEE Vendor Report

Purpose

In this activity, you check classes for BBBEE vendor report.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. |  |  |
| 2 | Access the App Manage Classes | Open App Manage Classes (CL02). | The Class screen is displayed. |  |
| 3 | Enter Class and Class Type | Enter Class BBBEE and Class Type 010 Vendor. | The Basic Data screen is displayed. |  |
| 4 | Display Characteristics | Choose Char. tab. | A list of characteristics of class BBBEE is displayed. |  |
| 5 | Exit the App Manage Classes | Choose Exit to return to the home page. | The SAP Home screen is displayed. |  |
| 6 | Open the App Manage Characteristics | Open App Manage Characteristics (CT04). | The Characteristics screen is displayed. |  |
| 7 | Search Characteristics | Choose input help of Characteristic field and enter BBBEE* as search criteria. | A list of Characteristics for BBBEE reports is displayed. |  |
| 8 | Display Characteristics | Choose BBBEE_BLACK_OWNERSHIP, for instance. | The Basic Data screen of the characteristic is displayed. |  |
| 9 | Display Charactersistics Values | Choose Values tab. | Characteristics Values are displayed. |  |

##### Assignment of BBBEE Classes to Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage assignment of BBBEE classes to vendor.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Product Configuration Modeler. |  |  |
| 2 | Access the SAP Fiori App | Open App Manage Class Assignments (CL24N). | The Assign Objects/Classes to Class screen is displayed. |  |
| 3 | Enter Class and Class Type | Enter Class BBBEE and Class Type 010 Vendor. | The Change View "Define Compliance Reporting Entities": Overview view is displayed. |  |
| 4 | Check Available Assignments | Choose Display all assignments to check whether vendors have been assigned to BBBEE class already.In the Dialog Structure column, choose Assign Report Categories to Reporting Entity.In the displayed results, select the following:Report Category ID: RZA_CASHFLOW | A list of vendors already assigned to class BBBEE is displayed. |  |
| 5 | Add Vendor Relevant for BBBEE Reporting | Choose Change all assignments.Choose More/Edit/New assignments.Choose Vendor.Enter list of vendors (e.g.: 64300001 and 64300002) and set status to Released. | The vendor and status list are displayed on the screen. |  |
| 6 | Save and Display All Assignments | First choose Save, then Overview, and at last choose Display all assignments. | The full list of vendors assigned to class BBBEE is displayed. |  |

##### Maintain Business Partner Master Data BBBEE Class Values For Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain Business Partner master data BBBEE class values for vendor.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Vendor | Enter Vendor 64300001. | The Change View "Define Compliance Reporting Entities": Overview view is displayed. |  |
| 4 | Choose BP Role | Choose Supplier (Fin.Accounting) (defined). | The supplier role screen is displayed. |  |
| 5 | Go to Classification Screen | Choose Menu > Extras > Classification . | The Change Organization: Classification screen is displayed on the screen.Assignment of class BBBEE is displayed.Assignment of the following characteristics values are displayed:BBBEE Recognition LevelBBBEE Level Adjustment FactorBBBEE Expiry DateBBBEE Turover LevelBBBEE Black Ownership > 50%BBBEE Black Women Ownership >BBBEE Empowering SupplierBBBEE Enterprise Development |  |
| 6 | Assign Characteristics Values and Save | Choose values for characteristics from input help.Choose More > Assignment > Exit .Choose Save. | The full list of vendors assigned to class BBBEE appears. |  |

#### Assign Company Code

Purpose

In this activity, you assign a company code to your ACR reports.

Prerequisite

Company code has already been created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Statutory Reporting

1. For the row with Item Name of Basic Settings, choose Details (>).
2. For the Setting Up Your Compliance Reporting row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setting Up Your Compliance Reporting.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: RZA_RP_ENT |  |  |
| 2 | Validity | In the Dialog Structure pane, double-click Set Validity of Organization Unit and choose a Valid From date.Note If no date exists, a new Valid From date can be entered by choosing New Entries and entering the date. | The Change View "Set Validity of Organization Unit ": Overview view is displayed. |  |
| 3 | Assign | In the Dialog Structure pane, double-click Assign Org. Units to a Reporting Entity and enter the following:Organization Unit: COMPANYCODEVALUE: <your COMPANY CODE>Leading: Selected (there can only be one leading company code) |  |  |
| 4 | Save | Choose Save and then Exit. | The company code is assigned and saved. |  |

#### Activate Registration for Indirect Taxation Abroad

Purpose

For global Advance Compliance Reporting scope items (such as Compliance Formats – Support Preparation for Belgium (5P9) or Compliance Formats – Support Preparation for Germany (5O6)), you must activate Registration for Indirect Taxation Abroad (RITA).

If the Compliance Formats – Support Preparation (1J2) scope item is activated for your country and is to be used in conjunction with another Advance Compliance Reporting scope item (such as (such as Compliance Formats – Support Preparation for Belgium (5P9) or Compliance Formats – Support Preparation for Germany (5O6)), the activation of RITA is required. Activating reports from different countries requires RITA functionality to allow them to work properly.

The activation of RITA is only optional if the Compliance Formats – Support Preparation (1J2) scope item is activated and used alone, not in conjucntion with another Advance Compliance Reporting scope item.

The following reports are RITA-enabled:

- EC Sales List
- Advance VAT Return

##### Activate Registration for Indirect Taxation Abroad (Optional)

Purpose

Companies that operate in multiple countries or regions need to comply with the tax and reporting regulations of each country/region they do business in. In some cases, you can register legal entities for indirect taxation abroad without having to create a separate company code for each country or region. Registration for Indirect Taxation Abroad (RITA) lets you maintain a tax registration country or region that's different from your company code’s country or region. This registration helps you link taxable transactions in foreign countries or regions for indirect tax reporting (like the EU Tax Return, Intrastat, or EC Sales List) and tax payments.

Currently, you can use RITA in Germany, Austria, Czechia, Belgium, Finland, France, the Netherlands, Ireland, Spain, Italy, the United Kingdom, South Africa, Switzerland, and Sweden. For example, companies in Germany can register the Netherlands as a tax registration country/region, and vice versa.

|  |
| --- |
| Note You can't use RITA where, for instance, you maintain an establishment in a foreign country/region and are required to create a company code for that permanent presence. You also can't use it in any instance when you're required to create a company code. Neither of these cautions refer to the default company code when you activate SAP S/4HANA Cloud Public Edition. It's your responsibility to verify whether your business activities are considered as a permanent establishment under the law of the respective country/region. In this case, a company code would be required. |

Procedure

A full discussion of setting up RITA is outside of the scope of this test script. For more information, see the topics under [Registration for Indirect Taxation Abroad (RITA) on the SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/baee0f4d00de4f1693be3f57fd49685a.html).

## Overview Table

The scope items consist of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: South Africa

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Run Statutory Reports - South Africa AP Analytics](#unique_16) [page ] 18 | Accounts Payable Manager for South Africa | Run Statutory Reports - South Africa AP Analytics (F1515_ZA_1) | Report is generated and downloaded. |
| [Run Statutory Reports - VAT201 - Declaration](#unique_17) [page ] 19 | Accounts Payable Manager for South Africa | Run Statutory Reports - South Africa GL Reporting (F1515_ZA_2) | The report is generated and downloaded. |
| [Run Statutory Reports - VAT 201 - Supporting Data File](#unique_18) [page ] 21 | Accounts Payable Manager for South Africa | Run Statutory Reports - South Africa GL Reporting (F1515_ZA_2) | The report is generated and downloaded. |
| [Run Statutory Reports - South Africa Cash Flow Indirect Method Reporting](#unique_19) [page ] 24 | General Ledger Accountant for South Africa | Run Statutory Reports (F1515) | The report is generated and downloaded. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Statutory Reports - South Africa AP Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager for South Africa . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - South Africa AP Analytics (F1515_ZA_1). | The Run Statutory Reports - South Africa AP Analytics (F1515_ZA_1) view displays. |  |
| 3 | Enter Criteria | Make the following entries:Submission Due Date: <Date range>Report Name: RZA_BBBEE_CLFN | Report details entered. |  |
| 4 | Display Statutory Report | Select a task and choose Go. | A Statutory Reports table displays. |  |
| 5 | Select Report to Submit | Select the report to submit. | The relevant statutory report is displayed for selection. |  |
| 6 | New Run | Choose the New Run button at bottom of the view. | A New Run starts. |  |
| 7 | Enter Details | Make the following entries:Company Code: 6410Posting Date: <Date range> | Company code entries made. |  |
| 8 | Generate Report | Choose Run from the bottom of the view. | A new report is generates. |  |
| 9 | Select Report | If the new report status is still In process, choose the Refresh icon at the top of the view. Select the generated report. | Correct output is generated. |  |
| 10 | Review Data | Review data for all documents during posting period by different categories, including company code, document number, and business partner. | Data reviewed for all documents by different categories. |  |
| 11 | Select Link | Select BBBEE Supplier Classification details link. | The document displays. |  |
| 12 | Select Information | Select the Supplier Characteristics Details information. | The proposed generated supplier characteristic details display. |  |
| 13 | Download | Select Export to MS Excel. | The document downloads.. |  |

### Run Statutory Reports - VAT201 - Declaration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for South Africa . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - South Africa GL Reporting (F1515_ZA_2). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: RZA_VAT_DCL | A Statutory Reports table displays. |  |
| 4 | Select Report to Submit | Select a period to submit:South Africa VAT summary report with reported Item log Information | The relevant statutory report is displayed for selection. |  |
| 5 | New Run | Choose the New Run button. | A selection criteria dialog box displays. |  |
| 6 | Enter Details | Make or verify the following entries and choose Run:Company Code: 6410Reporting Date: <Date range>Run Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Report started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 7 | Select Report | If the new report status is still In process, choose Refresh. When the status is Generated Successfully, select the generated report. | The report details view displays. |  |
| 8 | Review Data | Review data for all documents during posting period by different categories, including company code, document number, and business partner. | Data reviewed for all documents by different categories. |  |
| 9 | Preview | Return to the South Africa VAT Declaration view. Under the Legal Reporting section, select the document name VAT BOX SUMMARY. | The preview documents display in a new view. |  |
| 10 | Review Preview Data | From the generated preview, expand the headings to review data. | The detailed reporting view is available. |  |
| 11 | Return | Once you consider the file to by finalized, return to the South Africa VAT Declaration report view. | The South Africa VAT Declaration view displays. |  |
| 12 | Download | Select the checkbox of the document name and choose Download. | The PDF file downloads. |  |
| 13 | Update Status | Choose the Update Submission Status button.A Confirmation Required dialog box displays a This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Authority "? notification. Choose Yes. | Status of Report Run Updated notification displays. Generation is finalized for the period and on the initial report view, under Submitted, the Report Run Status is Submission Accepted by Authority . |  |

### Run Statutory Reports - VAT 201 - Supporting Data File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for South Africa . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - South Africa GL Reporting (F1515_ZA_2). |  |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: RZA_VAT_DCL | A Statutory Reports table displays. |  |
| 4 | Select Report to Submit | Select a period to submit:South Africa VAT summary report with reported Item log Information | The relevant statutory report is displayed for selection. |  |
| 5 | New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 6 | Enter Details | Make or verify the following entries and choose Run:Company Code: 6410Reporting Date: <Date range>Run Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Report started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 7 | Select Report | If the new report status is still In process, choose Refresh. When the status is Generated Successfully, select the generated report. | The report details view displays. |  |
| 8 | Review Data | Review data for all documents during posting period by different categories, including company code, document number, and business partner. | Data reviewed for all documents by different categories. |  |
| 9 | Preview | Return to the South Africa VAT Declaration view. Under the Legal Reporting section, select the document name VAT BOX SUMMARY. | The preview documents display in a new view. |  |
| 10 | Review Preview Data | From the generated preview, expand the headings to review data. | The detailed reporting view is available. |  |
| 11 | Return | Once you consider the file to by finalized, return to the South Africa VAT Declaration report view. | The South Africa VAT Declaration view displays. |  |
| 12 | Download | Select the checkbox of the document name and choose Download. | The PDF file downloads. |  |
| 13 | Update Status | Choose the Update Submission Status button.A Confirmation Required dialog box displays a This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Authority "? notification. Choose Yes. | Status of Report Run Updated notification displays. Generation is finalized for the period and on the initial report view, under Submitted, the Report Run Status is Submission Accepted by Authority . |  |
| 14 | Start New Phase | Return to Activity screen, after setting all three activities (Manage Tax Items, South Africa VAT summary report with reported Item log Information, and Post Tax Payable) as Completed. Choose Start New Phase. | An option to select type of New Phase is displayed. |  |
| 15 | Select Due Date for New Clarification Phase | Enter a Due Date. | The activity South Africa Line Item Report appears on the Clarification tab. |  |
| 16 | New Run | Choose New Run. You cannot change selection parameters on this screen since it is a clarification phase.Choose Run. | A Report started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 17 | Select Report | If the new report status is still In process, choose Refresh. When the status is Generated Successfully, select the generated report. | The report details view displays. |  |
| 18 | Review Data | Review data for all documents during posting period by different categories, including company code, document number, and business partner. | Data reviewed for all documents by different categories. |  |
| 19 | Preview | Return to the South Africa VAT Declaration view. Under the Legal Reporting section, select the document name RZA_LINE_ITEM_DOCUMENT. | The preview documents display in a new view. |  |
| 20 | Review Preview Data | From the generated preview, expand the headings to review data. | The detailed reporting view is available. |  |
| 21 | Download | Choose the Excel icon to download the spreadsheet. | A detailed Excel file is downloaded. |  |
| 22 | Update Status | Choose the Update Submission Status button.A Confirmation Required dialog box displays a This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Authority "? notification. Choose Yes. | Status of Report Run Updated notification displays. Generation is finalized for the period and on the initial report view, under Submitted, the Report Run Status is Submission Accepted by Authority . |  |

### Run Statutory Reports - South Africa Cash Flow Indirect Method Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you generate the cash flow indirect method report in PDF format. You submit the form as a statutory report.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for South Africa . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). |  |  |
| 3 | Select Report | Make the following entries and choose Go:Reporting Entity Name: RZA_RP_ENTReport Name: RZA_CASHFLOW | Items display in the report result list by period, according to configuration.If the system has never added any ad-hoc reporting tasks, there should be no task in the report list. Otherwise you can view all the previously added ad-hoc reporting tasks in this list. |  |
| 4 | Add | Choose Create in the report list to add Ad-hoc reporting task.Enter the following parameters:Due date: for example, 04/15/2020Reporting period: for example, 01/01/2020 – 03/31/2020Reporting Year: for example, 2020 | A new Cash Flow report is generated and waiting to be updated (run). |  |
| 5 | New Run | Choose the statutory report for the period of reporting and choose New Run at the bottom of the view. | A new run starts and a selection criteria dialog box displays |  |
| 6 | Run Report | Make or verify the following entries and choose Run:Company Code: 6410Reporting Date: <Date range>, for example, 1/1/2020 to 03/31/2020Note If you are an authorized user, to display an Individual Number, select Display Individual Number.Run Options: Use the default settings.Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your prefer to set up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Run Started notification appears and a new report displays in the Generated section of the report details view. |  |
| 7 | Refresh Status | If the new report shows an In process status, choose Refresh. | The Report Run Status is Generated Successfully.Cash Flow Statement Indirect Method is now generated. |  |
| 8 | Select Report | Select the newly generated report. | A report details view displays. |  |
| 9 | Open Report | From the Legal Reporting section, on the row of the document name, click on the document name to display the detail of the report. | A Cash flow view displays. Preview the data in the ALV list on the Legal Reporting tab. |  |
| 10 | Download | Select Cashflow Statement Indirect Method and choose Download. | The report is downloaded. |  |
| 11 | Submission | Select report from Generated tab and click on Update Submission Status button.Choose the appropriate status.Click button Submitted to Authority – confirm the pop-up messageClick Update Submission Status button and select option Submission Accepted by Authority – confirm the pop-up message. | In the Submitted Tab, the status of report item change to Submitted to Authority. At the head of the page, Due date Status and Run Status have been changed Submitted to Authority .In the Submitted Tab, the status of report item change to Submission Accepted by Authority.At the head of the page, Due date Status has been changed to Submission Accepted by Authority and Run Status has been changed to Completed. |  |

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
> Flagged while digesting this document, not verified: The Overview Table lists Accounts Payable Manager for South Africa as the business role for the VAT201 Declaration and VAT 201 Supporting Data File steps, but the Test Procedures for both log on as General Ledger Accountant for South Africa.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-south-africa-5z0-113]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z5_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 47,356 chars in the whole document
