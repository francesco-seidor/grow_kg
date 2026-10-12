---
id: 04-tax-and-statutory-reporting/sale-of-services-2eq-ae-test-script-sap-s-4hana-cloud-public-edition-8
title: Sale of Services (2EQ_AE) Test Script - SAP S/4HANA Cloud Public Edition (2EQ_S4CLD2608_BPD_EN_AE)
description: "SAP test script for scope item 2EQ_AE Sale of Services (UAE): prerequisites, PEPPOL e-invoicing setup, sales order to billing, eDocument Cockpit, billing jobs."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/peppol-e-invoicing, topic/sale-of-services]
aliases: [2EQ_S4CLD2608_BPD_EN_AE]
keywords: [PEPPOL Electronic Invoicing, sale of services, test script, electronic invoicing, peppol configuration, sales orders, billing documents, edocument cockpit, value mapping, credit management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-817
topic: 04-tax-and-statutory-reporting/peppol-e-invoicing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sale of Services (2EQ_AE) Test Script - SAP S/4HANA Cloud Public Edition (2EQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **PEPPOL Electronic Invoicing** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sale of Services (2EQ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sale of Services (2EQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849350)

[2 Prerequisites 4](#_Toc232849351)

[2.1 System Access 4](#_Toc232849352)

[2.2 Roles 4](#_Toc232849353)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849354)

[2.4 Preliminary Steps 6](#_Toc232849355)

[2.4.1 Create Condition Records (Optional) 6](#_Toc232849356)

[2.4.2 Preliminary Steps for Electronic Invoicing (PEPPOL) 6](#_Toc232849357)

[2.4.2.1 Define Identification Types for Business Partners 7](#_Toc232849358)

[2.4.2.2 Maintain Company Code Data (FINSC_T001Z_N) 9](#_Toc232849359)

[2.4.2.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552) 11](#_Toc232849360)

[2.4.2.4 Maintain Business Partner Master Data 13](#_Toc232849361)

[2.4.2.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301) 14](#_Toc232849362)

[2.4.2.6 Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304) 16](#_Toc232849363)

[2.4.3 Optional Steps for Electronic Invoicing (PEPPOL) 18](#_Toc232849364)

[2.4.3.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 18](#_Toc232849365)

[2.4.3.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 19](#_Toc232849366)

[3 Overview Table 24](#_Toc232849367)

[4 Test Procedures 25](#_Toc232849368)

[4.1 Credit Management - Set Credit Limit (Optional) 25](#_Toc232849369)

[4.2 Sales Quotation (Optional) 26](#_Toc232849370)

[4.3 Sales Contract (Optional) 26](#_Toc232849371)

[4.4 Create Sales Order 27](#_Toc232849372)

[4.5 Process Sales Order Approval (Optional) 29](#_Toc232849373)

[4.6 Credit Management - Review Blocked Sales Orders (Optional) 29](#_Toc232849374)

[4.7 Create Billing Document 30](#_Toc232849375)

[4.8 eDocument Cockpit 32](#_Toc232849376)

[4.9 Add Text in Billing Document (Optional) 34](#_Toc232849377)

[5 Appendix 36](#_Toc232849378)

[5.1 Process Integration 36](#_Toc232849379)

[5.1.1 Succeeding Processes 36](#_Toc232849380)

[5.2 Limitations 36](#_Toc232849381)

[5.3 Scheduling Job Creation (optional) 37](#_Toc232849382)

[5.3.1 Scheduling Job for Billing Creation (optional) 37](#_Toc232849383)

[5.3.2 Scheduling Job for Billing Release (optional) 38](#_Toc232849384)

[5.3.3 Scheduling Job for Billing Output (optional) 39](#_Toc232849385)

## Purpose

Overview

A service product is used in the sales order. It allows the sales of services without delivery and direct (order-related) billing.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Credit Controller | SAP_BR_CREDIT_CONTROLLER | Credit Management | SAP_BR_CREDIT_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | SM0001 | Service Material 01 | If you use ANC procedure to extend the new country content, you need to manually extend the materials according to Master Data Script 31X |
| Sold-to party | 33100003 33100005 | Domestic UAE Customer 3Domestic UAE Customer 5 | You can test the scope item using another domestic customer.33100005 is for credit management. |
| Payer | 33100003 33100005 | Customer domestic 03Customer domestic 05 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| 31X | Create Product Master of type "Service Product" - MDS |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

#### Preliminary Steps for Electronic Invoicing (PEPPOL)

These settings are optional, but necessary if you want to test eDocuments Cockpit for PEPPOL.

Purpose

To be able to run the step e-Document Cockpit for PEPPOL United Arab Emirates, the following prerequisites should be met:

- Define Identification Types for Business Partners (SSCUI 103654)
- Maintain Additional Parameters (FINSC_T001Z_N)
- Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552)
- Maintain Business Partner Master Data
- Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301)
- Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304)

##### Define Identification Types for Business Partners

Purpose

Define identification type (ID Type) for the unique identification number your business partner received from the service provider.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Change Local Version | Click Set Local Version and switch to Malysia in view of Manage Your Solution. | Change local version as Malaysia. |  |
| 4 | Open Configure Your Solution | Click and choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 5 | Search Relevant Activities | Enter the following filters:Application Area: Database and Data ManagementSub Application Area: Business PartnerIn the items table, select the item with item name: Define Identification Types. | The result displays. |  |
| 6 | Navigate to Define Identification Types | Select the searched item and into view of Configure Your Solution - Business Partner.Select Define Identification Types in right section under tab of Configuration Steps.Click Configure and go to the view of Define Identification Types: Change. | The result displays. |  |
| 7 | Maintain Settings | Choose New Entries and get into the view of New Entries: Details of Added Entries.Make the following entries and save:ID Type: AELRIDDescription: Legal Registration IndentifierID Category: AELRIDOrganization: XPersons: XGroups: XID Type: AELRACDescription: Legal Registration Auth./Ctry.ID Category: AELRACOrganization: XPersons: XGroups: XChoose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Identification Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Define Identification Types screen displays. |  |
| 3 | Maintain Settings | Choose New Entries and get into the view of New Entries: Details of Added Entries.Make the following entries and save:ID Type: AELRIDDescription: Legal Registration IndentifierID Category: AELRIDOrganization: XPersons: XGroups: XID Type: AELRACDescription: Legal Registration Auth./Ctry.ID Category: AELRACOrganization: XPersons: XGroups: XChoose Save. |  |  |

##### Maintain Company Code Data (FINSC_T001Z_N)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add tax information to company code by configuration step.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Set local Version | Choose Set Local Version.In the dropdown list, choose Malsysia, and then choose Set Local Version. |  |  |
| 5 | Choose Application Area | Make the following entries:Application Area: FinanceSub Application Area: Master and Organizational Data |  |  |
| 6 | Go to Configuration Details | On the Configure Your Solution screen, search for the following configuration step: Maintain Additional Parameters. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Configure Your Solution - Maintain Additional Parameters screen，go to the configuration step Maintain Additional Parameters and choose Configure. | The Maintain Additional Parameters screen is displayed. |  |
| 7 | Create Additional Parameters | Create the following entries:Company Code: 3310Maintain AE tax numbers for this business partner:Parameter Type: AELRID (Legal Registration Identifier)Parameter Value: <123456>Parameter Type: AELRAC (Legal Registration Auth./Ctry.)Parameter Value: <Ministry>Parameter Type: SAPAE1 (Tax Identification Number)Parameter Value: <1234567890>Choose Save. | The new Additional Parameters are created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Additional Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configuration Your Solution- Maintain Additional Parameters screen is displayed. |  |
| 3 | Create Additional Parameters | Create the following entries:Company Code: 3310Maintain AE tax numbers for this business partner:Parameter Type: AELRID (Legal Registration Identifier)Parameter Value: <123456>Parameter Type: AELRAC (Legal Registration Auth./Ctry.)Parameter Value: <Ministry>Parameter Type: SAPAE1 (Tax Identification Number)Parameter Value: <1234567890>Choose Save. | The new Additional Parameters are created. |  |

##### Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to define process communication through Cloud services by configuration step. In this activity, you define, for a given company code, if an eDocument process integrates with SAP Document and Reporting Compliance, Cloud edition (using the standard integration or other types of integration) to exchange electronic documents with external communication parties.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Set Local Version | Choose Set Local Version.In the dropdown list, Choose United Arab Emirates, and then choose Set Local Version. |  |  |
| 5 | Choose Application Area | Make the following entries:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance |  |  |
| 6 | Go to Configuration Details | On the Configure Your Solution screen, search for the following configuration step: Define Process Communication Through Cloud Services. Choose Go.On the Configure Your Solution - Define Process Communication Through Cloud Services screen, go to the configuration step Define Process Communication Through Cloud Services and choose Configure. | The Define Process Communication Through Cloud Services screen is displayed. |  |
| 7 | Create Process Communication Through Cloud Services | Create the following entries:Company Code: 3310Maintain the entries as following:BUKRS: 3310Process: AEINVSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosBUKRS: 3310Process: AEINVINSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosChoose Save. | The new Process Communication Through Cloud Services is created. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Process Communication Through Cloud Services.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configuration Your Solution- Define Process Communication Through Cloud Services screen is displayed. |  |
| 3 | Create Process Communication Through Cloud Services | Create the following entries:Company Code: 3310Maintain the entries as following:BUKRS: 3310Process: AEINVSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosBUKRS: 3310Process: AEINVINSERVICE: X Cloud Edition: Peppol Exchange or Country/Region ScenariosChoose Save. | The new Process Communication Through Cloud Services is created. |  |

##### Maintain Business Partner Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you add tax information to Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data Test. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Business Partner: XXXXXXXX |  |  |
| 4 | Enter Business Partner | Hover over the text and choose the Switch Between Display and Change (F6) button to switch to change mode. |  |  |
| 5 | Change BP Role | In the Change in BP role field, choose the following value:Customer (Fin.Accouting) (FLCU00) |  |  |
| 6 | Maintain United Arab Emirates Tax Numbers | On the Identification tab, on the Tax Numbers screen, maintain the following data for this business partner:Category: AE0Tax Number Long: <123456789012345>Category: AE1Tax Number Long: <1234567890> |  |  |
| 6 | Save Your Data | Save your entries. |  |  |

##### Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301)

Purpose

In this activity, you define the party identification types that business partners use in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Business Partner | For the Assign Party ID Types to Business Partner row, choose Configure. | The Assign Party ID Types to Business Partner screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Type: C CustomerParty ID type: AE:TINE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Business Partner activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Business Partner screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Partner ID: <business partner ID>Type: C CustomerParty ID type: AE:TINE-mail: <select this only if the customer cannot receive electronic invoices> |  |  |

##### Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304)

Purpose

In this activity, you maintain the party identification types (party ID type) that your company uses in the exchange channels in the PEPPOL network.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Configure Your Solution | Choose Configure Your Solution.In the Set Country Version dialog box, select the country from the dropdown menu and choose Set Country Version. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and choose Enter:Application Area: Application Platform and InfrastructureSub Application Area: Legal Compliance | All entries display in Configuration Items section. |  |
| 5 | Find the Entry | Find the entry with Settings for Peppol item name and choose arrow at the item end. | The Configure Your Solution - Settings for Peppol screen displays. |  |
| 6 | Navigate to Assign Party ID Types to Companies | For the Assign Party ID Types to Companies row, choose Configure. | The Assign Party ID Types to Companies screen displays. |  |
| 7 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 3310Party ID type: AE:TIN |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Business Processes Configuration | Go to the Business Processes Configuration app.Search for the Assign Party ID Types to Companies activity and choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Assign Party ID Types to Companies screen displays. |  |
| 3 | Maintain Settings | Choose New Entries.Make the following entries and choose Save:Company code: 3310Party ID type: AE:TIN |  |  |

#### Optional Steps for Electronic Invoicing (PEPPOL)

##### Business Partner Master Data Maintenance for Electronic Invoicing (Optional)

Purpose

To run the steps in electronic invoicing, you must maintain the identification number and tax number category for customer master data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Master Data Specialist - Business Partner Data Test. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Business Partner | Make the following entry and choose Enter:Business Partner: for example, 33100003 | The view of Display Organization displays. |  |
| 4 | Switch to Change Mode | On the Display Organization: XXXXXXXX screen, choose Switch Between Display and Change. |  |  |
| 5 | Go to Identification Tab | On the Change Organization: XXXXXXXX screen, choose Business Partner (Gen.) in the Change in BP Role field.Choose Identification tab . |  |  |
| 6 | Maintain ID Type and Tax numbers for Business Partner | On the Identification tab, in the Identification Numbers screen, maintain Malaysia participant ID for this Business Partner:ID Type: AELRIDIdentification Number: for example, <123456> |  |  |
| 7 | Save Your Data | Choose Save. |  |  |

##### Value Mapping Maintenance for Electronic Invoicing (Optional)

Purpose

To run the step in electronic invoicing, you must maintain the value mapping for eDocument UBL.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Network Integration. | The SAP Fiori launchpad dis-plays. |  |
| 2 | Access the App | Open Configure Value Mapping (/AIF/VMAP_CONF). | The Configure Value Mapping view is displayed. |  |
| 3 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_ALLOW_COND_TYPE |  |  |
| 4 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 5 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Reason Code: <number of code>, for example, 95Reason Description: <description of code>, for example, DiscountCondition Type: <value>, for example, YK07Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 6 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value Mapping screen displays. |  |
| 7 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_CHARGE_COND_TYPE |  |  |
| 8 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 9 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Reason Code: <number of code>, for example, RVReason Description: <description of code>, for example, LoadingCondition Type: <value>, for example, DRV1Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 10 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value Mapping screen displays. |  |
| 11 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_DISTR_CHANNEL |  |  |
| 12 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 13 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Distribution Channel: <number of code>, for example, 60Sales Org.: <value>, for example, 3310Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 14 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 15 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_LEGAL_FORM |  |  |
| 16 | Switch to Change Mode | On the Display Value Mapping screen, choose Switch Between Display and Change. |  |  |
| 17 | Maintain Value Mapping | On the Change Value Mapping screen, click Append, choose append number.Maintain the following detail:Invoice Code: <number of code>, for example, 1Legal Form.: <value>, for example, FZMaintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 18 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 19 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_PAYM_MEANS_CODE |  |  |
| 20 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 21 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <value 1>Payment Method: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 22 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 23 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_TAX_CATEGORY |  |  |
| 24 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 25 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Tax code: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 26 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 27 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_TAX_EXEMPT_CODE |  |  |
| 28 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 29 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Tax Code: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 30 | Back | Choose Back to go to the screen Configure Value Mapping. |  |  |
| 31 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_PROFIT_MARGIN_PP |  |  |
| 32 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 33 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Pricing Procedure: <value>Sales Org.: 3310Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. |  |  |
| 34 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 35 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_RVS_CHRG_MECH |  |  |
| 36 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 37 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <number of index>Material Group: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |
| 38 | Back | Choose Back to go to the screen Configure Value Mapping. | The Configure Value mapping screen displays. |  |
| 39 | Enter Namespace and Value Mapping | Make the following entry and choose Execute.Namespace: /EDUBLValue Mapping: AE_ITEM_CATEGORY_SD |  |  |
| 40 | Switch to Change Mode | On the Display Value mapping screen, choose Switch Between Display and Change. |  |  |
| 41 | Maintain Value Mapping | On the Change Value mapping screen, click Append, choose append number.Maintain the following details:Value: <yes/no>Item Category: <xxx>Maintain all value mappings in next line items.Choose Save after maintaining the necessary entries. | Value Mapping Data are saved. |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App | Expected Results |
| --- | --- | --- | --- |
| [Credit Management - Set Credit Limit (Optional)](#unique_17) [page ] 25 | Credit Controller | See scope item no. BD6 | Credit Limit for Customer 33100005 has been set. |
| [Sales Quotation (Optional)](#unique_18) [page ] 26 | Internal Sales Representative | See scope item no. BDG |  |
| [Create Sales Order](#unique_19) [page ] 27 | Internal Sales Representative | Manage Sales Orders - Version 2 (F3893) |  |
| [Process Sales Order Approval (Optional)](#unique_20) [page ] 29 |  |  |  |
| [Credit Management - Review Blocked Sales Orders (Optional)](#unique_21) [page ] 29 | Credit Controller | See scope item no. BD6 |  |
| [Create Billing Document](#unique_22) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori Launchpad using the respective user, for example, Internal Sales Representative.

- Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.

- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your Search Criteria and choose the business object type, e.g.: Sales orders from dropdown menu in first field, enter sales order number in second field and choose Search. The sales order is listed.

- Choose the sales order number link: the system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page, You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects: (Visible depending on the assigned role)

- Sales order

- Quotation

- Billing document

- Credit Memo

- Debit Memo

- Customer 360 Fact sheet

### Credit Management - Set Credit Limit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set a credit limit for the used customer.

Procedure

Complete all the activities described in Basic Credit Management (BD6) scope item.

### Sales Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you the process for a standard sales quotation.

Procedure

Complete all the activities described in Sales Quotation (BDG) scope item.

|  |
| --- |
| Note If you want to use the optional link between Sales Quotation (BDG) scope item and this one, make sure to use consistent master data, such as Business Partner for customer quotation and for customer sales order. |

### Sales Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This scope item describes the process for a standard sales Contract.

Procedure

Complete all the activities described in the test script of Sales Contract Management (I9I) scope item.

|  |
| --- |
| Note If you want to use the optional link between Sales Contract Management (I9I) and Sale of Services (2EQ) scope items, this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Create Sales Order | On Manage Sales Orders - Version 2 screen, choose Create. |  |  |
| 4 | Enter Data | On the Create Sales Order screen, make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. |  |  |
| 5 | Enter Order Details | On the New: Sales Order screen, make the following entriesSold-to Party: 33100003Ship-to Party: 33100003Customer Reference: <Reference>Cust. Ref. Date: <Date>Material number: SM0001Order Quantity:Note The item category can change to <Quantity>TADN manually if the item is free of charge for free of charge for service Material Sales Order.Note The item category can change to CTAD manually if the item is Downpayment of Service Material. |  |  |
| 6 | Save Document | Choose Create. Make a note of the sales order number: __________. | The order is saved and the order confirmation is printed out. |  |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go:Sales Order: <Sales Order Number> | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Orders xxx: Overview screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display PDF Document | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a fact sheet screen in Manage Sales Orders - Version 2 (F3893) app:On Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number, and choose More Links. |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the Sell from Stock (BD9) scope item.

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval described in the test script of Sell from Stock (BD9) scope item.

### Credit Management - Review Blocked Sales Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process shows you how to review sales orders that might have been blocked due to the credit limit check.

Procedure

Complete all the activities described in Basic Credit Management (BD6) scope item.

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar. Select the following settings and choose OK:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFFNote Please set point 5 as ON only if you want to create particial billing of delivered items. |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select item(s) for Billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Creating Billing Documents window displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID Sxxxxxxxx will be displayed. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________ | To access the accounting data, navigate to Process Flow and click Journal Entry and navigate to Display Journal Entries:Material: Services (SERV)Debited Accounts: 33100003 Rcvbls Domestic UAE Customer 3Credited Accounts: 41000000 Rev Domestic Prod22001000 Output tax accrueCost Element / CO Object: none |  |
| 8 | Access the App | Open Manage Billing Documents (F0797) | The Manage Billing Documents screen displays. |  |
| 9 | Search for Previous Billing Document | If your billing document number does not show up in the results area, use the Billing Document field to help search for the billing document created in previous step. | The billing document created in the previous step displays. |  |
| 10 | Display Billing Document | Select the billing document item and choose Display. | The Billing Document displays. |  |
| 11 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items.Note You may need to use the arrows to scroll to the end of the list to locate Output Items. | There is one entry in the item with BILLING_DOCUMENT output type. |  |
| 12 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 13 | Cancel Billing Document (Optional) | Select certain Billing document, and choose Cancel Billing Docs. | There is a log display: Billing Document Canceled. |  |
| 14 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments.Save your changes by pressing Save in the footer bar. |  |  |
| 15 | Update New Text (Optional) | In the Edit mode, add, delete and update the text.Save your changes by pressing Save in the footer bar. |  |  |

### eDocument Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you change or maintain the status of your eDocument.

|  |
| --- |
| Note Starting with the SAP S/4HANA Cloud 2208 release, if you are a new customer and want to enable advanced eDocument features such as eDocument Submit, Cancel and Reject, you must first activate the Document and Reporting Compliance features for your country/region. Otherwise, only Display mode is available. For more information, refer to Activate Document and Reporting Compliance Features in the Preliminary Steps section of the test script for scope item Document and Reporting Compliance (5XU). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open eDocument Cockpit (EDOC_COCKPIT). | The eDocument Cockpit view is displayed. |  |
| 3 | Select eInvoice Document | Make the following entries:Source Document: <Invoice number from prior steps>Note You can also search for your invoice. In the Results Overview section, expand your country/region to display your country's/region's eInvoice . | The eInvoice screen for your country/region displays. |  |
| 4 | Submit eInvoice | Select the row and choose Submit.Note The submission of the eDocument requires a connection to the SAP Cloud Platform. | The eDocument status updates with a Message Text: Action successfully executed: SUBMIT. |  |
| 5 | Review status | Review the eDocument status. The possible status of submitted eDocument:Accepted by receiving Access PointeDocument CreatedError at Sending Access PointSending RequestedReceived by Access PointError at Receiving Access Point |  |  |
| 6 | Display eDocument | Select the row for an eDocument with Accepted by receiving Access Point status.From dropdown for Display, select Display/Preview XML. | The eDocument in XML format is shown. |  |
| 7 | Display Source Document | Select the row of an eDocument and from the Go to dropdown, select Source Document. | A view displays of the original transaction that generated the eDocument (source document). |  |
| 8 | Back | Choose < (Back) to return to the previous view. |  |  |
| 9 | Review History of eDocument | From the Goto dropdown, select History to review the eDocument history. | The view displays the last process steps and statuses from selected eDocument. |  |
| 10 | Back | When completing your review, choose the Back button at the bottom of the view to return to the previous view. |  |  |
| 11 | Review Application Log | From the Goto dropdown, select Application Log.When there are no errors, a No Application Log found for the selected eDocument notification displays at the bottom of the view.If there are errors, an Application Log dialog box displays with information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 12 | Message Dashboard | Access Message Dashboard.If you encounter errors, a dialog box displays information about the error. Review the message and choose Continue to close the dialog box. |  |  |
| 13 | Cancel eDocument | To cancel an eDocument, choose the row of an eDocument with Created, Sending Requested, Error at Send. Acc. Point, or Val. Error at Rec. Acc. Point status.From the buttons above the list, from the More dropdown, select Cancel eDocument. | The status of eDocument changes to eDocument Cancelled and the status icon turns to green color |  |
| 14 | Delete eDocument | To delete an eDocument, choose a row from the list with a Created status.Mark the eDocument in status Created.From the buttons above the list, from the More dropdown, select Delete eDocument. | At the bottom of the view a Number of eDocuments that have been deleted: 1 notification displays. |  |

### Add Text in Billing Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to add a text in a billing document.

Procedure

Table 3: Add Text in Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Change Billing Documents (VF02). | The Change Billing Documents (VF02) screen displays. |  |
| 3 | Enter the Billing Number | On the Change Billing Documents (VF02) screen, enter the respective billing document number created in the previous step.Choose Enter. | The billing document displays. |  |
| 4 | Enter External Invoice Number and Date | Click the Display Header Details icon and then choose the Header Texts tab.On the left side, double-click the text type External Number of Invoice and enter your External Invoice Number. Repeat the same for External Date of Invoice and enter the date. | The relevant text is added. |  |
| 5 | Enter Invoice Revision Number and Date (Optional) | Click the Display Header Details icon and then choose the Header Texts tab.On the left side, double-click the text type Invoice Revision Number and enter your Invoice Revision Number. Repeat the same for Invoice Revision Date and enter the date. | The relevant text is added. |  |
| 6 | Save your changes | Save your changes by choosing Save in the footer bar | The billing document is saved. |  |

Table 4: Display Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Billing Documents (VF03). | The Display Billing Documents (VF03) screen displays. |  |
| 3 | Enter the Billing Number | On the Display Billing Documents (VF03) screen, enter the respective billing document number and choose Continue. | The billing document displays. |  |
| 4 | Check Output Condition | On the Invoice xxxxxxxx (F2) Display: Overview of Billing Items screen, choose More > Goto > Header > Output |  |  |
| 5 | Display PDF Document | On the Invoice xxxxxxxx (F2) Display: Output screen, select output item with Output Type BILLING_DOCUMENT and Form Template SDBIL_INVOICE_RU. Choose Display PDF Document. | Preview for PDF document displays. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting.Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SD Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Limitations

Please consider that Sale of Services (2EQ) is not covering the processing of a service order until confirmation. This is addressed by Service Order Management (41Z).

### Scheduling Job Creation (optional)

#### Scheduling Job for Billing Creation (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define the schedule background job for creation billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs displays. The app shall be started with the history of application jobs. |  |
| 3. | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4. | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Billing Creation Job Log | In screen Application Jobs, after status of job item turn to finish, choose Job Log.Note Choose Magnifier, the job list refreshes. | Screen goes to log details. |  |

#### Scheduling Job for Billing Release (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define the schedule background job for release billing documents to accounting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Schedule Billing Output. | The Application Jobs displays. The app shall be started with the history of application jobs. |  |
| 3. | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should be default as Schedule Billing Release. |  |
| 4. | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5. | Schedule | Choose Schedule. | A billing release job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Billing Release Job Log | In screen Application Jobs, after job item’s status turn to Finish, choose Job Log.Note Choose Magnifier, the job list will refresh. | Screen goes to log details. |  |

#### Scheduling Job for Billing Output (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to define the schedule background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as aBilling Clerk | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs displays. The app shall be started with the history of application jobs. |  |
| 3. | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. Job Template should be default as Schedule Billing Output. |  |
| 4. | Job Parameters | Define scheduling options and parameter section for batch job if necessary, then choose Check. | The system displays the message Go Ahead and Schedule the Job. |  |
| 5. | Schedule | Choose Schedule. | A billing output job is scheduled. Screen back to Application Jobs. |  |
| 6. | Check Billing Output Job Log | In screen Application Jobs, after job item’s status turn to finish, choose Job Log.Note Click Magnifier, the job list will refresh | Screen goes to log details. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2EQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 63,407 chars in the whole document
