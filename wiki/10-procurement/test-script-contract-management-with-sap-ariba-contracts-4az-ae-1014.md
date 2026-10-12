---
id: 10-procurement/test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014
title: "Test Script: Contract Management with SAP Ariba Contracts (4AZ_AE) (4AZ_S4CLD2608_BPD_EN_AE)"
description: SAP S/4HANA Cloud Public Edition 2608 test script (scope item 4AZ) for creating contracts or scheduling agreements in SAP Ariba Contracts and reviewing them in S/4HANA.
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-contracts]
aliases: [4AZ_S4CLD2608_BPD_EN_AE]
keywords: [Contracts with SAP Ariba Contracts, ariba contracts integration, purchase contracts, scheduling agreements, contract creation, contract id synchronization, additional configuration, business roles, master data, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1014
topic: 10-procurement/ariba-contracts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Management with SAP Ariba Contracts (4AZ_AE) (4AZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contracts with SAP Ariba Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Management with SAP Ariba Contracts (4AZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854894)

[2 Prerequisites 3](#_Toc232854895)

[2.1 Additional Manual Configuration 3](#_Toc232854896)

[2.2 System Access 3](#_Toc232854897)

[2.3 Roles 3](#_Toc232854898)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232854899)

[3 Overview Table 5](#_Toc232854900)

[4 Test Procedures 6](#_Toc232854901)

[4.1 Create Contract or Scheduling Agreement in SAP Ariba Contracts 6](#_Toc232854902)

[4.2 Review Contract in SAP S/4HANA Cloud Public Edition 9](#_Toc232854903)

[4.3 Review Scheduling Agreement in SAP S/4HANA Cloud Public Edition (Optional) 10](#_Toc232854904)

[4.4 Check Updated Contract ID or Scheduling Agreement ID in SAP Ariba Contracts 11](#_Toc232854905)

## Purpose

Overview

Integrate SAP S/4HANA Cloud Public Edition with SAP Ariba Contracts to connect value and quantity contracts. These are agreements for a company to order certain quantities of products during a specified period. In SAP Ariba Contracts, users can negotiate prices for goods and lean services to be procured, and they can sign a legally binding contract with a supplier. In source determination in SAP S/4HANA Cloud Public Edition, contracts can then be assigned in the source list as fixed sources of supply. Pricing details are passed on from SAP Ariba Contracts to the operational system, so that operational purchasers can use these prices to buy goods or services as required. Target groups of Contract Management with SAP Ariba Contracts are purchasing managers as well as strategic buyers and operational purchasers.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/b97c5c6ad1dcd4552128c9464231ef9c)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Ariba | Accessible via the SAP Ariba portal. Your system administrator provides you with logon data. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor/Supplier | 33300001 | Vendor domestic United Arab Emirates Ariba |  |
| Material | TG10TG11 | Trad.Good 10,PD,Third PartyTrading.Good 11,PD,Reg.Trading |  |

## Overview Table

This scope item consists of several process steps, reports, items provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Contract or Scheduling Agreement in SAP Ariba Contracts](#unique_8) [page ] 6 | Purchaser (in SAP Ariba Contracts) |  | A purchasing contract or a scheduling agreement is created in SAP Ariba Contracts. |
| [Review Contract in SAP S/4HANA Cloud Public Edition](#unique_9) [page ] 9 | Purchaser | Manage Purchase Contracts (F1600A) | The newly created purchasing contract or scheduling agreement is visible in SAP S/4HANA Cloud Public Edition and can be reviewed. |
| [Review Scheduling Agreement in SAP S/4HANA Cloud Public Edition (Optional)](#unique_10) [page ] 10 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | The newly created scheduling agreement is visible in SAP S/4HANA Cloud Public Edition and can be reviewed. |
| [Check Updated Contract ID or Scheduling Agreement ID in SAP Ariba Contracts](#unique_11) [page ] 11 | Purchaser (in SAP Ariba Contracts) |  | The purchasing contract ID or the scheduling agreement ID is updated in SAP Ariba Contracts. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Contract or Scheduling Agreement in SAP Ariba Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchasing contract or a scheduling agreement in SAP Ariba.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Ariba Contracts as a Purchaser. | The Home screen is displayed.Note Your system administrator provides you with logon data for your SAP Ariba system. |  |
| 2 | Access App | In the Common Action section, choose the Contract Workspace (Procurement) link. | The Contract Workspace (Procurement) screen is displayed. |  |
| 3 | Enter Contract Header Data | Enter the following data according to your business requirements:Name: Ariba ContractTest Project: NoSupplier: SAP S/4HANA Cloud Private Edition Supplier testNote The supplier name is an example value. It can differ depending on the system configurations.Contract Amount: 1000AEDAgreement date: <Today’s date>Effective date: <First day of next month>Expiration date: <Current date + 3 months> |  |  |
| 4 | Enter Data for External System | Enter the following data according to your business requirements:Select a template: SAP S/4HANA Cloud Private Edition IntegrationCompany Code: 3310External System: Select the external system integrated with your SAP Ariba realm.Purchasing Organization: 3310Purchasing Group: 001Document Type: Contract or Schedule Agreement (L)Document Category: MK Quantity Contract or LP Schedule Agreement |  |  |
| 5 | Create Contract | Choose Create. |  |  |
| 6 | Open Contract Line Items Document (CLID) | In the Documents section, select the CLID link and choose Open. | The CLID screen is displayed. |  |
| 7 | Add Contract Lines | In the All content section, choose Add > Items From Item Master Data.In the Material Number field, enter TG11, and choose Search.Select the line with material number TG11, and choose Copy.Enter the following data according to your business requirements:Price: 10Quantity: 2Plant: 3310Item Category: 0 (Standard)Material Group: L001Custom UoM: EAIf you can’t find material TG11 in the Search list, navigate to the All content section, and choose Add > Item.Enter the following data according to your business requirements:Name: test itemDescription: test itemCommodity: All Commodities AllPrice: 10Quantity: 2Plant: 3310Item Category: 0 (Standard)Material Group: L001Custom UoM: EAChoose Done. |  |  |
| 8 | Add Outline (Optional) | In the All content section, choose Add > Outline.Enter the following data according to your business requirements:Name: test item 1Description: test item 1Product Type: materialChoose Done.Note You can add up to 4 outlines. | An outline is added. |  |
| 9 | Create Material Item for Outline (Optional) | In the All content section, select the Outline checkbox and choose Add > Items From Item Master Data.Select the line with material number TG11 and choose Copy.Enter the following data according to your business requirements:Price: 10Quantity: 2If you can't find the material number TG11 in the search results list, go to the All content section, and choose Add > Item.Enter the following data according to your business requirements:Name: test itemDescription: test itemCommodity: Industrial Cleaning Services 76Price: 10Quantity: 2Plant: 3310Item Category: 0 (Standard)Material Group: L001Material Code: TG10Choose Done. | A material item for the outline is created. |  |
| 10 | Check Data Validity (Optional) | Choose Validate Master Data. | The message Master Data is valid is displayed. |  |
| 11 | Publish Contract Line Items Document | Choose Publish.Review the content, and choose OK. | The message ‘CLID’ has been published successfully is displayed. |  |
| 12 | Publish Contract | In the Contract Attributes section, choose Action > Publish. |  |  |
| 13 | Send Contract to SAP S/4HANA Cloud Public Edition | In the Documents section, select the CLID link, and choose Send to External System.On the next screen, choose OK. | The message Send to External system is successful is displayed. |  |
| 14 | Check Document Sending Status | In the Overview section, select the Action link, and choose View History. | The latest message in the list has the status SendContractRequestSuccess. |  |

### Review Contract in SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display and review the purchasing contract that you've created in [Create Contract or Scheduling Agreement in SAP Ariba Contracts](#unique_8) [page ] 6 in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Contracts (Version 2) (F1600A) app. | The Manage Purchase Contracts screen is displayed. |  |
| 3 | Search for the Contract | Search for the contract using the following filter criteria:Creation Date: todayExternal Reference ID: <Contract ID from SAP Ariba Contracts>Choose Go. |  |  |
| 4 | Open Document | From the search results list, select the purchasing contract that you've created in [Create Contract or Scheduling Agreement in SAP Ariba Contracts](#unique_8) [page ] 6.Note If you want to perform the steps described in [Check Updated Contract ID or Scheduling Agreement ID in SAP Ariba Contracts](#unique_11) [page ] 11, make a note of the Contract ID. | The choosen purchasing contract is opened and can be reviewed. |  |

### Review Scheduling Agreement in SAP S/4HANA Cloud Public Edition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display and review the scheduling agreement that you've created in [Create Contract or Scheduling Agreement in SAP Ariba Contracts](#unique_8) [page ] 6 in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note Please note that this step is optional and can be executed only if you have selected scheduling agreement as a document type in [Review Contract in SAP S/4HANA Cloud Public Edition](#unique_9) [page ] 9. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Scheduling Agreements (F2179) app. | The Manage Purchase Scheduling Agreements screen is displayed. |  |
| 3 | Search Scheduling Agreement | To search for a scheduling agreement, enter the following search criteria:Company Code: 3310Supplier: 33300001Choose Go. |  |  |
| 4 | Open Document | From the search results list, select the scheduling agreement that you've created in [Create Contract or Scheduling Agreement in SAP Ariba Contracts](#unique_8) [page ] 6.Note If you want to perform the steps described in [Check Updated Contract ID or Scheduling Agreement ID in SAP Ariba Contracts](#unique_11) [page ] 11, make a note of the Scheduling Agreement ID. | The choosen scheduling agreement is opened and can be reviewed. |  |

### Check Updated Contract ID or Scheduling Agreement ID in SAP Ariba Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the updated contract ID or scheduling agreement ID sent from SAP S/4HANA Cloud Public Edition to SAP Ariba Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Ariba Contracts as a Purchaser. | The Home screen is displayed. |  |
| 2 | Search for Purchasing Contract or Scheduling Agreement | Select the Contract tab.On the Contract tab, choose Search. In the Project Type field, select Contract Workspace (Procurement) from the dropdown list. In the search field, enter the contract ID or scheduling agreement ID, and choose Search. |  |  |
| 3 | Open Contract and Check for Updated Contract ID or Scheduling Agreement ID | From the search results list, select the relevant purchasing contract or scheduling agreement and choose Open from the dropdown list.Select the Overview tab, and go to Contract Attributes. Check if the Related ID field is updated with the contract ID or scheduling agreement ID you noted down in [Review Contract in SAP S/4HANA Cloud Public Edition](#unique_9) [page ] 9 or [Review Scheduling Agreement in SAP S/4HANA Cloud Public Edition (Optional)](#unique_10) [page ] 10. |  |  |

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
> Flagged while digesting this document, not verified: Step 3 and 4 name the supplier/template 'SAP S/4HANA Cloud Private Edition' within a Public Edition script; the doc says the name is example/configuration dependent

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/contract-for-central-procurement-with-sap-ariba-contracts-4b0-test-scr]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4AZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 20,518 chars in the whole document
