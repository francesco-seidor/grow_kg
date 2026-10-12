---
id: 10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business
title: "Test Script: Automation of Central Procurement Quote with SAP Business Network (5JT) (5JT_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script 5JT: central RFQ via SAP Business Network, supplier quote, award, follow-on PO, supplier quick enablement."
cluster: 10-procurement
tags: [kb/procurement, topic/central-sourcing, topic/business-network-purchase-to-pay]
aliases: [5JT_S4CLD2608_BPD_EN_XX]
keywords: [Central Sourcing and Central Procurement, central request for quotation, central procurement, sap business network, supplier quotation award, price quote submission, supplier quick enablement, supplier registration, purchase requisition update, follow-on purchase order]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5JT_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1106
topic: 10-procurement/central-sourcing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automation of Central Procurement Quote with SAP Business Network (5JT) (5JT_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5JT_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Sourcing and Central Procurement** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automation of Central Procurement Quote with SAP Business Network (5JT) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841062)

[2 Prerequisites 4](#_Toc232841063)

[2.1 System Access 4](#_Toc232841064)

[2.2 Roles 4](#_Toc232841065)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232841066)

[2.4 Additional Manual Configuration 6](#_Toc232841067)

[2.5 Business Conditions 6](#_Toc232841068)

[3 Overview Table 7](#_Toc232841069)

[4 Test Procedures 9](#_Toc232841070)

[4.1 Create Central Request for Quotation 9](#_Toc232841071)

[4.2 Edit Central Request for Quotations 11](#_Toc232841072)

[4.3 Submit Price Quote (as a Supplier in SAP Business Network Discovery) 12](#_Toc232841073)

[4.4 Close and Award Price Quote (Optional as a Buyer in SAP Ariba Discovery) 13](#_Toc232841074)

[4.5 Display Central Supplier Quotation (Optional) 14](#_Toc232841075)

[4.6 Award Central Supplier Quotation 15](#_Toc232841076)

[4.7 Update Purchase Requisition (Optional) 15](#_Toc232841077)

[4.8 Create Follow-On Document Purchase Order in a Connected System 17](#_Toc232841078)

[4.9 Quick Enablement of Suppliers 18](#_Toc232841079)

[4.9.1 Allow Quick Enablement of Suppliers 18](#_Toc232841080)

[4.9.2 Add or Update Supplier Email Address 19](#_Toc232841081)

[4.9.3 Create Central Request for Quotation 20](#_Toc232841082)

[4.9.4 Register Supplier 22](#_Toc232841083)

[4.9.5 Check Supplier Data (as a Buyer in the SAP Business Network) 23](#_Toc232841084)

## Purpose

Overview

Integrate SAP S/4HANA Cloud Public Edition and SAP Business Network through SAP Integration Suite, managed gateway for spend management and SAP Business Network. This integration gives you access to more than two million companies that can provide quotations and quick and easy supplier discovery.

Create central request for quotations (cRFQs) in SAP S/4HANA Cloud Public Edition for central procurement. You can pool purchase requisitions from connected SAP S/4HANA systems. Suppliers submit their bids through SAP Business Network Discovery. After awarding the supplier quotations in SAP S/4HANA Cloud Public Edition for central procurement, the supplier quotation generates either purchase orders or purchasing contracts in the respective connected backend system.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | Identifies any SAP S/4HANA Cloud Public Edition system on software version 1905 or higher. The SAP S/4HANA Cloud Public Edition system acts as a hub system when it's connected to multiple connected systems.Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP ERP6.0, EHP6, or higher system version with HUBERPI add-on is considered as connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher system version with HUBS4IC add-on is considered as connected system.Any SAP S/4HANA Cloud Public Edition 1908 system version is considered as connected system. |
| SAP Business Network | Accessible via SAP Business Network. Your system administrator provides you with the URL and logon data to access SAP Business Network. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, see [How to Create a Business Role for the Administrator](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) on SAP Help Portal.

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_MM_SPT_CNTRL_PURCHASING_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

|  |
| --- |
| ExampleDataSample ValueDetailsCommentsPlant1010PlantStorage Location101AStd. storage 1Storage Location101BStd. storage 2Company Code1010Company Code 1010Purchase Organization1010Purch. Org. 1010Purchasing Group001Group 001Vendor1030008510300085We assume that the supplier in SAP Business Network uses the same name as in the SAP S/4HANA Cloud Public Edition system.MaterialTG0011Trading Good 0011, PD,Regular Proc.no Serial no.; no batchFor more information, refer to [Business Conditions](#unique_6) [page ] 6.Central Purchase Organization1010Purch. Org. 1010Central Purchase group001Group 001 |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1830bc3b4618fa702c3b54496f8b7a72)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2XT – Central Purchasing | To run through this test script, the Central Purchase Requisition must be created according to 2XT - Central Purchasing scope item. The prerequisites of 2XT must be fulfilled, and the following steps of test procedure must be completed before the test procedure of this test script is started:Create Purchase RequisitionImport Purchase RequisitionsManage Purchase Requisitions Centrally |
| 3ZF – Central Sourcing | To run through this test script, the prerequisites of 3ZF must be fulfilled. |
| 4BL - Central Sourcing | To run through this test script, the prerequisites of 4BL must be fulfilled. |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Central Request for Quotation](#unique_9) [page ] 9 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) | You created a cRFQ from multiple purchase requisition items. |
| [Edit Central Request for Quotations](#unique_10) [page ] 11 | Purchaser - Central Procurement | Manage Central RFQs (F3974) | You edited your cRFQ. |
| [Submit Price Quote (as a Supplier in SAP Business Network Discovery)](#unique_11) [page ] 12 | Supplier in SAP Business Network Discovery | [discovery.ariba.com](https://discovery.ariba.com/) | You submitted the price quote. |
| [Display Central Supplier Quotation (Optional)](#unique_12) [page ] 14 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) | You reviewed the detailed information of the central supplier quotation. |
| [Award Central Supplier Quotation](#unique_13) [page ] 15 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) | You awarded a central supplier quotation. |
| [Create Follow-On Document Purchase Order in a Connected System](#unique_14) [page ] 17 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) | You created a purchase order as follow-on document from the automatically created supplier quotation in the connected system. |
| [Allow Quick Enablement of Suppliers](#unique_15) [page ] 18 | Buyer in SAP Business Network | [https://buyer.ariba.com](https://buyer.ariba.com) | You allowed the quick enablement of suppliers. |
| [Add or Update Supplier Email Address](#unique_16) [page ] 19 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You added or updated the email address of the supplier. |
| [Create Central Request for Quotation](#unique_17) [page ] 20 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) | You created a cRFQ from multiple purchase requisition items. |
| [Allow Quick Enablement of Suppliers](#unique_15) [page ] 18 | SAP Business Network | link in registration email from SAP Business Network | You registered a supplier in SAP Business Network. |
| [Check Supplier Data (as a Buyer in the SAP Business Network)](#unique_18) [page ] 23 | Buyer in SAP Business Network | [https://buyer.ariba.com](https://buyer.ariba.com) | You check the data of a new supplier. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Central Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase requisitions from different connected systems get replicated (extracted) to the SAP S/4HANA Cloud Public Edition (procurement hub) system and are available for sourcing in the Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) app. You are unable to find a source of supply for the purchase requisition items, but you can select multiple requisition items and create a central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) app. | The Process Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Create Central RFQ | Enter the required search criteria, and choose Go.Select the checkbox of multiple Purchase Requisition Items.To create a new central purchase RFQ, choose Create Document > Create Central RFQ. | The New Central RFQ screen is displayed. |  |
| 4 | Enter Central RFQ Data | On the New Central RFQ screen, do the following steps:In the General Information section, enter the following data according to your business requirements:ExampleRFQ Type: Ext. Price Request (default value)RFQ Description: <RFQ Description>Language Key: ENQuotation Deadline: <today>Central Purchasing Group: 001Central Purchasing Organization: 1010Central Company Code: 1010Follow-On Document Type: POThe follow-on document type defined here will determine the available option in the central supplier quotation as mentioned in [Create Follow-On Document Purchase Order in a Connected System](#unique_14) [page ] 17. For example, for purchase order (PO), the option in Central Supplier Quotation is Create Purchase Order.In the Delivery and Payment Terms section, enter the following data according to your business requirements:ExampleTarget Value: 200Currency: EURIn the Items section, the selected purchase requisition items are listed under Request for Quotation Items. Do the following steps:Ensure that the data is correct.Select one of the items.The details screen of the selected item is displayed.Go to the Notes section. Enter the following data according to your business requirements:Item Note: Optionally, enter an item note.Attachments: Attachments are not supported by SAP Business Network at item-level.Note You can add attachments at header-level (step 6).Review your changes and choose Apply.The New Central RFQ screen is displayed.In the Bidders section, the selected purchase requisition items are listed. Do the following steps:Choose Add Bidder.In the Supplier field, enter, for example, 10300085.In the Notes section, enter the following data according to your business requirements:Detailed Description: Optionally, enter a detailed description.Internal Note: Optionally, enter an internal note.In the Attachments section, optionally choose Upload or Add Link to add an attachment.Choose Create > Publish. | You created a central RFQ from multiple purchase requisition items. |  |

### Edit Central Request for Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter additional details like payment terms and incoterms for a central RFQ (cRFQ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central RFQs (F3974). | The Manage Central RFQs screen is displayed. |  |
| 3 | Search Central RFQ | On the Manage Central RFQs screen, enter the required search criteria to search for your cRFQ.To display the details of your cRFQ, select your cRFQ from the search result list. |  |  |
| 4 | Edit the Central RFQ Data | You can change the content. For example, change the quotation deadline, or modify the cRFQ description.Choose Save > Publish. | You edited your cRFQ. |  |

### Submit Price Quote (as a Supplier in SAP Business Network Discovery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter your bids as a supplier in SAP Business Network Discovery.

After the quotation deadline (as set in [Edit Central Request for Quotations](#unique_10) [page ] 11) passed the bid is forwarded to the buyer. For example, after entering the bid, you've to wait until the quotation deadline you entered in the RFQ has passed (that would typically be the next day if you set the quotation deadline to today) before you can continue with the test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network Discovery as a Supplier on [discovery.ariba.com](https://discovery.ariba.com/). |  |  |
| 2 | Display Automated RFQ Overview | Choose I'm Selling > Leads .Search for the relevant RFQ.In the Details section, comments and attachments are displayed. | An overview list of the existing RFQs is displayed by default. |  |
| 3 | Open RFQ | From the overview list of the existing RFQs, select an RFQ to open it. | In the Details section, comments and attachments are displayed. |  |
| 4 | Create Response | Choose Quote all.You can also select a line item that you want to bid on and choose Quote Selected. | The list of all item parts of the RFQ is displayed. |  |
| 5 | Submit Response | For each of the items, enter the following data according to your business requirements:Price: 1Choose Submit. | You submitted the price quote. |  |

### Close and Award Price Quote (Optional as a Buyer in SAP Ariba Discovery)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to award and close the quotation as a Buyer in SAP Ariba Discovery. Then the bid is forwared to the buyer.

|  |
| --- |
| Note This step is optional based on the template setting in SAP Ariba Discovery. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Ariba Discovery as a Buyer on [discovery.ariba.com](https://discovery.ariba.com/). |  |  |
| 2 | Display Automated RFQ Overview | Choose I’m Buying > Postings. | An overview list of the existing RFQs is displayed. |  |
| 3 | Select RFQ | Search for the relevant RFQ and open it. |  |  |
| 4 | Compare Bids | Choose Bids. | The list of all items that are part of the RFQ is displayed.You can compare quotations from different suppliers. |  |
| 5 | Close and Award | Choose Close and Award. | The quotation is closed, awarded, and automatically created in SAP S/4HANA Cloud Public Edition for central procurement. |  |

### Display Central Supplier Quotation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created supplier quotation in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central Supplier Quotations (F3975) app. | The Manage Central Supplier Quotations screen is displayed with a list of existing central supplier quotations. |  |
| 3 | Search for Central Supplier Quotation | To search for a specific central supplier quotation based on the previously created central RFQ, enter the required seach criteria.Choose Go. |  |  |
| 4 | Open Central Supplier Quotation | Select the Central Quotation and open it. |  |  |
| 5 | Display Central Supplier Quotation | Review the detailed information of this central supplier quotation.You can review and compare different central supplier quotations, and choose one to award. | You reviewed the detailed information of the central supplier quotation. |  |

### Award Central Supplier Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to award the automatically created central supplier quotation in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central Supplier Quotations (F3975) app. | The Manage Central Supplier Quotations screen is displayed with a list of existing central supplier quotations. |  |
| 3 | Search for Central Supplier Quotation | To search for a specific central supplier quotation, enter the required seach criteria.Choose Go. |  |  |
| 4 | Award Central Supplier Quotation | Select a central supplier quotation and choose Award. | You awarded a central supplier quotation. |  |

### Update Purchase Requisition (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to update the purchase requisition in your SAP S/4HANA Cloud Public Edition system. With the update, the valuation price and the fixed supplier of the purchase requisition match the price and the supplier of the central supplier quotation in SAP Ariba Discovery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Central Supplier Quotations (F3975) app. | The Manage Central Supplier Quotations screen is displayed. |  |
| 3 | Search for Central Supplier Quotation | To search for a specific central supplier quotation, enter the required search criteria.Choose Go. |  |  |
| 4 | Update Purchase Requisitions | Select a central supplier quotation and choose Update Purchase Requisitions > Close. | The Update Purchase Requisitions system message is displayed. |  |
| 5 | Log on to Connected System | If you’re using SAP S/4HANA Cloud Public Edition as a connected system, log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 6 | Access App | Open the Manage Purchase Requisitions - Professional (F2229) app. | The Manage Purchase Requisitions - Professional screen is displayed. |  |
| 7 | Search for the Purchase Requisition | To search for the purchase requisition that you've updated, enter the required search criteria.Choose Go. |  |  |
| 8 | Select the Purchase Requisition | Select the purchase requisition. | The Purchase Requisition screen is displayed. |  |
| 9 | Select the Purchase Requisition Item | Go to the Items tab. |  |  |
| 10 | Review Valuation Price | In the Purchase Requisition Items table, review the entry in the Valuation Price column. | The valuation price has been updated to match the price of the central supplier quotation in SAP Ariba Discovery. |  |
| 11 | Review Source of Supplier | To review the source of supplier, choose Settings (). Search for the Fixed Supplier column and select the checkbox to view this column in the Purchase Requisitions Items table. | The entry in the Fixed Vendor column is updated. |  |

### Create Follow-On Document Purchase Order in a Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a purchase order as follow-on document from the automatically created supplier quotation in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the respective connected system as a Purchaser - Central Procurement. |  |  |
| 2 | Access App | Open the Manage Central Supplier Quotations (F3975) app. | The Manage Central Supplier Quotations screen is displayed with a list of existing central supplier quotation. |  |
| 3 | Search for Central Supplier Quotation | To search for the central supplier quotation that you awarded, enter the required search criteria.Choose Go. |  |  |
| 4 | Display Central Supplier Quotation | Select a Central RFQ, and open it. |  |  |
| 5 | Create Purchase Order | Choose Follow-on Document > Create Purchase Order .On the Purchase Order Creation screen, choose Order. | You created a purchase order as follow-on document from the automatically created supplier quotation in the connected system. |  |

### Quick Enablement of Suppliers

The following chapters describe the process for quick enablement of a supplier, triggered by a central request for quotation (cRFQ).

Context

For a supplier who is available in SAP S/4HANA Cloud Public Edition, but not in SAP Business Network, the process triggers onboarding of the supplier to SAP Business Network, so that the supplier can be used in a commerce automation process.

Some steps have to be processed before a cRFQ can be sent to SAP Business Network. For example, you need to add or update the supplier email address that then triggers the invitation and registration process for the supplier in SAP Business Network.

Restrictions

The following restrictions apply to the quick enablement of suppliers:

- E-mail is the only communication method supported to invite suppliers for quick enablement.
- Quick enablement flow doesn't work for accounts in the test environment (ANID-T). It's only supported for accounts in the productive environment (ANID).

#### Allow Quick Enablement of Suppliers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to allow quick enablement of suppliers through a central request for quotation (cRFW) in your Ariba buyer account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). |  |  |
| 2 | Allow Quick Enablement | Select the profile picture and choose Manage Profile > Default Transaction Rules .In the Quick Enablement Rules section, select the Allow Quick Enablement checkbox.Choose Save. | The quick enablement of suppliers is allowed. |  |

#### Add or Update Supplier Email Address

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to add or update the email address of the supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access App | Open the Manage Supplier Master Data (F1053A) app. | The Manage Supplier Master Data screen is displayed. |  |
| 3 | Search for Purchase Order | To search for the supplier, enter a business partner ID.Tip You can use the value help (  ), to select the correct data.Choose Go. | In the search result list, the supplier is displayed. |  |
| 4 | Select Supplier | To add or update the data of the supplier, select the supplier. | The Supplier screen is displayed. |  |
| 5 | Select Supplier Address | On the Supplier screen, choose Address > Address Details .Select the address that has the value Yes in the Standard column. | The Address Details screen is displayed. |  |
| 6 | Add or Update Email Address | On the Address Details screen, choose Communication > Email .Add or update an email address. In the Standard column, select the checkbox.Choose Apply > Save . | The email address is added or updated, and is set as standard. |  |

#### Create Central Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase requisitions from different connected systems get replicated (extracted) to the SAP S/4HANA Cloud Public Edition (procurement hub) system and are available for sourcing in the Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) app. You are unable to find a source of supply for the purchase requisition items, but you can select multiple requisition items and create a central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser - Central Procurement. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) app. | The Process Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Create Central RFQ | Enter the required search criteria, and choose Go.Select the checkbox of multiple Purchase Requisition Items.To create a new central purchase RFQ, choose Create Document > Create Central RFQ. | The New Central RFQ screen is displayed. |  |
| 4 | Enter Central RFQ Data | On the New Central RFQ screen, do the following steps:In the General Information section, enter the following data according to your business requirements:ExampleRFQ Type: Ext. Price Request (default value)RFQ Description: <RFQ Description>Language Key: ENQuotation Deadline: <today>Central Purchasing Group: 001Central Purchasing Organization: 1010Central Company Code: 1010Follow-On Document Type: POThe follow-on document type defined here will determine the available option in the central supplier quotation as mentioned in [Create Follow-On Document Purchase Order in a Connected System](#unique_14) [page ] 17. For example, for purchase order (PO), the option in Central Supplier Quotation is Create Purchase Order.In the Delivery and Payment Terms section, enter the following data according to your business requirements:ExampleTarget Value: 200Currency: EURIn the Items section, the selected purchase requisition items are listed under Request for Quotation Items. Do the following steps:Ensure that the data is correct.Select one of the items.The details screen of the selected item is displayed.Go to the Notes section. Enter the following data according to your business requirements:Item Note: Optionally, enter an item note.Attachments: Attachments are not supported by SAP Business Network at item-level.Note You can add attachments at header-level (step 6).Review your changes and choose Apply.The New Central RFQ screen is displayed.In the Bidders section, the selected purchase requisition items are listed. Do the following steps:Choose Add Bidder.In the Supplier field, enter, for example, 10300085.In the Notes section, enter the following data according to your business requirements:Detailed Description: Optionally, enter a detailed description.Internal Note: Optionally, enter an internal note.In the Attachments section, optionally choose Upload or Add Link to add an attachment.Choose Create > Publish. | You created a central RFQ from multiple purchase requisition items. |  |

#### Register Supplier

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to register a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Receive Registration Email | After you received a registration email from SAP Business Network, select the link in the email to activate your account. |  |  |
| 2 | Register Supplier | Enter a temporary ID and a secure code. If you're asked to check for existing accounts, continue with the creation of a new account.Tip Note down the user name and password that you entered. | An activation email is sent to you. |  |
| 3 | Confirm Activation | Confirm the activation as described in the activation email. | An SAP Business Network registration confirmation email is sent to you. |  |
| 4 | Check Registration Data | Check if the SAP Business Network registration confirmation email provides you with the following information for your supplier:Company NameUser NameAriba Network ID (ANID)Logon URL | You registered a supplier in SAP Business Network. |  |

#### Check Supplier Data (as a Buyer in the SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the data of the new supplier in SAP Business Network as a buyer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Business Network as a Buyer on [https://buyer.ariba.com](https://buyer.ariba.com). | The Home screen is displayed. |  |
| 2 | Check Supplier Settings in the Buyer Account | Choose Supplier Enablement > Active Relationships. | The newly created supplier is listed with the Ariba Network ID (ANID) that you received in the SAP Business Network registration confirmation email. |  |
| 3 | Check Supplier Data | Select the supplier, and choose More Actions > Edit. | The supplier number from SAP S/4HANA Cloud Public Edition is displayed in the Vendor ID field. |  |

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
- related-to :: [[10-procurement/test-script-central-sourcing-3zf-sap-s-4hana-cloud-public-edition-990]]
- see-also :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5JT_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 39,668 chars in the whole document
