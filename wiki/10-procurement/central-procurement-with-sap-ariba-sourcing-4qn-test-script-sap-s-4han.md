---
id: 10-procurement/central-procurement-with-sap-ariba-sourcing-4qn-test-script-sap-s-4han
title: "Central Procurement with SAP Ariba Sourcing (4QN) - Test Script, SAP S/4HANA Cloud Public Edition (4QN_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 4QN: central RFQ, Ariba Sourcing (guided/classic UI), award, supplier quotation and follow-on contract or PO in S/4HANA Cloud Public."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-sourcing]
aliases: [4QN_S4CLD2608_BPD_EN_XX]
keywords: [Sourcing with SAP Ariba Sourcing, central procurement, central rfq, ariba sourcing, guided sourcing ui, classic sourcing ui, supplier bidding, award scenarios, central supplier quotation, follow-on documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4QN_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1043
topic: 10-procurement/ariba-sourcing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Central Procurement with SAP Ariba Sourcing (4QN) - Test Script, SAP S/4HANA Cloud Public Edition (4QN_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4QN_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Sourcing with SAP Ariba Sourcing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Central Procurement with SAP Ariba Sourcing (4QN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232834669)

[2 Prerequisites 4](#_Toc232834670)

[2.1 System Access 4](#_Toc232834671)

[2.2 Roles 4](#_Toc232834672)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232834673)

[2.4 Additional Manual Configuration 5](#_Toc232834674)

[2.5 Business Conditions 5](#_Toc232834675)

[3 Overview Table 7](#_Toc232834676)

[4 Test Procedures 9](#_Toc232834677)

[4.1 Create Central Request for Quotation 9](#_Toc232834678)

[4.2 Manage Central Request for Quotations 11](#_Toc232834679)

[4.3 Sourcing with SAP Ariba Guided Sourcing UI 11](#_Toc232834680)

[4.3.1 Create Sourcing Project (as a Buyer in Ariba Sourcing) 12](#_Toc232834681)

[4.3.2 Participate in Sourcing Event (as a Supplier in Ariba Sourcing) 14](#_Toc232834682)

[4.3.3 Accept Supplier's bidding (as a Buyer in Ariba Sourcing) 15](#_Toc232834683)

[4.4 Sourcing with SAP Ariba Classic Sourcing UI 17](#_Toc232834684)

[4.4.1 Create Sourcing project (as a buyer in Ariba Sourcing) 17](#_Toc232834685)

[4.4.2 Participate in Sourcing Event (as a Supplier in Ariba Sourcing) 19](#_Toc232834686)

[4.4.3 Accept Supplier's bidding (as a Buyer in Ariba Sourcing) 21](#_Toc232834687)

[4.4.4 Send Quote Message (as a Buyer in Ariba Sourcing) 22](#_Toc232834688)

[4.5 Display Automatically Created Central Supplier Quotation from Award 23](#_Toc232834689)

[4.6 Display Follow-on Document 24](#_Toc232834690)

[4.6.1 Display Logs for Follow-On Docs 24](#_Toc232834691)

[4.6.2 Display Follow-On Documents in Business Process Flow 25](#_Toc232834692)

[4.7 Create Follow-on Document 25](#_Toc232834693)

[4.7.1 Scenario 1: Create Purchase Contract 25](#_Toc232834694)

[4.7.1.1 Display Central Purchase Contracts 26](#_Toc232834695)

[4.7.1.2 Check Local Contract - In Connected System 27](#_Toc232834696)

[4.7.2 Scenario 2: Create Purchase Order 27](#_Toc232834697)

[4.7.2.1 Display Purchase Order - In Connected System 28](#_Toc232834698)

[4.7.2.2 Post Goods Receipt - In Connected System 28](#_Toc232834699)

[4.7.2.3 Create Supply Invoice - In Connected System 29](#_Toc232834700)

## Purpose

Overview

The SAP S/4HANA Hub system offers a centralized RFQ process with a deep integration into the customer's landscape. It connects SAP Ariba Sourcing to the customer’s SAP ERP or SAP S/4HANA system (on-premise or Cloud).

With the SAP S/4HANA Hub system, you can pool or aggregate purchase requisitions created in multiple connected backend systems. This allows you to create a single central RFQ and thus get support for better pricing.

SAP Ariba Sourcing provides access to intuitive RFX tools (for requests for information and requests for proposals). It connects you to more than two million companies for quick and easy supplier discovery. It also offers automated and adjustable negotiation procedures.

Once the award process is completed in SAP Ariba Sourcing, the supplier contract created in the SAP S/4HANA Hub system generates either purchase orders or contracts in the respective connected backend system.

This scenario is recommended for the indirect sourcing process only. This scope item requires an additional license for SAP Ariba Strategic Sourcing.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition HUB system | Identifies the SAP S/4HANA Cloud Public Edition system on software version 1905 or higher. The SAP S/4HANA Cloud Private Edition system acts as a hub system when it is connected to multiple connected systems.Accessible via the SAP Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Connected System | Any ERP system from release ERP6.0 and EHP6 above with add-on HUBERPI is considered as the connected system.Any SAP S/4HANA Cloud Private Edition 1709 and higher, with add-on HUBS4IC is considered as connected system.Any SAP S/4HANA Cloud Public Edition 1908 and higher is considered as connected system. |
| Ariba Sourcing | Accessible via Ariba Sourcing. Your system administrator provides you with the URL and logon data to access Ariba Sourcing. |
| SAP Business Network | Accessible via SAP Business Network. Your system administrator provides you with the URL and logon data to access SAP Business Network. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| PurchaserPurchaser | SAP_BR_PURCHASER | Operational Purchasing | SAP_BR_PURCHASER |  |
| Purchaser - Central Procurement | SAP_BR_CENTRAL_PURCHASER | Central Procurement | SAP_BR_CENTRAL_PURCHASER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Central Company Code | 1010 | Company Code 1010 |  |
| Central Purchase Organization | 1010 | Purch. Org. 1010 |  |
| Central Purchase group | 001 | Group 001 |  |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data Script | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS – MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1129475738a40a781f5cd0f13b15244f)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2XT – Central Purchasing | To run through this test script, a central purchase requisition must be created according to scope item 2XT - Central Purchasing. The prerequisites of 2XT must be fulfilled, and the following steps of test procedure must be completed before the test procedure of this test script is started:Create Purchase RequisitionImport Purchase RequisitionsProcess Purchase Requisitions Centrally |
| 22Z – Procurement of Services | To create purchase requisition with lean service, please follow this step in 22Z - Procurement of Services.Standard Procurement of Service > Option A: Create Purchase Requisition > Case 1: Purchase Service without Material NumberThen complete the following test procedures in 2XT - Central PurchasingImport Purchase RequisitionsProcess Purchase Requisitions Centrally |
| 2ME – Central Purchase Contracts | To run through this test script, the prerequisites of 2ME must be fulfilled. |
| 3ZF – Central Sourcing | To run through this test script, the prerequisites of 3ZF must be fulfilled. |

## Overview Table

This scope itemCentral Sourcing with SAP Ariba Sourcing consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other apps not included on the homepage using the search bar.If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose Settings > App Finder . |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Central Request for Quotation](#unique_9) [page ] 9 | Purchaser - Central Procurement | Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290) |  |
| [Manage Central Request for Quotations](#unique_10) [page ] 11 | Purchaser - Central Procurement | Manage Central RFQs (F3974) |  |
| [Create Sourcing project (as a buyer in Ariba Sourcing)](#unique_11) [page ] 17 | Buyer in Ariba Sourcing |  |  |
| [Participate in Sourcing Event (as a Supplier in Ariba Sourcing)](#unique_12) [page ] 19 | Buyer in Ariba Sourcing |  |  |
| [Accept Supplier's bidding (as a Buyer in Ariba Sourcing)](#unique_13) [page ] 21 | Buyer in Ariba Sourcing |  |  |
| [Send Quote Message (as a Buyer in Ariba Sourcing)](#unique_14) [page ] 22 | Buyer in Ariba Sourcing |  |  |
| [Display Automatically Created Central Supplier Quotation from Award](#unique_15) [page ] 23 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) |  |
| [Scenario 1: Create Purchase Contract](#unique_16) [page ] 25 | Purchaser - Central Procurement | Manage Central Supplier Quotations (F3975) |  |
| [Display Central Purchase Contracts](#unique_17) [page ] 26 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Check Local Contract - In Connected System](#unique_18) [page ] 27 | Purchaser - Central Procurement |  |  |
| [Scenario 2: Create Purchase Order](#unique_19) [page ] 27 | Purchaser - Central Procurement | ECC |  |
| [Display Purchase Order - In Connected System](#unique_20) [page ] 28 | Purchaser - Central Procurement | Manage Central Purchase Contracts (F3144) |  |
| [Post Goods Receipt - In Connected System](#unique_21) [page ] 28 | Warehouse Clerk | ECC |  |
| [Create Supply Invoice - In Connected System](#unique_22) [page ] 29 | Accounts Payable Accountant | ECC |  |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create Central Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Purchase Requisitions from different connected systems get replicated(extracted) to the S/4HANA (Procurement hub) system and will be available for sourcing in the Manage Purchase Requisitions Centrally app. You are unable to find a source of supply for the PR items, but you can select multiple requisition items and create Central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Process Purchase Requisitions Centrally - Formerly Manage Purchase Requisitions Centrally (F3290). | The Manage Purchase Requisitions Centrally screen is displayed. |  |
| 3 | Start Central RFQ creation | Apply the searching cirteria and choose Go.Select the checkbox of multiple Purchase Requisition Items and choose Create Document ,Choose Create Central RFQ to create a new central purchase RFQ. | The Central Request for Quotation screen is displayed. |  |
| 4 | Enter Central RFQ data | On the Central RFQ screen, navigate to the General Information section and make the following entries:RFQ Type(default value): Ext. Souring RFQRFQ Description : enter the descriptionLanguage Key : for example, ENQuotation Deadline : <today + 1 month>Central Purchasing Group : 001Central Purchasing Organization : 1010Central Company Code : 1010Follow-On Doc. Type : for example, MKNote The Follow-on Doc. Type defined here will determine the available option in Central Supplier Quotation as mentioned in section Create Follow-on Documents. For example:The Follow-on Doc. Type defined here will determine the available option in Central Supplier Quotation as mentioned in section Create Follow-on Documents. For example:For Quantity Contract (MK) or Value Contract (WK), the option is Create Central Contract in Central Supplier Quotation.For Purchase Order (PO), the option is Create Purchase Order in Central Supplier Quotation.If leave this field with blank, both of the options are available in Central Supplier Quotation.Purchasing group and RFQ Description is mandatory for external sourcing to Ariba sourcing.Validity Per. Start (does not exist for follow-on doc. type PO): <today>Validity Period End (does not exist for follow-on doc. type PO): <today + 2 months>In the Delivery and Payment Terms section, make the following entries:Target Value : for example, 200 EURCurrency : EURIn the Items section, the selected purchase requisition items are listed.For service item, update below custom fields when it is necessary: Start of Performance Period and End of Performance Period.Ensure the data is correct.In the Notes section(choose language):Detailed Description: enter the descriptionInternal Notes: enter the notesIn the Attachments section, choose upload or add a link to add attachments.Choose Create . |  |  |

### Manage Central Request for Quotations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can maintain the additional details like Bidders, Payment Terms and Incoterms for Central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Central RFQs (F3974) | The Manage Central RFQs screen is displayed. |  |
| 3 | Search Central RFQ | On the Manage Central RFQs screen, enter search criteria to search your Central RFQ.Then choose Your Central RFQ. | Your Central RFQ is displayed. |  |
| 4 | Edit the Central RFQ data | You can change the content. For example, change the Quotation Deadline, or modify RFQ Description.Choose Save .Choose Publish . |  |  |

### Sourcing with SAP Ariba Guided Sourcing UI

In this section, you will act as strategic buyer and participates in sourcing with SAP Ariba Guided sourcing UI, If your system is not enabled with Guided sourcing UI, please go to Sourcing with SAP Ariba Classic Sourcing UI.

#### Create Sourcing Project (as a Buyer in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The buyer creates a sourcing project in Ariba Sourcing. The sourcing project has specific terms for the sourcing in order to invite suppliers to offer their bids on the Central Sourcing Request (RFQ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer on Ariba Sourcing. | The Home screen opens.Your system administrator provides you with logon data for Ariba Sourcing. |  |
| 2 | Open Sourcing Request | Choose the Sourcing tab.Under the Sourcing tab choose Search . In the Project Type filed choose Sourcing Request from the dropdown menu. In the Search Filter enter the Sourcing Request ID and choose Search bottom.Select the relevant Sourcing Request from the result list and choose Open from the dropdown menu.Eventually ignore the Desktop File Sync warning message.Choose the Tasks tab.Select Prepare Sourcing Request > View Task Details .Choose Mark complete .Select Approval for Sourcing Request > View Task Details .Make the following entry:Fixed Date : todayChoose Submit . | Describe any results that may be relevant for subsequent steps in this procedure or other process steps. Leave empty if you are just repeating information. |  |
| 3 | Create Sourcing Project | Choose the Documents tab.Select Sourcing Project > Open .Make the following entries:Name : xxxProject Type: Choose Single Event checkboxEvent Type : RFPTest Project : YesIn the Select a template area choose Request for Proposal For Guided sourcing-IES template.Choose Create . | The sourcing project is created |  |
| 4 | Update Event Duration | In the Event Duration area, click Edit:Event Starts : Please click on the check box Start after Click Publish.If there is no checkbox please select today's date.Event ends: select DurationDuration : 30 minutesChoose Save . |  |  |
| 5 | Invite Suppliers | In the Suppliers area, select the available supplier. If there is no supplier choose Invite Suppliers button.On the Invite Suppliers screen, input your supplier, for example, 17300086 and choose Search .Note If you don't have this supplier, use others.Select the suppliers from the Search Result list.Choose Invite.Select the suppliers. |  |  |
| 6 | Items that need quotes | Select the item for quotes |  |  |
| 7 | Questions, Requirements,a nd attachments | Select your questions, requirements, and attachments |  |  |
| 8 | Publish Sourcing Project | Review the Sourcing Overview.Choose PublishChoose Monitor |  |  |

#### Participate in Sourcing Event (as a Supplier in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The suppliers are bidding on previously created sourcing event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer. | The Home screen opens. |  |
| 2 | Access App | Choose Sourcing tab.In the My Documents area, open the previously created sourcing project. |  |  |
| 3 | Check Sourcing state | Check that the Sourcing event is in Event duration .You can reduce the timing left. Choose Edit and select Duration. Specify duration and choose Update. |  |  |
| 4 | Log on as a Supplier | In the Items that need quotes tab.Select the vertically aligned dots of the suppliers (on the right of supplier name)Press Surrogate BidIf the Surrogate Bid is missing, depending on system setup, carry out the following steps:From the Home screen of Ariba Sourcing, under Manage , choose Administration .Under User-Manager , choose Users. Type: External Supplier or Customer User Choose List all .Under Actions on the right-hand side of the user you are looking for, choose Act as. | In the next steps you are acting as a supplier. |  |
| 5 | Confirm prerequisites | Select the previously created sourcing event with status Open from events list.In the Event Details area, choose Review and Accept Prerequisites.Choose I accept the terms of this agreement.Choose OK .Submit agreement by confirming with OK. |  |  |
| 6 | Select Lots | Mark the available for bidding lots.Choose Confirm Selected Lots . |  |  |
| 7 | Submit Response | Make the following entries:Price: for example, 1Discount Amount : for example, 0Discount Percentage : for example, 0Surcharge Amount : example 0Surcharge Percentage : example 0%Choose Submit Entire Response.Confirm to submit this response with OK . | You can make the necessary entries only after the timer (on the top right) has reached 0. |  |
| 8 | Stop acting as Supplier | Choose Stop on the right top corner of the screen. |  |  |

#### Accept Supplier's bidding (as a Buyer in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After the invitees have sent their bids the buyer can accept one or more of the respondents as his chosen supplier. The following procedure describes the required steps in order to nominate one supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer | The Home screen opens. |  |
| 2 | Review supplier responses | Choose the Sourcing tab.In the My Documents area, open the previously created Sourcing Project.On the Items that need quotes tab, review the bids for the corresponding suppliers. |  |  |
| 3 | Check Sourcing state | Check that the sourcing event is in state Review reponses on the top left of the screen.If the status is Open you can reduce the timing left.Choose Edit in event duration section and select Duration.Specify duration and choose Update. |  |  |
| 4 | Award supplier | Choose the Award Scenario tab.In the Award scenarios section, Choose Scenario Make > Create Award Scenario .Enter your Scenario name and choose Start a new scenario, then choose Done.In the allocate awards section, choose the supplier to award and enter 100% in field Allocate by Percentage.Check the Scenario summary in award scenariosChoose AwardChoose Stay on this event review your sourcing project.On Confirm Award screen, select Mark this supplier's item with 'Awarded' status checkbox. If you want to create follow-on documents, select Yes.Choose Confirm.On success message screen, choose Go to Dashboard. |  |  |

### Sourcing with SAP Ariba Classic Sourcing UI

In this section, you will act as strategic buyer and participates in sourcing with SAP Ariba Classic sourcing UI, If Guided sourcing UI is enabled in your system, please go to [Sourcing with SAP Ariba Guided Sourcing UI](#unique_24) [page ] 11.

#### Create Sourcing project (as a buyer in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The buyer creates a sourcing project in Ariba Sourcing. The sourcing project has specific terms for the sourcing in order to invite suppliers to offer their bids on the Central Sourcing Request (RFQ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer on Ariba Sourcing. | The Home screen opens.Note Your system administrator provides you with logon data for Ariba Sourcing. |  |
| 2 | Open Sourcing Request | Choose the Sourcing tab.Under the Sourcing tab choose Search . In the Project Type filed choose Sourcing Request from the dropdown menu. In the Search Filter enter the Sourcing Request ID and choose Search bottom.Select the relevant Sourcing Request from the result list and choose Open from the dropdown menu.Eventually ignore the Desktop File Sync warning message.Choose the Tasks tab.Select Prepare Sourcing Request > View Task Details .Choose Mark complete .Select Approval for Sourcing Request > View Task Details .Make the following entry:Fixed Date : todayChoose Submit . | Describe any results that may be relevant for subsequent steps in this procedure or other process steps. Leave empty if you are just repeating information. |  |
| 3 | Create Sourcing Project | Choose the Documents tab.Select Sourcing Project > Open .Make the following entries:Name : xxxProject : Quick ProjectEvent Type : RFPTest Project : YesIn the Select a template area choose Request for Proposal template.Choose Create . | The sourcing project is created |  |
| 4 | Define Timing Rules | In the Timing Rules area, make the following entries:Response start date : Please click on the check box When I Click the Publish button on the Summary page.If there is no checkbox please select today's date.Due date: selectDuration : 30 minutesChoose Next . |  |  |
| 5 | Define Team Members | Choose Next without any changes. |  |  |
| 6 | Define participants | In the Invited Participants area, select the available supplier and choose Next . If there is no supplier choose Invite Participants button.On the Participant Search screen search for the desired supplier, for example, 17300086 and choose Search .Select the suppliers from the Search Result list.Choose OK .Choose Next . |  |  |
| 7 | Define Content | Choose Next without any changes. |  |  |
| 8 | Publish Sourcing Project | Review the Sourcing Overview.Choose PublishChoose Monitor |  |  |

#### Participate in Sourcing Event (as a Supplier in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The suppliers are bidding on the previously created sourcing event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer. | The Home screen opens. |  |
| 2 | Access App | Choose the Sourcing tab.In the My Documents area, open the previously created sourcing project. |  |  |
| 3 | Check Sourcing state | Check that the Sourcing event is in state Time remaining (top right).Note If the status is Time remaining until publish, you can reduce the timing left. Choose Actions and select Reduce Timing . Specify reduction and choose OK . |  |  |
| 4 | Log on as a Supplier | Choose the Suppliers tab.Select a supplier from the Invited Participants list.Choose Surrogate Bid .If the Surrogate Bid is missing, depending on system setup, carry out the following steps:From the Home screen of Ariba Sourcing, under Manage , choose Administration .Under User-Manager , choose Users. Type: External Supplier or Customer User Choose List all .Under Actions on the right-hand side of the user you are looking for, choose Act as . | In the next steps you are acting as a supplier. |  |
| 5 | Confirm prerequisites | Select the previously created Sourcing Event from the list.In the Event Details area, choose Review and Accept Prerequisites.Choose I accept the terms of this agreement.Choose OK .Submit agreement by confirming with OK. |  |  |
| 6 | Select Lots | Mark the available for bidding lots.Choose Confirm Selected Lots . |  |  |
| 7 | Submit Response | Make the following entries:Price: for example, 1Discount Amount : for example, 0Discount Percentage : for example, 0Surcharge Amount : example 0Surcharge Percentage : example 0%Choose Submit Entire Response.Confirm to submit this response with OK . | Note You can make the necessary entries only after the timer (on the top right) has reached 0. |  |
| 8 | Stop acting as Supplier | Choose Stop on the right top corner of the screen. |  |  |

#### Accept Supplier's bidding (as a Buyer in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After the invitees have sent their bids the buyer can accept one or more of the respondents as his chosen supplier. The following procedure describes the required steps in order to nominate one supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer | The Home screen opens. |  |
| 2 | Review supplier responses | Choose the Sourcing tab.In the My Documents area, open the previously created Sourcing Project.On the Content tab, review bids for corresponding suppliers. |  |  |
| 3 | Check Sourcing state | Check that the sourcing event is in state Pending Selection on the top right of the screen.Note If the status is Time Remaining you can reduce the timing left.Choose Actions and select Reduce Timing.Choose Actions and select Reduce Timing .Specify reduction and choose OK . |  |  |
| 4 | Award supplier | Choose the Scenario tab.Choose Create Manual Scenario .The result of the Sourcing event can be an automatically created Purchase Order or a Contract in SAP S/4HANA system. Make the following entries depending on your requirements:Name : example: Scenario xxxDocument Type : Purchase OrderDocument Category: NB Standard Purchase OrderSelect a supplier for each of the items listed in the All Content area.Choose Submit for awardDeselect Send Emails to Awarded Participants .Choose Done . |  |  |

#### Send Quote Message (as a Buyer in Ariba Sourcing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

After a supplier was nominated the buyer sends the Quote message to the SAP S/4HANA in order to create a new Purchase Order from the Sourcing Event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the Ariba Sourcing as a Strategic Buyer | The Home screen opens. |  |
| 2 | Send Quote | Choose the Sourcing tab.In the My Documents area, open the previously created Sourcing Project.Select Action > Send Quotes to External System.Confirm send dialog with OK . |  |  |

### Display Automatically Created Central Supplier Quotation from Award

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA Cloud Public Edition system and display the central supplier quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Central Supplier Quotations | Choose Manage Central Supplier Quotations (F3975). | The Manage Central Supplier Quotations screen is displayed. |  |
| 3 | Search for Central Supplier Quotation | Make the following entries and choose Go :RFQ xxx | You search for the automatic created Supplier Quotation |  |

### Display Follow-on Document

#### Display Logs for Follow-On Docs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA Cloud Public Edition system and display the processing logs for follow-on docs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Purchaser - Central Procurement. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Choose Monitor Follow-On Document's Logs - Central Sourcing (F5300). | The Application Logs screen is displayed. |  |
| 3 | Search for Follow-on Document Creation Logs | Make the following entries and choose Go :From: TodayTo: TodayCategory: MMPUR_CQTN | You search for the application logs of follow-on documents generation. |  |
| 4 | Check the Application Log | Choose the application logs of central supplier quotation and click on the arrow on the right. | The log details of follow-on documents generation is displayed. |  |

#### Display Follow-On Documents in Business Process Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to the SAP S/4HANA Cloud Public Edition system and display the busines process flow of Central RFQ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Central RFQs (F3974) | The Manage Central RFQs screen is displayed. |  |
| 3 | Search Central RFQ | On the Manage Central RFQs screen, enter search criteria to search your central RFQ.Then choose Your Central RFQ. | Your Central RFQ is displayed. |  |
| 4 | Check the Follow-on Document | On the Manage Central RFQs screen, choose the tab Process Flow.Check your follow-on Documents. | The business process flow chart is Displayed. |  |

### Create Follow-on Document

#### Scenario 1: Create Purchase Contract

Context

Purchase Contract will be created through background job automatically.

##### Display Central Purchase Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the distribution status and local contract in central purchase contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser - Central Procurement. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Choose Manage Central Purchase Contracts (F3144) . | The Manage Central Purchase Contracts screen is displayed. |  |
| 3 | Search central contract | On the Manage Central Purchase Contracts screen, enter search criteria to search your central purchase contract.Then choose your central purchase contract. | Your central contract is displayed. |  |
| 4 | Check distribution status and local contract number | On the Central Purchase Contracts screen, navigate to the Items section and choose the item entry.On the Central Purchase Contract Item screen, navigate to the Distributed Outline Agreements section.You can check the local contract/schedule agreement number in column Outline Agreements .If Distribution Status is Error in Distribution , you can choose Information in the column of Error Information to check detail error information. After error is fixed in connected system, you can select the line and choose Reinitiate Distribution to distribute central purchase contract again. |  |  |

##### Check Local Contract - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can check the contract which is a copy of the central contract in connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Access the respective connected system Purchaser - Central Procurement. |  |  |
| 2 | Check Local Outline Agreements | Check the local contract distributed from central contract with transaction ME33K.If Info Record Update Code is assigned in contract distribution, you can check the updated info record by choosing Environment > Info Record in local contract/scheduling agreement.The account assignment category U(Unknown) for free text and (Blank) for material are currently supported as account assignment category for central contract item. |  |  |

#### Scenario 2: Create Purchase Order

Context

Purchase Order will be created automatically through background jobs.

##### Display Purchase Order - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a successful background job run, you can check the purchase order in the connected system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system as a Purchaser. |  |  |
| 2 | Display Purchase Order | Check the purchase order with transaction ME23N. |  |  |

##### Post Goods Receipt - In Connected System

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto ECC | Access the respective connected system as a Warehouse Clerk. |  |  |
| 2 | Display Purchase Order | Post goods receipt with Transaction MIGO. | Goods Receipt is posted in connected system. |  |

##### Create Supply Invoice - In Connected System

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
| 1 | Log onto ECC | Access the respective connected system as an Accounts Payable Accountant. |  |  |
| 2 | Create Invoice Verification | Create supplier invoice with Transaction Code MIRO.Choose Invoice . | Invoice is created in the connected system. |  |

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
> Flagged while digesting this document, not verified: System Access row describes the hub as an SAP S/4HANA Cloud Public Edition system (1905 or higher) but the next sentence says an SAP S/4HANA Cloud Private Edition system acts as a hub when connected to multiple connected systems; the hub edition is stated inconsistently.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-sourcing-with-sap-ariba-sourcing-4bl-ae-sap-s-4hana-cloud]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4QN_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 43,908 chars in the whole document
