---
id: 10-procurement/contract-for-central-procurement-with-sap-ariba-contracts-4b0-test-scr
title: Contract for Central Procurement with SAP Ariba Contracts (4B0) - Test Script (4B0_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 4B0: creating, reviewing and updating central purchase contracts in SAP Ariba Contracts and creating a sourcing project, with S/4HANA Cloud Public Edition."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-contracts]
aliases: [4B0_S4CLD2608_BPD_EN_XX]
keywords: [Contracts with SAP Ariba Contracts, central purchase contracts, sap ariba contracts, central procurement, sourcing project, test script, contract amendment, business roles, test prerequisites, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B0_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1015
topic: 10-procurement/ariba-contracts
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Contract for Central Procurement with SAP Ariba Contracts (4B0) - Test Script (4B0_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B0_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Contracts with SAP Ariba Contracts** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract for Central Procurement with SAP Ariba Contracts (4B0) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232838709)

[2 Prerequisites 3](#_Toc232838710)

[2.1 Additional Manual Configuration 3](#_Toc232838711)

[2.2 System Access 3](#_Toc232838712)

[2.3 Roles 3](#_Toc232838713)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232838714)

[2.5 Business Conditions 4](#_Toc232838715)

[3 Overview Table 5](#_Toc232838716)

[4 Test Procedures 6](#_Toc232838717)

[4.1 Create Central Purchase Contract in SAP Ariba Contracts 6](#_Toc232838718)

[4.2 Review Central Purchase Contract in Connected System 9](#_Toc232838719)

[4.3 Update Central Purchase Contract in SAP Ariba Contracts 9](#_Toc232838720)

[4.4 Create Sourcing Project in SAP Ariba Contracts 11](#_Toc232838721)

## Purpose

Overview

In this scope item, you can integrate value and quantity contracts. These are agreements for a company to order certain quantities of products during a specified period. In SAP Ariba Contracts, users can negotiate prices for goods and lean services to be procured, and they can sign a legally binding contract with a supplier. Pricing details are passed on from SAP Ariba Contracts to the operational system, so that operational purchasers can use these prices to buy goods or services as required.

Central procurement offers a centralized contract process across industries with a deep integration into the customer's landscape. It connects SAP Ariba Contracts to the customer’s ERP or SAP S/4HANA Cloud Public Edition systems, and exchanges business documents to ensure end-to-end business processes into finance and logistics that run in the connected systems.

In this scope item, you can integrate value and quantity contracts. These are agreements for a company to order certain quantities of products during a specified period. In SAP Ariba Contracts, users can negotiate prices for goods and lean services to be procured, and they can sign a legally binding contract with a supplier. Pricing details are passed on from SAP Ariba Contracts to the operational system, so that operational purchasers can use these prices to buy goods or services as required.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0808c015b48f5f1478c37514a3341dce)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | The SAP S/4HANA Cloud Public Edition system acts as a hub system when it’s connected to multiple back-end systems.Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Backend System (Connected System) | System type supported as backend system: SAP S/4HANA Cloud Private Edition, SAP S/4HANA Cloud Public Edition, ECC. |
| Ariba Contract | Accessible via Ariba portal. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |

### Master Data, Organizational Data, and Other Data

Master data in your system landscape

- Initial set of master data such as Account Assignment Category, material group, purchasing organization, purchasing group, existing in the back-end system should also exist and be in sync with the Hub system and the SAP Ariba Buying system.
- Organizational data of back-end systems should exist in the Hub and the SAP Ariba Buying system, such as the Purchasing Organization and Purchasing groups.

### Business Conditions

The business process described in this test script is part of a bigger chain of integrated business processes or scope items. So you must have completed the following processes and fulfilled the following business conditions before going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| 2ME - Central Purchase Contracts | Complete the Preliminary Steps in the test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Central Purchase Contract in SAP Ariba Contracts](#unique_9) [page ] 6 | Purchaser in SAP Ariba Contracts |  | The central purchase contract is created in SAP Ariba Contracts. |
| [Review Central Purchase Contract in Connected System](#unique_10) [page ] 9 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) | The central purchase contract can be reviewed in the connected system, for example, SAP S/4HANA Cloud Public Edition. |
| [Update Central Purchase Contract in SAP Ariba Contracts](#unique_11) [page ] 9 | Purchaser in SAP Ariba Contracts |  | The central purchase contract is updated in SAP Ariba Contracts. |
| [Create Sourcing Project in SAP Ariba Contracts](#unique_12) [page ] 11 | Purchaser in SAP Ariba Contracts |  | A sourcing project is created in SAP Ariba Contracts. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Central Purchase Contract in SAP Ariba Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a central purchase contract in SAP Ariba Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access SAP Ariba as a Purchaser (in SAP Ariba Contracts). | The Home screen opens.Your system administrator provides you with logon data for your SAP Ariba system. |  |
| 2 | Access App | In Common Action section, choose the Contract Workspace (Procurement) link. | The Contract Workspace (Procurement) screen opens. |  |
| 3 | Enter Contract Header Data | Enter all of the necessary data.Name: Ariba ContractTest Project: NoSupplier: Sourcing Sup 10_2_1Contract Amount: 1000USDAgreement Date: Today’s dateEffective Date: First day of next monthExpiration Date: Current date + 3 months |  |  |
| 4 | Enter Data for External System | Enter all of the necessary data.External System Select the external system integrated with your SAP Ariba realm.Select a Template SAP S/4HANA Cloud Private Edition Integration testingCompany Code 1010Purchasing Organization 1010Purchasing Group 001Document Type Central ContractDocument Category MK Quantity Contract |  |  |
| 5 | Create Central Purchase Contract | Choose Create.Ignore the desktop file sync warning message. |  |  |
| 6 | Open Contract Line Items Document (CLID) | In the Documents section, choose the CLID link and select Open action. | The CLID screen opens. |  |
| 7 | Add Contract Lines | In the All Content section, choose Add and select the Items From Item Master Data action.In the material number field, enter TG0011 and choose Search.Select the line with the material number TG0011 and choose Copy.Enter all of the necessary data:Price:10Quantity:2You can either add items from master data or choose them freely.In the All content section, choose Add and select the Item action.Enter all of the necessary data:Name: test contract itemDescription: test contract itemCommodity: All Commodities AllProduct Type: MaterialPrice: 10Quantity: 2Plant: 1010Item Category: 8 or 0 StandardMaterial Group: L001Choose Done.You can freely add ad-hoc item for service.In the All Content section, choose Add and select the Item action.Enter all necessary data:Name: test contract itemDescription: test contract itemProduct Type: ServicePrice: 10Quantity: 2Plant: 1010Item Category: 0 StandardMaterial Group: L001Choose Done. |  |  |
| 8 | Check Data Validity | Choose Validate Master Data. | No error messages should be displayed. |  |
| 9 | Publish Contract Line Items Document | Choose Publish.Review the content and choose OK. | The system message ‘CLID’ has been published successfully is displayed. |  |
| 10 | Publish Central Purchase Contract | In the Contract Attributes section, choose Action and then Publish. |  |  |
| 11 | Send Contract to SAP S/4HANA Cloud Public Edition | In the Documents section, choose the CLID link and the Send to External System action.Choose OK on the next page. | The system message Send to External system is successful is displayed. |  |
| 12 | Check Document Sending Status | In the Overview section, choose the Action link, then select View History. | The latest message in the list is in status SendContractRequestSuccess. |  |

### Review Central Purchase Contract in Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can review the central purchase contract you've created in [Create Central Purchase Contract in SAP Ariba Contracts](#unique_9) [page ] 6.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to Connected System | If you're using SAP S/4HANA Cloud Public Edition as a connected system, log on to SAP Fiori launchpad as a Purchaser - Central Procurement. |  |  |
| 2 | Access App | Open the Manage Central Purchase Contracts (F3144) app. |  |  |
| 3 | Review Central Purchase Contract | Review the central purchase contract that you've created in [Create Central Purchase Contract in SAP Ariba Contracts](#unique_9) [page ] 6.Search for the contract using the following filter criteria:Created On: today |  |  |

|  |
| --- |
| Note For succeeding processes such as distributing central contracts, creating a purchase order, and so on, you can refer to the test script of scope item [Central Purchase Contracts (2ME)](https://me.sap.com/processnavigator/SolP/2ME). |

### Update Central Purchase Contract in SAP Ariba Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you update the central purchase contract information in SAP Ariba Contracts, such as item information, contracts price, and so on. Afterwards, the updates can be replicated to external systems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access Ariba as a Purchaser (in SAP Ariba Contracts). | The Home screen opens.Your system administrator provides you with logon data for your SAP Ariba system. |  |
| 2 | Access App | Access the central purchase contract that you've created in [Create Central Purchase Contract in SAP Ariba Contracts](#unique_9) [page ] 6. |  |  |
| 3 | Choose Amend Type | In the Contract Attributes section, choose Action > Amend.Choose Amend Type and type in Amendment Reason Comment. For example: AmendmentOn the next screen, choose OK. |  |  |
| 4 | Open Contract Line Items (CLID) | In the Documents section, choose the CLID link and select Open action. | The CLID screen opens. |  |
| 5 | Update Line Items | Change line items information as desired. For example, reset Price or Quantity. |  |  |
| 6 | Publish Contract Line Items Document | In Confirm Publish - CLID page, review the changes and choose OK. | The system message 'CLID' has been published successfully is displayed. |  |
| 7 | Publish Contract | In the Contract Attributes section, choose Action and then Publish. |  |  |
| 8 | Send Central Purchase Contract to SAP S/4HANA Cloud Public Edition | In the Documents section, choose the CLID link and the Send to External System action.Choose OK on the next page. | The system message Send to External System is successful is displayed. |  |
| 9 | Check Document Sending Status | In the Overview section, choose the Action link, then select View History. | The latest message in the list is in status SendContractRequestSuccess. |  |
| 10 | Review Central Purchase Contract in Connected System | You can review the updatedcentral purchase contract in the connected system, for example, SAP S/4HANA Cloud Public Edition.For more information, see [Review Central Purchase Contract in Connected System](#unique_10) [page ] 9. |  |  |

### Create Sourcing Project in SAP Ariba Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a sourcing project in SAP Ariba Sourcing as a strategic buyer. The sourcing project has specific terms for the sourcing in order to invite suppliers to offer their bids on SAP Ariba Contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access SAP Ariba as a Purchaser (in SAP Ariba Contracts). | The Home screen is displayed.Your system administrator provides you with logon data for your SAP Ariba system. |  |
| 2 | Create Sourcing Project | In the Common Action section, Choose Sourcing Project > Open .Enter the following data according to your business requirements:Name: Ariba Sourcing ProjectEvent Type: RFPTest Project: YesIn the Select a Template field, select IES S2C Request for Proposal.Choose Create. |  |  |
| 3 | Define Time Rules | In the Time Rules section, enter the following data according to your business requirements:Response start date: When I select the publish button on the Summary pageDue date : <today>Duration : 30 minutesChoose Next. |  |  |
| 4 | Define Team | Choose Next. |  |  |
| 5 | Define Participants | Choose Invite Participants.Choose Search and select one supplier, for example, Test SLP 03.Choose OK > Next . |  |  |
| 6 | Define Contents | Choose Pricing > Add .Review the dropdown list and choose Line Item.Enter the following data according to your business requirements:Name: MFT1 for Simple PricingDescription: MFT1 for Simple PricingCommodity: All CommoditiesEnter the following data according to your business requirements:Price: 10Historic: 12Quantity: 2Choose Add. From the dropdown list, choose Term.Select Discount Amount/Discount Percentage then, choose OK.Enter the following data according to your business requirements:Discount Amount: 9Discount Percentage: 8%Choose Done. |  |  |
| 7 | Publish Pricing Condition | Choose Next > Publish .Choose Monitor Event |  |  |
| 8 | Check Sourcing State | Check that the Sourcing event is in state Time remaining.If the status is Time remaining until publish, you can reduce the timing left. Choose Actions and select Reduce Timing. Specify the time reduction and choose OK. |  |  |
| 9 | Surrogate Bid for Suppliers | Choose tab Suppliers and select the Invited Participants you defined in Step 9. Then, select Surrogate Bid.If the Surrogate Bid is missing, do the following steps depending on system setup:From the Home screen of SAP Ariba Sourcing, choose Manage > Administration > Supplier and Customer Manager > Users .Choose List all.To act as a specific supplier user you defined in Step 9, Go to the row of that supplier and choose Actions > Act as .Note In the following steps you are acting as a supplier.Find the sourcing project you created in the status Open section, then select it. |  |  |
| 10 | Confirm Prerequisites | Select the previously created sourcing event that is in status Open from the Events list.In the Event Details area, choose Review and Accept Prerequisites.Select the I accept the terms of this agreement checkbox.Choose OK twice. |  |  |
| 11 | Select Lots | Mark the available for bidding lots.Choose Confirm Selected Lots. |  |  |
| 12 | Submit Response | Enter the following data according to your business requirements:You can make the necessary entries only when the timer is running.Price: 9Discount Amount: 9Discount Percentage: 8%Choose Submit Entire Response > OK . |  |  |
| 13 | Stop Acting as Supplier | To stop acting as a supplier, choose Stop. |  |  |
| 14 | Check Sourcing State | Check that the sourcing event is in state Pending Selection.If the status is Time Remaining you can reduce the timing left.Choose Actions > Reduce Timing .Specify the time reduction and choose OK. |  |  |
| 15 | Set up Scenario | Select Scenario section and select Best Bit. Then, select Edit. |  |  |
| 16 | Set up Award Sourcing | Choose Optimize. Then select Continue working on this scenario.Select Submit for award.Deselect the Send Emails to Awarded Participants checkbox.Choose Done. |  |  |
| 17 | Award Confirmation | Choose Done. You can see the status change to Completed. |  |  |
| 18 | Create New Contract by award sourcing | Select Award section and select Contract. Choose Create new contract from the dropdown list.Select Invited Participants, then choose Create new contract. Select Contract Workspace (Procurement).Enter most of the necessary data reference by the previous precdure [Create Central Purchase Contract in SAP Ariba Contracts](#unique_9) [page ] 6.Document Type: Central ContractDocument Category: WK Value ContractChoose Create.Ignore the desktop file sync warning message. |  |  |
| 19 | Confirm Award sourcing | In the Documents section, choose the line items Document link and select Open action. |  |  |

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
- related-to :: [[10-procurement/test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B0_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,362 chars in the whole document
