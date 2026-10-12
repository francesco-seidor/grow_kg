---
id: 04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257
title: "Test Script: Invoice Correction Process with Debit Memo (BDQ_AE) (BDQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item BDQ (UAE): debit memo request, billing, eDocument PEPPOL submission, plus prerequisites and job scheduling."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/peppol-e-invoicing, topic/debit-and-credit-memo-processing]
aliases: [BDQ_S4CLD2608_BPD_EN_AE]
keywords: [PEPPOL Electronic Invoicing, debit memo request, invoice correction, billing block, debit memo creation, edocument cockpit, electronic invoicing peppol, value mapping, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1257
topic: 04-tax-and-statutory-reporting/peppol-e-invoicing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Invoice Correction Process with Debit Memo (BDQ_AE) (BDQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **PEPPOL Electronic Invoicing** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Invoice Correction Process with Debit Memo (BDQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861348)

[2 Prerequisites 4](#_Toc232861349)

[2.1 System Access 4](#_Toc232861350)

[2.2 Roles 4](#_Toc232861351)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861352)

[2.4 Business Conditions 7](#_Toc232861353)

[2.5 Preliminary Steps 7](#_Toc232861354)

[2.5.1 Create Condition Records (Optional) 7](#_Toc232861355)

[2.5.2 Preliminary Steps for Electronic Invoicing (PEPPOL) 7](#_Toc232861356)

[2.5.2.1 Define Identification Types for Business Partners 8](#_Toc232861357)

[2.5.2.2 Maintain Company Code Data (FINSC_T001Z_N) 10](#_Toc232861358)

[2.5.2.3 Define Process Communication Through Cloud Services (EDOCOMPPROCCOMV) (SSCUI 105552) 12](#_Toc232861359)

[2.5.2.4 Maintain Business Partner Master Data 15](#_Toc232861360)

[2.5.2.5 Assign Party ID Types to Business Partner (EDOEUBUPAV) (SSCUI 103301) 16](#_Toc232861361)

[2.5.2.6 Assign Party ID Types to Companies (EDOEUCOMPV) (SSCUI 103304) 17](#_Toc232861362)

[2.5.3 Optional Steps for Electronic Invoicing (PEPPOL) 19](#_Toc232861363)

[2.5.3.1 Business Partner Master Data Maintenance for Electronic Invoicing (Optional) 19](#_Toc232861364)

[2.5.3.2 Value Mapping Maintenance for Electronic Invoicing (Optional) 20](#_Toc232861365)

[3 Overview Table 25](#_Toc232861366)

[4 Test Procedures 26](#_Toc232861367)

[4.1 Create Debit Memo Request 26](#_Toc232861368)

[4.2 Create Attachment for Sales Order (Optional) 29](#_Toc232861369)

[4.3 Remove Billing Block 30](#_Toc232861370)

[4.4 Create Debit Memo 30](#_Toc232861371)

[4.5 eDocument Cockpit 32](#_Toc232861372)

[4.6 Create Attachment for Billing (Optional) 34](#_Toc232861373)

[5 Appendix 36](#_Toc232861374)

[5.1 Process Integration 36](#_Toc232861375)

[5.1.1 Succeeding Processes 36](#_Toc232861376)

[5.2 Scheduling Job (alternative) 36](#_Toc232861377)

[5.2.1 Job Scheduling for Billing Creation (Alternative) 36](#_Toc232861378)

[5.2.2 Job Scheduling for Billing Release (Alternative) 37](#_Toc232861379)

[5.2.3 Job Scheduling for Billing Output (Alternative) 38](#_Toc232861380)

## Purpose

Overview

This scope item makes it possible to correct errors in pricing or sales tax calculations. If errors are detected, debit memo requests can be created with a correction of the amount to be debited. This is then placed on a billing block for review. The amount to be debited is calculated as the difference between the original amount and the correct amount. This is entered manually into the debit memo request. Once checked, it is released and becomes relevant for billing. The amount then appears in the billing due list. The debit memo can be created manually. Alternatively, the automatic periodic billing process creates a debit memo to be sent to the customer and posts a journal entry.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics. Check your SAP system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no batch | See section Business Conditions. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no batch | See section Business Conditions. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG/ BLH).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG/ BLH).See sections Business Conditions and Preliminary Steps. |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 | You can test the test script using another domestic customer. |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  | Shipping w/o LWM |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS– MDS |
| BND | Create Customer Master - MDS– MDS |

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock orBD3 - Sales Processing using Third-Party with Shipping Notification orBDK - Sales Processing Using Third-Party Without Shipping Notification orBDN - Sales of Non-Stock Item with Order-Specific Procurement | To run through this test script, you must already have sold some goods. This means you must have completed at least one of the test scripts |

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

The scope item Invoice Correction Process with Debit Memo (BDQ) consists of several choose the appropriate entity: process steps, reports, items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Debit Memo Request](#unique_18) [page ] 26 | Internal Sales Representative | Manage Debit Memo Requests - Version 2 (F1988A) | The Manage Debit Memo Requests screen displays. |
| [Create Attachment for Sales Order (Optional)](#unique_19) [page ] 29 | Internal Sales Representative | Manage Debit Memo Requests - Version 2 (F1988A) |  |
| [Remove Billing Block](#unique_20) [page ] 30 | Internal Sales Representative Billing Clerk | Manage Debit Memo Requests - Version 2 (F1988A) | The Release Sales Orders for Billing screen displays. |
| [Create Debit Memo](#unique_21) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_22) [page ] 34 | Billing Clerk | Display Billing Documents (VF03) | The Display Billing Documents (VF03) screen displays. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, You can search for objects such as: Apps, factsheets for business objects. From the data found, you can go directly to the respective apps and factsheets to display, edit the data or find related objects.

How to access and check a factsheet:

1. Log on to the SAP Fiori Launchpad using the respective user. For example: Internal Sales Representative.
2. Access the Enterprise Search Bar and choose the magnifying glass icon in the upper right corner. The Enterprise Search bar is displayed
3. Two filter fields display left to the search button. Enter your Search Criteria and choose the business object type, for example: Sales orders from drop-down menu in 1st field, enter sales order number in 2nd field and choose Search, The sales order is listed.
4. Choose the sales order number link. The system navigates to the factsheet screen and sales order related information is integrated and summarized in one Fiori page, You can get detailed data via choosing the corresponding links.

There are factsheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Create Debit Memo Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer receives a debit for incorrect charges. This process step shows you how to create a debit memo request.

|  |
| --- |
| Note Partner function Employee Responsible is prerequisite for credit memo request output. It can be added under Partners tab of credit memo request header. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests - Version 2 (F1988A) | The Manage Debit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Create Sales Document Screen | Choose Create with reference > From Invoice.Note When creating with reference, line items may need to be deleted. Select the items and choose Delete. |  |  |
| 4 | Enter Sales Document Type | Make the following entries:Debit Memo Request Type: Invoice Increase Req (CBII) |  |  |
| 5 | Choose the Reference Document | Enter the billing document number and choose Continue.Note If you are referencing a billing with related batch materials, after inputting the billing number, choose Item selection. Choose the item with open quantity and choose Copy. |  |  |
| 6 | Enter Order Reason | Enter an order reason (for example, Price Difference: Price was too low (200)). |  |  |
| 7 | Save Document | Choose Create.Note Please refer to chapter Process Credit Memo Request Approval (Optional) of scope item BKL for workflow related process. | The order is saved. A billing block is automatically assigned to the debit memo. |  |

|  |
| --- |
| Note The sales document is automatically created by copying lines from the original invoice. For every line in the invoice, two lines are created in the sales document:The first one cannot be modified and reports the total amount of the original invoice line with the same quantity and the opposite value sign.The second one can be modified and reports the total amount of the original invoice with same quantity and same value sign.When correcting the amount of an invoice line that was wrong in its original line, the user specifies the correct amount in the second of the two lines. In this way the total correction amount is correctly calculated as the difference between the first line (reporting the old wrong value) and the second line (reporting the new correct value). |

|  |
| --- |
| Note If you want to change the header text on the invoice that is created later in the process, choose the menu Goto > Header > Texts.Choose Sales Note for Customer, enter note text (for example, Reason for Debit Memo) and choose Save. If you want to change the item text, select an item and choose the menu.Goto > Item > Texts .Choose Material Sales Text, enter the item text, and save your entries. |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in the Manage Debit Memo Request app:On the Manage Debit Memo Request screen, enter search terms in filter bar and choose Go.In search result, select your debit memo request and choose sales order number. |

Print Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests (F1988). | The Manage Debit Memo Requests (F1988) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose GoFor example, enter Debit Memo Request number in field Debit Memo Request. | Debit Memo requests display in result list. |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Display Debit Memo Request. |  |  |
| 5 | Check Output Condition | On the Display Invoice Increase Req xxx: Overview screen, choose More Extras Output Header Edit. | The document prints. |  |
| 6 | Display Print Preview | On the Display Invoice Increase Req xxx: Output screen, select the line already created for the print output and choose Display PDF Document. | Choose your local destination and press Print. |  |

### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Debit Memo Requests - Version 2 (F1988A). | The Manage Debit Memo Requests - Version 2 screen displays. |  |
| 3 | Navigate to Display Debit Memo Request Screen | On the Manage Debit Memo Requests - Version 2 screen, enter the respective order number created in previous step in the Debit Memo Requests and choose Go.Choose the debit memo request line that displays. |  |  |
| 4 | Create Attachment for Sales Order | Choose Edit, then choose Attachments in the top right corner of the screen. | The Import File screen displays. |  |
| 5 | Import File | Choose Upload.On the Open view, choose local path and file, and choose Open. | The attachment is successfully created. |  |
| 6 | Save Attachment | Choose Save. | The attachment is successfully Saved. |  |

### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The sales order entry procedure assigned a billing block to the debit memo. This process step shows you how to remove the billing block.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Manage Debit Memo Requests - Version 2 (F1988A). | The Manage Debit Memo Requests - Version 2 screen displays. |  |
| 3 | Find the Document | Enter the document number you created in last step and choose Go. | The document displays. |  |
| 4 | Remove Billing Block | Choose the document and choose Billing Block > Remove Billing Block. |  |  |

### Create Debit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a debit memo and debit the customer's account.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search Billing Due Items | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Select Billing Item(s) | Select row(s) of a sales document created previously, and choose Create Billing Documents. | The Billing Documents screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Debit Memo (L2) and maintain billing date, for example, <current date>, then choose OK. | The new billing document is created. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Postings

| Product | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000 Rev Domestic Prod12100000 G/L ACC | 41000000 Rev Domestic Prod22000000 Output tax (MWS) | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search Billing Document | Enter the Billing document number recorded in previous step. Choose Enter. | The billing document displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments. Choose Save in the footer bar. |  |  |
| 7 | Update New Text (Optional) | In the Edit mode, you can add, delete, and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

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

### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

This optional process step shows you how to create attachment for billing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F2250). | The Displaying Billing Documents screen displays. |  |
| 3 | Enter the Billing Number | On the Display Billing Document screen, enter the respective invoice number created in previous step and choose Continue. | The Debit Memo xxx Display: Overview of Billing Items screen displays. |  |
| 4 | Create Attachment | Choose Services for Object in the top right corner of the screen, choose Create Attachment. | The Import File screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.On the Open screen, choose local path and file, choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object in the top right corner of the screen, choose Attachment list. | Attachment displays on the Service: Attachment list screen. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | In this activity you post a customer invoiceUsing the master data from this document, complete the following activities described in the test script:Accounts Receivable (J59) (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items). |
| BKK - Sales Order Fulfillment Monitoring and Operations ( (optional) | This test script describes the collection of periodic activities, such as day’s ending activities.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations (BKK) (Sections Review Sales Documents Blocked for Billing, Review Billing Due List, Review Log of Collective Invoice Creation and Review List of Blocked (for accounting) Billing Documents) |

### Scheduling Job (alternative)

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details displays. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/sale-of-services-2eq-ae-test-script-sap-s-4hana-cloud-public-edition-8]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 67,059 chars in the whole document
