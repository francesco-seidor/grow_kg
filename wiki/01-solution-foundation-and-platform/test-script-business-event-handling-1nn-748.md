---
id: 01-solution-foundation-and-platform/test-script-business-event-handling-1nn-748
title: "Test Script: Business Event Handling (1NN) (1NN_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1NN: testing business event integration with Event Mesh and Advanced Event Mesh."
cluster: 01-solution-foundation-and-platform
tags: [kb/solution-foundation-and-platform, topic/business-events-and-event-mesh]
aliases: [1NN_S4CLD2608_BPD_EN_XX]
keywords: [Business Event Handling with Event Mesh, business event handling, event mesh integration, advanced event mesh, event monitor, sales order change, business partner change, event queues, test scripts, side-by-side extensions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NN_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-748
topic: 01-solution-foundation-and-platform/business-events-and-event-mesh
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Business Event Handling (1NN) (1NN_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NN_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Business Event Handling with Event Mesh** in Solution Foundation and Platform. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Business Event Handling (1NN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232859147)

[2 Prerequisites 3](#_Toc232859148)

[2.1 System Access 3](#_Toc232859149)

[2.2 Additional Manual Configuration 3](#_Toc232859150)

[3 Overview Table 4](#_Toc232859151)

[4 Test Procedures 5](#_Toc232859152)

[4.1 Test the Integration with Event Mesh In Integration Suite 5](#_Toc232859153)

[4.1.1 Change Sales Order 5](#_Toc232859154)

[4.1.2 Enterprise Event Enablement - Event Monitor 6](#_Toc232859155)

[4.1.3 Monitoring Event Mesh Usage 7](#_Toc232859156)

[4.2 Test the Integration with SAP Integration Suite, Advanced Event Mesh 8](#_Toc232859157)

[4.2.1 Change Business Partner 8](#_Toc232859158)

[4.2.2 Enterprise Event Enablement - Event Monitor 9](#_Toc232859159)

[4.2.3 Check Message Queue 11](#_Toc232859160)

## Purpose

Events provide a system-wide standardized event mechanism for business objects across SAP S/4HANA Cloud Public Edition applications. Business event handling can enable applications, partners and customers to consume events related to SAP S/4HANA Cloud Public Edition business objects. Based on the publish-subscribe pattern, a central event handling component can receive events from multiple senders which can be consumed by receivers, who have previously subscribed to the events centrally.

Side-by-side extensions provide a powerful way of extending SAP S/4HANA Cloud Public Edition applications on SAP Business Technology Platform (SAP BTP) for customers and partners without impacting the digital core, by building decoupled extension applications running side-by-side with SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note The test script covers the test procedures for:Integration between SAP S/4HANA Cloud Public Edition and Event Mesh In Integration SuiteIntegration between SAP S/4HANA Cloud Public Edition and SAP Integration Suite, advanced event mesh, event add-on for ERPValues in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Before you can test this scope item, you must have completed the activation of scope item 1NN, and finished the additional configuration steps that are described in the Set-Up Instructions for this scope item. For more information, see

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| SAP Integration Suite | Accessible via SAP Integration Suite application. Your system administrator provides you with the URL to access the app assigned to your role. |
| SAP Integration Suite, advanced event mesh | Accessible via SAP Integration Suite, advanced event mesh application. Your system administrator provides you with the URL to access the app assigned to your role. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

## Overview Table

This scope item consists of several process steps provided in the tables below.

Test the Integration with Event Mesh In Integration Suite

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Change Sales Order | Internal Sales Representative | Manage Sales Orders – Version 2 (F3893) | Sales order changes are saved. |
| Check status of Outbound Events in SAP Fiori Launchpad | Administrator | Enterprise Event Enablement - Event Monitor (F6983) | The user is able to view the outbound event message that was sent successfully. |
| Check status of Event Queues in SAP BTP | EventMeshDeveloper | Monitoring Event Mesh Usage | The user is able to view the messages received in the queue successfully. |

Test the Integration with SAP Integration Suite, advanced event mesh

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Change Business Partner | Master Data Specialist - Business Partner Data | Manage Business Partner (BP) | Business Partner changes are saved. |
| Check status of Outbound Events in SAP Fiori Launchpad | Administrator | Enterprise Event Enablement - Event Monitor (F6983) | The user is able to view the outbound event message that was sent successfully. |
| Check status of Event Queues in SAP BTP | EventMeshDeveloper | Monitoring Event Mesh Usage | The user is able to view the messages received in the queue successfully. |

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder.You can find all other apps not included on the homepage using the search bar. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Test the Integration with Event Mesh In Integration Suite

#### Change Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Fiori app Manage Sales Orders - Version 2 on your SAP Fiori launchpad to change a sales order.

In this test step, changes to the sales order are saved in the system, and an underlying event is triggered.

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with role Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Sales Order – Version 2 app. | The Manage Sales Order – Version 2 app opens. |  |
| 3 | Display Sales Orders | Choose Go. | All sales orders are displayed. |  |
| 4 | Choose Sales Order | Choose your sales order.For example, < 140111 > | The selected sales order is displayed. |  |
| 5 | Switch to Edit | Choose Edit. | The sales order changes to edit mode. |  |
| 6 | Change Sales Order | Make some changes for your sales order.For example, change the value for Billing Date. | The sales order has been changed. |  |
| 7 | Save Sales Order | Choose Save. | The change for the sales order has been saved. |  |

#### Enterprise Event Enablement - Event Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Fiori app Enterprise Event Enablement - Event Monitor on your SAP Fiori launchpad to monitor the traffic and state of channels configured between SAP S/4HANA Cloud Public Edition and the SAP BTP Event Mesh service for the exchange of business events. The monitor displays inbound and outbound events grouped by topic and status.

In this test step, you test the outbound events of the app:

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with role Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Enterprise Event Enablement - Event Monitor app. | The Enterprise Event Enablement - Event Monitor app opens. |  |
| 3 | Display Channels | Choose Go. | Allavailable channels are displayed. |  |
| 4 | Choose Channel | Choose your channel.For example, < EMIS_0092 > | The Channel page opens. |  |
| 5 | Choose Outbound Event Topic | Choose your Topic under Outbound Event.For example,<em/client/s4h/ce/sap/s4/beh/salesorder/v1/SalesOrder/Changed/v1> | The Outbound Events are displaying. |  |
| 6 | Choose Outbound Event | Choose Details of the Outbound Event. | The outbound event details page opens. |  |
| 7 | Download Payload | Navigate to Payload tab and download payload json file. | The payload json file has been downloaded. |  |
| 8 | Open Payload | Open the downloaded payload json file. | The payload json file opens. |  |
| 9 | Check Payload | Check the payload file for the changed sales order information:For example, <"SalesOrder":"140111">, | The event for changing of sales order was sent from S/4HANA Public Cloud successfully. |  |

#### Monitoring Event Mesh Usage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Integration Suite app Monitoring Event Mesh Usage on your SAP BTP to monitor the traffic and state of channels configured between SAP ABAP Platform and the SAP BTP Event Mesh service for exchange of business events. The monitor displays inbound and outbound events grouped by topic and status.

In this test step, the following features of the app are to be tested:

Outbound Events

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On SAP BTP | Log on to SAP BTP. |  |  |
| 2 | Access the Application | Open the SAP Integration Suite application. | The SAP Integration Suite application opens. |  |
| 3 | Access Event Mesh Monitor | Choose Event Mesh under Monitor. | The Monitoring Event Mesh Usage page opens. |  |
| 4 | Display Event Queues | Choose Queues tab. | A list of all the Event Queues is displayed. |  |
| 5 | Choose Event Queue | Choose Event Queue.For example, <em/client/s4h /SalesOrder> | A list of all the Event Messages is displayed. |  |
| 6 | Choose Event Message | Choose Event Message. | A detail of event message is displayed. |  |
| 7 | Navigate to Payload | Navigate to Payload tab. | The Payload file is displayed. |  |
| 8 | Check Payload | Check the payload file for the changed sales order information.For example, <"SalesOrder":"140111">. | The event for changing of sales order received successfully. |  |

### Test the Integration with SAP Integration Suite, Advanced Event Mesh

#### Change Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Fiori app Manage Business Partner on your SAP Fiori launchpad to change business partner data.

In this test step, the changes to the Business Partner are saved in the system, and the underlying event is triggered.

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with role Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Maintain Business Partner app. | The Maintain Business Partner app opens. |  |
| 3 | Display Business Partners | Choose Start. | Allbusiness partners are displayed. |  |
| 4 | Choose Business Partner | Choose your business partner.For example, < 1001011 > | The selected business partner is displayed. |  |
| 5 | Switch to Change | Choose Switch Between Display and Change. | The business partner changes to edit mode. |  |
| 6 | Change Business Partner | Make some changes for your business partner.For example, change the value for Street/House Number. | The business partner has been changed. |  |
| 7 | Save Business Partner | Choose Save. | The change for the business partner has been saved. |  |

#### Enterprise Event Enablement - Event Monitor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Fiori app Enterprise Event Enablement - Event Monitor on your SAP Fiori launchpad to monitor the traffic and state of channels configured between SAP S/4HANA Cloud Public Edition and the SAP BTP Event Mesh service for the exchange of business events. The monitor displays inbound and outbound events grouped by topic and status.

In this test step, the following features of the app are to be tested:

Outbound Events

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with role Administrator. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Enterprise Event Enablement - Event Monitor app. | The Enterprise Event Enablement - Event Monitor app opens. |  |
| 3 | Display Channels | Choose Go. | Allavailable channels are displayed. |  |
| 4 | Choose Channel | Choose your channel.For example, <AEM_Broker> | The Channel page opens. |  |
| 5 | Choose Outbound Event Topic | Choose your Topic under Outbound Event.For example,<1NN/AEM/S4H/ce/ sap/s4/beh/businesspartner/v1/BusinessPartner/Changed/v1> | The Outbound Events are displaying. |  |
| 6 | Choose Outbound Event | Choose Details of the Outbound Event. | The outbound event details page opens. |  |
| 7 | Download Payload | Navigate to Payload tab and download payload json file. | The payload json file has been downloaded. |  |
| 8 | Open Payload | Open the downloaded payload json file. | The payload json file opens. |  |
| 9 | Check Payload | Check the payload file for the changed business partner information:For example, <" Business Partner ":"1001011">, | The event for changing of business partner was sent from S/4HANA Public Cloud successfully. |  |

#### Check Message Queue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use the SAP Integration Suite, advanced event mesh app Message Queue on your SAP BTP to monitor the traffic and state of channels configured between SAP ABAP Platform and the SAP BTP Event Mesh service for exchange of business events. The monitor displays inbound and outbound events grouped by topic and status.

In this test step, the following features of the app are to be tested:

Outbound Events

Procedure

| Test Step # | Test Step | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On SAP BTP | Log on to the SAP BTP. |  |  |
| 2 | Access the Application | Open the SAPIntegration Suite, advanced event mesh application. | The SAP Integration Suite, advanced event mesh application opens. |  |
| 3 | Access the Service | Choose your service.For example, <AEMService> | The Service Details pageopens. |  |
| 4 | Access the Manage Tab | Choose Manage tab | The Manage tab opens. |  |
| 5 | Display Event Queues | Choose Queues in the Broker Manager Quick Links menu | A list of all the Event Queues is displayed. |  |
| 6 | Verify Messages Queued | Verify the columns Messages Queued (msgs) and Messages Queued (MB). | The Messages Queued (msgs)column shows1message (or more if you published multiple messages), and that a non-zero value is shown in theMessages Queued (MB)column. |  |
| 7 | Choose Event Queue | Choose your Event Queue.For example, <1NN_AEM_QUEUE> | The Summary page of the Event Queue is displayed. |  |
| 8 | Access the Messages Queued | Choose Messages Queued tab | The Messages Queued tabopens. |  |
| 9 | Check Event Message | Verify the list of Event Message. | A detail of event message is displayed. |  |

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
- see-also :: [[01-solution-foundation-and-platform/edi-extensibility-customer-guide-229]]
- see-also :: [[16-two-tier-erp-and-central-finance/two-tier-erp-pricing-master-integration-using-cloud-integration-237]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NN_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 19,749 chars in the whole document
