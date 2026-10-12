---
id: 10-procurement/test-script-sourcing-with-sap-ariba-sourcing-4bl-ae-sap-s-4hana-cloud
title: "Test Script: Sourcing with SAP Ariba Sourcing (4BL_AE) - SAP S/4HANA Cloud Public Edition (4BL_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 4BL_AE: RFQ in S/4HANA Cloud, Ariba sourcing project, event and award (Guided/Classic UI), then supplier quotation, PO, contract."
cluster: 10-procurement
tags: [kb/procurement, topic/ariba-sourcing]
aliases: [4BL_S4CLD2608_BPD_EN_AE]
keywords: [Sourcing with SAP Ariba Sourcing, ariba sourcing, test scripts, request for quotation, guided sourcing ui, classic sourcing ui, sourcing projects, sourcing events, supplier award, supplier quotations]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4BL_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1019
topic: 10-procurement/ariba-sourcing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sourcing with SAP Ariba Sourcing (4BL_AE) - SAP S/4HANA Cloud Public Edition (4BL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4BL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sourcing with SAP Ariba Sourcing** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sourcing with SAP Ariba Sourcing (4BL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854535)

[2 Prerequisites 4](#_Toc232854536)

[2.1 Additional Manual Configuration 4](#_Toc232854537)

[2.2 System Access 4](#_Toc232854538)

[2.3 Roles 4](#_Toc232854539)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232854540)

[3 Overview Table 7](#_Toc232854541)

[4 Test Procedures 8](#_Toc232854542)

[4.1 Create Request for Quotation 8](#_Toc232854543)

[4.2 Sourcing with SAP Ariba Guided Sourcing UI 9](#_Toc232854544)

[4.2.1 Create Sourcing Project 10](#_Toc232854545)

[4.2.2 Participate in Sourcing Event 11](#_Toc232854546)

[4.2.3 Accept Supplier's Bidding 13](#_Toc232854547)

[4.3 Sourcing with SAP Ariba Classic Sourcing UI 14](#_Toc232854548)

[4.3.1 Create Sourcing Project 14](#_Toc232854549)

[4.3.2 Participate in Sourcing Event 17](#_Toc232854550)

[4.3.3 Accept Supplier's Bidding 18](#_Toc232854551)

[4.3.4 Send Quote Message 20](#_Toc232854552)

[4.4 Display Automatically Created Supplier Quotation from Award 20](#_Toc232854553)

[4.5 Display Automatically Created Purchase Order 21](#_Toc232854554)

[4.6 Display Automatically Created Purchase Contract (Optional) 22](#_Toc232854555)

## Purpose

Overview

Connect your SAP S/4HANA digital core for sourcing and procurement to SAP Business Network and SAP Ariba Sourcing. This connection provides access to intuitive RFX tools for requests for information, proposals, and reverse auctions. You can connect with over two million companies, discover suppliers quickly and easily, and automate and adjust negotiation procedures.

Ensure event success by using the SAP Ariba Sourcing support desk and event-day management assistance. Evaluate the total cost impact of your sourcing decisions. Reduce the time and effort spent on administrative tasks. Handy wizards and tools help you launch events, collaborate, and negotiate. Choose from a variety of suppliers based on their profile information, ratings, and assessments. This helps you to develop a large supply base and backup sources, reducing supplier risks. Once you subscribe to SAP Ariba Sourcing, you can simply activate this scope item with guided configuration.

This scope item uses SAP Integration Suite, managed gateway for spend management and SAP Business Network for the integration. It covers the full functional scope of the Sourcing with SAP Ariba Sourcing (1A0) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/726fb21aa768b5b0e2ad8ebebc763817)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible through SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Ariba Sourcing | Accessible via Ariba Sourcing. Your system administrator provides you with the URL and logon data to access the Ariba Sourcing. |

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

Use your own master data to go through the test procedure:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor | 33300086 | 33300086 | We assume that the supplier in Ariba Sourcing uses the same name as in S/4HANA. |
| Material | TG0011 | Trading Good 0011,PD,Regular Proc.no Serial no.; no batch |  |

For more information on creating master data objects, refer to the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Request for Quotation](#unique_8) [page ] 8 | Purchaser | Manage RFQs (F2049) | A request for quotation (RFQ) is created from an existing purchase requisition and send to SAP Ariba Sourcing. |
| [Create Sourcing Project](#unique_9) [page ] 10 | Strategic Buyer in SAP Ariba Guided Sourcing UI |  | The sourcing project is published. |
| [Participate in Sourcing Event](#unique_10) [page ] 11 | Strategic Buyer & Supplier in SAP Ariba Guided Sourcing UI |  | Suppliers entered their bids on the created sourcing event. |
| [Accept Supplier's Bidding](#unique_11) [page ] 13 | Strategic Buyer in SAP Ariba Guided Sourcing UI |  | The buyer accepts one or more supplier biddings. |
| [Create Sourcing Project](#unique_12) [page ] 14 | Strategic Buyer in SAP Ariba Classic Sourcing UI |  | The sourcing project is published. |
| [Participate in Sourcing Event](#unique_13) [page ] 17 | Strategic Buyer & Supplier in SAP Ariba Classic Sourcing UI |  | Suppliers entered their bids on the created sourcing event. |
| [Accept Supplier's Bidding](#unique_14) [page ] 18 | Strategic Buyer in SAP Ariba Classic Sourcing UI |  | The buyer accepts one or more supplier biddings. |
| [Send Quote Message](#unique_15) [page ] 20 | Strategic Buyer in SAP Ariba Classic Sourcing UI |  | The quote messages are sent to the SAP S/4HANA Cloud Public Edition system. |
| [Display Automatically Created Supplier Quotation from Award](#unique_16) [page ] 20 | Purchaser | Manage RFQs (F2049) | The automatically created supplier quotation is displayed in the SAP S/4HANA Cloud Public Edition system. |
| [Display Automatically Created Purchase Order](#unique_17) [page ] 21 | Purchaser | Manage RFQs (F2049) | The automatically created purchase order is displayed in the SAP S/4HANA Cloud Public Edition system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Request for Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a request for quotation (RFQ) from an existing purchase requisition and send it to SAP Ariba Sourcing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to your SAP S/4HANA Cloud Public Edition as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed. |  |
| 3 | Access New Request for Quotation | On the Manage RFQs screen, choose Create and select Ext. Sourcing Req. from the dropdown list. | The New Request for Quotation screen is displayed. |  |
| 4 | Create New Request for Quotation | On the New Request for Quotation screen, enter the required data.On the General Information tab, enter the following data according to your business requirements:ExampleRFQ Description: <Short description or the title of the RFQ>Note This field is mandatory.Language Key: To select a language key use the Value Help ().Quotation Deadline: todayPurchasing Group: 001Purch. Organization: 3310Company Code: 3310Follow-On Document Type: NB Standard PO or MK Quantity ContractOn the Delivery and Payment Terms tab, enter the following data according to your business requirements:Currency: AEDOn the Items tab, choose Create, and select the newly created RFQ Item. In the Request for Quotation Item screen, enter the following data according to your business requirements:Material: TG0011Material Group: L001Plant: 3310Requested Quantity: 20 EADelivery date: today + 1 monthInfo Record Update: Select the checkbox.Choose Apply. You return to the New Request for Quotation screen.On the Bidders tab, choose Create, and add one or more bidders, for example, Supplier: 33300086Choose Create. | The new request for quotation is created. |  |
| 5 | Publish Request for Quotation | On the Request for Quotation screen, choose Publish. | The workflow for automatic approval of the request for quotation is triggered. After approval, the request for quotation is published. |  |

### Sourcing with SAP Ariba Guided Sourcing UI

In this section, you will act as strategic buyer and participate in sourcing with SAP Ariba Guided Sourcing UI.

|  |
| --- |
| Note If the SAP Ariba Guided Sourcing UI is not (yet) enabled in your system, go to the section [Sourcing with SAP Ariba Classic Sourcing UI](#unique_20) [page ] 14. |

#### Create Sourcing Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a sourcing project in SAP Ariba Guided Sourcing UI as a strategic buyer. The sourcing project has specific terms for the sourcing in order to invite suppliers to offer their bids on the sourcing request (RFQ).

Prerequisites

Your system administrator provided you with logon data for SAP Ariba Sourcing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Ariba Sourcing as a Strategic Buyer. |  |  |
| 2 | Open Sourcing Request | To open a sourcing request, do the following substeps:Select the Sourcing tab.In the search bar, select Sourcing Request from the dropdown list and enter the Sourcing Request ID in the search field. Choose Search.From the search result list, select the relevant sourcing request. Choose Open.Note Ignore the Desktop File Sync warning message.On the <Sourcing Request ID> screen, select the Tasks tab.Choose Prepare Sourcing Request > View Task Details .Note The Prepare Sourcing Request task is an optional step. If you don't see the task listed on the Task tab, continue with step 7 (Approval for Sourcing Request task).On the To Do Task screen, choose Mark Complete.The <Sourcing Request ID> screen is displayed.On the <Sourcing Request ID> screen, choose Approval for Sourcing Request > View Task Details .The Approval Task screen is displayed.In the Fixed Date field, enter <today>.Choose Submit.On the <Sourcing Request ID> screen, check whether the sourcing request is in status Approval.If the sourcing request is in status Approval, choose Approval for Sourcing Request > Force Complete Task > OK . |  |  |
| 3 | Publish Sourcing Project | On the <Sourcing Request ID> screen, select the Documents tab.Choose Sourcing Project > Open .On the Create Guided Sourcing Project screen, enter the following data according to your business requirements:Name: <Name of Sourcing Project>Project: Select the Single Event checkbox.Event Type: RFPTest Project: Select the Yes checkbox.In the Template section, select the Request for Proposal (Guided Sourcing) template.Choose Create. |  |  |
| 4 | Review Sourcing Overview | Choose Publish. On the Success Message screen, choose Monitor Event. | The sourcing project is published. |  |

#### Participate in Sourcing Event

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to participate in a sourcing event and bid on the previously created sourcing event as a supplier in SAP Ariba Guided Sourcing UI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Ariba Sourcing as a Strategic Buyer. | The Home screen is displayed. |  |
| 2 | Open Sourcing Event | Choose the Sourcing tab.In the My Documents area, open the previously created sourcing project. |  |  |
| 3 | Check Sourcing Event State | In the Monitor Event section, check that the sourcing event is open. (In the Event Duration section, the timer has not reached 0.) |  |  |
| 4 | Act as a Supplier in SAP Ariba Sourcing | Choose the Items that Need Quotes tab. Choose More (  ).Choose Surrogate Bid.If the Surrogate Bid is missing, do the following steps depending on system setup:From the Home screen of SAP Ariba Sourcing, choose Manage > Administration .In the Supplier and Customer Manager section, choose Users > List all .To act as a specific supplier user, go to the row of that supplier and choose Actions > Act as .Note In the following steps you are acting as a supplier. |  |  |
| 5 | Confirm Prerequisites | Select the previously created sourcing event that is in status Open from the Events list.In the Event Details area, choose Review and Accept Prerequisites.Select the I accept the terms of this agreement checkbox.Choose OK twice. |  |  |
| 6 | Select Lots | Mark the available for bidding lots.Choose Confirm Selected Lots. |  |  |
| 7 | Submit Response | Enter the following data according to your business requirements:Note You can make the necessary entries only during the timer is running.ExamplePrice: 1Discount Amount: 0Discount Percentage: 0Surcharge Amount: 0Surcharge Percentage: 0%Choose Submit Entire Response > OK . |  |  |
| 8 | Stop Acting as Supplier | To stop acting as a supplier, choose Stop. | Suppliers entered their bids on the created sourcing event. |  |

#### Accept Supplier's Bidding

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the invitees have sent their bids, the buyer can accept one or more of the respondents as the chosen supplier. This procedure describes how to nominate one supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Ariba Sourcing as a Strategic Buyer. | The Home screen is displayed. |  |
| 2 | Stop Sourcing Event | Choose the Sourcing tab.In the My Documents section, open the previously created sourcing project.In the Monitor Event section, go to the Event Duration section and choose Edit > Stop Event . |  |  |
| 3 | Review Supplier Responses | On the Award Scenarios tab, review the bids of the corresponding suppliers. |  |  |
| 4 | Award Supplier | Choose Scenario Maker > Create Award Scenario .On the Create a Scenario screen, enter a scenario name in the Name field. Choose Start a new scenario > Done .Select the corresponding supplier and enter 100% in the Allocate by Percentage field.Choose Award.On the Confirm Award screen, select Yes, if you want to create follow-on documents.If you want to create follow-on documents, select Yes.Choose Confirm. On the success message screen, choose Go to Dashboard. | The buyer accepts one or more supplier biddings. |  |

### Sourcing with SAP Ariba Classic Sourcing UI

In this section, you will act as strategic buyer and participate in sourcing with SAP Ariba Classic Sourcing UI.

|  |
| --- |
| Note If the SAP Ariba Classic Sourcing UI is not (yet) enabled in your system, go to the section [Sourcing with SAP Ariba Guided Sourcing UI](#unique_19) [page ] 9. |

#### Create Sourcing Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create a sourcing project in SAP Ariba Classic Sourcing UI as a strategic buyer. The sourcing project has specific terms for the sourcing in order to invite suppliers to offer their bids on the sourcing request (RFQ).

|  |
| --- |
| Note If you use a sourcing template other than the default template described in the 4BL set-up instructions document, the test steps may be different. |

Prerequisites

Your system administrator provided you with logon data for SAP Ariba Sourcing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Ariba Sourcing as a Strategic Buyer. |  |  |
| 2 | Open Sourcing Request | To open a sourcing request, do the following substeps:Select the Sourcing tab.In the search bar, select Sourcing Request from the dropdown list and enter the Sourcing Request ID in the search field. Choose Search.From the search result list, select the relevant sourcing request. Choose Open.Note Ignore the Desktop File Sync warning message.On the <Sourcing Request ID> screen, select the Tasks tab.Choose Prepare Sourcing Request > View Task Details .Note The Prepare Sourcing Request task is an optional step. If you don't see the task listed on the Task tab, continue with step 7 (Approval for Sourcing Request task).On the To Do Task screen, choose Mark Complete.The <Sourcing Request ID> screen is displayed.On the <Sourcing Request ID> screen, choose Approval for Sourcing Request > View Task Details .The Approval Task screen is displayed.In the Fixed Date field, enter <today>.Choose Submit.On the <Sourcing Request ID> screen, check whether the sourcing request is in status Approval.If the sourcing request is in status Approval, choose Approval for Sourcing Request > Force Complete Task > OK . |  |  |
| 3 | Create Sourcing Project | On the <Sourcing Request ID> screen, select the Documents tab.Choose Sourcing Project > Open .On the Create Sourcing Project screen, enter the following data according to your business requirements:Name: <Name of Sourcing Project>Project: Select the Quick Project checkbox.Event Type: RFPTest Project: Select the Yes checkbox.In the Template section, select the Request for Proposal template.Choose Create. |  |  |
| 4 | Define Timing Rules | In the Timing Rules section, enter the following data according to your business requirements:Response start date: Select the When I Click the Publish button on the Summary page checkbox.If there's no checkbox, select today's date.Due date: <today>Duration: 30 minutesChoose Next. |  |  |
| 5 | Define Team Members | Don't enter any data.Choose Next. |  |  |
| 6 | Define Participants | In the Invited Participants section, select the available supplier and choose Next.If there's no supplier, choose Invite Participants.On the Participant Search screen, search for the desired supplier, for example, 33300086. Choose Search.From the search result list, select the suppliers.Choose OK > Next . |  |  |
| 7 | Define Content | Select the Item checkbox.Choose Edit > Content .In the Bidding Rules section, enter the following data according to your business requirements:Bid decrement (%): 1 (for example)Choose Done > Next . |  |  |
| 8 | Publish Sourcing Project | Review the sourcing overview.Choose Publish > Monitor . |  |  |

#### Participate in Sourcing Event

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to participate in a sourcing event and bid on the previously created sourcing event as a supplier in SAP Ariba Classic Sourcing UI.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon as Strategic Buyer in SAP Ariba Sourcing to check the Sourcing Event | Log on to SAP Ariba Sourcing as a Strategic Buyer. | The Home screen is displayed. |  |
| 2 | Open Sourcing Event | Choose the Sourcing tab.In the My Documents area, open the previously created sourcing project. |  |  |
| 3 | Check Sourcing State | Check that the Sourcing event is in state Time remaining in open bidding.Note If the status is Time remaining until publish, you can reduce the timing left. Choose Actions and select Reduce Timing. Specify the time reduction and choose OK. |  |  |
| 4 | Act as a Supplier in SAP Ariba Sourcing | Choose the Suppliers tab.Select the supplier and choose Surrogate Bid.If the Surrogate Bid is missing, do the following steps depending on system setup:From the Home screen of SAP Ariba Sourcing, choose Manage > Administration .In the Supplier and Customer Manager section, choose Users > List all .To act as a specific supplier user, go to the row of that supplier and choose Actions > Act as .Note In the following steps you are acting as a supplier. |  |  |
| 5 | Confirm Prerequisites | Select the previously created sourcing event that is in status Open from the Events list.In the Event Details area, choose Review and Accept Prerequisites.Select the I accept the terms of this agreement checkbox.Choose OK twice. |  |  |
| 6 | Select Lots | Mark the available for bidding lots.Choose Confirm Selected Lots. |  |  |
| 7 | Submit Response | Enter the following data according to your business requirements:Note You can make the necessary entries only during the timer is running.ExamplePrice: 1Discount Amount: 0Discount Percentage: 0Surcharge Amount: 0Surcharge Percentage: 0%Choose Submit Entire Response > OK . |  |  |
| 8 | Stop Acting as Supplier | To stop acting as a supplier, choose Stop. | Suppliers entered their bids on the created sourcing event. |  |

#### Accept Supplier's Bidding

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the invitees have sent their bids, the buyer can accept one or more of the respondents as the chosen supplier. This procedure describes how to nominate one supplier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Ariba Sourcing as a Strategic Buyer. | The Home screen is displayed. |  |
| 2 | Review Supplier Responses | Select the Sourcing tab.In the My Documents section, open the previously created sourcing project.On the Content tab, review the bids for the corresponding suppliers. |  |  |
| 3 | Check Sourcing State | Check that the sourcing event is in state Pending Selection.Note If the status is Time Remaining you can reduce the timing left.Choose Actions > Reduce Timing.Specify the time reduction and choose OK. |  |  |
| 4 | Award Supplier | Select the Scenario tab.Choose Create Manual Scenario.The result of the Sourcing event can be an automatically created purchase order or a contract in the SAP S/4HANA Cloud Public Edition system.Enter the following data according to your business requirements:ExampleName: <Scenario Name>Document Type: Purchase OrderDocument Category: NB Standard Purchase OrderSelect a supplier for each of the items listed in the All Content section.Choose Submit for award.Deselect the Send Emails to Awarded Participants checkbox.Choose Done. | The buyer accepts one or more supplier biddings. |  |

#### Send Quote Message

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how after a supplier was nominated the buyer sends the quote message to the SAP S/4HANA Cloud Public Edition system in order to create a new purchase order from the sourcing event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access the Ariba Sourcing as a Strategic Buyer | The Home screen is displayed. |  |
| 2 | Send Quote | Select the Sourcing tab.In the My Documents section, open the previously created sourcing project.Choose Action > Send Quotes to External System.Confirm the send dialog box with OK. |  |  |

### Display Automatically Created Supplier Quotation from Award

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created supplier quotation in the SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Supplier Quotations | Open the Manage Supplier Quotations (F1991) app. | The Manage Supplier Quotations screen is displayed. |  |
| 3 | Search for Supplier Quotation | In theRFQ field, enter a Supplier Quotation ID and choose Go. | A search result list is displayed. |  |
| 4 | Display Automatically Created Supplier Quotation | From the search result list, select a supplier quotation.On the Supplier Quotation <Supplier Quotation ID> screen, select the Items tab. | In the Supplier Quotation Item column, the number of the supplier quotation is displayed. |  |

### Display Automatically Created Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created purchase order in the SAP S/4HANA Cloud Public Edition system.

|  |
| --- |
| Note This step can only be executed if you’ve selected the purchase order as a follow-on document type in [Create Request for Quotation](#unique_8) [page ] 8. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to your SAP S/4HANA Cloud Public Edition system as a Purchaser | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed with a list of existing request for quotations items. |  |
| 3 | Search for RFQ | To search for a specific RFQ, enter the required search criteria and choose Go. | A search result table is displayed. |  |
| 4 | Open RFQ | To open an RFQ, select the corresponding row in the search result list. | The <RFQ ID> screen is displayed. |  |
| 5 | Display Purchase Order | On the <RFQ ID> screen, go to the Process Flow tab. | The automatically created purchase order ID is displayed. |  |

### Display Automatically Created Purchase Contract (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display the automatically created piurchase contract in SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note This step is optional and can only be executed if you’ve selected the contract as a follow-on document type in [Create Request for Quotation](#unique_8) [page ] 8. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access Apps | Open the Manage RFQs (F2049) app. | The Manage RFQs screen is displayed. |  |
| 3 | Search for Request for Quotation | Enter the required search criteria to search for a specific request for quotation.Choose Go. | The previously created request for quotation is displayed in the search results list. |  |
| 4 | Display Automatically Created Purchase Contract | Go to the Quotation tab.Choose Purchase Contract xxx > Manage Purchase Contract. | The automatically created purchase contract is displayed. |  |

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
> Flagged while digesting this document, not verified: Overview Table lists Manage RFQs (F2049) as the app for displaying the automatically created supplier quotation, but the test procedure for that step uses Manage Supplier Quotations (F1991).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/central-procurement-with-sap-ariba-sourcing-4qn-test-script-sap-s-4han]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4BL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 36,099 chars in the whole document
